#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting AI App Boilerplate in Development Mode${NC}"

# Check if .env exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}Warning: .env file not found. Creating from example...${NC}"
    cp .env.example .env
    echo -e "${YELLOW}Please update .env with your configuration${NC}"
fi

# Load environment variables
export $(grep -v '^#' .env | xargs)
export ENVIRONMENT=development

# Start PostgreSQL with pgvector if not running
if ! docker compose ps postgres | grep -q "Up"; then
    echo -e "${GREEN}Starting PostgreSQL with pgvector...${NC}"
    docker compose up -d postgres
    
    # Wait for PostgreSQL to be ready
    echo -e "${YELLOW}Waiting for PostgreSQL to be ready...${NC}"
    sleep 5
fi

# Initialize database if needed
echo -e "${GREEN}Setting up database...${NC}"
python -m alembic upgrade head

# Check if frontend dependencies are installed
if [ ! -d "../frontend/node_modules" ]; then
    echo -e "${YELLOW}Installing frontend dependencies...${NC}"
    cd ../frontend
    npm install
    cd ../backend
fi

# Start frontend in development mode (in background)
echo -e "${GREEN}Starting React development server...${NC}"
cd ../frontend
npm run dev &
FRONTEND_PID=$!
cd ../backend

# Wait for frontend dev server to start
sleep 3

# Start FastAPI with hot reload
echo -e "${GREEN}Starting FastAPI backend...${NC}"
python -m uvicorn main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --reload \
    --reload-dir ./src \
    --log-level info

# Cleanup on exit
trap "kill $FRONTEND_PID 2>/dev/null; exit" INT TERM

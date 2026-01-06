build-prod:
	@echo "Building production image..."
	docker build -t ai-app-boilerplate:latest .

run-prod:
	@echo "Starting production container..."
	docker run -p 8000:8000 --env-file .env ai-app-boilerplate:latest

dev:
	@echo "Starting development environment..."
	cd backend && chmod +x start.sh && ./start.sh

docker-dev:
	@echo "Starting development with Docker Compose..."
	docker-compose up --build

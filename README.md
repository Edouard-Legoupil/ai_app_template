# AI App Boilerplate

> experimental - not completed yet... 


This repo provides a unified full-stack production-ready open source and cloud-agnostic AI application starter with FastAPI backend, React frontend, agent orchestration (CrewAI/LLM/VectorDB-ready) and Dockerized deployment. All of this fully complies with the [United Nations Open Source Principle](https://unite.un.org/en/news/osi-first-endorse-united-nations-open-source-principles).

It includes an **opinionated approach to AI process automation**, with features like transparency, privacy, analytics, protocol compliance, and extensibility.

The goal is to offer a production-ready base to kick start real-world, secure, collaborative AI applications, allowing for easy extension and customization with AI vibe coding. Rather than starting from scratch, you can use this boilerplate as a starting point for your own AI application.


## AI is Not Just Automation - It's Amplification

### What is the added value of AI process automation?

__Without AI__:

 * People make decisions based on what they remember

 * Documents get lost or misunderstood

 * Teams work hard but sometimes at cross-purposes

 * Lessons from past mistakes get forgotten

__With AI__:

 * Everyone has perfect memory of all past decisions

 * Documents "tell" their own stories about why they exist

 * The team sees how their work connects

 * The business learns from everything that happens


AI process automation isn't about making robots do human work. It's about enabling:  

 * Perfect memory of all decisions and why they were made

 * Clear vision of how everything connects

 * Shared understanding across the whole team

 * Continuous learning from everything that happens

This approach allow to create automated systems that help the team make better decisions, faster, with full awareness of context and consequences  -  turning process automation from a cost-saving tool into a competitive advantage that makes the entire organization smarter.

## Core Design Challenge: Humans Think, Systems Execute

Think of Your Automated Process as a Living Ecosystem:

 * Decision Points = Where human judgment enters

 * Documents = The memory and context of those decisions

 * Path Tracking = The map of possibilities created/destroyed

 * Action Updates = How reality changes after execution

### 1. People Are Decision Makers (Not Just Button-Pushers)

You can't automate decision-making - you can only automate the presentation of decision points. Every automated process must be designed around where, when, and how human judgment gets inserted.

**Design Principle**: "Don't replace the judge - build a better courtroom" - *BAD DESIGN*: System automatically approves/rejects based on rules alone - *GOOD DESIGN*: System gathers all relevant information, presents clear options, highlights risks, and asks human: "Which path should we take?"

 * Identify every decision point in your process

 * Determine: What information does a human need to make this decision?

 * Design: How will the system present this information clearly?

 * Build: Decision "gates" where humans provide direction

 * Document: Record WHY each decision was made (not just what)



## # 2. Documents Tell Stories (Not Just Store Information)

Documents are not data to be processed - they are context containers. Automated systems must understand why a document exists, not just what it contains.

**Design Principle**: "Treat every document like a witness on the stand" - *BAD DESIGN*: Extract data fields, file the rest - *GOOD DESIGN*: Capture the story: Who created this? Why? What problem were they solving? 

 * What alternatives were considered?

 * For every document type, capture metadata about its creation context

 * Build relationships: This document → That decision → Those people

 * Create "document chains" showing evolution of thinking

 * Preserve rejected/alternative versions (they tell important stories)

 * Enable search by "document story" not just keywords            

### 3. Decisions Create Ripples (Not Just Tick Boxes)

Every automated process must track alternative paths that weren't taken. The system needs to understand what possibilities were created and destroyed with each choice.

**Design Principle**: "Map the forest of possibilities, not just the path taken" - *BAD DESIGN*: Record only what was chosen - *GOOD DESIGN*: Record what was considered, why alternatives were rejected, and track downstream consequences of the choice

 * Design decision logs that capture: Options considered, Pros/cons of each

 * Build "what-if" tracking: When we choose A over B, what changes?

 * Create alerts for downstream impacts: "Choosing vendor X affects timelines Y and Z"

 * Design for reversibility: Can we undo this decision? What would that take?

 * Monitor for "decision debt": Choices that limit future options            

### 4. Actions Make It Real (Not Just "Done" Checkmarks)

Actions change reality - and therefore change what's possible next. Automated systems must update the landscape of possibilities after each action.

**Design Principle**: "After every action, rebuild the map of what's possible" - *BAD DESIGN*: Mark task complete, move to next item - *GOOD DESIGN*: After action completes, ask: What changed? What new opportunities opened? What constraints were created? Update all downstream possibilities.

 * After every significant action: Reassess what's now possible/impossible

 * Design "reality checks": Did the action achieve what we expected?

 * Build feedback loops: Actions → Results → Adjust future actions

 * Create "action chains": Show how early actions enable/disable later ones

 * Monitor for "action side effects": Unintended consequences

## Organizational Advantages of an AI App Boilerplate

For any organization looking to implement AI-driven process automation, this boilerplate offers a substantial strategic head start. 

By providing a unified, production-ready foundation, it **eliminates the consequential upfront investment of time and resources** typically required to architect a secure, scalable, and ethically-grounded AI application from scratch. The core advantage lies in its opinionated design for intelligence amplification, which is baked into the technical architecture. 

Instead of treating AI as a simple automation tool, this framework enforces the **principles of transparent decision-making, contextual document memory, and path-tracking** from the very first line of code. This means organizations can immediately focus on modeling their unique business logic and decision points, rather than solving fundamental challenges around AI orchestration, data privacy, or audit trails. 

The boilerplate transforms AI implementation from a risky, open-ended software development project into a **controlled customization effort**. It allows teams to rapidly prototype and deploy systems that act as a "living ecosystem" for organizational intelligence, directly operationalizing the shift from cost-saving automation to creating a continuously learning, context-aware competitive advantage. 

By starting here, an organization doesn't just build an app; it instantiates a governance model and an architectural pattern designed to make the entire organization smarter, faster, and more aligned.

## Mainstreamed User Interaction for Organizational AI

A key barrier to AI adoption is the cognitive leap required from end-users, who are often non-technical professionals. 

This boilerplate addresses this by championing narrative-driven interfaces and decision-journey mapping as its core, mainstreamable interaction patterns. 

Rather than presenting users with raw data or complex AI parameters, or a chat interface, the interface is designed around the fundamental patterns described above:

 * The **Decision Dashboard**: This universal pattern replaces traditional task lists. For every process, users are presented with a clear visual "courtroom" of their pending decisions. Each card bundles the AI-curated context: the document story, a map of the potential paths (with pros/cons), the historical precedent, and a simple, guided choice mechanism. This transforms interaction from executing a task to presiding over a decision point.

 * The **Story Thread**: Every document, action, and agent output is presented not as isolated data but as a node in a continuous, navigable narrative. Users can follow a "story thread" to see the full evolution of a project—why a document was created, what decisions it informed, what alternatives were discarded, and what actions resulted. This pattern leverages natural human comprehension of stories, making complex process histories intuitively understandable.

 * The **Ripple Forecast Panel**: When a user contemplates a decision, the interface dynamically visualizes the "ripples"—the downstream possibilities created or constrained. This "what-if" panel, generated from the system's path-tracking logic, makes the abstract concept of consequential thinking tangible. It’s a mainstreamed pattern for proactive risk and opportunity assessment.

 * The **Collective Context Bar**: A persistent UI element that answers the fundamental human questions in collaboration: "What does my team know that I don't?" and "What's the shared goal right now?". It aggregates and displays real-time signals from the AI's "perfect memory"—recent team decisions, updated document contexts, and shifts in the landscape of possibilities—creating a shared situational awareness.

By embedding these interaction patterns, the boilerplate ensures the AI system's sophisticated backend capabilities are accessed through intuitive, human-centric metaphors. 

This mainstreams AI interaction, reducing training overhead and resistance, and ensuring the technology truly amplifies human judgment rather than complicating it. Teams don't learn a new tool; they engage with a familiar paradigm of stories, decisions, and consequences, supercharged by organizational memory.

## Quick Start

You can review a brainstroming around a list of potential UN processes where this approach could be applied in the `potential_process.md` file.

This boilerplate implements as an example a use case around AI Innovation Adoption & Scaling: 

 * **Decision Points**: Pilot selection, evaluation criteria, scaling readiness assessment

 * **Documents**: Innovation proposals, business process automation proposals, functional requirements documents ready for vibe coding

 * **Path Tracking**: How innovation adoption affects traditional program implementation

 * **Action Updates**: Balancing innovation with proven approaches in high-risk contexts


We suggest to first run this example to get a feel for the boilerplate and then adapt it to your own needs (see below). 

The example presented in this app precisely aims at helping to you to refine your own use case for AI automation. You will be able to use the output together with this present boilerplate to fast track your own AI automation app development. 

## Architecture

- **Development:** Separate servers with Vite proxy
- **Production:** Single FastAPI server serves API & React build
- **Database:** PostgreSQL + pgvector
- **Agent Engine:** CrewAI/LLM extensible

## Success Criteria

- `./start.sh` spins up dev environment and DB
- Single Dockerfile for backend + frontend
- React served from FastAPI in prod
- Hot-reload in dev
- AI/ML orchestration maintained
- Documentation included

### Development Mode

```bash
# Clone and setup
git clone https://github.com/Edouard-Legoupil/ai_app_template
cd ai-app-template
cp .env.example .env  # Update with your values

## create a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
alembic upgrade head

# Start development servers
make dev  # or cd backend && ./start.sh
```

### Production Deployment

```bash
# Build and run
docker build -t ai-app:latest .
docker run -p 8000:8000 --env-file .env ai-app:latest
# Visit http://localhost:8000
```

### Docker Compose (All-in-one)

```bash
docker-compose up --build
```


## Development/Production Details

- **start.sh**: Unified dev script (DB, migrations, frontend/backend hot reload)
- **Dockerfile**: Multistage, single image for cloud deployment
- **docker-compose.yml**: DB & backend orchestration, healthcheck
- **Vite**: Build to backend/static, dev API/ws proxy
- **Makefile**: Dev/prod/build convenience commands
- **Config/Env**: All variables managed via `.env` files

---

## Adapt it to your own needs

The output from the demo app presented in this boilerplate will help you to refine your own use case for AI automation. 

It will provide you with detailled functional description that you will be then able to use to adapt this boilerplate to your own needs. 

For customisation, you may use a cli tool like [opencode](https://opencode.ai/) or [gemini-cli](https://geminicli.com/), [claude-code](https://claude.com/product/claude-code) or [Qwen-code](https://qwenlm.github.io/qwen-code-docs/en/users/overview/) to start vibecoding within the forked and cloned repository.

See `vibe_coding_guide.md` for best practices and coding standards.

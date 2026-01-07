# AI App Boilerplate

> experimental - development not completed yet... 


This repo provides a unified full-stack production-ready open source and cloud-agnostic AI application starter based on a standard teck stack: FastAPI backend, React frontend, agent orchestration (CrewAI/LLM/VectorDB-ready) and Dockerized deployment. All of this fully complies with the [United Nations Open Source Principle](https://unite.un.org/en/news/osi-first-endorse-united-nations-open-source-principles).

It offers an **opinionated approach to AI process automation**, that enforces transparency, analytics, protocol compliance, and extensibility.

The goal is to offer a production-ready base to kick start real-world, secure, collaborative AI applications, allowing for easy extension and customization with AI vibe coding. Rather than starting from scratch, you can use this boilerplate as a starting point to configure your own AI process automation application.


## AI is Not Just Automation - It's Amplification

### What is the added value of AI process automation?

__Without AI__:

 * People make decisions based on what they remember

 * Documents get lost or misunderstood

 * Teams work hard but sometimes at cross-purposes

 * Lessons from past mistakes get forgotten

 * Knowledge exists in silos, never synthesized

__With AI__:

 * Everyone has perfect memory of all past decisions

 * Documents "tell" their own stories about why they exist

 * The team sees how their work connects

 * The business learns from everything that happens

 * Collective intelligence is curated, accessible, and action-ready



AI process automation isn't about making robots do human work. It's about enabling:  

 * Perfect **memory** of all decisions and why they were made

 * Clear **vision** of how everything connects

 * Shared **understanding** across the whole team

 * Continuous **learning** from everything that happens

 * Organized **intelligence** that's pre-synthesized for action

This approach allow to create automated systems that help the team make better decisions, faster, with full awareness of context and consequences  -  turning process automation from a cost-saving tool into a competitive advantage that makes the entire organization smarter.

## Core Design Challenge: Humans Think, Systems Execute

Think of Your Automated Process as a Living Ecosystem:

 * Knowledge Layer = The curated, validated organizational intelligence
 
 * Decision Points = Where human judgment enters

 * Documents = The memory and context of those decisions

 * Path Tracking = The map of possibilities created/destroyed

 * Action Updates = How reality changes after execution


### 1. Knowledge Must Be Curated (Not Just Retrieved) 

You can't build intelligent decisions on chaotic document retrieval - you must build on pre-synthesized organizational intelligence. Every automated process must start from validated knowledge, not raw documents.

**Design Principle**: "Build on bedrock, not quicksand" - *BAD DESIGN*: System retrieves random documents for each decision - *GOOD DESIGN*: System provides pre-curated Knowledge Cards that synthesize organizational intelligence, validated by experts, ready for decision-making.

 * Transform documents into Knowledge Cards through AI synthesis + human validation

 * Design for knowledge evolution: version control, expiration, confidence scoring

 * Create knowledge relationships: cards that support or conflict with each other

 * Ensure knowledge is process-aware: cards know which decisions they apply to

 * Build feedback loops: decision outcomes refine knowledge quality

### 2. People Are Decision Makers (Not Just Button-Pushers)

You can't automate decision-making - you can only automate the presentation of decision points. Every automated process must be designed around where, when, and how human judgment gets inserted.

**Design Principle**: "Don't replace the judge - build a better courtroom" - *BAD DESIGN*: System automatically approves/rejects based on rules alone - *GOOD DESIGN*: System gathers all relevant information, presents clear options, highlights risks, and asks human: "Which path should we take?"

 * Identify every decision point in your process

 * Determine: What information does a human need to make this decision?

 * Design: How will the system present this information clearly?

 * Build: Decision "gates" where humans provide direction

 * Document: Record WHY each decision was made (not just what)

### 3. Documents Tell Stories (Not Just Store Information)

Documents are not data to be processed - they are context containers. Automated systems must understand why a document exists, not just what it contains.

**Design Principle**: "Treat every document like a witness on the stand" - *BAD DESIGN*: Extract data fields, file the rest - *GOOD DESIGN*: Capture the story: Who created this? Why? What problem were they solving? 

 * What alternatives were considered?

 * For every document type, capture metadata about its creation context

 * Build relationships: This document → That decision → Those people

 * Create "document chains" showing evolution of thinking

 * Preserve rejected/alternative versions (they tell important stories)

 * Enable search by "document story" not just keywords            

### 4. Decisions Create Ripples (Not Just Tick Boxes)

Every automated process must track alternative paths that weren't taken. The system needs to understand what possibilities were created and destroyed with each choice.

**Design Principle**: "Map the forest of possibilities, not just the path taken" - *BAD DESIGN*: Record only what was chosen - *GOOD DESIGN*: Record what was considered, why alternatives were rejected, and track downstream consequences of the choice

 * Design decision logs that reference applied Knowledge Cards

 * Build "knowledge-informed what-if" tracking: "If we choose A (supported by Card X), then B becomes impossible (per Card Y)"

 * Create alerts for knowledge-based downstream impacts: "Choosing vendor X violates Security Card #789 unless we get exception"

 * Design for knowledge-aware reversibility: "To undo this decision, we need to address the concerns in Compliance Card #456"

 * Monitor for "knowledge-debt": Decisions that ignore important Knowledge Cards          

### 5. Actions Make It Real (Not Just "Done" Checkmarks)

Actions change reality - and therefore change what's possible next. Automated systems must update the landscape of possibilities after each action.

**Design Principle**: "After every action, rebuild the map of what's possible" - *BAD DESIGN*: Mark task complete, move to next item - *GOOD DESIGN*: After action completes, ask: What changed? What new opportunities opened? What constraints were created? Update all downstream possibilities.

 * After every significant action: Compare outcomes with knowledge-based predictions

 * Design "knowledge validation checks": Did the action confirm or contradict our Knowledge Cards?

 * Build feedback loops: Actions → Results → Update knowledge confidence → Improve future decisions

 * Create "knowledge generation workflows": Unexpected outcomes trigger new Knowledge Card creation

 * Monitor for "knowledge gaps": Situations where no Knowledge Card applied well

## Mainstreamed User Interaction for Organizational AI

A key barrier to AI adoption is the cognitive leap required from end-users, who are often non-technical professionals. 

This boilerplate addresses this by championing knowledge-driven interfaces and decision-journey mapping as its core, mainstreamable interaction patterns. 

Rather than presenting users with raw data or complex AI parameters, or a chat interface, the interface is designed around the fundamental patterns.

The main workspace is a vertical stack of panels, each representing a different aspect of the user's work:

 * Knowledge Dashboard (when curating organizational intelligence)

     ↓
 * Decision arenas structure complex choices(when action needed)

     ↓
 * Document Narrative (when context needed)

     ↓
 * Ripple Forecast (when considering options)

     ↓
 * Reflection Interface (when learning)

In addition, a permanent "context bar", always visible as a sidebar panel, provides situational awareness and teams feedback.

### The Knowledge Dashboard: From Document Chaos to Curated Intelligence

This critical workspace allows knowledge stewards (subject matter experts + AI) to curate the organization's intelligence base. Users can add and monitor documents needing synthesis into Knowledge Cards, review and validate AI-generated knowledge drafts, resolve conflicts between Knowledge Cards, and track knowledge usage and effectiveness. This maintains the organization's "single source of truth" repository

The dashboard transforms passive document storage into active knowledge creation, ensuring every process starts from validated intelligence rather than ad-hoc document retrieval.

### The Decision Dashboard: From Task Lists to Judgment Arenas

This universal pattern replaces traditional task lists. For every process, users are presented with a clear visual "courtroom" of their pending decisions, with pre-loaded relevant Knowledge Cards serving as expert witnesses. Each card bundles the AI-curated context: the document story, a map of the potential paths (with pros/cons), automatic conflict detection between applicable Knowledge Cards, the historical precedent, and a simple, guided choice mechanism. This transforms interaction from executing a task to presiding over a decision point. 

The dashboard doesn't just present choices—it creates a structured space for reasoned judgment, with AI serving as expert witness rather than decision-maker.

### The Story Thread: From Document Management to Narrative Intelligence

Every document, action, and agent output is presented not as isolated data but as a node in a continuous, navigable narrative. 

Users can follow a "templated story thread" to see the full evolution of a project — why a document was created, what validated intelligence informed each decision, what decisions it informed, what alternatives were discarded, and what actions resulted. 

This pattern leverages natural human comprehension of stories, making complex process histories intuitively understandable.

### The Ripple Forecast Panel: From Linear Planning to Consequence Mapping

When a user contemplates a decision, the interface dynamically visualizes the "ripples" — the downstream possibilities created or constrained, predicted by the Knowledge Card system. This "what-if" panel, generated from the system's path-tracking logic, makes the abstract concept of consequential thinking tangible. It shows consequences based on organizational knowledge, not just rules, it    highlights when choices violate important Knowledge Cards, and it suggests alternatives that align better with organizational intelligence. It’s a mainstreamed pattern for proactive risk and opportunity assessment.

Ripple warnings are knowledge-based and made BEFORE approval (not after) which allows to better document the approval rationale.

### The Collective Context Bar: the Collaboration Command Center

The Collective Context Bar serves as a persistent, context-aware panel that facilitates seamless collaboration within the AI-enhanced process management system. It functions as both a notification hub and an action gateway, continuously aggregating and prioritizing signals from across the organization. Its core capability is to surface relevant collaboration opportunities—such as pending decisions requiring input, document reviews, or invitations to contribute—based on the user's role, expertise, and current work context. The component intelligently filters and presents these items with clear priority indicators and estimated time commitments.

Key functionality includes the ability to trigger focused, modal-based interactions directly from the sidebar, allowing users to quickly comment, vote, or review without navigating away from their primary task. The system supports shared situational awareness and allows for 3 types of flexible collaboration:

    💬 Quick comment for simple input - Passive: Users see in Context Bar and engage voluntarily

    🎯 Structured input for important decisions - Active: specifically tag key stakeholders

    🤝 Formal collaboration for deep involvement - Structured: Feedback captured in decision context
    
It maintains awareness of team activities, process updates, and emerging opportunities, presenting them in a consolidated, glanceable view. The bar distinguishes between inbound requests (actions others require from the user) and outbound opportunities (where the user's expertise could benefit others), providing a balanced view of collaborative responsibilities and possibilities.

Behaviorally, the Context Bar operates with minimal disruption, respecting user focus through configurable settings while ensuring time-sensitive items receive appropriate attention. It provides progressive disclosure: summary items in the sidebar expand into detailed modal interfaces for interaction, with options to dive deeper into full process contexts when needed. The component tracks contributions and provides feedback on impact, fostering a culture of visible, valued participation. By centralizing collaborative touchpoints and integrating them contextually into the user's workflow, the Collective Context Bar reduces tool-switching overhead and supports more fluid, informed, and purposeful teamwork across distributed processes.


### The Reflection Interface: Turn experience into actionable intelligence

While current systems capture what happened, they rarely facilitate learning from what happened. A dedicated space for turning experience into into improved organizational intelligence ensures the system learns from every outcome.

Post-action reflection prompts users to evaluate how well Knowledge Cards predicted outcomes, suggest updates to existing Knowledge Cards based on new evidence, identify gaps in the knowledge base that need new cards, and rate the usefulness of each applied Knowledge Card.

Such mandatory reflection at project end allows for AI synthesis across projects and continuous improvement of process templates.

----

By embedding these interaction patterns, the boilerplate ensures the AI system's backend capabilities are accessed through intuitive, human-centric metaphors. 

┌─────────────────────────────────────────────────────────────┐
│ 1. DOCUMENTS → KNOWLEDGE CARDS (Continuous Background)      │
│    • AI synthesizes new documents into knowledge drafts     │
│    • Experts validate/refine into Knowledge Cards           │
│    ↓                                                        │
│ 2. START NEW PROCESS INSTANCE                               │
│    ↓                                                        │
│ 3. SYSTEM PRE-LOADS RELEVANT KNOWLEDGE CARDS                │
│    (Based on process type + initial answers)                │
│    ↓                                                        │
│ 4. COMPLETE KNOWLEDGE-AWARE CUSTOM FORM                     │
│    (Questions reference specific Knowledge Cards)           │
│    ↓                                                        │
│ 5. AI GENERATES INITIAL DOCS USING KNOWLEDGE CARD CONTEXT   │
│    (Pre-validated terminology, compliance points)           │
│    ↓                                                        │
│ 6. NOTIFICATIONS + CONTEXT BAR WITH KNOWLEDGE INJECTION     │
│    └─→ Users engage with knowledge-aware collaboration      │
│    OR                                                       │
│    └─→ Tag reviewers with specific Knowledge Card context   │
│    ↓                                                        │
│ 7. INCORPORATE FEEDBACK & ITERATE                           │
│    (System tracks all changes & knowledge applied)          │
│    ↓                                                        │
│ 8. KNOWLEDGE-INFORMED APPROVAL DECISION                     │
│    └─→ System shows ripple effects BASED ON KNOWLEDGE       │
│    └─→ Highlights conflicts with Knowledge Cards            │
│    ↓                                                        │
│ 9. APPROVE & EXECUTE                                        │
│    (Project moves to implementation)                        │
│    ↓                                                        │
│ 10. POST-ACTION REFLECTION                                  │
│    (Evaluate knowledge effectiveness, suggest updates)      │
│    ↓                                                        │
│ 11. AI SYNTHESIZES ORGANIZATIONAL LEARNING                  │
│    (Improves future instances AND Knowledge Cards)          │
└─────────────────────────────────────────────────────────────┘

This mainstreams AI interaction, reducing training overhead and resistance, and ensuring the technology truly amplifies human judgment rather than complicating it. 

The Process Initiator doesn't start from scratch (AI helps draft from knowledge base), gets intelligent feedback (knowledge-aware notifications), makes informed decisions (knowledge-based ripple warnings), and contributes to collective intelligence (closes the learning loop).

The organization benefits from consistent intelligence (Knowledge Cards ensure uniform understanding), cross-team knowledge sharing (breaks knowledge silos), institutional memory (every decision linked to applied knowledge), and continuous intelligence improvement (learning synthesized across projects into better Knowledge Cards).

Teams don't learn a new tool; they engage with a familiar paradigm of stories, decisions, and consequences, supercharged by curated organizational intelligence.

## Organizational Advantages of an AI App Boilerplate

For any organization looking to implement AI-driven process automation, this boilerplate offers a substantial strategic head start with knowledge intelligence built-in. 

By providing a unified, production-ready foundation with integrated knowledge management, it **eliminates the chaotic document retrieval problem that plagues most AI implementations**. The core advantage lies in its opinionated design for intelligence curation and application, which is baked into the technical architecture.

Instead of treating AI as a simple automation tool, this framework enforces the **principles of knowledge synthesis, validation, and application** from the very first line of code. This means organizations can immediately focus on modeling their unique business logic and decision points n top of a validated knowledge base, rather than solving fundamental challenges around AI orchestration, data privacy, or audit trails. 

The boilerplate transforms AI implementation from a risky, open-ended software development project into a **controlled customization and knowledge engineering effort**. It allows teams to rapidly prototype and deploy systems that act as a "living ecosystem" for organizational intelligence, directly operationalizing the shift from cost-saving automation to creating a continuously learning, knowledge-aware  competitive advantage. It also allow to configure proven patterns, gets AI capabilities automatically and focuses on domain-specific logic. This boilerplate provides the scaffolding for intelligent process systems. The developer adds the specific process logic and domain knowledge. 

By starting here, an organization doesn't just build an app; it instantiates a governance model and an architectural pattern designed to make the entire organization smarter, faster, and more aligned.



## Quick Start

You can review a brainstroming around a list of potential UN processes where this approach could be applied in the `potential_process.md` file.

This boilerplate implements, as an example, a use case around AI Process automation for Innovation Adoption & Scaling: 

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

The Customization Model is based on the 4 Layers below:

**LAYER 4: PROCESS-SPECIFIC**

* Custom forms & questions

* Domain-specific AI prompts

* Domain-specific integrations

* Industry-specific Knowledge Card taxonomies

* Process-specific knowledge validation workflows

**LAYER 3: KNOWLEDGE DOMAIN**
    
* Knowledge Card templates for your domain

* Document-to-knowledge extraction rules

* Expert validation workflows

* Knowledge conflict resolution protocols

* Domain-specific knowledge relationships

**LAYER 2: PROCESS TEMPLATES**

* Decision point types

* Document templates

* Collaboration rules

* Knowledge application rules

* Knowledge-informed ripple mapping

**LAYER 1: CORE BOILERPLATE**

* AI orchestration engine

* Decision tracking system

* UI components & patterns

* Learning feedback loop

* Knowledge curation engine

* Knowledge Card registry

* Context assembly system


The steps to adapt this boilerplate to your own needs are:

  1. Define Your Knowledge Taxonomy (/config/knowledge/taxonomy.yaml)

  2. Configure Document-to-Knowledge Rules (/config/knowledge/extraction_rules.yaml)

  3. Set Up Knowledge Stewardship (/config/knowledge/stewardship.yaml)
  
  4. Create process type definition (/config/process_type.yaml)

  5. Design the initiation form (/config/forms/[type].yaml)

  6. Write domain-specific AI prompts (/config/ai_prompts/[type].py)

  7. Define decision points (/config/decisions/[type].yaml)

  8. Create document templates (/config/documents/[type].jinja2)

  9. Configure ripple effects (/config/ripples/[type].py)

  10. Set up integrations (/config/integrations/[type].yaml)

  11. Define learning questions (/config/learning/[type].yaml)

  12. Customize UI (/config/ui/[type].json)


What You DON'T Need to Do:

❌ Build the Knowledge Curation Engine (already in boilerplate)

❌ Create the Knowledge Card Registry (already built)

❌ Design Knowledge Validation Workflows (already provided)

❌ Implement Knowledge Conflict Detection (already included)

❌ Build Knowledge-Aware UI Components (already there)

❌ Create Context Assembly System (already implemented)

❌ Design Organizational Memory Infrastructure (already architected)

What You DO Need to Do:

✅ Define YOUR knowledge domains and taxonomies

✅ Configure YOUR document-to-knowledge extraction rules

✅ Assign YOUR knowledge stewards and validation workflows

✅ Map YOUR process-specific knowledge requirements

✅ Create YOUR industry's Knowledge Card templates

✅ Set YOUR knowledge confidence thresholds and expiration policies

✅ Define YOUR knowledge application and conflict resolution rules

✅ Connect to YOUR document repositories for knowledge sourcing

✅ Customize YOUR knowledge-aware user interfaces

The boilerplate provides the engine. You provide the domain knowledge.  You're not just configuring another automation tool. You're establishing your organization's intelligence infrastructure. The goal isn't to have perfect knowledge from day one. It's to establish a system that improves organizational intelligence continuously. Every process you automate becomes both a consumer and a producer of validated knowledge, creating a virtuous cycle of organizational learning and improvement.

Define your knowledge domains and assign stewards -> 
 Configure document ingestion and Knowledge Card templates -> 
    Map your first process with knowledge requirements-> 
       Launch your first knowledge-aware automation process -> 
          See patterns in knowledge usage and gaps -> 
             Refine Knowledge Cards based on real application -> 
               Operate with a mature organizational intelligence base

For customisation, you may use a cli tool like [opencode](https://opencode.ai/) or [gemini-cli](https://geminicli.com/), [claude-code](https://claude.com/product/claude-code) or [Qwen-code](https://qwenlm.github.io/qwen-code-docs/en/users/overview/) to start vibecoding within the forked and cloned repository.

See `vibe_coding_guide.md` for best practices and coding standards.

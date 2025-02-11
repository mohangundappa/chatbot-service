# AI Chatbot Service for Customer Support & Sales

## 1. Project Goal 🎯
**Objective:** Build an AI-powered chatbot service to automate customer support and sales interactions while maintaining conversation context across multiple channels.

**Key Focus Areas:**
- Context-aware responses using conversation history
- Scalable thread management for high-volume interactions
- Unified interface for both synchronous (REST) and real-time (WebSocket) communication
- Extensible architecture for business-specific workflows

## 2. Business Overview & Features 💼
### Target Users
- Customer support teams
- Sales representatives
- E-commerce platforms
- Helpdesk systems

### Core Functionalities
✅ **Conversation Threading**  
   - Automatic thread creation per external chat ID  
   - Context preservation across sessions  
✅ **Multi-Protocol Support**  
   - REST API for traditional integrations  
   - WebSocket for real-time streaming  
✅ **State Management**  
   - Persistent conversation history  
   - Contextual response generation  
✅ **Scalable Architecture**  
   - Horizontal scaling support  
   - Rate limiting ready  

## 3. Technology Stack 🛠️
| Component              | Technology                          | Purpose                            |
|------------------------|-------------------------------------|------------------------------------|
| **Backend Framework**  | FastAPI (Python)                    | API & WebSocket endpoints          |
| **AI Orchestration**   | LangChain + LangGraph               | Conversation state management      |
| **LLM Integration**    | Langchain-OpenAI                    | GPT-4 model interactions           |
| **Validation**         | Pydantic                            | Data modeling & validation         |
| **Server**             | Uvicorn + Websockets                | ASGI server implementation         |
| **Config Management**  | Python-Dotenv                       | Environment variable handling      |
| **Packaging**          | Poetry/Pip                          | Dependency management              |

## 4. Implementation Architecture 🏗️
```mermaid
graph TD
    A[Client] -->|REST/WebSocket| B(API Gateway)
    B --> C{External Chat ID}
    C -->|New Chat| D[Create Thread]
    C -->|Existing Chat| E[Retrieve Thread]
    D/E --> F[Conversation Graph]
    F --> G[LLM Processing]
    G --> H[State Storage]
    H --> I[Response Generation]
    I --> B
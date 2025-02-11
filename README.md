
## Overview

The **Chatbot API** is a FastAPI-based service designed to handle external chat ID to thread ID mapping for persistent conversations. It provides RESTful and WebSocket endpoints for managing chatbot interactions.

## Features

- Exposes RESTful and WebSocket APIs for chatbot interactions.
    
- Supports CORS for cross-origin requests.
    
- Includes API documentation via Swagger and ReDoc.
    
- Provides a health check endpoint for monitoring service status.
    
- Uses LangGraph for stateful AI interactions.
    

## Tech Stack

- **FastAPI**: High-performance web framework for building APIs.
    
- **LangGraph**: For stateful chatbot interactions.
    
- **Langchain**: Integrates with LLMs.
    
- **CORS Middleware**: Enables cross-origin resource sharing.
    
- **Pydantic**: Data validation and settings management.
    
- **OpenAI API**: Uses OpenAI's language models.
    

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
    
- pip (Python package manager)
    

### Steps

1. Clone the repository:
    
    ```
    git clone <repository-url>
    cd <repository-directory>
    ```
    
2. Create and activate a virtual environment:
    
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    
3. Install dependencies:
    
    ```
    pip install -r requirements.txt
    ```
    

## Running the Application

Start the FastAPI application:

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

### Health Check

- **Endpoint**: `GET /health`
    
- **Response**:
    
    ```
    {
      "status": "healthy",
      "environment": "<app_env>",
      "model": "<model_name>"
    }
    ```
    

### Chat API

- **Endpoint**: `POST /api/v1/chat`
    
- **Request**:
    
    ```
    {
      "message": "Hello!",
      "external_chat_id": "user123"
    }
    ```
    
- **Response**:
    
    ```
    {
      "response": "Hello! How can I help you?",
      "thread_id": "abc-123",
      "external_chat_id": "user123"
    }
    ```
    

### WebSocket Chat API

- **Endpoint**: `ws://localhost:8000/ws/chat?external_chat_id=user123`
    
- **Usage**:
    
    - Send a message via WebSocket.
        
    - Receive chatbot responses in real-time.
        

### API Documentation

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
    
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
    

## CORS Configuration

The API allows cross-origin requests from all sources (`*`). This can be modified in the `app.add_middleware` section.

## Folder Structure

```
.
├── src/
│   ├── chatbot/
│   │   ├── api/
│   │   │   ├── routes.py
│   │   ├── config.py
│   │   ├── services.py
│   │   ├── graph.py
│   │   ├── models.py
├── main.py  # Entry point
├── requirements.txt
├── README.md
```

## Configuration

The application reads settings from a `.env` file:

```
OPENAI_API_KEY=<your_api_key>
APP_ENV=production
MODEL_NAME=gpt-4o-mini
```

## Setup and Packaging

```
from setuptools import setup, find_packages

setup(
    name="chatbot",
    version="0.1",
    packages=find_packages(),
    package_dir={"": "src"},
)
```

## Contributing

4. Fork the repository.
    
5. Create a feature branch.
    
6. Commit your changes.
    
7. Push to your branch.
    
8. Open a pull request.
    

## License

This project is licensed under the MIT License.
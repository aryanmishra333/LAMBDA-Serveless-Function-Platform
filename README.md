# Lambda Serverless Function

A serverless function platform that allows you to run Python and Node.js code in isolated containers, similar to AWS Lambda.

## Features

- Run Python and Node.js code in isolated Docker containers
- Support for multiple programming languages
- Container isolation for security
- Memory limits and timeout controls
- Simple REST API for function management
- Built-in code execution monitoring

## Prerequisites

- Python 3.10+
- Docker
- Node.js 18+ (for Node.js functions)

## 🛠️ Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/aryanmishra333/PES2UG22CS100_PES2UG22CS103_PES2UG22CS110_PES2UG22CS117_LAMBDA-Serverless_Function.git
```

2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Start the FastAPI Backend
```bash
uvicorn backend.main:app --reload
```

5. Start the Streamlit Frontend
```bash
streamlit run frontend/app.py
```

6. Access the App
- Frontend: http://localhost:8501
- API Docs: http://localhost:8000/docs

## 🧪 Supported Languages
- Python 3
- JavaScript (Node.js)

## API Endpoints

### Function Management

- `POST /functions/` - Upload a new function
- `GET /functions/{function_id}` - Get function details
- `POST /functions/{function_id}/run` - Execute a function
- `DELETE /functions/{function_id}` - Delete a function

## Project Structure

```
lambda-serverless-function/
├── backend/
│   ├── api/           # FastAPI routes and endpoints
│   ├── core/          # Core functionality
│   ├── db/            # Database models and operations
│   ├── schemas/       # Pydantic models
│   ├── tests/         # Test cases
│   └── utils/         # Utility functions
├── docker/            # Docker configuration files
├── frontend/          # Frontend application (if any)
└── requirements.txt   # Python dependencies
```
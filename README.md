<h1 align="center">⚡ Serverless Function Platform (Lambda Clone)</h1>

<p align="center">
  A lightweight serverless computing platform that lets you upload, manage, and run Python and JavaScript functions inside Docker or gVisor sandboxes. Includes monitoring and metrics dashboard.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>Upload and run serverless functions in Python or JavaScript</li>
  <li>Support for Docker and gVisor runtimes</li>
  <li>View function logs, metrics, and performance graphs</li>
  <li>Edit, delete, and manage uploaded functions</li>
  <li>Streamlit-based beautiful UI dashboard</li>
  <li>SQLite backend with FastAPI-powered API</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
.
├── backend
│   ├── api
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core
│   │   ├── docker_executor.py
│   ├── db
│   │   ├── database.py
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── main.py
│   ├── schemas
│   │   ├── function_schema.py
│   │   ├── __init__.py
│   └── utils
│       ├── file_handler.py
│       ├── __init__.py
├── docker
│   ├── base_node.Dockerfile
│   ├── base_python.Dockerfile
│   ├── code.js
│   └── code.py
├── frontend
│   ├── app.py
│   └── utils.py
├── functions
├── functions.db
├── README.md
└── requirements.txt
</pre>

<hr>

<h2>🛠️ Setup Instructions</h2>

<h3>1. Clone the Repository</h3>

<pre><code>git clone https://github.com/KARTIK9990/PES2UG22CS251_PES2UG22CS258_PES2UG22CS275_PES2UG22CS908_Lamda_serverless_function.git
cd lambda-platform
</code></pre>

<h3>2. Create a Virtual Environment</h3>

<pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
</code></pre>

<h3>3. Install Dependencies</h3>

<pre><code>pip install -r requirements.txt
</code></pre>

<h3>4. Start the FastAPI Backend</h3>

<pre><code>uvicorn backend.routes:router --reload --host 0.0.0.0 --port 8000
</code></pre>

<h3>5. Start the Streamlit Frontend</h3>

<pre><code>streamlit run frontend/app.py
</code></pre>

<h3>6. Access the App</h3>

<ul>
  <li>Frontend: <a href="http://localhost:8501" target="_blank">http://localhost:8501</a></li>
  <li>API Docs: <a href="http://localhost:8000/docs" target="_blank">http://localhost:8000/docs</a></li>
</ul>

<hr>

<h2>🧪 Supported Languages</h2>
<ul>
  <li>Python 3</li>
  <li>JavaScript (Node.js)</li>
</ul>

<hr>

<h2>📊 Monitoring & Logs</h2>
<ul>
  <li>View real-time execution metrics (CPU, memory, execution time)</li>
  <li>Charts for CPU and execution trends over time</li>
  <li>Detailed per-function logs</li>
</ul>

<hr>

<h2>📦 API Endpoints</h2>

<pre><code>POST   /functions/                     # Upload a new function
GET    /functions/                    # List all functions
POST   /functions/{id}/run            # Execute a function (use_gvisor: bool)
GET    /functions/{id}/logs           # View function logs
GET    /functions/{id}/metrics        # Get performance metrics
PUT    /functions/{id}                # Update function code
GET    /functions/{id}/code           # Retrieve raw code
DELETE /functions/{id}                # Delete a function
</code></pre>

<hr>

<h2>📌 Notes</h2>
<ul>
  <li>Uses Docker and optionally gVisor (ensure both are installed and configured)</li>
  <li>Execution is sandboxed with timeout and resource control</li>
  <li>SQLite3 is used for persistent storage (no external DB needed)</li>
</ul>

<hr>

<h2>🎯 Future Improvements</h2>
<ul>
  <li>Multi-language support (Go, Ruby, etc.)</li>
  <li>Auto-scaling execution pools</li>
  <li>Integrated billing/cost tracking system</li>
  <li>Authentication and function sharing</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>Developed by <strong>pes2ug22cs258,pes2ug22cs251,pes2ug22cs270,pes2ug22cs908</strong></p>
<p>Feel free to ⭐ the repo and contribute!</p>

<hr>

<h2>📝 License</h2>

<p>This project is licensed under the MIT License.</p>

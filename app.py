from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import socket
import datetime
import os

app = FastAPI(title="GitHub Actions CI/CD Project")

@app.get("/", response_class=HTMLResponse)
def home():
    hostname = socket.gethostname()
    build_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>GitHub Actions CI/CD</title>
    <style>
        body {{
            font-family: "Segoe UI", sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #ffffff;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 1000px;
            margin: 50px auto;
            background: rgba(255,255,255,0.08);
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }}
        h1 {{
            text-align: center;
            color: #00eaff;
        }}
        .card {{
            background: rgba(0,0,0,0.35);
            padding: 20px;
            margin: 20px 0;
            border-left: 5px solid #00eaff;
            border-radius: 10px;
        }}
        .workflow {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }}
        .step {{
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            transition: transform 0.3s;
        }}
        .step:hover {{
            transform: scale(1.05);
        }}
        .step span {{
            font-size: 36px;
            display: block;
            margin-bottom: 10px;
        }}
        footer {{
            text-align: center;
            margin-top: 40px;
            opacity: 0.8;
        }}
    </style>
</head>
<body>
<div class="container">
    <h1>🚀 GitHub Actions CI/CD Pipeline</h1>

    <div class="card">
        <h2>📦 Project Info</h2>
        <p><b>Docker Image:</b> github-actions-project</p>
        <p><b>Running Host:</b> {hostname}</p>
        <p><b>Build Time:</b> {build_time}</p>
        <p><b>Exposed Port:</b> 8009</p>
    </div>

    <div class="card">
        <h2>🔁 CI/CD Workflow</h2>
        <div class="workflow">
            <div class="step">
                <span>🧑‍💻</span>
                <b>Code Push</b>
                <p>Developer pushes code to GitHub</p>
            </div>
            <div class="step">
                <span>⚙️</span>
                <b>GitHub Actions</b>
                <p>Pipeline is triggered automatically</p>
            </div>
            <div class="step">
                <span>🐳</span>
                <b>Docker Build</b>
                <p>Image is built from Dockerfile</p>
            </div>
            <div class="step">
                <span>📤</span>
                <b>Docker Hub</b>
                <p>Image is pushed to Docker Hub</p>
            </div>
            <div class="step">
                <span>📥</span>
                <b>Docker Pull</b>
                <p>Same image is pulled</p>
            </div>
            <div class="step">
                <span>▶️</span>
                <b>Run Container</b>
                <p>App runs on port 8009</p>
            </div>
        </div>
    </div>

    <footer>
        <p>✅ CI/CD pipeline working successfully!</p>
        <p>Built using Python, Docker & GitHub Actions</p>
    </footer>
</div>
</body>
</html>
"""

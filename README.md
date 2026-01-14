# GitHub Actions CI/CD Project 🚀

A complete CI/CD pipeline demonstration project that automatically builds, pushes, and deploys a FastAPI application using GitHub Actions, Docker, and Docker Hub to an EC2 instance.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Workflow Details](#workflow-details)
- [Running Locally](#running-locally)
- [GitHub Secrets Configuration](#github-secrets-configuration)
- [EC2 Setup](#ec2-setup)
- [Testing the Pipeline](#testing-the-pipeline)
- [Accessing the Application](#accessing-the-application)
- [Troubleshooting](#troubleshooting)
- [Technologies Used](#technologies-used)

## 🎯 Overview

This project demonstrates a production-ready CI/CD pipeline that:

1. **Automatically triggers** when code is pushed to the `main` branch
2. **Builds** a Docker image of the FastAPI application
3. **Pushes** the image to Docker Hub
4. **Deploys** the application to an EC2 instance via SSH
5. **Runs** the containerized application on port 5050

The application displays a beautiful, animated dashboard showing the CI/CD workflow status and runtime information.

## ✨ Features

- ✅ Automated CI/CD pipeline with GitHub Actions
- ✅ Docker containerization for consistent deployments
- ✅ Automatic deployment to EC2 on code push
- ✅ Beautiful, responsive web dashboard
- ✅ Zero-downtime deployments (stops old container before starting new one)
- ✅ Container auto-restart on failure
- ✅ Real-time build and runtime information display

## 🏗️ Architecture

```
┌─────────────┐
│   GitHub    │
│ Repository  │
└──────┬──────┘
       │ Push to main
       ▼
┌─────────────────┐
│ GitHub Actions  │
│   Workflow      │
└──────┬──────────┘
       │
       ├──► Build Docker Image
       │
       ├──► Push to Docker Hub
       │
       └──► SSH to EC2
            │
            ├──► Pull Image
            ├──► Stop Old Container
            ├──► Remove Old Container
            └──► Run New Container
                 │
                 ▼
            ┌─────────────┐
            │   EC2       │
            │  Instance   │
            │ Port: 5050  │
            └─────────────┘
```

## 📦 Prerequisites

Before setting up this project, ensure you have:

- **GitHub Account** - For repository hosting and GitHub Actions
- **Docker Hub Account** - For storing Docker images
- **AWS EC2 Instance** - For hosting the application
- **Git** - Installed on your local machine
- **Docker** (optional) - For local testing

## 📁 Project Structure

```
github-actions-project/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions workflow configuration
│
├── app.py                     # FastAPI application with dashboard
├── Dockerfile                 # Docker image configuration
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

### File Descriptions

- **`app.py`**: FastAPI application that serves a beautiful HTML dashboard displaying CI/CD workflow information, hostname, build time, and workflow steps.

- **`Dockerfile`**: Multi-stage Docker configuration that:
  - Uses Python 3.11 slim base image
  - Installs dependencies from `requirements.txt`
  - Copies application code
  - Exposes port 5050
  - Runs the application with uvicorn

- **`requirements.txt`**: Python package dependencies:
  - `fastapi`: Modern web framework for building APIs
  - `uvicorn`: ASGI server for running FastAPI

- **`.github/workflows/ci-cd.yml`**: GitHub Actions workflow that:
  - Triggers on push to `main` branch
  - Builds Docker image
  - Pushes to Docker Hub
  - Deploys to EC2 via SSH

## 🚀 Setup Instructions

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `github-actions-project` (or any name you prefer)
3. Initialize with a README (optional)

### Step 2: Clone and Prepare Local Repository

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/github-actions-project.git
cd github-actions-project

# Copy all project files to this directory
# Ensure you have:
# - app.py
# - Dockerfile
# - requirements.txt
# - .github/workflows/ci-cd.yml
```

### Step 3: Create Docker Hub Repository

1. Go to [Docker Hub](https://hub.docker.com)
2. Click "Create Repository"
3. Name it `github-actions-project`
4. Set visibility to Public or Private (your choice)
5. Click "Create"

### Step 4: Configure GitHub Secrets

Navigate to your GitHub repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add the following secrets:

| Secret Name | Description | Example |
|------------|-------------|---------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username | `yourusername` |
| `DOCKERHUB_TOKEN` | Docker Hub access token | `dckr_pat_...` |
| `EC2_HOST` | EC2 instance public IP or hostname | `ec2-xx-xx-xx-xx.compute-1.amazonaws.com` |
| `EC2_USER` | EC2 SSH username (usually `ubuntu` or `ec2-user`) | `ubuntu` |
| `EC2_SSH_KEY` | Private SSH key for EC2 access | `-----BEGIN RSA PRIVATE KEY-----...` |

#### How to Get Docker Hub Token:

1. Go to Docker Hub → Account Settings → Security
2. Click "New Access Token"
3. Give it a name (e.g., "GitHub Actions")
4. Copy the token (you won't see it again!)

#### How to Get EC2 SSH Key:

If you don't have the SSH key:
1. Generate a new key pair in EC2 Console
2. Download the `.pem` file
3. Copy the entire contents (including `-----BEGIN` and `-----END` lines)

### Step 5: EC2 Instance Setup

#### 5.1 Launch EC2 Instance

1. Go to AWS EC2 Console
2. Launch a new instance:
   - **AMI**: Ubuntu Server 22.04 LTS (or latest)
   - **Instance Type**: t2.micro (free tier) or larger
   - **Key Pair**: Select or create a key pair
   - **Security Group**: Configure to allow:
     - SSH (port 22) from your IP
     - HTTP (port 5050) from anywhere (0.0.0.0/0)

#### 5.2 Install Docker on EC2

SSH into your EC2 instance:

```bash
ssh -i your-key.pem ubuntu@YOUR_EC2_IP
```

Install Docker:

```bash
# Update system packages
sudo apt-get update

# Install Docker
sudo apt-get install -y docker.io

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add your user to docker group (to run without sudo)
sudo usermod -aG docker ubuntu

# Log out and log back in for group changes to take effect
exit
```

Reconnect to verify Docker installation:

```bash
ssh -i your-key.pem ubuntu@YOUR_EC2_IP
docker --version
```

### Step 6: Push Code to GitHub

```bash
# Add all files
git add .

# Commit changes
git commit -m "Initial CI/CD Setup"

# Push to main branch
git push origin main
```

### Step 7: Monitor the Pipeline

1. Go to your GitHub repository
2. Click on the **Actions** tab
3. You should see the workflow running
4. Click on the workflow run to see detailed logs

## 🔄 Workflow Details

The CI/CD workflow (`ci-cd.yml`) performs the following steps:

### 1. Checkout Code
- Checks out the repository code to the GitHub Actions runner

### 2. Login to Docker Hub
- Authenticates with Docker Hub using secrets

### 3. Build Docker Image
- Builds the Docker image with tag: `USERNAME/github-actions-project:latest`

### 4. Push to Docker Hub
- Pushes the built image to Docker Hub registry

### 5. Deploy to EC2
- Connects to EC2 via SSH
- Logs into Docker Hub on EC2
- Stops and removes existing container (if any)
- Removes old Docker image (if any)
- Pulls the latest image from Docker Hub
- Runs a new container with:
  - Port mapping: `5050:5050`
  - Restart policy: `unless-stopped`
  - Container name: `github-actions-project`

## 💻 Running Locally

To test the application locally before deploying:

### Build Docker Image

```bash
docker build -t github-actions-project .
```

### Run Container

```bash
docker run -p 5050:5050 github-actions-project
```

### Access Application

Open your browser and navigate to:

```
http://localhost:5050
```

You should see the CI/CD dashboard with project information and workflow visualization.

## 🔐 GitHub Secrets Configuration

### Required Secrets

All secrets must be configured in: **Repository Settings** → **Secrets and variables** → **Actions**

| Secret | Purpose |
|--------|---------|
| `DOCKERHUB_USERNAME` | Docker Hub username for authentication |
| `DOCKERHUB_TOKEN` | Docker Hub access token (not password!) |
| `EC2_HOST` | EC2 instance public IP address or DNS |
| `EC2_USER` | SSH username (typically `ubuntu` for Ubuntu AMIs) |
| `EC2_SSH_KEY` | Complete private SSH key content |

### Security Best Practices

- ✅ Never commit secrets to the repository
- ✅ Use access tokens instead of passwords
- ✅ Rotate tokens regularly
- ✅ Use least-privilege IAM roles for EC2
- ✅ Restrict security group rules to specific IPs when possible

## 🖥️ EC2 Setup

### Security Group Configuration

Ensure your EC2 security group allows:

| Type | Protocol | Port Range | Source |
|------|----------|------------|--------|
| SSH | TCP | 22 | Your IP address |
| Custom TCP | TCP | 5050 | 0.0.0.0/0 (or specific IPs) |

### Docker Installation Verification

After installing Docker, verify it works:

```bash
# Test Docker
docker run hello-world

# Check Docker service status
sudo systemctl status docker
```

## 🧪 Testing the Pipeline

### Test Workflow Trigger

1. Make a small change to `app.py` (e.g., update a comment)
2. Commit and push:

```bash
git add app.py
git commit -m "Test CI/CD pipeline"
git push origin main
```

3. Watch the GitHub Actions tab for the workflow execution
4. Check logs for any errors

### Verify Deployment

After the workflow completes:

```bash
# SSH into EC2
ssh -i your-key.pem ubuntu@YOUR_EC2_IP

# Check running containers
docker ps

# Check container logs
docker logs github-actions-project

# Test the application
curl http://localhost:5050
```

## 🌐 Accessing the Application

Once deployed, access your application at:

```
http://YOUR_EC2_IP:5050
```

Replace `YOUR_EC2_IP` with your EC2 instance's public IP address.

The dashboard will display:
- Docker image information
- Running hostname
- Build timestamp
- Exposed port
- Visual CI/CD workflow steps

## 🐛 Troubleshooting

### Workflow Fails at Docker Login

**Problem**: Authentication error with Docker Hub

**Solutions**:
- Verify `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets are correct
- Ensure Docker Hub token has proper permissions
- Check if token has expired

### Workflow Fails at SSH Connection

**Problem**: Cannot connect to EC2 instance

**Solutions**:
- Verify `EC2_HOST` is correct (use public IP or DNS)
- Check `EC2_USER` matches your AMI (ubuntu/ec2-user)
- Ensure `EC2_SSH_KEY` includes complete key (BEGIN/END lines)
- Verify security group allows SSH from GitHub Actions IPs
- Check EC2 instance is running

### Container Fails to Start

**Problem**: Container exits immediately

**Solutions**:
- Check container logs: `docker logs github-actions-project`
- Verify port 5050 is not already in use
- Check security group allows traffic on port 5050
- Ensure Docker is running on EC2: `sudo systemctl status docker`

### Image Pull Fails on EC2

**Problem**: Cannot pull image from Docker Hub

**Solutions**:
- Verify Docker Hub repository exists and is accessible
- Check Docker login credentials in workflow
- Ensure image was successfully pushed in previous step
- Check EC2 instance has internet connectivity

### Port Already in Use

**Problem**: Port 5050 is already occupied

**Solutions**:
```bash
# Find process using port 5050
sudo lsof -i :5050

# Stop the container
docker stop github-actions-project

# Or change port in workflow and Dockerfile
```

## 🛠️ Technologies Used

- **Python 3.11** - Programming language
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server
- **Docker** - Containerization platform
- **GitHub Actions** - CI/CD automation platform
- **Docker Hub** - Container registry
- **AWS EC2** - Cloud computing instance
- **SSH** - Secure remote access protocol

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review GitHub Actions workflow logs
3. Check EC2 instance logs and Docker container logs

---

**Built with ❤️ using GitHub Actions, Docker, and FastAPI**

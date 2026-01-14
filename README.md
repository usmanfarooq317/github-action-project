📄 README.md

# GitHub Actions CI/CD Project 🚀

This project demonstrates a complete CI/CD workflow using:

- Python (FastAPI)
- Docker
- GitHub Actions
- Docker Hub

## Workflow
1. Push code to GitHub
2. GitHub Actions builds Docker image
3. Pushes image to Docker Hub
4. Pulls image back
5. Runs container on port 8009

## Run Locally
```bash
docker build -t github-actions-project .
docker run -p 8009:8009 github-actions-project


Open:
http://localhost:8009


---

# 7️⃣ How to Perform Everything (Step-by-Step)

### ✅ Step 1
Create GitHub repo:


github-actions-project


### ✅ Step 2
Add all files exactly as shown

### ✅ Step 3
Create Docker Hub repository:


github-actions-project


### ✅ Step 4
Add GitHub Secrets (username + token)

### ✅ Step 5
Push code to `main` branch

```bash
git add .
git commit -m "Initial CI/CD Setup"
git push origin main

✅ Step 6

Go to GitHub → Actions tab
✔ Pipeline runs automatically
✔ Image pushed to Docker Hub
✔ Container runs on port 8009

🎯 Final Result

When you open:

http://<server-ip>:8009


You will see a clean, professional, animated CI/CD dashboard clearly showing:

GitHub Actions workflow

Docker image

Runtime details.

Successful deployment!
# Quick Setup Guide - Student Management System CI/CD Project

## 🚀 Quick Start (5 Minutes)

### Prerequisites Check
```powershell
# Verify all tools are installed
python --version    # Should show Python 3.x
git --version       # Should show Git 2.x
docker --version    # Should show Docker 24.x+
```

If any command fails, install the missing tool first.

---

## Step 1: Test Application Locally (2 minutes)

```powershell
# Install dependencies
pip install flask

# Run application
python app.py

# Open browser: http://localhost:5000
# Press Ctrl+C to stop
```

✅ **Success:** You should see the Student Management System interface

---

## Step 2: Initialize Git Repository (1 minute)

```powershell
# Initialize Git
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add and commit files
git add .
git commit -m "Initial commit: Student Management System"
```

✅ **Success:** `git log` shows your commit

---

## Step 3: Create GitHub Repository (2 minutes)

1. Go to https://github.com/new
2. Repository name: `student-management-cicd`
3. Click "Create repository"
4. Copy the repository URL

```powershell
# Link to GitHub (replace with YOUR URL)
git remote add origin https://github.com/YOUR-USERNAME/student-management-cicd.git
git branch -M main
git push -u origin main
```

✅ **Success:** Code appears on GitHub

---

## Step 4: Test Docker (3 minutes)

```powershell
# Build Docker image
docker build -t student-app .

# Run container
docker run -d -p 5000:5000 --name student-app student-app

# Test it works
curl http://localhost:5000/health

# Or open browser: http://localhost:5000

# Stop when done
docker stop student-app
docker rm student-app
```

✅ **Success:** Application runs in Docker container

---

## Step 5: Setup Jenkins (5 minutes)

### Option A: Jenkins in Docker (Recommended)

```powershell
# Run Jenkins container
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

# Wait 2 minutes for Jenkins to start

# Get admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# Copy the password output
```

1. Open http://localhost:8080
2. Paste admin password
3. Click "Install suggested plugins" (wait 3-5 minutes)
4. Create admin user:
   - Username: admin
   - Password: admin (or your choice)
   - Full name: Your Name
   - Email: your email
5. Click "Save and Continue" → "Start using Jenkins"

### Create Pipeline:

1. Click "New Item"
2. Name: `Student-App-Pipeline`
3. Select "Pipeline" → OK
4. Scroll to "Pipeline" section
5. Definition: "Pipeline script from SCM"
6. SCM: Git
7. Repository URL: `https://github.com/YOUR-USERNAME/student-management-cicd.git`
8. Branch: `*/main`
9. Script Path: `Jenkinsfile`
10. Click "Save"
11. Click "Build Now"

✅ **Success:** Pipeline executes all 5 stages successfully

---

## 🎯 Testing Complete Workflow

```powershell
# 1. Make a change
# Edit app.py - change title or add a comment

# 2. Commit and push
git add .
git commit -m "Test CI/CD pipeline"
git push origin main

# 3. Jenkins automatically builds (if polling configured)
# Or click "Build Now" in Jenkins

# 4. Verify deployment
curl http://localhost:5000/health
```

---

## 📸 Screenshots Needed for Submission

Create a folder named `screenshots` and capture:

### Python & Flask
1. `python --version` terminal output
2. Flask app running in terminal
3. Application homepage in browser

### Git & GitHub
4. `git log` showing commits
5. GitHub repository page with files
6. Push success message

### Docker
7. `docker build` completion
8. `docker ps` showing running container
9. Application running via Docker

### Jenkins
10. Jenkins dashboard
11. Pipeline configuration
12. Successful build with all stages green
13. Console output showing each stage

### Application
14. Home page with student list
15. Add student form
16. Health check API response (`/health`)

---

## 🔧 Troubleshooting

### Port Already in Use
```powershell
# Find what's using the port
netstat -ano | findstr :5000

# Kill the process (replace PID)
taskkill /PID <PID> /F
```

### Docker Not Running
- Open Docker Desktop manually
- Wait for "Docker Desktop is running" message

### Git Push Authentication
- Use Personal Access Token instead of password
- Generate: GitHub → Settings → Developer settings → Personal access tokens
- Use token as password when pushing

### Jenkins Can't Access Docker
```powershell
# Restart Docker and Jenkins
docker restart jenkins
```

---

## 📝 Documentation Checklist

Before submission:

- [ ] Update LAB_ISE2_Documentation.md with your name and roll number
- [ ] Add your GitHub repository URL
- [ ] Take all required screenshots
- [ ] Test all commands and verify outputs
- [ ] Convert documentation to PDF
- [ ] Verify PDF is readable and complete
- [ ] Upload to ERP portal

---

## 🆘 Quick Commands Reference

```powershell
# Application
python app.py                                    # Run locally
curl http://localhost:5000                       # Test home
curl http://localhost:5000/health               # Health check
curl http://localhost:5000/api/students         # API test

# Git
git status                                       # Check status
git add .                                        # Stage all
git commit -m "message"                         # Commit
git push origin main                            # Push to GitHub
git log --oneline                               # View history

# Docker
docker ps                                        # List containers
docker logs student-app                         # View logs
docker stop student-app                         # Stop container
docker rm student-app                           # Remove container
docker images                                   # List images
docker system prune -a                          # Clean everything

# Jenkins (in Docker)
docker logs jenkins                             # View Jenkins logs
docker restart jenkins                          # Restart Jenkins
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

---

## ⏱️ Time Allocation

- Application testing: 10 minutes
- Git setup: 5 minutes
- GitHub setup: 5 minutes
- Docker testing: 10 minutes
- Jenkins setup: 15 minutes
- Pipeline configuration: 10 minutes
- Documentation: 30 minutes
- Screenshots: 15 minutes

**Total:** ~2 hours

---

## 📞 Help Resources

- **Lab In-charge:** Mr. Shekhar Jalane
- **Submission Date:** 29th October 2026
- **Marks:** 10 (ISE-2)

**Good luck! 🎓**

# CICD Pipeline and Monitoring Tools
## Summary Report

---

### Details - Student Entry

| Details | Student Entry |
|---------|---------------|
| **Student Name** | [Enter Your Name] |
| **Roll Number(s)** | [Enter Your Roll Number] |
| **Department / Class** | CSE (Data Science) - Final Year B.Tech |
| **Academic Year** | A.Y 2026-27 |
| **GitHub Repository URL** | [Enter Your Repository URL] |

---

## 1. Problem Statement

**Project:** Student Management System with Complete CI/CD Pipeline

Develop a **Student Management System** web application and implement the complete DevOps lifecycle on a Windows PC. The application provides functionality to manage student records (add, view, delete) with a modern web interface.

**Implementation includes:**
- **Version Control:** Git for tracking code changes and managing versions
- **Source Code Hosting:** GitHub for remote repository and collaboration
- **Application Development:** Python Flask framework for web application
- **Containerization:** Docker for packaging application with dependencies
- **CI/CD Automation:** Jenkins for automated build, test, and deployment pipeline
- **Monitoring:** Health check endpoints and Docker container monitoring

**Tools Used:** Python, Flask, Git, GitHub, Docker, Docker Compose, Jenkins

The project demonstrates the complete journey of an application from development to production deployment through automated DevOps practices.

---

## 2. Tools: Environment Setup

### 1. Python and Flask — Web Application Development

#### 1. Environment Setup

**Installation Steps:**
- Download Python 3.11+ from https://www.python.org/downloads/
- Run installer and check "Add Python to PATH"
- Verify installation by opening PowerShell

**Dependencies:**
- Flask 3.0.0 - Web framework
- Werkzeug 3.0.1 - WSGI utility library

#### 2. Commands to Run on Windows

```powershell
# Verify Python installation
python --version

# Output: Python 3.11.x

# Verify pip installation
pip --version

# Output: pip 23.x.x from C:\Python311\lib\site-packages\pip (python 3.11)

# Install Flask framework
pip install flask

# Output: Successfully installed Flask-3.0.0 Werkzeug-3.0.1

# Navigate to project directory
cd d:\AWS_lab\aws_ise2

# Run the Flask application
python app.py

# Output:
#  * Serving Flask app 'app'
#  * Debug mode: on
#  * Running on http://127.0.0.1:5000
#  * Press CTRL+C to quit
```

**Verification:**
- Open browser and navigate to http://localhost:5000
- Application should display Student Management System interface

**Screenshot Points:**
- [ ] Python version output
- [ ] Flask installation success
- [ ] Application running in terminal
- [ ] Web interface in browser

---

### 2. Git — Version Control

#### 1. Environment Setup

**Installation Steps:**
- Download Git for Windows from https://git-scm.com/download/win
- Run installer with default settings
- Select "Git from the command line and also from 3rd-party software"
- Configure user credentials for commit tracking

**Configuration:**
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### 2. Commands to Run on Windows

```powershell
# Verify Git installation
git --version

# Output: git version 2.43.0.windows.1

# Initialize Git repository in project folder
git init

# Output: Initialized empty Git repository in D:/AWS_lab/aws_ise2/.git/

# Check repository status
git status

# Output: 
# On branch master
# Untracked files:
#   app.py
#   Dockerfile
#   requirements.txt
#   ... (other files)

# Stage all files for commit
git add .

# Verify staged files
git status

# Output: Changes to be committed: (list of files)

# Create first commit
git commit -m "Initial commit: Student Management System with CI/CD pipeline"

# Output:
# [master (root-commit) abc1234] Initial commit: Student Management System with CI/CD pipeline
#  10 files changed, 520 insertions(+)

# View commit history
git log --oneline

# Output: abc1234 (HEAD -> master) Initial commit: Student Management System with CI/CD pipeline
```

**Verification:**
- `.git` folder created in project directory
- Files tracked by Git
- Commit history available

**Screenshot Points:**
- [ ] Git version verification
- [ ] Repository initialization
- [ ] Git status showing tracked files
- [ ] Successful commit message

---

### 3. GitHub — Source-Code Hosting

#### 1. Environment Setup

**Steps:**
1. **Create GitHub Account:**
   - Navigate to https://github.com
   - Sign up for free account
   - Verify email address

2. **Create Remote Repository:**
   - Click "New Repository"
   - Name: `student-management-cicd`
   - Description: "Student Management System with CI/CD Pipeline - ISE 2 Project"
   - Set as Public or Private
   - Do NOT initialize with README (we have local code)
   - Click "Create Repository"

3. **Configure Authentication:**
   
   **Option A: Personal Access Token (Recommended)**
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Generate new token with `repo` scope
   - Save token securely
   - Use token as password when pushing

   **Option B: SSH Key**
   ```powershell
   ssh-keygen -t ed25519 -C "your.email@example.com"
   # Add public key to GitHub Settings → SSH Keys
   ```

#### 2. Commands to Run on Windows

Replace `REPOSITORY_URL` with your actual GitHub repository URL.

```powershell
# Add remote repository
git remote add origin https://github.com/YOUR-USERNAME/student-management-cicd.git

# Verify remote configuration
git remote -v

# Output:
# origin  https://github.com/YOUR-USERNAME/student-management-cicd.git (fetch)
# origin  https://github.com/YOUR-USERNAME/student-management-cicd.git (push)

# Rename branch to main (GitHub default)
git branch -M main

# Push code to GitHub
git push -u origin main

# Output:
# Enumerating objects: 15, done.
# Counting objects: 100% (15/15), done.
# Delta compression using up to 8 threads
# Compressing objects: 100% (12/12), done.
# Writing objects: 100% (15/15), 12.34 KiB | 1.23 MiB/s, done.
# Total 15 (delta 2), reused 0 (delta 0), pack-reused 0
# To https://github.com/YOUR-USERNAME/student-management-cicd.git
#  * [new branch]      main -> main
# Branch 'main' set up to track remote branch 'main' from 'origin'.

# Pull latest changes from remote (for updates)
git pull origin main

# Output: Already up to date.
```

**Verification:**
- Navigate to your GitHub repository URL
- All project files should be visible
- Commit history should match local repository

**Screenshot Points:**
- [ ] GitHub repository page showing files
- [ ] Successful push output in terminal
- [ ] Repository commits page
- [ ] Remote verification command output

---

### 4. Docker — Application Containerization

#### 1. Environment Setup

**Installation Steps:**
1. **Download Docker Desktop:**
   - Visit https://www.docker.com/products/docker-desktop
   - Download Docker Desktop for Windows
   - System Requirements: Windows 10 64-bit Pro/Enterprise/Education or Windows 11

2. **Enable WSL 2 (if required):**
   ```powershell
   wsl --install
   wsl --set-default-version 2
   ```

3. **Install Docker Desktop:**
   - Run installer
   - Enable "Use WSL 2 instead of Hyper-V"
   - Restart computer
   - Start Docker Desktop
   - Wait for "Docker Desktop is running" status

4. **Verify Docker Engine:**
   - Docker icon should appear in system tray
   - Engine status should be green/running

#### 2. Commands to Run on Windows

```powershell
# Verify Docker installation
docker --version

# Output: Docker version 24.0.7, build 311b9ff

# Verify Docker Compose
docker compose version

# Output: Docker Compose version v2.23.3

# Check Docker system information
docker info

# Output: 
# Server Version: 24.0.7
# Storage Driver: overlay2
# Kernel Version: 5.15.133.1-microsoft-standard-WSL2
# Operating System: Docker Desktop
# ... (additional info)

# Navigate to project directory
cd d:\AWS_lab\aws_ise2

# Build Docker image from Dockerfile
docker build -t student-app .

# Output:
# [+] Building 45.3s (10/10) FINISHED
# => [internal] load build definition from Dockerfile
# => [internal] load .dockerignore
# => [internal] load metadata for docker.io/library/python:3.11-slim
# => [1/5] FROM docker.io/library/python:3.11-slim
# => [2/5] WORKDIR /app
# => [3/5] COPY requirements.txt .
# => [4/5] RUN pip install --no-cache-dir -r requirements.txt
# => [5/5] COPY . .
# => exporting to image
# => => naming to docker.io/library/student-app
# Successfully built abc123def456
# Successfully tagged student-app:latest

# List Docker images
docker images

# Output:
# REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
# student-app    latest    abc123def456   30 seconds ago   180MB

# Run container in detached mode
docker run -d -p 5000:5000 --name student-app student-app

# Output: xyz789abc123... (container ID)

# List running containers
docker ps

# Output:
# CONTAINER ID   IMAGE         COMMAND           CREATED         STATUS         PORTS                    NAMES
# xyz789abc123   student-app   "python app.py"   10 seconds ago  Up 9 seconds   0.0.0.0:5000->5000/tcp   student-app

# View container logs
docker logs student-app

# Output:
#  * Serving Flask app 'app'
#  * Running on all addresses (0.0.0.0)
#  * Running on http://127.0.0.1:5000
#  * Running on http://172.17.0.2:5000

# Check container stats
docker stats student-app --no-stream

# Stop container
docker stop student-app

# Remove container
docker rm student-app

# Alternative: Using Docker Compose
docker compose up -d

# Output:
# [+] Running 1/1
#  ✔ Container student-app  Started

# Stop using Docker Compose
docker compose down
```

**Verification:**
- Open browser: http://localhost:5000
- Application should load from containerized environment
- Same functionality as local Python execution

**Screenshot Points:**
- [ ] Docker version output
- [ ] Docker build process completion
- [ ] Docker images list
- [ ] Container running status (docker ps)
- [ ] Application running in browser via Docker
- [ ] Docker logs showing Flask startup

---

### 5. Jenkins — Continuous Integration and Continuous Deployment

#### 1. Environment Setup

**Prerequisites:**
- Java JDK 17 or later (required for Jenkins)
- Git (for source code checkout)
- Docker (for containerized builds)

**Installation Option A: Jenkins on Windows**

1. **Install Java JDK:**
   - Download from https://www.oracle.com/java/technologies/downloads/
   - Install and set JAVA_HOME environment variable
   ```powershell
   $env:JAVA_HOME = "C:\Program Files\Java\jdk-17"
   ```

2. **Install Jenkins:**
   - Download Jenkins WAR from https://www.jenkins.io/download/
   - Or download Windows Installer
   - Run installer or start WAR file:
   ```powershell
   java -jar jenkins.war --httpPort=8080
   ```

**Installation Option B: Jenkins in Docker (Recommended)**

```powershell
# Pull Jenkins LTS image and run container
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

# Get initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

**Initial Jenkins Setup:**
1. Navigate to http://localhost:8080
2. Enter initial admin password (from above command)
3. Install suggested plugins
4. Create first admin user
5. Configure Jenkins URL: http://localhost:8080/

**Configure Docker Integration:**
1. Manage Jenkins → Manage Plugins
2. Install "Docker Pipeline" plugin
3. Manage Jenkins → Global Tool Configuration
4. Configure Docker (if needed)

**Configure Git Integration:**
1. Manage Jenkins → Global Tool Configuration
2. Git should be auto-detected
3. If not, provide Git executable path: `C:\Program Files\Git\bin\git.exe`

#### 2. Commands to Run on Windows

**For Jenkins installed directly on Windows:**

```powershell
# Verify Java installation
java -version

# Output:
# openjdk version "17.0.9" 2023-10-17
# OpenJDK Runtime Environment (build 17.0.9+9-Ubuntu-122.04)

# Verify Git installation
git --version

# Output: git version 2.43.0.windows.1

# Verify Docker installation
docker --version

# Output: Docker version 24.0.7, build 311b9ff

# Start Jenkins service (if installed as Windows service)
net start jenkins

# Output: The Jenkins service is starting...

# Check Jenkins status
Get-Service jenkins

# Alternative: Start Jenkins WAR file
java -jar jenkins.war --httpPort=8080
```

**For Jenkins running as a Docker container named jenkins:**

```powershell
# Check if Jenkins container is running
docker ps

# Output:
# CONTAINER ID   IMAGE                 STATUS         PORTS                               NAMES
# abc123def456   jenkins/jenkins:lts   Up 5 minutes   0.0.0.0:8080->8080/tcp, 50000/tcp   jenkins

# View Jenkins logs
docker logs jenkins

# Output: (Jenkins startup logs and initial admin password)

# Start Jenkins container (if stopped)
docker start jenkins

# Output: jenkins

# Stop Jenkins container
docker stop jenkins

# Restart Jenkins container
docker restart jenkins

# Execute commands inside Jenkins container
docker exec jenkins java -version

# Output: openjdk version "17.0.9"

# Get initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# Output: abc123def456789...
```

**Create Jenkins Pipeline:**

1. **Create New Job:**
   - Click "New Item"
   - Enter name: "Student-App-Pipeline"
   - Select "Pipeline"
   - Click "OK"

2. **Configure Pipeline:**
   - Description: "CI/CD Pipeline for Student Management System"
   
   - **Build Triggers:**
     - ✓ Poll SCM: `H/5 * * * *` (check every 5 minutes)
     - Or GitHub webhook for instant triggers
   
   - **Pipeline Definition:**
     - Definition: Pipeline script from SCM
     - SCM: Git
     - Repository URL: `https://github.com/YOUR-USERNAME/student-management-cicd.git`
     - Credentials: Add GitHub credentials if private
     - Branch: `*/main`
     - Script Path: `Jenkinsfile`
   
3. **Save and Build:**
   - Click "Save"
   - Click "Build Now"

**Pipeline Execution:**

The Jenkinsfile defines these stages:

```
Stage 1: Checkout - Pull code from GitHub
Stage 2: Build - Build Docker image
Stage 3: Test - Run basic tests
Stage 4: Deploy - Deploy container
Stage 5: Health Check - Verify deployment
```

**Monitor Build:**
```powershell
# After triggering build in Jenkins UI
# Monitor console output for each stage

# Build Output Example:
# [Pipeline] Start of Pipeline
# [Pipeline] node
# [Pipeline] {
# [Pipeline] stage (Checkout)
# [Pipeline] { (Checkout)
# [Pipeline] echo
# Checking out code from GitHub...
# [Pipeline] checkout
# Cloning repository https://github.com/YOUR-USERNAME/student-management-cicd.git
# [Pipeline] } (Checkout)
# 
# [Pipeline] stage (Build)
# [Pipeline] { (Build)
# [Pipeline] echo
# Building Docker image...
# [Pipeline] bat
# docker build -t student-app:1 .
# Successfully built abc123
# [Pipeline] } (Build)
# 
# [Pipeline] stage (Test)
# [Pipeline] { (Test)
# [Pipeline] echo
# Running tests...
# App module loaded successfully
# [Pipeline] } (Test)
# 
# [Pipeline] stage (Deploy)
# [Pipeline] { (Deploy)
# [Pipeline] echo
# Deploying application...
# [Pipeline] bat
# docker run -d -p 5000:5000 --name student-app student-app:latest
# [Pipeline] } (Deploy)
# 
# [Pipeline] stage (Health Check)
# [Pipeline] { (Health Check)
# [Pipeline] echo
# Performing health check...
# {"status":"healthy","timestamp":"2026-10-27T23:00:00","total_students":0}
# [Pipeline] } (Health Check)
# 
# [Pipeline] } (node)
# [Pipeline] End of Pipeline
# Finished: SUCCESS
```

**Verification:**
- Jenkins Dashboard shows successful build (blue ball)
- Console output shows all stages passed
- Application accessible at http://localhost:5000

**Screenshot Points:**
- [ ] Java version verification
- [ ] Jenkins dashboard homepage
- [ ] Pipeline configuration page
- [ ] Build history showing successful builds
- [ ] Console output of successful pipeline execution
- [ ] Each pipeline stage passing
- [ ] Application deployed and running

---

## 3. Complete CI/CD Workflow

### End-to-End Process

```
Developer → Git Commit → GitHub Push → Jenkins Trigger → 
Build Docker Image → Run Tests → Deploy Container → Health Check → Production
```

### Step-by-Step Workflow:

1. **Development Phase:**
   ```powershell
   # Make code changes in app.py
   python app.py  # Test locally
   ```

2. **Version Control:**
   ```powershell
   git add .
   git commit -m "Add new feature: Student search"
   git push origin main
   ```

3. **Automated CI/CD (Jenkins):**
   - Jenkins detects GitHub push (via polling or webhook)
   - Automatically triggers pipeline
   - Executes all stages: Checkout → Build → Test → Deploy → Health Check

4. **Verification:**
   ```powershell
   # Check running container
   docker ps
   
   # Test application
   curl http://localhost:5000/health
   
   # Access in browser
   start http://localhost:5000
   ```

---

## 4. Application Features

### Student Management System

**Core Functionality:**
- ✅ View all students in a responsive table
- ✅ Add new students with details (Name, Roll Number, Department, Email)
- ✅ Delete students with confirmation
- ✅ RESTful API for programmatic access
- ✅ Health monitoring endpoint for DevOps
- ✅ Modern, responsive UI design
- ✅ JSON-based data persistence

**API Endpoints:**

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/` | GET | Home page with student list | HTML |
| `/add` | GET/POST | Add student form | HTML/Redirect |
| `/delete/<id>` | GET | Delete student | Redirect |
| `/api/students` | GET | Get all students | JSON Array |
| `/health` | GET | Health status | JSON Object |

**Health Check Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-10-27T23:00:00.123456",
  "total_students": 5
}
```

---

## 5. Project File Structure

```
aws_ise2/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker image definition
├── docker-compose.yml          # Docker Compose configuration
├── Jenkinsfile                 # CI/CD pipeline definition
├── .gitignore                  # Git ignore patterns
├── README.md                   # Complete project documentation
├── LAB_ISE2_Documentation.md   # This lab report
│
├── templates/                  # Flask HTML templates
│   ├── index.html             # Home page (student list)
│   └── add_student.html       # Add student form
│
└── students.json              # Data storage (created at runtime)
```

---

## 6. Screenshots Required for Submission

### Python & Flask
- [ ] `python --version` output
- [ ] `pip install flask` success message
- [ ] Application running in terminal
- [ ] Web interface in browser (http://localhost:5000)

### Git
- [ ] `git --version` output
- [ ] `git init` initialization
- [ ] `git status` showing tracked files
- [ ] `git commit` success message
- [ ] `git log` showing commit history

### GitHub
- [ ] GitHub repository main page with files
- [ ] `git push` success output
- [ ] Repository commits page
- [ ] Repository file tree

### Docker
- [ ] `docker --version` output
- [ ] `docker build` process completion
- [ ] `docker images` list
- [ ] `docker ps` showing running container
- [ ] `docker logs` showing Flask startup
- [ ] Application running via Docker

### Jenkins
- [ ] Jenkins dashboard
- [ ] Pipeline configuration page
- [ ] Build history showing success
- [ ] Console output of pipeline stages
- [ ] Each stage (Checkout, Build, Test, Deploy, Health Check) passing
- [ ] Blue Ocean view (if available)

### Application Features
- [ ] Home page with student list
- [ ] Add student form
- [ ] Student successfully added
- [ ] Health check API response
- [ ] API endpoint JSON response

---

## 7. Commands Summary Cheat Sheet

```powershell
# Python & Flask
python --version
pip --version
pip install flask
python app.py

# Git
git --version
git init
git status
git add .
git commit -m "message"
git log --oneline

# GitHub
git remote add origin URL
git remote -v
git branch -M main
git push -u origin main
git pull origin main

# Docker
docker --version
docker compose version
docker info
docker build -t student-app .
docker images
docker run -d -p 5000:5000 --name student-app student-app
docker ps
docker logs student-app
docker stop student-app
docker rm student-app
docker compose up -d
docker compose down

# Jenkins (Docker)
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
docker ps
docker logs jenkins
docker start jenkins
docker stop jenkins
docker exec jenkins java -version

# Jenkins (Windows)
java -version
git --version
docker --version
net start jenkins

# Testing
curl http://localhost:5000/health
curl http://localhost:5000/api/students
```

---

## 8. Troubleshooting Guide

### Common Issues and Solutions

**Python/Flask:**
```powershell
# Issue: Flask not found
# Solution:
pip install --upgrade flask

# Issue: Port 5000 already in use
# Solution: Change port in app.py
# app.run(host='0.0.0.0', port=5001)
```

**Git/GitHub:**
```powershell
# Issue: Authentication failed
# Solution: Use Personal Access Token
# Generate token: GitHub Settings → Developer settings → Personal access tokens
# Use token as password when pushing

# Issue: Remote already exists
# Solution:
git remote remove origin
git remote add origin NEW_URL
```

**Docker:**
```powershell
# Issue: Docker daemon not running
# Solution: Start Docker Desktop manually

# Issue: Port conflict
# Solution: Stop conflicting containers
docker stop $(docker ps -q)

# Issue: Build fails
# Solution: Clear Docker cache
docker builder prune
docker build --no-cache -t student-app .
```

**Jenkins:**
```powershell
# Issue: Jenkins can't access Docker
# Solution: Ensure Docker is running and accessible

# Issue: Build fails at Docker stage
# Solution: Check Jenkins has Docker permissions
# Add jenkins user to docker group (Linux)
# Or run Jenkins with admin privileges (Windows)

# Issue: Can't clone from GitHub
# Solution: Add GitHub credentials in Jenkins
# Manage Jenkins → Manage Credentials → Add Credentials
```

---

## 9. Learning Outcomes Achieved

### Technical Skills Acquired:

1. **Web Application Development (CO1 - L2)**
   - ✅ Built functional Flask web application
   - ✅ Implemented CRUD operations
   - ✅ Created RESTful API endpoints
   - ✅ Designed responsive user interface

2. **Version Control (CO1 - L2)**
   - ✅ Initialized Git repository
   - ✅ Tracked file changes with commits
   - ✅ Managed remote repository on GitHub
   - ✅ Understood branching and merging concepts

3. **Containerization (CO4 - L4)**
   - ✅ Created Docker images from Dockerfile
   - ✅ Ran applications in isolated containers
   - ✅ Configured Docker Compose for multi-container apps
   - ✅ Understood container orchestration basics

4. **CI/CD Pipeline (CO4 - L4)**
   - ✅ Configured Jenkins automation server
   - ✅ Created declarative Jenkins pipeline
   - ✅ Integrated Git, Docker, and deployment
   - ✅ Implemented automated testing and deployment

5. **DevOps Practices (CO1, CO4)**
   - ✅ Understood software development lifecycle
   - ✅ Automated build and deployment processes
   - ✅ Implemented monitoring and health checks
   - ✅ Applied Infrastructure as Code principles

---

## 10. Conclusion

This project successfully demonstrates the complete DevOps lifecycle on Windows platform. The Student Management System web application was developed using Python Flask, version-controlled with Git, hosted on GitHub, containerized with Docker, and deployed through an automated Jenkins CI/CD pipeline.

**Key Achievements:**
- Functional web application with database operations
- Complete version control and remote repository management
- Successfully containerized application running in Docker
- Fully automated CI/CD pipeline from code commit to deployment
- Health monitoring and logging capabilities

**Tools Mastery:**
- Python & Flask for web development
- Git & GitHub for version control
- Docker & Docker Compose for containerization
- Jenkins for continuous integration and deployment

This hands-on experience provides a solid foundation for modern software development practices and prepares for real-world DevOps scenarios in the industry.

---

## 11. References and Resources

### Official Documentation:
1. **Python:** https://docs.python.org/3/
2. **Flask:** https://flask.palletsprojects.com/
3. **Git:** https://git-scm.com/doc
4. **GitHub:** https://docs.github.com/
5. **Docker:** https://docs.docker.com/
6. **Jenkins:** https://www.jenkins.io/doc/

### Tutorials and Guides:
- Flask Mega-Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- Docker Get Started: https://docs.docker.com/get-started/
- Jenkins Pipeline Tutorial: https://www.jenkins.io/doc/book/pipeline/getting-started/

### Additional Resources:
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
- Docker Cheat Sheet: https://docs.docker.com/get-started/docker_cheatsheet.pdf
- DevOps Roadmap: https://roadmap.sh/devops

---

## 12. Submission Details

**Course Information:**
- **Course Name:** ML DevOps Laboratory
- **Course Code:** UDSPC0732
- **Semester:** VII (Final Year B.Tech)
- **Department:** Computer Science and Engineering (Data Science)
- **Academic Year:** 2026-27

**Assessment:**
- **ISE-2:** 10 Marks
- **Evaluation Criteria:**
  - CO1 (L2): Understanding of DevOps tools - 50%
  - CO4 (L4): CI/CD pipeline implementation - 50%

**Scheduled Date:** 29th October 2026

**Course In-charge:** Mr. Shekhar Jalane

**Submission Requirements:**
1. ✅ PDF version of this documentation
2. ✅ GitHub repository with complete code
3. ✅ Screenshots of all commands and outputs
4. ✅ Working demonstration (if required)

---

## Appendix A: Configuration Files

### requirements.txt
```txt
Flask==3.0.0
Werkzeug==3.0.1
```

### Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
CMD ["python", "app.py"]
```

### docker-compose.yml
```yaml
version: '3.8'
services:
  web:
    build: .
    container_name: student-app
    ports:
      - "5000:5000"
    volumes:
      - ./students.json:/app/students.json
    environment:
      - FLASK_APP=app.py
      - FLASK_ENV=production
    restart: unless-stopped
```

### Jenkinsfile (Abbreviated)
```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') { ... }
        stage('Build') { ... }
        stage('Test') { ... }
        stage('Deploy') { ... }
        stage('Health Check') { ... }
    }
}
```

---

## Appendix B: Sample Data

### Sample Students JSON
```json
[
  {
    "id": 1,
    "name": "Rahul Sharma",
    "roll_number": "2026001",
    "department": "CSE (Data Science)",
    "email": "rahul.sharma@example.com",
    "added_date": "2026-10-27 22:30:45"
  },
  {
    "id": 2,
    "name": "Priya Patel",
    "roll_number": "2026002",
    "department": "CSE (Data Science)",
    "email": "priya.patel@example.com",
    "added_date": "2026-10-27 22:35:12"
  }
]
```

---

**Document Version:** 1.0  
**Last Updated:** 27th October 2026  
**Prepared By:** [Your Name]  
**Roll Number:** [Your Roll Number]

---

**End of Report**

---

### Instructions for PDF Conversion:

1. **Update Personal Information:**
   - Replace `[Enter Your Name]` with your actual name
   - Replace `[Enter Your Roll Number]` with your roll number
   - Replace `[Enter Your Repository URL]` with your GitHub repository URL
   - Update `[Your Name]` in Author sections

2. **Add Screenshots:**
   - Take screenshots as per the checklist in Section 6
   - Insert screenshots in appropriate sections
   - Ensure screenshots are clear and readable

3. **Convert to PDF:**
   - Use Markdown to PDF converter (e.g., Pandoc, VS Code Markdown PDF extension)
   - Or copy content to Microsoft Word and save as PDF
   - Ensure formatting is preserved

4. **Final Review:**
   - Check all commands are correctly documented
   - Verify all outputs match your actual execution
   - Ensure all personal information is filled
   - Review for completeness

5. **Submit:**
   - Upload PDF to ERP portal
   - Include GitHub repository link
   - Submit before deadline: 29th October 2026

---

**Good luck with your submission! 🚀**

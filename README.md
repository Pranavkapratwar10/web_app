# Student Management System - CI/CD Pipeline Project

## ISE-2: ML DevOps Laboratory
**Course Code:** UDSPC0732  
**Academic Year:** 2026-27  
**Semester:** VII

---

## 📋 Problem Statement

Develop a **Student Management System** web application and implement a complete DevOps lifecycle on Windows. The project demonstrates:
- Version control with **Git**
- Source code hosting on **GitHub**
- Application containerization with **Docker**
- CI/CD automation with **Jenkins**
- End-to-end deployment pipeline

---

## 🛠️ Tools & Technologies

### 1. **Python and Flask** - Web Application Development

**Features:**
- Student CRUD operations (Create, Read, Delete)
- RESTful API endpoints
- Health monitoring endpoint
- Responsive UI with modern design
- JSON-based data persistence

**Environment Setup:**
```powershell
# Check Python installation
python --version

# Check pip installation
pip --version

# Install Flask and dependencies
pip install flask

# Run the application
python app.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

---

### 2. **Git** - Version Control

**Environment Setup:**
- Download and install Git for Windows from https://git-scm.com/
- Configure user credentials

**Commands to Run:**
```powershell
# Verify Git installation
git --version

# Configure Git (replace with your details)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize repository
git init

# Check status
git status

# Stage all files
git add .

# Commit changes
git commit -m "Initial commit: Student Management System with CI/CD"

# View commit history
git log --oneline
```

**Expected Output:**
```
git version 2.43.0.windows.1
Initialized empty Git repository in D:/AWS_lab/aws_ise2/.git/
[main (root-commit) abc1234] Initial commit: Student Management System with CI/CD
 10 files changed, 500 insertions(+)
```

---

### 3. **GitHub** - Source Code Hosting

**Environment Setup:**
1. Create GitHub account at https://github.com
2. Create a new repository named `student-management-cicd`
3. Configure authentication using GitHub Personal Access Token or SSH

**Commands to Run:**
```powershell
# Add remote repository (replace with your URL)
git remote add origin https://github.com/YOUR-USERNAME/student-management-cicd.git

# Verify remote
git remote -v

# Rename branch to main
git branch -M main

# Push code to GitHub
git push -u origin main

# Pull latest changes
git pull origin main
```

**Expected Output:**
```
Enumerating objects: 15, done.
Writing objects: 100% (15/15), 12.34 KiB | 1.23 MiB/s, done.
To https://github.com/YOUR-USERNAME/student-management-cicd.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

### 4. **Docker** - Application Containerization

**Environment Setup:**
1. Download Docker Desktop from https://www.docker.com/products/docker-desktop
2. Install and enable WSL 2 backend
3. Start Docker Desktop

**Commands to Run:**
```powershell
# Verify Docker installation
docker --version

# Verify Docker Compose
docker compose version

# Check Docker info
docker info

# Build Docker image
docker build -t student-app .

# List images
docker images

# Run container
docker run -d -p 5000:5000 --name student-app student-app

# List running containers
docker ps

# View container logs
docker logs student-app

# Stop container
docker stop student-app

# Remove container
docker rm student-app

# Using Docker Compose
docker compose up -d

# Stop Docker Compose
docker compose down
```

**Expected Output:**
```
Docker version 24.0.7, build 311b9ff
Docker Compose version v2.23.3

Successfully built abc123def456
Successfully tagged student-app:latest

CONTAINER ID   IMAGE          STATUS        PORTS                    NAMES
xyz123abc456   student-app   Up 5 seconds   0.0.0.0:5000->5000/tcp   student-app
```

**Access Application:** http://localhost:5000

---

### 5. **Jenkins** - CI/CD Pipeline

**Environment Setup:**

**Option A: Jenkins on Windows**
1. Install Java JDK 17 or later
2. Download Jenkins WAR or Windows installer
3. Start Jenkins service

**Option B: Jenkins in Docker (Recommended)**
```powershell
# Run Jenkins in Docker
docker run -d -p 8080:8080 -p 50000:50000 `
  --name jenkins `
  -v jenkins_home:/var/jenkins_home `
  -v /var/run/docker.sock:/var/run/docker.sock `
  jenkins/jenkins:lts

# Get initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

**Commands to Run:**

**For Jenkins on Windows:**
```powershell
# Verify Java installation
java -version

# Verify Git (required for Jenkins)
git --version

# Verify Docker (required for pipeline)
docker --version

# Start Jenkins (if installed as service)
net start jenkins
```

**For Jenkins in Docker:**
```powershell
# Check Jenkins container status
docker ps

# View Jenkins logs
docker logs jenkins

# Start Jenkins container
docker start jenkins

# Stop Jenkins container
docker stop jenkins

# Check Java version inside container
docker exec jenkins java -version
```

**Expected Output:**
```
openjdk version "17.0.9" 2023-10-17
Docker version 24.0.7, build 311b9ff
git version 2.43.0.windows.1

CONTAINER ID   IMAGE                 STATUS          PORTS
abc123         jenkins/jenkins:lts   Up 2 minutes    0.0.0.0:8080->8080/tcp
```

**Jenkins Setup Steps:**
1. Access Jenkins at http://localhost:8080
2. Enter initial admin password
3. Install suggested plugins
4. Create first admin user
5. Configure Jenkins URL

**Configure Jenkins Pipeline:**
1. Create New Item → Pipeline
2. Configure Source Code Management:
   - Select "Git"
   - Enter repository URL
   - Add credentials if private repo
3. Build Triggers:
   - Select "GitHub hook trigger for GITScm polling" (for automatic builds)
   - Or "Poll SCM" with schedule `H/5 * * * *` (every 5 minutes)
4. Pipeline Definition:
   - Select "Pipeline script from SCM"
   - SCM: Git
   - Script Path: `Jenkinsfile`
5. Save and Build

**Pipeline Stages:**
1. **Checkout** - Pull latest code from GitHub
2. **Build** - Build Docker image
3. **Test** - Run basic tests
4. **Deploy** - Deploy container
5. **Health Check** - Verify application is running

---

## 🚀 Complete Workflow

### Step 1: Develop Application
```powershell
# Create and test Flask app locally
python app.py
```

### Step 2: Version Control
```powershell
git init
git add .
git commit -m "Initial commit"
```

### Step 3: Push to GitHub
```powershell
git remote add origin YOUR_REPO_URL
git push -u origin main
```

### Step 4: Containerize with Docker
```powershell
docker build -t student-app .
docker run -d -p 5000:5000 student-app
```

### Step 5: Automate with Jenkins
1. Create Jenkins pipeline job
2. Connect to GitHub repository
3. Configure Jenkinsfile
4. Trigger build
5. Monitor pipeline execution

### Step 6: Verify Deployment
```powershell
# Check container status
docker ps

# Test health endpoint
curl http://localhost:5000/health

# Access application
start http://localhost:5000
```

---

## 📊 Application Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page - List all students |
| `/add` | GET/POST | Add new student form |
| `/delete/<id>` | GET | Delete student by ID |
| `/api/students` | GET | JSON API - Get all students |
| `/health` | GET | Health check endpoint |

---

## 🔍 Monitoring & Verification

### Application Health Check
```powershell
curl http://localhost:5000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-10-27T23:00:00",
  "total_students": 5
}
```

### Docker Monitoring
```powershell
# Container stats
docker stats student-app

# Container logs
docker logs -f student-app

# Container inspection
docker inspect student-app
```

### Jenkins Monitoring
- Access Jenkins Dashboard: http://localhost:8080
- View build history and console output
- Monitor pipeline stages
- Check build artifacts

---

## 📁 Project Structure

```
aws_ise2/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── Jenkinsfile           # Jenkins pipeline definition
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
├── templates/
│   ├── index.html        # Home page template
│   └── add_student.html  # Add student form
└── students.json         # Data storage (created at runtime)
```

---

## 🎯 Learning Outcomes

This project demonstrates:
1. ✅ **CO1 (L2)** - Understanding DevOps tools and their integration
2. ✅ **CO4 (L4)** - Analyzing and implementing complete CI/CD pipeline
3. ✅ Version control and collaborative development
4. ✅ Containerization best practices
5. ✅ Automated build and deployment
6. ✅ Monitoring and health checks

---

## 🐛 Troubleshooting

### Python Issues
```powershell
# If Flask not found
pip install --upgrade flask

# If port 5000 in use
# Change port in app.py: app.run(port=5001)
```

### Docker Issues
```powershell
# If Docker daemon not running
# Start Docker Desktop manually

# If port conflict
docker stop $(docker ps -q)
```

### Jenkins Issues
```powershell
# If Jenkins can't access Docker
# Ensure Jenkins user has Docker permissions

# If build fails
# Check Jenkins console output for specific errors
```

---

## 📝 Submission Checklist

- [x] Flask application developed and tested
- [x] Git repository initialized and configured
- [x] Code pushed to GitHub
- [x] Dockerfile created and tested
- [x] Jenkins pipeline configured
- [x] CI/CD pipeline executed successfully
- [x] Documentation completed
- [x] Screenshots captured
- [x] PDF report generated

---

## 👨‍💻 Author

**Student Name:** [Your Name]  
**Roll Number:** [Your Roll Number]  
**Department:** CSE (Data Science)  
**Academic Year:** A.Y 2026-27

**GitHub Repository:** [Your Repository URL]

---

## 📅 Submission Details

**Due Date:** 29th October 2026  
**Course In-charge:** Mr. Shekhar Jalane

---

## 🔗 References

- Flask Documentation: https://flask.palletsprojects.com/
- Docker Documentation: https://docs.docker.com/
- Jenkins Documentation: https://www.jenkins.io/doc/
- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/

---

**Note:** Replace placeholder values (Your Name, Roll Number, Repository URL) with your actual information before submission.

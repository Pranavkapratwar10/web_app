pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'student-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                script {
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                    bat "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    bat "docker run --rm ${DOCKER_IMAGE}:${DOCKER_TAG} python -c \"import app; print('App module loaded successfully')\""
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                script {
                    // Stop and remove existing container if running
                    bat "docker stop student-app || exit 0"
                    bat "docker rm student-app || exit 0"
                    
                    // Run new container
                    bat "docker run -d -p 5000:5000 --name student-app ${DOCKER_IMAGE}:latest"
                }
            }
        }
        
        stage('Health Check') {
            steps {
                echo 'Performing health check...'
                script {
                    sleep 10
                    bat "curl http://localhost:5000/health || exit 0"
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
            echo "Application is running at http://localhost:5000"
        }
        failure {
            echo 'Pipeline failed! Check logs for details.'
        }
        always {
            echo 'Cleaning up...'
            bat "docker image prune -f || exit 0"
        }
    }
}

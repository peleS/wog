pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flaskapp'
        DOCKER_CONTAINER = 'flask_app'
        DOCKERHUB_USER = 'pelesh'
        DOCKERHUB_REPO = 'training'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker-compose up -d'
                    sleep 10 // Give some time for the service to be fully up
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def result = sh(script: 'python3 e2e.py', returnStatus: true)
                    if (result != 0) {
                        error('E2E test failed!')
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker-compose down'
                    sh "docker tag ${DOCKER_IMAGE} ${DOCKERHUB_USER}/${DOCKERHUB_REPO}:${BUILD_NUMBER}"
                    sh "docker push ${DOCKERHUB_USER}/${DOCKERHUB_REPO}:${BUILD_NUMBER}"
                }
            }
        }
    }
}

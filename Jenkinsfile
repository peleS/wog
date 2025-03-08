pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Application') {
            steps {
                sh 'docker-compose up -d app'
                sleep 8  # Wait for service to start
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker-compose run --rm test'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker-compose down'
            }
        }
    }
}

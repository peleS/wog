pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/user/world_of_games.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t world_of_games .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:8777 --name world_games world_of_games'
            }
        }
        stage('Test') {
            steps {
                sh 'python e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker stop world_games && docker rm world_games'
                sh 'docker push user/world_of_games'
            }
        }
    }
}
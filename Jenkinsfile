pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'sudo docker build -t world_of_games .'
            }
        }
        stage('Run') {
            steps {
                sh 'sudo docker rm -f world_games || true'
                sh 'sudo docker run -d -p 8777:8777 --name world_games world_of_games'
            }
        }
        stage('Test') {
            steps {
                sh 'python e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'sudo docker stop world_games && docker rm world_games'
                sh 'sudo docker push user/world_of_games'
            }
        }
    }
}
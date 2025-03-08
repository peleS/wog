pipeline {
    agent any

    stages {
        stage('Cleanup Old Containers') {
            steps {
                    sh '''
                    if sudo docker ps -a --format "{{.Names}}" | grep -q "^world_games$"; then
                    sudo docker rm -f world_games
                    fi
                    sudo docker ps -a
                    '''
            }
        }

        stage('Check Environment') {
            steps {
                    sh 'env'  // Print all environment variables
                    }
        }

        stage('Check Scores.txt File') {
            steps {
                    sh 'ls -l ./Scores.txt'  // Check if the file is in the workspace
                    }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                set -x
                docker-compose --verbose build
                sudo docker logs world_games || true
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh 'docker-compose up -d app'
                sh 'sleep 8'
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

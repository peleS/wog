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
                sh '''
                    if sudo docker ps -a --format "{{.Names}}" | grep -q "^world_games$"; then
                    sudo docker rm -f world_games
                    fi
                    sudo docker run -d -p 8777:8777 --name world_games world_of_games
                    '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    sudo docker logs world_games
                    sudo docker ps -a
                    for i in {1..15}; do
                        if sudo docker ps -a --format "{{.Names}}" | grep -q "^world_games$"; then
                            sudo docker exec world_games python test/e2e.py
                            break
                        else
                            echo "Attempt $i: Container world_games is not running. Retrying..."
                            sleep 1
                        fi
                    done

                    # Option 2: Run test in a new container with network access to the running app
                    # sudo docker run --network=host world_of_games python test/e2e.py

                '''
            }
        }
        stage('Finalize') {
            steps {
                sh 'sudo docker stop world_games && sudo docker rm world_games'
                sh 'sudo docker push user/world_of_games'
            }
        }
    }
}
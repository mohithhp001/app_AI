pipeline {
    agent any

    stages {
        stage('Docker Build & Deploy') {
            steps {
                sh '''
                    export PATH=$PATH:/opt/homebrew/bin
                    docker-compose down
                    docker-compose build --no-cache
                    docker-compose up -d
                '''
            }
        }

        stage('Testing Services') {
            steps {
                sh '''
                    sleep 10
                    curl --fail http://localhost:3000 || exit 1
                    curl --fail http://localhost:8000/docs || exit 1
                    curl --fail http://localhost:5001/docs || exit 1
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build and Deployment Successful!'
        }
        failure {
            echo '❌ Build or Deployment Failed!'
        }
    }
}

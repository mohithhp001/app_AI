pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/mohithhp001/app_AI.git', credentialsId: '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'
            }
        }

        stage('Docker Build & Deploy') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose build --no-cache'
                sh 'docker-compose up -d'
            }
        }

        stage('Testing Services') {
            steps {
                sh 'sleep 10'
                sh 'curl --fail http://localhost:3000 || exit 1'
                sh 'curl --fail http://localhost:8000/docs || exit 1'
                sh 'curl --fail http://localhost:5001/docs || exit 1'
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

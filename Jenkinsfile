pipeline {
    agent any

    stages {
        stage('🚧 Checkout') {
            steps {
                checkout scm
            }
        }

        stage('🐋 Docker Build') {
          steps {
              sh 'docker-compose down'
              sh 'docker-compose build --no-cache'
              sh 'docker-compose up -d'
          }
      }

      stage('🧪 Automated Tests') {
          steps {
              sh 'sleep 10'  // Allow services time to start clearly
              sh 'curl --fail http://localhost:3000'
              sh 'curl --fail http://localhost:8000/docs'
              sh 'curl --fail http://localhost:5001/docs'
          }
      }
  }
}

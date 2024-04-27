pipeline{
    agent any
    stages{
        stage('Deploy to container'){
            steps{
                sh 'docker run -d -p 8081:8081 flask_weatherapi:letest'
            }
        }
 }          

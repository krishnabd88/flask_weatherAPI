pipeline{
    agent any
    environment{
        SONAR_HOME= tool "sonar-scanner"
    }
    stages{
      
        stage("Code Checkout"){
            steps{
                git url:"git@github.com:krishnabd88/flask_weatherAPI.git", branch:"main"
            }
        }
        
        stage("SonarQube Code Analysis"){
            steps{
                withSonarQubeEnv("sonar-server"){
                    sh "$SONAR_HOME/bin/sonar-scanner -Dsonar.projectName=weatherapi -Dsonar.projectKey=weatherapi"
                }
            }
        stage('Deploy to container'){
            steps{
                sh 'docker run -d -p 8081:8081 flask_weatherapi:letest'
            }
        }


    }
}           
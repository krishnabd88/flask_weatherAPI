pipeline{
    agent any
    environment{
        SONAR_HOME= tool "sonar"
    }
    stages{
      
        stage("Code Checkout"){
            steps{
                git url:"git@github.com:krishnabd88/flask_weatherAPI.git", branch:"main"
            }
        }
        
        stage("SonarQube Code Analysis"){
            steps{
                withSonarQubeEnv("Sonar-server"){
                    sh "$SONAR_HOME/bin/sonar-scanner -Dsonar.projectName=weatherapi -Dsonar.projectKey=weatherapi"
                }
            }
        }

    }
}           

pipeline{
    agent any
    environment{
        SONAR_HOME= tool "Sonar"
    }
    stages{
      
        stage("Code Checkout"){
            steps{
                git url:"git@github.com:krishnabd88/flask_weatherAPI.git", branch:"main"
            }
        }
        
        stage("SonarQube Code Analysis"){
            steps{
                withSonarQubeEnv("Sonar"){
                    sh "$SONAR_HOME/bin/sonar-scanner -Dsonar.projectName=wanderlust -Dsonar.projectKey=wanderlust"
                }
            }
        }

    }
}           
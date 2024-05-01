pipeline{
    agent any
    environment{
        SONAR_HOME= tool "sonar-scanner"
    }
    stages{
      
        stage("Code Checkout"){
            steps{
                git url:"https://github.com/krishnabd88/flask_weatherAPI.git", 
                    branch:"main"
            }
        }
        
        stage("SonarQube Code Analysis"){
            steps{
                withSonarQubeEnv("sonar-server"){
                    sh "$SONAR_HOME/bin/sonar-scanner -Dsonar.projectName=weatherapi -Dsonar.projectKey=weatherapi"
                }
              }
            }

        stage("docker build"){
            steps{
                sh "docker build -t krishnabd88/flask_weatherapi:latest ."
                }
             }
        Stage("docker deploy"){
            Steps{
                sh "docker run -d -t -p 8081:8081 --name weatherapi krishnabd88/flask_weatherapi:latest"
                }
            }
        }           
    }

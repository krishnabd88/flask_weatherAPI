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
        stage("docker image scan by trivy"){
            steps{
                sh "trivy image krishnabd88/flask_weatherapi --format table -o trivy-appimage-report.html --cache-opt= --dir $HOME/trivy-cache"
                }
            }
         stage("docker deploy"){
            steps{
                sh "docker run -d -t -p 8081:8081 --name weatherapi krishnabd88/flask_weatherapi:latest"
                }
            }
        }           
    }

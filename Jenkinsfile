pipeline {
    agent any

    environment {
        PYTHON_VERSION = "python3"
        VIRTUAL_ENV = "venv/bin/activate"    
    }

    stages {
        stage('Modules'){
            steps{
                sh 'sudo apt-get update && sudo apt-get install -y nodejs npm python3 python3-venv python3-pip'
            }
        }
        stage('Dependencies') {
            parallel {
                stage('Frontend') {
                    steps {
                        dir('frontend') {
                            sh 'npm install'
                        }
                    }
                }
                
                stage('Backend Setup') {
                    steps {
                        dir('backend') {
                            sh """
                            ${PYTHON_VERSION} -m venv venv
                            source ${VIRTUAL_ENV}
                            pip install --upgrade pip
                            pip install -r requirements.txt
                            """
                        }
                    }
                }
            }
        }
    }
}
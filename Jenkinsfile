pipeline {
    agent any

    environment {
        PYTHON_VERSION = "3.14.2"
        VIRTUAL_ENV = "backend/venv/bin/activate"    
    }

    stages {
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
                            python${PYTHON_VERSION} -m venv venv
                            source venv/bin/activate
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
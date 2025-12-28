pipeline {
    agent any

    environment {
        PYTHON_VERSION = "python3"
        VIRTUAL_ENV = "venv/bin/activate"    
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
                
                stage('Backend') {
                    steps {
                        dir('backend') { 
                            sh """
                            ${PYTHON_VERSION} -m venv venv
                            . ${VIRTUAL_ENV}
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
pipeline {
    agent any

    environment {
        PYTHON_VERSION = "python3"
        VIRTUAL_ENV = "venv/bin/activate"    
    }

    stages {
        stage('Install Dependencies') {
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
        stage('Run Testing'){
            parallel{
                stage('React Test'){
                    steps{
                        dir('frontend'){
                            sh 'CI=true npm run test'
                            echo('React test successfull.')
                        }
                    }
                }
                stage('FastAPI Test'){
                    steps{
                        dir('backend'){
                            sh 'PYTHONPATH=. venv/bin/pytest tests/ -v'
                            echo('React test successfull.')
                        }
                    }
                }
            }
        }
    }
}
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
                            sh 'npm ci || npm install'
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
                stage('Frontend'){
                    steps{
                        dir('frontend'){
                            sh 'CI=true npm run test'
                            echo('Frontend test successfull.')
                        }
                    }
                }
                stage('Backend'){
                    steps{
                        dir('backend'){
                            sh 'PYTHONPATH=. venv/bin/pytest tests/ -v'
                            echo('Backend test successfull.')
                        }
                    }
                }
            }
        }
    }
}
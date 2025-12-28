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

        stage('Build Image'){
            parallel{
                stage('Frontend'){
                    steps{
                        dir('frontend'){
                            sh 'docker build -t mmsalmanfaris/advanced-jenkins-frontend:${env.GIT_COMMIT}'
                            echo('Frontend docker build success')
                        }
                    }
                }
                stage('Backend'){
                    steps{
                        dir('backend'){
                            sh 'docker build -t mmsalmanfaris/advanced-jenkins-backend:${env.GIT_COMMIT}'
                            echo('Backend docker build success')
                        }
                    }
                }
            }
        }

        stage('Login to dockerhub'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]){
                    sh 'echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin'
                    echo 'Login Success'
                }
            }
        }

        stage('Push frontend image'){
            steps{
                    sh 'docker push mmsalmanfaris/advanced-jenkins-frontend:${env.GIT_COMMIT}'
                }
        }

        stage('Push backend image'){
            steps{
                    sh 'docker push mmsalmanfaris/advanced-jenkins-backend:${env.GIT_COMMIT}'
            }
        }
    }
}
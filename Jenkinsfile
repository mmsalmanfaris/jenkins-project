pipeline {
    agent any

    environment {
        PYTHON_VERSION = "python3"
        REGISTRY= "mmsalmanfaris"
        GIT_COMMIT_SHORT= "${env.GIT_COMMIT.take(7)}"
    }

    stages {

        stage('Debug Context') {
    steps {
        sh '''
          echo "CHANGE_ID=$CHANGE_ID"
          echo "CHANGE_TARGET=$CHANGE_TARGET"
          echo "BRANCH_NAME=$BRANCH_NAME"
        '''
    }
}


        stage('PR Guard') {
    when {
        expression { env.CHANGE_ID == null }
    }
    steps {
        echo "Not a PR build. Skipping pipeline."
        currentBuild.result = 'NOT_BUILT'
        error('Stopping non-PR build')
    }
}

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
                            venv/bin/pip install --upgrade pip
                            venv/bin/pip install -r requirements.txt
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
                            sh 'CI=true npm test -- --watchAll=false'
                            sh 'echo "Frontend test successfull"'
                        }
                    }
                }
                stage('Backend'){
                    steps{
                        dir('backend'){
                            sh """
                            ${PYTHON_VERSION} -m venv venv
                            venv/bin/pip install --upgrade pip
                            venv/bin/pip install -r requirements.txt
                            PYTHONPATH=. venv/bin/pytest tests/ -v
                            """
                            sh 'echo "Backend test successfull"'
                        }
                    }
                }
            }
        }

        // stage('Build Image'){
        //     parallel{
        //         stage('Frontend'){
        //             steps{
        //                 dir('frontend'){
        //                     sh 'docker build -t ${REGISTRY}/advanced-jenkins-frontend:${GIT_COMMIT_SHORT} .'
        //                     sh 'echo "Frontend docker build success"'
        //                 }
        //             }
        //         }
        //         stage('Backend'){
        //             steps{
        //                 dir('backend'){
        //                     sh 'docker build -t ${REGISTRY}/advanced-jenkins-backend:${GIT_COMMIT_SHORT} .'
        //                     sh 'echo "Backend docker build success"'
        //                 }
        //             }
        //         }
        //     }
        // }

        // stage('Login to dockerhub'){
        //     steps{
        //         withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]){
        //             sh 'echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin'
        //             sh 'echo "Login Success"'
        //         }
        //     }
        // }
        // stage('Push images'){
        //     parallel{
        //         stage('Push frontend image'){
        //             steps{
        //                     sh 'docker push ${REGISTRY}/advanced-jenkins-frontend:${GIT_COMMIT_SHORT}'
        //                 }
        //         }

        //         stage('Push backend image'){
        //             steps{
        //                     sh 'docker push mmsalmanfaris/advanced-jenkins-backend:${GIT_COMMIT_SHORT}'
        //             }
        //         }
        //     }
        // }

    }

    post{
            success {
                echo "PR ${env.CHANGE_ID} passed"
            }
            failure {
    echo env.CHANGE_ID ?
        "PR ${env.CHANGE_ID} failed" :
        "Non-PR build skipped"
}

        }
}
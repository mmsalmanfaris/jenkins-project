pipeline{
    agent any

    environment{
        PYTHON_VERSION = "python3"
    }

    stages{
        // Pull Request
        stage('CI - PR Validation'){
            when{
                allOf{
                    expression {env.CHANGE_ID}
                    expression {env.CHANGE_TARGET == 'develop'}
                }
            }
            steps{
                echo "Running CI for PR -> develop"
            }
        }
        stage('Install Dependencies') {
            when{
                allOf{
                    expression {env.CHANGE_ID}
                    expression {env.CHANGE_TARGET == 'develop'}
                }
            }

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
            when{
                allOf{
                    expression {env.CHANGE_ID}
                    expression {env.CHANGE_TARGET == 'develop'}
                }
            }
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

        stage('Develop Branch - Skip'){
            when{
                expression {env.BRANCH_NAME == 'develop' && !env.CHANGE_ID}
            }
            steps{
                echo "Develop branch push detected - skipping pipeline"
            }
        }

        stage('CD - Release'){
            when{
                branch 'main'
            }
            steps{
                echo "Release pipeline"
            }
        }
    }

    post{
        failure {
            script{
                if(env.CHANGE_ID && env.CHANGE_TARGET =='develop'){
                    slackSend(
                        tokenCredentialId: 'slack-token',
                        channel: '#github-pr-check',
                        botUser: true,
                        message: """
                                PR Check Failed :x:
                                *Repo:* ${env.JOB_NAME}
                                *PR:* #${env.CHANGE_ID}
                                *Branch:* ${env.CHANGE_BRANCH}
                                """.stripIndent()
                    )
                }
            }
        }
        success{
            script{
                if(env.CHANGE_ID && env.CHANGE_TARGET == 'develop' && currentBuild.previousBuild?.result == 'FAILURE'){
                    slackSend(
                        tokenCredentialId: 'slack-token',
                        channel: '#github-pr-check',
                        botUser: true,
                        message: """ PR Check Fixed ✅
                                    *Repo:* ${env.JOB_NAME}
                                    *PR:* #${env.CHANGE_ID}
                                    *Branch:* ${env.CHANGE_BRANCH}
                                 """
                    )
                }
            }
        }
    }
}
pipeline{
    agent any

    stages{
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

        stage('Develop Branch - Skip'){
            when{
                expression {env.BRANCH_NAME == 'develop' && !env.CHANGE_ID}
            }
            steps{
                echo "Develop branch push detected - skipping pieline"
            }
        }

        stage('CD - Release'){
            when{
                branch 'main'
            }
            steps{
                echo "Release pieline"
            }
        }
    }
}
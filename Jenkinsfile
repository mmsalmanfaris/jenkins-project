pipeline{
    agent any

    stages{
        stage('Dependencies'){
            parallel{
                stages{
                    stage('Frontend'){
                        steps{
                            sh 'cd ./frontend'
                            sh 'npm install'
                        }
                    }
                    stage('Backend'){
                        steps{
                            // sh 'cd ./backend'
                            // sh 'python3 -m pip install --upgrade pip'
                            // sh 'pip install -r requirements.txt'
                        }
                    }
                }
            }
        }
        stage('Version'){
            steps{
                // sh 'pip --version'

            }
        }
        stage(Build){
            steps{
                // docker build
            }
        }
    }
}
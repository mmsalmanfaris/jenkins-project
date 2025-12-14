pipeline{
    agent any

    environment{
        PYTHON_VERSION = "3.14.2"
        VIRTUAL_ENV = "venv/bin/activate"    
    }

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
                        stages{
                            stage('Setup venv'){
                                steps{
                                    sh'''
                                    cd ./backend
                                    python${PYTHON_VERSION} -m venv venv
                                    source ${VIRTUAL_ENV}
                                    pip install --upgrade pip
                                    '''
                                }
                            }

                            stage('Install Dependencies'){
                                steps{
                                    sh'''
                                    source ${VIRTUAL_ENV}
                                    pip install -r requirements.txt
                                    '''
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
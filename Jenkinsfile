@Library('ciinabox') _

pipeline {

    environment {
        PROJECT='demo-aws-sam-cdk'
        S3_BUCKET = 'demo'
    }

    agent {
        label 'linux'
    }

    stages {

        stage('unit tests') {
            agent {
                docker {
                    image 'ghcr.io/base2services/pytest:3.8'
                }
            }
        }

        stage('compile cloudformation') {
            agent {
                docker {
                    image 'ghcr.io/base2services/aws-cdk:1.63.0'
                }
            }
            steps {
                sh 'python -m pip install -r requirements.txt'
                sh 'cdk synth > template.yaml'
            }
        }

        stage('build lambdas') {
            agent {
                docker {
                    image 'ghcr.io/base2services/sam-cli:1.0.0'
                }
            }
            steps {
                sh 'sam build'
            }
        }
    }
}
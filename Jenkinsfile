pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/harisastha6/aceest-devops.git'
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r app/requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t aceest-app .'
            }
        }

        stage('Push Docker') {
            steps {
                sh 'docker tag aceest-app harisastha6/aceest-app:v1'
                sh 'docker push harisastha6/aceest-app:v1'
            }
        }
    }
}
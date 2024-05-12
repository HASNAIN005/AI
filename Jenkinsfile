pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('BFS') {
            steps {
               sh 'python3 BFS.py'
            }
        }
    }
}

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git url: 'https://github.com/HASNAIN005/AI'
            }
        }
        stage('Run A STAR.py') {
            steps {
                // Execute A STAR.py and capture its output
                script {
                    def output = sh(script: 'python "A STAR.py"', returnStdout: true).trim()
                    echo "Output of A STAR.py:\n${output}"
                }
            }
        }
    }
}

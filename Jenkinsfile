pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-southeast-1'
        S3_BUCKET = 'raw-images-uploads-bucket'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/sarveshghag-cloud/Automated-Image-Zipping-Pipeline-using-AWS-Serverless-Services.git'
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Deploy UI to S3') {
            steps {
                withAWS(credentials: 'aws-credentials', region: 'ap-southeast-1') {
                    sh '''
                    aws s3 cp index.html s3://raw-images-uploads-bucket/
                    aws s3 cp app.js s3://raw-images-uploads-bucket/
                    aws s3 cp style.css s3://raw-images-uploads-bucket/
                    '''
                }
            }
        }
    }
}
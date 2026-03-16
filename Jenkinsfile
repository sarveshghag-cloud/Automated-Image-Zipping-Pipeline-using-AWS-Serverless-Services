pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-southeast-1'
        S3_BUCKET = 'raw-images-uploads-bucket'
        LAMBDA_FUNCTION = 'image-zip-lambda'
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
                sh '''
                aws s3 cp index.html s3://$S3_BUCKET/
                aws s3 cp app.js s3://$S3_BUCKET/
                '''
            }
        }

        stage('Deploy Lambda Code') {
            steps {
                sh '''
                zip lambda.zip lambda_function.py
                aws lambda update-function-code \
                --function-name $LAMBDA_FUNCTION \
                --zip-file fileb://lambda.zip \
                --region $AWS_REGION
                '''
            }
        }

    }

    post {
        success {
            echo 'Deployment Successful 🎉'
        }
        failure {
            echo 'Deployment Failed ❌'
        }
    }
}
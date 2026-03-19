pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-southeast-1'
        S3_BUCKET = 'raw-images-uploads-bucket'
        LAMBDA_FUNCTION = 'image-zip-function'
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
                echo "Uploading UI to S3..."
                aws s3 sync . s3://$S3_BUCKET --exclude ".git/*"
                '''
            }
        }

        stage('Package Lambda') {
            steps {
                sh '''
                echo "Zipping Lambda code..."
                zip -r lambda.zip lambda_function.py
                '''
            }
        }

        stage('Deploy Lambda') {
            steps {
                sh '''
                echo "Updating Lambda function..."
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
            echo "Deployment Successful 🚀"
        }
        failure {
            echo "Deployment Failed ❌"
        }
    }
}
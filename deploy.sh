#!/bin/sh

# full commands
account_id=$(aws sts get-caller-identity --output text --query 'Account') ## this will be the deployment account id
echo "Local Account Id is $account_id"

#-------------------------------------------------------------
#The application building and deployment
#-------------------------------------------------------------
cd $CODEBUILD_SRC_DIR
echo "Run dependencies installation"
echo "Run copy to S3 s3://mbition-webapp-demo.example.com"
aws s3 sync dist/ s3://mbition-webapp-demo.example.com --delete
echo "Clean up the cache for cloudfront"
aws cloudfront create-invalidation --distribution-id 'E2TDU4DXXIRA4F' --paths '/*'
echo "Deployment is done"

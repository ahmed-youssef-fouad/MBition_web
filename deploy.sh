#!/bin/sh

# full commands
account_id=$(aws sts get-caller-identity --output text --query 'Account') ## this will be the deployment account id
echo "Local Account Id is $account_id"

#-------------------------------------------------------------
#The application building and deployment
#-------------------------------------------------------------
echo "Run dependencies installation"
echo "Run copy to S3 s3://mbition-webapp-demo.example.com"
aws s3 sync dist/ s3://mbition-webapp-demo.example.com --delete
echo "Clean up the cache for cloudfront"
aws cloudfront create-invalidation --distribution-id 'E24ONXJL4X8F4W' --paths '/*'
echo "Deployment is done"

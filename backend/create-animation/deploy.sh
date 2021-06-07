#!/bin/bash

## Zip archive
rm lambdaCode.zip || true
zip -r lambdaCode.zip ./* --exclude 'deploy.sh' --exclude 'lambdaCode.zip'

## copy to s3
aws s3 cp lambdaCode.zip s3://200543/code/create-anim/lambdaCode.zip

## update function code
aws lambda update-function-code --function-name 200543__create-animation --s3-bucket 200543 --s3-key code/create-anim/lambdaCode.zip --publish
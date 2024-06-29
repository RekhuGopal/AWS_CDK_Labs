# AWS_CDK_Labs
This repo helps you to onboard to AWS CDK learning

## Install AWS CDK in Windows (npm is pre-requisites)
1. npm install -g aws-cdk
2. aws configure (AWS CLI)
2. cdk bootstrap aws://357171621133/us-west-2

## Commands AWS CDK
1. mkdir <project-name>
2. cd <project-name>
3. cdk init app --language python
4. cd .venv\Scripts
5. .\Activate.ps1
6. cd ..
6. pip install -r requirements.txt

## Deploy The Project.
1. cdk synth
2. cdk diff
3. cdk deploy

## Delete all resource
1. cdk destroy
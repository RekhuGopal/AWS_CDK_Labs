# AWS_CDK_Labs
This repo helps you to onboard to AWS CDK learning

## Install AWS CDK in Windows (npm is pre-requisites)
1. npm install -g aws-cdk
2. aws configure (AWS CLI)
2. cdk bootstrap aws://<AccountNumber>/<Region>

## Commands AWS CDK ( Run venv)
1. mkdir <project-name>
2. cd <project-name>
3. cdk init app --language python
4. cd .venv\Scripts
5. .\Activate.ps1
6. cd ..
7. pip install -r requirements.txt

## ## Commands AWS CDK ( Run without venv - provided you laptop has installed python "aws-cdk-lib" module )
1. mkdir <project-name>
2. cd <project-name>
3. cdk init app --language python
4. pip install -r requirements.txt

## Deploy The Project.
1. cdk synth
2. cdk diff
3. cdk deploy

## Delete all resource
1. cdk destroy
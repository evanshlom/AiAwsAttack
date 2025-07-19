# AiAwsAttack
ATTACK AI Agent projects with FAST FLEXIBLE dev+deploy cicd pipeline.

* Crew AI: Popular framework with 1 py file and 2 yml files for rapid config.
* AWS Bedrock: Titan-Express LLM as a starting point for agent crew.
* AWS Lambda: Quickly deploy a POC as one Lambda function and you can test it by invoking the Lambda function from AWS CLI or AWS Console. (For next steps: connect the Lambda function to an AWS API Gateway)

## Project Structure
```
content-crew/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── src/
│   ├── __init__.py
│   ├── crew.py
│   └── config/
│       ├── agents.yml
│       └── tasks.yml
├── main.py
├── lambda_handler.py
├── requirements.txt
└── .env
```

## Quick Start

### CICD Secrets
Add these to GitHub Actions Secrets before pushing the CICD pipe:
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* (The CICD yml file uses AWS Region us-east-1)

### Deploy to AWS Lambda
```bash
# First time: Create Lambda function
aws lambda create-function \
  --function-name content-strategy-crew \
  --runtime python3.11 \
  --role arn:aws:iam::YOUR_ACCOUNT:role/lambda-execution-role \
  --handler lambda_handler.lambda_handler \
  --timeout 300 \
  --memory-size 1024

# Deploy via GitHub Actions
git add .
git commit -m "Deploy"
git push origin main
```

### Test the Lambda Deployment
```bash
# Default topic
aws lambda invoke --function-name content-strategy-crew output.json

# Custom topic
aws lambda invoke \
  --function-name content-strategy-crew \
  --payload '{"topic": "Content for crypto VCs"}' \
  output.json

cat output.json
```

## Agentic Workflow

Three-agent workflow:
1. **Researcher**: Finds similar creators across platforms
2. **Analyzer**: Ranks platforms by opportunity
3. **Strategist**: Creates 30-day content plan

Stack: CrewAI + AWS Bedrock (Titan Express) + Lambda
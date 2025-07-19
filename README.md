# AiAwsAttack
ATTACK AI projects with FAST FLEXIBLE dev+deploy cicd pipeline.

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

### Local Development
```bash
# Clone and setup
git clone <repo>
cd content-crew
pip install -r requirements.txt

# Add AWS credentials
cp .env.example .env
# Edit .env with your credentials

# Run locally
python main.py
```

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

### Test Lambda
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

## Architecture

Three-agent workflow:
1. **Researcher**: Finds similar creators across platforms
2. **Analyzer**: Ranks platforms by opportunity
3. **Strategist**: Creates 30-day content plan

Stack: CrewAI + AWS Bedrock (Titan Express) + Lambda
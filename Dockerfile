FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt .
RUN pip install -r requirements.txt

# Install pysqlite3-binary to override system sqlite3 for lambda
RUN pip install pysqlite3-binary

COPY src/ ./src/
COPY lambda_handler.py .

# Set HOME to /tmp to avoid read-only filesystem errors
ENV HOME=/tmp

# Set the CMD to your handler
CMD ["lambda_handler.lambda_handler"]
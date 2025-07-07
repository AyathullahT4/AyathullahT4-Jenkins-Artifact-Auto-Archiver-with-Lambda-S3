# AyathullahT4-Jenkins-Artifact-Auto-Archiver-with-Lambda-S3
Automatically archive Jenkins build artifacts — specifically `build-log.txt` — to Amazon S3 using AWS Lambda. This project helps reduce disk usage on Jenkins servers by offloading older build logs to S3 for long-term retention.

📦 Tools & Concepts Covered:
| Tool           | Purpose                                       |
| -------------- | --------------------------------------------- |
| Jenkins        | CI/CD job runner                              |
| AWS Lambda     | Serverless script to automate archiving       |
| S3             | Object storage for long-term artifact backup  |
| EventBridge    | Scheduled trigger every 5 minutes             |
| Boto3 (Python) | AWS SDK used inside Lambda for S3 ops         |
| CloudWatch     | Logs & monitoring for Lambda invocations      |
| IAM            | Scoped permissions for Lambda and Jenkins EC2 |
| EC2            | Hosting Jenkins with minimal setup            |

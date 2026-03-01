# Serverless Feedback Management System

A production-style serverless web application that collects user feedback and provides an admin dashboard to view recent submissions.

Built using AWS managed services with a fully serverless architecture.

---

## 🚀 Architecture Overview

User → S3 Static Website → API Gateway → Lambda → DynamoDB

### AWS Services Used

- Amazon S3 – Static website hosting
- Amazon API Gateway – HTTP API
- AWS Lambda – Backend compute
- Amazon DynamoDB – NoSQL database
- CloudWatch – Monitoring & Logs
- IAM – Least privilege access control

---

## 🌍 Live Endpoints

### Frontend (S3 Website)
http://your-bucket-name.s3-website-region.amazonaws.com

### API Base URL
https://your-api-id.execute-api.region.amazonaws.com

### API Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /feedback | Create feedback |
| GET | /admin/feedback | List recent feedback |

---

## 🗄 DynamoDB Schema

**Table Name:** feedback

### Primary Key

| Attribute | Type | Key |
|------------|------|-----|
| feedbackId | String | Partition Key |

### Attributes Stored

- feedbackId (UUID)
- name (String)
- email (String)
- message (String)
- createdAt (ISO timestamp)

Billing Mode: On-Demand

---

## 📁 Project Structure


serverless-feedback-app/
│
├── backend/
│ ├── lambda_function.py
│ └── iam-policy.json
│
├── frontend/
│ ├── index.html
│ └── admin.html
│
└── README.md


---

## ⚙ Backend Details

### Lambda Function

Handles:
- POST /feedback
- GET /admin/feedback

Features:
- UUID generation
- Input validation
- CORS handling
- Stage-aware routing
- ISO timestamp storage

Environment Variable:

TABLE_NAME=feedback

---

## 🔐 IAM Policy

Least privilege permissions:

- dynamodb:PutItem
- dynamodb:Scan

Scoped only to the feedback table.

---

## 🌐 Frontend

### index.html
- Feedback submission form
- Sends POST request to API

### admin.html
- Displays recent 20 feedback entries
- Read-only dashboard

---

## 📊 Monitoring

- Lambda logs available in CloudWatch
- API Gateway execution logs enabled
- Error tracking via CloudWatch metrics

---

## 🔥 Optional Enhancements

- Cognito authentication for admin
- Pagination using LastEvaluatedKey
- GSI on createdAt
- Delete & Update endpoints (Full CRUD)
- CloudFront + Custom Domain + HTTPS
- Infrastructure as Code (Terraform / SAM)

---

## 🎯 Resume Description

Designed and deployed a serverless feedback collection system using AWS. Implemented RESTful APIs with Lambda and API Gateway, stored data in DynamoDB with least-privilege IAM policies, and hosted the frontend on S3 static website hosting. Enabled CORS handling and monitoring with CloudWatch for production readiness.

---

## 📌 Deployment Steps (Summary)

1. Create DynamoDB table
2. Create Lambda function and attach IAM policy
3. Configure API Gateway (HTTP API)
4. Enable CORS
5. Deploy S3 static website
6. Update frontend with API URL
7. Test application

---

## 🏗 Final Architecture Diagram

            ┌───────────────┐
            │   User        │
            └───────┬───────┘
                    │
                    ▼
            ┌───────────────┐
            │  S3 Website   │
            └───────┬───────┘
                    │
                    ▼
            ┌───────────────┐
            │ API Gateway   │
            └───────┬───────┘
                    │
                    ▼
            ┌───────────────┐
            │   Lambda      │
            └───────┬───────┘
                    │
                    ▼
            ┌───────────────┐
            │  DynamoDB     │
            └───────────────┘

---

## 📜 License

This project is for educational and portfolio purposes.

import json
import boto3
import uuid
from datetime import datetime
import os

# Initialize DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]
    path = event["rawPath"]

    # Remove stage name (like /prod) if present
    stage = event["requestContext"]["stage"]
    if path.startswith(f"/{stage}"):
        path = path[len(stage) + 1:]

    # -----------------------
    # CREATE FEEDBACK
    # -----------------------
    if method == "POST" and path == "/feedback":
        try:
            body = json.loads(event["body"])
        except Exception:
            return build_response(400, {"error": "Invalid JSON"})

        if not body.get("name") or not body.get("email") or not body.get("message"):
            return build_response(400, {"error": "All fields are required"})

        item = {
            "feedbackId": str(uuid.uuid4()),
            "name": body["name"],
            "email": body["email"],
            "message": body["message"],
            "createdAt": datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        return build_response(200, {"message": "Feedback saved successfully"})

    # -----------------------
    # LIST FEEDBACK (ADMIN)
    # -----------------------
    if method == "GET" and path == "/admin/feedback":

        response = table.scan(Limit=20)

        items = sorted(
            response.get("Items", []),
            key=lambda x: x["createdAt"],
            reverse=True
        )

        return build_response(200, items)

    # -----------------------
    # ROUTE NOT FOUND
    # -----------------------
    return build_response(404, {"error": "Route not found"})

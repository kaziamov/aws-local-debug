def lambda_handler(event, context):
    print(f"event: {event}\ncontext: {context}")

    response = {
        "status_code": 200,
        "body": "hello from lambda"
    }

    return response
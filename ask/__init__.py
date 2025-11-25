import json
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("RRSA Insight 'ask' function processed a request.")

    try:
        body = req.get_json()
    except ValueError:
        body = {}

    question = body.get("question")
    user_id = body.get("user_id")

    if question:
        answer = f"(stub) I received your question: '{question}'"
    else:
        answer = "No question was provided."

    response = {
        "answer": answer,
        "debug": {
            "handled_by": "stub",
            "user_id": user_id
        }
    }

    return func.HttpResponse(
        json.dumps(response),
        status_code=200,
        mimetype="application/json"
    )

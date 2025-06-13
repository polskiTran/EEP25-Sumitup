import base64
import json


def gmail_response_to_html(response_json: dict) -> str:
    html_body_data = None
    for part in response_json["payload"]["parts"]:
        if part["mimeType"] == "text/html":
            encoded_data = part["body"].get("data")
            if encoded_data:
                html_body_data = base64.urlsafe_b64decode(encoded_data).decode("utf-8")
            break
    return html_body_data


if __name__ == "__main__":
    # test gmail_response_to_html
    response_json = json.load(
        open("TEST_Newsletters/TLDR_AI_Jun_12.json", "r", encoding="utf-8")
    )
    html_body = gmail_response_to_html(response_json)
    print(html_body)

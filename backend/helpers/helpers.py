import base64
import json
from email.utils import parseaddr
from typing import Dict


def get_html_from_gmail_response(response_json: dict) -> str:
    """Get the html body from the gmail response

    Args:
        response_json (dict): The gmail response json

    Returns:
        str: The html body value
    """
    html_body_data = None
    for part in response_json["payload"]["parts"]:
        if part["mimeType"] == "text/html":
            encoded_data = part["body"].get("data")
            if encoded_data:
                html_body_data = base64.urlsafe_b64decode(encoded_data).decode("utf-8")
            break
    return html_body_data


def get_sender_from_gmail_response(response_json: dict) -> str:
    """Get the sender from the gmail response

    Args:
        response_json (dict): The gmail response json

    Returns:
        str: The sender value
    """
    for header in response_json["payload"]["headers"]:
        if header["name"] == "From":
            return header["value"]
    return None


def parse_sender(sender: str) -> Dict[str, str]:
    """Parse the sender from the gmail response
    Args:
        sender (str): The sender value

    Returns:
        Dict[str, str]: {"name": str, "email": str}
    """
    name, email = parseaddr(sender)
    return {"name": name, "email": email}


if __name__ == "__main__":
    # test get_html_from_gmail_response
    response_json = json.load(
        open("TEST_Newsletters/TLDR_AI_Jun_13.json", "r", encoding="utf-8")
    )
    # result = get_sender_from_gmail_response(response_json)
    # print(result)
    result = parse_sender(get_sender_from_gmail_response(response_json))
    print(result.get("name"))

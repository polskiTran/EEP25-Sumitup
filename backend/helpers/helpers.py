import base64
from datetime import datetime, timezone
from email.utils import parseaddr
from typing import Dict

from models.newsletter import Newsletter


def get_item_from_gmail_response(response_json: dict, item: str) -> str:
    """Get a specific item (html, sender, subject) from the gmail response

    Args:
        response_json (dict): The gmail response json
        item (str): The item to extract ('html', 'sender', 'subject')

    Returns:
        str: The requested value, or None if not found
    """
    if item == "html":
        raw_html = None
        for part in response_json.get("payload", {}).get("parts", []):
            if part.get("mimeType") == "text/html":
                encoded_data = part["body"].get("data")
                if encoded_data:
                    raw_html = base64.urlsafe_b64decode(encoded_data).decode("utf-8")
                break
        return raw_html
    elif item == "sender":
        for header in response_json.get("payload", {}).get("headers", []):
            if header.get("name") == "From":
                return header.get("value", None)
        return None
    elif item == "subject":
        for header in response_json.get("payload", {}).get("headers", []):
            if header.get("name") == "Subject":
                return header.get("value", None)
        return None
    elif item == "internal_date":
        return response_json.get("internalDate", None)
    elif item == "thread_id":
        return response_json.get("threadId", None)
    elif item == "history_id":
        return response_json.get("historyId", None)
    elif item == "id":
        return response_json.get("id", None)
    else:
        return None


def construct_sender_info(sender_info: Dict[str, str]) -> str:
    """Construct the sender info from the sender name and email
    Args:
        sender_name (str): The sender name
        sender_email (str): The sender email
    Returns:
        str: The sender info value
    """
    return f"{sender_info['name']} <{sender_info['email']}>" if sender_info else None


def parse_sender(sender: str) -> Dict[str, str]:
    """Parse the sender from the gmail response
    Args:
        sender (str): The sender value

    Returns:
        Dict[str, str]: {"name": str, "email": str}
    """
    name, email = parseaddr(sender)
    return {"name": name, "email": email}


def convert_internal_date_to_datetime(internal_date: int) -> datetime:
    """Convert the internal date to a datetime object
    Args:
        internal_date (int): The internal date value (milliseconds since epoch)
    Returns:
        datetime: The datetime object
    """
    internal_date_s = internal_date / 1000
    converted_date = datetime.fromtimestamp(internal_date_s, tz=timezone.utc)
    return converted_date.strftime("%Y-%m-%d %H:%M:%S UTC")


if __name__ == "__main__":
    # test convert_internal_date_to_datetime
    internal_date = 1749821410000
    print(convert_internal_date_to_datetime(internal_date))

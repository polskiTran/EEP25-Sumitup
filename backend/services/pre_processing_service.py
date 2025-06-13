import json

import requests
from bs4 import BeautifulSoup
from config import settings
from helpers.helpers import get_html_from_gmail_response


class HTMLToMarkdownConfig:
    BASE_URL = settings.html_md_converter_api_base_url
    TOKEN = settings.html_md_converter_api_token
    TIMEOUT = 30

    HEADERS = {"Content-Type": "application/json", "X-API-Key": TOKEN}


def get_html_body_from_gmail_response(response_json: dict) -> str:
    """Get the html body from the gmail response

    Args:
        response_json (dict): The gmail response json

    Returns:
        str: The html body value
    """
    html_body = get_html_from_gmail_response(response_json)
    soup = BeautifulSoup(html_body, "html.parser")
    return str(soup.find("body"))


def test_api_endpoint():
    """Test the api endpoint for html to markdown conversion"""
    gmail_response_file_path = f"TEST_Newsletters/{settings.test_newsletter_name}.json"

    response_json = json.load(open(gmail_response_file_path, "r", encoding="utf-8"))
    html_body = get_html_body_from_gmail_response(response_json)
    payload = {"html": html_body}
    # print(payload)

    response = requests.post(
        f"{HTMLToMarkdownConfig.BASE_URL}",
        json=payload,
        headers=HTMLToMarkdownConfig.HEADERS,
        timeout=30,
    )
    with open(
        f"TEST_Newsletters/responses/{settings.test_newsletter_name}_html_md_converter.json",
        "w",
        encoding="utf-8",
    ) as f:
        f.write(response.text)

    return response.status_code == 201
    # return True


if __name__ == "__main__":
    success = test_api_endpoint()
    print("✅ Test passed" if success else "❌ Test failed")

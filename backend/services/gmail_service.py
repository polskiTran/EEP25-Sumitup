import os
import os.path
from datetime import datetime

from config import settings
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from models.newsletter import Newsletter

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def gmail_authenticate():
    """Authenticate with the Gmail API and return the service."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)


async def fetch_and_process_latest():
    """Fetch the latest email from Gmail and process it (save + summarize)."""
    # In a real implementation, use Gmail API to fetch email:
    # e.g., service = build('gmail', 'v1', credentials=...)
    # message = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    # For now, this is a placeholder:
    newsletter_data = {
        "subject": "(demo) Latest Newsletter",
        "sender": "example@example.com",
        "body": "<p>Hello world</p>",
        "date": datetime.now().isoformat(),
    }
    # TODO: Save to DB and trigger summarization
    # from database import get_collection_names  # Use your actual DB functions
    print("Newsletter data processed:", newsletter_data)
    return newsletter_data


# region gmail api test functions ==============================================
# gmail ingestion test function
# def test_gmail_ingestion():
#     newsletter_data: Newsletter = Newsletter(
#         subject="(demo) Latest Newsletter",
#         sender="example@example.com",
#         body="<p>Hello world</p>",
#         date=datetime.now(),
#     )
#     return newsletter_data


# # gmail process test function
# async def test_gmail_process():
#     """Test function for isolated testing"""
#     print("Testing Gmail service...")

#     newsletter = test_gmail_ingestion()
#     # strip html tags from body
#     return newsletter


# # Test function that can be run independently
# async def test():
#     """Test function for isolated testing"""
#     print("Testing Gmail service...")

#     # Test 1: Create newsletter object
#     newsletter = test_gmail_ingestion()
#     print(f"✅ Newsletter created: {newsletter.subject}")

#     # Test 2: Process latest newsletter
#     result = await fetch_and_process_latest()
#     print(f"✅ Newsletter processed: {result}")


# def gmail_api_test():
#     """Shows basic usage of the Gmail API.
#     Lists the user's Gmail labels.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists("token.json"):
#         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open("token.json", "w") as token:
#             token.write(creds.to_json())

#     try:
#         # Call the Gmail API
#         service = build("gmail", "v1", credentials=creds)
#         results = service.users().labels().list(userId="me").execute()
#         labels = results.get("labels", [])

#         if not labels:
#             print("No labels found.")
#             return
#         print("Labels:")
#         for label in labels:
#             print(label["name"])

#     except HttpError as error:
#         # TODO(developer) - Handle errors from gmail API.
#         print(f"An error occurred: {error}")


# endregion

if __name__ == "__main__":
    import asyncio

    # gmail_api_test()
    # asyncio.run(test())
    service = gmail_authenticate()

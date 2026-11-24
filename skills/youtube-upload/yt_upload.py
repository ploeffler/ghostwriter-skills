"""Lädt ein Video über die YouTube Data API v3 hoch.

Benötigt: pip install google-api-python-client google-auth-oauthlib
Erwartet client_secret.json im aktuellen Ordner; speichert token.json dort.
"""
import argparse
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def auth():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w", encoding="utf-8") as f:
            f.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def main():
    p = argparse.ArgumentParser(description="Video auf YouTube hochladen")
    p.add_argument("video")
    p.add_argument("--title", required=True)
    p.add_argument("--description", default="")
    p.add_argument("--description-file")
    p.add_argument("--tags", default="")
    p.add_argument("--privacy", choices=["private", "unlisted", "public"], default="private")
    p.add_argument("--category", default="22")
    p.add_argument("--language", default="de")
    a = p.parse_args()

    desc = a.description
    if a.description_file:
        with open(a.description_file, encoding="utf-8") as f:
            desc = f.read()

    body = {
        "snippet": {
            "title": a.title[:100],
            "description": desc[:5000],
            "tags": [t.strip() for t in a.tags.split(",") if t.strip()],
            "categoryId": a.category,
            "defaultLanguage": a.language,
        },
        "status": {"privacyStatus": a.privacy, "selfDeclaredMadeForKids": False},
    }
    media = MediaFileUpload(a.video, chunksize=8 * 1024 * 1024, resumable=True)
    req = auth().videos().insert(part="snippet,status", body=body, media_body=media)

    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            print(f"{int(status.progress() * 100)} %")
    print("Fertig: https://youtu.be/" + resp["id"])


if __name__ == "__main__":
    main()

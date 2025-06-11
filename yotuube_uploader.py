
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def get_service():
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as f:
            creds = pickle.load(f)
    else:
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", GOOGLE)
        creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as f:
            pickle.dump(creds, f)

    return build("youtube", "v3", credentials=creds)

def uploader_video(video_path, titre, description):
    youtube = get_service()

    body = {
        "snippet": {
            "title": titre,
            "description": description,
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "private"
        }
    }

    media = MediaFileUpload(video_path)

    print("Envoi de la vidéo")
    req = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )
    res = req.execute()
    print(" Vidéo envoyée ! ID :", res["id"])

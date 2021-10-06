import os.path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def upload_to_gdrive(build_paths):
    builds = []
    for build_path in build_paths:
        url = _upload_file(build_path)
        name = os.path.basename(build_path)
        builds.append([name, url])
    return builds


def _upload_file(path):
    # https://www.youtube.com/watch?v=fNfr8WDbKCM
    gauth = GoogleAuth()
    if gauth.credentials is None:
        gauth.LoadCredentialsFile("mycreds.txt")
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds.txt")
    drive = GoogleDrive(gauth)

    drive_name = os.path.basename(path)
    file_settings = {"title": drive_name, "parents": [{"id": "1c5PD2dS706BSK_pCJr5eHip445nY-T9Q"}]}
    zip_file = drive.CreateFile(file_settings)
    zip_file.SetContentFile(path)
    zip_file.Upload({"convert": True})
    url = zip_file["alternateLink"]
    return url

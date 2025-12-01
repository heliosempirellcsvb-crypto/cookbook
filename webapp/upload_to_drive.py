from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Follow prompt for approval

drive = GoogleDrive(gauth)

WEBAPP_DIR = "./"
for root, dirs, files in os.walk(WEBAPP_DIR):
    for fname in files:
        fpath = os.path.join(root, fname)
        gfile = drive.CreateFile({'title': fname})
        gfile.SetContentFile(fpath)
        gfile.Upload()
        print(f"Uploaded {fname} to Google Drive.")

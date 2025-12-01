import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from datetime import datetime

# Set up Google Sheets API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client = gspread.authorize(creds)

# Open or create archive sheet
sheet = client.open("WebApp_Ledger_Archive").sheet1

# Scan files and append metadata
WEBAPP_DIR = "./"
for root, dirs, files in os.walk(WEBAPP_DIR):
    for fname in files:
        fpath = os.path.join(root, fname)
        ftype = os.path.splitext(fname)[1]
        mod_time = datetime.fromtimestamp(os.path.getmtime(fpath)).isoformat()
        sheet.append_row([fname, ftype, mod_time, fpath])
        print(f"Archived {fname} in Google Sheets ledger.")

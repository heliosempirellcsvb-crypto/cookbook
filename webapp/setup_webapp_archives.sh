#!/bin/bash
sudo apt update && sudo apt install -y python3-pip
pip3 install flask pydrive gspread oauth2client
echo "Ready to archive files to Google Drive and Google Sheets!"
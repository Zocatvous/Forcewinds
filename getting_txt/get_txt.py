#retrieve the list of files within the folder. Here's an example script that demonstrates how to iterate over all files in a specific folder:
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError
import os
from dotenv import load_dotenv



# Load environment variables
load_dotenv()
json_key_location = os.getenv('API_KEY_JSON_PATH')

# Set up Google Drive API credentials
credentials = service_account.Credentials.from_service_account_file(json_key_location, scopes=['https://www.googleapis.com/auth/drive.readonly'])

# Create a Google Drive API service
drive_service = build('drive', 'v3', credentials=credentials)
#docs_service = build('docs', 'v1', credentials=credentials)

# Define the folder ID of the target folder
# folder_id = 'My Drive'
folder_id = '1RyT2IS-dhGLCNcod_LVt246463PBR3bH'
kai_kan_files_id = '1w4ypR3y2RMRbU-4wtHR-4J8yk0w68bb-'
force_powers_files_id = '16u6WeIgoPY2sMNIrFWdgoSMDOMxJhZ7c'



# Retrieve the files in the specified folder
results = drive_service.files().list(q=f"'{force_powers_files_id}' in parents").execute()
# print(results)
files = results.get('files', [])
mime_type = 'text/plain'
# Iterate over the files
for file in files:
    print(f"File Name: {file['name']}")
    print(f"File ID: {file['id']}")
    if file['mimeType'] != 'application/vnd.google-apps.document':
        # Skip files that are not Google Docs files
        print("Skipping file. Not a Google Docs file.")
        continue
    request = drive_service.files().export_media(fileId=file['id'], mimeType='text/plain')
    response = request.execute()
    with open(f"./files/{file['name']}.txt", 'wb') as f:
    	downloader = MediaIoBaseDownload(f, request)
    	f.write(response)






























# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# # from google import create_service
# import requests
# import pprint

# import os

# forcewinds_folder_url = '1RyT2IS-dhGLCNcod_LVt246463PBR3bH'

# scopes_list = [
# 'https://www.googleapis.com/auth/drive.file',
# 'https://www.googleapis.com/auth/drive.appdata',
# 'https://www.googleapis.com/auth/drive.metadata',
# 'https://www.googleapis.com/auth/drive.metadata.readonly',
# 'https://www.googleapis.com/auth/drive.photos.readonly',
# 'https://www.googleapis.com/auth/drive.readonly'
# ]

# load_dotenv()
# api_key = os.getenv('JAKE_KEY')
# json_key_location = os.getenv('API_KEY_JSON_PATH')
# # Replace 'YOUR_JSON_FILE.json' with the path to your downloaded JSON credentials file
# credentials = service_account.Credentials.from_service_account_file(json_key_location, scopes=scopes_list)

# file_ids = ['1Bb3QLYXm12RagPs9aZ6Subd5FUjrvdcEGt4wP5lAfnI']

# # Create a Google Drive API service
# drive_service = build('drive', 'v3', credentials=credentials)
# #folder_name = 'Star Wars: The Forcewinds of Iloa'
# folder_name = '1RyT2IS-dhGLCNcod_LVt246463PBR3bH'
# #folder_name = 'https://docs.google.com/document/d/1Bb3QLYXm12RagPs9aZ6Subd5FUjrvdcEGt4wP5lAfnI/edit'

# results = drive_service.files().list(q=f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'").execute()
# folders = results.get('files', [])

# # Check if the folder was found and retrieve its ID
# if folders:
#     folder_id = folders[0]['id']
#     print(f"The folder ID for '{folder_name}' is: {folder_id}")
# else:
#     print(f"No folder found with the name '{folder_name}'")






















# # Replace 'DOCUMENT_ID' with the ID of your Google Doc
# document_id = 'DOCUMENT_ID'

# # API endpoint to fetch the document
# url = f'https://docs.googleapis.com/v1/documents/{document_id}'

# # # Make the API request
# response = requests.get(url, headers={'Authorization': f'Bearer {credentials.token}'})
# document = response.json()

# # pprint.pprint(document)
# input('did it work')


# # Extract the contents of the document
# content = ''
# for element in document['body']['content']:
#     if 'paragraph' in element:
#         for paragraph in element['paragraph']['elements']:
#             if 'textRun' in paragraph:
#                 content += paragraph['textRun']['content']

# # Save the contents to a text file
# with open('./output.txt', 'w', encoding='utf-8') as file:
#     file.write(content)

# print('Google Doc contents saved to output.txt')
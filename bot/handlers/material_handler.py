from aiogram import types
from aiogram.dispatcher import FSMContext
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'splendid-myth-419715-0316d98d2723.json'

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate using the service account
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Drive service
drive_service = build('drive', 'v3', credentials=creds)

# Folder IDs for Notes and PYQs for each subject in each semester
folder_ids = {
    'Computer Science': {
        '6th': {
            'Compiler Design': {
                'Notes': '1qGVdSxP5cJxyMjH9iEcIxJCplMlKo2yZ',
                'Previous Year Questions': '1lrSRHEUBo_tD6XWSP-sD67VDDHGl-Mux',
            },
            'CGIP': {
                'Notes': '13SK_U_Bf4lXh23P7Q-2kEPoa8VCfMRoj',
                'Previous Year Questions': '17HyhpT0pLA4ZJbEzQiQUP64P0rW21b-U',
            },
            'AAD': {
                'Notes': 'YOUR_AAD_NOTES_FOLDER_ID',
                'Previous Year Questions': 'YOUR_AAD_PYQ_FOLDER_ID',
            },
            'DCC': {
                'Notes': 'YOUR_DCC_NOTES_FOLDER_ID',
                'Previous Year Questions': 'YOUR_DCC_PYQ_FOLDER_ID',
            },
            'IEFT': {
                'Notes': 'YOUR_IEFT_NOTES_FOLDER_ID',
                'Previous Year Questions': 'YOUR_IEFT_PYQ_FOLDER_ID',
            },
        },
        # Add other semesters and subjects here
    },
    # Add other departments here
}

# Function to list files in a folder
def list_files_in_folder(folder_id):
    query = f"'{folder_id}' in parents"
    results = drive_service.files().list(q=query).execute()
    return results.get('files', [])

async def material_handler(message: types.Message, state: FSMContext):
    material_type = message.text
    await state.update_data(material_type=material_type)

    user_data = await state.get_data()
    department = user_data.get('department')
    semester = user_data.get('semester')
    subject = user_data.get('subject')
    material_type = user_data.get('material_type')

    folder_id = folder_ids.get(department, {}).get(semester, {}).get(subject, {}).get(material_type)
    if not folder_id:
        await message.reply("Sorry, the requested material type is not available.")
        return

    files = list_files_in_folder(folder_id)
    if not files:
        await message.reply("No files found for the selected material type.")
        return

    for file in files:
        file_id = file['id']
        file_name = file['name']
        file_url = f"https://drive.google.com/uc?export=download&id={file_id}"
        await message.reply(f"{file_name}\n[Download]({file_url})", parse_mode='Markdown')

    print(f"Material type selected: {material_type} for subject: {subject}, semester: {semester}, department: {department}")

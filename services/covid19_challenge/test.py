from apiclient.discovery import build
from apiclient.http import MediaFileUpload
import oauth2client
import httplib2

CLIENT_SECRET_FILE = 'client_secrets.json'
CREDENTIAL_FILE = 'credential.json'
APPLICATION_NAME = 'test'

SCOPES = 'https://www.googleapis.com/auth/drive' # Quickstarts と スコープを変える

store = oauth2client.file.Storage(CREDENTIAL_FILE)
creds = store.get()
if not creds or creds.invalid:
    flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    creds = oauth2client.tools.run_flow(flow, store)
drive_service = build('drive', 'v3', http=creds.authorize(httplib2.Http())) # Setup the Drive v3 API

file_metadata = {
    'name': 'My Report',
    'mimeType': 'application/vnd.google-apps.spreadsheet'
}
media = MediaFileUpload('out/sengen_vs_kansen_tokyo.csv',
                        mimetype='text/csv',
                        resumable=True)

file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
print 'File ID: %s' % file.get('id')
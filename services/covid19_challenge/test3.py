from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import gspread
import numpy as np

# authorize
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
gc = gspread.authorize(gauth.credentials)

# read csv
fname_csv = 'out/sengen_vs_kansen_tokyo.csv'
data = np.loadtxt(fname_csv, delimiter=',',dtype=np.str)

# make spreadsheet
folder_id = '1Txf3PMgCmMrIx5IqfKsAHhVtTqk1DFuq'
file_id = '1jUOVimIITkjuIrFfCx24fN8qkSeDlw3pw9tZftUU6oA'
f = drive.CreateFile({
    'title': 'sengen_vs_kansen_tokyo',
    'mimeType': 'application/vnd.google-apps.spreadsheet',
    "parents": [{"id": folder_id}],
    'id': file_id})
f.Upload()

# open spreadsheet
workbook = gc.open_by_key(f['id'])
worksheet = workbook.sheet1

# write spreadsheet
worksheet.update('A1',data.tolist())
tmp = data[1:,1:].astype(np.float)
tmp[np.isnan(tmp)] = 0
tmp[np.isinf(tmp)] = 0
worksheet.update('B2',tmp.tolist())


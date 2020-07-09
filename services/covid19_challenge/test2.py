import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiclient.http import MediaFileUpload

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

# upload covid-19 dataset
file_paths = ['csv/case_rikansyatoukei.csv','csv/case_rikansya.csv',
        'csv/relation_rikansyakankei.csv','csv/symptom_syoujou.csv']
file_ids = ['1fHFcyOFbVBfDThsopjsQ8r9cKWIkwCDF','1epFL_nJR3E7DZn3ZU6dAWuQERznco5c_',
        '1HLOQbfx-o70GKeq54ivef0cfMtvoziXf','1uTT8dpWWYBjzoAqzeIth3Hou2z4hsw8F']
for i, file_path in enumerate(file_paths):
    f = drive.CreateFile({'id': file_ids[i]})
    f.SetContentFile(file_path)
    f['title'] = os.path.basename(file_path)
    print('uploading...')
    f.Upload()

# upload sengen_vs_kansen_tokyo.py outputs
file_paths = ['out/sengen_vs_kansen_tokyo.csv','out/png/sengen_vs_kansen_tokyo.png']
file_ids = ['1bYGRA6pi0pTyz4X_D_C_skkmMgo1lFMe','16KvNqDR9Y7ilF0cknx26E3mhe5yAAe1y']
for i, file_path in enumerate(file_paths):
    f = drive.CreateFile({'id': file_ids[i]})
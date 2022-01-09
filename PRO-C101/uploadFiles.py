import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dir, files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root,file)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = "/"+file_to+"/" + relative_path
                print(dropbox_path)
                with open(file_from, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A_wUnl8957dH8HsHXpTvqgRBiUFb-jbvuZMD2Y-MflkAOkU7yqw5YrTdnqGs34PUjDviBhc_CNIq_pIvweA3YH6m26QjWEyY1upep9zCNEHN2_Jzrogo15gt23MlVo4qlwFY2-u-acLg'
    transferdata = TransferData(access_token)

    file_from = input("Enter Your file name: ")
    file_to = input("Enter the full path of your file: ")
    transferdata.upload_files(file_from, file_to)
    print("Files uploaded successfully!")

if __name__ == '__main__':
    main()
    
    # NOTICE: The access token has been revoked for safety issues. Please email me if you have any questions about dropbox access tokens in public repositories.

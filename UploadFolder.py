import dropbox

class TransferData:
    def __init(self, acess_token):
        self.acess_token = acess_token

    def upload_folder(self, folder_from, folder_to):
        self.acess_token = acess.token

    def upload_folder(self, folder_from, folder_to):
        dbx = dropbox.Dropbox(self.acess_token)
        
        for root,dirs,files in os.walk(folder_from, folder_to):
            relative_path = os.path.relpath(local_path, folder_from)
            dropox_path = os.path.join(folder_to, relative_path)

        with open(local_path, 'rb') as f:
            dbx.folders_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

    def main():
        acess_token = 'sl.A-YJpsSJCqYgnhu-3L9G-cCei-GlYMSmDpyFZgbufWO8t-BDaZApryl38SpiyfpOXt4WO2eNvHgtZiIpl9JmNity7tSKH6eOIvv0aP9fwtyaHISvCvOjNRS8DsOI16qh8htPV8Y'
        transferData = TransferData(acess_token)

        folder_from = input("Enter the file path to tranfer :-")
        folder_to = input("enter the full path to upload to dropbox:- ")

        transferData.upload_folder(folder_from, folder_to)
        print("Mission successfull")

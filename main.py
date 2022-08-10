from __future__ import print_function

import db
from APIDrive import api
from File import *


def main():
    print('Start Application')
    service = api()
    try:
        results = service.files().list(
            pageSize=1000, fields="nextPageToken, files(*)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('File:')
        for item in items:
            file = File(item['id'], item['name'], item['owners'][0]['emailAddress'], item['shared'],
                        item['modifiedTime'],
                        item['mimeType'])
            db.insertData(file)
        print('Arquivos inseridos na base de dados!')

        print('-=-=' * 100)
        print('Hist')
        for item in items:
            # id, name, owners, shared, modifiedTime, mimeType
            fileHist = File(item['id'], item['name'], item['owners'][0]['emailAddress'], item['shared'], None, None)
            if fileHist.shared is True:
                print(f'Name: {fileHist.name}')
                db.insertDataLog(fileHist)
                service.permissions().delete(fileId=fileHist.id, permissionId='anyoneWithLink').execute()




    except Exception as error:
        print(f'Error {error}')


if __name__ == '__main__':
    main()

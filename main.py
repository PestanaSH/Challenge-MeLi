from __future__ import print_function

import db
from APIDrive import api
from db import *
from File import *

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def main():
    print('Start Application')
    service = api()
    listFiles = []
    try:
        results = service.files().list(
            pageSize=1000, fields="nextPageToken, files(*)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('File:')
        for item in items:
            # file = [item['id'], item['name'], item['owners'][0]['emailAddress'], item['shared'], item['modifiedTime'],
            #         item['mimeType']]
            # print(file)
            file = File(item['id'], item['name'], item['owners'][0]['emailAddress'], item['shared'],
                        item['modifiedTime'],
                        item['mimeType'])
            db.insertData(file)

    except Exception as error:
        print(f'Error {error}')


if __name__ == '__main__':
    main()

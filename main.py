from __future__ import print_function

import base64
from email.message import EmailMessage

from APIDrive import api
from File import *
from db import Database


def send_email(file):
    # create gmail api client
    gmail = api('gmail')
    message = EmailMessage()

    msg = f'Prezado(a), por motivo de segurança, a visibilidade do arquivo "{file.name}" foi modificado.'
    message.set_content(msg)

    # headers
    message['To'] = file.owners
    message['From'] = 'lucas.challenge.meli@gmail.com'
    message['Subject'] = f'Documento Drive - {file.name}'

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {
        'raw': encoded_message
    }
    user = 'lucas.pestana.codigos@gmail.com'
    gmail.users().messages().send(userId=user, body=create_message).execute()
    print('Email enviado!')


def main():
    print('Start Application')
    service = api('drive')
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
            Database.insertData(file)
        print('Arquivos inseridos na base de dados!')

        print('-=-=' * 100)
        print('Hist')
        for item in items:
            # id, name, owners, shared, modifiedTime, mimeType
            fileHist = File(item['id'], item['name'], item['owners'][0]['emailAddress'], item['shared'], None, None)
            if fileHist.shared is True:
                print(f'Name: {fileHist.name}')
                Database.insertDataLog(fileHist)
                service.permissions().delete(fileId=fileHist.id, permissionId='anyoneWithLink').execute()
                send_email(fileHist)




    except Exception as error:
        print(f'Error {error}')


if __name__ == '__main__':
    main()

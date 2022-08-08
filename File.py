# item['id'], item['name'], item['owners'][0]['emailAddress'], item['shared'], item['modifiedTime'],
#                     item['mimeType']]

class File():
    def __init__(self, id, name, owners, shared, modifiedTime, mimeType):
        self.id = id
        self.name = name
        self.owners = owners
        self.shared = shared
        self.modifiedTime = modifiedTime
        self.mimeType = mimeType

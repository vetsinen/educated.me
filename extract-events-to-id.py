import facebook
token = "EAAJso34oskUBABKMARfHCVpnI8FolDm9ViKOuF7w8tn5ZC4c0kjTfh5e8GBNwlEv5hLGODsMy60uagQdi9ZCwPMwfJYdCSkSPEEZCF5sxvyOZBdEWE19stM3ZC1eLZBkRVCFJpTAO5UpOOrk8cxS13tA9ZBy8dIlpZBAAR4dYCyX2gKtOKumCzyiQCarkEevVkURZA6OoH7rPjAZDZD"
userid = "162568371295069"
graph = facebook.GraphAPI(access_token=token, version="2.12")
rez = graph.get_all_connections(id=userid, connection_name='events')

# https://github.com/patx/pickledb
import pickledb
db = pickledb.load('fbevents.db', False)
l=0
for event in rez:
    db.set(event["id"],event)
    l=l+1

db.dump()
print(l)

db = pickledb.load('fbevents.db', False)
print(len(db.getall()))

import facebook
token = "EAAJso34oskUBABKMARfHCVpnI8FolDm9ViKOuF7w8tn5ZC4c0kjTfh5e8GBNwlEv5hLGODsMy60uagQdi9ZCwPMwfJYdCSkSPEEZCF5sxvyOZBdEWE19stM3ZC1eLZBkRVCFJpTAO5UpOOrk8cxS13tA9ZBy8dIlpZBAAR4dYCyX2gKtOKumCzyiQCarkEevVkURZA6OoH7rPjAZDZD"
userid = "162568371295069"
graph = facebook.GraphAPI(access_token=token, version="2.12")
rez = graph.get_all_connections(id=userid, connection_name='events')

# https://github.com/patx/pickledb
import pickledb
db = pickledb.load('dated-events.db', False)
l=0
datedevents = {}
for event in rez:
    datestr = event['start_time'][:10]
    if datestr not in datedevents:
        datedevents[datestr]=[]
    datedevents[datestr].append(event)
    l=l+1


print(str(l)+ " events were extracted")
for date in datedevents.keys():
    db.set(date, datedevents[date])
db.dump()


# db.dump()
# print(l)
#
# db = pickledb.load('fbevents.db', False)
# print(len(db.getall()))

import facebook
token = "EAAeZATMPe23sBAFdpzjIh0fQBIxuW4HEEUiSt0zbQTBdrZAwWK3gTZBEK8lAGnG83v9QISN4FLPETGrTIyetNjxg96GTjwpD1AoI4dyDjc9CanirhhR0rYzupWHPKtZAPRhPC496n9ZBUE1NQgZCkyoJhjsvBn9PlssLZBX3aGZAGxz0kZCpBZCIjSr4ZBE1mU8fPLzP7hZCSovNvQZDZD"
userid = "166974190854487"#sl "10155705847047361"#vm
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

import facebook
token = "EAAeZATMPe23sBAGLuC9hgWdYsTTrt23hL8CmLsZA3YJ2hje4FShZAilMZCokRX8plaoxC4Y5uw41RZAwei0YSp6ndYSjFW0Q8CZCbJu7YvLmsLoZA0n9gARHz4k0E47QSjfaTYVRHFB5Ii6RZBd8QsXLarujEtBrnl3dkYcZBF0mGwTT5M7C3CDJZCEIUGtStSRFqtnN0JsVXzWwZDZD"
userid = "166974190854487"
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

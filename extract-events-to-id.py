import facebook
token = "EAAeZATMPe23sBACuwoo2SDIKazXwRQAllcRDCrzpe9xGAQ753EEWEYE2V878OVekqj0Y7sLZC0DBwqKypTwKUq8aCZCAVWrsmlspLeRVCCH2ynZA6aAT0TRRmZB1yENy8NZCmFS2WF7xkCMx71ZAZBAPSCZCvp2XxurhifnFL4aPLHhZAr1B2nurmXloJNpzAsFe4jZBBy1iyPt9wZDZD"
userid =  "166974190854487"#sl "10155705847047361"#vm
graph = facebook.GraphAPI(access_token=token, version="2.12")
rez = graph.get_all_connections(id=userid, connection_name='events')
from mstore import events

# https://github.com/patx/pickledb
l=0
for event in rez:
    l=l+1
    event['_id']=event["id"]
    events.insert(event)

print('inserted: '+str(l))

# db = pickledb.load('fbevents.db', False)
# print(len(db.getall()))

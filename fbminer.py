# import http.client
# conn = http.client.HTTPSConnection("www.python.org")
# conn.request("GET", "/")
# r1 = conn.getresponse()
# data1 = r1.read()

# fb-library https://github.com/mobolic/facebook-sdk
import facebook
token = "EAAJso34oskUBAPGHIX8L9rMYT8IqFiW4HTUtp5HkRQs8AirYZCOuT346cZClw6iIvTtXgvxXEC5rwLgVK21bRCigUhIwguZAyixpfdpTOpQmkPrbVTuMN2xUgDIzmsgGYRbeh2gLEPZAPyAA1qq2lSVFZAzYP0RKa4u77AGNuuo9b6j4RZC2U0wzq58JvAOrcirjg4VQ59cAZDZD"
userid = "162568371295069"
graph = facebook.GraphAPI(access_token=token, version="2.12")
rez = graph.get_all_connections(id=userid, connection_name='events')
print(rez)

# https://github.com/patx/pickledb
import pickledb
db = pickledb.load('fbevents.db', False)

for event in rez:
    db.set(event["id"],event)

db.dump()

db = pickledb.load('fbevents.db', False)
print(len(db.getall()))
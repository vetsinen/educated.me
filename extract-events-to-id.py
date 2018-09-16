import facebook
token = "EAAJso34oskUBALjfNiudGDQnus2TitLGlFtiSZCPgzKEaZC5qpvq5JWN4mzdtRrECjHcr54MjOaZCTg3Ar1hl16cbIHdh12g5LpTvm7kFgJvP6UnDMdUeFaU2TjCBtQwPGaZAzIOODg8ZC7wMT5q3fDbE2Ifs5Ex17pTMNzDgdM5o2cCZCCIVDTzHeZCMTOti85Y6Ye9BTu3QZDZD"
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

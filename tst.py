from mstore import events
from pprint import pprint


events.insert( {"_id":"435475535325235235", "name": "John", "address": "Highway 37" })

for x in events.find():
    pprint(x)

# import pickledb
# db = pickledb.load('dated-events.db', False)
# print(len(db.getall()))
#
# for date in db.getall():
#     print(len(db.get(date)))

# i=0
# for evid in db.getall():
#     print(db.get(evid)['description'])
#     i=i+1
#     if i>20:
#         exit()
# #print(len(db.getall()[:20]))
#
# from datetime import datetime
# a={"key":"value"}
# print(type(a))
# sd00 = '2018-12-02T15:00:00+0200'
# print(sd00[:10])
# print(datetime.strptime(sd00[:10],'%Y-%m-%d').date())
# d00 = datetime.strptime(sd00[:10],'%Y-%m-%d')
# d00 = d00.date()
# print(type(d00))
#
# import pickledb
# db = pickledb.load('fbevents.db', False)
#
# es = db.getall()
# print(len(es))
#
#
# i=0
# for k in es:
#     ev = db.get(k)
#     print(ev['start_time'])
#     i=i+1
#     if i>5:
#         exit()
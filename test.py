import pickledb
db = pickledb.load('fbevents.db', False)
print(len(db.getall()))

i=0
for evid in db.getall():
    print(db.get(evid)['description'])
    i=i+1
    if i>20:
        exit()
#print(len(db.getall()[:20]))
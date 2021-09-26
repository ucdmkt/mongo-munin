
def getDatabasesStats():
    c = getClient()

    dbs = {}
    for k in c.database_names():
        if k != "admin" and k != "local" and k != "":
            db = c[k]
            dbs[k] = {}
            for coll in db.collection_names():
                if '.' not in coll:
                    dbs[k][coll] = db[coll].count()

    return dbs

name = "documents"


def doData():
    ss = getDatabasesStats()
    import six
    for k,v in six.iteritems(ss):
        for a,b in six.iteritems(v):
            print(str(k)+str(a) + ".value " + str(b))


def doConfig():

    print("graph_title MongoDB documents count")
    print("graph_args --base 1000 -l 0 --vertical-label Docs")
    print("graph_category MongoDB")

    ss = getDatabasesStats()
    import six
    for k,v in six.iteritems(ss):
        for a,b in six.iteritems(v):
            print(str(k)+str(a) + ".label " + str(k) + " " + str(a))
            print(str(k)+str(a) + ".draw LINE1")

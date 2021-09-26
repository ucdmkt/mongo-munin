
def get():
    return getServerStatus()["indexCounters"]

def doData():
    import six
    for k,v in six.iteritems(get()):
        print( str(k) + ".value " + str(int(v)) )

def doConfig():

    print("graph_title MongoDB btree stats")
    print("graph_args --base 1000 -l 0")
    print("graph_vlabel mb ${graph_period}")
    print("graph_category MongoDB")

    for k in get():
        print(k + ".label " + k)
        print(k + ".min 0")
        print(k + ".type COUNTER")
        print(k + ".max 500000")
        print(k + ".draw LINE1")

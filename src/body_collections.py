import re
FIELD_ESCAPE = re.compile("[^A-Za-z_]")


def escape_field(name):
    return FIELD_ESCAPE.sub("_", name)


def need_multigraph():
    if 'MUNIN_CAP_MULTIGRAPH' not in os.environ:
        sys.stderr.write('MUNIN_CAP_MULTIGRAPH not found in environment\n')
        sys.exit(1)


def collections(include_stats=False):
    c = getClient()
    for db in c.database_names():
        for collection in c[db].collection_names():
            name = db + "." + collection
            if include_stats:
                yield name, c[db].command("collstats", collection)
            else:
                yield name


def doData():
    need_multigraph()
    data = list(collections(True))

    print("multigraph collection_count")
    for name, stats in data:
        print(escape_field(name) + ".value " + str(stats["count"]))

    print("multigraph collection_size")
    for name, stats in data:
        print(escape_field(name) + ".value " + str(stats["size"]))


def doConfig():
    need_multigraph()
    names = list(collections())

    print("multigraph collection_count")
    print("graph_title MongoDB collection document count")
    print("graph_args --base 1000 -l 0")
    print("graph_vlabel collection document count")
    print("graph_category MongoDB")
    print("graph_total total")

    for name in names:
        field_name = escape_field(name)
        print(field_name + ".label " + name)
        print(field_name + ".min 0")
        print(field_name + ".type GAUGE")
        print(field_name + ".draw LINE1")

    print("multigraph collection_size")
    print("graph_title MongoDB collection size")
    print("graph_args --base 1024 -l 0")
    print("graph_vlabel collection size")
    print("graph_category MongoDB")
    print("graph_total total")

    for name in names:
        field_name = escape_field(name)
        print(field_name + ".label " + name)
        print(field_name + ".min 0")
        print(field_name + ".type GAUGE")
        print(field_name + ".draw LINE1")

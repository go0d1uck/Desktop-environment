import psutil


def getID():
    return psutil.pids()


def getStatus():
    ids = getID()
    result = []
    for pId in ids:
        p = psutil.Process(pId)
        tup = (pId, p.name(), p.status(), p.memory_percent(), p.num_threads(), p.create_time())
        result.append(tup)
    return result

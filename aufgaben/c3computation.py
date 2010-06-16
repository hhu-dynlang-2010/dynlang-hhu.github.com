def compute_C3_mro(w_obj):
    order_w = []
    parents_w = w_obj.getparents()
    orderlists = [w_base.get_mro()
            for w_base in parents_w]
    orderlists.append([w_obj] + parents_w)
    while orderlists:
        for candidatelist in orderlists:
            w_candidate = candidatelist[0]
            if mro_blockinglist(w_candidate, orderlists) is None:
                break    # good w_candidate
        else:
            return mro_error(orderlists)  # no candidate found
        assert w_candidate not in order_w
        order_w.append(w_candidate)
        for i in range(len(orderlists)-1, -1, -1):
            if orderlists[i][0] is w_candidate:
                del orderlists[i][0]
                if len(orderlists[i]) == 0:
                    del orderlists[i]
    return order_w


def mro_blockinglist(w_candidate, orderlists):
    for lst in orderlists:
        if w_candidate in lst[1:]:
            return lst
    return None # good candidate

def mro_error(orderlists):
    # w_obj.getname() is a pure debugging-helper. it can return whatever string
    cycle = []
    w_candidate = orderlists[-1][0]
    if w_candidate in orderlists[-1][1:]:
        # explicit error message for this specific case
        raise TypeError("duplicate parent %s" % w_candidate.getname())
    while w_candidate not in cycle:
        cycle.append(w_candidate)
        nextblockinglist = mro_blockinglist(w_candidate, orderlists)
        w_candidate = nextblockinglist[0]
    del cycle[:cycle.index(w_candidate)]
    cycle.append(w_candidate)
    cycle.reverse()
    names = [w_obj.getname() for w_obj in cycle]
    raise TypeError("cycle among base parents: " + ' < '.join(names))


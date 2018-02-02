import pprint

def stringsRearrangement(i):

    def createGraph(i):
        tree = dict()
        l = len(i)
        x = 0
        while x < l:
            v = i[x]
            vals = []
            for ev in i:
                if ev == v:
                    continue
                else:
                    if sum(1 for a, b in zip(v, ev) if a != b) == 1:
                        vals.append(ev)
                    else:
                        continue
            tree.update({v: vals})
            x += 1
        for key, val in tree.items():
            if len(val) > 0:
                continue
            else:
                return False
        pprint.pprint (tree)
        return tree

    createGraph(i)

test1 = ["abc", "abc", "acc", "acc", "azc"]

stringsRearrangement(test1)

# TODO
# 1) mod to deal with duplicates; test1 yeilds 3 entries instead of 5
# 2) modularize this into a graph utility
# 3) create the analysis function to solve for the codefight 'Strings Rearrangement'
#   a) easy! look for any dict entries that have the same length as the input - 1
#   b) then use same logic from SA_perms to test

#####################################################
# Current state: just creates a vertice:[edges] dict from a set of inputs (that's handy!)
#####################################################

# just for preso purposes
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

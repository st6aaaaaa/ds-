
from binarytree import build
import math
def isvalid(node,low=-math.inf,high=math.inf):
    if not node :
        return True
    if node.val <= low or node.val >= high:
        return False

    return isvalid(node.left,low,node.val) and isvalid(node.right,node.val,high)

nodes = [40,30,50,10,35,39]
bin_tree = build(nodes)

r = isvalid(bin_tree)
print(r)
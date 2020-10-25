import xml.etree.ElementTree as etree

maxdepth = -1
def depth(e, l):
    global maxdepth
    if (l == maxdepth):
        maxdepth += 1
    for c in e:
        depth(c, l + 1)
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
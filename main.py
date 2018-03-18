import DecisionTree

def main():
    
    file = open('train6.csv')
    target = "Class"
    #print(target)
    data = [[]]
    for line in file:
        line = line.strip("\r\n")
        data.append(line.split(','))
    #print(data)
    data.remove([])
   # print(data)
    attributes = data[0]
    data.remove(attributes)
    types = data[1]
    data.remove(types)
   ## print(attributes)
    tree = DecisionTree.makeTree(data, attributes, target, 0)
    print "generated decision tree"
    file = open('program.py', 'w')
    file.write("import Node\n\n")
    file.write("data = [[]]\n")
    file.write("f = open('test6_6.csv')\n")#without class
    file.write("for line in f:\n\tline = line.strip(\"\\r\\n\")\n\tdata.append(line.split(','))\n")
    file.write("data.remove([])\n")
    file.write("attributes = data[0]\n")
    file.write("types = data[1]\n")
    file.write("data.remove(attributes)\n")
    file.write("data.remove(types)\n")
    file.write("data1 = [[]]\n")
    file.write("f = open('test6.csv')\n")#withclass
    file.write("for line in f:\n\tline = line.strip(\"\\r\\n\")\n\tdata1.append(line.split(','))\n")
    file.write("data1.remove([])\n")
    file.write("attributes1 = data1[0]\n")
    file.write("types1 = data1[1]\n")
    file.write("data1.remove(attributes1)\n")
    file.write("data1.remove(types1)\n")
    file.write("tree = %s\n" % str(tree))
    file.write("attributes = %s\n" % str(attributes))
    file.write("count = 0\n")
    file.write("c = 0\n")
    file.write("result2=[[]]\n")
    file.write("for line in data1:\n\tresult2.append(line[-1])\n")    
    file.write("for entry in data:\n")
    file.write("\tcount += 1\n")
    file.write("\ttempDict = tree.copy()\n")
    file.write("\tresult = \"\"\n")
    file.write("\twhile(isinstance(tempDict, dict)):\n")
    file.write("\t\troot = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])\n")
    file.write("\t\ttempDict = tempDict[tempDict.keys()[0]]\n")
    file.write("\t\tindex = attributes.index(root.value)\n")
    file.write("\t\tvalue = entry[index]\n")
    file.write("\t\tif(value in tempDict.keys()):\n")
    file.write("\t\t\tchild = Node.Node(value, tempDict[value])\n")
    file.write("\t\t\tresult = tempDict[value]\n")
    file.write("\t\t\ttempDict = tempDict[value]\n")
    file.write("\t\telse:\n")
    file.write("\t\t\tprint \"can't process input %s\" % count\n")
    file.write("\t\t\tresult = \"?\"\n")
    file.write("\t\t\tbreak\n")
    file.write("\tprint (\"entry%s = %s\" % (count, result))\n")
    file.write("\td=int(count)\n")
    file.write("\tif result2[d] == result:\n\t\tc += 1\n")   
    file.write("print (\"Number of correct estimation = %s\" % c)\nprint (\"Total estimation = %s\" % count)\n")
    file.write("acc=0\n")
    file.write("acc=(float(c)/count)*100\nprint (\"accuracy= %s\" % (acc) )") 
    print "written program"

if __name__ == '__main__':
    main()


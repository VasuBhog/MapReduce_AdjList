#!/usr/bin/env python
"""reducer.py"""

import sys
import os
import copy 

dagL = {}


#Helper Functions

#EX. ADJ LIST
#{'1': ['2', '5', '7', '8', '9', '11', '17', '254913', '438238'],
#{'2': [1],'5': [1]}

#Get Undirected graph
def undirected(d):
    inv = copy.deepcopy(d)
    for key in d:
        #get values from dict
        # print(d[key])
        for item in d[key]:
            #Get each item
            # print(item)
            if item not in inv:
                #create new list
                inv[item] = [key]
            else:
                inv[item].append(key)
    return inv

#Get Max Key
def maxKey(d):
    max_key = max(d, key = lambda x: len(set(d[x])))
    return max_key

#Get Lengths of Dict
def lengthDict(d):
    lengths = [len(v) for v in d.values()]
    # min_key = min(d, key = lambda x: len(set(d[x])))
    return lengths

#Get Min Key
def minKey(length, dict):
    minlen = min(length)
    minIndex = length.index(minlen)
    x = dict.keys()
    min_key = list(x)[0]
    return min_key


#Create Result File
def resultFile():
    path = os.getcwd()
    f = open(os.path.join(path,"result.txt"),"w+")
    f.close()
    return f

#Program Starts here
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, val = line.split('\t', 1)
    if key not in dagL:
        dagL[key] = [val]
    else:
        tmp = dagL[key]
        tmp.append(val)
        dagL[key] = tmp


d = dagL
#Convert Directed Graph to Undirected 
unD = undirected(dagL)

#ADJ Lists
# print("\nDirected Graph: \n" + str(d))
# print("\nUndirected Graph: \n" + str(unD))

#Begin Writing to Result File
# resultFile()

# f = open("result.txt",'a+')

#### OUTPUTS ###

##Directed ---

#Longest Adj List
maxkeyD = maxKey(d)
valD = d.get(maxkeyD)

#Min
lenD = lengthDict(d)
minkeyD = minKey(lenD,d)
# f.write("\nLongest Adj List for Directed Graph: \n" + str(maxkeyD) + ":" + str(valD))

# #Max and Min Node
# f.write("\n\nDirected Graph --- \nNode with Max Connectivity: " + str(maxkeyD))
# f.write("\nNode with Min Connectivity: " + str(minkeyD))

##Undirected ----

#Longest Adj List
maxkeyUND = maxKey(unD)
valUND = d.get(maxkeyUND)
# f.write("\n\nLongest Adj List for Undirected Graph: \n" + str(maxkeyUND) + ":" + str(valUND))

#Min
lenUND = lengthDict(unD)
minkeyUND = minKey(lenUND,unD)

# #Max and Min Node
# f.write("\n\nUndirected Graph --- \nNode with Max Connectivity: " + str(maxkeyUND))
# f.write("\nNode with Min Connectivity: " + str(minkeyUND))

#For Number of Connections 
maxConD = d.keys().index(maxkeyD)
minConD = d.keys().index(minkeyD)
maxConUND = unD.keys().index(maxkeyUND)
minConUND = unD.keys().index(minkeyUND)

#Print
print("\nLongest Adj List for Directed Graph: \n" + str(maxkeyD) + ":" + str(valD))
print("\nDirected Graph Analysis --- ")

print("\nNode with Max Connectivity: " + str(maxkeyD))
print("Number of Connections: " + str(lenD[maxConD]))

print("\nNode with Min Connectivity: " + str(minkeyD))
print("Number of Connections: " + str(lenD[minConD]))

print("\n\nLongest Adj List for Undirected Graph: \n" + str(maxkeyUND) + ":" + str(valUND))
print("\nUndirected Graph Analysis ---")

print("\nNode with Max Connectivity: " + str(maxkeyUND))
print("Number of Connections: " + str(lenUND[maxConUND]))
 
print("\nNode with Min Connectivity: " + str(minkeyUND))
print("Number of Connections: " + str(lenUND[minConUND]) + "\n")

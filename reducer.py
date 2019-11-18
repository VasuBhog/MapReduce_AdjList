#!/usr/bin/env python
"""reducer.py"""

#Vasu Bhog
import sys
import copy 

dagL = {}


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
            #take out duplicates
            if item not in inv:
                #create new list
                inv[item] = [key]
            else:
                inv[item].append(key)
    return inv

#Get Max Key
def maxKey(d):
    max_key = max(d, key = lambda x: len(d[x]))
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
    min_key = list(x)[minIndex]
    return min_key


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
        if val not in dagL[key]:
            dagL[key].append(val)
        else: 
            pass


d = dagL
#Convert Directed Graph to Undirected 
unD = undirected(dagL)

#ADJ Lists
# print("\nDirected Graph: \n" + str(d))
# print("\nUndirected Graph: \n" + str(unD))

#### OUTPUTS ###

##Directed ---

#Longest Directed Adj List
maxkeyD = maxKey(d)
valD = d[maxkeyD]

#Min
lenD = lengthDict(d)
minkeyD = minKey(lenD,d)


##Undirected ----

#Longest Undirected Adj List
maxkeyUND = maxKey(unD)
valUND = unD[maxkeyUND]

#Min
lenUND = lengthDict(unD)
minkeyUND = minKey(lenUND,unD)

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
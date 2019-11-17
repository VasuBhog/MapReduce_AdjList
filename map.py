import copy 

def openFile():
    dagL = {}
    with open('sample.txt','r') as f:
        for line in f:
            if line[0] == '#':
                pass
            else:
                x = line.split()
                #Reduce Noise (list needs two pairs)
                #Drop values that do not have two edges (ex. _ 2)
                if len(x) == 1:
                    pass
                else:
                    key = x[0]
                    val = x[1]
                    if key not in dagL:
                        dagL[key] = [val]
                    else:
                        tmp = dagL[key]
                        tmp.append(val)
                        dagL[key] = tmp
    return dagL

#EX. ADJ LIST
#{'1': ['2', '5', '7', '8', '9', '11', '17', '254913', '438238'],
#{'2': [1],'5': [1]}
def undirected(d):
    inv = copy.deepcopy(d)
    print(inv)
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

def maxKey(d):
    max_key = max(d, key = lambda x: len(d[x]))
    return max_key

def lengthDict(d):
    lengths = [len(v) for v in d.values()]
    return lengths

def minKey(length, dict):
    minlen = min(length)
    minIndex = length.index(minlen)
    x = dict.keys()
    min_key = list(x)[0]
    return min_key


#Create Result File
def resultFile():
    f = open("result.txt","w+")
    f.close()
    return f


#MAIN FILE
if __name__ == '__main__':
    #Directed Graph = d
    d = openFile()

    #Convert Directed Graph to Undirected 
    unD = undirected(d)

    #ADJ Lists
    # print("\nDirected Graph: \n" + str(d))
    # print("\nUndirected Graph: \n" + str(unD))

    #Begin Writing to Result File
    resultFile()
    f = open("result.txt",'a+')

    #### OUTPUTS ###

    ##Directed ---

    #Longest Adj List
    maxkeyD = maxKey(d)
    valD = d.get(maxkeyD)

    #Min
    lenD = lengthDict(d)
    minkeyD = minKey(lenD,d)
    f.write("Longest Adj List for Directed Graph: \n" + str(maxkeyD) + ":" + str(valD))

    # #Max and Min Node
    f.write("\n\nDirected Graph --- \nNode with Max Connectivity: " + str(maxkeyD))
    f.write("\nNode with Min Connectivity: " + str(minkeyD))
    

    ##Undirected ----

    #Longest Adj List
    maxkeyUND = maxKey(unD)
    valUND = d.get(maxkeyUND)
    f.write("\n\nLongest Adj List for Undirected Graph: \n" + str(maxkeyUND) + ":" + str(valUND))

    #Min
    lenUND = lengthDict(unD)
    minkeyUND = minKey(lenUND,unD)

    # #Max and Min Node
    f.write("\n\nUndirected Graph --- \nNode with Max Connectivity: " + str(maxkeyUND))
    f.write("\nNode with Min Connectivity: " + str(minkeyUND))

    #PRINTING to CONSOLE
    print("Longest Adj List for Directed Graph: \n" + str(maxkeyD) + ":" + str(valD))
    print("\n\nDirected Graph --- \nNode with Max Connectivity: " + str(maxkeyD))
    print("\nNode with Min Connectivity: " + str(minkeyD))
    print("\n\nLongest Adj List for Undirected Graph: \n" + str(maxkeyUND) + ":" + str(valUND))
    print("\n\nUndirected Graph --- \nNode with Max Connectivity: " + str(maxkeyUND))
    print("\nNode with Min Connectivity: " + str(minkeyUND))

#hadoop jar /usr/hdp/3.0.0.0-1634/hadoop-mapreduce//hadoop-streaming.jar -file /home/bhogvu/mapper.py -mapper /home/bhogvu/mapper.py -file /home/bhogvu/reducer.py -reducer /home/bhogvu/reducer.py -input /user/bhogvu/project2/web-BerkStan.txt -output /user/bhogvu/output

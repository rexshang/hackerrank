'''
Created on Nov 16, 2016

@author: erexsha
'''

from Queue import Queue

class Node(object):

    def __init__(self, id):
        self.path = {}
        self.id = id
        
    def __str__(self):
        return "ID: " + str(self.id) + ", Path: " + str(self.path) + ";"
    
    def __repr__(self):
        return "ID: " + str(self.id) + ", Path: " + str(self.path) + ";"
        
    def addPath(self, conn, weight):
        self.path[conn] = weight
        
    def getPath(self):
        return self.path
    
    def getWeight(self, conn):
        return self.path[conn]
    
node_list = {}

    
def findPath(top):
    global node_list

    que = Queue()
    costs = {top: 0}
    
    que.put(top)
    while not que.empty():
        currentNode = que.get()
        for nextNode in node_list[currentNode].getPath():
            if nextNode in costs:
                continue
            else:
                costs[nextNode] = costs[currentNode] + node_list[currentNode].getWeight(nextNode)
                que.put(nextNode)
         
    return costs

def main():
    global node_list
    tc = int(raw_input().strip())
    
    for testcase in range(tc):
    
        nodes, edges = map(int, raw_input().strip().split(' '))
        
        for i in range(1, nodes + 1):
            node_list[i] = Node(i)
            
        for i in range(edges):
            u, v =  map(int, raw_input().strip().split(' '))
            
            if u <= nodes and v <= nodes:
                node_list[u].addPath(v, 6)
                node_list[v].addPath(u, 6)
        
        top = int(raw_input().strip())
        
        costs = findPath(top)

        output = []
        for j in range(1, nodes + 1):
            if j != top:
                if (j in costs):
                    output.append(costs[j])
                else:
                    output.append(-1)
    
        print (" ".join(str(e) for e in output))

main()
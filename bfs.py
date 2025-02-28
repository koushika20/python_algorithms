graph = {

'A':['B', 'C'],

'B':['A', 'C', 'D'],

'C':['A', 'B', 'Ε'],

'D':['B','E'],

'E':['C', 'D']

}

visitedNodes= []

queueNodes=[]

#function

def bfs (visitedNodes, graph, snode):
    

       visitedNodes.append(snode)

       queueNodes.append(snode)

       print()

       print("Result:")

       while queueNodes:

          s=queueNodes.pop(0)

          print(s, end = "")

          for neighbour in graph[s]:

             if neighbour not in visitedNodes:

                visitedNodes.append(neighbour)

                queueNodes.append(neighbour)

#Main code

snode=input("Enter starting Node (A, B, C, D, or E):").upper()

#Calling bfs function

bfs (visitedNodes, graph, snode)

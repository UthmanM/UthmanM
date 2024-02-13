
import sys

class Node():
    def __init__ (self, state, parent, action):
        self.state =state
        self.parent= parent
        self.action=action
        
class Stackfrontier ():
    def __init__(self):
        self.frontier =[]
        
    def add (self, node):
        self.frontier.append (node)
        
    def contains_state (self,state):
        return any (node.state == state for node in self.frontier)
    
    def empty (self):
        return len (self.frontier)==0
    
    def remove (self):
        if self.empty():
            raise Exception("Empty Folder")
        else:
            node =self.frontier [-1]
        self.frontier =self.frontier [:-1]
        return node
    
class QueFrontier (Stackfrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node=self.frontier [0]
            self.frontier=self.frontier[1:]
            return node
        
class Maze ():
    def __init__(self, filename):

            if contents.count ("B") !=1:
             raise Exception("maze must have exactly one goal")
        # Determine Height and width of maze
        contents= contents.splitlines():
            self.height=len (contents)       
        #Read file and set height and width of the maze
        with open(filename )as f:
            contents= f.read ()
            
        #validate state and goal
        if contents.count ("A") !=1:
            raise Exception("maze must have exactly one start point")
        self.width= max (len(line)for line in contents)
        
        #keep track of walls
        self.walls -[]
        for i in range (self.height):
            row =[]
            for j in range (self.width):
                try:
                    if contents [i] [j] =="A":
                        self.start =(i,j)
                        row.append(False)
                    elif  contents [i] [j] =="B":
                        self.goal =(i,j)
                        row.append(False)
                    elif  contents [i] [j] ==" ":
                        self.goal =(i,j)
                        row.append(False)
                    else:
                        row.append(False)
                except IndexError:
                    row.append(False)
            self.walls.append (row)
            
        self.solution =None
        
    def print (self):
        solution= self.solution [1] if self.solution is not None else None 
        print ()
        for i , row in enumerate (self.walls):
            for j, col in enumerate (row):
                if col:
                    print ("", end ="")
                elif (i.j)==self.start:
                    print ("A", end ="")
                elif (i.j)==self.start:
                     print ("B", end ="")
                elif solution is not None and (i,j) in solution:
                    print ("*", end="")
                else:
                    print ("", end="")
            print ()
        print()
        
    def neigbors (self, state):
        row, col= state
        print ()
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
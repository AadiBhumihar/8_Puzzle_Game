#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 01:55:17 2017

@author: bhumihar
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:34:18 2017

@author: bhumihar
"""


import LinkedList        

        
class Dfs :

    def __init__(self,start,goal) :
        self.start = start;
        self.goal = goal
        self.statelist = LinkedList.link_list(); 
        self.leveldepth = {}
        self.statehist = {}
        
        self.nodes = 0      #counter for node generation
        self.limit = 100    # counter for limit
        self.unique = -1
        self.newvalue = None;
        self.current_state = None;
        self.solution = False;
        self.addtostatelist(start,None)

    def list_to_str(self,state) :
        if (state == None) :
            val = None ;
        else :
            val = "".join(str(x) for x in state)
        return val;
        
    def addtostatelist(self,newstate,oldstate) :
        nwstate = self.list_to_str(newstate)
        odstate = self.list_to_str(oldstate)
            
        if (nwstate not in self.leveldepth.keys()) :
            if (self.newvalue == None) and (oldstate==None) :
                self.newvalue =0;
            else :
                self.newvalue = self.leveldepth[odstate] + 1;
                
            self.unique = self.unique + 1;
            self.leveldepth[nwstate] = self.newvalue ;
            self.statehist[nwstate] = oldstate;
            self.statelist.add_to_last(newstate)    ## In Bfs new Node is added to last of Linked List 
            
    def move_up( self ,state ):
        new_state = state[:]
        index = new_state.index( 0 )
        if index not in [0, 3, 6]:
            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None
    
    def move_down( self,state ):
        new_state = state[:]
        index = new_state.index( 0 )
        if index not in [2, 5, 8]:
            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None
    
    def move_left( self,state ):
        """Moves the blank tile left on the board. Returns a new state as a list."""
        new_state = state[:]
        index = new_state.index( 0 )
        # Sanity check
        if index not in [0, 1, 2]:
            # Swap the values.
            temp = new_state[index - 3]
            new_state[index - 3] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            # Can't move it, return None
            return None
    
    def move_right( self,state ):
        new_state = state[:]
        index = new_state.index( 0 )
        if index not in [6, 7, 8]:
            temp = new_state[index + 3]
            new_state[index + 3] = new_state[index]
            new_state[index] = temp
            return new_state
        else:
            return None

        
    def dosearch(self) :
        while(not self.statelist.isempty()) :
            self.current_state = self.statelist.remove_first();
            if (self.current_state==self.goal) :
                self.solution = True;
                print('found')
                break ;
            else :
                if(self.leveldepth[self.list_to_str(self.current_state)]<self.limit) :
                    u_list = self.move_up(self.current_state)
                    if (u_list !=None) :
                        self.nodes = self.nodes +1 
                        self.addtostatelist(u_list,self.current_state)
                    d_list = self.move_down(self.current_state)
                    if (d_list !=None) :
                        self.nodes = self.nodes +1 
                        self.addtostatelist(d_list,self.current_state)
                    l_list = self.move_left(self.current_state)
                    if (l_list !=None) :
                        self.nodes = self.nodes +1 
                        self.addtostatelist(l_list,self.current_state)
                    r_list = self.move_right(self.current_state)
                    if (r_list !=None) :
                        self.nodes = self.nodes +1 
                        self.addtostatelist(r_list,self.current_state)
        if (self.solution) :
            print('Solution Found');
        else :
            print('Solution not Found')
                
 	

start = [0,1,2,3,4,5,6,7,8]
goal = [1, 8, 7, 2, 0, 6, 3, 4, 5]            
dfs =  Dfs(start,goal);
dfs.dosearch();
print(dfs.nodes) 	

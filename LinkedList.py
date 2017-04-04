#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:37:22 2017

@author: bhumihar
"""

class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class link_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_first(self,data) :
        new_node = node() # create a new node
        new_node.data = data
        if (self.head==None) :
            self.head = new_node;
            self.tail = new_node;
        else :
            new_node.next = self.head;
            self.head = new_node;   

    def add_to_last(self, data):
        new_node = node() # create a new node
        new_node.data = data
        if (self.head==None) :
            self.head = new_node;
            self.tail = new_node;
        else :
            self.tail.next = new_node;
            self.tail = new_node;
                        
    def list_print(self):
        node = self.head # cant point to ll!
        while node!=None:
            print (node.data)
            node = node.next
            
    def remove_first(self) :       
       node = self.head
       try :
           val =  node.data;
           self.head = node.next
           node = None
           return val
       except AttributeError :
           print ("Error: Object is empty")

    def isempty(self) :
        if (self.head==None):
            return True;
        else :
            return False
            
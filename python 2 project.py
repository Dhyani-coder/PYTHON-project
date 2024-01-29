# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:36:31 2024

@author: user
"""

from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

random_number_list = Label(root)
random_number_sorted_list = Label(root)

a= ["Bottle","tiffin","IDcard","chocolates","chips","tickets","hanky"]
def randomlist():
    randomlist = random.sample(a,k=4)
    random_number_list["text"] = "random list : " + str(randomlist)
    randomlist.sort()
    random_number_sorted_list["text"] = "sorted random numbers :" + str(randomlist)
    
btn=Button(root,text="generate random list ",command=randomlist)  
btn.place(relx = 0.5,rely=0.4,anchor=CENTER)
 
random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER) 

root.mainloop()

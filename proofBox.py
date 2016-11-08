#!/usr/bin/env python      
import Tkinter as tk
from Tkinter import Tk, Text, BOTH, W, N, E, S, StringVar, Menu

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.createWidgets()
        self.initUI()

    def initUI(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_cascade(label="New Window")
        fileMenu.add_cascade(label="Open")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
        editMenu = Menu(menubar)
        editMenu.add_cascade(label="Undo")
        editMenu.add_cascade(label="Redo")
        editMenu.add_separator()
        editMenu.add_cascade(label="Cut")
        editMenu.add_cascade(label="Copy")
        editMenu.add_cascade(label="Paste")
        menubar.add_cascade(label="Edit", underline=0, menu=editMenu)
        proofMenu = Menu(menubar)
        proofMenu.add_cascade(label="Add Premise")
        proofMenu.add_cascade(label="Add Step")
        proofMenu.add_cascade(label="Delete Step")
        proofMenu.add_separator()
        proofMenu.add_cascade(label="Add New Subproof")
        proofMenu.add_cascade(label="End Subproof")
        menubar.add_cascade(label="Proof", underline=0, menu=proofMenu)        

    def createWidgets(self):

        self.stepNumber = tk.Text(self, width=3, height=20)
        self.stepNumber.grid(row=0, column=0, rowspan=4, 
            padx=5, pady=5, sticky=N+W+E+S)
        
        self.sentence = tk.Text(self, width=50, height=20)
        self.sentence.grid(row=0, column=1, rowspan=4, 
            padx=5, pady=5, sticky=N+W+E+S)
        
        variable = StringVar(self)
        variable.set("Select Rule")
        self.inferenceRules = tk.OptionMenu(self, variable, "One")
        self.inferenceRules.grid(row=0, column=2, rowspan=1, 
            padx=5, pady=5, sticky=N+W+E+S)

        self.reference = tk.Label(self, width=5, height=20)
        self.reference.grid(row=0, column=3, rowspan=4, 
            padx=5, pady=5, sticky=N+W+E+S)
        
        #self.quitButton = tk.Button(self, text='Quit',
        #   command=self.quit)            
        #self.quitButton.grid(row=5, column=2)   
        
    def onExit(self):
        self.quit()        

app = Application()                       
app.master.title('Proof')    
app.mainloop() 
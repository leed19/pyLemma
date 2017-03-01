# 2/27/2017:
# NEW PLAN
# A complete redesign of this thing.
# VOL 3 WHEN


import Tkinter as tk
from Tkinter import *
import tkFileDialog

class Application(tk.Frame): 
    step = 5
    amount = 0
    lines = []
    
    def __init__(self, master=None):   
        tk.Frame.__init__(self, master)   
        self.grid()
        self.canvas = Canvas(self, width=640, height=480)
        self.canvas.pack()        
        #self.master.columnconfigure(0, weight=1)
        #self.master.rowconfigure(0, weight=1)
        self.initUI()
        self.bind('<Key>', self.addStep)
    
    def initUI(self):
        menubar = Menu(self.master)
        fileMenu = Menu(menubar)
        fileMenu.add_cascade(label="New Window")
        fileMenu.add_cascade(label="Open")
        fileMenu.add_cascade(label="Save")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit")
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
        proofMenu.add_cascade(label="Add Step", command=self.addStep, accelerator="Ctrl+P")
        proofMenu.add_cascade(label="Delete Step")
        proofMenu.add_separator()
        proofMenu.add_cascade(label="Add New Subproof")
        proofMenu.add_cascade(label="End Subproof")
        proofMenu.add_cascade(label="Verify Proof")
        menubar.add_cascade(label="Proof", underline=0, menu=proofMenu) 
        rulesMenu=Menu(menubar)
        rulesMenu.add_cascade(label="Add Inference Rule")
        menubar.add_cascade(label="Rules", underline=0, menu=rulesMenu)         
        self.master.config(menu=menubar)
           
        
    def addStep(self):
        self.addLine(self.step)
        self.step += 30    
    
    # This adds a proof line containing four components:
    # step number, sentence, inference rule, and references
    # self: the self frame,
    # yStart: the y coordinate that determines where the line is placed
    def addLine(self, yStart):
        
        #self.canvas.create_line(0,0,500,200,width=2, arrow=tk.LAST)
        self.amount += 1
        num = StringVar(self)
        self.stepNumber = Label(self, width=3, height=1, padx=5, pady=5, textvariable=num)
        self.stepNumber.pack()
        num.set(self.amount)
        self.stepNumber.place(x=5,y=yStart)
        
        self.sentence = Text(self, width=50, height=1, padx=5, pady=5)
        self.sentence.pack()
        self.sentence.place(x=45,y=yStart)
        #self.sentence.grid(row=0, column=1, rowspan=4, 
        #    padx=5, pady=5, sticky=N+W+E+S)
        
        variable = StringVar(self)
        variable.set("Select Rule")
        self.inferenceRules = OptionMenu(self, variable, "One")
        self.inferenceRules.pack()
        self.inferenceRules.place(x=400,y=yStart)
        #self.inferenceRules.grid(row=0, column=2, 
        #    padx=5, pady=5, sticky=N+W+E+S)

        ref = StringVar(self)
        self.reference = tk.Label(self, width=5, height=1, padx=5,pady=5,textvariable = ref)
        self.reference.pack()
        self.reference.place(x=500,y=yStart)
        ref.set("Test")
        #self.reference.grid(row=0, column=3, rowspan=4, 
        #    padx=5, pady=5, sticky=N+W+E+S)
        
        #self.quitButton = tk.Button(self, text='Quit',
        #   command=self.quit)            
        #self.quitButton.grid(row=5, column=2)   
        
    def onExit(self):
        self.quit()        

app = Application()                       
app.master.title('New Proof')    
app.mainloop() 
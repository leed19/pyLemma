# 2/27/2017:
# NEW PLAN
# A complete redesign of this thing.
# VOL 3 WHEN
# 3/10/2017
# Able to keep track of lines now

from collections import namedtuple
import Tkinter as tk
from Tkinter import *
import tkFileDialog

class Application(tk.Frame): 
    step = 5
    amount = 0
    proofs = []
    global lines
    lines = []
    
    global ProofLine 
    ProofLine = namedtuple("ProofLine", "field1 field2 field3 field4 field5")
    # create a set of structs for lines
    # Each line will have the following list of attributes:
    # line number, sentence, inference rule, reference, which proof it belongs to.
    
    def __init__(self, master=None):   
        tk.Frame.__init__(self, master)   
        self.stepNumber = []
        self.sentence = []
        self.inferenceRules = []
        self.reference = []
        self.variable = []
        self.include = []
        self.grid()
        self.canvas = Canvas(self, width=800, height=600)
        self.canvas.pack()        
        #self.master.columnconfigure(0, weight=1)
        #self.master.rowconfigure(0, weight=1)
        self.initUI()
        self.bind('<Key>', self.addStep)
    
    def initUI(self):
        menubar = Menu(self.master)
        fileMenu = Menu(menubar)
        fileMenu.add_cascade(label="New Window")
        fileMenu.add_cascade(label="Open", command=self.openFile)
        fileMenu.add_cascade(label="Save", command=self.saveFile) # Will create a prf file.
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
        proofMenu.add_cascade(label="Add New Subproof") # This will make a new list of lines representing different subproof
        proofMenu.add_cascade(label="End Subproof")
        proofMenu.add_cascade(label="Verify Proof")
        menubar.add_cascade(label="Proof", underline=0, menu=proofMenu) 
        rulesMenu=Menu(menubar)
        rulesMenu.add_cascade(label="Add Inference Rule") # When this is added, a screen will show up, select inf rule, drop down menu will add those rules as choices.
        menubar.add_cascade(label="Rules", underline=0, menu=rulesMenu)         
        self.master.config(menu=menubar)
        
    def addInference(self):
        return 0
        
    def addStep(self):
        self.addLine(self.step)
        lastS = self.stepNumber[len(self.stepNumber) - 1]
        lastSen = self.sentence[len(self.sentence) - 1]
        lastRef = self.reference[len(self.reference) - 1]
        l = ProofLine(lastS.cget("text"), lastSen.get("1.0",END), lastRef.cget("text"), "sad", "dsa")
        lines.append(l)        
        self.step += 30    
        
    def saveFile(self):
        n = self.stepNumber
        s = self.sentence
        v = self.variable
        r = self.reference
        f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".prf")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        f.write("proof" + "\n")
        for i in range(0,len(n)):
            step2save = str(n[i].cget("text"))# str(n[i].cget("text")).splitlines()
            text2save = str(s[i].get(1.0, "end"))# str(s[i].get(1.0, "end")).splitlines()
            text2save = text2save[:len(text2save)-1]
            rule2save = v[i].get()
            refs2save = str(r[i].cget("text"))
            # for j in range(0,len(step2save)):
            f.write(step2save + "\t" + text2save + "\t" + rule2save + "\t" + refs2save + "\n")
            #step2save = str(n[i].cget("text")).splitlines()
            #text2save = str(s[i].get(1.0, "end")).splitlines()
            #for j in range(0,len(step2save)):
            #   f.write(step2save[j] + "\t" + text2save[j] + "\n")
        f.write("done" + "\n")
        f.close()   
        
    def openFile(self):
        f = tkFileDialog.askopenfile(mode='r', defaultextension=".prf")
        if f is None:
            return
        lines = f.readlines()
        numL = []
        stepL = []
        ruleL = []
        refL = []
        for l in lines:
            elem = l.split('\t')
            if (len(elem) == 4):
                numL.append(elem[0])
                stepL.append(elem[1])
                ruleL.append(elem[2])
                refL.append(elem[3])
        for i in range(0,len(numL)):
            self.addLine(self.step)
            lastS = self.stepNumber[len(self.stepNumber) - 1]
            lastSen = self.sentence[len(self.sentence) - 1]
            lastRef = self.reference[len(self.reference) - 1]
            l = ProofLine(lastS.cget("text"), lastSen.get("1.0",END), lastRef.cget("text"), "sad", "dsa")
            lines.append(l)        
            self.step += 30
        for i in range(0,len(numL)):
            self.sentence[i].insert("insert", stepL[i])
        f.close()
    
    # This adds a proof line containing four components:
    # step number, sentence, inference rule, and references
    # self: the self frame,
    # yStart: the y coordinate that determines where the line is placed
    def addLine(self, yStart):
        
        #self.canvas.create_line(0,0,500,200,width=2, arrow=tk.LAST)
        self.amount += 1
        num = StringVar(self)
        self.stepNumber.append(Label(self, width=3, height=1, padx=5, pady=5, textvariable=num))
        self.stepNumber[len(self.stepNumber) - 1].pack()
        num.set(self.amount)
        self.stepNumber[len(self.stepNumber) - 1].place(x=5,y=yStart)
        
        self.sentence.append(Text(self, width=50, height=1, padx=5, pady=5))
        self.sentence[len(self.sentence) - 1].pack()
        self.sentence[len(self.sentence) - 1].place(x=45,y=yStart)
        #self.sentence.grid(row=0, column=1, rowspan=4, 
        #    padx=5, pady=5, sticky=N+W+E+S)
        
        self.variable.append(StringVar(self))
        self.variable[len(self.variable) - 1].set("Select Rule")
        self.inferenceRules.append(OptionMenu(self, self.variable[len(self.variable) - 1], "Assumption", "And Elim Left", "And Elim Right"))
        self.inferenceRules[len(self.inferenceRules) - 1].pack()
        self.inferenceRules[len(self.inferenceRules) - 1].place(x=400,y=yStart)
        #self.inferenceRules.grid(row=0, column=2, 
        #    padx=5, pady=5, sticky=N+W+E+S)

        ref = StringVar(self)
        self.reference.append(tk.Label(self, width=5, height=1, padx=5,pady=5,textvariable = ref))
        self.reference[len(self.reference) - 1].pack()
        self.reference[len(self.reference) - 1].place(x=600,y=yStart)
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
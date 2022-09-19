import os
import trimesh
import random
from tkinter import *
from tkinter import filedialog

# set paths to folder containing 3D shapes
psb_path = "PrincetonShapeBenchmark/"

def loadModel():
    modelPath = filedialog.askopenfilename(initialdir=psb_path)
    
    try:
        mesh = trimesh.load(modelPath)
        mesh.show()
    except:
        return
        
window = Tk()
button = Button(text="Load model",command=loadModel)
button.pack()
window.mainloop()
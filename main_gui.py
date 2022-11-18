#### This code has been taken from Github (https://github.com/EdwardChamberlain/PySimpleGUI-3D-Viewer) #####
#### and modeified by us to change the mesh viewer and serve our purpose ####


import PySimpleGUI as sg

import os
import re
import numpy as np
import sys

from dataset import Dataset
from distance import Distance
from ANN import Annoy


def refresh_view(RENDER_MODE,objects,nums=None):
    if nums is None:
        nums = list(range(6))
    for i in nums:

        split_path = re.split(r'\\|/', objects[i])
        split_path[-3] = "thumbnails"
        file = str.split(split_path[-1], '.')
        file[1] = "png"
        split_path[-1] = '.'.join(file)
        path = os.sep.join(split_path)
        #print(path)

        window[f'-THMB-{i}'].Update(path)

        canvas: sg.Image = window[f'-THMB-{i}']
        canvas = sg.Image(path, size=(240, 240))

def get_path(elements):
    path = elements[0]
    for i in range(1,len(elements)):
        path = os.path.join(path,elements[i])
    return path

# Create Scene

# init Dataset and Distance
ds = Dataset("Princeton_remeshed_normalized", write_basic_csv = False, write_other_csv = False)
dist = Distance("Princeton_remeshed_normalized", ["m1693.ply"])
ann = Annoy("Princeton_remeshed_normalized", ["m1693.ply"], n_bins=30)

#keep these default values for now because it prefills objects[] even though it is cursed af
main_path = get_path(['.','Princeton','aircraft'])
meshes_names = ['m1139.ply','m1127.ply','m1119.ply','m1149.ply','m1159.ply','m1169.ply']

nums = len(meshes_names)

paths = [os.path.join(main_path,name) for name in meshes_names]
objects = [paths]
# my_camera = planar_projection.Camera_3D(
#     focal_distance=-2,
#     projection_plane_distance=1
# )
sg.theme('DarkAmber')
THUMB_SIZE = (100,100) if sg.running_trinket() else (150,150)

def generate_element(st_idx,dist,text,i):

    text_ele = [sg.Text(str(text),font=('Helvetica', 15))]
    thumbs = [sg.Image(size=THUMB_SIZE, enable_events=True, key=f'-THMB-{i}') ]
    dist_text = [sg.Text("dis="+str(dist),font=('Helvetica', 15),key=f'-DIST-{i}') if dist is not None else sg.Text("",font=('Helvetica', 15),key=f'-DIST-{i}') ]
    col = sg.Column([text_ele,thumbs,dist_text], element_justification='center', expand_x=True)
    return col

text = ['Query shape','1','2','3','4','5']
dists = [None,None,None,None,None,None,None]
layout = [[generate_element(i,dists[i],text[i],i) for i in range(6)]]
layout.append([[sg.Text("Choose a file: "), sg.Input(key='-BROWSE-'), sg.FileBrowse()],[sg.Button("Submit")],sg.Text("Render Mode:"), sg.Combo(['POINTS', "LINES", 'FACES', 'SHADED'], 'FACES', key="-REDNER_TYPE-", readonly=True, enable_events=True)])

def function_called_when_mesh_selected(i,names):
    #print("mesh selected name is",names[i])
    ds.show_mesh(names[i])
#print()
window = sg.Window('3D Viewport', layout)

drag_loc = None
first_time = True
while True:
    if first_time:
        window.Finalize()
        # refresh_view('FACES',objects)
        first_time = False

    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    elif event == "-REDNER_TYPE-":
        refresh_view(values['-REDNER_TYPE-'],objects)
    elif event == 'Submit':

        # write code here
        path = values['-BROWSE-']
        #print(path,os.sep)
        objects[0] = path #obj_reader.import_obj(path, rotation=('z', 0), translation=(0, 0, 0))

        if len(sys.argv) < 2:
            result = dist.query(path, dist.euclidean_EMD, k=5)
            print("Using custom distance function...")
        else:
            if sys.argv[1] == "--ann":
                result = ann.query(path, k=5)
                print("Using custom ANN euclidean...")
            elif sys.argv[1] == "--custom":
                result = dist.query(path, dist.euclidean_EMD, k=5)
                print("Using custom distance function...")
            else:
                print("Not a valid distance function")

        meshes = [i[0] for i in result]
        meshpaths = [ds.get_mesh_file_path(m) for m in meshes]
        meshes_names[1:] = meshes
        print(meshes, meshpaths)
        dists = [i[1] for i in result]

        objects[1:] = list(meshpaths)

        refresh_view(values['-REDNER_TYPE-'],objects)
        # set the new distances
        for i in range(1,6):
            window[f'-DIST-{i}'].Update(f'dist={str(round(dists[i-1], 6))}')


    else:
        for i in range(nums):
            if event == f'-THMB-0':
                print("Can't show query mesh")
            elif event == f'-THMB-{i}':
                function_called_when_mesh_selected(i,meshes_names)
            elif event == '-GRAPH-+UP':
                drag_loc = None



window.close()

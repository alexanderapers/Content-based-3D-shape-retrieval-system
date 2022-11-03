import PySimpleGUI as sg

from PySimpleGUI3D import planar_projection
from PySimpleGUI3D import obj_reader
from PySimpleGUI3D import workarounds

import trimesh
import pyrender

import os
import numpy as np
def RGB_2_HEX(x: tuple):
    return f"#{x[0]:02x}{x[1]:02x}{x[2]:02x}"
def get_boundries(points,i):
    mn = 1000000
    mx = -1000000
    for point in points:
        if point[i]>mx:
            mx = point[i]
        if point[i]<mn:
            mn = point[i]
    return mn,mx
def standerdize(n,mn,mx):
    n = (n-mn)/(mx-mn)
    return n
def correct_dimensions(obj):
    n = len(obj.verts[0])
    dims_ranges = []
    for i in range(n):
        ds = [v[i] for v in obj.verts]
        dims_ranges.append(max(ds)-min(ds))
    # x is the longest, y is the next, and z is the least
    sorting = np.argsort(dims_ranges)[::-1]
    # sorting = [2,1,0]
    new_vertices = [[0,0,0]for _ in obj.verts]
    for i,vert in enumerate(obj.verts):
        for j,idx in enumerate(sorting):
            new_vertices[i][j] = vert[idx]
    obj.verts = new_vertices
    return obj
      
        
def refresh_view(RENDER_MODE,objects,nums=None):
    if nums is None:
        nums = list(range(len(objects)))
    for i in nums:
        canvas: sg.Graph = window[f'-GRAPH-{i}']
        canvas.erase()
        my_object = objects[i]
        # makes the orientation of the mesh good for displaying
        my_object = correct_dimensions(my_object)
        points = my_camera.project_object(my_object)
        mn_y,mx_y = get_boundries(points,0)
        mn_z,mx_z = get_boundries(points,1)

        points = [(standerdize(p[0],mn_y,mx_y)-1/2,standerdize(p[1],mn_z,mx_z)-1/2)for p in points]
        if RENDER_MODE == 'LINES':
            if my_object.edges is None:
                canvas.draw_text("No lines data in file!", (0, 0), 'white')
                return

            for p1, p2 in my_camera.get_edges(my_object):
                canvas.draw_line(p1, p2, 'white', 3)

        if RENDER_MODE == 'POINTS':
            if my_object.verts is None:
                canvas.draw_text("No points in file!", (0, 0), 'white')
                return

            for p in points:
                canvas.draw_circle(p, 0.005, 'white', 'white')

        if RENDER_MODE == 'FACES':
            if my_object.faces is None:
                canvas.draw_text("No faces data in file!", (0, 0), 'white')
                return

            for f in my_camera.get_faces(my_object):
                verts = [points[p] for p in f]
                canvas.draw_polygon(verts, 'grey', 'orange', 0.02)

        if RENDER_MODE == 'SHADED':
            if my_object.faces is None:
                canvas.draw_text("No faces data in file!", (0, 0), 'white')
                return

            faces = my_camera.get_faces(my_object)
            for n, f in enumerate(faces):
                c = int(n / len(faces) * 150) + 50
                face_colour = RGB_2_HEX((c, c, c))
                verts = [points[p] for p in f]
                canvas.draw_polygon(verts, face_colour, face_colour, 0.02)


def get_path(elements):
    path = elements[0]
    for i in range(1,len(elements)):
        path = os.path.join(path,elements[i])
    return path

# Create Scene

main_path = get_path(['.','meshes','Princeton','aircraft'])
meshes_names = ['m1139.ply','m1127.ply','m1119.ply','m1149.ply','m1159.ply','m1169.ply']

nums = len(meshes_names)

paths = [os.path.join(main_path,name) for name in meshes_names]
objects = [obj_reader.import_obj(path, rotation=('z', 0), translation=(0, 0, 0)) for path in paths]
my_camera = planar_projection.Camera_3D(
    focal_distance=-2,
    projection_plane_distance=1
)
sg.theme('DarkAmber')
GRAPH_SIZE = (100,100) if sg.running_trinket() else (150,150)

def generate_element(st_idx,dist,text,i):
    
    text_ele = [sg.Text(str(text),font=('Helvetica', 15))]
    graphs = [sg.Graph(GRAPH_SIZE, (-1, -1), (1, 1), 'black', float_values=True, enable_events=True, key=f'-GRAPH-{i}', drag_submits=True) ]
    dist_text = [sg.Text("dis="+str(dist),font=('Helvetica', 15),key=f'-DIST-{i}') if dist is not None else sg.Text("",font=('Helvetica', 15),key=f'-DIST-{i}') ]
    col = sg.Column([text_ele,graphs,dist_text], element_justification='center', expand_x=True)
    return col

text = ['Query shape','1','2','3','4','5']
dists = [None,None,None,None,None,None,None]
layout = [[generate_element(i,dists[i],text[i],i) for i in range(6)]]
layout.append([[sg.Text("Choose a file: "), sg.Input(key='-BROWSE-'), sg.FileBrowse()],[sg.Button("Submit")],sg.Text("Render Mode:"), sg.Combo(['POINTS', "LINES", 'FACES', 'SHADED'], 'FACES', key="-REDNER_TYPE-", readonly=True, enable_events=True)])

def function_called_when_mesh_selected(i,names):
    print("mesh selected name is",names[i])
print()
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
        print(path,os.sep)
        objects[0] = obj_reader.import_obj(path, rotation=('z', 0), translation=(0, 0, 0))
        # set the new_objects with your custom objects
        new_objects = objects[1:]
        objects[1:] = new_objects
        refresh_view(values['-REDNER_TYPE-'],objects)
        # set the new distances
        dists = [0,.14,0.21,0.33,0.56,0.67]
        for i in range(1,6):
            window[f'-DIST-{i}'].Update(f'dist={dists[i]}')
            
        
    else:
        for i in range(nums):
            if event == f'-GRAPH-{i}':
                new_drag_location = values[f'-GRAPH-{i}']

                if not drag_loc:
                    drag_loc = new_drag_location
                
                objects[i].orientation += (drag_loc[0] - new_drag_location[0]) * 360
                objects[i].position[0] += (drag_loc[1] - new_drag_location[1]) * -10

                drag_loc = new_drag_location


                # window['-O-'].update(objects[i].orientation)
                # window['-X-'].update(objects[i].position[0])
                
                # refresh_view(values['-REDNER_TYPE-'],objects,[i])
                function_called_when_mesh_selected(i,meshes_names)
            if event == '-GRAPH-+UP':
                drag_loc = None

    

window.close()

# INFOMR-2022

Dependencies:
- trimesh
- scipy
- pyglet==1.5.27
- networkx
- pillow
- shapely
- open3d (requires python 3.9 or lower)
- numba

To visualise a mesh run like this:  
**python main.py mesh_name**  
example:  
**python main.py m484.ply**  
or:  
**python main.py**  
to only open first mesh file  

To visualise a querying UI run like this:
<!--* create a folder named "meshes" and in this folder place meshes folders
(I have Princeton, Princeton_remeshed,Princeton_remeshed_normalized right now)-->
* make sure you have the PySimpleGUI3D folder, which is taken from Github (https://github.com/EdwardChamberlain/PySimpleGUI-3D-Viewer) for some dependencies:
     1. object reader to read the object (changed to read .ply)
     2. the planar projection camera to render the 3D objects
     3. the function refresh view (a simple function to update the graphs which is changed too)

* run "pip install -r requirements.txt"
* run "python main_gui.py"

<!--P.S.
The step of creating the "meshes" folder is just to make the hard coded paths in the code work fine for testing purposes. You can change these paths instead if you don't want to change your meshes location in your local computer-->

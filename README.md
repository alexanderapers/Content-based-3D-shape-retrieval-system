# INFOMR-2022

Main dependencies:
- trimesh
- scipy
- pyglet==1.5.27
- networkx
- pillow
- shapely
- open3d (requires python 3.9 or lower)
- numba
- PySimpleGUI
- Annoy
- seaborns
- pickle
- pandas
- numpy
- sklearn
- tqdm
- matplotlib

Run the command "pip install -r requirements.txt" to install all the dependencies.

To visualise a mesh, run like this:  

* python main.py _mesh_name_

example:  
* python main.py m484.ply
or:  
* python main.py
to only open first mesh file  

To visualise the querying UI run like this:

* python main_gui.py

It will automatically use our custom distance function.
To use the ANN querying with L2 distance function, add the "--ann" command line argument.

* python main_gui.py --ann
* python main_gui.py --custom

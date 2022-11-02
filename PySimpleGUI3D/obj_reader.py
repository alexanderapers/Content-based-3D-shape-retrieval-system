from . import planar_projection
from mesh import Mesh

def import_obj(filename: str, rotation=None, translation=None):
    my_mesh = Mesh(filename)

    verticies = my_mesh.get_vertices()
    faces = my_mesh.get_faces()
    

    imported_object = planar_projection.Object_3D(
        verts=verticies,
        edges=None,
        faces=faces
    )

    if rotation[0] == 'x':
        imported_object._verts = [imported_object.roatate_point_x(p, rotation[1]) for p in imported_object._verts]
    if rotation[0] == 'z':
        imported_object._verts = [imported_object.roatate_point_z(p, rotation[1]) for p in imported_object._verts]
    if translation:
        imported_object._verts = [imported_object.translate_point(p, translation) for p in imported_object._verts]


    return imported_object




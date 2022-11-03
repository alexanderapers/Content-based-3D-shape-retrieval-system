import open3d as o3d

def view(mesh_file_path):
    mesh = o3d.io.read_triangle_mesh(mesh_file_path)
    lineset = o3d.geometry.LineSet.create_from_triangle_mesh(mesh)
    o3d.visualization.draw_geometries([lineset])

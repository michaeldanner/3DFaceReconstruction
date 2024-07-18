import pyvista as pv
import argparse


def visualize_vti(vti_file_path, threshold=0.07, output_file_path=None):

    reader = pv.XMLImageDataReader(vti_file_path)

    # Read the .vti file
    data = reader.read()

    # Print some information about the data
    print(data)

    # Apply a threshold to visualize areas with scalar values above a certain level
    thresholded = data.threshold(value=threshold)  # Adjust the value as needed

    # Create a plotter object
    plotter = pv.Plotter()

    # Add the thresholded data to the plotter
    plotter.add_mesh(thresholded)

    # plotter.add_mesh(data)
    # plotter.add_mesh(data.slice_orthogonal())
    #  Add volume rendering
    # plotter.add_volume(data, opacity='linear')  # Try 'linear', 'sigmoid', or a custom opacity function

    if output_file_path:
        # Export the thresholded mesh as an .obj file
        thresholded.save(output_file_path+'.vtk', binary=False)
        vtk_to_obj(output_file_path + '.vtk', output_file_path + '.obj')
    else:
        plotter.show()


def vtk_to_obj(vtk_file_path, obj_file_path):
    # Read the .vtk file
    mesh = pv.read(vtk_file_path)

    # Print some information about the mesh
    print(mesh)

    # Ensure the mesh is a PolyData object before saving as .obj
    if not isinstance(mesh, pv.PolyData):
        # Convert the mesh to PolyData
        mesh = mesh.extract_geometry()

    # Save the mesh as an .obj file
    mesh.save(obj_file_path, binary=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize a .vti file with optional thresholding.")
    parser.add_argument("filename", type=str, help="Path to the .vti file.")
    parser.add_argument("--threshold", type=float, help="Optional threshold value for scalar visualization.", default=None)
    parser.add_argument("--output", type=str, help="Path to the output .obj file.", default=None)

    args = parser.parse_args()

    visualize_vti(args.filename, args.threshold, args.output)


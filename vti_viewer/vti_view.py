import pyvista as pv
import argparse


def visualize_vti(vti_file_path, threshold=0.07):

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

    plotter.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize a .vti file with optional thresholding.")
    parser.add_argument("filename", type=str, help="Path to the .vti file.")
    parser.add_argument("--threshold", type=float, help="Optional threshold value for scalar visualization.", default=None)

    args = parser.parse_args()

    visualize_vti(args.filename, args.threshold)

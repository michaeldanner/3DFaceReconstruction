
# VTI Visualizer

This Python program visualizes `.vti` files using PyVista. It supports optional thresholding to highlight specific scalar value ranges within the dataset.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/michaeldanner/3DFaceReconstruction
   cd vti_viewer
   ```

2. **Install dependencies:**

   Make sure you have Python and pip installed. Then install the required package using pip:

   ```sh
   pip install pyvista
   ```

## Usage

Run the program from the command line, providing the path to your `.vti` file as a parameter. Optionally, you can also provide a threshold value.

### Basic Usage

To visualize a `.vti` file without thresholding:

```sh
python vti_view.py path/to/your/file.vti
```

### Thresholding

To visualize a `.vti` file with a threshold:

```sh
python vti_view.py path/to/your/file.vti --threshold 100
```

### Parameters

- `filename`: Path to the `.vti` file to visualize.
- `--threshold`: (Optional) Scalar value for thresholding the visualization.
- `--output`: (Optional) Path to the `.obj` file to export.

## Example

Visualize a `.vti` file located at `data/sample.vti` with a threshold value of `150`:

```sh
python vti_view.py data/sample.vti --threshold 150
```

Export a `.obj` file located at `out/sample.obj` with a threshold value of `0.09`:

```sh
python vti_view.py data/sample.vti --threshold 0.09 --output out/sample
```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs or enhancements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

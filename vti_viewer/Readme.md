
# VTI Visualizer

This Python program visualizes `.vti` files using PyVista. It supports optional thresholding to highlight specific scalar value ranges within the dataset.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/vti-visualizer.git
   cd vti-visualizer
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
python visualize_vti.py path/to/your/file.vti
```

### Thresholding

To visualize a `.vti` file with a threshold:

```sh
python visualize_vti.py path/to/your/file.vti --threshold 100
```

### Parameters

- `filename`: Path to the `.vti` file to visualize.
- `--threshold`: (Optional) Scalar value for thresholding the visualization.

## Example

Visualize a `.vti` file located at `data/sample.vti` with a threshold value of `150`:

```sh
python visualize_vti.py data/sample.vti --threshold 150
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bugs or enhancements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

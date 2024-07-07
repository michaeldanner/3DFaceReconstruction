# GAN-Powered Model & Landmark-Free Reconstruction: A Versatile Approach for High-Quality 3D Facial and Object Recovery from Single Images

This repository contains the source code and datasets used in the paper "GAN-Powered Model & Landmark-Free Reconstruction: A Versatile Approach for High-Quality 3D Facial and Object Recovery from Single Images," presented at the 4th International Conference on Deep Learning Theory and Applications in 2023.

## Authors
- Michael Danner
- Patrik Huber
- Muhammad Awais
- Matthias Rätsch
- Josef Kittler

## Paper Abstract
The paper presents a novel approach for 3D reconstruction of facial and general objects from single images using Generative Adversarial Networks (GANs). Unlike traditional methods, this approach does not rely on predefined models or landmarks, enabling versatile and high-quality 3D recovery. This method is applicable to both facial and general object reconstruction tasks, offering a robust framework for various applications in computer vision and graphics.

## Repository Contents
- **Source Code**: Implementation of the GAN-powered model and landmark-free reconstruction method.
- **Datasets**: Sample datasets used in the experiments.
- **Pretrained Models**: Models trained using the proposed GAN approach.
- **Documentation**: Detailed instructions on how to use the code and replicate the experiments.

## Getting Started

### Prerequisites
- Python 3.8 or later
- TensorFlow 2.4 or later
- NumPy
- OpenCV
- Other dependencies listed in `requirements.txt`

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/michaeldanner/3DFaceReconstruction.git
    cd 3DFaceReconstruction
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
To run the experiments, follow these steps:

1. **Data Preparation**: Ensure your datasets are structured as expected. Refer to the `data/README.md` for details on dataset preparation.
2. **Training**: Train the model using the provided training scripts.
    ```bash
    python train.py --config configs/train_config.yaml
    ```
3. **Evaluation**: Evaluate the trained models on the test datasets.
    ```bash
    python evaluate.py --config configs/eval_config.yaml
    ```

### Results
The results of our experiments, including performance metrics and visualizations, can be found in the `results/` directory. Detailed analysis and discussion of these results are provided in the paper.

## Citation
If you use this code in your research, please cite our paper:

@inproceedings{danner2023modelfree,
title={GAN-Powered Model&Landmark-Free Reconstruction: A Versatile Approach for High-Quality 3D Facial and Object Recovery from Single Images.},
author={Danner, Michael and Huber, Patrik and Awais, Muhammad and Rätsch, Matthias and Kittler, Josef},
booktitle={Proceedings of the 4th International Conference on Deep Learning Theory and Applications},
year={2023}
}


## Acknowledgements
We would like to thank our collaborators and the institutions that supported this research. Special thanks to the reviewers for their valuable feedback.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

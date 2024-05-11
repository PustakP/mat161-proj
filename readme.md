# Eigenfaces: Facial Recognition with Linear Algebra

This repository contains code for implementing facial recognition using Eigenfaces, a classical method in the field of computer vision and pattern recognition. The project was developed as part of the MAT161 Applied Linear Algebra course.

## 📸 Custom Image Dataset

To train and test the Eigenfaces model, a custom dataset of 1600 face images was created. These images were generated uniquely for this project using StyleGAN2, ensuring a diverse and realistic dataset for robust facial recognition.

## 🤖 How it Works

The Eigenfaces method involves several steps:

1. **Preprocessing**: Images are resized to 100x100 pixels and converted to grayscale.
2. **Eigenface Calculation**: Principal Component Analysis (PCA) is applied to calculate the eigenfaces, which are the principal components of the dataset.
3. **Face Detection**: Faces in new images are detected by measuring the distance between the input image and the mean-subtracted projected image vectors.
4. **Face Recognition**: Faces are recognized by comparing the distance between the projected image vectors of the input image and those of the images in the dataset.

## 🚀 Usage

To use this code:

1. Ensure you have Python installed along with the necessary libraries listed.
2. Generate or use the given dataset of face images.
3. Run the provided scripts for dataset generation and Eigenfaces implementation.

## 🙌 Acknowledgments

Special thanks to the contributors of the following libraries used in this project:

- [OpenCV](https://opencv.org/) for image processing.
- [NumPy](https://numpy.org/) for numerical operations.
- [matplotlib](https://matplotlib.org/) for visualization.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

For more information, refer to the detailed documentation and comments within the code files. Happy face recognition! 😊🔍

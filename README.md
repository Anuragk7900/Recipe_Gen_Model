# Recipe Generation Model

A deep learning-based recipe ingredient classification project built using Python and TensorFlow.

## Features
- Ingredient image classification
- CNN-based deep learning model
- Recipe prediction from images
- Training and testing scripts
- Confusion matrix generation

## Project Structure

```
left/
├── backend/
│   ├── cnn/
│   ├── datasets/
│   ├── models/
│   ├── infer3.py
│   ├── train1.py
│   └── requirements.txt
├── README.md
└── .gitignore
```

## Installation

```bash
git clone https://github.com/Anuragk7900/Recipe_Gen_Model.git
cd Recipe_Gen_Model

pip install -r requirements.txt
```
## Download Pre-trained Model

The trained model files are too large for GitHub (>100 MB) and are therefore not included in this repository.

Download them from Google Drive:

👉 [https://drive.google.com/your-drive-link-here](https://drive.google.com/drive/folders/1gSAv_WGzlVwNBw6kMW4C5xQQ6c7aibPh?usp=sharing)

After downloading, place the files in:

```
left/backend/cnn/
```

The required files are:

- ingredient_model.h5
- ingredient_classifier.h5
- ingredient_classifier_checkpoint.h5 (if needed)
## Run the Project

```bash
python infer3.py
```

## Train the Model

```bash
python train1.py
```

## Technologies Used

- Python 3.11
- TensorFlow/Keras
- NumPy
- OpenCV
- Pandas
- Matplotlib

## Note

Large trained model files (`*.h5`) are not included in this repository because they exceed GitHub's file size limit. Download or generate the model separately before running inference.

## Author

Anurag Kumar

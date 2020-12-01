# CNNs-and-Transfer-Learning
Final Project for Lighthouse Labs Data Science Bootcamp
Project utilizes Transfer Learning to train a model to classify types of asphalt deficiencies. 

## How to use this repository

A description of the files and directory structure in the repository.
```bash
org/repo/
├── Data Collection/
|     ├── folder_description.md                       
|     ├── 01_downloading_images.ipynb                 # notebook for image downloads
|     └── 02_data_splitting.ipynb                     # notebook for train/test/validation splits
│
├── Model Selection and Tuning/
|     ├── folder_description.md
|     ├── 01_understanding_models.ipynb               # notebook containing information on torchvision models
|     ├── 02_model_comparision.ipynb                  # comparing out-of-box model performance
|     ├── 03_hyperparameter_tuning.ipynb              # notebook for skeleton of hyperparameter tuning
│
├── Final Model/
|     ├── folder_description.md
|     └── 01_final_model.ipynb                        # final model training and saving of state_dict
│
├── Deployment Files/
│     ├── folder_description.md                                     
│     ├── app.py                                      # deploy with streamlit
│     ├── image_classification.py                     # perform predictions
│     ├── load_css.py                                 # loading html formatting
│     └── style.css                                   # formatting
│
├── Scripts/
│     ├── folder_description.md
│     ├── performance_plots.py                          
│     ├── 
│     └── 
|
├── LICENSE                                           # MIT license 
└── README.md                                         # This file
```


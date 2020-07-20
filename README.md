# Music-Classifier

Python files (*.py) :
  1- ConvertToWav.py : To convert "au" files to "wav" for analysis
  2- CreateDataset.py : Extracting different features by hand 
  3- Pure_mfcc_features.py : Extracting only mfcc featrues 
  
Data :
  1- Data_set.csv : The hand crafted features from CreateDataset.py
  2- labels2.npy and mfccdata2.npy : The labels and the mfcc features saved in a numpy array

Classifier :
  1- music_classifer (1).ipynb : notebook for different classifiers(Random Forset Classifier, Support Vector Classifer, KNN Classifer, Traditionnal neural network, CNN)

Research papers : 
  - https://arxiv.org/pdf/1804.01149.pdf
  - https://arxiv.org/pdf/1802.09697.pdf
  - https://www.sciencedirect.com/science/article/pii/S1877050919310646/pdf?md5=4f9a5242eb223b5c96c9ebf130855467&pid=1-s2.0-S1877050919310646-main.pdf

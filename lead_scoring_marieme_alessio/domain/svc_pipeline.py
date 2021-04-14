import numpy as np 
import pandas as pd

import json 

import os
import os.path
from os import path

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn import svm, datasets
from sklearn.svm import SVC

import matplotlib.pyplot as plt
import seaborn as sns

import lead_scoring_marieme_alessio.config.config as cf
from lead_scoring_marieme_alessio.infrastructure.clean_data_transformer import CleanDataTransformer
from lead_scoring_marieme_alessio.domain.categorical_transformer import CategoricalTransformer
from lead_scoring_marieme_alessio.domain.numerical_transformer import NumericalTransformer
from lead_scoring_marieme_alessio.domain.feature_selector import FeatureSelector
from lead_scoring_marieme_alessio.domain.evaluate_model import evaluate_model
from lead_scoring_marieme_alessio.domain.pipeline_transformer import pipeline_transformer



def svc_pipeline(X_train, y_train):
    
    full_pipeline = pipeline_transformer()

    param_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../notebook/best_params.json'))

    C = 1,
    gamma = 'scale',
    kernel = 'linear',
    
    if path.isfile(param_path) :
        with open(param_path) as param_file:
            data = json.load(param_file)
            if 'svm' in data.keys():
                params = data['svm']
                if 'C' in params.keys():
                    C = params['C']
                if 'gamma' in params.keys():
                    gamma = params['gamma']
                if 'kernel' in params.keys():
                    kernel = params['kernel'] 

    svc_pipeline = Pipeline( steps = [ 
        ( 'full_pipeline', full_pipeline),
        ( 'rf', SVC(
                    #C=C,
                    #gamma=gamma,
                    #kernel=kernel,
                    probability=True
                )) 
    ])


    svc_pipeline.fit( X_train, y_train )


    return svc_pipeline


























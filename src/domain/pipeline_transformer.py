import numpy as np 
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion, Pipeline 
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler, LabelEncoder, LabelBinarizer, OrdinalEncoder, OneHotEncoder
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, KFold


import src.config.config as cf
from src.infrastructure.CleanDataTransformer import CleanDataTransformer
from src.domain.CategoricalTransformer import CategoricalTransformer
from src.domain.NumericalTransformer import NumericalTransformer
from src.domain.FeatureSelector import FeatureSelector





def pipeline_transformer():

    #Defining the steps in the categorical pipeline 
    categorical_pipeline = Pipeline( steps = [ 
                ( 'cat_selector', FeatureSelector(cf.CAT_FEAT) ),
                ( 'cat transformer', CategoricalTransformer()),
                ( 'cat_inputer', SimpleImputer(missing_values = np.nan,strategy='most_frequent') ),
                ( 'one_hot_encoder', OneHotEncoder( sparse = True ) )
        ])
    
    #Defining the steps in the numerical pipeline     
    numerical_pipeline = Pipeline( steps = [ 
                ( 'num_selector', FeatureSelector(cf.NUM_FEAT) ),
                ( 'num_transformer', NumericalTransformer() ),
                ( 'num_inputer', SimpleImputer(missing_values = np.nan,strategy='median') ),
                ( 'std_scaler', StandardScaler() ) 
        ])
    
    enc = OrdinalEncoder()
    cats = [['Faible', 1], ['Moyen', 2], ['Elevé', 3]]
    enc.fit(cats)
    categorical_pipeline_ord = Pipeline( steps = [ 
            ( 'cat_selector_ord', FeatureSelector(cf.CAT_FEAT_ORD) ),
            ( 'cat_inputer_ord', SimpleImputer(strategy='most_frequent') ),
            ( 'ordinal_encoder_ord', enc)
    ])


    #Combining numerical and categorical piepline into one full big pipeline horizontally 
    #using FeatureUnion
    union_pipeline = FeatureUnion( transformer_list = [ ( 'categorical_pipeline', categorical_pipeline ), 
                                                ( 'numerical_pipeline', numerical_pipeline ),
                                                ('ordinal_transformer', categorical_pipeline_ord) ] )



    return union_pipeline
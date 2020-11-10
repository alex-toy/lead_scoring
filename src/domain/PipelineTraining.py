import numpy as np 
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion, Pipeline 

class PipelineTraining:

    def __init__(self, categorical_features, numerical_features, data):
        #Categrical features to pass down the categorical pipeline 
        self.categorical_features = categorical_features

        #Numerical features to pass down the numerical pipeline 
        self.numerical_features = numerical_features

        #data is a dataframe
        self.data = data.copy()

    def _separate_target_and_feature(self)
        #Leave it as a dataframe because our pipeline is called on a 
        #pandas dataframe to extract the appropriate columns
        self.X = self.data.drop('converti', axis = 1) 
        self.y = self.data['converti'].values 

    def _split_data(self):
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split( self.X, self.y , test_size = 0.2 , random_state = 42 )


    def _pipeline(self):
        #Defining the steps in the categorical pipeline 
        categorical_pipeline = Pipeline( steps = [ ( 'cat_selector', FeatureSelector(self.categorical_features) ),
                                        ( 'cat_transformer', CategoricalTransformer() ) ] )
        
        #Defining the steps in the numerical pipeline     
        numerical_pipeline = Pipeline( steps = [ ( 'num_selector', FeatureSelector(self.numerical_features) ),
                                        
                                        ( 'num_transformer', NumericalTransformer() ) ] )

        #Combining numerical and categorical piepline into one full big pipeline horizontally 
        #using FeatureUnion
        union_pipeline = FeatureUnion( transformer_list = [ ( 'categorical_pipeline', categorical_pipeline ), 
                                                    
                                                    ( 'numerical_pipeline', numerical_pipeline ) ] )

        full_pipeline = Pipeline( steps = [ ( 'union_pipeline', union_pipeline), ( 'model', modele ) ] )
        return full_pipeline


    def train(self):
        _separate_target_and_feature()
        _split_data():
        full_pipeline = _pipeline()
        #Can call fit on it just like any other pipeline
        full_pipeline.fit( self.X_train, self.y_train )

    def prediction_with_data_test(self):
        #Can predict with it like any other pipeline
        y_pred = full_pipeline.predict( self.X_val )

import numpy as np 
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion, Pipeline 

if __name__ == "__main__":

 
    #Defining the steps in the categorical pipeline 
    categorical_pipeline = Pipeline( steps = [ ( 'cat_selector', FeatureSelector(categorical_features) ),
                                    ( 'cat_transformer', CategoricalTransformer() ) ] )
    
    #Defining the steps in the numerical pipeline     
    numerical_pipeline = Pipeline( steps = [ ( 'num_selector', FeatureSelector(numerical_features) ),
                                    
                                    ( 'num_transformer', NumericalTransformer() ) ] )

    #Combining numerical and categorical piepline into one full big pipeline horizontally 
    #using FeatureUnion
    union_pipeline = FeatureUnion( transformer_list = [ ( 'categorical_pipeline', categorical_pipeline ), 
                                                
                                                ( 'numerical_pipeline', numerical_pipeline ) ] )

    full_pipeline = Pipeline( steps = [ ( 'union_pipeline', union_pipeline), ( 'model', modele ) ] )

   
    full_pipeline = _pipeline()
    #Can call fit on it just like any other pipeline
    full_pipeline.fit( self.X_train, self.y_train )

    #Can predict with it like any other pipeline
    y_pred = full_pipeline.predict( self.X_val )

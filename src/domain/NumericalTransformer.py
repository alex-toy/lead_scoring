from sklearn.base import BaseEstimator, TransformerMixin


#Custom transformer we wrote to engineer features 
class NumericalTransformer(BaseEstimator, TransformerMixin):
    #Class Constructor
    def __init__( self, param ):
        self.param = param
        
    #Return self, nothing else to do here
    def fit( self, X, y = None ):
        return self 
    
    #Custom transform method we wrote that creates aformentioned features and drops redundant ones 
    def transform(self, X, y = None):
        return X[]

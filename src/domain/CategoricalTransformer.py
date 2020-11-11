#Custom transformer that converts certain features to binary or numerical value
class CategoricalTransformer( BaseEstimator, TransformerMixin ):
    #Class constructor method that takes in a list of values as its argument
    def __init__(self, param):
        self.param = param

    #Return self nothing else to do here
    def fit( self, X, y = None  ):
        return self

    def transform(self, X , y = None ):
        return X[]

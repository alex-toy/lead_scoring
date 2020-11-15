from sklearn.base import BaseEstimator, TransformerMixin

#Custom transformer we wrote to engineer features 
class NumericalTransformer(BaseEstimator, TransformerMixin):
    
    #Class Constructor
    def __init__( self ) :
        pass
        
    #Return self, nothing else to do here
    def fit( self, X, y = None ) :
        return self 

    #Custom transform that replace ouliers by the maximum value 
    def transform(self, X , y = None ):
        new_X =X

        #remove outliers
        new_X.loc[new_X ['NB_VISITES'] > 50,['NB_VISITES']] = 50 
        new_X.loc[new_X ['NB_PAGES_VUES_PAR_VISITE'] > 20, ['NB_PAGES_VUES_PAR_VISITE']] = 20

        return new_X 
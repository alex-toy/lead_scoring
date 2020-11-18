# Lead Scoring Alessio Marieme

The aim of the project is to build a machine learning model in which a score is given to each of the leads such that prospects with a higher score have a bigger chance of conversion and vice versa.

lead-scoring-alessio-marieme
├── data
│   └── data                         
│                                 
├── notebooks
│   ├── phase_exploratoire
│   ├── Recherche_Modele                                               
│   └── Intelligibilite
│
├── src                                                             
│   ├── __init__.py
│   ├── infrastructur
│   │   ├── __init__.py
│   │   └── CleanDataTransformer.py                           
│   ├── domain
│   │   ├── __init__.py
│   │   ├── CategoricalTransformer.py
│   │   ├── NumericalTransformer.py    
│   │   ├── pipeline_tranformer.py                                          
│   │   └── FeatureSelector.py
│   ├── application
│   │   ├── __init__.py
│   │   ├── predict.py
│   │   ├── train_model.py
│   │   └── main.py
│   └── postprocessing.py
├── .gitignore                                                     
├── poetry.lock
├── pyproject.toml                                            
├── README.md                                                       
└── assignement
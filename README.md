# Lead Scoring Alessio Marieme 
========================================================

The aim of the project is to build a machine learning model in which a score is given to each of the leads such that prospects with a higher score have a bigger chance of conversion and vice versa.

Before running anything :

- go into the folders predict and data and read the README.md files inside.
- create folders /models and /output at the root.


example of use:

    >>> from leads_scoring_marieme_alessio.pipeline_transformer import pipeline_transformer
    >>> pipeline_transformer()


.
├── README.md
├── activate.sh
├── assignment
│   └── Lead Scoring - Data Dictionary.pdf
├── data
│   └── README.md
├── init.sh
├── lead_scoring_marieme_alessio
│   ├── __init__.py
│   ├── application
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── predict.py
│   │   └── train_model.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── use_der_act.txt
│   │   ├── use_qualite_lead.txt
│   │   └── use_tags.txt
│   ├── domain
│   │   ├── __init__.py
│   │   ├── categorical_transformer.py
│   │   ├── evaluate_model.py
│   │   ├── feature_selector.py
│   │   ├── gb_pipeline.py
│   │   ├── log_reg_pipeline.py
│   │   ├── numerical_transformer.py
│   │   ├── perf.txt
│   │   ├── pipeline_transformer.py
│   │   ├── rand_for_pipeline.py
│   │   └── svc_pipeline.py
│   └── infrastructure
│       ├── __init__.py
│       └── clean_data_transformer.py
├── logs
│   └── lead_scoring_info_log.log
├── notebook
│   ├── data_model_rf.pickle
│   ├── exploration_finale.ipynb
│   ├── gridsearch.ipynb
│   ├── rf_interpretability.ipynb
│   └── utils
│       ├── Icon\015
│       ├── __init__.py
│       ├── mltask.py
│       ├── plot.py
│       └── postprocessing.py
├── poetry.lock
├── predict
│   └── README.md
└── pyproject.toml

## Prerequisite: install the last version of poetry if you haven't installed it yet 
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
$ poetry config virtualenvs.in-project true

## 0. Clone this repository

```
$ git clone <this project>
$ cd <this project>
```

## 1. Setup your virtual environment and activate it

Goal : create a local virtual environment with poetry in the folder `./.venv/`.

- First: check your python3 version:

    ```
    $ python3 --version
    # examples of outputs: 
    Python 3.6.2 :: Anaconda, Inc.
    Python 3.8.5 (this code was written with this version)

    $ which python3
    /Users/benjamin/anaconda3/bin/python3
    /usr/bin/python3
    ```

    - If you don't have python3 and you are working on your mac: install it from [python.org](https://www.python.org/downloads/)
    - If you don't have python3 and are working on an ubuntu-like system: install from package manager:

        ```
        $ apt-get update
        $ apt-get -y install python3 python3-pip python3-venv
        ```

- Now that python3 is installed create your environment, install the project's requirements and activate it:

    ```
    $ make init
    $ source activate.sh
    if you see error like this: bash: .venv/bin/activate: Permission denied
    do : chmod 741 .venv/bin/activate before doing source activate.sh
    ```

    You sould **allways** activate your environment when working on the project.

    If it fails with one of the following message :
    ```
    "ERROR: failed to create the .venv : do it yourself!"
    "ERROR: failed to activate virtual environment .venv! ask for advice on #dev "
    ```

    instructions on how to create an environment by yourself:
        if you have a pyproject.toml file in the folder do:
            $ poetry install 
        else 
            $ poetry init
            $ install the modules in the pyproject.toml in gitlab by doing: poetry add <name_module>




## 2. Start using the app

- You first want to train the models :

    - activate the python environment : source activate.sh

    - put your csv file containing data as well as target (CONVERTI) in the data folder at the root of the project.

    - cd into lead_scoring_marieme_alessio/application

    - run python main.py and choose option 1 (default)

    - if everything runs correctly, the application has created different .joblib files in the models folder.


- You now want to make predictions :

    - put your csv file that you want to get predictions for in the predict folder.

    - run python main.py

    - choose option 2.

    - enter the name of the file (defaults to data.csv)

    - choose your strategy :

        - option 1 (default) : you can choose your model based on all the available .joblib files that you have previously created.

        - option 2 : the application has stored in the lead_scoring_marieme_alessio/domain the perf.txt file that contains the precision of all available models. Based on that it will choose the best model for you.

    - if everything runs properly you can get your csv file containing a new PREDICTED_PROBABILITY column in the lead-scoring-alessio-marieme/output folder.

    - the application now offers to retrieve your data based on a threshold.


You can also run the notebook/gridsearch.ipynb notebook if you want to grid search your model. it will produce a best_params.json file in the notebook folder. The application will then automatically use those parameters when training the models.








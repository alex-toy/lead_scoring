import app.config.config as cf
import os

from sklearn.model_selection import train_test_split

from app.domain.pip_log_reg import log_reg_pipeline
from app.domain.pip_knn import knneighboors_pipeline
from app.domain.pip_rand_for import rand_for_pipeline
from app.domain.pip_svc import svc_pipeline
from app.domain.pip_gb import gb_pipeline

from app.domain.evaluate_model import evaluate_model

from app.infrastructure.CustomerProcessor import CustomerProcessor

import logging


if __name__ == '__main__':
    """
    Trains and evaluates models thanks to provided pipelines
    Gives the user information to be able to choose among the models    
    """


    logging.basicConfig(format=cf.LOGGING_FORMAT, filename=cf.FILE_LOG, level=logging.INFO)
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    logger = logging.getLogger('tcpserver')


    logger.info('Run play_file: %s', 'loading data', extra=d)
    cp = CustomerProcessor(path=cf.FILE_DATA)
    data = cp.load_cleaned_data()
    X = data.drop(cf.TARGET, axis = 1)
    y = data[cf.TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    nb_expl = str(len(y_test))
    nb_pos_expl = str(sum(y_test))
    nb_neg_expl = str(len(y_test) - sum(y_test))
    print('Number of examples : ' + nb_expl)
    print('Number of positive examples : ' + nb_pos_expl)
    print('Number of negative examples : ' + nb_neg_expl)


    file_path = os.path.join(os.path.os.getcwd(), cf.PERF_FILE)
    f = open(file_path, "a")
    f.truncate(0)
    f.close()


    print('*'*50)
    print('Logistic regression')
    logger.info('Run train_model: %s', 'initiated Logistic regression training job', extra=d)
    evaluate_model(log_reg_pipeline, X_train, X_test, y_train, y_test, cf.LOG_REG_MODEL_FILE)
    

    print('*'*50)
    print('Random forest')
    logger.info('Run train_model: %s', 'initiated random forest training job', extra=d)
    evaluate_model(rand_for_pipeline, X_train, X_test, y_train, y_test, cf.RF_MODEL_FILE)


    print('*'*50)
    print('Gradient boosting')
    logger.info('Run train_model: %s', 'initiated gradient boosting training job', extra=d)
    evaluate_model(gb_pipeline, X_train, X_test, y_train, y_test, cf.GB_MODEL_FILE)
    
    


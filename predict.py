
import pandas as pd

import joblib
import config


def make_prediction(input_data):
    
    _pipe_price = joblib.load(filename=config.PIPELINE_NAME)
    
    results = _pipe_price.predict(input_data)

    return results
    
   
if __name__ == '__main__':
    
    # test pipeline
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import  accuracy_score

    data = pd.read_csv(config.TESTING_DATA_FILE)

    input_data = data[config.FEATURES]


    '''
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.1,
        random_state=0)
    '''
    
    pred = make_prediction(input_data)

    print(pred)


    
    # determine accuracy
    #print('test accuracy: {}'.format(int(accuracy_score(y_test, pred))))
    '''
    print('test rmse: {}'.format(int(
        np.sqrt(mean_squared_error(y_test, np.exp(pred))))))
    print('test r2: {}'.format(
        r2_score(y_test, np.exp(pred))))
    print()
    '''


from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

import preprocessors as pp
import config


price_pipe = Pipeline(
    [
        ('categorical_imputer',
            pp.CategoricalImputer(variables=config.CATEGORICAL_VARS_WITH_NA)),
         
        ('numerical_inputer',
            pp.NumericalImputer(variables=config.NUMERICAL_VARS_WITH_NA)),
         
         
        ('rare_label_encoder',
            pp.RareLabelCategoricalEncoder(
                tol=0.01,
                variables=config.CATEGORICAL_VARS)),
         
        ('categorical_encoder',
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
         
 
        ('random_forest', RandomForestClassifier(n_estimators=100, random_state=0))
    ]
)

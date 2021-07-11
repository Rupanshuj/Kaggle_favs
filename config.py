
# data
TRAINING_DATA_FILE = "train.csv"
TESTING_DATA_FILE = "test.csv"
PIPELINE_NAME = 'random_forest'

TARGET = 'target'

# input variables 
FEATURES = ['v4', 'v6', 'v9', 'v10', 'v12', 'v14', 'v16', 'v18', 'v19', 'v21', 'v34',
       'v36', 'v38', 'v39', 'v40', 'v45', 'v50', 'v53', 'v57', 'v58', 'v62', 'v68', 'v69', 'v72',
       'v80', 'v81', 'v82', 'v85', 'v88', 'v90', 'v93', 'v98', 'v99', 'v100', 'v114', 'v115',
       'v119', 'v120', 'v123', 'v124', 'v127', 'v129','v22', 'v24', 'v30', 'v31', 'v47', 'v52', 'v56', 'v66', 'v71', 'v75', 'v79', 'v112', 'v113',
       'v125']



# numerical variables with NA in train set
NUMERICAL_VARS_WITH_NA = ['v4', 'v6', 'v9', 'v10', 'v12', 'v14', 'v16', 'v18', 'v19', 'v21', 'v34',
       'v36', 'v39', 'v40', 'v45', 'v50', 'v53', 'v57', 'v58',  'v68', 'v69', 
       'v80', 'v81', 'v82', 'v85', 'v88', 'v90', 'v93', 'v98', 'v99', 'v100', 'v114', 'v115',
       'v119', 'v120', 'v123', 'v124', 'v127']

# categorical variables with NA in train set
CATEGORICAL_VARS_WITH_NA = ['v22', 'v30', 'v31', 'v52', 'v56', 'v112', 'v113', 'v125']

#TEMPORAL_VARS = ''

# variables to log transform
#NUMERICALS_LOG_VARS = ['LotFrontage', '1stFlrSF', 'GrLivArea']

# categorical variables to encode
CATEGORICAL_VARS = ['v22', 'v24', 'v30', 'v31', 'v47', 'v52', 'v56', 'v66', 'v71', 'v75', 'v79', 'v112', 'v113',
       'v125']

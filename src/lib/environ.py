import os

abs_lambda = lambda x: os.path.abspath(x)
CUR_FILE_PATH = abs_lambda(os.path.dirname(__file__))
ROOT_DIR_PATH= abs_lambda(os.path.join(CUR_FILE_PATH, os.pardir, os.pardir))
CONF_PATH = abs_lambda(os.path.join(ROOT_DIR_PATH, 'conf'))
DATA_PATH = abs_lambda(os.path.join(ROOT_DIR_PATH, 'data'))
LOG_PATH = abs_lambda(os.path.join(ROOT_DIR_PATH, 'log'))
RESOURCE_PATH = abs_lambda(os.path.join(ROOT_DIR_PATH, 'src', 'resource'))



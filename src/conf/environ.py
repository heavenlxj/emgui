import sys
import os

abs_lambda = lambda x: os.path.abspath(x)
CONF_PATH = abs_lambda(os.path.dirname(__file__))
ROOT_DIR_PATH= abs_lambda(os.path.join(CONF_PATH, os.pardir))
SCHEMA_PATH = abs_lambda(os.path.join(ROOT_DIR_PATH, 'schema'))



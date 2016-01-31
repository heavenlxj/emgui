import logging
import logging.handlers
import math
from collections import OrderedDict

from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QValidator,QRegExpValidator,QMessageBox

from lib.environ import *
from dao.initital import parse


class Utils():

    def __init__(self):
        pass

    FORMAT_PATTERN = '(([0-9][0-9]|1[0-9][0-9])-[0-9][0-9]\.[0-9][0-9][0-9] (N|S|W|E))'

    @staticmethod
    def getCountryPortsMapper():
        mapper=OrderedDict()
        try:
            file_path = os.path.join(CONF_PATH, 'country_port.csv')

            fp = open(file_path, 'r')
        except IOError, ex:
            #TODO open error prompt dialog
            msg_box = QMessageBox(QMessageBox.Critical, "Error", str(ex))
            msg_box.exec_()
            return None

        all = fp.readlines()
        for item in all:
            list = item.split(',')
            country,port = list[1],list[0]
            country = country.replace('\n', '')
            if mapper.has_key(country):
                mapper[country].append(port)
            else:
                mapper[country]=[port]

        return mapper

    @staticmethod
    def readGeneralConfigFromXml():
        config = {}
        config_file = abs_lambda(os.path.join(DATA_PATH, 'initial.xml'))
        if os.path.exists(config_file):
            try:
                root = parse(config_file, silence=True)
                config['ship_name'] = root.Property.ship_name
                config['call_sign'] = root.Property.call_sign
                config['captain_name'] = root.Property.captain_name
            except Exception, ex:
                return None, 'Parse config file failed, please check the schema. \n' + str(ex)

            return config, 'Load general data successfully'
        else:
            return None, 'General data could not be loaded due to the initial configs not generated'

    @staticmethod
    def checkState(value, pattern):
        regexp = QRegExp(pattern)
        validator = QRegExpValidator(regexp)
        state = validator.validate(value, 0)[0]
        if state == QValidator.Acceptable:
            return True
        else:
            return False

    @staticmethod
    def createDateDir():
        #create data directory
        data_dir = os.path.join(ROOT_DIR_PATH, 'data')
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)

        return data_dir

    @staticmethod
    def setupLogger(name, fn=None, level=logging.DEBUG):

        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            formatter = logging.Formatter("%(asctime)s-[%(name)s]-[%(levelname)s]: %(message)s")
            handler = logging.handlers.TimedRotatingFileHandler(fn, 'D')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger

    @staticmethod
    def calCourseGCFormula(s_lat, s_long, d_lat, d_long):
        pass

    @staticmethod
    def calCourseRLFormula(s_lat, s_long, d_lat, d_long):
        pass

    @staticmethod
    def calDistanceGCFormula(s_lat, s_long, d_lat, d_long):
        pass

    @staticmethod
    def calDistanceRLFormula(s_lat, s_long, d_lat, d_long):
        pass

    @staticmethod
    def sign(x):
        if x==0:
            return 0
        elif x<0:
            return -1
        else:
            return 1
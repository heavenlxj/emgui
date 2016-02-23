import logging
import logging.handlers
from math import *
from collections import OrderedDict

from PyQt4.QtCore import QRegExp
from PyQt4.QtGui import QValidator,QRegExpValidator,QMessageBox

from lib.environ import *
from dao.initital import parse

E = 0.0818191908426215

class PointType:
    LATITUDE = 0
    LONGTITUDE = 1

class Utils():

    def __init__(self):
        pass

    FORMAT_PATTERN = '(([0-9][0-9]|1[0-9][0-9])-[0-9][0-9]\.[0-9][0-9][0-9] (N|S|W|E))'
    LATITUDE_PATTERN = '(-?[0-8][0-9][0-5][0-9])((\.[0-9]{1,3})?)'
    LONGTITUDE_PATTERN = '(-?)(([0-9][0-9])|[0-1][0-7][0-9])([0-5][0-9])((\.[0-9]{1,3})?)'

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
    def _formatLatitude(value):

        if value.startswith('-'):
            orient = 'S'
        else:
            orient = 'N'
        temp_value = value.strip('-')
        deg = temp_value[:2]
        min = temp_value[2:]
        dot_index = temp_value.find('.')
        if dot_index != -1:
            float_part = str(temp_value[dot_index+1:])
            float_len = len(float_part)
            zero_pad = '0' * (3-float_len)
        else:
            zero_pad = '.000'

        format_value = str.format('{0}-{1} {2}', str(deg), str(min)+zero_pad, orient)
        return format_value


    @staticmethod
    def _formatLongtitude(value):
        if value.startswith('-'):
            orient = 'W'
        else:
            orient = 'E'
        temp_value = value.strip('-')
        temp_list = temp_value.split('.')
        part1 = temp_list[0]
        deg=0
        min=0
        zero_pad=''
        if len(part1)==4:
            deg=part1[:2]
            min=part1[2:]
        elif len(part1)==5:
            deg=part1[:3]
            min=part1[3:]
        if temp_list>1:
            part2 = temp_list[1]
            min=min+'.'+part2
            if len(part2) < 3:
                zero_pad = '0' * (3-len(part2))
                min=min+zero_pad
        else:
            zero_pad = '000'
            min=min+'.'+zero_pad

        format_value = str.format('{0}-{1} {2}', str(deg), str(min), orient)
        return format_value

    @staticmethod
    def formatPoint(value, type):
        pattern = None
        if type == PointType.LATITUDE:
            pattern = Utils.LATITUDE_PATTERN
        else:
            pattern = Utils.LONGTITUDE_PATTERN

        if Utils.checkState(value, pattern):
            temp_value = str(value)
            if type == PointType.LATITUDE:
                format_value = Utils._formatLatitude(temp_value)
            else:
                format_value = Utils._formatLongtitude(temp_value)
            return format_value
        elif Utils.checkState(value, Utils.FORMAT_PATTERN):
            return value
        else:
            return '#VALUE!'


    @staticmethod
    def createDataDir():
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
        res = ''
        if s_lat.isEmpty() or s_long.isEmpty() or d_lat.isEmpty() or d_long.isEmpty():
            res='END'
        else:
            s_lat = float(s_lat)
            s_long = float(s_long)
            d_lat = float(d_lat)
            d_long = float(d_long)

            dis = 180-90*((1+ Utils.sign(d_lat-s_lat))*Utils.sign(d_long-s_long))
            mid_v = sin(radians(d_long-s_long))/(cos(radians(s_lat))*tan(radians(d_lat))-sin(radians(s_lat))*cos(radians(d_long-s_long)))
            course= dis + degrees(atan(mid_v))

            res = '%.4f' % course
        return res

    @staticmethod
    def calCourseRLFormula(s_lat, s_long, d_lat, d_long):
        res = ''
        if s_lat.isEmpty() or s_long.isEmpty() or d_lat.isEmpty() or d_long.isEmpty():
            res='END'
        else:
            s_lat = float(s_lat)
            s_long = float(s_long)
            d_lat = float(d_lat)
            d_long = float(d_long)

            dis = 180-90*((1+ Utils.sign(d_lat-s_lat))*Utils.sign(d_long-s_long))
            mid_v = 180/pi*(atan(radians(d_long-s_long)/(atanh(sin(radians(d_lat)))-atanh(sin(radians(s_lat)))-E*atanh(E*sin(radians(d_lat)))+E*atanh(E*sin(radians(s_lat))))))
            course= dis + mid_v
            res = '%.4f' % course
        return res

    @staticmethod
    def calDistanceGCFormula(s_lat, s_long, d_lat, d_long):
        res = ''
        if s_lat.isEmpty() or s_long.isEmpty() or d_lat.isEmpty() or d_long.isEmpty():
            res='END'
        else:
            s_lat = float(s_lat)
            s_long = float(s_long)
            d_lat = float(d_lat)
            d_long = float(d_long)

            distance = 60*degrees(acos(sin(radians(s_lat))*sin(radians(d_lat))+cos(radians(s_lat))*cos(radians(d_lat))*cos(radians(d_long-s_long))))
            res = '%.4f' % distance
        return res

    @staticmethod
    def calDistanceRLFormula(s_lat, s_long, d_lat, d_long):
        res = ''
        if s_lat.isEmpty() or s_long.isEmpty() or d_lat.isEmpty() or d_long.isEmpty():
            res='END'
        else:
            course = float(Utils.calCourseRLFormula(s_lat, s_long, d_lat, d_long))
            distance = (float(d_lat)-float(s_lat))*60/cos(radians(course))
            res = '%.4f' % distance
        return res

    @staticmethod
    def sign(x):
        if x==0:
            return 0
        elif x<0:
            return -1
        else:
            return 1
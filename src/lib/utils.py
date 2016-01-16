
from conf.environ import *
from collections import OrderedDict
from dao.initital import parse

class Utils():

    def __init__(self):
        pass

    @staticmethod
    def getCountryPortsMapper():
        mapper=OrderedDict()
        try:
            file_path = os.path.join(CONF_PATH, 'country_port.csv')
            fp = open(file_path, 'r')
        except IOError, ex:
            #TODO open error prompt dialog
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
        config_file = SCHEMA_PATH + '/initial.xml'
        if os.path.exists(config_file):
            root = parse(config_file)
            print root
        else:
            return None

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
        config_file = abs_lambda(os.path.join(SCHEMA_PATH, 'initial.xml'))
        if os.path.exists(config_file):
            try:
                root = parse(config_file)
                config['ship_name'] = root.Property.ship_name
                config['call_sign'] = root.Property.call_sign
                config['voyage_number'] = root.Property.voyage_number
                config['captain_name'] = root.Property.captain_name
                config['date'] = root.Property.date
            except Exception, ex:
                return None, 'Parse config file failed, please check the schema. \n' + str(ex)

            return root, 'Load general data successfully'
        else:
            return None, 'General data could not be loaded due to the initial configs not generated'
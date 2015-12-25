#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Mon Dec 21 23:24:04 2015 by generateDS.py version 2.17a.
#
# Command line options:
#   ('--use-getter-setter', 'none')
#   ('-o', 'D:\\GitRepo\\emgui\\src\\dao\\request.py')
#
# Command line arguments:
#   D:\GitRepo\emgui\src\schema\request.xsd
#
# Command line:
#   E:\Python27\Scripts\generateDS.py --use-getter-setter="none" -o "D:\GitRepo\emgui\src\dao\request.py" D:\GitRepo\emgui\src\schema\request.xsd
#
# Current working directory (os.getcwd()):
#   Scripts
#
from base import *

#
# Data representation classes.
#


class Property(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, ship_name=None, call_sign=None, voyage_number=None, date=None, voyage_detail=None, via=None, use_dw_route=None, maximum_draft=None, load_condition=None, speed_setting=None, etd=None):
        self.original_tagname_ = None
        self.ship_name = ship_name
        self.call_sign = call_sign
        self.voyage_number = voyage_number
        if isinstance(date, basestring):
            initvalue_ = datetime_.datetime.strptime(date, '%Y-%m-%d').date()
        else:
            initvalue_ = date
        self.date = initvalue_
        self.voyage_detail = voyage_detail
        self.via = via
        self.use_dw_route = use_dw_route
        self.maximum_draft = maximum_draft
        self.load_condition = load_condition
        self.speed_setting = speed_setting
        self.etd = etd
    def factory(*args_, **kwargs_):
        if Property.subclass:
            return Property.subclass(*args_, **kwargs_)
        else:
            return Property(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.ship_name is not None or
            self.call_sign is not None or
            self.voyage_number is not None or
            self.date is not None or
            self.voyage_detail is not None or
            self.via is not None or
            self.use_dw_route is not None or
            self.maximum_draft is not None or
            self.load_condition is not None or
            self.speed_setting is not None or
            self.etd is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='Property', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='Property')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='Property', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='Property'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='Property', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ship_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sship_name>%s</%sship_name>%s' % (namespace_, self.gds_format_string(quote_xml(self.ship_name).encode(ExternalEncoding), input_name='ship_name'), namespace_, eol_))
        if self.call_sign is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scall_sign>%s</%scall_sign>%s' % (namespace_, self.gds_format_string(quote_xml(self.call_sign).encode(ExternalEncoding), input_name='call_sign'), namespace_, eol_))
        if self.voyage_number is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svoyage_number>%s</%svoyage_number>%s' % (namespace_, self.gds_format_string(quote_xml(self.voyage_number).encode(ExternalEncoding), input_name='voyage_number'), namespace_, eol_))
        if self.date is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdate>%s</%sdate>%s' % (namespace_, self.gds_format_date(self.date, input_name='date'), namespace_, eol_))
        if self.voyage_detail is not None:
            self.voyage_detail.export(outfile, level, namespace_, name_='voyage_detail', pretty_print=pretty_print)
        if self.via is not None:
            self.via.export(outfile, level, namespace_, name_='via', pretty_print=pretty_print)
        if self.use_dw_route is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suse_dw_route>%s</%suse_dw_route>%s' % (namespace_, self.gds_format_boolean(self.use_dw_route, input_name='use_dw_route'), namespace_, eol_))
        if self.maximum_draft is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smaximum_draft>%s</%smaximum_draft>%s' % (namespace_, self.gds_format_string(quote_xml(self.maximum_draft).encode(ExternalEncoding), input_name='maximum_draft'), namespace_, eol_))
        if self.load_condition is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sload_condition>%s</%sload_condition>%s' % (namespace_, self.gds_format_string(quote_xml(self.load_condition).encode(ExternalEncoding), input_name='load_condition'), namespace_, eol_))
        if self.speed_setting is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sspeed_setting>%s</%sspeed_setting>%s' % (namespace_, self.gds_format_string(quote_xml(self.speed_setting).encode(ExternalEncoding), input_name='speed_setting'), namespace_, eol_))
        if self.etd is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%setd>%s</%setd>%s' % (namespace_, self.gds_format_string(quote_xml(self.etd).encode(ExternalEncoding), input_name='etd'), namespace_, eol_))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ship_name':
            ship_name_ = child_.text
            ship_name_ = self.gds_validate_string(ship_name_, node, 'ship_name')
            self.ship_name = ship_name_
        elif nodeName_ == 'call_sign':
            call_sign_ = child_.text
            call_sign_ = self.gds_validate_string(call_sign_, node, 'call_sign')
            self.call_sign = call_sign_
        elif nodeName_ == 'voyage_number':
            voyage_number_ = child_.text
            voyage_number_ = self.gds_validate_string(voyage_number_, node, 'voyage_number')
            self.voyage_number = voyage_number_
        elif nodeName_ == 'date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.date = dval_
        elif nodeName_ == 'voyage_detail':
            obj_ = voyage_detail.factory()
            obj_.build(child_)
            self.voyage_detail = obj_
            obj_.original_tagname_ = 'voyage_detail'
        elif nodeName_ == 'via':
            obj_ = via.factory()
            obj_.build(child_)
            self.via = obj_
            obj_.original_tagname_ = 'via'
        elif nodeName_ == 'use_dw_route':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'use_dw_route')
            self.use_dw_route = ival_
        elif nodeName_ == 'maximum_draft':
            maximum_draft_ = child_.text
            maximum_draft_ = self.gds_validate_string(maximum_draft_, node, 'maximum_draft')
            self.maximum_draft = maximum_draft_
        elif nodeName_ == 'load_condition':
            load_condition_ = child_.text
            load_condition_ = self.gds_validate_string(load_condition_, node, 'load_condition')
            self.load_condition = load_condition_
        elif nodeName_ == 'speed_setting':
            speed_setting_ = child_.text
            speed_setting_ = self.gds_validate_string(speed_setting_, node, 'speed_setting')
            self.speed_setting = speed_setting_
        elif nodeName_ == 'etd':
            etd_ = child_.text
            etd_ = self.gds_validate_string(etd_, node, 'etd')
            self.etd = etd_
# end class Property


class departure(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, country=None, port=None, unlo_code=None, terminal=None):
        self.original_tagname_ = None
        self.country = country
        self.port = port
        self.validate_port(self.port)
        self.unlo_code = unlo_code
        self.terminal = terminal
    def factory(*args_, **kwargs_):
        if departure.subclass:
            return departure.subclass(*args_, **kwargs_)
        else:
            return departure(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_port(self, value):
        # Validate type port, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.country is not None or
            self.port is not None or
            self.unlo_code is not None or
            self.terminal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='departure', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='departure')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='departure', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='departure'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='departure', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.country is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountry>%s</%scountry>%s' % (namespace_, self.gds_format_string(quote_xml(self.country).encode(ExternalEncoding), input_name='country'), namespace_, eol_))
        if self.port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sport>%s</%sport>%s' % (namespace_, self.gds_format_string(quote_xml(self.port).encode(ExternalEncoding), input_name='port'), namespace_, eol_))
        if self.unlo_code is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunlo_code>%s</%sunlo_code>%s' % (namespace_, self.gds_format_string(quote_xml(self.unlo_code).encode(ExternalEncoding), input_name='unlo_code'), namespace_, eol_))
        if self.terminal is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sterminal>%s</%sterminal>%s' % (namespace_, self.gds_format_string(quote_xml(self.terminal).encode(ExternalEncoding), input_name='terminal'), namespace_, eol_))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'country':
            country_ = child_.text
            country_ = self.gds_validate_string(country_, node, 'country')
            self.country = country_
        elif nodeName_ == 'port':
            port_ = child_.text
            port_ = self.gds_validate_string(port_, node, 'port')
            self.port = port_
            # validate type port
            self.validate_port(self.port)
        elif nodeName_ == 'unlo_code':
            unlo_code_ = child_.text
            unlo_code_ = self.gds_validate_string(unlo_code_, node, 'unlo_code')
            self.unlo_code = unlo_code_
        elif nodeName_ == 'terminal':
            terminal_ = child_.text
            terminal_ = self.gds_validate_string(terminal_, node, 'terminal')
            self.terminal = terminal_
# end class departure


class destination(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, country=None, port=None, unlo_code=None, terminal=None):
        self.original_tagname_ = None
        self.country = country
        self.port = port
        self.validate_port(self.port)
        self.unlo_code = unlo_code
        self.terminal = terminal
    def factory(*args_, **kwargs_):
        if destination.subclass:
            return destination.subclass(*args_, **kwargs_)
        else:
            return destination(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_port(self, value):
        # Validate type port, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.country is not None or
            self.port is not None or
            self.unlo_code is not None or
            self.terminal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='destination', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='destination')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='destination', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='destination'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='destination', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.country is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountry>%s</%scountry>%s' % (namespace_, self.gds_format_string(quote_xml(self.country).encode(ExternalEncoding), input_name='country'), namespace_, eol_))
        if self.port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sport>%s</%sport>%s' % (namespace_, self.gds_format_string(quote_xml(self.port).encode(ExternalEncoding), input_name='port'), namespace_, eol_))
        if self.unlo_code is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunlo_code>%s</%sunlo_code>%s' % (namespace_, self.gds_format_string(quote_xml(self.unlo_code).encode(ExternalEncoding), input_name='unlo_code'), namespace_, eol_))
        if self.terminal is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sterminal>%s</%sterminal>%s' % (namespace_, self.gds_format_string(quote_xml(self.terminal).encode(ExternalEncoding), input_name='terminal'), namespace_, eol_))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'country':
            country_ = child_.text
            country_ = self.gds_validate_string(country_, node, 'country')
            self.country = country_
        elif nodeName_ == 'port':
            port_ = child_.text
            port_ = self.gds_validate_string(port_, node, 'port')
            self.port = port_
            # validate type port
            self.validate_port(self.port)
        elif nodeName_ == 'unlo_code':
            unlo_code_ = child_.text
            unlo_code_ = self.gds_validate_string(unlo_code_, node, 'unlo_code')
            self.unlo_code = unlo_code_
        elif nodeName_ == 'terminal':
            terminal_ = child_.text
            terminal_ = self.gds_validate_string(terminal_, node, 'terminal')
            self.terminal = terminal_
# end class destination


class port(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self):
        self.original_tagname_ = None
    def factory(*args_, **kwargs_):
        if port.subclass:
            return port.subclass(*args_, **kwargs_)
        else:
            return port(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='port', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='port')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='port', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='port'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='port', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class port


class request_report(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Property=None):
        self.original_tagname_ = None
        self.Property = Property
    def factory(*args_, **kwargs_):
        if request_report.subclass:
            return request_report.subclass(*args_, **kwargs_)
        else:
            return request_report(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Property is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='request_report', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='request_report')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='request_report', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='request_report'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='request_report', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Property is not None:
            self.Property.export(outfile, level, namespace_, name_='Property', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Property':
            obj_ = Property.factory()
            obj_.build(child_)
            self.Property = obj_
            obj_.original_tagname_ = 'Property'
# end class request_report


class via(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, port=None):
        self.original_tagname_ = None
        if port is None:
            self.port = []
        else:
            self.port = port
    def factory(*args_, **kwargs_):
        if via.subclass:
            return via.subclass(*args_, **kwargs_)
        else:
            return via(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_port(self, value):
        # Validate type port, a restriction on xs:string.
        pass
    def hasContent_(self):
        if (
            self.port
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='via', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='via')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='via', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='via'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='via', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for port_ in self.port:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sport>%s</%sport>%s' % (namespace_, self.gds_format_string(quote_xml(port_).encode(ExternalEncoding), input_name='port'), namespace_, eol_))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'port':
            port_ = child_.text
            port_ = self.gds_validate_string(port_, node, 'port')
            self.port.append(port_)
            # validate type port
            self.validate_port(self.port[-1])
# end class via


class voyage_detail(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, departure=None, destination=None):
        self.original_tagname_ = None
        self.departure = departure
        self.destination = destination
    def factory(*args_, **kwargs_):
        if voyage_detail.subclass:
            return voyage_detail.subclass(*args_, **kwargs_)
        else:
            return voyage_detail(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.departure is not None or
            self.destination is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespace_='', name_='voyage_detail', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='voyage_detail')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_='', name_='voyage_detail', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='voyage_detail'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='voyage_detail', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.departure is not None:
            self.departure.export(outfile, level, namespace_, name_='departure', pretty_print=pretty_print)
        if self.destination is not None:
            self.destination.export(outfile, level, namespace_, name_='destination', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'departure':
            obj_ = departure.factory()
            obj_.build(child_)
            self.departure = obj_
            obj_.original_tagname_ = 'departure'
        elif nodeName_ == 'destination':
            obj_ = destination.factory()
            obj_.build(child_)
            self.destination = obj_
            obj_.original_tagname_ = 'destination'
# end class voyage_detail


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def parse(inFileName, silence=False):
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Property'
        rootClass = Property
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFileName, silence=False):
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Property'
        rootClass = Property
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Property'
        rootClass = Property
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFileName, silence=False):
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Property'
        rootClass = Property
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from request import *\n\n')
        sys.stdout.write('import request as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


__all__ = [
    "Property",
    "departure",
    "destination",
    "port",
    "request_report",
    "via",
    "voyage_detail"
]

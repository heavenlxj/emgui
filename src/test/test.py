import os,sys
sys.path.append('..')
import dao.initital as ini

obj = ini.initial_report()

f= open(r'd:\test.xml', 'w')
obj.export(f, 1)
pass








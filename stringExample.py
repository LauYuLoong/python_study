# -*- codeing: gbk -*-
from math import pi;
# from string import template;
import string;

if __name__ == '__main__':
	website = 'http://www.python.org';
	print website[-3:];

	formatStr = 'Hello %s. %s enough for ya?';
	values = ('world', 'hot');
	print formatStr % values;

	formatFlo = 'PI with three decimails: %.48f';
	print formatFlo % pi;

	# s = string.Template('$x, glorius $x!');
	# s.substitute(x='simon');
	# print s;

	print 'Price of Eggs: $%d' % 42;
	print 'Hexadecimal Price of Eggs: $%x' % 42;
	print 'Useing str: %s' % 42L;
	print 'Useing repr: %r' % 42L;
	print '%10f' % pi;
	print '%10.2f' % pi;
	print '%.2f' % pi;
	print '%.5s' % 'Guido van Rossum';
	print '%.*s' % (10,'Guido van Rossum');
	print '%010.2f' % pi;
	print '%-10.2f' % pi;
	print ('% 5d' % 10) + '\n' + ('% 5d' % -10);
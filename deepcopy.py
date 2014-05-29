# -*- encoding = gbk -*-

from copy import deepcopy

if __name__ == '__main__':
	d = {'names':['Alfred','Bertrand']}
	c = d.copy()
	dc = deepcopy(d)

	d['names'].append('Clive')

	print c
	print dc
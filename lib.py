# -*- encoding=gbk -*-

def fibs(num):
	'Use this function do fibs'
	result = [0, 1];
	for i in range(num - 2):
		result.append(result[-2] + result[-1]);

	return result;

__metaclass__ = type

class Person:
	"""docstring for Person"""
	def setName(self, name ):
		self.name = name;

	def getName(self):
		return self.name;

	def greet(self):
		print "Hello world! I'm %s" % self.name

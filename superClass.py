# -*- codeing: gbk -*-

class Fliter:
	"""docstring for fliter"""
	def __init__(self):
		self.blocked = []

	def fliter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
	"""docstring for SPAMFilter"""
	def __init__(self, arg):
		self.blocked = [SPAM]
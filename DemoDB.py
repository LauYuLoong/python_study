# -*- encoding=gbk -*-

if __name__ == '__main__':
	people = {
		'Alice':{
			'phone':'2341',
			'addr':'Foo Drive 23'
		},
		'Beth':{
			'phone':'4562',
			'addr':'Bar street 42'
		},
		'Cecil':{
			'phone':'3158',
			'addr':'Baz avenue 90'
		}
	}

	lables = {'phone':'phone number', 'addr':'address'}

	# name = raw_input('Name') or 'Beth'
	name = 'Beth'
	request = 'p'

	if request == 'p':
		key = 'phone'
	if request == 'a':
		key = 'addr'

	if name in people:
		print "%s's %s is %s" % (name, lables[key], people[name][key])
		 
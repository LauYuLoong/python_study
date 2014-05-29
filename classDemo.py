# -*- encoding=gbk -*-

from lib import Person;

if __name__ == '__main__':
	foo = Person();
	bar = Person();

	foo.setName('Luke Skywalker');
	bar.setName('Anakin Skywalker');

	foo.greet();
	bar.greet();

# -*- codeing:gbk -*-
if __name__ == '__main__':
	# width = raw_input( 'Please enter width:' )
	width = 35;

	price_Width = 10;
	item_Width = width - price_Width;

	header_format = '%-*s%*s';
	format = '%-*s%*.2f';

	print '=' * width;

	print header_format % (item_Width, 'ITEM', price_Width, 'PRICE');

	print '-' * width;

	print format % (item_Width, 'Apples', price_Width, 0.4);
	print format % (item_Width, 'Pears', price_Width, 0.5);
	print format % (item_Width, 'Cantaloupes', price_Width, 1.92);
	print format % (item_Width, 'Dired Apricots(16 oz)', price_Width, 8);
	print format % (item_Width, 'Prunes (4 lbs)', price_Width, 12);

	print '=' * width;
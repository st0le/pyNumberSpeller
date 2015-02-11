import random
# pyNumberSpeller

small_number = {
				0 : 'zero',
				1 : 'one',
				2 : 'two',
				3 : 'three',
				4 : 'four',
				5 : 'five',
				6 : 'six',
				7 : 'seven',
				8 : 'eight',
				9 : 'nine',
				10 : 'ten',
				11 : 'eleven',
				12 : 'twelve',
				13 : 'thirteen',
				14 : 'fourteen',
				15 : 'fifteen',
				16 : 'sixteen',
				17 : 'seventeen',
				18 : 'eighteen',
				19 : 'nineteen',
				20 : 'twenty',
				30 : 'thirty',
				40 : 'forty',
				50 : 'fifty',
				60 : 'sixty',
				70 : 'seventy',
				80 : 'eighty',
				90 : 'ninety',
				}

large_numbers = ['thousand','million','billion','trillion','quadrillion','quintillion','sextillion','septillion','octillion','nonillion','decillion','undecillion','duodecillion','tredecillion','quattuordecillion','quindecillion','sexdecillion','septendecillion','octodecillion','novemdecillion','vigintillion']

def spell(number):
	if number == 0: return small_number[number]

	def spell_below_1000(n):
		w = []
		if n >= 100:
			w.append('%s hundred' % small_number[n / 100])
		n %= 100
		if n > 0:
			if n in small_number:
				w.append(small_number[n])
			else:
				tens,units = divmod(n,10)
				w.append(small_number[tens * 10])
				w.append(small_number[units])
		return ' '.join(w)

	i = 0
	words = []
	neg = number < 0
	number = abs(number)
	while number > 0:
		number,last3 = divmod(number,1000)
		words.append(spell_below_1000(last3))
		if number > 0:
			words.append(large_numbers[i])
		i += 1
	if neg: words.append('minus')
	return ' '.join(reversed(words))


if __name__ == '__main__':
	for i in xrange(100):
		x = random.randint(-10**3,10**3)
		print x,spell(x)

# https://projecteuler.net/problem=31

import time

start = time.time()

def change_money(value=2, value_type='£'):
	if value_type in ['£', 'pound', 'pounds']:
		pence_value = value*100
	elif value_type in ['p', 'pence']:
		pence_value = value
	else:
		raise ValueError("value_type must me '£'' / 'pound' or 'p' / 'pence'")

	coins = [200, 100, 50, 20, 10, 5, 2, 1]

	pass # will be continued

print('evaluation time:', time.time() - start,'s')

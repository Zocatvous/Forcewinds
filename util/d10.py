import random as rand

def roll(num):
	r_list = []
	results_list = []
	for i in range(num):
		r_list.append(rand.randint(1,10))
	for item in r_list:
		if item == 10:
			results_list.append(2)
		elif item==7 or item==8 or item==9:
			results_list.append(1)
		else:results_list.append(0)
	return sum(results_list)

def dam_roll(num):
	r_list = []
	results_list = []
	for i in range(num):
		r_list.append(rand.randint(1,10))
	for item in r_list:
		if item==7 or item==8 or item==9 or item==10:
			results_list.append(1)
		else:results_list.append(0)
	return sum(results_list)

def adv_roll(num):
	r_list = []
	results_list = []
	for i in range(num):
		r_list.append(rand.randint(1,10))
	for item in r_list:
		if item == 10:
			results_list.append(2)
		elif item == 6 or item==7 or item==8 or item==9:
			results_list.append(1)
		else:results_list.append(0)
	return sum(results_list)


def adv_roll_dam(num):
	r_list = []
	results_list = []
	for i in range(num):
		r_list.append(rand.randint(1,10))
	for item in r_list:
		if item == 6 or item==7 or item==8 or item==9 or item==10:
			results_list.append(1)
		else:results_list.append(0)
	return sum(results_list)
# for i in range(1000):
# 	print("You rolled {} Successes".format(sum(roll(i))))
# 	time.sleep(1)


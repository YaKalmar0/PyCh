import random
def writf(fl_nm, trig):
	if trig == 1:
		file = open(fl_nm, "w")
	elif trig == 0:
		file = open(fl_nm, "wb")
	N = 10000
	i = 0
	if trig == 1:
		for i in range(N):
			file.write(str(random.randint(0, N)) + "\n")
	elif trig == 0:
		for i in range(N):
			n = random.randint(0, N)
			file.write(n.to_bytes(2, "little"))

	file.close()
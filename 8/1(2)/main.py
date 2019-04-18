import wr
import r

if __name__ == '__main__':
	flag = 0
	if flag == 1:
		file = "test.txt"
	elif flag == 0:
		file = "text.bin"
	wr.writf(file, flag)
	s = r.readf(file, flag)
	print("The sum =", s)
def readf(fl_nm, trig):
    if trig == 1:
        file = open(fl_nm, "r")
    elif trig == 0:
        file = open(fl_nm, "rb")
    sum = 0
    if trig == 1:
        for line in file:
            sum += int(line)
    elif trig == 0:
        import struct
        str = []
        for i in struct.unpack('<i', file.read(4)):
            str.append(i)
            sum += int(str[0])
    file.close()
    return sum


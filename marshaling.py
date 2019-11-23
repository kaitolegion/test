import marshal , base64
def ubah(huruf):
	e = ""
	e += str(ord(huruf))
	e += ','
	return e
def ubah1(a):
	global z
	z = ""
	for huruf in a:
		z += ubah(huruf)
	return z
def hasil():
	x = 'a=['+z+'];exec"".join([ chr(i) for i in a])'
	b = compile(x,'','exec')
	c = marshal.dumps(b)
	d = open('kaito.py','w')
	d.write('import marshal\n')
	d.write('exec(marshal.loads('+repr(c)+'))')
	d.close()
if __name__ == '__main__':
	print"Enter your Path."
	file = raw_input("[*] Path :~#")
	a = open(file,'r').read()
	ubah1(a)
	hasil()

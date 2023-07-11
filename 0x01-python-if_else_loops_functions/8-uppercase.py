def uppercase(s):
	for c in s:
	ascii_val = ord(c)
	if ascii_val >= 97 and ascii_val <= 122:
		ascii_val -= 32
	print(chr(ascii_val), end="")
	print()

with open("message.dat") as message:
	text = message.read()
	print(len(text.split()))
	print("".join([chr(int(bin_str, 2)) for bin_str in text.split(" ")]))

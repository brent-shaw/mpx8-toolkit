s = "This is a test"
h = s.encode("hex")
f = open("KIT1.KIT","w")
f.write(h)
f.close()

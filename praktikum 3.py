print("Akram Satya")
print("312210461\n")
print ("//Masukan input")
print ("Program menghitung luas dan keliling lingkaran")
print ("----------------------------------------------")

r = float(input('Masukan nilai jari-jari : '))

phi = 3.14
Diameter = 2*r

luas = phi*r*r
keliling = phi*Diameter
print('\nLuasnya =', str("%.2f" % luas))
print('kelilingnya =', str("%.2f" % keliling))
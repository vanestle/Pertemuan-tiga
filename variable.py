#multi assigment
a,b,c = 1,2,"Check"
print('a:',type(a),a)
print('a:',type(b),b)
print('a:',type(c),c)

print("================================")

#variable nilai yang sama
d = e = f = 10
print('d:',d)
print('e:',e)
print('f:',f)

nama = "peppy"
print(nama)

#tipe data numerik
#tipe float
panjang = 5
lebar = 10.5
luas = panjang * lebar

print(panjang, '*', lebar,'=',luas)
print('Type var panjang:',type(panjang))
print('Type var lebar:',type(lebar))
print('Type var luas:',type(luas))

print("================================")

#tipe tuple
panjang = 5
lebar = 10,5
luas = panjang * lebar

print(panjang, '*', lebar,'=',luas)
print('Type var panjang:',type(panjang))
print('Type var lebar:',type(lebar))
print('Type var luas:',type(luas))
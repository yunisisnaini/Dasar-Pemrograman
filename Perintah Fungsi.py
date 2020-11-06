def luaspersegi(s):
    luas=s*s
    print("Luas Persegi : %d" %luas)
def kelilingpersegi(s):
    keliling=s+s+s+s
    print("Keliling Persegi : %d" %keliling)
def luaspersegipanjang (p,l):
    luas=p*l
    print("Luas Persegi Panjang : %d" %luas)
def kelilingpersegipanjang(p,l):
    keliling=p+p+l+l
    print("Keliling Persegi Panjang : %d" %keliling)
def luassegitiga(a,t):
    luas=0.5*a*t
    return luas
def kelilingsegitiga(s):
    keliling=s+s+s
    return keliling
def kelilinglingkaran(r):
    keliling=3.14*2*r
    return keliling
def luaslingkaran(r):
    luas=3.14*r*r
    return luas
print("===========================")
print("Operasi Bangun Datar")
print("===========================")

print("===========================")
print("1. Luas dan Keliling Persegi")
print("2. Luas dan Keliling Persegi Panjang")
print("3. Luas dan Keliling Lingkaran")
print("4. Luas dan Keliling Segitiga")
print("5. Keluar")
print("==========================")
pilihan=int(input("Masukan pilihan Anda : "))
print()
print()
if pilihan ==1:
    print("Menghitung Luas dan Keliling Persegi")
    s=int(input("Masukan Nilai Sisi : "))
    luaspersegi(s)
    kelilingpersegi(s)
if pilihan ==2:
    print("Menghitung Luas dan Keliling Persegi Panjang")
    p=int(input("Masukan Nilai Panjang : "))
    l=int(input("Masukan Nilai Lebar : "))
    luaspersegipanjang(p,l)
    kelilingpersegipanjang(p,l)
if pilihan ==3:
    print("Menghitung Luas dan Keliling Lingkaran")
    r=int(input("Masukan Nilai Jari-Jari : "))
    print("Luas Lingkaran : %f" %luaslingkaran(r))
    print("Keliling Lingkaran : %f" %kelilinglingkaran(r))
if pilihan==4:
    print("Menghitung Luas dan Keliling Segitiga")
    a=int(input("Masukan Nilai Alas : "))
    t=int(input("Masukan Nilai Tinggi : "))
    s=int(input("Masukan Nilai Sisi Miring : "))
    print("Luas Segitiga : %f" %luassegitiga(a,t))
    print("Keliling Segitiga : %f" %kelilingsegitiga(s))
if pilihan==5:
    exec("exit()")
else:
    print("Masukan Pilihan Anda Salah")

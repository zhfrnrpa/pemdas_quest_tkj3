# Volume Bangun Ruang

print("\n1. Volume Balok")
p = int(input("Masukkan nilai panjang: "))
l = int(input("Masukkan nilai lebar: "))
t = int(input("Masukkan nilai tinggi: "))
volume_b = p * l * t
print("Volume Balok tersebut adalah", volume_b)

print("\n2. Volume Kubus")
s = int(input("Masukkan nilai sisi: "))
volume_k = s * s * s
print("Volume Kubus tersebut adalah", volume_k)

print("\n3. Volume Limas")
la = int(input("Masukkan nilai luas alas: "))
t = int(input("Masukkan nilai tinggi: "))
volume_l = 1/3 * (la * la) * t
print("Volume Limas tersebut adalah", volume_l)

print("\n4. Volume Tabung")
phi = 22/7
r = int(input("Masukkan nilai jari  jari: "))
t = int(input("Masukkan nilai tinggi: "))
volume_t = phi * r * r * t
print("Volume Tabung tersebut adalah", volume_t)

# Celcius to Reamur

print("\n1. Nilai celcius ke reamur")
celcius = int(input("Masukkan nilai celcius: " ))
nilai_r = 4/5 * celcius
print("Nilai Reamur nya adalah", nilai_r)



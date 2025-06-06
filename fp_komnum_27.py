from math import factorial

def stirling_interpolasi(f0, delta_f0, delta_f_1, delta2_f0, delta3_f0, delta3_f_1, delta4_f_1, x0, h, x, yt=None):
    # nilai s
    s = (x - x0) / h

    # rata-rata di delta f(x) dan delta-3 f(x) pada tabel
    delta1 = 0.5 * (delta_f0 + delta_f_1)
    delta3 = 0.5 * (delta3_f0 + delta3_f_1)

    # nilai f(x) ketika x = 14 dengan menggunakan Stirling
    fx = (f0 + s * delta1 + (s * (s - 1) / factorial(2)) * delta2_f0 + (s * (s - 1) * (s - 2) / factorial(3)) * delta3 + ((x / 4) * s * (s - 1) * (s - 2) / factorial(3)) * delta4_f_1)

    # nilai f(x) ketika x = 14 dengan menggunakan Stirling dengan pembulatan 2 angka di belakang koma
    fx = round(fx, 2)

    if yt is not None:
        Et = round(abs((yt - fx) / yt) * 100, 2)
        return fx, Et
    else:
        return fx

# data dari tabel
f0 = 634575
delta_f0 = 1039299
delta_f_1 = 449619
delta2_f0 = 589680
delta3_f0 = 292896
delta3_f_1 = 438696
delta4_f_1 = 145800

# nilai x0, xs, dan h
x0 = 15
h = 3
xs = 14

# nilai sebenarnya
xt = 436366

# vaiabel untuk return hasil
f14, Et = stirling_interpolasi(f0, delta_f0, delta_f_1, delta2_f0, delta3_f0, delta3_f_1, delta4_f_1, x0, h, xs, xt)

# output
print(f"Nilai f({xs}) dengan interpolasi Stirling: {f14}")
print(f"Nilai Et: {Et}%")

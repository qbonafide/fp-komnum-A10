|    NRP     |      Name      |
| :--------: | :------------: |
| 5025241021 | Kartika Nana Naulita |
| 5025241059 | Puspita Wijayanti .K. |
| 5025241060 | Christina Tan |
| 5025241069 | Erica Triana Widyastuti |
| 5025241086 | Callista Fidelya |

# FINAL PRAKTIKUM KOMPUTASI NUMERIK

### 27. Interpolasi Stirling

## *Soal*  
>Carilah nilai f(x) ketika x = 14 dengan menggunakan Stirling dengan Xo = 15 dan Y sebenarnya = 436366 [Cari juga nilai Et]

## Kode dan Penjelasan  
>def stirling_interpolasi(f0, delta_f0, delta_f_1, delta2_f0, delta3_f0, delta3_f_1, delta4_f_1, x0, h, x, yt=None):  

Merupakan fungsi utama yang akan digunakan dalam penyelesaian soal stirling ini. Fungsi ini menerima parameter nilai dari tabel selisih hingga dari tabel data (f0, delta_f0, delta_f_1, delta2_f0, delta3_f0, delta3_f_1, delta4_f_1), titik tengah x0, interval antar titik h, titik yang akan dihitung x, dan nilai sebenarnya yt.

>s = (x - x0) / h  

Nilai s merupakan parameter dari interpolasi stirling, dimana jarak titik yang akan dihitung x terhadap titik pusat x0 dibagi dengan selisih antar data h.

>`delta1 = 0.5 * (delta_f0 + delta_f_1)  
>    delta3 = 0.5 * (delta3_f0 + delta3_f_1)`  

Mencari rata-rata delta1 dan delta3 dari selisih nilai yang berada di atas dan di bawah titik pisat xo.

>fx = (f0 + s * delta1 + (s * (s - 1) / factorial(2)) * delta2_f0 + (s * (s - 1) * (s - 2) / factorial(3)) * delta3 + ((x / 4) * s * (s - 1) * (s - 2) / factorial(3)) * delta4_f_1)  

Menghitung nilai interpolasi stirling, di mana f0 merupakan nilai fungsi dari x0, berikutnya kalikan s, faktorial, dan nilai delta. 

>fx = round(fx, 2)  

Hasil dari perhitungan nilai fx dilakukan pembulatan 2 angka dibelakang koma.

>`if yt is not None:  
>        Et = round(abs((yt - fx) / yt) * 100, 2)  
>        return fx, Et  
>    else:  
>        return fx`  

Menghitung nilai Error True, jika diketahui nilai sebenarnya yt. Maka Error True diperoleh dari mutlak selisih nilai sebenarnya yt dan nilai fx dibagi dengan yt lalu dikalikan dengan 100%. Langkah terakhir yakni dengan membulatkan hasilnya dengan 2 angka di belakang koma.

  
### DATA DARI TABEL
| Notasi    | Nilai   |
|-----------|---------|
| f₀        | 634575  |
| Δf₀       | 1039299 |
| Δf₋₁      | 449619  |
| Δ²f₀      | 589680  |
| Δ³f₀      | 292896  |
| Δ³f₋₁     | 438696  |
| Δ⁴f₋₁     | 145800  |   

x0 = 15  
h = 3  
xs = 14  
xt = 436366  

>f14, Et = stirling_interpolasi(f0, delta_f0, delta_f_1, delta2_f0, delta3_f0, delta3_f_1, delta4_f_1, x0, h, xs, xt)  

Melakukan pemanggilan fungsi untuk menghitung nilai dari interpolasi stirling dan nilai Error True x = 14.  

>`print(f"Nilai f({xs}) dengan interpolasi Stirling: {f14}")  
>print(f"Nilai Et: {Et}%")`  

Menampilkan hasil dari interpolasi stirling dan juga nilai Error True.

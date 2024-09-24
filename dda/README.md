# Digital Differential Analyzer (DDA)

Digital Differential Analyzer adalah algoritma paling sederhana untuk menggambar garis.

## Algoritma
1. Tentukan 2 titik.
2. Tentukan salah satu sebagai titik awal $(x_1, y_1)$ dan satu lainnya sebagai titik akhir $(x_2, y_2)$.
3. Hitung selisih koordinat x ($dx$) dan koordinat y ($dy$)
4. Tentukan step. Jika $|dx| > |dy|$, maka $step = |dx|$. Jika tidak, maka $step = |dy|$
5. Hitung penambahan koordinat piksel.
```math
x_{\text{inc}} = dx / \text{step}
```
```math
y_{\text{inc}} = dy / \text{step}
```

7. Tentukan koordinat selanjutnya.
```math
x = x + x_{\text{inc}}
```
```math
y = y + y_{\text{inc}}
```
8. Lakukan pembulatan, dan tampilkan pada sistem koordinat.
```math
u = \text{round}(x)
```
``` math
v = \text{round}(y)
```
9. Ulangi langkah 6 dan 7 sampai $x = x_2$ dan $y = y_2$.
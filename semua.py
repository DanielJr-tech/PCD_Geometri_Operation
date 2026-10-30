import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Membaca gambar
img = cv2.imread("kucing.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
tinggi, lebar = img.shape[:2]
pusat = (lebar // 2, tinggi // 2)

# ==========================================
# 2. PROSES SEMUA TRANSFORMASI
# ==========================================

# A. Rotasi
M1 = cv2.getRotationMatrix2D(pusat, 45, 1.0)
M2 = cv2.getRotationMatrix2D(pusat, 90, 1.0)
M3 = cv2.getRotationMatrix2D(pusat, 180, 1.0)
rotasi_45 = cv2.warpAffine(img, M1, (lebar, tinggi))
rotasi_90 = cv2.warpAffine(img, M2, (lebar, tinggi))
rotasi_180 = cv2.warpAffine(img, M3, (lebar, tinggi))

# B. Scaling
scaling = cv2.resize(img, None, fx=0.5, fy=2, interpolation=cv2.INTER_LINEAR)

# C. Translasi
M_trans = np.float32([
    [1, 0, 150],
    [0, 1, 75]
])
translasi = cv2.warpAffine(img, M_trans, (lebar, tinggi))

# D. Flip
horizontal_flip = cv2.flip(img, 1)
vertical_flip = cv2.flip(img, 0)


# ==========================================
# 3. MENAMPILKAN SEMUA HASIL DALAM SATU FIGUR
# ==========================================

plt.figure(figsize=(16, 9))

# Daftar gambar dan judul untuk ditampilkan
list_gambar = [
    (img, "Citra Asli"),
    (rotasi_45, "Rotasi 45 Derajat"),
    (rotasi_90, "Rotasi 90 Derajat"),
    (rotasi_180, "Rotasi 180 Derajat"),
    (scaling, f"Scaling ({scaling.shape[1]}x{scaling.shape[0]})"),
    (translasi, "Translasi (150, 75)"),
    (horizontal_flip, "Horizontal Flip"),
    (vertical_flip, "Vertical Flip")
]

# Melakukan perulangan (looping) untuk membuat subplot 2 baris 4 kolom
for i, (gambar, judul) in enumerate(list_gambar, 1):
    plt.subplot(2, 4, i)
    plt.imshow(gambar)
    plt.title(judul, fontsize=10)
    plt.axis("off")

plt.tight_layout()
plt.show()
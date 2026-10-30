import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("kucing.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 1. Horizontal Flip (flipCode = 1)
horizontal_flip = cv2.flip(img, 1)

# 2. Vertical Flip (flipCode = 0)
vertical_flip = cv2.flip(img, 0)

# Menampilkan hasil dengan Matplotlib
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(horizontal_flip)
plt.title("Horizontal Flip")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(vertical_flip)
plt.title("Vertical Flip")
plt.axis("off")

plt.tight_layout()
plt.show()
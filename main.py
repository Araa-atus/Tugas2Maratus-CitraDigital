
import cv2
import os

# Lokasi gambar
input_path = "data/foto_asli.jpg"
output_folder = "output"

# Membuat folder output jika belum ada
os.makedirs(output_folder, exist_ok=True)

# Membaca gambar asli
gambar = cv2.imread(input_path)

if gambar is None:
    print("Foto tidak ditemukan! Periksa lokasi dan nama file.")
else:
    # Brightness Adjustment
    brightness = 40
    hasil = cv2.convertScaleAbs(gambar, alpha=1.0, beta=brightness)

    # Menyimpan hasil gambar
    output_path = os.path.join(
        output_folder, "hasil_brightness.jpg"
    )
    cv2.imwrite(output_path, hasil)

    # Menampilkan gambar sebelum dan sesudah
    cv2.imshow("Foto Asli", gambar)
    cv2.imshow("Hasil Brightness Adjustment", hasil)

    print("Brightness Adjustment berhasil!")
    print("Hasil tersimpan di:", output_path)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

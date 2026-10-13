from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Init tkinter (tanpa window utama)
root = tk.Tk()
root.withdraw()

# Pilih banyak gambar
files = filedialog.askopenfilenames(
    title="Pilih gambar",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
)

if not files:
    messagebox.showwarning("Batal", "Ga ada gambar yg dipilih")
    exit()

# Dialog simpan PDF
pdf_file = filedialog.asksaveasfilename(
    title="Simpan sebagai PDF",
    defaultextension=".pdf",
    filetypes=[("PDF Files", "*.pdf")]
)

if not pdf_file:
    messagebox.showwarning("Batal", "Penyimpanan PDF dibatalkan")
    exit()

# Load & convert gambar
images = []
for f in files:
    img = Image.open(f).convert("RGB")
    images.append(img)

# Simpan ke PDF (multi-page)
images[0].save(
    pdf_file,
    save_all=True,
    append_images=images[1:]
)

# Popup sukses
messagebox.showinfo(
    "Sukses",
    f"{len(images)} gambar berhasil digabung\n\nFile:\n{os.path.basename(pdf_file)}"
)
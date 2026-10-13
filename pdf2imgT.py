from pdf2image import convert_from_path
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime


today = datetime.now().strftime("%d-%m-%Y")

# Init tkinter
root = tk.Tk()
root.withdraw()

# Browse PDF
pdf_file = filedialog.askopenfilename(
    title="Pilih file PDF",
    filetypes=[("PDF Files", "*.pdf")]
)

if not pdf_file:
    messagebox.showwarning("Batal", "Ga ada file PDF yg dipilih")
    exit()

# Pilih folder output
output_dir = filedialog.askdirectory(
    title="Pilih folder output PNG"
)

if not output_dir:
    messagebox.showwarning("Batal", "Folder output ga dipilih")
    exit()

try:
    # Convert PDF ke PNG
    pages = convert_from_path(pdf_file, dpi=950)

    for i, page in enumerate(pages):
        output_path = os.path.join(
            output_dir,
            f"pdf2img{today}_{i+1}.png"
        )
        page.save(output_path, "PNG")

    # Popup sukses
    messagebox.showinfo(
        "Sukses",
        f"{len(pages)} halaman berhasil dikonversi ke PNG"
    )

except Exception as e:
    messagebox.showerror(
        "Error",
        f"Gagal convert PDF\n\n{str(e)}"
    )

import pandas as pd
import os

# Path utama
base_path = "/workspaces/verbose-space-bassoon/Jakarta Utara/Kelapa Gading"
excel_path = "/workspaces/verbose-space-bassoon/Jakarta Utara/Data Jakarta Utara.xlsx"


# Inisialisasi DataFrame kosong untuk menyimpan hasil gabungan CSV
df_list = []

# Loop melalui folder 1-12
for month in range(1, 13):
    csv_path = os.path.join(base_path, str(month), "daily_averages.csv")
    if os.path.exists(csv_path):  # Pastikan file ada sebelum membaca
        df = pd.read_csv(csv_path)

        # Ubah nama kolom agar seragam
        df.rename(columns={"Tanggal": "Date"}, inplace=True)

        # Konversi format tanggal CSV (sudah dalam YYYY-MM-DD, cukup gunakan pd.to_datetime)
        df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

        df["Month"] = month  # Tambahkan informasi bulan
        df_list.append(df)

# Gabungkan semua file CSV
if df_list:
    df_csv = pd.concat(df_list, ignore_index=True)
else:
    raise FileNotFoundError("Tidak ada file daily_averages.csv yang ditemukan di folder 1-12")

# Baca data dari file Excel
df_excel = pd.read_excel(excel_path)

# Ubah nama kolom tanggal agar seragam
df_excel.rename(columns={"TANGGAL": "Date"}, inplace=True)

# Konversi format tanggal Excel (dalam DD-MM-YYYY)
df_excel["Date"] = pd.to_datetime(df_excel["Date"], format="%d-%m-%Y")

# Gabungkan berdasarkan kolom tanggal
df_merged = pd.merge(df_csv, df_excel, on="Date", how="outer")

# Simpan hasil gabungan ke dalam file baru
output_path = os.path.join(base_path, "Merged_Data.xlsx")
df_merged.to_excel(output_path, index=False)

print(f"File hasil gabungan disimpan di: {output_path}")

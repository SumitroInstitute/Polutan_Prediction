import pandas as pd
import os

# Path file CSV
csv_file_1 = "/workspaces/Polutan_Prediction/Data_Final/Lubang_Buaya_nasa_power_data.csv"   # Misalnya berisi kolom 'Date'
csv_file_2 = "/workspaces/Polutan_Prediction/Data_Final/Lubang Buaya Daily Averages.csv"  # Misalnya berisi kolom 'Tanggal'

# Baca kedua file CSV
df1 = pd.read_csv(csv_file_1)
df2 = pd.read_csv(csv_file_2)

# Seragamkan nama kolom tanggal
df1.rename(columns={"date": "Date"}, inplace=True)
df2.rename(columns={"Tanggal": "Date"}, inplace=True)

# Konversi ke format datetime
df1["Date"] = pd.to_datetime(df1["Date"], errors="coerce")
df2["Date"] = pd.to_datetime(df2["Date"], errors="coerce")

# Gabungkan berdasarkan 'Date'
df_merged = pd.merge(df1, df2, on="Date", how="outer")

# Tambahkan kolom location
df_merged["location"] = "Jakarta Timur"

# Simpan ke file CSV
output_path = "/workspaces/Polutan_Prediction/Data_Final/Final/Jakarta_Timur.csv"
df_merged.to_csv(output_path, index=False)

print(f"File hasil gabungan disimpan di: {output_path}")

import os
import pandas as pd
import re  # Import regex library

# Hanya sampai folder "Kelapa Gading"
folder_path = "/workspaces/Polutan_Prediction/Data Mentah/Bundaran HI"

daily_averages = []

# Cari semua file .xlsx secara rekursif
for dirpath, _, filenames in os.walk(folder_path):
    for file in filenames:
        if file.endswith(".xlsx") and not file.startswith("~$"):  # Hindari file sementara Excel
            file_path = os.path.join(dirpath, file)

            try:
                print(f"\nMemproses file: {file}")

                # Baca file Excel
                df = pd.read_excel(file_path, engine="openpyxl")

                # Cek kolom yang tersedia
                print(f"Kolom tersedia di {file}: {df.columns.tolist()}")

                expected_cols = ["ISPU PM10", "ISPU PM2.5", "ISPU SO2", "ISPU CO", "ISPU O3", "ISPU NO2"]
                if not all(col in df.columns for col in expected_cols):
                    print(f"File {file} tidak memiliki semua kolom yang diharapkan, dilewati")
                    continue

                # Cek isi awal dataframe
                print(f"Data awal dalam {file}:\n", df.head())

                # Konversi ke numerik
                df[expected_cols] = df[expected_cols].apply(pd.to_numeric, errors='coerce')

                # Cek jumlah NaN
                print(f"Jumlah NaN setelah konversi di {file}:\n", df[expected_cols].isna().sum())

                # Hitung rata-rata
                avg_values = df[expected_cols].mean(skipna=True)

                if avg_values.isna().all():
                    print(f"Semua nilai ISPU di file {file} adalah NaN, dilewati")
                    continue

                # Ekstrak tanggal dari nama file dengan pola YYYY-MM-DD
                date_match = re.search(r'(\d{4}-\d{2}-\d{2})', file)
                if date_match:
                    date_str = date_match.group(0)
                    try:
                        date = pd.to_datetime(date_str, format="%Y-%m-%d", errors="raise")
                        print(f"Tanggal yang diparsing: {date}")
                    except Exception as e:
                        print(f"Error parsing tanggal dari file {file}: {e}")
                        date = pd.NaT
                else:
                    print(f"Tanggal tidak ditemukan dalam nama file: {file}, dilewati")
                    date = pd.NaT

                # Simpan hasil
                daily_averages.append([date] + avg_values.tolist())

            except Exception as e:
                print(f"Error membaca file {file}: {e}")

# Buat DataFrame hasil
df_daily = pd.DataFrame(daily_averages, columns=["Tanggal", "PM 10", "PM 2.5", "O2", "CO", "O3", "NO2"])
df_daily = df_daily.sort_values(by="Tanggal").reset_index(drop=True)

# Tampilkan hasil akhir
print("\nHasil Kelapa Gading Daily Averages:")
print(df_daily)

# Simpan hasil sebagai CSV
output_csv_path = os.path.join(folder_path, "/workspaces/Polutan_Prediction/Data_Final/Bundaran HI Daily Averages.csv")
df_daily.to_csv(output_csv_path, index=False)
print(f"\nData telah disimpan ke {output_csv_path}")

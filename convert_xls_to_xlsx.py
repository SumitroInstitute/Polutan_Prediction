import os
import subprocess

def convert_xls_to_xlsx(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(".xls"):
            file_path = os.path.join(folder_path, file)
            new_file_path = file_path.replace(".xls", ".xlsx")
            
            try:
                # Perintah LibreOffice untuk konversi dan menimpa file yang ada
                subprocess.run(["soffice", "--headless", "--convert-to", "xlsx", file_path, "--outdir", folder_path], check=True)
                print(f"Berhasil dikonversi dan menimpa: {file} -> {new_file_path}")
                
                # Menghapus file .xls setelah konversi
                os.remove(file_path)
                print(f"File .xls telah dihapus: {file}")
                
            except subprocess.CalledProcessError as e:
                print(f"Error mengonversi {file}: {e}")
            except Exception as e:
                print(f"Error saat menghapus file {file}: {e}")

# Ganti dengan path folder yang sesuai
folder_path = "/workspaces/verbose-space-bassoon/Jakarta Utara/Kelapa Gading/12"
convert_xls_to_xlsx(folder_path)

import os
import subprocess

def convert_all_xls_to_xlsx(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith(".xls"):
                file_path = os.path.join(dirpath, file)
                new_file_path = file_path.replace(".xls", ".xlsx")

                try:
                    # Jalankan LibreOffice untuk konversi
                    subprocess.run([
                        "soffice", "--headless", "--convert-to", "xlsx", file_path, "--outdir", dirpath
                    ], check=True)
                    print(f"Berhasil dikonversi dan menimpa: {file_path} -> {new_file_path}")

                    # Hapus file .xls setelah konversi
                    os.remove(file_path)
                    print(f"File .xls telah dihapus: {file_path}")

                except subprocess.CalledProcessError as e:
                    print(f"Error mengonversi {file_path}: {e}")
                except Exception as e:
                    print(f"Error saat menghapus file {file_path}: {e}")

# Ganti path berikut dengan path root ke folder yang memiliki subfolder .xls
root_folder_path = "/workspaces/Polutan_Prediction/Data Mentah/Bundaran HI"
convert_all_xls_to_xlsx(root_folder_path)

import os
from PyPDF2 import PdfFileReader
import pandas as pd

folder_path = '/home/xpms/Downloads/OneDrive_2_28-02-2023'
folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
files_info = []

print(folders)
for folder in folders:
    f_path = os.path.join(folder_path, folder)
    for file_name in os.listdir(f_path):
        files_info.append(file_name)
df = pd.DataFrame(files_info)
newdf = df.drop_duplicates()
newdf.to_csv("contracts_files72.csv", index=False)
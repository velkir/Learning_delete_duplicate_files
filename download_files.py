import gdown

url = "https://drive.google.com/drive/folders/1eqTkFXM9xqPr_D51XKdmzourOCeSRnjL"

gdown.download_folder(url, quiet=True, use_cookies=False)
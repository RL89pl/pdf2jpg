from pdf2image import convert_from_path
pages = convert_from_path('infografika.pdf', 500)
pages[0].save('infografika_.jpg', 'JPEG')
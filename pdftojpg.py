from pdf2image import convert_from_path
pages = convert_from_path('infografika.pdf', 500)
for page in pages:
    page.save('infografika_.jpg', 'JPEG')
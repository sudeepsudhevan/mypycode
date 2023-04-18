import pdfkit

config= pdfkit.configuration(wkhtmltopdf= r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

pdfkit.from_url('https://www.google.com','out.pdf',configuration=config)
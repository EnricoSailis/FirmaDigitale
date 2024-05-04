# Adding annotation to pdf file

from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText

# Fill the writer with the pages you want
#pdf_path = os.path.join(RESOURCE_ROOT, "crazyones.pdf")
reader = PdfReader('example1.pdf')
writer = PdfWriter()
n_pages = 0
for page in reader.pages:
    writer.add_page(page)
    n_pages += 1
writer.add_blank_page()

# Create the annotation and add it
annotation = FreeText(
    text="Hello World\nThis is the last page!",
    rect=(0, 0, 600, 850),
    font="Arial",
    bold=True,
    italic=True,
    font_size="20pt",
    font_color="00ff00",
    border_color="0000ff",
    background_color="cdcdcd",
)
writer.add_annotation(n_pages, annotation=annotation)

# Write the annotated file to disk
with open("annotated-pdf.pdf", "wb") as fp:
    writer.write(fp)
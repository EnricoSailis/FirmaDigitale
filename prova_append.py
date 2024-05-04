# esempio di append ad un file pdf

from pypdf import PdfWriter

merger = PdfWriter()

input1 = open("example1.pdf", "rb")
input2 = open("example2.pdf", "rb")
input3 = open("example3.pdf", "rb")

# Add the first page of input1 document to output
merger.append(fileobj=input1, pages=(0,1))

# Insert the second page of input2 into the output beginning after the second page
merger.merge(position=2, fileobj=input2, pages=(1, 2))

# Append entire input3 document to the end of the output document
merger.append(input3)

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)

# Close file descriptors
merger.close()
output.close()

import fitz  # PyMuPDF
import os

# this method overlays the contents of a .png file over each page of a given pdf document
def overlay_fullpage_png(input_pdf: str, output_pdf: str, image_path: str) -> None:
    
    doc = fitz.open(input_pdf)                          # create document object

    for page in doc:                                    # for each page in the pdf, 
        rect = page.rect                                # create rectangle object from the full page
        page.insert_image(rect, filename=image_path)    # stretch PNG over the full page and overlay

    doc.save(output_pdf)                                # save output file

# retrieve input filenames
files: list[str] = [f for f in os.listdir('input') if f.endswith('.pdf')]

# run image overlay method on each input file
for f in files:
    overlay_fullpage_png(
        input_pdf = os.path.join("input", f),
        output_pdf = os.path.join("output", "overlay-"+f),
        image_path = "icon.png"
    )
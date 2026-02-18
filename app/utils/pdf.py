from pdfrw import PdfReader, PdfWriter, PdfDict

def fill_pdf(data: dict, template_path: str, output_path: str):
    pdf = PdfReader(template_path)
    for page in pdf.pages:
        annotations = page.get('/Annots')
        if not annotations:
            continue

        for annotation in annotations:
            if annotation.Subtype == '/Widget' and annotation.T:
                key = annotation.T[1:-1]
                if key in data:
                    annotation.V = PdfDict(V=str(data[key]))
                    annotation.AP = None

    PdfWriter().write(output_path, pdf)
    return output_path
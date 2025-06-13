def generate_pdf_report(assay_data):
    html = render_to_string("core/report_template.html", {"assay": assay_data})
    pdf_file = HTML(string=html).write_pdf()
    return pdf_file
import reportlab
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch


def generate_report_from_dict(filename, title, description, contents_dict):
    
    report = SimpleDocTemplate(filename, pagesize=letter)
    flow_tables = []
    styles = getSampleStyleSheet()
 

    report_title = Paragraph(title, styles["h1"])
    flow_tables.append(report_title)

    description = description.replace("\n", "<br/>")
    report_description = Paragraph("<br/>" +description + "<br/>"*2, styles["Normal"])
    flow_tables.append(report_description)

    contents_list = []
    contens_list_header =  [ Paragraph("Item No.", styles["BodyText"]),
        Paragraph("Item Name", styles["BodyText"]),
        Paragraph("Item Price (PHP)", styles["BodyText"])
        
        ] 

    contents_list.append(contens_list_header)

    for item_id, item_contents in contents_dict.items():
        contents_list.append( [ Paragraph(str(item_id), styles["BodyText"]),
         Paragraph(str(item_contents["name"]), styles["BodyText"]),
         Paragraph(str(item_contents["price"]), styles["BodyText"]),
        
        ] )
                       

    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
    report_table = Table(data = contents_list, colWidths=(0.5*inch, 5*inch, 1*inch), style = table_style, hAlign = "LEFT")
    flow_tables.append(report_table)

    report.build(flow_tables)

def main():

    # Sample test only.

    sample_dict = {
        1:{"name": "Name 01", "price": "Value 01"},
        2:{"name": "Name 02", "price": "Value 02"},
        3:{"name": "Name 03", "price": "Value 03"},
    }
    generate_report_from_dict("sample.pdf", "My Title", "Sample description.", sample_dict)

if __name__ == "__main__":
    main()


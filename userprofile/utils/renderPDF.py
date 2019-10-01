from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
import base64
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    # result = open('abc.pdf', 'wb')
    # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    # result.close()
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    return base64.b64encode(result.getvalue()).decode()
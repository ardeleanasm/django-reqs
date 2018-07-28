from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

class Render:

    @staticmethod
    def render(content,file_name:str):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="'+file_name+'.pdf"'
        pisaStatus = pisa.CreatePDF(content, dest=response)
        if pisaStatus.err:
            return HttpResponse("Error Rendering PDF", status=400)
        return response
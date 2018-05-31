from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from apps.restaurant.models import Restaurante


# imports libreria códigos qr
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics import renderPDF
from io import BytesIO, StringIO
from zipfile import ZipFile, ZIP_DEFLATED

# Create your views here.


def order_list(request, *args, **kwargs):
    return render(request, 'manager/order_list.html')


class ManagerIndexView(DetailView):
    model = Restaurante
    template_name = 'index.html'
    context_object_name = 'restaurante'
    
    def get_context_data(self, **kwargs):
        # import pdb;pdb.set_trace()        
        # sesion
        self.request.session['mesa_id'] = self.kwargs.get('mesa_id')
        self.request.session['restaurante_slug'] = self.object.slug
        self.request.session['restaurante_nombre'] = self.object.nombre
        # context
        context = super(ManagerIndexView, self).get_context_data(**kwargs)
        context['mesa_id'] = self.request.session['mesa_id']
        context['restaurante_slug'] = self.request.session['restaurante_slug']
        context['restaurante_nombre'] = self.request.session['restaurante_nombre']
        return context


def manager_index(request, *args, **kwargs):
    return render(request, 'manager/manager_index.html')


def qr_cretate(request, *args, **kwargs):
    

    url = "192.168.0.2:8000"
    slug = "mil-sabores"
    # slug = kwargs.get('restaurant_slug')
    restaurante = Restaurante.objects.filter(slug=slug)
    tables = 10
    lista = []

    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="Códigos-QR.zip"'
    # Crear el fichero zip contenedor
    fzip = BytesIO()
    #crear archivo
    #archive = ZipFile('w', ZIP_DEFLATED)

    archive = ZipFile(fzip, 'w', ZIP_DEFLATED)

    for i in range(tables):

        # Crear el fichero pdf
        fpdf = BytesIO()

        # Crear el area de dibujo y vincularla al fichero pdf
        p = canvas.Canvas(fpdf)

        # Cargar la informacion del codigo qr
        qrw = QrCodeWidget('http://' + url + '/' +
                           slug + '/mesa-' + str(i + 1))
        qrw.barLevel = 'L'
        qrw.barWidth = 200
        qrw.barHeight = 200
        # Calcular el ancho y alto del codigo qr
        b = qrw.getBounds()
        w = b[2] - b[0]
        h = b[3] - b[1]

        # Ajustar el tamaño del canvas al tamaño del codigo
        p.setPageSize((w + 2, h + 2))

        #print(qrw)

        # Dibujar el codigo qr
        d = Drawing()
        d.add(qrw)
        renderPDF.draw(d, p, 1, 1)

        # Crear la pagina y guardar el contenido del pdf
        p.showPage()
        p.save()

        # Agregar el fichero pdf al contenedor zip
        archive.writestr('qrcode' + str(i + 1) + '.pdf', fpdf.getvalue())
        fpdf.close()

        # Agregar el nombre del fichero pdf a la lista
        #lista.append('qrcode'+str(i+1)+'.pdf')

    # Convertir la lista de ficheros en formato texto y escribirla en el fichero CSV
    #lista = "\n".join(lista)
    #fcsv.write(lista)

    #Agregar la lista (CSV) al contenedor zip
    #archive.writestr('lote.csv', fcsv.getvalue())
    #fcsv.close()

    # Cerrar el fichero zip
    archive.close()

    # Obtener el contenido del fichero zip
    fzip.flush()
    rzip = fzip.getvalue()
    fzip.close()
    response.write(rzip)
    

    # Cargar el contenido del fichero zip en la response
    #response.write(rzip)
    # Enviar la response con el fichero zip para ser descargada.
    return response

# qr_cretate('192.168.0.37:8000', 'mil-sabores', 5)

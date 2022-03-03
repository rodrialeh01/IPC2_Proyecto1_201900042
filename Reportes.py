import os
#METODO PARA GENERAR UN ARCHIVO TXT DE INSTRUCCIONES
def generarReportetxt(nombrep, ins):
    archivo = open('Instrucciones del piso ' + str(nombrep) + '.txt','w', encoding='utf-8')
    archivo.write(str(ins))
    archivo.close()
    os.startfile('Instrucciones del piso ' + str(nombrep) + '.txt')

#METODO PARA GENERAR UN ARCHIVO HTML DE INSTRUCCIONES
def generarReportehtml(nombrep, instrucciones):
    contenido = ''
    contenido += '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="shortcut icon" href="Icono.ico">
    <title>Instrucciones del Piso ''' + str(nombrep) +''' </title>
  </head>
  <body>
    <div class="p-3 mb-2 bg-primary text-white">
        <h1><center> CERAMICA-BOT </center></h1>
    </div>
    <div class="p-3 mb-2 text-white" style="background-color:#0789aa;">
        <h1><center>Instrucciones del Piso ''' + str(nombrep) +'''</center></h1>
    </div>
    <div class="p-3 mb-2 text-dark" style="background-color:#8f8f8f;">
        <h3>''' + str(instrucciones) +''' </h3>
    </div>
  </body>
</html>'''
    archivo = open('Instrucciones del piso ' + str(nombrep) + '.html','w', encoding='utf-8')
    archivo.write(contenido)
    archivo.close()
    os.startfile('Instrucciones del piso ' + str(nombrep) + '.html')

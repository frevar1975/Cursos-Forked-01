# -*- coding: utf-8 -*-
"""
Punto de entrada principal a la aplicación

Extiende el RequestHandler standard de webapp2, un micro framework para
desarrollo de aplicaciones con Python sobre App Engine.
Documentación: http://webapp-improved.appspot.com/

"""

import webapp2


class IdentityPage(webapp2.RequestHandler):
  """
  Handler principal de la aplicación

  Define los métodos que atenderán las solicitudes
  que se hagan a la raiz del sitio ("/")
  """
  TIPOS_DOCUMENTOS = {
    '1': "Cedula de Ciudadanía",
    '2': "Cedula de Extranjería",
    '3': "Tarjeta de Identidad"
  }

  def get(self):
    """
    Atiende solicitudes con el método GET
    """
    self.response.write("""
      <!DOCTYPE html>
      <html lang="es">
        <head>
          <meta charset='utf-8'>
          <title>Censo Local -- Identificación</title>
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
          <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
        </head>
        <body>
          <div class="container">
            <form method="POST" role="form" class="form-horizontal">
              <fieldset>
                <legend>Censo Nacional App Engine</legend>
                <div class="form-group">
                  <label for="doc_type" class="col-xs-2">Documento</label>
                  <div class="col-xs-4">
                    <select name="doc_type" class="form-control col-xs-3">
                      <option>-- Tipo --</option>
                      <option value="1">Cedula de Ciudadanía</option>
                      <option value="2">Cedula de Extranjeria</option>
                      <option value="3">Tarjeta de Identidad</option>
                    </select>
                  </div>
                  <div class="col-xs-4">
                    <input type="text" name="doc_number" placeholder="Número de documento"  class="form-control">
                  </div>
                </div>
                <div class="form-group">
                  <label for="doc_type" class="col-xs-2">Correo electrónico</label>
                  <div class="col-xs-8">
                    <input type="email" name="email" placeholder="Correo electrónico" class="form-control">
                  </div>
                </div>
                <div class="checkbox">
                  <label>
                    <input type="checkbox" name="true_info_check">
                    Confirmo que los datos aquí registrados son veraces correctos y actualizados.
                  </label>
                </div>
                <div class="form-group">
                  <div class="col-xs-12"><hr></div>
                  <div class="col-xs-1 col-xs-offset-9">
                    <input type="submit" value="Enviar" class="btn btn-primary pull-right">
                  </div>
                </div>
              </fieldset>
            </form>
          </div>
        </body>
      </html>
    """)

  def post(self):
    """
    Atiende solicitudes con el método POST
    """
    self.response.write('Hola Mundo: Solicitud POST %s' % self.request.POST)
    self.response.write("""
      <!DOCTYPE html>
      <html lang="es">
        <head>
          <meta charset='utf-8'>
          <title>Censo Local -- Identificación</title>
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
          <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
        </head>
        <body>
          <div class="container">
          </div>
        </body>
      </html>
    """)


class QuestionPage(webapp2.RequestHandler):

  def get(self, qid):
    """
    Handler de preguntas de la encuesta

    Args
      - qid: (int) recibe el número del paso de la encuesta (1 a 3)
    """
    forms_preguntas = dict()
    forms_preguntas['paso-1'] = """
            <form method="POST" role="form" class="form-horizontal">
              <fieldset>
                <legend>Censo Nacional App Engine - 1</legend>
                <div class="form-group">
                  <label for="doc_type" class="col-xs-2">Documento</label>
                  <div class="col-xs-4">
                    <select name="doc_type" class="form-control col-xs-3">
                      <option>-- Tipo --</option>
                      <option value="1">Cedula de Ciudadanía</option>
                      <option value="2">Cedula de Extranjeria</option>
                      <option value="3">Tarjeta de Identidad</option>
                    </select>
                  </div>
                  <div class="col-xs-4">
                    <input type="text" name="doc_number" placeholder="Número de documento"  class="form-control">
                  </div>
                </div>
                <div class="form-group">
                  <label for="doc_type" class="col-xs-2">Correo electrónico</label>
                  <div class="col-xs-8">
                    <input type="email" name="email" placeholder="Correo electrónico" class="form-control">
                  </div>
                </div>
                <div class="form-group">
                  <div class="col-xs-12"><hr></div>
                  <div class="col-xs-1 col-xs-offset-9">
                    <input type="submit" value="Enviar" class="btn btn-primary pull-right">
                  </div>
                </div>
              </fieldset>
            </form>"""

    forms_preguntas['paso-2'] = """
            <form method="POST" role="form" class="form-horizontal">
              <fieldset>
                <legend>Censo Nacional App Engine - 2</legend>
              </fieldset>
            </form>"""

    forms_preguntas['paso-3'] = """
            <form method="POST" role="form" class="form-horizontal">
              <fieldset>
                <legend>Censo Nacional App Engine - 3</legend>
              </fieldset>
            </form>"""

    paso = 'paso-%s' % qid
    if paso not in forms_preguntas:
      pass

    self.response.write("""
      <!DOCTYPE html>
      <html lang="es">
        <head>
          <meta charset='utf-8'>
          <title>Censo Local -- Preguntas</title>
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
          <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
        </head>
        <body>
          <div class="container">{form_data}
          </div>
        </body>
      </html>
    """.format(form_data=forms_preguntas[paso]))


class ResultPage(webapp2.RequestHandler):
  pass

app = webapp2.WSGIApplication([
    webapp2.Route(r'/identity', handler=IdentityPage, name='identity'),
    webapp2.Route(r'/questions/<qid:\d+>', handler=QuestionPage, name='questions'),
    webapp2.Route(r'/result', handler=ResultPage, name='results')
], debug=True)

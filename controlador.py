#!/usr/bin/python3
from modelousuario import ObtenerUsuario
import cgi

datos = cgi.FieldStorage()

print('Content-Type: text/html')
print('')

username=datos.getvalue('uname')
password=datos.getvalue('passw')

print(ObtenerUsuario(username,password))

#def render(archivo,modelo=False):
 # with open(archivo) as f:
  # pagina=f.read()
  #return pagina

#if username == None:
 # print("none")
#else:
 # p=render("loggin.html")
  #print(p)

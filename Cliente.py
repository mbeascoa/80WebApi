import requests
import json

#------------- Recogemos un empleado en concreto --------------------------------
api_url = "https://apiempleadosspgs.azurewebsites.net/api/Empleados/7499"
#capturamos la respuesta
response = requests.get(api_url)
#convertimos la respuesta a objeto diccionario
empleado = response.json()
print(empleado)
print(empleado["apellido"])

#------------- Recogemos todos los empleados --------------------------------
api_url = "https://apiempleadosspgs.azurewebsites.net/api/Empleados"
#capturamos la respuesta
response = requests.get(api_url)

print(response)
#<Response [200]>  imprime esto en caso positivo
#convertimos la respuesta a objeto diccionario
empleados = response.json()
print("Listado empleados")
print("-------------------")
for i in empleados:
    print( '\t' + i["apellido"])

#------------- Recogemos los datos en formato clave:valor ----------------------

import requests
from requests.exceptions import HTTPError
apiurl = "https://apiempleadosspgs.azurewebsites.net/api/Empleados/7839"
try:
	response = requests.get(apiurl)
	response.raise_for_status()
	# access JSOn content
	jsonResponse = response.json()
	for key, value in jsonResponse.items():
		print(key, ":", value)

except HTTPError as http_err:
	print(f'HTTP error occurred: {http_err}')
except Exception as err:
	print(f'Other error occurred: {err}')


#------------------------------

import requests
from requests.exceptions import HTTPError
apiurl = "https://apiempleadosspgs.azurewebsites.net/aooopi/Empleados/7839"
try:
	response = requests.get(apiurl)
	response.raise_for_status()
	# access JSOn content
	jsonResponse = response.json()
	print("Entire JSON response")
	print(jsonResponse)

except HTTPError as http_err:
	print(f'HTTP error occurred: {http_err}')
except Exception as err:
	print(f'Other error occurred: {err}')
import requests
apiurl = "https://apicruddepartamentoscore.azurewebsites.net"
request = "/api/departamentos"
departamento = {"numero": 40, "nombre": "PRODUCCION", "localidad": "SEVILLA"}

response = requests.post(apiurl + request, json=departamento)
#convertimos la respuesta a objeto diccionario
#print(response.json())
print("Status: " + str(response.status_code))


#EJEMPLO PUT (MODIFICAR)

import requests
apiurl = "https://apicruddepartamentoscore.azurewebsites.net"
request = "/api/departamentos"
departamento = {"numero": 20, "nombre": "INVESTIGACION", "localidad": "MADRID"}

response = requests.put(apiurl + request, json=departamento)
#convertimos la respuesta a objeto diccionario
#print(response.json())
print("Status: " + str(response.status_code))

#EJEMPLO DELETE (ELIMINAR)

import requests
apiurl = "https://apicruddepartamentoscore.azurewebsites.net"
request = "/api/departamentos/122234"
#departamento = {"numero": 10, "nombre": "CONTABILIDAD", "localidad": "ELCHE"}
response = requests.delete(apiurl + request)
#response = requests.put(apiurl + request, json=departamento)
#convertimos la respuesta a objeto diccionario
#print(response.json())
print("Status: " + str(response.status_code))
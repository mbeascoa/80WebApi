import requests
from requests.exceptions import HTTPError
apiurl = "https://apiempleadosspgs.azurewebsites.net/api/Empleados/7839"
#apiurl = "https://apiempleadosspgs.azurewebsites.net/api000000/Empleados/7839"
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

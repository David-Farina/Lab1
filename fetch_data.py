#imports the requests library
import requests

#Parameters

URL = "https://data.fixer.io/api/symbols"

API = "fbd212a848efe29f1d103c06a530cf0c"

#Making a variable that contains the data for the symbols
response = requests.get(
    URL,
    params = {"access_key": API},
    headers = {"Accept": "application/json"}
)

#Prints the response number and the symbol data
print(response)
print(response.json())

#Sends the data into a .txt file
file_path = rf"C:\Users\dfari\Desktop\Programming\TLDP\Lab1\API_symbols.txt"
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(str(response.json()))

print(f"file '{file_path}' created successfully.")
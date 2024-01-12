#!/usr/local/bin/python3
import os 

def parse_query_string(query):
    params = {}
    for pair in query.split("&"):
        if "=" in pair:
            key, value = pair.split("=", 1)
            params[key] = value
    return params

env_vars = ['REQUEST_URI', 'QUERY_STRING', 'REQUEST_METHOD', 'REMOTE_ADDR', 'REQUEST_SCHEME']
envs = "<ul>" + "".join([f"<li>{var} = {os.environ.get(var)}</li>" for var in env_vars]) + "</ul>"

query_string = os.environ.get("QUERY_STRING", "")
parsed_query = parse_query_string(query_string)

print('Content-Type: text/html\r')
print("Connection: close\r")
print('\r')
print(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
     <h1>Environment Variables</h1>
    {envs}
    <h2>Parsed Query String</h2>
    <pre>{parsed_query}</pre>
</body>
</html>
''')
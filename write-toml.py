import toml

# Writing to a TOML file
data = {
    'mysql': {
        'host': 'localhost:31016', 
        'username': 'root', 
        'password': 'password', 
        'database': 'students'
        }
    }

with open('result.toml', 'w') as file:
    toml.dump(data, file)
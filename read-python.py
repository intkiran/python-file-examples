import toml

# Reading the entire TOML file
with open('config.toml', 'r') as filestr:
    data = toml.load(filestr)
    print(data)
#
print(data['mysql']['host'])
print(data['mysql']['username'])
print(data['mysql']['password'])
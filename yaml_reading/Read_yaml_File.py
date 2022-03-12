import yaml

with open(r'D:\MyGitHub\Python_Projects\yaml_reading\sample.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

type(data)  #dict
for k, v in data.items():
    print(k, ':', v)

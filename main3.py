import yaml
import jinja2

with open("network.yaml", "r") as f:
    data = yaml.load(f, Loader = yaml.SafeLoader)

with open("template.j2", "r") as f:
    template = f.read()

template = jinja2.Template(template)

conf = template.render(data)
print(conf)


from netmiko import ConnectHandler

cisco = {
    'device_type': 'cisco_ios',
    'host':   '10.23.23.1',
    'username': 'admin',
    'password': 'admin',
    'secret': 'cisco',     
     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco)
output = net_connect.send_command('show run')
print(output)
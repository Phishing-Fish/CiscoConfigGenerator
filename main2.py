import yaml
import jinja2

with open("network.yaml", "r") as f:
    data = yaml.load(f, Loader = yaml.SafeLoader)

with open("template.j2", "r") as f:
    template = f.read()

template = jinja2.Template(template)

conf = template.render(data)
print(conf)


# import telnetlib
# HOST = '10.23.23.1'
# UNAME = 'admin'
# PASSWD = 'admin'
# ENABLE_PWD = 'cisco'

# tn = telnetlib.Telnet(HOST)
# tn.read_until(b'Username: ')
# tn.write(UNAME.encode('ascii') + b'\n')
# tn.read_until(b'Password: ')
# tn.write(PASSWD.encode('ascii') + b'\n')
# tn.read_until('R1>')
# tn.write(b'enable\n')
# tn.write(ENABLE_PWD.encode('ascii') + b'\n')
# tn.write(b'show run\n')
# print(tn.read_all().decode('ascii'))
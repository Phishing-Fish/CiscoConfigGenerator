import csv

routers = {}

def config_ip(row):
    if not row[0] in routers:
        routers[row[0]] = ''
    
    addr = row[2].split('/')
    match addr[1]:
        case '24':
            addr[1] = '255.255.255.0'
        case '27':
            addr[1] = '255.255.255.224' # 11100000  = 224
        case '30':
            addr[1] = '255.255.255.252'
    routers[row[0]] += f'''
!
interface {row[1]}
  ip addr {addr[0]} {addr[1]}
  no shutdown
!
'''


with open('network.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    first_line = True
    for row in spamreader:
        if first_line:
            first_line = False
            continue
        config_ip(row)

    for i in routers:
        print(f'Configuration for {i}')
        print(routers[i])
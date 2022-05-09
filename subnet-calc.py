from numpy import binary_repr


# Представление ip-адресса в бинарном виде
def ip_binary_repr(ip_address: str) -> str:
    return '.'.join([binary_repr(int(i), width=8) for i in ip_address.split('.')])


t = '192.168.1.1'
print(t, "-->", ip_binary_repr(t))

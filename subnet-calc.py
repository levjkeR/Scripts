# Представление ip-адресса в бинарном виде
def ip_binary_repr(ip_address: str) -> str:
    return '0b' + ''.join([bin(int(x) + 256)[3:] for x in ip_address.split('.')])


# Переход от безклассовой адрессаци
def cidr_to_netmask(cidr: int) -> tuple[str, str]:
    mask = bin((0xffffffff >> (32 - cidr)) << (32 - cidr))[2:]
    return '.'.join([str(mask[i:i + 8]) for i in range(0, 32, 8)]), \
           '.'.join([str(int(mask[i:i + 8], 2)) for i in range(0, 32, 8)])


# Переход к безклассовой адрессаци
def netmask_to_cidr(mask: str) -> int:
    return sum([bin(int(octet)).count('1') for octet in mask.split('.')])


def get_subnet_info(ip_address: str, cidr: int = 24):
    mask = cidr_to_netmask(cidr)
    network = list(zip(ip_address.split('.'), mask[1].split('.')))
    network_address = '.'.join([str(int(ip_octet) & int(mask_octet)) for ip_octet, mask_octet in network])
    broadcast_address = '.'.join([str((int(ip_octet) | ~int(mask_octet)) & 0xff) for ip_octet, mask_octet in network])
    print(f"IP Address: {ip_address}\n"
          f"Network Address: {network_address}\n"
          f"Broadcast Address: {broadcast_address}\n"
          f"Subnet Mask: {mask[0]}\n"
          f"Binary Mask: {mask[1]}\n"
          f"Hosts: {2**(32-cidr)}\n")


get_subnet_info('10.10.10.10', 30)

#!/usr/bin/env python3

import ipaddress
import math
import pyfiglet

# couleurs
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"  

def calculate_network_and_subnet(num_hosts):
    """
        Calcule l'adresse réseau et le masque en fonction du nombre de machines
    """
    # bit pour les hôtes
    bits_needed = math.ceil(math.log2(num_hosts + 2))  # +2 pour réseau et broadcast
    
    subnet_mask_bits = 32 - bits_needed
    subnet_mask = str(ipaddress.IPv4Network(f'0.0.0.0/{subnet_mask_bits}').netmask)

    # Déterminer la classe 
    if num_hosts <= 254:  # Classe C
        network_address = ipaddress.IPv4Network('192.168.0.0/24', strict=False)
    elif num_hosts <= 65534:  # Classe B
        network_address = ipaddress.IPv4Network('172.16.0.0/16', strict=False)
    elif num_hosts <= 16777214:  # Classe A
        network_address = ipaddress.IPv4Network('10.0.0.0/8', strict=False)
    else:
        return None  # Trop d'hôtes pour les plages A, B, C

    # Créer le réseau avec le masque calculé
    network = ipaddress.IPv4Network(f'{network_address.network_address}/{subnet_mask_bits}', strict=False)

    # Info 
    network_address = f"{network.network_address}/{subnet_mask_bits}"  # Format adresse réseau/masque
    first_ip = list(network.hosts())[0]
    last_ip = list(network.hosts())[-1]
    broadcast_address = network.broadcast_address
    gateway = last_ip  # dernière IP pour le routeur
    next_network = network.network_address + network.num_addresses

    return network_address, first_ip, last_ip, broadcast_address, gateway, subnet_mask, next_network

def main():
    """
        app
    """
    
    ascii_banner = pyfiglet.figlet_format("Network Setup")
    print(ascii_banner)
    print("@Sekhmet.23z")

    while True:
        action = input(f"{GREEN}Appuyez sur 'Entrée' pour continuer ou 'e' pour quitter : {RESET}")
        if action.lower() == 'e':
            print(f"{RED}kill{RESET}")
            break  # quit

        try:
            num_hosts = int(input(f"{GREEN}Entrez le nombre de postes dans le réseau : {RESET}"))

            result = calculate_network_and_subnet(num_hosts)

            if result:
                network_address, first_ip, last_ip, broadcast_address, gateway, subnet_mask, next_network = result

                # Afficher les résultats
                print(f"{RED}Adresse de réseau (avec masque) : {YELLOW}{network_address}{RESET}")
                print(f"{RED}Première adresse IP utilisable : {YELLOW}{first_ip}{RESET}")
                print(f"{RED}Dernière adresse IP utilisable : {YELLOW}{last_ip}{RESET}")
                print(f"{RED}Adresse de broadcast : {YELLOW}{broadcast_address}{RESET}")
                print(f"{RED}Gateway : {YELLOW}{gateway}{RESET}")
                print(f"{RED}Masque de sous-réseau : {YELLOW}{subnet_mask}{RESET}")
                print(f"{RED}Adresse du prochain réseau : {YELLOW}{next_network}{RESET}")
            else:
                print(f"{RED}Le nombre d'hôtes dépasse la capacité maximale des plages d'adresses A, B, C.{RESET}")

        except ValueError:
            print(f"{RED}Veuillez entrer un nombre valide pour le nombre de postes.{RESET}")

if __name__ == "__main__":
    main()

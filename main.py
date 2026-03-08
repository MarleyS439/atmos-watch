# Script de captura de dados
import platform, sys, colorama

from colorama import Fore, Back, Style, init

# Inicializa o colorama
init()

# Atmos ASCII Arte
print(Fore.BLUE + """
   ███    ████████ ██     ██  ███████   ██████  
  ██ ██      ██    ███   ███ ██     ██ ██    ██ 
 ██   ██     ██    ████ ████ ██     ██ ██       
██     ██    ██    ██ ███ ██ ██     ██  ██████  
█████████    ██    ██     ██ ██     ██       ██ 
██     ██    ██    ██     ██ ██     ██ ██    ██ 
██     ██    ██    ██     ██  ███████   ██████  
""" + Style.RESET_ALL)

# Obtém as informações do sistema
sistema_operacional = platform.uname()

print(Fore.BLUE + "Sistema operacional: " + Style.RESET_ALL + sistema_operacional.system)
print(Fore.BLUE + "Host: " + Style.RESET_ALL + sistema_operacional.node)
print(Fore.BLUE + "Kernel: " + Style.RESET_ALL + sistema_operacional.release)
print(Fore.BLUE + "Versão: " + Style.RESET_ALL + sistema_operacional.version)
print(Fore.BLUE + "Máquina: " + Style.RESET_ALL + sistema_operacional.machine)

# Vetor de argumentos de linha de comando (Ex.: python3 script.py -r - Todos os items após o 'script.py' são argumentos)
argumentos = sys.argv

# Verifica se o argumento de frequência de leitura foi passado
if len(argumentos) > 2:
    frequencia = float(argumentos[2])
elif len(argumentos) < 2:
    # Encerra o programa mostrando o uso correto
    print(Fore.RED + "\nInforme um argumento!" + Style.RESET_ALL)
    print("Uso: " + Fore.YELLOW + "python3 captura.py [comando] [frequência]" +Style.RESET_ALL)
    sys.exit(1)




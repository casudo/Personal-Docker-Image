# Import ASCII art
from art import *

# Grabbed from Stackoverflow (https://stackoverflow.com/a/17303428)
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Print he business card
tprint("Casudo")

print(color.BOLD + "Hello, my name is " + color.GREEN + "Kida! :)\n" + color.END)
print("This is my virtual business card.\n")

print(color.BOLD + color.YELLOW + "E-Mail:" + color.END + " contact@k1da.de")
print(color.BOLD + color.PURPLE + "GitHub:" + color.END + " https://github.com/casudo")
print(color.BOLD + color.GREEN + "Website:" + color.END + " https://k1da.de")
print(color.BOLD + color.CYAN + "Wiki:" + color.END + " https://wiki.k1da.de")
print(color.BOLD + color.RED + "Uptime:" + color.END + " https://uptime.k1da.de")
print(color.BOLD + color.BLUE + "LinkedIn:" + color.END + " Please ask me directly\n")

print(color.UNDERLINE + color.DARKCYAN + "2048-Bit RSA public key:" + color.END)
print("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoIAKZnv/YDclt0B0Sk1YO6QD430J5e6TzGIo3hUYN9/abPdb9Sdm4phiHScIQq7X5jN2PkN6pM25OwKmqrUJ7vBUScZlZahkP+gbWpk836Te8CX1/jAYqtEBWQsbUSUvFVwX8xOJOk8NwBE7OhQ0GudNi/wNbtkLEaAYYhsad+nbEasrlKE27ub6MMFW2U6QJ/aG1w+edT0ofizClOF2Vm2skKBU+jmz+xAVexntjL5jbgfO5moZrp7lLiyVn5Gz2fbyu/36Y6TXm36/0ZJ0epMzG1mDjSOPQSd/rv8vx7mse5BZli0+M8SbruiSJTtRSqAjEWo7j6E1BVIslxjpkwIDAQAB")

print("\n© k1da 2023")
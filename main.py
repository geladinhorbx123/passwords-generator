import random
import string
comprimento = int(input("digite o comprimento da senha: "))
characteres = string.ascii_letters + string.digits + string.punctuation
senha = ""
for i in range(comprimento):
    senha += random.choice(characteres)
print(senha)

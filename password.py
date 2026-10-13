import random
import string

def senha(tamanho):
    characteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""
    for i in range(tamanho):
        senha += random.choice(characteres)
    return senha
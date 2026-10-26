import hashlib
import itertools
import string

print("=== PROJETO ALURA - CRIPTOGRAFIA E HASH ===\n")

# 1 - Gerando Hash
def gerar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

senha = "alura123"
hash_gerado = gerar_hash(senha)
print(f"Senha: {senha}")
print(f"Hash SHA-256: {hash_gerado}\n")

# 2 - Ataque de força bruta (sua última aula)
def forca_bruta(hash_alvo):
    caracteres = string.ascii_lowercase + string.digits
    for tamanho in range(1, 5):
        for tentativa in itertools.product(caracteres, repeat=tamanho):
            palavra = ''.join(tentativa)
            if gerar_hash(palavra) == hash_alvo:
                return palavra
    return None

print(f"Tentando quebrar o hash de 'a1b'...")
resultado = forca_bruta(gerar_hash("a1b"))
print(f"Senha encontrada: {resultado}")

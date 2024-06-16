import random

def encrypt(strings):
    # Gera um valor aleatório n entre 1 e 10 para a chave de criptografia
    n = random.randint(1, 10)
    
    # Função para criptografar uma única string
    def encrypt_string(s, n):
        encrypted_chars = []
        for char in s:
            char_code = ord(char)
            new_char_code = char_code + n
            if new_char_code > 126:
                new_char_code = 33 + (new_char_code - 127)
            encrypted_chars.append(chr(new_char_code))
        return ''.join(encrypted_chars)
    
    # Criptografa cada string na lista usando a função encrypt_string
    encrypted_strings = [encrypt_string(s, n) for s in strings]
    
    return encrypted_strings, n

# Exemplo de uso
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print("Nomes criptografados:", nomes_criptografados)
print("Chave de criptografia:", chave)

# Para simular o exemplo com chave 5, substituímos a geração aleatória por um valor fixo
def encrypt_with_fixed_key(strings, n):
    def encrypt_string(s, n):
        encrypted_chars = []
        for char in s:
            char_code = ord(char)
            new_char_code = char_code + n
            if new_char_code > 126:
                new_char_code = 33 + (new_char_code - 127)
            encrypted_chars.append(chr(new_char_code))
        return ''.join(encrypted_chars)
    
    encrypted_strings = [encrypt_string(s, n) for s in strings]
    return encrypted_strings, n

# Testando com chave 5
chave_aleatoria = 5
nomes_cript = encrypt_with_fixed_key(nomes, chave_aleatoria)
print("Nomes criptografados com chave 5:", nomes_cript[0])
print("Chave de criptografia fixa:", chave_aleatoria)


def decoder(seq_bytes):
    temperatura = seq_bytes[0]
    umidade = seq_bytes[1]
    return temperatura, umidade

mensagem = b'\x18\x50'  # Mensagem enviada pela aplicação
t,u = decoder(mensagem)       # Simula o decoder presente na TTN

vetor = [('temperatura', t), ('umidade', u)]
dicionario = dict(vetor)
print(dicionario)
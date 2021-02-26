
def decoder(seq_bytes):
    identificador = seq_bytes[0] + seq_bytes[1]
    temperatura = seq_bytes[2]
    umidade = seq_bytes[3]
    return identificador, temperatura, umidade

mensagem = b'\x01\xFF\x18\x50'  # Mensagem enviada pela aplicação
i,t,u = decoder(mensagem)       # Simula o decoder presente na TTN

vetor = [('identificador', i), ('temperatura', t), ('umidade', u)]
dicionario = dict(vetor)
print(dicionario)
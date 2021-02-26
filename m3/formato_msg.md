# Formato das mensagens

## Enquadramento dos dados

O formato das mensagens será uma sequência de byte que representam três campos: `identificador`, `temperatura` e `umidade`. O tamanho de todo pacote **DEVE** ser 4 bytes. A tabela abaixo define os tamanhos de cada campo do pacote:

|Nome do campo| Tamanho |Descrição|
|-|-|-|
|identificador|2 bytes|identificador do endpoint|
|temperatura|1 byte|valor medido da temperatura|
|umidade|1 byte|valor medido da umidade|

---

## Exemplo:

Para o pacote em hexadecimal a seguir:

- `01 FF 18 50`

Temos:

- Identificador: `01 FF`
- Temperatura: `18`
- Umidade: `50`

O que convertido para decimal é:

- Identificador: `256`
- Temperatura: `24`
- Umidade: `80`

----

## Aplicação na TTN: payload

Em `Payload Formats` é possível inserir um código (em javaScript) capaz de transformar os valores recebidos para que os mesmos se tornem de fácil identificação.

- [Exemplo: ttn-lorawan-application](https://github.com/mftutui/ttn-lorawan-application#aplica%C3%A7%C3%A3o-payload)

- Decoder:

```js
function Decoder(bytes, port) {
  var id = bytes[0] + bytes[1];
  var tmp = bytes[2]
  var umi = bytes[3]

  return {
    identificador: id,
    temperatura: tmp,
    umidade: umi
  };
}
```

- Payload:

```json
{
    "identificador" : 0,
    "temperatura" : 0,
    "umidade" : 0
}
```

Aqui há uma versão funcional do decoder em python:
- [Decoder em python](m3/teste_decoder.py)
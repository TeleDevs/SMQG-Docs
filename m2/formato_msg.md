# Formato das mensagens

## Enquadramento dos dados

O formato das mensagens será uma sequência de byte que representam três campos: `temperatura` e `umidade`. O tamanho de todo *payload* **DEVE** ser 2 bytes. A tabela abaixo define os tamanhos de cada campo do pacote:

|Nome do campo| Tamanho |Descrição|
|-|-|-|
|temperatura|1 byte|valor medido da temperatura|
|umidade|1 byte|valor medido da umidade|

---

## Exemplo:

Para o pacote em hexadecimal a seguir:

- `18 50`

Temos:

- Temperatura: `18`
- Umidade: `50`

O que convertido para decimal é:

- Temperatura: `24`
- Umidade: `80`

----

## Aplicação na TTN: payload

Em `Payload Formats` é possível inserir um código (em javaScript) capaz de transformar os valores recebidos para que os mesmos se tornem de fácil identificação.

- [Exemplo: ttn-lorawan-application](https://github.com/mftutui/ttn-lorawan-application#aplica%C3%A7%C3%A3o-payload)

- Decoder:

```js
function Decoder(bytes, port) {
  var tmp = bytes[0];
  var umi = bytes[1];

  return {
    temperatura: tmp,
    umidade: umi
  };
}
```

- Payload:

```json
{
    "temperatura" : 0,
    "umidade" : 0
}
```

Aqui há uma versão funcional do decoder em python:
- [Decoder em python](teste_decoder.py)
# Formato das mensagens

## Comunicação Estação - Gateway

O formato das mensagens será em JSON:

- O dispositivo Android SEMPRE irá enviar uma mensagem com pelo menos o campo o `cod`. Veja os possíveis valores deste campo logo abaixo:

---

|Valor|Descrição|
|:-:|-|
|0|Realiza o sincronismo do relógio do Arduino.
|1|Solicita a coleta dos dados do sensor naquele instante. |
|2|Solicita a coleta dos dados do sensor que estão armazenados no Arduino. |

---

- A estação (Arduino) possui uma resposta diferente de acordo com o comando recebido. Essas mensagens podem ser vistas a seguir:

- **Sincronizar relógio**

    - Mensagem pedido (`Android -> Arduino`):

        ```json
        {
            "cod":0,
            "time":1618885785
        }
        ```
        > Não há mensagem de resposta.

- **Realizar coleta atual**

    - Mensagem pedido (`Android -> Arduino`):

        ```json
        {
            "cod":1
        }
        ```

    - Mensagem resposta (`Arduino -> Android`):

        ```json
        {
            "tmp":29,
            "umi":80, 
            "dia":"2021-03-14 13:07:08.104114"
        }
        ```

- **Realizar coleta dos valores armazenados**

    - Mensagem pedido (`Android -> Arduino`):

        ```json
        {
            "cod":2
        }
        ```

    - Mensagem resposta (`Arduino -> Android`):

        ```json
        {
            "tmp":29,
            "umi":80,
            "dia":"2021-03-14 13:07:08.104114"
        }
        ```

## Comunicação Gateway - Broker MQTT

O formato das mensagens será em JSON. Ao realizar o método `PUBLISH`, o Gateway irá enviar uma mensagem com o seguinte formato:

```json
{
    "idLocal":"SJ-001",
    "idSensor":"00:20:10:07:33:A4",
    "temperature":29.30,
    "humidity":80,
    "datetime":"2021-03-14 13:07:08.104114"
}
```
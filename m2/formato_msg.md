# Formato das mensagens

O formato das mensagens será em JSON:

- O dispositivo Android SEMPRE irá enviar uma mensagem com um único campo o `cod`. Veja os possíveis valores deste campo logo abaixo:

|Valor|Descrição|
|:-:|-|
|1|Solicita a coleta dos dados do sensor naquele instante. |
|2|Solicita a coleta dos dados do sensor que estão armazenados no Arduino. |

- A estação (Arduino) possui uma resposta diferente de acordo com o comando recebido. Essas mensagens podem ser vistas a seguir:

    - Realizar coleta atual

        - Mensagem pedido (`Android -> Arduino`):

            ```json
            {
                "cod":1
            }
            ```

        - Mensagem resposta (`Arduino -> Android`):

            ```json
            {
                "id":123,
                "tmp":29,
                "umi":80
            }
            ```

    - Realizar coleta dos valores armazenados

        - Mensagem pedido (`Android -> Arduino`):

            ```json
            {
                "cod":2
            }
            ```

        - Mensagem resposta (`Arduino -> Android`):

            ```json
            {
                "id":123,
                "dia":12042020,
                "tmp":29,
                "umi":80
            }
            ```
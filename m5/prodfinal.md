# Produto final

##  Hardware 

## Software

A interface do aplicativo Android desenvolvido nesse projeto, teve o intuito de abordar uma área mais técnica. Exibindo dados da comunicação Bluetooth e com o Broker MQTT. Esse tipo de interface, pode não ser tão intuitiva para um usuário final.

Hoje, para coletar e publicar as coletas o usuário deve seguir o seguinte procedimento:

1. Abrir o aplicativo;
2. Selecionar a saca de grãos;
3. Inserir o broker MQTT;
4. Digitar local da coleta;
5. Pressionar o botão `Coletar Armazenado` (comunicação entre Arduino e Android);
6. Pressionar o botão `Publish` (envio dos dados para o broker MQTT);

O fluxo proposto, resume-se a:

1. Abrir o aplicativo;
2. Selecionar a saca de grãos;
3. Fazer um *login* com usuário e senha;
    - Baseado neste *login*, os dados do Broker MQTT serão carregados;
4. Digitar local da coleta;
5. Pressionar o botão `Coletar Armazenado`
    - Ao pressionar esse botão, todo o processo de coletar os dados da estação e publicar no broker MQTT ocorrerão sem nenhuma outra interferência do usuário.

Abaixo há uma proposta de uma nova tela de usuário. Sem as abas de histórico e publish MQTT e tampouco a exibição dos JSONs trocados durante a comunicação Bluetooth:

<img src="img/softprop.png" alt="drawing" width="300"/>

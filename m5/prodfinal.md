# Produto final

##  Hardware 

A estação projetada neste trabalho utilizou componentes e placas de desenvolvimento mais didáticas para a criar a solução. A utilização do arduino nano traz algumas limitações, principalmente de capacidade de armazenamento para os dados coletados pelo sensor.
Uma solucação para esse problema é utilizar chips extras na placa, como por exemplo o módulo de memória EEPROM At24c256, com uma capacidade de 32kbytes permitindo o armazenamento de muito mais dados coletados.

O preço do módulo de memória EEPROM At24c256 tem o custo de aproximadamente R$15,00, inseridos no orçamento da estação.



## Software

A interface do aplicativo Android desenvolvido nesse projeto, teve o intuito de abordar uma área mais técnica. Exibindo dados da comunicação Bluetooth e com o Broker MQTT. Esse tipo de interface, pode não ser tão intuitiva para um usuário final.

Nesse cenário, para coletar e publicar as coletas o usuário deve seguir o seguinte procedimento:

1. Abrir o aplicativo;
2. Selecionar a saca de grãos;
3. Inserir o broker MQTT;
4. Digitar local da coleta;
5. Pressionar o botão `Coletar Armazenado` (comunicação entre Arduino e Android);
6. Pressionar o botão `Publish` (envio dos dados para o broker MQTT);

O fluxo proposto a seguir, busca deixar a interface mais simples e intuitiva. Resumindo-se a:

1. Abrir o aplicativo;
2. Selecionar a saca de grãos;
3. Fazer um *login* com usuário e senha;
    - Baseado neste *login*, os dados do Broker MQTT serão carregados;
4. Digitar local da coleta;
5. Pressionar o botão `Coletar Armazenado`
    - Ao pressionar esse botão, todo o processo de coletar os dados da estação e publicar no broker MQTT ocorrerão sem nenhuma outra interferência do usuário.

Abaixo há uma proposta de uma nova tela de usuário. Sem as abas de histórico e publish MQTT e tampouco a exibição dos JSONs trocados durante a comunicação Bluetooth:

<img src="img/softprop.png" alt="drawing" width="300"/>

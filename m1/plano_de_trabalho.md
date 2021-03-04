# Plano de Trabalho

## Sumário

1. [Identificação da proposta](#identificação-da-proposta)
2. [Descrição da proposta](#descrição-da-proposta)
   1. [Justificativa](#justificativa)
   2. [Objetivo Geral](#objetivo-geral)
   3. [Objetivos específicos](#objetivos-específicos)
3. [Metas](#metas)
   1. [Identificação das Metas/Macro entregas](#identificação-das-metasmacro-entregas)
   2. [Identificação das Etapas](#identificação-das-etapas)
   3. [Cronograma de execução](#cronograma-de-execução)
4. [Materiais e insumos previstos](#materiais-e-insumos-previstos)

## Identificação da proposta

- **Título:** Sistema de monitoramento para qualidade de grãos.

- **Prazo:** 30/11/2020 até 15/04/2021

- **Equipe:** Elisa Rodrigues, Guilherme Lopes Roque, Yan Lucas Martins

- **Resumo da proposta:** Esta proposta visa monitorar o armazenamento de sacas de grãos a fim de garantir a qualidade do produto impedindo o excesso ou a escassez de temperatura e umidade, as quais contribuem para a criação de fungos e germinação da planta.

- **Data de início do projeto:** 10/12/2020

## Descrição da proposta

### **Justificativa**
  
O armazenamento correto de grãos influencia diretamente na porcentagem de germinação e no vigor de uma semente, bem como evita a proliferação de fungos e outras pragas que causam danos ao produto. Estima-se que pelo menos 15% das perdas de grãos armazenados são causadas diretamente por insetos e fungos.

No Brasil, o armazenamento em sacaria, chamado de convencional, é amplamente utilizado devido ao baixo custo inicial de instalação. No entanto, essas unidades armazenadoras possuem pouca ou nenhuma condição de medição das condições do ambiente. Com um sistema econômico que ofereça dados de temperatura e umidade, o produtor poderá tomar providências para garantir que o seu produto mantenha a qualidade aumentando a quantidade de grãos aptos para comércio e plantio.

### **Objetivo Geral**

Desenvolver sistema distribuído de baixo custo para monitoramento de medidas do ambiente, como temperatura e umidade, através da coleta, persistência e exibição dos dados.

### **Objetivos específicos**

- Desenvolvimento de uma estação de monitoramento protótipo para prova de conceito;
- Desenvolvimento de um sistema servidor para comunicação com as estações de monitoramento, persistência e tratamento dos dados;
- Desenvolvimento de uma interface gráfica para exibição dos dados coletados;
- Pesquisa e projeto do produto final da estação de monitoramento com custo otimizado;

## Metas

### Identificação das Metas/Macro entregas 

| Metas | Nº  | Responsável pela etapa | Descrição das atividades                                          |
|-------|-----|------------------------|-------------------------------------------------------------------|
| M1    | E1  | Elisa Rodrigues        | Definição do plano de trabalho                                    |
|       | E2  | Guilherme Roque        | Definição do hardware para protótipo                              |
|       | E3  | Yan Martins            | Definição do hardware para sistema servidor (aplicação e gateway) |
|       | E4  | Elisa Rodrigues        | Definição do software para protótipo                              |
|       | E5  | Guilherme Roque        | Definição do software para sistema servidor (aplicação e gateway) |
|       | E6  | Yan Martins            | Requisitar materiais e infraestrutura necessária                  |
| M2    | E7  | Guilherme Roque        | Implementação banco de dados                       |
|       | E8  | Guilherme Roque        | Implementação *dashboard* grafana                    |
|       | E9  | Elisa Rodrigues        | Implementação da leitura do DHT11                  |
|       | E10 | Yan Martins        | Especificação do payload na TTN                                             |
|       | E11 | Yan Martins        | Desenvolvimento do software de tratamento de dados( gateway) |
| M3    | E12 | Elisa Rodrigues        | Desenvolvimento dos drivers (estação)                             |
|       | E13 | Yan Martins            | Upload de dados na TTN     |
|       | E14 | Elisa Rodrigues        | Desenvolvimento da FSM (estação)                                  |
|       | E15 | Elisa Rodrigues        | Desenvolvimento da exibição dos dados (aplicação)                 |
| M4    | E16 | Guilherme Roque        | Validação em bancada                                              |
|       | E17 | Yan Martins            | Validação em campo                                                |
|       | E18 | Elisa Rodrigues        | Desenvolvimento dos ajustes finais                                |
| M5    | E19 | Guilherme Roque        | Definição do hardware para produto final                          |
|       | E20 | Yan Martins            | Definição do software para produto final                          |
|       | E21 | Elisa Rodrigues        | Projeto da PCB                                                    |
---

### Datas previstas

| Semana |     Dia    |    Metas   | Status |
|:------:|:----------:|:----------:|:------:|
|    1   | 17/12/2020 | entrega M1 |   OK   |
|    2   | 24/12/2020 |   Férias   |   -    |
|    3   | 31/12/2020 |   Férias   |   -    |
|    4   | 07/01/2021 |   Férias   |   -    |
|    5   | 14/01/2021 |   Férias   |   -    |
|    6   | 21/01/2021 |   Férias   |   -    |
|    7   | 28/01/2021 |   Férias   |   -    |
|    8   | 04/02/2021 |     M2     |   -    |
|    9   | 11/02/2021 |     M2     |   -    |
|   10   | 18/02/2021 |     M2     |   -    |
|   11   | 25/02/2021 |     M2     |   -    |
|   12   | 04/03/2021 | entrega M2 |        |
|   13   | 11/03/2021 |     M3     |        |
|   14   | 18/03/2021 |     M3     |        |
|   15   | 25/03/2021 | entrega M3 |        |
|   16   | 01/04/2021 |     M4     |        |
|   17   | 08/04/2021 | entrega M4 |        |
|   18   | 15/04/2021 |     M5     |        |
|   19   | 22/04/2021 | entrega M5 |        |

---

### Cronograma de Execução
|        | S | e | m | a | n | a | s |   |   |    |    |    |    |    |    |    |    |    |    |
|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|---|----|----|----|----|----|----|----|----|----|----|
| Etapas | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| E1     | x |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |
| E2     | x |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |
| E3     | x |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |
| E4     | x |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |
| E5     | x |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |
| E6     | x |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    |    |    |
| E7     |   |   |   |   |   |   |   | x | x | x  | x  | x  |    |    |    |    |    |    |    |
| E8     |   |   |   |   |   |   |   | x | x | x  | x  | x  |    |    |    |    |    |    |    |
| E9     |   |   |   |   |   |   |   | x | x | x  | x  | x  |    |    |    |    |    |    |    |
| E10    |   |   |   |   |   |   |   | x | x | x  | x  | x  |    |    |    |    |    |    |    |
| E11    |   |   |   |   |   |   |   | x | x | x  | x  | x  |    |    |    |    |    |    |    |
| E12    |   |   |   |   |   |   |   |   |   |    |    |    | x  | x  | x  |    |    |    |    |
| E13    |   |   |   |   |   |   |   |   |   |    |    |    | x  | x  | x  |    |    |    |    |
| E14    |   |   |   |   |   |   |   |   |   |    |    |    | x  | x  | x  |    |    |    |    |
| E15    |   |   |   |   |   |   |   |   |   |    |    |    | x  | x  | x  |    |    |    |    |
| E16    |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    | x  | x  |    |    |
| E17    |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |  x | x  |    |    |
| E18    |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |  x | x  |    |    |
| E19    |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    | x  | x  |
| E20    |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    | x  | x  |
| E21    |   |   |   |   |   |   |   |   |   |    |    |    |    |    |    |    |    | x  | x  |

---

## Materiais e insumos previstos

- Arduino/Esp
- Sensor de umidade
- Sensor de temperatura
- Módulo LoRa
- Gateway LoRa/Raspberry
- Módulo Bluetooth
- Protoboard
- Jumper
- Leds

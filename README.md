# Projeto IoT: Armario de Cozinha

## 1 - Descrição do projeto :four_leaf_clover:

Repositório contendo códigos para a avaliação final de C115, a proposta é informa a quantidade de produtos dentro do armário e quando o produto estiver acabando o mesmo é inserido dentro de uma lista de compras através de sensores e do protocolo MQTT, para envio das informações. Este projeto inicialmente não utiliza sensores externos, o mesmo realiza uma simulação deste sensore (através dos aquivos '''main.py''' e '''sensor.py'''. 

Para o projeto foi utilizado:

| **Tópicos** | **Software**  |
|------------------|--------------|
| IDE/Compilador | VS Code |
| Protocolo | MQTT |
| Linguagem | Python 3 |
| Aplicativo para Computador | MQTTBox |
| Aplicativo para Celular | IoT MQTT Panel |


## 2 - Como o usuário pode utilizar :desktop_computer:
É necessário baixar e instalar no sistema operacional utilizado, o python 3 e a IDE de preferência, aqui iremos utilizar VS Code.

### Instalando o python:
```
https://www.python.org/downloads/
``` 

### Instalando o VS Code:
```
https://code.visualstudio.com/
```

### Instalando o MQTTBox(Windows):
```
https://apps.microsoft.com/store/detail/mqttbox/9NBLGGH55JZG?hl=pt-br&gl=br
```

### Configuração do MQTTBox(Windows):
![image](https://user-images.githubusercontent.com/85804680/204111455-fef3ee68-9b04-4fdc-ab64-0f934d1c8e87.png)
![image](https://user-images.githubusercontent.com/85804680/204375624-7ba5b284-8c03-499a-b6b1-80691f2b7964.png)


### Instalando o IoT MQTT Panel(Android):
```
https://apps.microsoft.com/store/detail/mqttbox/9NBLGGH55JZG?hl=pt-br&gl=br
```

### Opção 1: Configuração do IoT MQTT Panel(Android):
![image](https://user-images.githubusercontent.com/85804680/204116780-660758db-6f97-498d-9886-bc48c214cf1c.png)
![image](https://user-images.githubusercontent.com/85804680/204116718-8c73d7cb-0c50-4c43-a2b5-a92a2e36ba94.png)
![image](https://user-images.githubusercontent.com/85804680/204116726-f28391b7-316e-4398-b9d1-a5b407fb6a71.png)

#### Configuração de cada item em armario:

<img src="https://user-images.githubusercontent.com/85804680/204117104-69a56c44-a96f-49b8-b4d5-b4f5624f67cf.png" width="250"> <img src="https://user-images.githubusercontent.com/85804680/204117150-f1324934-d431-4d40-bbe1-046df03a4b2f.png" width="250">

#### Configuração de cada item em Lista de Compras:
![image](https://user-images.githubusercontent.com/85804680/204117260-29783a20-6f96-4c71-8724-f2de1308e6d8.png)

### Opção 2: Configuração do IoT MQTT Panel(Android):

#### Passe o arquivo ```CozinhaIoT.json```, que está dentro da pasta ```IoTMQTTPanel```, para o um celular andoid e siga o seguintes passo:
![image](https://user-images.githubusercontent.com/85804680/204117328-a18db800-098d-4086-ba20-0eb3c4cb4897.png)
![image](https://user-images.githubusercontent.com/85804680/204117344-f34b82b4-3cc5-45e6-9857-e14864044343.png)
![image](https://user-images.githubusercontent.com/85804680/204117352-b1aab207-8567-4c59-8644-e0310359e8f1.png)
![image](https://user-images.githubusercontent.com/85804680/204117417-51f4d6e7-1b17-4d41-b5a7-55ed27f506a4.png)

### Clonando repositório:
```bash
git clone https://github.com/Matheusilva431/IoTCozinhaArmario
```

### Instalando as dependências:
```bash
pip install -r requirements.tx
```

### Executando:
```bash
python main.py
```

## 3 - Autores :curly_haired_man:

| **Nome**        |
|-----------------|
| [Matheus Chagas](https://github.com/Matheusilva431) |
| [Isadora Bello](https://github.com/isadorabello1) |

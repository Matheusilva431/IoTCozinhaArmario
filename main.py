import time
import threading
from input_sen.sensor import Sensor
from controller.armario import Armario
from controller.listacompra import ListaCompra
import paho.mqtt.client as mqtt

#Conectando ao mqtt
mqttBroker ="test.mosquitto.org"

client = mqtt.Client("armarioC115Inatel")
client.connect(mqttBroker)

#instanciando um armario
armario = Armario()

#Instanciando um sensor
sensor = Sensor()

#instanciando um lista de compras
listacompra = ListaCompra()

end = False
produtos = []

#Solicita e publicar os valores de produtos
def readSensor():
    global op
    global produtos
    while not(end):
        produtos = sensor.sendValue()
        payloadjson = armario.to_json(produto=produtos)
        client.publish(topic="Cozinha/Armario", retain=False, payload=payloadjson)
        time.sleep(5)

#Gera a lista de compras e publica
def readList():
    global op
    global produtos
    while not(end):
        produtos = sensor.sendValue()
        listacompra.Calculate(produtos)
        payloadjson = listacompra.to_json()
        client.publish(topic="Cozinha/ListaCompras", retain=False, payload=payloadjson)
        time.sleep(5)

def consumir():
    print("Esvasiando todos os produtos")
    sensor.emptyValue(produtos)
    time.sleep(15)

    print("Deixando na metada todos os produtos")
    sensor.halffullValue(produtos)
    time.sleep(15)

    print("Enchendo todos os produtos")
    sensor.fullValue(produtos)
    time.sleep(15)

    print("Consumindo 10% de arroz")
    sensor.consume(produt=produtos,nomeProduto="Arroz", porcentagem=10)
    time.sleep(15)

    print("Consumindo 80% de cafe")
    sensor.consume(produt=produtos,nomeProduto="Cafe", porcentagem=80)
    time.sleep(15)

    global end
    end = True

sensor.init()
x = threading.Thread(target=readSensor, args=())
y = threading.Thread(target=readList, args=())
z = threading.Thread(target=consumir, args=())
x.start()
y.start()
z.start()

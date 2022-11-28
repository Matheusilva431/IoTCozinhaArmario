from controller.armario import Armario

class Sensor(object):
    #Criando um vetor de produtos vazio
    produtos = []

    #Produtos pre-definidos
    criarprodutos = [
        ["Arroz", 0, 5, 2.1],
        ["Feijao", 0, 5, 2],
        ["Cafe", 0, 2, 0],
        ["Sal", 0, 2, 2],
        ["Acucar", 0, 5, 1.4],
        ["Farinha", 0, 2, 1.7],
        ["Oleo", 0, 10, 1],
        ["Leite", 0, 10, 2],
        ["Molho", 0, 10, 3],
        ["CremeLeite", 0, 10, 4],
        ["Condensado", 0, 10, 5],
        ["Milho", 0, 10, 7],
        ["Ervilha", 0, 10, 2],
        ["Miojo", 0, 10, 8],
    ]

    #instanciando um armario
    armario = Armario()

    def init(self):
        #Inserindo os produtos pre-definido no vetor de produtos
        for aux in self.criarprodutos:
            self.produtos = self.armario.createProduct(aux[0], aux[1], aux[2], aux[3], self.produtos)

    #Função atualizar valores de produtos
    def update(self, produt):
        self.produtos = produt

    #Função que envia os valores dos produtos
    def sendValue(self):
        return self.produtos

    #Função que enche
    def fullValue(self, produt):
        for i in range(len(produt)):
            produt[i].atual = self.criarprodutos[i][2]
        
        self.update(produt)

    #Função que esvaziar
    def emptyValue(self, produt):
        for i in range(len(produt)):
            produt[i].atual = self.criarprodutos[i][1]
        
        self.update(produt)

    #Função que deixa meio cheio
    def halffullValue(self, produt):
        for i in range(len(produt)):
            produt[i].atual = self.criarprodutos[i][2]/2
        
        self.update(produt)

    #Consumir parte do produto
    def consume(self, produt, nomeProduto, porcentagem):
        for aux in produt:
            if aux.nome == nomeProduto:
                aux.atual *= (100-porcentagem)/100

        self.update(produt)

"""class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5

        self.idade += 1
    
    def engordar(self,):
        self.peso += 1
    
    def emagrecer(self,):
        self.peso -= 1
    
    def crescer(self,):
        self.altura += 1

lucas = Pessoa("Lucas", 20, 80, 1.80)
jenifer = Pessoa("Jenifer", 21, 80, 1.80)"""


class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = 5
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        gasolina_carro = valor / self.valorLitro
        print("o valor abastecido foi:", "R$",valor, "rendendo:", gasolina_carro,'litros')
        self.quantidadeCombustivel -= gasolina_carro
        print("litros restantes:", self.quantidadeCombustivel)

    def abastecerPorLitro(self, litros):
        gasolina_carro = litros
        print("o litro abastecido foi:", litros, "rendendo:", gasolina_carro,'litros')
        self.quantidadeCombustivel -= gasolina_carro
        print("litros restantes:", self.quantidadeCombustivel)
    
    def alterarValor(self, novoValor):
        self.valorLitro = novoValor
        print("o valor foi alterado para:", self.valorLitro)

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel
        print("o combustivel foi alterado para:", self.tipoCombustivel)
    
    def alterarQuantidade(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade
        print("a quantidade foi alterada para:", self.quantidadeCombustivel)
    
bomba1 = BombaCombustivel("Gasolina", 5, 100)
bomba2 = BombaCombustivel("Etanol", 6, 100)

bomba1.abastecerPorValor(100)
bomba1.abastecerPorLitro(10)
bomba1.alterarValor(4)
bomba1.alterarCombustivel("GNV")
bomba1.alterarQuantidade(50)
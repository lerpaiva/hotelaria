class Hotel:
    def __init__(self,nome,endereco,cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.cliente =  {}
        self.reservas = {}
        

    def cadastrarCliente(self, id, nome, cpf, tel):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
        self.cliente[self.id] = [self.nome, self.cpf , self.tel]



    def listarClientes(self):
        for chave, valor in self.cliente.items():
            print(f"ID: {chave} -Nome: {valor[0]} -CPF: {valor[1]} -Telefone: {valor[2]}")

    def reservarQuartos(self,id,reserva_quarto):
        self.idd = id
        self.reserva_quarto = reserva_quarto
        
        if self.reserva_quarto == 1:
            x = "Quarto deluxe"
        elif self.reserva_quarto == 2:
            x = "Quarto casal"
        elif self.reserva_quarto == 3:
            x = "Quarto solteiro"
        else:
            x = "Opção inválida"
        self.reservas[self.idd] = x

    def listarReservas(self):
        for chave, valor in self.reservas.items():
            print(f"ID: {chave} - Quarto: {valor}")

    def cancelarReserva(self, id):
        if id in self.reservas:
            quarto_reservado = self.reservas[id]
            del self.reservas[id]
            if quarto_reservado == 1:
                DeluxeQuarto.setReservaQuarto(DeluxeQuarto.getqtdQuarto()+1)
            elif quarto_reservado == 2:
                CasalQuarto.setReservaQuarto(CasalQuarto.getqtdQuarto()+1)
            elif quarto_reservado == 3:
                SolteiroQuarto.setReservaQuarto(SolteiroQuarto.getqtdQuarto()+1)
            print(f"Reserva do cliente de id '{id}' foi cancelada")
        else:
            print("Sem registro")
    def apagarCadastro(self, id):
        del self.cliente[id]
        print("Cliente excluído com sucesso!!!!!")


class Quarto(Hotel):
    def __init__(self, qtd, capacidade, valor,desc):
        self.qtd = qtd
        self.capacidade = capacidade
        self.valor = valor
        self.desc = desc
    def getqtdQuarto(self):
        return self.qtd
    def setReservaQuarto(self,qtd):
        self.qtd = qtd
    def getDesc(self):
        return self.desc
    def getValor(self):
        return self.valor

class DeluxeQuarto(Quarto):
    pass
class CasalQuarto(Quarto):
    pass
class SolteiroQuarto(Quarto):
    pass
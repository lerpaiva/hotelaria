from classes import *
import os

hotel = Hotel("MALT","SP","123456789")
quartoDeluxe = DeluxeQuarto(2,4,500,"Quarto espaçoso e com cama Queen")
quartoCasal = CasalQuarto(3,2,300,"Quarto com frigobar e cama King")
quartoSolteiro = SolteiroQuarto(8,1,150,"Quarto simples e com cama de solteiro")
def main():
    contID = 0
    
    leave = False
    while leave == False:
        try:
            os.system("cls")
            print("-Hotel MALT-")
            print(" [1] Cadastrar cliente \n [2] Quartos disponíveis \n [3] Reservar quarto \n [4] Cancelar reserva \n [5] Listar quartos reservados \n [6] Listar clientes \n [7] Apagar cadastro do cliente \n [8] Sair")
            menu = int (input("O que deseja fazer?: "))
            os.system("pause")
            match menu:
                case 1:
                    os.system("cls")
                    print("-Cadastro de Cliente-")
                    print("Informe os dados do cliente")
                    nome = input("Nome: ")
                    cpf = int (input("CPF: "))
                    tel = int (input("Telefone: "))
                    contID += 1
                    id = contID
                    hotel.cadastrarCliente(id,nome,cpf,tel)
                    print(f"O id do cliente '{nome}' é {id}")
                    print ("Cliente cadastrado")
                    os.system("pause")
                case 2:
                    os.system("cls")
                    print("-Quartos disponíveis-")
                    print(f"Quartos DELUXE: {quartoDeluxe.getqtdQuarto()} - Descrição: {quartoDeluxe.getDesc()} - Preço: R${quartoDeluxe.getValor()}")
                    print(f"Quartos CASAL: {quartoCasal.getqtdQuarto()} - Descrição: {quartoCasal.getDesc()} - Preço: R${quartoCasal.getValor()}")
                    print(f"Quartos SOLTEIRO: {quartoSolteiro.getqtdQuarto()} - Descrição: {quartoSolteiro.getDesc()} - Preço: R${quartoSolteiro.getValor()}")
                    os.system("pause")
                case 3:
                    os.system("cls")
                    print("-Quartos disponíveis-")
                    print(f"Quartos DELUXE: {quartoDeluxe.getqtdQuarto()} - Descrição: {quartoDeluxe.getDesc()} - Preço: R${quartoDeluxe.getValor()}")
                    print(f"Quartos CASAL: {quartoCasal.getqtdQuarto()} - Descrição: {quartoCasal.getDesc()} - Preço: R${quartoCasal.getValor()}")
                    print(f"Quartos SOLTEIRO: {quartoSolteiro.getqtdQuarto()} - Descrição: {quartoSolteiro.getDesc()} - Preço: R${quartoSolteiro.getValor()}")
                    print("")
                    reserva_quarto = int(input("--Qual quarto deseja reservar?-- \n [1] Deluxe \n [2] Casal \n [3] Solteiro \n - "))
                    idd = int (input("ID do cliente:"))

                    if  reserva_quarto>0 and reserva_quarto <=3:
                        hotel.reservarQuartos(idd,reserva_quarto)
                        if reserva_quarto == 1:
                                quartoDeluxe.setReservaQuarto(quartoDeluxe.getqtdQuarto()-1)
                                print("Quarto deluxe reservado com sucesso!!")
                        elif reserva_quarto ==2:
                                quartoCasal.setReservaQuarto(quartoCasal.getqtdQuarto()-1)
                                print("Quarto casal reservado com sucesso!!")
                        else:
                            quartoSolteiro.setReservaQuarto(quartoSolteiro.getqtdQuarto()-1)
                            print("Quarto de solteiro reservado com sucesso!!")
                    else:
                        print("opção inválida")
                    os.system("pause")

                case 4:
                    os.system("cls")
                    print("-Cancelamento de reserva-")
                    idee = int(input("ID do cliente que deseja cancelar a reserva: "))
                    hotel.cancelarReserva(idee)
                    os.system("pause")
                case 5:
                    os.system("cls")
                    print("-Lista de quartos reservados-")
                    print("")
                    hotel.listarReservas()
                    os.system("pause")
                case 6:
                    os.system("cls")
                    print("-Lista de clientes-")
                    hotel.listarClientes()
                    os.system("pause")
                case 7:
                    os.system("cls")
                    print("-Apagar Cadastros-")
                    ideee = int(input("Informe o id do cadastro que deseja apagar: "))
                    hotel.apagarCadastro(ideee)
                case 8:
                    leave = True
                case _:
                    print("Opção inválida")

        except Exception as erro:
            print("Inválido")

        
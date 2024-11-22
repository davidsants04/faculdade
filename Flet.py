from flet import *

nome_bank = []
senha_bank = []
dinheiro_bank = []
cpf_bank = []
cartao_bank = []

def main (page:Page):

    def bank_data(e):
        nome_bank.append(nome_user.value)
        senha_bank.append(senha.value)
        dinheiro_bank.append(dinheiro.value)
        cpf_bank.append(cpf.value)
        cartao_bank.append(cartao.value)

        print(f"{nome_bank},{senha_bank},{dinheiro_bank},{cpf_bank},{cartao_bank}")

    page.title = "Gerador de dinheiro infinito"
    nome_user = TextField(label="Nome")
    senha= TextField(label="Senha",password=True)
    btncadastrarusu=ElevatedButton('Cadastrar',icon=icons.ADD,on_click=bank_data)
    linha=Row(controls=[nome_user,senha,btncadastrarusu])
    page.add(linha)
    dinheiro = TextField(label="dinheiro")
    cpf=TextField(label="cpf")
    cartao=TextField(label="numero do cartão")
    linha2=Row(controls=[dinheiro,cpf,cartao])
    page.add(linha2)
    image = Image(src=f'poo/OIP (1).jpg', width=950, height=500)
    page.add(image)
    page.update()



app(main)

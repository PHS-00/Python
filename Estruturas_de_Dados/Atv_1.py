import datetime

class User:
    # O método __init__ inicializar os valores
    def __init__(self, name, age, email, date_birth):
        self.name = name
        self.age = age
        self.email = email
        self.date_birth = date_birth

    

    # O método __str__ define como o objeto aparece ao dar um print()
    def __str__(self):
        return (f"|Usuário:\n"
                f"|____Nome: {self.name}\n"
                f"|____Idade: {self.age}\n"
                f"|____Email: {self.email}\n"
                f"|____Nascimento: {self.date_birth.strftime('%d/%m/%Y')}")

name = str(input("Digite o nome do Usuario: "))
age = int(input("Digite a idade do Usuario: "))
email = str(input("Digite o email do Usuario: "))

if email.find("@") >= 0 and email.find("@") < email.rfind("."):
    print("Email válido")
else:
    print("Email inválido")

date = [0, 0, 0]
label = ['Dia', 'Mes', "Ano"]

for x in range(3):
    date[x] = int(input(f"Digite {label[x]}: "))

new_user = User(name, age, email, datetime.date(day = date[0], month = date[1], year = date[2]))

print("\n\n")
print(new_user)

cadastro = {"542345263": ["Michelle", 1978, "São José do Rio Pardo, SP"],
            "51804898510": ["Mayene", 2002, "São Paulo", "SP" ],
            "874389578": ["Mario", 2005, "São Paulo" , "SP" ]}

'''print(cadastro)
print(cadastro["542345263"])


cadastro["542345263"][1]= 1980
print(cadastro["542345263"])

del cadastro ["542345263"]
print(cadastro)

print("51804898510")

print("51804898510" in cadastro) '''

while True:
    cpf=input("Digite seu cpf: ")

    if cpf == "fim":
        break
    if cpf in cadastro:
        print(f"Ano de nascimento da(o) {cadastro[cpf][0]} é {cadastro[cpf][1]}.")
    else:
        print("produto não encontrado")



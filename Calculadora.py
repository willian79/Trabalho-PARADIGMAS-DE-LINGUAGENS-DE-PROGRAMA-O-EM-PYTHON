# Função Adicionar
def adicionar(x, y):
    return x + y

# Função Subtrair
def subtrair(x, y):
    return x - y

# Função Multiplicar
def multiplicar(x, y):
    return x * y

# Função Dividir
def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    else: 
        return x / y
def main():
    while True:
        # Exibe o menu de opções
        print("Selecione a operação:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")
        
        # Recebe a escolha do usuário
        escolha = input("Digite a escolha (1/2/3/4/5): ")
        
        # Verifica se a escolha é para sair
        if escolha == '5':
            print("Saindo do programa. Adeus!")
            break
        
        # Verifica se a escolha é válida
        if escolha in ['1', '2', '3', '4']:
            try:
                # Recebe os números do usuário
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                # Realiza a operação correspondente
                if escolha == '1':
                    print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
                elif escolha == '2':
                    print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
                elif escolha == '3':
                    print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                elif escolha == '4':
                    resultado = dividir(num1, num2)
                    if resultado == "Erro: Divisão por zero não é permitida.":
                        print(resultado)
                    else:
                        print(f"Resultado: {num1} / {num2} = {resultado}")
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")
        else:
            print("Escolha inválida. Por favor, selecione uma opção entre 1 e 5.")
            
if __name__ == "__main__":
    main()

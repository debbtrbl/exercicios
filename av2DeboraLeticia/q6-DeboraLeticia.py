with open('trabalhadores_entrada.txt', 'r') as arquivo_entrada:
    with open('trabalhadores_saida.txt', 'w') as arquivo_saida:
        for linha in arquivo_entrada:
            partes = linha.strip().split()
            nome = partes[0]
            horas = partes[1:]
            horas1 = []
            for i in horas:
                horas1.append(int(i))  
            media = sum(horas1) / len(horas1)

            arquivo_saida.write(f"{nome} {media:.2f}\n")

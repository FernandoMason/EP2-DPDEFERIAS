def preenche_frota(dados_de_posicionamento, nome_navio, frota):
    def define_posicoes(linha, coluna, orientacao, tamanho):
        posicao = []
        posicao.append([linha, coluna])
        i = 0
        if orientacao == "vertical":
            while i < tamanho - 1:
                linha += 1
                i += 1
                posicao.append([linha, coluna])
        elif orientacao == "horizontal":
            while i < tamanho - 1:
                coluna += 1
                i += 1
                posicao.append([linha, coluna])
        return posicao

    posicoes = define_posicoes(dados_de_posicionamento["linha"],
                               dados_de_posicionamento["coluna"],
                               dados_de_posicionamento["orientacao"],
                               dados_de_posicionamento["tamanho"])

    novo_navio = {"tipo": nome_navio, "posicoes": posicoes}
    frota.append(novo_navio)
    return frota
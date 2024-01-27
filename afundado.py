def afundados(frota, tabuleiro):
    navios_afundados = 0

    for navio in frota:
        afundado = True

        for posicao in navio["posicoes"]:
            linha, coluna = posicao

            if tabuleiro[linha][coluna] != 'X':
                afundado = False
                break

        if afundado:
            navios_afundados += 1

    return navios_afundados

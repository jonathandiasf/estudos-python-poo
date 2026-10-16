"""Demonstra operadores lógicos e associa países aos seus continentes."""

paises_por_continente = {
    "América do Sul": ["Brasil", "Argentina", "Chile", "Uruguai"],
    "Europa": ["Alemanha", "França", "Espanha"],
    "Ásia": ["China", "Japão", "Índia"],
    "Oceania": ["Austrália", "Nova Zelândia"],
    "África": ["Nigéria", "Egito", "África do Sul"],
    "América do Norte": ["Estados Unidos", "Canadá", "México"],
}

continente_por_pais = {
    pais.casefold(): continente
    for continente, paises in paises_por_continente.items()
    for pais in paises
}


def exibir_paises_por_continente():
    print("Países disponíveis por continente:")
    for continente, paises in paises_por_continente.items():
        print(f"- {continente}: {', '.join(paises)}")



def consultar_pais():
    pais_informado = input("\nDigite o nome de um país para consultar: ").strip()

    # not verifica se a entrada está vazia.
    if not pais_informado:
        print("Nenhum país foi informado.")
        return

    pais_normalizado = pais_informado.casefold()

    # and exige que a entrada não esteja vazia e que o país esteja cadastrado.
    if pais_informado and pais_normalizado in continente_por_pais:
        continente = continente_por_pais[pais_normalizado]
        print(f"{pais_informado.title()} pertence à {continente}.")

        # or verifica se o continente é um dos dois representados neste exemplo.
        if continente == "América do Sul" or continente == "Europa":
            print("Este continente está representado na lista de estudos.")
    else:
        print(f"{pais_informado} não está na lista de países cadastrados.")


def main():
    print("Demonstração dos operadores lógicos and, or e not.")
    exibir_paises_por_continente()
    consultar_pais()


if __name__ == "__main__":
    main()

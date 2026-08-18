def ler_nota(mensagem):
    """
    Solicita uma nota entre 0 e 10.
    """

    while True:

        try:

            nota = float(input(mensagem))

            if nota < 0 or nota > 10:
                print("ERRO: a nota deve estar entre 0 e 10.")
            else:
                return nota

        except ValueError:
            print("ERRO: digite um número válido.")
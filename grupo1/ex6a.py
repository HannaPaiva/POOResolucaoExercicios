def comparar_strings(str1, str2):
    # Verificar o comprimento
    len_str1 = len(str1)
    len_str2 = len(str2)

    print(f"Tamanho de \"{str1}\": {len_str1} caracteres")
    print(f"Tamanho de \"{str2}\": {len_str2} caracteres")

    if len_str1 == len_str2:
        print("As duas strings têm o mesmo comprimento.")
    else:
        print("As duas strings são de tamanhos diferentes.")


    if str1 == str2:
        print("As duas strings possuem o mesmo conteúdo.")
    else:
        print("As duas strings possuem conteúdo diferente.")


string1 = "Portugal é campeão da Europa"
string2 = "Portugal! é campeão da Europa!"

comparar_strings(string1, string2)

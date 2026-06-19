from candidaturas import adicionar, listar, atualizar_status, exportar_csv


def menu():
    while True:
        print("\n=== PAINEL DE CANDIDATURAS ===")
        print("1. Adicionar candidatura")
        print("2. Listar todas")
        print("3. Filtrar por status")
        print("4. Atualizar status")
        print("5. Exportar CSV")
        print("0. Sair")

        opcao = input("\nOpção: ").strip()

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            print("Status: Candidatado / Entrevista / Reprovado / Oferta")
            filtro = input("Filtrar por: ").strip()
            listar(filtro_status=filtro)
        elif opcao == "4":
            atualizar_status()
        elif opcao == "5":
            exportar_csv()
        elif opcao == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
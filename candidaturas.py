import csv
from datetime import date
from storage import carregar, salvar


def adicionar():
    dados = carregar()
    empresa = input("Empresa: ").strip()
    vaga = input("Vaga: ").strip()
    plataforma = input("Plataforma (LinkedIn/InfoJobs/Indeed/Outro): ").strip()

    if not empresa or not vaga:
        print("Empresa e vaga são obrigatórios.")
        return

    dados.append({
        "id": len(dados) + 1,
        "empresa": empresa,
        "vaga": vaga,
        "plataforma": plataforma,
        "status": "Candidatado",
        "data": str(date.today()),
        "observacoes": ""
    })
    salvar(dados)
    print("✅ Candidatura registrada.")


def listar(filtro_status=None, filtro_plataforma=None):
    dados = carregar()
    if not dados:
        print("Nenhuma candidatura registrada.")
        return

    if filtro_status:
        dados = [c for c in dados if c["status"] == filtro_status]
    if filtro_plataforma:
        dados = [c for c in dados if c["plataforma"] == filtro_plataforma]

    print(f"\n{'ID':<4} {'Empresa':<20} {'Vaga':<25} {'Status':<12} {'Data'}")
    print("-" * 70)
    for c in dados:
        print(f"{c['id']:<4} {c['empresa']:<20} {c['vaga']:<25} {c['status']:<12} {c['data']}")


def atualizar_status():
    dados = carregar()
    listar()
    try:
        id_ = int(input("\nID para atualizar: "))
        item = next((c for c in dados if c["id"] == id_), None)
        if not item:
            print("ID não encontrado.")
            return
        print("1-Candidatado  2-Entrevista  3-Reprovado  4-Oferta")
        opcao = input("Novo status: ")
        mapa = {"1": "Candidatado", "2": "Entrevista", "3": "Reprovado", "4": "Oferta"}
        if opcao in mapa:
            item["status"] = mapa[opcao]
            salvar(dados)
            print(f"✅ Status atualizado para: {item['status']}")
    except ValueError:
        print("ID inválido.")


def exportar_csv():
    dados = carregar()
    if not dados:
        print("Nenhuma candidatura para exportar.")
        return
    with open("candidaturas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=dados[0].keys())
        writer.writeheader()
        writer.writerows(dados)
    print("✅ Exportado para candidaturas.csv")
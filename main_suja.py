# código bagunçado que ignora qualquer padrão
import random

def pessoaCoisaFuncional(nome, cpf, email, inventario, brainstorming_data):
    pessoa = {
        "identificacao": f"{nome}-{random.randint(0,9999)}",
        "dados": [nome, cpf, email, "ATIVO", True],
        "acoes": []
    }

    # Acessa o projeto limpo...
    from services.armazenador import ArmazenadorDeInventario
    from services.barista import BaristaCorporativo
    from services.consultor import ConsultorDeInovacao

    # Totalmente sem padrão
    def fazTudoAleatorio():
        print("\n--- Iniciando função fazTudoAleatorio() ---")
        try:
            if random.randint(0, 1):
                print("Chamando serviço limpo: ArmazenadorDeInventario")
                ArmazenadorDeInventario().armazenar(inventario)
            else:
                print("Chamando serviço limpo: BaristaCorporativo")
                BaristaCorporativo().preparar_cafe("latte", 3, 80)
        except Exception as tudoErrado:
            print("Algo deu ruim em fazTudoAleatorio():", tudoErrado)

    def misturarIdeiaECafe():
        print("\n--- Iniciando função misturarIdeiaECafe() ---")
        try:
            cafe = BaristaCorporativo()
            ideias = ConsultorDeInovacao()
            cafe.preparar_cafe("americano", 1, 70)
            ideias.gerar_ideias(brainstorming_data)
            print("Café + Ideias = Sucesso?")
        except:
            print("Erro ao misturar café e ideias")

    def exportaDadosDeTudoQueForPossivel():
        print("\n--- Exportando dados de forma caótica ---")
        print("Nome:", pessoa["dados"][0])
        print("Email:", pessoa["dados"][2])
        print("Status:", pessoa["dados"][3])
        print("Chamando novamente função fazTudoAleatorio()")
        fazTudoAleatorio()

    pessoa["acoes"].append(fazTudoAleatorio)
    pessoa["acoes"].append(misturarIdeiaECafe)
    pessoa["acoes"].append(exportaDadosDeTudoQueForPossivel)

    return pessoa

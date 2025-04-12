from utils.mocks import processar_dado_para_ideia, avaliar_viabilidade, gerar_documento_com_ideias, enviar_para_diretoria, salvar_backup, enviar_alerta_para_gerencia

class ConsultorDeInovacao:
    def gerar_ideias(self, brainstorming_data):
        try:
            ideias = []
            for dado in brainstorming_data:
                ideia = processar_dado_para_ideia(dado)
                if avaliar_viabilidade(ideia):
                    ideias.append(ideia)
            documento = gerar_documento_com_ideias(ideias)
            enviar_para_diretoria(documento)
            print("Ideias enviadas para diretoria.")
        except Exception as erro:
            print(f"Erro ao processar ideias criativas: {erro}")
            salvar_backup(brainstorming_data)
            enviar_alerta_para_gerencia()
            raise erro

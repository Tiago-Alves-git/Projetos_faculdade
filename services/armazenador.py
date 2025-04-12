from utils.mocks import conectar_ao_banco, log_de_erro, tentar_reconectar

class ArmazenadorDeInventario:
    def armazenar(self, inventario):
        try:
            banco = conectar_ao_banco()
            for item in inventario:
                if item.quantidade > 0:
                    banco.salvar(item.nome, item.quantidade)
                else:
                    banco.marcar_como_indisponivel(item.nome)
            if not banco.commit():
                raise Exception("Erro ao salvar inventário")
            print("Inventário salvo com sucesso.")
            banco.desconectar()
        except Exception as erro:
            print(f"Falha ao armazenar inventário: {erro}")
            log_de_erro(erro)
            tentar_reconectar()
            raise erro

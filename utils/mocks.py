def conectar_ao_banco():
    class BancoSimulado:
        def salvar(self, nome, qtd): print(f"Salvando {nome} ({qtd})")
        def marcar_como_indisponivel(self, nome): print(f"{nome} indisponível")
        def commit(self): return True
        def desconectar(self): print("Desconectado")
    return BancoSimulado()

def log_de_erro(erro): print(f"[LOG] {erro}")
def tentar_reconectar(): print("Tentando reconectar...")

class Cafeteira:
    def ligar(self): print("Cafeteira ligada")
    def configurar_tipo(self, tipo): print(f"Tipo: {tipo}")
    def definir_temperatura(self, t): print(f"Temperatura: {t}°C")
    def adicionar_acucar(self, qtd): print(f"Adicionando {qtd} de açúcar")
    def iniciar(self): print("Preparando café...")
    def finalizado(self): return True
    def retirar(self): return "café quentinho"

class Bandeja:
    def servir(self, cafe): print(f"Servindo {cafe}")

def registrar_erro_no_sistema(e): print(f"[Sistema] Erro registrado: {e}")
def notificar_chefe(msg): print(f"Chefe notificado: {msg}")

def processar_dado_para_ideia(dado): return f"Ideia a partir de {dado}"
def avaliar_viabilidade(ideia): return True
def gerar_documento_com_ideias(ideias): return f"Documento: {ideias}"
def enviar_para_diretoria(doc): print(f"Enviado à diretoria: {doc}")
def salvar_backup(dados): print("Backup feito")
def enviar_alerta_para_gerencia(): print("Alerta para gerência enviado")

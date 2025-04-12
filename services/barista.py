from utils.mocks import Cafeteira, Bandeja, registrar_erro_no_sistema, notificar_chefe

class BaristaCorporativo:
    def preparar_cafe(self, tipo, acucar, temperatura):
        try:
            cafeteira = Cafeteira()
            cafeteira.ligar()
            cafeteira.configurar_tipo(tipo)
            cafeteira.definir_temperatura(temperatura)
            if acucar > 0:
                cafeteira.adicionar_acucar(acucar)
            cafeteira.iniciar()
            if not cafeteira.finalizado():
                raise Exception("Café não foi preparado corretamente.")
            bandeja = Bandeja()
            bandeja.servir(cafeteira.retirar())
            print("Café servido com sucesso.")
        except Exception as e:
            print(f"Erro ao fazer café: {e}")
            registrar_erro_no_sistema(e)
            notificar_chefe("Seu café atrasará.")
            raise e

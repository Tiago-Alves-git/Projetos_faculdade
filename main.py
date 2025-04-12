from models.pessoa import Pessoa
from services.armazenador import ArmazenadorDeInventario
from services.barista import BaristaCorporativo
from services.consultor import ConsultorDeInovacao

# Criando uma pessoa
tiago = Pessoa("Tiago", "123.456.789-00", "tiago@email.com")

# Usando os serviços separados
armazenador = ArmazenadorDeInventario()
armazenador.armazenar(inventario=[])

barista = BaristaCorporativo()
barista.preparar_cafe(tipo="espresso", acucar=2, temperatura=90)

consultor = ConsultorDeInovacao()
consultor.gerar_ideias(brainstorming_data=["IA para RH", "Logística 4.0"])

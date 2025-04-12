
# ☠️ Como **NÃO** aplicar a primeira regra do SOLID (SRP)

> A seguir, um caso real de **transtorno arquitetural** em Python.  
Prepare-se para um passeio pelo caos.

---

## 🔥 O "Herói" do Código Sujo

```python
def pessoaCoisaFuncional(nome, cpf, email, inventario, brainstorming_data):
    # Armazena nome, cpf, email... e um estado aleatório
    pessoa = {
        "identificacao": f"{nome}-{random.randint(0,9999)}",
        "dados": [nome, cpf, email, "ATIVO", True],
        "acoes": []
    }

    # Mistura funções aleatórias e serviços do projeto limpo
    def fazTudoAleatorio(): ...
    def misturarIdeiaECafe(): ...
    def exportaDadosDeTudoQueForPossivel(): ...

    # Armazena as funções num array porque sim
    pessoa["acoes"].append(...)
    return pessoa
```

---

## 🧠 Funções que fazem tudo, nada e o inesperado

### ☕ `misturarIdeiaECafe()`

```python
def misturarIdeiaECafe():
    cafe = BaristaCorporativo()
    ideias = ConsultorDeInovacao()
    cafe.preparar_cafe("americano", 1, 70)
    ideias.gerar_ideias(brainstorming_data)
```

👎 Problemas:

- Não respeita o princípio de coesão
- A função não tem objetivo claro
- Junta dois serviços distintos em uma única ideia bizarra: **"ideação cafeinada"**

---

### 🎲 `fazTudoAleatorio()`

```python
def fazTudoAleatorio():
    if random.randint(0, 1):
        ArmazenadorDeInventario().armazenar(inventario)
    else:
        BaristaCorporativo().preparar_cafe("latte", 3, 80)
```

👎 Problemas:

- Decisões aleatórias no fluxo de trabalho
- Sem testes possíveis
- Sem qualquer lógica de negócio previsível

---

## 🧩 Arquitetura do Terror

### 🔗 Comunicação com o Projeto Limpo

- Importações são feitas **dentro das funções**
- Chamadas aos serviços limpos feitas sem controle ou abstração
- Ignora qualquer estrutura de injeção de dependência ou camadas
- Não há encapsulamento — tudo acessa tudo

```
sujo -> services/armazenador_de_inventario.py
      -> services/barista_corporativo.py
      -> services/consultor_de_inovacao.py
```

---

## 📉 Resultado da Execução

```bash
--- Iniciando função fazTudoAleatorio() ---
Chamando serviço limpo: BaristaCorporativo
[INFO] Preparando café: latte com 3 colheres de açúcar a 80°C
[INFO] Café pronto!

--- Iniciando função misturarIdeiaECafe() ---
[INFO] Preparando café: americano com 1 colheres de açúcar a 70°C
[INFO] Café pronto!
[INFO] Gerando ideias com base em dados de brainstorming
[INFO] Ideias geradas: ['Ideia 1', 'Ideia 2', 'Ideia 3']
Café + Ideias = Sucesso?

--- Exportando dados de forma caótica ---
Nome: Fulano
Email: fulano@email.com
Status: ATIVO
Chamando novamente função fazTudoAleatorio()
```

---

## 🚨 Diagnóstico SRP

| Área                  | Sintoma                                                           | Diagnóstico                     |
|-----------------------|--------------------------------------------------------------------|---------------------------------|
| Classe `Pessoa`       | Faz café, gera ideias e armazena inventário                       | **Multifunção do mal**          |
| Funções internas      | Sem propósito único                                               | **Alta coesão inexistente**     |
| Estrutura             | Código difícil de testar, manter ou escalar                       | **Violação brutal de SRP**      |
| Importações           | Acontecem dentro das funções, sem estrutura                       | **Design Frankenstein**         |
| Comunicação com o limpo | Acesso direto sem contrato, sem isolamento                     | **Acoplamento nojento**         |

---

## ✅ Como deveria ser...

### 🧼 Projeto Limpo (já feito!)

```python
class Pessoa:
    def __init__(self, nome, cpf, email): ...
```

E os serviços separados:

```python
class ArmazenadorDeInventario:
    def armazenar(self, inventario): ...

class BaristaCorporativo:
    def preparar_cafe(self, tipo, acucar, temperatura): ...

class ConsultorDeInovacao:
    def gerar_ideias(self, brainstorming_data): ...
```

---

## 💡 Conclusão

**Este projeto sujo é uma lição viva sobre o SRP:**

> *"Uma classe deve ter um — e apenas um — motivo para mudar."*  
Aqui, a pessoa muda porque o café queimou, o inventário falhou, e a ideia foi ruim.

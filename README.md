# Sprint-01-Challange-Godwe-2026-MLAM
readme_content = """# CHALLENGE SPRINT 1
## Plataforma de Orquestração de Recarga Comercial de Veículos Elétricos

### RELATÓRIO TÉCNICO
#### Análise Exploratória de Dados — Estações de Recarga EV

**Integrantes:**
* [Vinicius Molena] — Matrícula: [571270]
* [Matheus Ferreira] — Matrícula: [569638]
* [Nathan Werner] — Matrícula: [572925]
* [Gabriel Vilas] — Matrícula: [571603]
* [Gustavo Henrique] — Matrícula: [569921]
* [Ricardo Santos] — Matrícula: [569600]

**Data:** Maio de 2026

---

## 1. Introdução
Este relatório apresenta a análise exploratória de uma base de dados real contendo informações sobre 385 estações de recarga de veículos elétricos localizadas no estado de Connecticut, Estados Unidos. A análise foi desenvolvida no contexto de uma plataforma de orquestração de recarga comercial, cujo objetivo é registrar dados de sessão, acionar regras de cobrança dinâmica e integrar automação física via protocolos OCPP e MODBUS.

A base original foi obtida a partir de dados públicos de estações de recarga e enriquecida com variáveis derivadas que simulam cenários operacionais realistas, como sessões mensais estimadas, potência máxima de carregamento e tarifas médias por kWh. Todas as variáveis derivadas foram calculadas a partir de parâmetros reais da infraestrutura existente.

---

## 2. Descrição da Base de Dados
A base de dados final contém 385 observações e 14 variáveis, organizadas conforme a classificação estatística apresentada a seguir.

### 2.1 Classificação das Variáveis

| Variável | Tipo | Classificação | Descrição |
| :--- | :--- | :--- | :--- |
| Nome_Estacao | Qualitativa | Nominal | Nome do estabelecimento |
| Cidade | Qualitativa | Nominal | Cidade de localização |
| Tipo_Local | Qualitativa | Nominal | Categoria do estabelecimento |
| Conector_Predominante | Qualitativa | Nominal | Tipo principal de conector |
| Porte_Estacao | Qualitativa | Ordinal | Porte (Peq < Méd < Gra < M.Grande) |
| Faixa_Disponibilidade | Qualitativa | Ordinal | Nível de disponibilidade |
| Qtd_Level2 | Quantitativa | Discreta | Conectores Level 2 |
| Qtd_DC_Fast | Quantitativa | Discreta | Conectores DC Fast |
| Total_Conectores | Quantitativa | Discreta | Total de conectores |
| Sessoes_Mensais | Quantitativa | Discreta | Sessões estimadas/mês |
| Potencia_Maxima_kW | Quantitativa | Contínua | Potência máxima (kW) |
| Tarifa_Media_kWh | Quantitativa | Contínua | Tarifa média ($/kWh) |
| Latitude | Quantitativa | Contínua | Coordenada geográfica |
| Longitude | Quantitativa | Contínua | Coordenada geográfica |

Tabela 1 — Classificação das variáveis da base de dados

---

## 3. Análise de Distribuição de Frequências

### 3.1 Total de Conectores (Variável Quantitativa Discreta)
A variável Total_Conectores representa o número total de pontos de carregamento disponíveis em cada estação. A tabela de distribuição de frequências revela a concentração da infraestrutura de recarga.

| Xi | Fi | Fac | fri | frac | fri% | frac% |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 93 | 93 | 0.2416 | 0.2416 | 24.16 | 24.16 |
| 2 | 189 | 282 | 0.4909 | 0.7325 | 49.09 | 73.25 |
| 3 | 32 | 314 | 0.0831 | 0.8156 | 8.31 | 81.56 |
| 4 | 36 | 350 | 0.0935 | 0.9091 | 9.35 | 90.91 |
| 5 | 3 | 353 | 0.0078 | 0.9169 | 0.78 | 91.69 |
| 6 | 5 | 358 | 0.0130 | 0.9299 | 1.30 | 92.99 |
| 7 | 1 | 359 | 0.0026 | 0.9325 | 0.26 | 93.25 |
| 8 | 10 | 369 | 0.0260 | 0.9585 | 2.60 | 95.85 |
| 10 | 6 | 375 | 0.0156 | 0.9741 | 1.56 | 97.41 |
| 11 | 2 | 377 | 0.0052 | 0.9793 | 0.52 | 97.93 |
| 12 | 4 | 381 | 0.0104 | 0.9897 | 1.04 | 98.97 |
| 14 | 2 | 383 | 0.0052 | 0.9949 | 0.52 | 99.49 |
| 16 | 1 | 384 | 0.0026 | 0.9975 | 0.26 | 99.75 |
| 18 | 1 | 385 | 0.0026 | 1.0000 | 0.26 | 100.00 |

Tabela 2 — Distribuição de frequências: Total de Conectores

* **Insight 1 — Predominância de estações de pequeno porte:** 73,25% das estações possuem no máximo 2 conectores. Isso indica que a rede de recarga é composta majoritariamente por pontos de pequeno porte. Para a plataforma de orquestração, essa concentração exige que o sistema seja otimizado para gerenciar um grande volume de estações simples, priorizando escalabilidade horizontal, monitoramento remoto eficiente via OCPP e distribuição geográfica inteligente dos pontos.
* **Insight 2 — Hubs estratégicos de alta capacidade:** Apenas 6,75% das estações possuem 8 ou mais conectores. Apesar de representarem uma parcela pequena, essas estações concentram alto potencial de receita e volume de sessões. São candidatas ideais para a implementação de cobrança dinâmica com regras de precificação por demanda, balanceamento de carga via protocolo OCPP e monitoramento avançado via MODBUS.

### 3.2 Potência Máxima em kW (Variável Quantitativa Contínua)
A variável Potencia_Maxima_kW representa a capacidade máxima de carregamento de cada estação. As classes foram definidas pela Regra de Sturges (k = 10 classes, amplitude h = 35 kW).

| Classe (kW) | Fi | Fac | fri | frac | fri% | frac% |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 \|-- 35 | 331 | 331 | 0.8597 | 0.8597 | 85.97 | 85.97 |
| 35 \|-- 70 | 2 | 333 | 0.0052 | 0.8649 | 0.52 | 86.49 |
| 70 \|-- 105 | 10 | 343 | 0.0260 | 0.8909 | 2.60 | 89.09 |
| 105 \|-- 140 | 0 | 343 | 0.0000 | 0.8909 | 0.00 | 89.09 |
| 140 \|-- 175 | 6 | 349 | 0.0156 | 0.9065 | 1.56 | 90.65 |
| 175 \|-- 210 | 9 | 358 | 0.0234 | 0.9299 | 2.34 | 92.99 |
| 210 \|-- 245 | 9 | 367 | 0.0234 | 0.9533 | 2.34 | 95.33 |
| 245 \|-- 280 | 7 | 374 | 0.0182 | 0.9715 | 1.82 | 97.15 |
| 280 \|-- 315 | 3 | 377 | 0.0078 | 0.9793 | 0.78 | 97.93 |
| 315 \|-- 350 | 8 | 385 | 0.0208 | 1.0000 | 2.08 | 100.00 |

Tabela 3 — Distribuição de frequências: Potência Máxima (kW)

* **Insight 1 — Mercado dominado por carregamento de baixa potência:** 86,49% das estações operam com potência inferior a 40 kW (Level 2). Esse cenário evidencia que a infraestrutura ainda é voltada para carregamento lento, típico de estacionamentos de longa permanência. Para a plataforma, isso reforça a necessidade de algoritmos de agendamento inteligente que maximizem a rotatividade e o aproveitamento desses carregadores.
* **Insight 2 — Alta potência como diferencial competitivo:** Aproximadamente 10,91% das estações oferecem potência acima de 100 kW (DC Fast Charging). Embora minoritárias, essas estações atendem um segmento de altíssimo valor: frotas comerciais e viagens de longa distância. A integração com protocolo MODBUS para monitoramento em tempo real da potência entregue é essencial neste segmento, viabilizando cobrança dinâmica baseada na energia efetivamente consumida.

---

## 4. Contribuições para a Tomada de Decisão
Os resultados obtidos nas análises dos itens anteriores fornecem subsídios concretos para a tomada de decisão no desenvolvimento da plataforma de orquestração de recarga comercial:

* **Estratégia de Precificação Dinâmica:** A concentração de 86% das estações na faixa de baixa potência, combinada com a predominância de estações com poucos conectores, sugere que o modelo de cobrança dinâmica deve contemplar dois perfis distintos: uma tarifa base competitiva para carregadores Level 2 (maioria do mercado) e uma tarifa premium variável por demanda para DC Fast Chargers, onde o protocolo MODBUS monitora a potência em tempo real.
* **Arquitetura do Sistema OCPP:** Com 73% das estações possuindo apenas 1-2 conectores, a arquitetura OCPP da plataforma deve ser leve e escalável, capaz de manter conexões persistentes com centenas de pontos simples simultaneamente, sem comprometer a latência de comunicação.
* **Priorização de Investimentos:** As estações de grande porte (8+ conectores, 6,75% do total) devem ser priorizadas para funcionalidades avançadas como balanceamento de carga inteligente, reserva de horário e integração com sistemas de pagamento corporativo, dado o maior potencial de receita por ponto.
* **Expansão da Rede:** A distribuição geográfica concentrada em Connecticut oferece um cenário piloto controlado. A análise de frequência das cidades permite identificar regiões com maior densidade de estações e planejar a expansão para áreas subatendidas.

---

## 5. Conclusão
A análise exploratória da base de dados de estações de recarga de veículos elétricos revelou padrões fundamentais para o desenho da plataforma de orquestração comercial. A predominância de estações de pequeno porte com carregadores de baixa potência indica um mercado em fase inicial de maturação, onde a diferenciação competitiva virá da capacidade de gerenciar eficientemente uma rede distribuída e fragmentada. A segmentação entre carregadores Level 2 e DC Fast é o eixo central da estratégia de cobrança dinâmica, e os protocolos OCPP e MODBUS são as tecnologias habilitadoras para transformar dados operacionais em inteligência de negócio.

---

## 6. Referências
* **Base de dados:** Electric Vehicle Charging Stations — Connecticut Open Data. Disponível em: data.ct.gov. Acesso em: maio de 2026.
* **Open Charge Point Protocol (OCPP) — Open Charge Alliance.** Disponível em: openchargealliance.org.
* **MODBUS Protocol Specification — Modbus Organization.** Disponível em: modbus.org.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("File README.md successfully created.")

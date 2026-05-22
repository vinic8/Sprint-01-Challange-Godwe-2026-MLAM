# ============================================================================
# CHALLENGE SPRINT 1 - Análise de Distribuição de Frequências
# Plataforma de Orquestração de Recarga Comercial de Veículos Elétricos
# ============================================================================
# Integrantes: [NOME COMPLETO - MATRÍCULA] (preencher antes da entrega)
# ============================================================================

import pandas as pd
import numpy as np

# Carregar a base de dados
df = pd.read_csv('base_estacoes_recarga_ev.csv')

print("=" * 80)
print("BASE DE DADOS - Estações de Recarga de Veículos Elétricos")
print(f"Total de observações: {len(df)}")
print(f"Total de variáveis: {len(df.columns)}")
print("=" * 80)

# ============================================================================
# CLASSIFICAÇÃO DAS VARIÁVEIS
# ============================================================================

print("\n>>> CLASSIFICAÇÃO DAS VARIÁVEIS <<<\n")
print("QUALITATIVAS NOMINAIS:")
print("  1. Tipo_Local        - Categoria do estabelecimento (Hotel, Concessionária, etc.)")
print("  2. Conector_Predominante - Tipo de conector principal (Level 1, Level 2, DC Fast)")

print("\nQUALITATIVAS ORDINAIS:")
print("  1. Porte_Estacao     - Tamanho da estação (Pequeno < Médio < Grande < Muito Grande)")
print("  2. Faixa_Disponibilidade - Nível de acesso (Horário Comercial < Variável < Integral Restrito < Integral)")

print("\nQUANTITATIVAS DISCRETAS:")
print("  1. Total_Conectores  - Número total de conectores na estação")
print("  2. Sessoes_Mensais   - Quantidade estimada de sessões de recarga por mês")

print("\nQUANTITATIVAS CONTÍNUAS:")
print("  1. Potencia_Maxima_kW - Potência máxima de carregamento em kilowatts")
print("  2. Tarifa_Media_kWh   - Tarifa média cobrada por kWh")


# ============================================================================
# ITEM 02a) TABELA DE FREQUÊNCIA - VARIÁVEL QUANTITATIVA DISCRETA
# Variável escolhida: Total_Conectores
# ============================================================================

print("\n" + "=" * 80)
print("02a) TABELA DE DISTRIBUIÇÃO DE FREQUÊNCIAS")
print("     Variável: Total_Conectores (Quantitativa Discreta)")
print("=" * 80)

var_discreta = df['Total_Conectores']

# Construir tabela de frequência
freq_abs = var_discreta.value_counts().sort_index()
freq_rel = (freq_abs / len(df)).round(4)
freq_abs_acum = freq_abs.cumsum()
freq_rel_acum = freq_rel.cumsum().round(4)
freq_perc = (freq_rel * 100).round(2)
freq_perc_acum = (freq_rel_acum * 100).round(2)

tabela_discreta = pd.DataFrame({
    'Xi': freq_abs.index,
    'Fi (Freq. Absoluta)': freq_abs.values,
    'Fac (Freq. Abs. Acumulada)': freq_abs_acum.values,
    'fri (Freq. Relativa)': freq_rel.values,
    'frac (Freq. Rel. Acumulada)': freq_rel_acum.values,
    'fri% (Percentual)': freq_perc.values,
    'frac% (Perc. Acumulado)': freq_perc_acum.values
})

print(tabela_discreta.to_string(index=False))
print(f"\nTotal de observações (ΣFi): {freq_abs.sum()}")

# INSIGHT 1 - Concentração em estações com poucos conectores
# A maioria das estações (aproximadamente 73%) possui no máximo 2 conectores,
# indicando que a rede é composta predominantemente por pontos de recarga de
# pequeno porte. Para a plataforma de orquestração, isso significa que o sistema
# deve ser otimizado para gerenciar muitas estações simples, priorizando
# escalabilidade horizontal e distribuição geográfica inteligente.

total_ate_2 = freq_abs[freq_abs.index <= 2].sum()
perc_ate_2 = round(total_ate_2 / len(df) * 100, 2)
print(f"\n# INSIGHT 1: {perc_ate_2}% das estações possuem até 2 conectores.")
print("#   Implicação: A plataforma deve priorizar escalabilidade horizontal,")
print("#   gerenciando muitas estações pequenas de forma eficiente.")

# INSIGHT 2 - Estações de grande porte como hubs estratégicos
# Estações com 8 ou mais conectores representam menos de 5% do total, porém
# concentram alto volume de sessões. Essas estações são candidatas ideais para
# a implementação de cobrança dinâmica (regras de preço por demanda),
# balanceamento de carga e integração com protocolos OCPP avançados.

total_8plus = freq_abs[freq_abs.index >= 8].sum()
perc_8plus = round(total_8plus / len(df) * 100, 2)
print(f"\n# INSIGHT 2: Apenas {perc_8plus}% das estações possuem 8+ conectores.")
print("#   Implicação: Essas grandes estações são hubs estratégicos onde a")
print("#   cobrança dinâmica e o balanceamento de carga OCPP geram mais valor.")


# ============================================================================
# ITEM 02b) TABELA DE FREQUÊNCIA - VARIÁVEL QUANTITATIVA CONTÍNUA
# Variável escolhida: Potencia_Maxima_kW
# ============================================================================

print("\n" + "=" * 80)
print("02b) TABELA DE DISTRIBUIÇÃO DE FREQUÊNCIAS")
print("     Variável: Potencia_Maxima_kW (Quantitativa Contínua)")
print("=" * 80)

var_continua = df['Potencia_Maxima_kW']

# Estatísticas descritivas
print(f"\nEstatísticas descritivas:")
print(f"  Mínimo:  {var_continua.min():.2f} kW")
print(f"  Máximo:  {var_continua.max():.2f} kW")
print(f"  Média:   {var_continua.mean():.2f} kW")
print(f"  Mediana: {var_continua.median():.2f} kW")
print(f"  Desvio:  {var_continua.std():.2f} kW")

# Regra de Sturges: k = 1 + 3.322 * log10(n)
n = len(var_continua)
k = int(np.ceil(1 + 3.322 * np.log10(n)))
amplitude_total = var_continua.max() - var_continua.min()
h = np.ceil(amplitude_total / k)

print(f"\n  n = {n} | k (Sturges) = {k} classes | AT = {amplitude_total:.2f} | h ≈ {h:.0f} kW")

# Definir limites das classes
bins = np.arange(0, var_continua.max() + h, h)
labels = [f"{bins[i]:.0f} ├── {bins[i+1]:.0f}" for i in range(len(bins)-1)]

# Classificar
classes = pd.cut(var_continua, bins=bins, right=False, labels=labels[:len(bins)-1])

freq_abs_c = classes.value_counts().sort_index()
freq_rel_c = (freq_abs_c / n).round(4)
freq_abs_acum_c = freq_abs_c.cumsum()
freq_rel_acum_c = freq_rel_c.cumsum().round(4)
freq_perc_c = (freq_rel_c * 100).round(2)
freq_perc_acum_c = (freq_rel_acum_c * 100).round(2)

tabela_continua = pd.DataFrame({
    'Classe (kW)': freq_abs_c.index,
    'Fi': freq_abs_c.values,
    'Fac': freq_abs_acum_c.values,
    'fri': freq_rel_c.values,
    'frac': freq_rel_acum_c.values,
    'fri%': freq_perc_c.values,
    'frac%': freq_perc_acum_c.values
})

print(f"\n{tabela_continua.to_string(index=False)}")
print(f"\nTotal de observações (ΣFi): {freq_abs_c.sum()}")

# INSIGHT 1 - Predominância de carregadores de baixa/média potência
# A grande maioria das estações opera com potência abaixo de 40 kW (Level 2),
# o que indica um mercado ainda focado em carregamento lento/residencial.
# Para a plataforma, é essencial implementar algoritmos de agendamento
# inteligente que otimizem o tempo de ocupação desses carregadores mais lentos,
# aumentando a rotatividade e receita por ponto.

total_baixa = freq_abs_c[freq_abs_c.index.isin([l for l in labels if float(l.split('├──')[0]) < 40])].sum()
perc_baixa = round(total_baixa / n * 100, 2)
print(f"\n# INSIGHT 1: {perc_baixa}% das estações operam abaixo de 40 kW.")
print("#   Implicação: Algoritmos de agendamento inteligente são essenciais para")
print("#   otimizar a ocupação de carregadores lentos e aumentar a rotatividade.")

# INSIGHT 2 - Segmento de alta potência como diferencial competitivo
# Estações com potência acima de 100 kW (DC Fast Charging) formam um segmento
# menor, mas de altíssimo valor para fleets comerciais e viagens de longa
# distância. A integração com protocolo MODBUS para monitoramento em tempo real
# da potência entregue é crítica neste segmento, permitindo cobrança dinâmica
# baseada na potência efetivamente consumida.

total_alta = freq_abs_c[freq_abs_c.index.isin([l for l in labels if float(l.split('├──')[0]) >= 100])].sum()
perc_alta = round(total_alta / n * 100, 2)
print(f"\n# INSIGHT 2: {perc_alta}% das estações operam acima de 100 kW (DC Fast).")
print("#   Implicação: Segmento premium ideal para cobrança dinâmica via MODBUS,")
print("#   com precificação baseada na potência efetivamente consumida.")

print("\n" + "=" * 80)
print("FIM DA ANÁLISE")
print("=" * 80)

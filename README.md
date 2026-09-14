# 🛠️ Sistema de Análise e Precificação de Ferramentais (Moldes & Estampos)

Projeto de Engenharia de Dados e Análise Financeira em Python desenvolvido para a estimativa automatizada de custos de fabricação, usinagem e precificação de ferramentas industriais automotivas (Moldes de Injeção Plástica e Estampos de Corte/Dobra/Repuxo).

---

## 📌 Visão Geral do Projeto

Na indústria de manufatura e no setor automotivo, a orçamentação precisa de ferramentais protótipos e de série é fundamental para manter a margem operacional e viabilizar novos produtos.

Este projeto resolve o problema de precificação manual ao implementar um **pipeline de cálculo automatizado** que considera:
* **Cubagem e Peso de Aço:** Cálculo automático via densidade volumétrica ($\approx 7,85 \text{ g/cm}^3$).
* **Capacidade Operacional:** Horas/máquina e horas/homem para CNC, Eletroerosão (EDM/WEDM), Ajuste e Try-out.
* **Custos Específicos do Processo:**
  * *Injeção:* Insumos como sistemas de câmara quente, gavetas e pinos.
  * *Estamparia:* Tratamento térmico (têmpera/revenimento de Aço D2/VND) e componentes padronizados (colunas/molas prato).
* **Precificação Final:** Aplicação de margens operacionais, contingência e impostos sobre o Custo Direto de Fabricação.

---

## 📦 Módulos do Sistema

1. **`orcamento_molde.py`**:
   * Focado em **Moldes de Injeção Plástica**.
   * Computa custos de aço P20/1045, sistemas de câmara quente, gavetas mecânicas, extração e try-out em injetora.

2. **`orcamento_estampo.py`**:
   * Focado em **Estampos de Corte, Dobra e Repuxo**.
   * Computa custos de aço VND/D2, tratamento térmico (têmpera/revenimento), eletroerosão a fio (WEDM) e try-out em prensa hidráulica/excêntrica.

---

## 📐 Fórmulas Utilizadas

### 1. Estimativa de Peso Bruto ($kg$)
$$\text{Volume } (cm^3) = \frac{\text{Comprimento } (mm)}{10} \times \frac{\text{Largura } (mm)}{10} \times \frac{\text{Altura } (mm)}{10}$$

$$\text{Peso } (kg) = \frac{\text{Volume } (cm^3) \times 7,85}{1000}$$

### 2. Custo Total de Mão de Obra e Usinagem
$$\text{Custo M.O.} = \sum (\text{Horas Estimadas}_i \times \text{Taxa Hora}_i)$$

### 3. Precificação Final
$$\text{Valor Final} = (\text{Custo M.O.} + \text{Custo Materiais}) \times \left(1 + \frac{\text{Margem \%}}{100}\right)$$

---

## ⚙️ Como Executar o Projeto

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/analise-custo-ferramental.git](https://github.com/SEU_USUARIO/analise-custo-ferramental.git)

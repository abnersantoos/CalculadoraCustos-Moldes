# 🚪 Calculadora de Custo e Orçamento para Moldes de Injeção Plástica

Projeto em Python desenvolvido para automatizar a estimativa de custos de fabricação, usinagem e precificação de moldes de injeção plástica para o setor automotivo e industrial.

---

## 📌 Visão Geral do Projeto

A orçamentação de moldes de injeção exige precisão no cálculo de cubagem de aço, tempo de usinagem e custos de insumos complexos (como sistemas de câmara quente e acionamentos mecânicos).

Este módulo calcula automaticamente:
* **Peso Bruto de Aço:** Baseado nas dimensões ($mm$) e densidade do aço ($\approx 7,85 \text{ g/cm}^3$), considerando a combinação de aço P20 (cavidades) e Aço 1045 (porta-molde).
* **Carga Horária & Taxa/Hora:** Mão de obra e máquina para Projeto CAD/CAM, Usinagem CNC, Eletroerosão (EDM), Montagem/Ajuste e Try-out em Injetora.
* **Componentes Específicos:** Inclusão de custos de câmara quente, pinos extratores, buchas e gavetas mecânicas.
* **Precificação Final:** Aplicação de margem de segurança e tributos sobre o custo direto.

---

## 📐 Fórmulas Utilizadas

$$\text{Volume } (cm^3) = \frac{\text{Comprimento}}{10} \times \frac{\text{Largura}}{10} \times \frac{\text{Altura}}{10}$$

$$\text{Peso } (kg) = \frac{\text{Volume } (cm^3) \times 7,85}{1000}$$

$$\text{Valor Final} = (\text{Custo M.O.} + \text{Custo Insumos}) \times \left(1 + \frac{\text{Margem \%}}{100}\right)$$

---

## ⚙️ Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone o repositório e navegue até a pasta:
   ```bash
   git clone [https://github.com/SEU_USUARIO/orcameto-ferramentais.git](https://github.com/SEU_USUARIO/orcameto-ferramentais.git)
   cd orcameto-ferramentais

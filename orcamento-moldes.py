from dataclasses import dataclass

@dataclass
class ParametrosFerramental:
    # Dimensões do bloco em mm
    comprimento: float  # mm
    largura: float      # mm
    altura: float       # mm
    
    # Insumos fixos / componentes
    custo_camara_quente: float
    custo_padronizados: float  # pinos, guias, molas
    preco_kg_aco: float = 25.0  # R$/kg média ponderada P20 + 1045
    
    # Horas estimadas
    horas_cad_cam: float = 60.0
    horas_cnc: float = 110.0
    horas_convencional: float = 50.0
    horas_edm: float = 30.0
    horas_montagem: float = 70.0
    horas_tryout: float = 16.0
    
    # Taxas Horárias (R$/h)
    taxa_cad_cam: float = 120.0
    taxa_cnc: float = 160.0
    taxa_convencional: float = 90.0
    taxa_edm: float = 130.0
    taxa_montagem: float = 110.0
    taxa_tryout: float = 250.0
    
    # Margem sobre o custo de fabricação (%)
    margem_impostos: float = 30.0


class CalculadoraFerramental:
    DENSIDADE_ACO_G_CM3 = 7.85  # g/cm³

    def __init__(self, params: ParametrosFerramental):
        self.p = params

    def calcular_peso(self) -> float:
        # Volume em cm³
        volume_cm3 = (self.p.comprimento / 10) * (self.p.largura / 10) * (self.p.altura / 10)
        # Peso em kg
        peso_kg = (volume_cm3 * self.DENSIDADE_ACO_G_CM3) / 1000
        return peso_kg

    def calcular_custos_mao_de_obra(self) -> dict:
        mo = {
            "CAD/CAM": self.p.horas_cad_cam * self.p.taxa_cad_cam,
            "Usinagem CNC": self.p.horas_cnc * self.p.taxa_cnc,
            "Usinagem Convencional": self.p.horas_convencional * self.p.taxa_convencional,
            "Eletroerosão (EDM)": self.p.horas_edm * self.p.taxa_edm,
            "Bancada / Montagem": self.p.horas_montagem * self.p.taxa_montagem,
            "Try-out": self.p.horas_tryout * self.p.taxa_tryout,
        }
        mo["Total M.O."] = sum(mo.values())
        return mo

    def gerar_relatorio(self):
        peso = self.calcular_peso()
        custo_aco = peso * self.p.preco_kg_aco
        custo_materiais = custo_aco + self.p.custo_camara_quente + self.p.custo_padronizados
        
        custos_mo = self.calcular_custos_mao_de_obra()
        custo_mo_total = custos_mo["Total M.O."]
        
        custo_fabricacao = custo_mo_total + custo_materiais
        valor_final = custo_fabricacao * (1 + (self.p.margem_impostos / 100))
        
        horas_totais = (self.p.horas_cad_cam + self.p.horas_cnc + self.p.horas_convencional + 
                        self.p.horas_edm + self.p.horas_montagem + self.p.horas_tryout)

        print("=" * 65)
        print("          SIMULAÇÃO DE ORÇAMENTO DE FERRAMENTAL")
        print("=" * 65)
        print(f"Dimensões do Molde: {self.p.comprimento:.0f} x {self.p.largura:.0f} x {self.p.altura:.0f} mm")
        print(f"Peso Estimado de Aço: {peso:,.2f} kg")
        print(f"Horas Totais do Projeto: {horas_totais:.0f} h")
        print("-" * 65)
        print("DETALHAMENTO DE MÃO DE OBRA E MÁQUINA:")
        for etapa, custo in custos_mo.items():
            if etapa != "Total M.O.":
                print(f"  - {etapa:<25}: R$ {custo:>10,.2f}")
        print(f"  --> SUB-TOTAL M.O.:         R$ {custo_mo_total:>10,.2f}")
        print("-" * 65)
        print("DETALHAMENTO DE MATERIAIS E COMPONENTES:")
        print(f"  - Bloco de Aço (P20/1045):  R$ {custo_aco:>10,.2f}")
        print(f"  - Câmara Quente:            R$ {self.p.custo_camara_quente:>10,.2f}")
        print(f"  - Padronizados/Acessórios: R$ {self.p.custo_padronizados:>10,.2f}")
        print(f"  --> SUB-TOTAL MATERIAIS:    R$ {custo_materiais:>10,.2f}")
        print("-" * 65)
        print(f"CUSTO DIRETO DE FABRICAÇÃO:    R$ {custo_fabricacao:>10,.2f}")
        print(f"VALOR FINAL COM MARGEM ({self.p.margem_impostos:.0f}%): R$ {valor_final:>10,.2f}")
        print("=" * 65)


# ==============================================================================
# EXEMPLO DE USO PARA NOVAS AQUISIÇÕES
# ==============================================================================
if __name__ == "__main__":
    # Exemplo: Novo molde menor (400x400x300 mm) sem câmara quente
    novo_projeto = ParametrosFerramental(
        comprimento=400,
        largura=400,
        altura=300,
        custo_camara_quente=0.0,      # Injeção convencional
        custo_padronizados=3500.0,
        horas_cnc=70.0,              # Menos tempo de usinagem
        horas_montagem=40.0
    )
    
    calculadora = CalculadoraFerramental(novo_projeto)
    calculadora.gerar_relatorio()

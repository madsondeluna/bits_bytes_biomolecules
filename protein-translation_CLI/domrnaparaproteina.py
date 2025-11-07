#!/usr/bin/env python3
"""
Animação Educacional sobre Tradução de Proteínas
Uma ferramenta interativa CLI para visualizar e aprender sobre tradução de proteínas
"""

import time
import sys
import os

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def digitar_texto(texto, atraso=0.03):
    """Imprime texto com efeito de animação de digitação"""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

def imprimir_cabecalho(titulo):
    """Imprime um cabeçalho formatado"""
    limpar_tela()
    largura = 80
    print("=" * largura)
    print(titulo.center(largura))
    print("=" * largura)
    print()

def animar_pontos(duracao=2):
    """Anima pontos de carregamento"""
    for _ in range(duracao):
        for pontos in ['   ', '.  ', '.. ', '...']:
            sys.stdout.write(f'\r{pontos}')
            sys.stdout.flush()
            time.sleep(0.25)
    print('\r   ')

def desenhar_molecula(nome, estrutura):
    """Desenha arte ASCII para moléculas"""
    print(f"\n{nome}:")
    print(estrutura)
    print()

def introducao():
    """Introdução à tradução de proteínas"""
    imprimir_cabecalho("TRADUÇÃO DE PROTEÍNAS: Uma Jornada Passo a Passo")
    
    digitar_texto("Bem-vindo à Ferramenta Educacional de Tradução de Proteínas!")
    time.sleep(0.5)
    digitar_texto("\nEste programa interativo irá guiá-lo através do fascinante")
    digitar_texto("processo de como as células convertem informação genética em proteínas.")
    time.sleep(1)
    
    digitar_texto("\nPressione ENTER para começar a jornada...")
    input()

def dogma_central():
    """Explica o dogma central"""
    imprimir_cabecalho("O DOGMA CENTRAL DA BIOLOGIA MOLECULAR")
    
    digitar_texto("Antes de mergulhar na tradução, vamos entender o panorama geral:")
    time.sleep(1)
    
    print("\n")
    print("     ┌─────────────┐")
    print("     │     DNA     │")
    print("     └──────┬──────┘")
    print("            │ Replicação")
    print("            ↓")
    print("     ┌──────────────┐")
    print("     │     DNA      │")
    print("     └──────┬───────┘")
    print("            │ Transcrição")
    print("            ↓")
    print("     ┌──────────────┐")
    print("     │     RNA      │ (mRNA)")
    print("     └──────┬───────┘")
    print("            │ TRADUÇÃO [***]")
    print("            ↓")
    print("     ┌──────────────┐")
    print("     │   PROTEÍNA   │")
    print("     └──────────────┘")
    print()
    
    time.sleep(2)
    digitar_texto("\n[***] A TRADUÇÃO é onde a mágica acontece!")
    digitar_texto("Ela converte a mensagem do mRNA em uma proteína funcional.")
    
    digitar_texto("\nPressione ENTER para continuar...")
    input()

def maquinaria_traducao():
    """Mostra os componentes da maquinaria de tradução"""
    imprimir_cabecalho("A MAQUINARIA DE TRADUÇÃO")
    
    digitar_texto("A tradução requer vários atores moleculares chave:")
    time.sleep(1)
    
    componentes = [
        ("1. mRNA", "O mensageiro carregando instruções genéticas"),
        ("2. Ribossomos", "A fábrica de síntese proteica (subunidades 40S + 60S)"),
        ("3. tRNA", "RNA transportador - o caminhão de entrega de aminoácidos"),
        ("4. Aminoácidos", "Os blocos de construção das proteínas"),
        ("5. Fatores de iniciação", "eIF4E, eIF4G, eIF4A, PABP"),
        ("6. Fatores de elongação", "eEF1A, eEF1B, eEF2"),
        ("7. Energia", "ATP e GTP - o combustível celular")
    ]
    
    for componente, descricao in componentes:
        print(f"\n  {componente}")
        digitar_texto(f"    → {descricao}", atraso=0.02)
        time.sleep(0.5)
    
    print("\n")
    desenhar_molecula("Estrutura do Ribossomo", """
        ┌─────────────────┐
        │ Subunidade 60S  │  ← Subunidade maior
        │    (rRNA +      │
        │   proteínas)    │
        ├─────────────────┤
        │                 │
        │      mRNA  →    │  ← mRNA passando através
        │                 │
        ├─────────────────┤
        │ Subunidade 40S  │  ← Subunidade menor
        │    (rRNA +      │
        │   proteínas)    │
        └─────────────────┘
    """)
    
    digitar_texto("Pressione ENTER para ver a tradução em ação...")
    input()

def fase_iniciacao():
    """Demonstra a fase de iniciação"""
    imprimir_cabecalho("FASE 1: INICIAÇÃO")
    
    digitar_texto("A iniciação é onde a tradução começa!")
    digitar_texto("Esta fase prepara o ribossomo para começar a ler o mRNA.")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\nPasso 1: Reconhecimento do Cap 5'", atraso=0.02)
    animar_pontos(1)
    
    print("""
    Cap 5' (m7G)
        ↓
    ╔═══╗
    ║ • ║ ← eIF4E se liga aqui
    ╚═══╝
    ═════════════════════> mRNA
    """)
    digitar_texto("[✓] eIF4E reconhece e se liga ao cap 5' do mRNA")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\nPasso 2: Recrutamento de fatores de iniciação", atraso=0.02)
    animar_pontos(1)
    
    print("""
         eIF4G  eIF4A  PABP
           ↓      ↓      ↓
    ╔═══╗━━━━━━━━━━━━━━━╗
    ║ • ║                ║ Cauda Poli-A
    ╚═══╝                ╚═══════════
    ═════════════════════>
    """)
    digitar_texto("[✓] eIF4G, eIF4A e PABP se juntam ao complexo")
    digitar_texto("[✓] mRNA forma uma estrutura circular para tradução eficiente")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\nPasso 3: Recrutamento da subunidade 40S do ribossomo", atraso=0.02)
    animar_pontos(1)
    
    print("""
              ┌─────────┐
              │   40S   │
              └────┬────┘
                   ↓
    ╔═══╗━━━━━━━━━━━━━━━╗
    ║ • ║═══════════════>║
    ╚═══╝                ╚═══════════
         5'  ------>  AUG (códon de início)
    """)
    digitar_texto("[✓] A subunidade 40S é recrutada para o mRNA")
    digitar_texto("[✓] Ela escaneia ao longo do mRNA procurando o códon de início (AUG)")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\nPasso 4: Reconhecimento do códon de início e união da 60S", atraso=0.02)
    animar_pontos(1)
    
    print("""
         ┌─────────────┐
         │   60S       │
         ╞═════════════╡
         │  A  P  E    │ ← Três sítios de ligação
         │  │  │  │    │
    5' ══╡══AUG════════│═══> 3'
         │     │       │
         │   Met-tRNA  │ ← tRNA iniciador
         └─────────────┘
         │   40S       │
         └─────────────┘
    """)
    digitar_texto("[✓] Códon de início AUG encontrado!")
    digitar_texto("[✓] Met-tRNA (carregando Metionina) se liga ao AUG")
    digitar_texto("[✓] Subunidade 60S se junta para formar o ribossomo 80S completo")
    digitar_texto("[✓] A tradução está pronta para começar!")
    time.sleep(2)
    
    digitar_texto("\n[ALVO] INICIAÇÃO COMPLETA! Pronto para construir a cadeia proteica.")
    digitar_texto("\nPressione ENTER para continuar para a elongação...")
    input()

def fase_elongacao():
    """Demonstra a fase de elongação"""
    imprimir_cabecalho("FASE 2: ELONGAÇÃO")
    
    digitar_texto("A elongação é onde a cadeia proteica cresce!")
    digitar_texto("Este ciclo se repete para cada aminoácido adicionado à proteína.")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\nLembrete: O Código Genético", atraso=0.02)
    print("""
    ╔═══════════════════════════════════════╗
    ║  CÓDON → AMINOÁCIDO                   ║
    ║  AUG → Metionina (INÍCIO)             ║
    ║  UUU → Fenilalanina                   ║
    ║  GCU → Alanina                        ║
    ║  UAA, UAG, UGA → PARADA               ║
    ╚═══════════════════════════════════════╝
    """)
    time.sleep(1)
    
    aminoacidos = ["Met", "Phe", "Ala", "Gly"]
    codons = ["AUG", "UUU", "GCU", "GGU"]
    
    for i, (aa, codon) in enumerate(zip(aminoacidos, codons)):
        print("\n" + "═" * 80)
        digitar_texto(f"\n[CICLO] CICLO DE ELONGAÇÃO {i+1}: Adicionando {aa}", atraso=0.02)
        animar_pontos(1)
        
        print("\n" + "─" * 80)
        digitar_texto("Passo 1: Aminoacil-tRNA entra no sítio A", atraso=0.02)
        time.sleep(0.5)
        
        print(f"""
              ┌─────────────────┐
              │ Subunidade 60S  │
              ├─────────────────┤
              │   E   P   A     │ ← Sítios de ligação
              │       │   │     │
        5' ═══│═══{codons[i-1] if i > 0 else '───'}═{codon}═══│═══> 3'
              │       │   │     │
              │       {aminoacidos[i-1] if i > 0 else '   '}  {aa}    │ ← Aminoácido entrando
              │       │   │     │
              └───────┴───┴─────┘
                     tRNA tRNA
        """)
        digitar_texto(f"[✓] {aa}-tRNA reconhece o códon {codon}")
        digitar_texto(f"[✓] {aa}-tRNA se liga ao sítio A (Aminoacil)")
        time.sleep(1)
        
        print("\n" + "─" * 80)
        digitar_texto("Passo 2: Formação da ligação peptídica", atraso=0.02)
        time.sleep(0.5)
        
        print("""
              ┌─────────────────┐
              │   Peptidil      │
              │ transferase [*] │ ← Centro catalítico
              ├─────────────────┤
              │   E   P ~ A     │
              │       │ ╲ │     │
              │       │  ╲│     │ ← Ligação peptídica formando
              │     Peptídeo    │
              └─────────────────┘
        """)
        digitar_texto("[✓] Peptidil transferase catalisa a formação da ligação peptídica")
        digitar_texto(f"[✓] Cadeia peptídica crescente agora ligada a {aa}")
        time.sleep(1)
        
        print("\n" + "─" * 80)
        digitar_texto("Passo 3: Translocação do ribossomo", atraso=0.02)
        time.sleep(0.5)
        
        print(f"""
              ┌─────────────────┐
              │ Subunidade 60S  │
              ├─────────────────┤
              │   E   P   A     │
              │   │   │         │
        5' ═══│═{codon}═══────═══│═══> 3'
              │   │   │         │    ↓ Ribossomo se move
              │     Peptídeo    │    ↓ 3 nucleotídeos
              └─────────────────┘
                       ⬇ ⬇ ⬇
        """)
        digitar_texto("[✓] eEF2 (fator de elongação 2) usa energia GTP")
        digitar_texto("[✓] Ribossomo move 3 nucleotídeos para frente (um códon)")
        digitar_texto("[✓] tRNAs mudam: sítios A→P→E")
        digitar_texto("[✓] tRNA vazio sai pelo sítio E")
        time.sleep(1)
        
        print(f"\n[***] Aminoácido #{i+1} adicionado! Peptídeo atual: ", end="")
        print("-".join(aminoacidos[:i+1]))
        time.sleep(1)
    
    print("\n" + "═" * 80)
    digitar_texto("\n[REPETIR] Este ciclo se repete centenas ou milhares de vezes!")
    digitar_texto("Cada ciclo adiciona um aminoácido à cadeia proteica crescente.")
    digitar_texto(f"\n[RESULTADO] Peptídeo final até agora: {'-'.join(aminoacidos)}")
    
    digitar_texto("\nPressione ENTER para continuar para a terminação...")
    input()

def fase_terminacao():
    """Demonstra a fase de terminação"""
    imprimir_cabecalho("FASE 3: TERMINAÇÃO")
    
    digitar_texto("A terminação encerra a tradução quando um códon STOP é alcançado.")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\nPasso 1: Reconhecimento do códon de parada", atraso=0.02)
    animar_pontos(1)
    
    print("""
              ┌─────────────────┐
              │ Subunidade 60S  │
              ├─────────────────┤
              │   E   P   A     │
              │       │   │     │
        5' ═══│═══GGU═UAA═══════│═══> 3'
              │       │   [!]   │
              │  Peptídeo PARE! │
              │       │         │
              └───────┴─────────┘
                     tRNA   
    """)
    digitar_texto("[✓] Códon de parada (UAA, UAG ou UGA) entra no sítio A")
    digitar_texto("[✓] Nenhum tRNA reconhece códons de parada!")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\nPasso 2: Ligação do fator de liberação", atraso=0.02)
    animar_pontos(1)
    
    print("""
              ┌─────────────────┐
              │ Subunidade 60S  │
              ├─────────────────┤
              │   E   P   A     │
              │       │   │     │
        5' ═══│═══GGU═UAA═══════│═══> 3'
              │       │  eRF1   │ ← Fator de liberação
              │  Peptídeo│      │
              │       │ eRF3•GTP│
              └───────┴─────────┘
    """)
    digitar_texto("[✓] Fatores de liberação eRF1 e eRF3•GTP reconhecem o códon de parada")
    digitar_texto("[✓] eRF1 imita a forma de uma molécula de tRNA")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\nPasso 3: Liberação do peptídeo", atraso=0.02)
    animar_pontos(1)
    
    print("""
                  ╔════════════╗
                  ║  PROTEÍNA! ║ ← Liberada!
                  ╚════════════╝
                       ⬆
              ┌─────────────────┐
              │   Peptidil      │
              │  transferase    │
              │   (hidrolisa)   │
              ├─────────────────┤
              │   E   P   A     │
              │       ╳   │     │
        5' ═══│═══GGU═UAA═══════│═══> 3'
              └─────────────────┘
    """)
    digitar_texto("[✓] Peptidil transferase hidrolisa a ligação peptídeo-tRNA")
    digitar_texto("[✓] Proteína completa é liberada para a célula!")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\nPasso 4: Desmontagem do ribossomo", atraso=0.02)
    animar_pontos(1)
    
    print("""
         ┌─────────────┐
         │   60S       │ ───→ Liberada
         └─────────────┘
    
    
         ┌─────────────┐
         │   40S       │ ───→ Liberada
         └─────────────┘
    
        5' ═══════════════════> 3'
              mRNA (pode ser reciclado)
    """)
    digitar_texto("[✓] Subunidades do ribossomo (60S e 40S) se dissociam")
    digitar_texto("[✓] mRNA é liberado (pode ser traduzido novamente)")
    digitar_texto("[✓] tRNA é liberado (pode pegar novos aminoácidos)")
    time.sleep(1)
    
    print("\n" + "═" * 80)
    digitar_texto("\n[SUCESSO] TRADUÇÃO COMPLETA!")
    digitar_texto("Uma proteína funcional foi sintetizada!")
    
    digitar_texto("\nPressione ENTER para ver o resumo...")
    input()

def dobramento_proteico():
    """Mostra o dobramento de proteínas"""
    imprimir_cabecalho("DOBRAMENTO E MATURAÇÃO PROTEICA")
    
    digitar_texto("Após a tradução, a proteína deve se dobrar em sua forma 3D funcional.")
    time.sleep(1)
    
    print("\n")
    print("     Cadeia Proteica Linear")
    print("     ═════════════════════")
    print("     Met-Phe-Ala-Gly-...")
    print()
    animar_pontos(2)
    print("            ↓ Dobramento")
    animar_pontos(2)
    print()
    print("       Proteína Dobrada")
    print("          ╔═══╗")
    print("       ╔══╝   ╚══╗")
    print("       ║         ║")
    print("       ║  SÍTIO  ║  ← Estrutura 3D funcional")
    print("       ║  ATIVO  ║")
    print("       ╚═════════╝")
    print()
    
    digitar_texto("\n[✓] Proteínas se dobram com base na sequência de aminoácidos")
    digitar_texto("[✓] Proteínas chaperonas ajudam no dobramento adequado")
    digitar_texto("[✓] Modificações pós-traducionais podem ocorrer:")
    print("    • Fosforilação")
    print("    • Metilação")
    print("    • Glicosilação")
    print("    • Ubiquitinação")
    
    time.sleep(2)
    digitar_texto("\nPressione ENTER para continuar...")
    input()

def resumo():
    """Fornece um resumo do processo de tradução"""
    imprimir_cabecalho("RESUMO DA TRADUÇÃO")
    
    digitar_texto("Vamos revisar o processo completo de tradução:")
    time.sleep(1)
    
    print("\n")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                    TRADUÇÃO DE PROTEÍNAS                       ║")
    print("╠════════════════════════════════════════════════════════════════╣")
    print("║                                                                ║")
    print("║  [1] INICIAÇÃO                                                 ║")
    print("║      • Reconhecimento do cap 5' por eIF4E                     ║")
    print("║      • Recrutamento do ribossomo (subunidade 40S)             ║")
    print("║      • Reconhecimento do códon de início AUG                  ║")
    print("║      • União da subunidade 60S → ribossomo 80S                ║")
    print("║                                                                ║")
    print("║  [2] ELONGAÇÃO (CICLO REPETITIVO)                             ║")
    print("║      • Aminoacil-tRNA entra no sítio A                        ║")
    print("║      • Formação da ligação peptídica (peptidil transferase)   ║")
    print("║      • Translocação (ribossomo move 3 nucleotídeos)           ║")
    print("║      • Movimento do tRNA: sítios A → P → E                    ║")
    print("║                                                                ║")
    print("║  [3] TERMINAÇÃO                                                ║")
    print("║      • Reconhecimento do códon de parada (UAA/UAG/UGA)        ║")
    print("║      • Ligação dos fatores de liberação (eRF1/eRF3•GTP)       ║")
    print("║      • Liberação da cadeia peptídica                          ║")
    print("║      • Desmontagem do ribossomo                               ║")
    print("║                                                                ║")
    print("║  [4] PÓS-TRADUÇÃO                                              ║")
    print("║      • Dobramento proteico (assistido por chaperonas)         ║")
    print("║      • Modificações pós-traducionais                          ║")
    print("║      • Direcionamento para localização celular final          ║")
    print("║                                                                ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print()
    
    time.sleep(2)
    
    digitar_texto("\n[TEMPO] VELOCIDADE: Tradução ocorre a ~5-10 aminoácidos por segundo!")
    digitar_texto("[TAMANHO] COMPRIMENTO: Proteína média tem ~300-400 aminoácidos")
    digitar_texto("[ENERGIA] ENERGIA: ~4 equivalentes de ATP por aminoácido adicionado")
    
    digitar_texto("\nPressione ENTER para continuar...")
    input()

def relevancia_clinica():
    """Mostra a relevância clínica"""
    imprimir_cabecalho("RELEVÂNCIA CLÍNICA")
    
    digitar_texto("A desregulação da tradução está envolvida em muitas doenças:")
    time.sleep(1)
    
    doencas = [
        ("[NEURO] DOENÇAS NEURODEGENERATIVAS", [
            "• Alzheimer: agregação de β-amiloide, fosforilação de eIF2α",
            "• Parkinson: agregação de α-sinucleína, mutações em eIF4G1",
            "• ELA: ativação de UPR, inibição da tradução mediada por PERK",
            "• Huntington: expansão CAG, agregação de poliglutamina"
        ]),
        ("[CÂNCER] CÂNCER", [
            "• Superexpressão de eIF4E, eIF4A, eEF2",
            "• Desregulação da via mTOR",
            "• Alteração na expressão de proteínas ribossomais",
            "• Mudanças nas modificações de tRNA"
        ]),
        ("[VÍRUS] DOENÇAS INFECCIOSAS", [
            "• Vírus sequestram a maquinaria de tradução do hospedeiro",
            "• Proteínas virais competem pela ligação a eIF4E",
            "• Exemplo: Potyvirus usa VPg em vez do cap 5'"
        ]),
        ("[CARDIO] DOENÇAS CARDIOVASCULARES", [
            "• Cardiomiopatia hipertrófica",
            "• Aumento da síntese proteica em cardiomiócitos",
            "• Proteína TIP30 regula a tradução via eEF1A"
        ])
    ]
    
    for tipo_doenca, detalhes in doencas:
        print("\n" + "─" * 80)
        digitar_texto(f"\n{tipo_doenca}", atraso=0.02)
        for detalhe in detalhes:
            print(f"  {detalhe}")
            time.sleep(0.3)
        time.sleep(0.5)
    
    print("\n" + "═" * 80)
    digitar_texto("\n[TERAPIA] ESTRATÉGIAS TERAPÊUTICAS:", atraso=0.02)
    print("\n  • Inibidores de mTOR: Rapamicina, Everolimus, Temsirolimus")
    print("  • Inibidores de eIF4E: Ribavirina, LY2275796")
    print("  • Inibidores de eIF4A: Silvestrol, Rocaglatos")
    print("  • Moduladores de eIF2α: Salubrinal (neuroproteção)")
    
    time.sleep(2)
    digitar_texto("\nPressione ENTER para continuar...")
    input()

def tecnicas_pesquisa():
    """Mostra técnicas de pesquisa"""
    imprimir_cabecalho("TÉCNICAS DE PESQUISA")
    
    digitar_texto("Cientistas usam técnicas avançadas para estudar a tradução:")
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\n[1] PERFILAMENTO RIBOSSÔMICO (Ribo-seq)", atraso=0.02)
    print("""
    Inibidores    Digestão      Isolar        Sequenciar
    de tradução → com RNase  → pegadas  →  e analisar
                              (~28 pb)
    
    Resultado: Mapa genômico das posições dos ribossomos
    """)
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\n[2] PROTEÔMICA POR ESPECTROMETRIA DE MASSA", atraso=0.02)
    print("""
    Amostra     Digerir em    Ionizar e      Detectar e
    proteica → peptídeos   → separar    →  identificar
    
    Métodos: SILAC, iTRAQ, TMT
    Resultado: Dados quantitativos de expressão proteica
    """)
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\n[3] ABORDAGENS DE CÉLULA ÚNICA", atraso=0.02)
    print("""
    Células    Isolar        Perfilar       Analisar
    únicas  → RNA/proteína → células    → heterogeneidade
                            individuais
    
    Técnicas: scRNA-seq, scRibo-seq, proteômica nascente
    """)
    time.sleep(1)
    
    print("\n" + "─" * 80)
    digitar_texto("\n[4] PERFILAMENTO DE POLISSOMOS", atraso=0.02)
    print("""
    Lisado     Separar por    Fracionar     Analisar
    celular → sedimentação → polissomos → atividade de
              (gradiente                   tradução
              de sacarose)
    """)
    time.sleep(1)
    
    digitar_texto("\nPressione ENTER para finalizar...")
    input()

def conclusao():
    """Observações finais"""
    imprimir_cabecalho("CONCLUSÃO")
    
    digitar_texto("Parabéns! Você completou o tutorial sobre Tradução!")
    time.sleep(1)
    
    print("\n")
    print("    ╔════════════════════════════════════════════╗")
    print("    ║                                            ║")
    print("    ║      DNA → mRNA → Ribossomo → PROTEÍNA    ║")
    print("    ║                                            ║")
    print("    ║   A tradução é fundamental para a vida!    ║")
    print("    ║                                            ║")
    print("    ╚════════════════════════════════════════════╝")
    print()
    
    digitar_texto("\n[PONTOS-CHAVE] PRINCIPAIS CONCLUSÕES:")
    print("  [✓] A tradução converte mRNA em proteínas")
    print("  [✓] Três fases: Iniciação, Elongação, Terminação")
    print("  [✓] Ribossomos são as máquinas moleculares")
    print("  [✓] tRNA entrega aminoácidos baseado no reconhecimento de códons")
    print("  [✓] Desregulação da tradução causa doenças")
    print("  [✓] Existem muitos alvos terapêuticos")
    
    time.sleep(2)
    
    print("\n" + "═" * 80)
    digitar_texto("\n[LEITURA] LEITURA RECOMENDADA:", atraso=0.02)
    print("\n  • Jia et al. (2024) - Signal Transduction and Targeted Therapy")
    print("    'Protein translation: biological processes and therapeutic")
    print("     strategies for human diseases'")
    print("\n  • DOI: 10.1038/s41392-024-01749-9")
    
    time.sleep(1)
    
    print("\n" + "═" * 80)
    digitar_texto("\n[***] Obrigado por aprender sobre Tradução de Proteínas! [***]")
    digitar_texto("\nCriado por Madson Aragão @ UFMG")
    print()

def main():
    """Fluxo principal do programa"""
    try:
        introducao()
        dogma_central()
        maquinaria_traducao()
        fase_iniciacao()
        fase_elongacao()
        fase_terminacao()
        dobramento_proteico()
        resumo()
        relevancia_clinica()
        tecnicas_pesquisa()
        conclusao()
        
    except KeyboardInterrupt:
        print("\n\n[!] Tutorial interrompido pelo usuário.")
        print("Obrigado por participar!\n")
        sys.exit(0)

if __name__ == "__main__":
    main()

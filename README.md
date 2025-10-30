# Bits, Bytes e Biomoléculas: Introdução à Modelagem de Proteínas com Métodos Clássicos e de Aprendizado de Máquina

### Instrutor: Madson Aragão (Bioinformática @ UFMG, MSc em Genética & Biologia Molecular)
### Monitor: Saulo Penna (Biomedicina @ UFPE, Pesquisador no LGBV/UFPE)
### Evento: XV Jornada PPGGBM - 19 de Novembro de 2025

Este repositório contém o material de referência completo para o curso, incluindo conceitos fundamentais, guias de ferramentas e leituras recomendadas.

---

## O Desafio Central: O Enovelamento de Proteínas

O problema do enovelamento de proteínas — como uma cadeia polipeptídica linear atinge sua complexa e funcional estrutura tridimensional — representa um dos maiores desafios da biologia molecular contemporânea. Avanços notáveis, como o AlphaFold, forneceram soluções preditivas sem precedentes, mas a compreensão fundamental dos mecanismos de enovelamento, regidos pela termodinâmica e pela evolução, permanece um campo de intensa investigação para biólogos, físicos e químicos.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### A Paisagem Energética: O Funil de Enovelamento

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

Para visualizar a complexidade deste processo, utilizamos a metáfora do **funil de enovelamento**. Este modelo descreve a paisagem energética que uma proteína atravessa para atingir sua conformação nativa.
*   **Topo do Funil (Alta Energia, Alta Entropia):** No topo, a proteína recém-sintetizada (desenovelada) existe em um vasto número de conformações possíveis, caracterizando um estado de alta entropia conformacional e alta energia livre de Gibbs.
*   **Paisagem Rugosa (Estados Intermediários):** À medida que a proteína se enovela, ela "desce" pelo funil, restringindo seu espaço conformacional e diminuindo sua energia livre. As paredes do funil são **rugosas**, com depressões que representam **estados intermediários metaestáveis**. Alguns destes estados podem possuir atividade biológica, indicando que o processo de enovelamento pode ser funcionalmente relevante.
*   **Fundo do Funil (Mínimo de Energia Livre):** O ponto mais baixo representa o **estado nativo**: a conformação tridimensional termodinamicamente mais estável e biologicamente ativa, caracterizada por seu mínimo global de energia livre.

### A Lógica da Energia em Bioquímica
Em biologia molecular, a estabilidade de um sistema é descrita pela **energia livre de Gibbs (ΔG)**. Processos espontâneos, como o enovelamento de proteínas, ocorrem com uma diminuição da energia livre total do sistema (ΔG < 0). Portanto, um valor de **ΔG mais negativo** indica uma conformação mais estável e energeticamente favorável.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### O Paradoxo de Levinthal
Formulado por Cyrus Levinthal, este paradoxo destaca a impossibilidade de o enovelamento ocorrer por uma busca aleatória. Ele calculou que uma proteína levaria mais tempo que a idade do universo para testar todas as suas conformações possíveis. Isso demonstra que o enovelamento não é um processo aleatório, mas sim um processo altamente direcionado que segue "caminhos" ou "rotas" específicas, otimizadas ao longo da evolução, para atingir o estado nativo em uma escala de tempo biologicamente viável.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

---

## Módulo 1: Fundamentos da Sequência e Estrutura Proteica

### Estrutura Secundária: Os Pilares da Arquitetura Proteica

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

A **estrutura secundária** refere-se aos arranjos locais e regulares da cadeia polipeptídica, estabilizados por um padrão de pontes de hidrogênio entre os átomos do esqueleto peptídico (N-H e C=O).

| Estrutura | Descrição e Características |
|:---|:---|
| **α-Hélice** | Estrutura helicoidal, geralmente dextrogira. Estabilizada por pontes de hidrogênio **intracadeia** entre o resíduo *i* e o *i+4*. Contém **3.6 resíduos por volta**. |
| **Hélice 3₁₀** | Uma hélice mais "apertada", com **3 resíduos por volta** (pontes de hidrogênio *i* a *i+3*). Menos estável que a α-hélice, frequentemente encontrada em suas extremidades. |
| **Hélice π** | Hélice mais larga com **4.4 resíduos por volta** (pontes de hidrogênio *i* a *i+5*). Energeticamente menos favorável e rara. |
| **Fita-β** | Um segmento quase totalmente estendido da cadeia polipeptídica. Isolada, é instável. |
| **Folha-β** | Formada pela associação de duas ou mais **fitas-β** adjacentes, estabilizadas por pontes de hidrogênio **intercadeias**. Podem ser **paralelas** ou **antiparalelas**. |
| **Voltas e Alças** | Regiões não repetitivas que conectam elementos de estrutura secundária. **Voltas-β** são curtas (4 resíduos) e causam uma reversão de 180°. |

### α-Hélice: Um Fóssil Estrutural
A α-hélice é considerada um "fóssil estrutural". Sua estabilidade depende apenas de interações locais, tornando-a um módulo autônomo e robusto, provavelmente um dos primeiros a surgir na evolução de proteínas.

> Este texto de revisão estará disponível em breve no bioRxiv sob o título: *Everything In Its Right Place: Thermodynamic and Evolutionary Drivers of the Primordial α-Helix Prevalence in Proteins*. Um vez disponível, poderá ser encontrado também em https://madsondeluna.github.io/.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Everything in its Right Place? Talvez o Radiohead estivesse certo esse tempo todos!

A α-hélice constitui um motivo estrutural fundamental em proteínas, representando uma topologia cuja origem pode ser associada até aos processos químicos pré-bióticos que precederam o surgimento da vida. A compreensão das forças que governam a prevalência deste elemento estrutural requer uma análise integrada que conecte a bioquímica do período pré-biótico, os princípios termodinâmicos de enovelamento proteico e a distribuição de domínios estruturais entre as mais diversas proteínas encontradas nos seres vivos.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### O Repertório Pré-biótico e Propensões Conformacionais

Experimentos pioneiros de síntese abiótica, iniciados com Miller e Urey, e análises composicionais de meteoritos carbonáceos estabeleceram um consenso quanto aos aminoácidos disponíveis na Terra primitiva. Este repertório pré-biótico, compreendendo aproximadamente 10 aminoácidos (Gly, Ala, Val, Leu, Ile, Pro, Ser, Thr, Asp, Glu), apresentava características notáveis: ausência de resíduos básicos (Lys, Arg, His) e aromáticos volumosos (Trp, Tyr, Phe), resultando em um conjunto de monômeros de natureza ácida e hidrofobicidade moderada. Crucialmente, este alfabeto molecular exibia propensões conformacionais assimétricas. Por exemplo, a Alanina é reconhecida como um dos mais potentes formadores de α-hélices devido à ausência de impedimentos estéricos em sua cadeia lateral metílica, seguida por Leucina, que combina hidrofobicidade com estabilização helicoidal. Em contrapartida, Glicina, devido à sua flexibilidade conformacional irrestrita, e Prolina, devido à rigidez imposta por seu anel imídico, que restringe os ângulos diedrais, atuam como disruptores de estruturas secundárias regulares.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Estabilidade Termodinâmica

A estabilidade termodinâmica da α-hélice deriva de múltiplas contribuições energéticas. As ligações de hidrogênio entre o grupo carbonila (C=O) do resíduo i e o grupo amida (N-H) do resíduo i+4 contribuem com aproximadamente 40% da estabilidade total, satisfazendo os requisitos polares da cadeia principal peptídica. As interações de van der Waals entre cadeias laterais hidrofóbicas no núcleo helicoidal contribuem com cerca de 60% da estabilização. Esta arquitetura é particularmente favorecida em ambientes apolares, como o núcleo hidrofóbico de membranas lipídicas, onde a energia livre de inserção de segmentos helicoidais hidrofóbicos é substancialmente negativa.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### A Interface Peptídeo-Membrana

Outro ponto da bioquímica pré-biótica é a interface peptídeo-membrana, que representa um contexto termodinâmico e cinético privilegiado para a emergência de estruturas helicoidais na Terra primitiva. Vesículas lipídicas primitivas teriam concentrado aminoácidos da solução aquosa diluída, aumentando drasticamente a probabilidade de polimerização via mecanismos de ciclagem úmido-seco ou catálise mineral. Simultaneamente, peptídeos nascentes contendo sequências hidrofóbicas derivadas de Ala, Val, Leu e Ile teriam sido espontaneamente recrutados para a interface membrana-água ou inseridos no núcleo apolar da bicamada, onde a formação de α-hélices seria termodinamicamente favorecida para maximizar ligações de hidrogênio intramoleculares. Esta simbiose primordial peptídeo-membrana teria criado as condições ideais para a seleção evolutiva de sequências helicoidais funcionais, incluindo precursores de proteínas de membrana, canais iônicos primitivos e peptídeos antimicrobianos.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Síntese e Análise Contemporânea

Este trabalho integra a análise de princípios teóricos da química pré-biótica e termodinâmica proteica com uma investigação quantitativa em larga escala do Protein Data Bank (PDB), visando explorar e comentar a hipótese de que a prevalência contemporânea de motivos helicoidais é um reflexo direto das restrições bioquímicas e vantagens termodinâmicas que consagraram a α-hélice como um bloco de construção arquitetônico fundamental desde as origens da vida.

---

### Motivos Supersecundários e Domínios Proteicos

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

A combinação de elementos de estrutura secundária forma **motivos supersecundários**, os blocos de construção dos **domínios** proteicos (regiões que se enovelam e funcionam de forma independente).

| Motivo | Descrição | Função/Exemplos |
|:---|:---|:---|
| **Hélice-Alça-Hélice** | Duas α-hélices conectadas por uma alça. | Comum em fatores de transcrição que se ligam ao DNA. |
| **Forquilha-β (β-hairpin)** | Duas fitas-β antiparalelas conectadas por uma volta-β curta. | Um dos motivos mais simples e comuns. |
| **Motivo β-α-β** | Duas fitas-β paralelas conectadas por uma α-hélice. | Componente central de muitas dobras, como o *Rossmann fold*. |
| **Barril-β** | Uma grande folha-β que se fecha sobre si mesma, formando um cilindro. | Característico de porinas de membrana. |

Para explorar a diversidade de dobras, utilizamos bancos de dados como o **CATH (Class, Architecture, Topology, Homologous superfamily)**. O CATH organiza as estruturas em uma hierarquia que nos ajuda a entender as relações evolutivas entre as proteínas.
**[Explorar o CATH](https://www.cathdb.info/ "Abrir em nova aba")**

---

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Propriedades dos Aminoácidos Canônicos
| Aminoácido | Propriedades | Tendência Estrutural |
|:---|:---|:---|
| Alanina (Ala) | Apolar, hidrofóbico | Forte formador de α-hélice |
| Arginina (Arg) | Polar, carregado positivamente | Superfície, formação de pontes salinas |
| Glicina (Gly) | Apolar, muito flexível | Regiões de curvas (turns) e loops |
| Prolina (Pro) | Cíclico, conformacionalmente restrito | "Quebrador" de estruturas secundárias |
| Leucina (Leu), Valina (Val), Isoleucina (Ile) | Apolares, hidrofóbicos | Núcleo hidrofóbico |
| Fenilalanina (Phe), Triptófano (Trp), Tirosina (Tyr) | Aromáticos | Núcleo hidrofóbico, interações de empilhamento (pi-stacking) |

---

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Interações Intermoleculares Estabilizadoras
| Interação | Distância (Å) | Natureza da Força | Aminoácidos Frequentes |
|:---|:---:|:---|:---|
| Ponte de Hidrogênio | 2.7–3.2 | Eletrostática (dipolo-dipolo forte) | Ser, Thr, Tyr, Asn, Gln, His e esqueleto peptídico |
| Ponte Salina (Iônica) | 2.8–4.0 | Eletrostática entre cargas opostas | Arg, Lys, His (+) com Asp, Glu (-) |
| Empilhamento Pi (π-π Stacking) | 3.4–4.0 | Interação entre as nuvens de elétrons de anéis aromáticos | Phe, Tyr, Trp, His |
| Forças de van der Waals | 3.5–4.0 | Flutuações de dipolos instantâneos | Todos os resíduos, crucial no empacotamento do núcleo |
| Interação Cátion-π | 3.5–5.0 | Eletrostática entre um cátion e um anel aromático | Arg, Lys com Phe, Tyr, Trp |

### Ferramentas e Bancos de Dados Essenciais
*   **[UniProt](https://www.uniprot.org/ "Abrir em nova aba")**, **[PDB](https://www.rcsb.org/ "Abrir em nova aba")**, **[InterProScan](https://www.ebi.ac.uk/interpro/ "Abrir em nova aba")**, **[ExPASy ProtParam](https://web.expasy.org/protparam/ "Abrir em nova aba")**.

---

## Módulo 2: Técnicas Clássicas de Modelagem Molecular

### Modelagem por Homologia (Comparativa)
*   **Servidor Principal:** **[SWISS-MODEL](https://swissmodel.expasy.org/ "Abrir em nova aba")**.

### Modelagem *Ab Initio*
*   **Como Funciona:** **Rosetta** usa uma abordagem de montagem por fragmentos, combinados por um algoritmo de busca estocástica para encontrar o mínimo energético.
*   **TOP-7 e o Nobel de 2024:** Em 2003, o Rosetta foi usado para projetar a **Top7**, um marco que contribuiu para o **Prêmio Nobel de Química de 2024**.

### Threading (Reconhecimento de Dobra)
*   **Como Funciona:** O algoritmo realiza um alinhamento sequência-estrutura, avaliando a compatibilidade de uma sequência com cada dobra de uma biblioteca.
*   **I-TASSER:** O **[I-TASSER](https://zhanggroup.org/I-TASSER/ "Abrir em nova aba")** combina Threading com montagem e refino.

---

## Módulo 3: A Revolução do Aprendizado de Máquina

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Comparativo de Ferramentas de Aprendizado de Máquina
| Ferramenta | Descrição | Aplicação | Link |
|:---|:---|:---|:---|
| AlphaFold 2 | Predição de estruturas monoméricas usando redes neurais e MSAs. | Estruturas monoméricas. | [Artigo](https://www.nature.com/articles/s41586-021-03819-2 "Abrir em nova aba") |
| AlphaFold-Multimer | Extensão para prever estruturas de complexos proteicos. | Complexos proteína-proteína. | [Artigo](https://www.nature.com/articles/s41467-021-24462-3 "Abrir em nova aba") |
| AlphaFold 3 | Versão mais recente para diversos tipos de biomoléculas. | Monômeros, multímeros, interações com DNA/RNA. | [Site Oficial](https://alphafold.ebi.ac.uk/ "Abrir em nova aba") |
| RoseTTAFold | Modelo que integra informações de sequência, estrutura e contato. | Predição estrutural, incluindo multímeros. | [Site Oficial](https://robetta.bakerlab.org/ "Abrir em nova aba") |
| ESM Atlas | Modelo baseado em linguagem de proteínas para predição. | Interações proteína-proteína usando embeddings. | [Site Oficial](https://esmatlas.com/ "Abrir em nova aba") |
| ESM Cambrian | Modelo de linguagem de última geração para predição detalhada. | Estruturas e interações complexas. | [Site Oficial](https://esmatlas.com/ "Abrir em nova aba") |

---

## Módulo 4: Análise, Validação e Interpretação de Modelos Estruturais

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Ferramentas de Visualização Molecular
*   **[PyMOL](https://pymol.org/2/ "Download PyMOL")**: Padrão para geração de figuras de alta qualidade.
*   **[VMD](https://www.ks.uiuc.edu/Research/vmd/ "Download VMD")**: Excelente para análise de trajetórias de dinâmica molecular.
*   **[ChimeraX](https://www.cgl.ucsf.edu/chimerax/ "Download ChimeraX")**: Poderoso e extensível, com ótima integração com bancos de dados.

### Análise Comparativa: RMSD e sua Importância
O **Root Mean Square Deviation (RMSD)** quantifica a diferença média entre as posições dos átomos correspondentes em duas estruturas alinhadas. A fórmula é:
\[
RMSD = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} \delta_i^2 }
\]
onde \(N\) é o número de átomos e \(\delta_i\) é a distância entre o átomo *i* em cada estrutura.

É crucial em:
*   **Dinâmica Molecular:** Para avaliar a estabilidade de uma simulação (um RMSD baixo e estável indica que a proteína não está se "desfazendo").
*   **Docking Molecular:** Para validar um protocolo (re-docking) e avaliar a similaridade entre poses de ligantes geradas.

### Servidores de Validação de Estrutura
| Servidor | Descrição |
|:---|:---|
| **[SAVES](https://saves.mbi.ucla.edu/ "Abrir em nova aba")** | Integra PROCHECK (estereoquímica) e ERRAT (interações não-ligadas). |
| **[MolProbity](http://molprobity.biochem.duke.edu/ "Abrir em nova aba")** | Focado em contatos atômicos (clashes) e geometria. |
| **[QMEANDisCo](https://swissmodel.expasy.org/qmean/ "Abrir em nova aba")** | Avalia a qualidade global e local do modelo. |

---

## Referências e Leituras Recomendadas

1.  Anfinsen, C. B. (1973). Principles that govern the folding of protein chains. *Science, 181(4096)*, 223–230.
2.  Dill, K. A., & MacCallum, J. L. (2012). The Protein-Folding Problem, 50 Years On. *Science, 338(6110)*, 1042–1046.
3.  Jumper, J. et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature, 596(7873)*, 583–589.
4.  Kuhlman, B., Dantas, G., et al. (2003). Design of a novel globular protein fold with atomic-level accuracy. *Science, 302(5649)*, 1364–1368.
5.  Yang, J., et al. (2015). The I-TASSER Suite: protein structure and function prediction. *Nature Methods, 12(1)*, 7–8.
6.  [Nobel Prize in Chemistry 2024 - Popular Information](https://www.nobelprize.org/prizes/chemistry/2024/popular-information/ "Abrir em nova aba")


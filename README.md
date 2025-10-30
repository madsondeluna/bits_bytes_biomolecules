# Bits, Bytes e Biomoléculas: Introdução à Modelagem de Proteínas com Métodos Clássicos e de Aprendizado de Máquina

### Instrutor: Madson Aragão (Bioinformática @ UFMG, MSc em Genética & Biologia Molecular)
### Evento: XV Jornada PPGGBM - 19 de Novembro de 2025

Este repositório contém o material de referência completo para o curso, incluindo conceitos fundamentais, guias de ferramentas e leituras recomendadas.

---

## O Desafio Central: O Enovelamento de Proteínas

O problema do enovelamento de proteínas — como uma cadeia polipeptídica linear atinge sua complexa e funcional estrutura tridimensional — representa um dos maiores desafios da biologia molecular contemporânea. Avanços notáveis, como o AlphaFold, forneceram soluções preditivas sem precedentes, mas a compreensão fundamental dos mecanismos de enovelamento, regidos pela termodinâmica e pela evolução, permanece um campo de intensa investigação.

### A Paisagem Energética: O Funil de Enovelamento

[ADICIONAR IMAGEM EXPLICATIVA AQUI]
<!-- Comentário: Inserir um diagrama do funil de enovelamento, mostrando a alta entropia no topo, a paisagem rugosa com estados intermediários e o estado nativo de mínima energia no fundo. -->

Para visualizar a complexidade deste processo, utilizamos a metáfora do **funil de enovelamento**. Este modelo descreve a paisagem energética que uma proteína atravessa para atingir sua conformação nativa.
*   **Topo do Funil (Alta Energia, Alta Entropia):** No topo, a proteína recém-sintetizada (desenovelada) existe em um vasto número de conformações possíveis, caracterizando um estado de alta entropia conformacional e alta energia livre de Gibbs.
*   **Paisagem Rugosa (Estados Intermediários):** À medida que se enovela, a proteína "desce" pelo funil, restringindo seu espaço conformacional e diminuindo sua energia livre. As paredes do funil são **rugosas**, com depressões que representam **estados intermediários metaestáveis**. Alguns destes estados podem possuir atividade biológica, indicando que o processo de enovelamento pode ser funcionalmente relevante.
*   **Fundo do Funil (Mínimo de Energia Livre):** O ponto mais baixo representa o **estado nativo**: a conformação tridimensional termodinamicamente mais estável e biologicamente ativa, caracterizada por seu mínimo global de energia livre.

### O Paradoxo de Levinthal
Formulado por Cyrus Levinthal, este paradoxo destaca a impossibilidade de o enovelamento ocorrer por uma busca aleatória. Ele calculou que uma proteína levaria mais tempo que a idade do universo para testar todas as suas conformações possíveis. Isso demonstra que o enovelamento segue "caminhos" ou "rotas" específicas, otimizadas evolutivamente, para atingir o estado nativo em uma escala de tempo biologicamente viável.

---

## Módulo 1: Fundamentos da Sequência e Estrutura Proteica

### Estrutura Secundária: Os Pilares da Arquitetura Proteica

[ADICIONAR IMAGEM EXPLICATIVA AQUI]
<!-- Comentário: Inserir uma imagem que mostre em detalhe uma alfa-hélice e uma folha-beta, destacando as pontes de hidrogênio em cada uma. -->

A **estrutura secundária** refere-se aos arranjos locais e regulares da cadeia polipeptídica, estabilizados por um padrão de pontes de hidrogênio entre os átomos do esqueleto peptídico (N-H e C=O).

| Estrutura | Descrição e Características |
|:---|:---|
| **α-Hélice** | Estrutura helicoidal, geralmente dextrogira (sentido horário). É estabilizada por pontes de hidrogênio **intracadeia** entre o grupo C=O do resíduo *i* e o grupo N-H do resíduo *i+4*. Contém **3.6 resíduos por volta**. |
| **Hélice 3₁₀** | Uma hélice mais "apertada" e menos comum, com **3 resíduos por volta**. As pontes de hidrogênio se formam entre o resíduo *i* e o *i+3*. |
| **Fita-β** | Um segmento quase totalmente estendido da cadeia polipeptídica. Uma fita-β isolada é instável. |
| **Folha-β** | Formada pela associação de duas ou mais **fitas-β** adjacentes, estabilizadas por pontes de hidrogênio **intercadeias**. As fitas podem se alinhar de forma **paralela** ou **antiparalela**. |
| **Voltas e Alças** | Regiões não repetitivas que conectam elementos de estrutura secundária. **Voltas-β** são curtas (4 resíduos) e causam uma reversão de 180° na cadeia. |

#### α-Hélice: Um Fóssil Estrutural
A α-hélice é considerada um "fóssil estrutural" da evolução. Sua estabilidade depende apenas de interações locais (entre resíduos próximos na sequência), tornando-a um módulo estrutural autônomo e robusto, provavelmente um dos primeiros a surgir na evolução de proteínas.

### Motivos Supersecundários e Domínios Proteicos

[ADICIONAR IMAGEM EXPLICATIVA AQUI]
<!-- Comentário: Inserir uma imagem mostrando exemplos de motivos supersecundários, como Hélice-Alça-Hélice, Forquilha-β e Barril-β. -->

A combinação de elementos de estrutura secundária forma **motivos supersecundários**, que são os blocos de construção dos **domínios** proteicos (regiões de uma proteína que se enovelam e funcionam de forma independente).
*   **Hélice-Alça-Hélice:** Duas α-hélices conectadas por uma alça, comum em fatores de transcrição que se ligam ao DNA.
*   **Forquilha-β (β-hairpin):** Duas fitas-β antiparalelas conectadas por uma volta-β.
*   **Motivo β-α-β:** Duas fitas-β paralelas conectadas por uma α-hélice.
*   **Barril-β:** Uma grande folha-β que se fecha sobre si mesma, formando uma estrutura cilíndrica, comum em porinas de membrana.

Para explorar a vasta diversidade de dobras proteicas, utilizamos bancos de dados como o **CATH (Class, Architecture, Topology, Homologous superfamily)**. O CATH organiza as estruturas do PDB em uma hierarquia evolutiva, permitindo analisar como diferentes combinações de estruturas secundárias (Arquitetura e Topologia) dão origem a famílias de proteínas funcionalmente diversas.
*   **[Explorar o CATH](https://www.cathdb.info/)**

### Propriedades dos Aminoácidos Canônicos
| Aminoácido | Propriedades | Tendência Estrutural |
|:---|:---|:---|
| Alanina (Ala) | Apolar, hidrofóbico | Forte formador de α-hélice |
| Arginina (Arg) | Polar, carregado positivamente | Superfície, formação de pontes salinas |
| Glicina (Gly) | Apolar, muito flexível | Regiões de curvas (turns) e loops |
| Prolina (Pro) | Cíclico, conformacionalmente restrito | "Quebrador" de estruturas secundárias, comum em curvas |
| Leucina (Leu) | Apolar, hidrofóbico | Forte formador de α-hélices e núcleo hidrofóbico |
| Fenilalanina (Phe) | Aromático, hidrofóbico | Núcleo hidrofóbico, interações de empilhamento (pi-stacking) |

### Ferramentas e Bancos de Dados Essenciais
*   **[UniProt](https://www.uniprot.org/)**, **[PDB](https://www.rcsb.org/)**, **[InterProScan](https://www.ebi.ac.uk/interpro/)**, **[ExPASy ProtParam](https://web.expasy.org/protparam/)**.

---

## Módulo 2: Técnicas Clássicas de Modelagem Molecular

### Modelagem por Homologia (Comparativa)
Baseada no princípio de que proteínas com identidade de sequência significativa (>30%) conservam sua estrutura tridimensional.
*   **Servidor Principal:** **[SWISS-MODEL](https://swissmodel.expasy.org/)**.

### Modelagem *Ab Initio*
Busca prever a estrutura 3D a partir de princípios físico-químicos, usando apenas a sequência.
*   **Como Funciona:** O software **Rosetta** utiliza uma abordagem de montagem por fragmentos, onde pequenos fragmentos (3-9 resíduos) de estruturas conhecidas são combinados por um algoritmo de busca estocástica (Monte Carlo).
*   **TOP-7 e o Nobel de 2024:** Em 2003, o Rosetta foi usado para projetar a **Top7**, a primeira proteína com uma dobra totalmente nova, um marco que contribuiu para o **Prêmio Nobel de Química de 2024**.

### Threading (Reconhecimento de Dobra)
Método para proteínas que não possuem homólogos de sequência, mas cuja dobra pode ser semelhante a uma já conhecida.
*   **Como Funciona:** O algoritmo realiza um alinhamento sequência-estrutura, avaliando a compatibilidade de uma sequência alvo com cada estrutura de uma biblioteca de dobras.
*   **I-TASSER:** O **[I-TASSER](https://zhanggroup.org/I-TASSER/)** combina Threading com montagem de fragmentos e refino por simulação.

---

## Módulo 3: A Revolução do Aprendizado de Máquina

### Comparativo de Ferramentas de Aprendizado de Máquina
| Ferramenta | Descrição | Aplicação |
|:---|:---|:---|
| AlphaFold 2 | Predição de estruturas monoméricas usando redes neurais e MSAs. | Estruturas monoméricas. |
| AlphaFold-Multimer | Extensão para prever estruturas de complexos proteicos. | Complexos proteína-proteína. |
| AlphaFold 3 | Versão mais recente para diversos tipos de biomoléculas. | Monômeros, multímeros, interações com DNA/RNA. |
| RoseTTAFold | Modelo que integra informações de sequência, estrutura e contato. | Predição estrutural, incluindo multímeros. |
| ESM Atlas | Modelo baseado em linguagem de proteínas para predição de estrutura e interações. | Interações proteína-proteína usando embeddings. |

---

## Módulo 4: Análise e Validação Estrutural

### Ferramentas de Visualização
*   **[PyMOL](https://pymol.org/2/)**, **[VMD](https://www.ks.uiuc.edu/Research/vmd/)**.

### Servidores de Validação de Estrutura
| Servidor | Descrição |
|:---|:---|
| **[SAVES](https://saves.mbi.ucla.edu/)** | Integra ferramentas como PROCHECK (estereoquímica) e ERRAT (interações não-ligadas). |
| **[MolProbity](http://molprobity.biochem.duke.edu/)** | Focado na análise de contatos atômicos (clashes) e geometria. |
| **[QMEANDisCo](https://swissmodel.expasy.org/qmean/)** | Avalia a qualidade global e local do modelo. |

---

## Referências e Leituras Recomendadas

1.  Anfinsen, C. B. (1973). Principles that govern the folding of protein chains. *Science, 181(4096)*, 223–230.
2.  Dill, K. A., & MacCallum, J. L. (2012). The Protein-Folding Problem, 50 Years On. *Science, 338(6110)*, 1042–1046.
3.  Jumper, J. et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature, 596(7873)*, 583–589.
4.  Kuhlman, B., Dantas, G., et al. (2003). Design of a novel globular protein fold with atomic-level accuracy. *Science, 302(5649)*, 1364–1368.
5.  Yang, J., et al. (2015). The I-TASSER Suite: protein structure and function prediction. *Nature Methods, 12(1)*, 7–8.
6.  [Nobel Prize in Chemistry 2024 - Popular Information](https://www.nobelprize.org/prizes/chemistry/2024/popular-information/)


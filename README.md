# Bits, Bytes e Biomoléculas: Introdução à Modelagem de Proteínas com Métodos Clássicos e de Aprendizado de Máquina

### Instrutor: Madson Aragão (Bioinformática @ UFMG, MSc em Genética & Biologia Molecular)
### Evento: XV Jornada PPGGBM - 19 de Novembro de 2025

Este repositório contém o material de referência completo para o curso, incluindo conceitos fundamentais, guias de ferramentas e leituras recomendadas.

---

## O Desafio Central: O Enovelamento de Proteínas

O problema do enovelamento de proteínas — como uma cadeia polipeptídica linear atinge sua complexa e funcional estrutura tridimensional — representa um dos maiores desafios da biologia molecular. Avanços notáveis, como o AlphaFold, forneceram soluções preditivas sem precedentes, mas a compreensão fundamental dos mecanismos de enovelamento, regidos pela termodinâmica e pela evolução, permanece um campo de intensa investigação.

### A Paisagem Energética: O Funil de Enovelamento

Para visualizar a complexidade deste processo, utilizamos a metáfora do **funil de enovelamento**. Este modelo descreve a paisagem energética que uma proteína atravessa para atingir sua conformação nativa.
*   **Topo do Funil (Alta Energia, Alta Entropia):** No topo, a proteína recém-sintetizada (desenovelada) existe em um vasto número de conformações possíveis, caracterizando um estado de alta entropia conformacional e alta energia livre de Gibbs.
*   **Paisagem Rugosa (Estados Intermediários):** À medida que se enovela, a proteína "desce" pelo funil, restringindo seu espaço conformacional e diminuindo sua energia livre. As paredes do funil são **rugosas**, com depressões que representam **estados intermediários metaestáveis**. Alguns destes estados podem possuir atividade biológica, indicando que o processo de enovelamento pode ser funcionalmente relevante.
*   **Fundo do Funil (Mínimo de Energia Livre):** O ponto mais baixo representa o **estado nativo**: a conformação tridimensional termodinamicamente mais estável e biologicamente ativa, caracterizada por seu mínimo global de energia livre.

### A Termodinâmica da Estabilidade
Em bioquímica, a estabilidade é quantificada pela **energia livre de Gibbs (ΔG)**. Processos espontâneos, como o enovelamento, ocorrem com uma diminuição da energia livre (ΔG < 0). Portanto, um valor de **ΔG mais negativo** indica uma conformação mais estável.

### O Paradoxo de Levinthal
Formulado por Cyrus Levinthal, este paradoxo destaca a impossibilidade de o enovelamento ocorrer por uma busca aleatória. Ele calculou que uma proteína levaria mais tempo que a idade do universo para testar todas as suas conformações possíveis. Isso demonstra que o enovelamento segue "caminhos" ou "rotas" específicas, otimizadas evolutivamente, para atingir o estado nativo em uma escala de tempo biologicamente viável.

---

## Módulo 1: Fundamentos da Sequência e Estrutura Proteica

A sequência primária é o código que dita as interações físico-químicas que guiarão o enovelamento.

### Propriedades dos Aminoácidos Canônicos

| Aminoácido | Propriedades | Tendência Estrutural |
|:---|:---|:---|
| Alanina (Ala) | Apolar, hidrofóbico | Forte formador de α-hélice |
| Arginina (Arg) | Polar, carregado positivamente | Superfície, formação de pontes salinas |
| Asparagina (Asn) | Polar, não carregado | Superfície, formação de pontes de hidrogênio |
| Ácido aspártico (Asp) | Polar, carregado negativamente | Superfície, formação de pontes salinas |
| Cisteína (Cys) | Polar, pode formar pontes dissulfeto | Estabilização covalente de dobras |
| Glutamina (Gln) | Polar, não carregado | Superfície, interação com água |
| Ácido glutâmico (Glu) | Polar, carregado negativamente | Superfície, formação de pontes salinas |
| Glicina (Gly) | Apolar, muito flexível | Regiões de curvas (turns) e loops |
| Histidina (His) | Polar, pode ser neutra ou positiva em pH fisiológico | Sítios catalíticos, interações metal-proteína |
| Isoleucina (Ile) | Apolar, hidrofóbico, cadeia lateral β-ramificada | Núcleo hidrofóbico, formação de folhas-β |
| Leucina (Leu) | Apolar, hidrofóbico | Forte formador de α-hélices e núcleo hidrofóbico |
| Lisina (Lys) | Polar, carregado positivamente | Superfície, formação de pontes salinas |
| Metionina (Met) | Apolar, hidrofóbico | Núcleo hidrofóbico, início da tradução |
| Fenilalanina (Phe) | Aromático, hidrofóbico | Núcleo hidrofóbico, interações de empilhamento (pi-stacking) |
| Prolina (Pro) | Cíclico, conformacionalmente restrito | "Quebrador" de estruturas secundárias, comum em curvas |
| Serina (Ser) | Polar, não carregado | Superfície, formação de pontes de hidrogênio |
| Treonina (Thr) | Polar, não carregado | Superfície, interações hidrofílicas |
| Triptófano (Trp) | Aromático, o mais hidrofóbico | Núcleo hidrofóbico, âncora de membrana |
| Tirosina (Tyr) | Aromático, polar | Superfície e núcleo, pode ser fosforilada |
| Valina (Val) | Apolar, hidrofóbico, cadeia lateral β-ramificada | Núcleo hidrofóbico, formação de folhas-β |

### Interações Intermoleculares Estabilizadoras

| Interação | Distância (Å) | Natureza da Força | Aminoácidos Frequentes |
|:---|:---:|:---|:---|
| Ponte de Hidrogênio | 2.7–3.2 | Eletrostática (dipolo-dipolo forte) | Ser, Thr, Tyr, Asn, Gln, His e esqueleto peptídico |
| Ponte Salina (Iônica) | 2.8–4.0 | Eletrostática entre grupos com cargas opostas | Arg, Lys, His (+) com Asp, Glu (-) |
| Empilhamento Pi (π-π Stacking) | 3.4–4.0 | Interação entre as nuvens de elétrons de anéis aromáticos | Phe, Tyr, Trp, His |
| Interações CH-π | 3.0–4.0 | Interação fraca entre um grupo C-H e um anel aromático | Leucina, Isoleucina com Phe, Tyr, Trp |
| Forças de van der Waals | 3.5–4.0 | Flutuações de dipolos instantâneos, atrativas a curta distância | Todos os resíduos, crucial no empacotamento do núcleo |

### Ferramentas e Bancos de Dados Essenciais
*   **[UniProt](https://www.uniprot.org/):** Principal recurso para informações de sequência, função e anotações.
*   **[Protein Data Bank (PDB)](https://www.rcsb.org/):** Repositório mundial de estruturas 3D de macromoléculas.
*   **[InterProScan](https://www.ebi.ac.uk/interpro/):** Ferramenta para classificar proteínas, prever domínios e sítios funcionais.
*   **[ExPASy ProtParam](https://web.expasy.org/protparam/):** Calcula propriedades físico-químicas a partir da sequência.

---

## Módulo 2: Técnicas Clássicas de Modelagem Molecular

### Modelagem por Homologia (Comparativa)
Baseada no princípio de que proteínas com ancestralidade comum (e, portanto, identidade de sequência significativa, >30%) conservam sua estrutura tridimensional.
*   **Servidor Principal:** **[SWISS-MODEL](https://swissmodel.expasy.org/)**.

### Modelagem *Ab Initio*
Busca prever a estrutura 3D a partir de princípios físico-químicos, usando apenas a sequência.
*   **Como Funciona:** O software **Rosetta** utiliza uma abordagem de montagem por fragmentos, onde pequenos fragmentos (3-9 resíduos) de estruturas conhecidas são combinados por um algoritmo de busca estocástica (Monte Carlo). Cada conformação é avaliada por uma função de energia, buscando o mínimo energético.
*   **TOP-7 e o Nobel de 2024:** Em 2003, o Rosetta foi usado para projetar a **Top7**, a primeira proteína com uma dobra totalmente nova, um marco que contribuiu para o **Prêmio Nobel de Química de 2024**.

### Threading (Reconhecimento de Dobra)
Método para proteínas que não possuem homólogos de sequência, mas cuja dobra pode ser semelhante a uma já conhecida.
*   **Como Funciona:** O algoritmo realiza um alinhamento sequência-estrutura, avaliando a compatibilidade de uma sequência alvo com cada estrutura de uma biblioteca de dobras. A pontuação considera a preferência de cada aminoácido por um determinado ambiente estrutural.
*   **I-TASSER:** O **[I-TASSER](https://zhanggroup.org/I-TASSER/)** combina Threading com montagem de fragmentos e refino por simulação, sendo um dos métodos mais bem-sucedidos na área.

---

## Módulo 3: A Revolução do Aprendizado de Máquina

### Comparativo de Ferramentas de Aprendizado de Máquina

| Ferramenta | Descrição | Aplicação | Destaques |
|:---|:---|:---|:---|
| AlphaFold 2 | Predição de estruturas monoméricas usando redes neurais e MSAs. | Estruturas monoméricas. | Alta precisão, pLDDT confiável. |
| AlphaFold-Multimer | Extensão para prever estruturas de complexos proteicos. | Complexos proteína-proteína. | Predição multímera. |
| AlphaFold 3 | Versão mais recente para diversos tipos de biomoléculas. | Monômeros, multímeros, interações com DNA/RNA. | Melhorias em escala e escopo. |
| RoseTTAFold | Modelo que integra informações de sequência, estrutura e contato. | Predição estrutural, incluindo multímeros. | Bom balanço entre precisão e velocidade. |
| ESM Atlas | Modelo baseado em linguagem de proteínas para predição de estrutura e interações. | Interações proteína-proteína usando embeddings. | Inovador no uso de aprendizado de linguagem. |
| ESM Cambrian | Modelo de linguagem de última geração para predição detalhada de complexos. | Estruturas e interações complexas. | Alto desempenho em benchmarks. |

### Métricas de Confiança
*   **pLDDT (predicted Local Distance Difference Test):** Confiança na predição da estrutura local (por resíduo).
*   **PAE (Predicted Aligned Error):** Confiança na orientação relativa dos domínios.

---

## Módulo 4: Análise e Validação Estrutural

### Ferramentas de Visualização
*   **[PyMOL](https://pymol.org/2/)**: Padrão da indústria para geração de figuras de alta qualidade.
*   **[VMD (Visual Molecular Dynamics)](https://www.ks.uiuc.edu/Research/vmd/)**: Excelente para análise de trajetórias de dinâmica molecular.

### Servidores de Validação de Estrutura

| Servidor | Descrição |
|:---|:---|
| **[SAVES](https://saves.mbi.ucla.edu/)** | Portal que integra ferramentas como PROCHECK (análise estereoquímica) e ERRAT (qualidade de interações não-ligadas). |
| **[MolProbity](http://molprobity.biochem.duke.edu/)** | Ferramenta focada na análise de contatos atômicos (clashes), geometria e conformação de cadeias laterais. |
| **[QMEANDisCo](https://swissmodel.expasy.org/qmean/)** | Avalia a qualidade global (comparando com estruturas experimentais) e local (acordo entre resíduos) do modelo. |

---

## Referências e Leituras Recomendadas

1.  Anfinsen, C. B. (1973). Principles that govern the folding of protein chains. *Science, 181(4096)*, 223–230.
2.  Dill, K. A., & MacCallum, J. L. (2012). The Protein-Folding Problem, 50 Years On. *Science, 338(6110)*, 1042–1046.
3.  Jumper, J. et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature, 596(7873)*, 583–589.
4.  Kuhlman, B., Dantas, G., Ireton, G. C., Varani, G., Stoddard, B. L., & Baker, D. (2003). Design of a novel globular protein fold with atomic-level accuracy. *Science, 302(5649)*, 1364–1368.
5.  Yang, J., Yan, R., Roy, A., Xu, D., Poisson, J., & Zhang, Y. (2015). The I-TASSER Suite: protein structure and function prediction. *Nature Methods, 12(1)*, 7–8.
6.  [Nobel Prize in Chemistry 2024 - Popular Information](https://www.nobelprize.org/prizes/chemistry/2024/popular-information/)


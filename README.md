# Bits, Bytes e Biomoléculas: Guia Detalhado do Curso

Bem-vindo ao repositório de "Bits, Bytes e Biomoléculas"! Este documento serve como um guia expandido para o nosso curso de 8 horas sobre modelagem de proteínas, cobrindo desde os fundamentos clássicos até as mais recentes técnicas de aprendizado de máquina.

## Estrutura do Curso
- **Módulo I:** 8:00 - 12:00
- **Módulo II:** 13:30 - 17:30

---

## Módulo 1: Fundamentos e Caracterização da Sequências Primárias (2 horas)

Neste módulo, construiremos a base para entender como a sequência de aminoácidos dita a forma e a função de uma proteína.

### Conteúdo Programático Detalhado

1.  **Níveis de Organização Estrutural:**
    *   **Primária:** A sequência linear de aminoácidos.
    *   **Secundária:** Arranjos locais como **α-hélices** e **folhas-β** estabilizados por pontes de hidrogênio.
    *   **Terciária:** O dobramento tridimensional completo de uma cadeia polipeptídica.
    *   **Quaternária:** A associação de duas ou mais cadeias polipeptídicas para formar um complexo funcional.

2.  **Princípios do Enovelamento Proteico:**
    *   **Ligação Peptídica:** A ligação covalente que une os aminoácidos.
    *   **Ângulos Diédricos (Phi, Psi):** As rotações em torno das ligações N-Cα (phi, φ) e Cα-C (psi, ψ) que definem a conformação do esqueleto polipeptídico.
    *   **Gráfico de Ramachandran:** Um gráfico que mostra as combinações de ângulos phi e psi energeticamente permitidas. É uma ferramenta essencial para validar a qualidade estereoquímica de uma estrutura.
    *   **Termodinâmica do Dobramento (Funil de Enovelamento):** Um conceito que ilustra como uma proteína explora diversas conformações de alta energia até atingir seu estado nativo de menor energia.

3.  **Conceitos Estruturais e Funcionais:**
    *   **Domínios:** Regiões de uma proteína que se dobram de forma independente e frequentemente possuem uma função específica.
    *   **Motivos:** Padrões de estrutura secundária curtos e conservados (ex: hélice-alça-hélice).
    *   **Famílias de Proteínas:** Grupos de proteínas com ancestralidade evolutiva comum, geralmente compartilhando domínios e funções similares.

### Atividades Práticas e Ferramentas

- **Bancos de Dados Essenciais:**
  - **[UniProt](https://www.uniprot.org/):** O principal recurso para informações sobre sequências e funções de proteínas.
  - **[Protein Data Bank (PDB)](https://www.rcsb.org/):** O repositório mundial de estruturas 3D de macromoléculas biológicas.
  - **[InterProScan](https://www.ebi.ac.uk/interpro/):** Ferramenta que combina múltiplas bases de dados para classificar proteínas em famílias e prever domínios e sítios importantes.

- **Ferramentas de Análise (Portal [ExPASy](https://www.expasy.org/)):**
  - **[ProtParam](https://web.expasy.org/protparam/):** Calcula propriedades físico-químicas como peso molecular, ponto isoelétrico (pI), e composição de aminoácidos a partir de uma sequência.

---

## Módulo 2: Técnicas Clássicas de Modelagem Molecular (2 horas)

Aqui, mergulhamos no método mais tradicional de predição de estrutura: a modelagem por homologia, que se baseia no princípio de que proteínas com sequências semelhantes têm estruturas semelhantes.

### Conteúdo Programático Detalhado

1.  **Identidade vs. Similaridade:**
    *   **Identidade:** A porcentagem de resíduos idênticos entre duas sequências.
    *   **Similaridade:** Considera também resíduos com propriedades físico-químicas parecidas. A modelagem por homologia é mais confiável com identidade de sequência acima de 30%.

2.  **Modelagem por Homologia (Comparativa):**
    *   **Passo 1: Identificação de Templates:** Usar ferramentas como o [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi) para procurar no PDB por estruturas resolvidas (templates) que sejam homólogas à nossa proteína-alvo (query).
    *   **Passo 2: Alinhamento Sequência-Molde:** Alinhar a sequência do alvo com a do molde.
    *   **Passo 3: Construção do Modelo:** Copiar as coordenadas dos resíduos conservados do molde para o alvo e modelar as regiões não conservadas.
    *   **Passo 4: Refino e Validação:** Corrigir possíveis erros estereoquímicos e avaliar a qualidade global do modelo.

3.  **Outros Métodos Clássicos:**
    *   **Threading:** Tenta "encaixar" a sequência alvo em uma biblioteca de dobras estruturais conhecidas.
    *   ***Ab Initio:*** Tenta prever a estrutura a partir de princípios físico-químicos, sem usar um template.

### Atividades Práticas e Ferramentas

- **Servidor Web:**
  - **[SWISS-MODEL](https://swissmodel.expasy.org/):** Plataforma automatizada para modelagem por homologia.

- **Análise do Modelo:**
  - **Validação:** Análise do Gráfico de Ramachandran e escores de qualidade como QMEAN e Z-score.

---

## Módulo 3: A Revolução do Aprendizado de Máquina (2 horas)

Este módulo aborda como o Deep Learning transformou a predição de estruturas, alcançando precisão comparável à de métodos experimentais.

### Comparativo de Ferramentas de Aprendizado de Máquina

| Ferramenta | Descrição | Aplicação | Destaques | Link |
|:---|:---|:---|:---|:---|
| AlphaFold 2 (canônico) | Predição altamente precisa de estruturas individuais de proteínas utilizando redes neurais profundas e MSAs. | Predição de estruturas monoméricas. | Alta precisão, pLDDT confiável. | [Artigo](https://www.nature.com/articles/s41586-021-03819-2) |
| AlphaFold-Multimer | Extensão do AlphaFold 2 para prever estruturas de complexos proteicos (multímeros). | Predição de complexos proteína-proteína. | Predição multímera, avaliação de interação. | [Artigo](https://www.nature.com/articles/s41467-021-24462-3) |
| AlphaFold 3 | Versão mais recente com melhorias em rapidez e precisão. | Predição de estruturas monoméricas e multímeras. | Melhorias em escala e eficiência. | [Site oficial](https://alphafold.ebi.ac.uk/) |
| RoseTTAFold | Modelo baseado em rede neural que integra sequência, estrutura e informação de contato. | Predição estrutural, incluindo multímeros. | Bom balanceamento entre precisão e velocidade. | [Site oficial](https://robetta.bakerlab.org/) |
| ESM-Complex (ESM-C) | Modelo baseado em linguagem de proteínas para predição de interações e estruturas de complexos. | Predição de interações proteína-proteína usando embeddings de linguagem. | Método inovador usando aprendizado de linguagem de proteínas. | [Site oficial](https://esmatlas.com/complex) |

### Interpretação das Métricas de Confiança
- **pLDDT (predicted Local Distance Difference Test):** Métrica por resíduo (0-100) que indica a confiança na predição da estrutura local.
- **PAE (Predicted Aligned Error):** Avalia a confiança na orientação relativa dos domínios.

### Atividades Práticas
- Submissão de uma sequência para predição estrutural no AlphaFold.
- Comparação direta do modelo gerado pelo AlphaFold com o obtido por homologia no Módulo 2.

---

## Módulo 4: Análise e Validação Estrutural (2 horas)

Com os modelos em mãos, o passo final é analisá-los, validá-los em profundidade e extrair insights biológicos.

### Conteúdo Programático Detalhado
1.  **Visualização Molecular:** Representações (cartoon, sticks), coloração e renderização.
2.  **Validação Avançada:** Análise da qualidade estereoquímica, empacotamento e energia.
3.  **Análise de Propriedades 3D:** Mapas de potencial eletrostático, hidrofobicidade e identificação de cavidades.

### Atividades Práticas e Ferramentas

**Requisito:** Instalar previamente o [PyMOL](https://pymol.org/2/) ou o [VMD](https://www.ks.uiuc.edu/Research/vmd/).

- **Softwares de Visualização:** Uso de PyMOL/VMD para carregar, alinhar e gerar imagens de alta qualidade.
- **Servidores de Validação:**
  - **[SAVES](https://saves.mbi.ucla.edu/):** Portal que integra ferramentas como PROCHECK e ERRAT.
  - **[MolProbity](http://molprobity.biochem.duke.edu/):** Ferramenta para validação focada em clashes atômicos e geometria.

---

## Leituras Fundamentais e Artigos de Impacto

Para aprofundar o conhecimento, esta seção reúne artigos científicos cruciais que servem de base para os tópicos abordados no curso.

| title | author | year | summary | link |
|:---|:---|---:|:---|:---|
| Recent advances in deep learning for protein-protein interaction | Jiafu Cui et al. | 2025 | Uma revisão abrangente dos avanços recentes em deep learning aplicados à predição de interações proteína-proteína, incluindo o uso de GNNs, CNNs, RNNs, Transformers e aprendizado multitarefa. | https://pmc.ncbi.nlm.nih.gov/articles/PMC12168265/ |
| Highly accurate protein structure prediction with AlphaFold | John Jumper et al. | 2021 | O estudo seminal que demonstrou o sucesso do AlphaFold na predição estrutural precisa de proteínas, revolucionando o campo da bioinformática estrutural. | https://www.nature.com/articles/s41586-021-03819-2 |
| Deep learning techniques have significantly impacted protein structure prediction and protein design | Robin Pearce et al. | 2021 | Revisão dos impactos significativos do deep learning na predição e design de estruturas proteicas com destaques para abordagens recentes. | https://pmc.ncbi.nlm.nih.gov/articles/PMC8222070/ |


# Bits, Bytes e Biomoléculas: Introdução à Modelagem de Proteínas com Métodos Clássicos e de Aprendizado de Máquina

**Instrutor:** Madson Aragão (Estudante de PhD @ UFMG, MSc em Genética e Biologia Molecular @ UFPE)

**Monitor:** Saulo Penna (BSc em Biomedicina @ UFPE, Pesquisador no LGBV/UFPE)

**Evento:** XV Jornada PPGGBM - 19 de Novembro de 2025

**Contato:** madsondeluna@gmail.com

**Portfólio:** <a href="https://madsondeluna.github.io/" target="_blank" rel="noopener noreferrer">https://madsondeluna.github.io/</a>

**Códigos/Projetos:** <a href="https://github.com/madsondeluna" target="_blank" rel="noopener noreferrer">https://github.com/madsondeluna</a>

> Este repositório contém o material de referência completo para o curso, incluindo conceitos fundamentais, guias de ferramentas e leituras recomendadas. Qualquer sugestão ou feedback pode ser enc[...] 

---

## Sumário

- [O Desafio Central: O Enovelamento de Proteínas](#o-desafio-central-o-enovelamento-de-proteínas)
  - [A Paisagem Energética: O Funil de Enovelamento](#a-paisagem-energética-o-funil-de-enovelamento)
  - [A Lógica da Energia em Bioquímica](#a-lógica-da-energia-em-bioquímica)
  - [O Paradoxo de Levinthal](#o-paradoxo-de-levinthal)
- [Módulo 1: Fundamentos da Sequência e Estrutura Proteica](#módulo-1-fundamentos-da-sequência-e-estrutura-proteica)
  - [Estrutura Secundária: Os Pilares da Arquitetura Proteica](#estrutura-secundária-os-pilares-da-arquitetura-proteica)
  - [α-Hélice: Um Fóssil Estrutural](#α-hélice-um-fóssil-estrutural)
  - [Everything in its Right Place? Talvez o Radiohead estivesse certo esse tempo todos!](#everything-in-its-right-place-talvez-o-radiohead-estivesse-certo-esse-tempo-todos)
  - [O Repertório Pré-biótico e Propensões Conformacionais](#o-repertório-pré-biótico-e-propensões-conformacionais)
  - [Estabilidade Termodinâmica](#estabilidade-termodinâmica)
  - [A Interface Peptídeo-Membrana](#a-interface-peptídeo-membrana)
  - [Síntese e Análise Contemporânea](#síntese-e-análise-contemporânea)
  - [Motivos Supersecundários e Domínios Proteicos](#motivos-supersecundários-e-domínios-proteicos)
  - [Propriedades dos Aminoácidos Canônicos](#propriedades-dos-aminoácidos-canônicos)
  - [Interações Intermoleculares Estabilizadoras](#interações-intermoleculares-estabilizadoras)
  - [Ferramentas e Bancos de Dados Essenciais](#ferramentas-e-bancos-de-dados-essenciais)
- [Módulo 2: Técnicas Clássicas de Modelagem Molecular](#módulo-2-técnicas-clássicas-de-modelagem-molecular)
  - [Uma Nota Crucial: Identidade vs. Similaridade de Sequência](#uma-nota-crucial-identidade-vs-similaridade-de-sequência)
  - [1. Modelagem por Homologia (Modelagem Comparativa)](#1-modelagem-por-homologia-modelagem-comparativa)
  - [2. Threading (Reconhecimento de Dobra)](#2-threading-reconhecimento-de-dobra)
  - [3. Modelagem Ab Initio](#3-modelagem-ab-initio)
- [Módulo 3: A Revolução do Aprendizado de Máquina e a Nova Era da Biologia Estrutural](#módulo-3-a-revolução-do-aprendizado-de-máquina-e-a-nova-era-da-biologia-estrutural)
  - [Contexto Histórico: A Longa Estrada do CASP e a Promessa do AlphaFold 1](#contexto-histórico-a-longa-estrada-do-casp-e-a-promessa-do-alphafold-1)
  - [O Ponto de Inflexão: AlphaFold 2 e o "Problema Resolvido? Nem tanto"](#o-ponto-de-inflexão-alphafold-2-e-o-problema-resolvido-nem-tanto)
  - [A Próxima Geração: AlphaFold 3 e o Paradoxo do Código Fechado](#a-próxima-geração-alphafold-3-e-o-paradoxo-do-código-fechado)
  - [Comparativo de Ferramentas de Aprendizado de Máquina](#comparativo-de-ferramentas-de-aprendizado-de-máquina)
- [Métodos Clássicos vs. Métodos de ML/DL? Quando usar?](#métodos-clássicos-vs-métodos-de-mldl-quando-usar)
  - [Extra 1: Estudando a Dinâmica e Variações Estruturais](#extra-1-estudando-a-dinâmica-e-variações-estruturais)
  - [Extra 2: Modelagem de Sítios Ativos com Ligantes e Cofatores](#extra-2-modelagem-de-sítios-ativos-com-ligantes-e-cofatores)
  - [Extra 3: Design de Proteínas (De Novo)](#extra-3-design-de-proteínas-de-novo)
  - [Extra 4: Velocidade, Acessibilidade e Recursos Computacionais](#extra-4-velocidade-acessibilidade-e-recursos-computacionais)
  - [Tabela Resumo: Quando Usar Qual Ferramenta?](#tabela-resumo-quando-usar-qual-ferramenta)
- [Módulo 4: Análise, Validação e Interpretação de Modelos Estruturais](#módulo-4-análise-validação-e-interpretação-de-modelos-estruturais)
  - [Ferramentas de Visualização Molecular](#ferramentas-de-visualização-molecular)
  - [Análise Comparativa: RMSD e sua Importância](#análise-comparativa-rmsd-e-sua-importância)
  - [Servidores de Validação de Estrutura](#servidores-de-validação-de-estrutura)
  - [Métricas Chave de Validação Explicadas](#métricas-chave-de-validação-explicadas)
- [Referências e Leituras Recomendadas](#referências-e-leituras-recomendadas)

---

## O Desafio Central: O Enovelamento de Proteínas

O problema do enovelamento de proteínas — como uma cadeia polipeptídica linear atinge sua complexa e funcional estrutura tridimensional, representa um dos maiores desafios da biologia molecular contemporânea. Avanços notáveis, como o AlphaFold, forneceram soluções preditivas sem precedentes, mas a compreensão fundamental dos mecanismos de enovelamento, regidos pela termodinâmica e pela evolução, permanece um campo de intensa investigação para biólogos, físicos e químicos.

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

Para explorar a diversidade de dobras, utilizamos bancos de dados como o **CATH (Class, Architecture, Topology, Homologous superfamily)**. O CATH organiza as estruturas em uma hierarquia que nos ajuda a entender as relações evolutivas entre as proteínas. Fica a sugestão de **[Explorar o CATH](https://www.cathdb.info/ "Abrir em nova aba")**!

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

As mais comuns são: **[UniProt](https://www.uniprot.org/ "Abrir em nova aba")**, **[PDB](https://www.rcsb.org/ "Abrir em nova aba")**, **[InterProScan](https://www.ebi.ac.uk/interpro/ "Abrir em nova aba")**, **[ExPASy ProtParam](https://web.expasy.org/protparam/ "Abrir em nova aba")**, mas não se limitam a essas.

---

## Módulo 2: Técnicas Clássicas de Modelagem Molecular

Neste módulo, exploramos os três pilares da modelagem de proteínas pré-Deep Learning. Embora ferramentas como o AlphaFold tenham revolucionado a predição de estruturas, os métodos clássicos continuam sendo indispensáveis para cenários específicos, oferecendo controle e abordagens que ainda não são o foco principal das novas tecnologias.

### Uma Nota Crucial: Identidade vs. Similaridade de Sequência

Antes de mergulharmos nos métodos, é essencial entender a diferença entre dois termos frequentemente confundidos: **identidade** e **similaridade**. A precisão da modelagem por homologia depende diretamente desses conceitos.

*   **Identidade de Sequência:** Refere-se à porcentagem de resíduos de aminoácidos que são **exatamente os mesmos** em posições correspondentes de um alinhamento. É uma contagem direta e rigorosa.

*   **Similaridade de Sequência:** É uma medida mais abrangente. Ela inclui os resíduos idênticos **mais** aqueles que, embora não sejam iguais, compartilham **propriedades físico-químicas semelhantes** (ex: tamanho, carga, polaridade). Uma substituição de Leucina (L) por Isoleucina (I), ambos aminoácidos grandes e hidrofóbicos, é um exemplo de substituição "conservativa" que conta como similaridade. Biologicamente, essas trocas têm menor probabilidade de perturbar a estrutura e a função da proteína.

**Exemplo Prático:**

Vamos analisar o seguinte alinhamento entre duas sequências curtas:

```
SeqA: V L I K G A T D
Alinh: | + | + | | +
SeqB: V I I R G A W E
```


*   **Identidades (`|`):** As posições com `V`, `I`, `G`, `A` são idênticas.
    *   **Cálculo:** 4 resíduos idênticos de um total de 8.
    *   **Identidade = (4 / 8) * 100 = 50%**

*   **Similaridades (`+`):** Além das identidades, temos substituições conservativas:
    *   `L` e `I` (ambos hidrofóbicos).
    *   `K` e `R` (ambos com carga positiva).
    *   `D` e `E` (ambos com carga negativa).
    *   **Cálculo:** 4 resíduos idênticos + 3 resíduos similares = 7.
    *   **Similaridade = (7 / 8) * 100 = 87.5%**

Note que a substituição de `T` (polar) por `W` (apolar e grande) não é considerada similar neste contexto.

**Conclusão:** A porcentagem de **similaridade** é sempre maior ou igual à de **identidade**. Para a modelagem por homologia, uma alta similaridade (>50%), mesmo com uma identidade mais baixa (~30%), já pode ser um forte indicativo de que as proteínas compartilham a mesma dobra estrutural.

---

### 1. Modelagem por Homologia (Modelagem Comparativa)

A modelagem por homologia parte de um princípio evolutivo fundamental: se duas proteínas compartilham uma sequência de aminoácidos similar, elas provavelmente terão estruturas tridimensionais muito parecidas.

*   **Como Funciona:** O processo busca por proteínas homólogas com estruturas já resolvidas experimentalmente (por cristalografia de raios-X, NMR, etc.), que servirão como "moldes" ou **templates**. A sequência da sua proteína-alvo é então alinhada com a do template, e um modelo 3D é construído transferindo as coordenadas dos átomos da estrutura conhecida para a sequência alvo. As regiões que não se alinham bem, como loops, são modeladas separadamente.

| Vantagens (Prós) | Desvantagens (Contras) |
| :--- | :--- |
| Alta precisão com bons templates (>30% de identidade). | A qualidade depende totalmente da qualidade do template. |
| Rápido e computacionalmente leve. | Incapaz de prever dobras proteicas novas. |
| Excelente para modelar mutações e estudar famílias de proteínas. | Erros no template são propagados para o modelo. |

*   **Aplicação Principal:** É o método mais preciso e confiável quando existe um bom template disponível. Ideal para modelar o efeito de pequenas mutações (SNPs), gerar estruturas de proteínas de espécies próximas e estudar famílias de proteínas com um ancestral comum bem caracterizado.
*   **Servidor Principal:** **[SWISS-MODEL](https://swissmodel.expasy.org/)** é um servidor web automatizado excelente, que escolhe o melhor template, constrói o modelo e realiza uma minimização de energia para otimizar a geometria.

### 2. Threading (Reconhecimento de Dobra)

E se não houver um homólogo com sequência similar? O Threading entra em cena. Ele se baseia na observação de que o número total de dobras (folds) proteicos existentes na natureza é limitado. O objetivo do Threading não é alinhar sequências, mas sim verificar se uma sequência de aminoácidos é compatível com uma dobra estrutural já conhecida.

*   **Como Funciona:** O algoritmo "passa" (threads) a sequência alvo por uma biblioteca de dobras proteicas conhecidas. Para cada dobra, ele calcula uma pontuação de energia (um *score*) que avalia o quão bem a sequência "se encaixa" naquela estrutura 3D. A dobra que resultar na menor energia é a mais provável.

| Vantagens (Prós) | Desvantagens (Contras) |
| :--- | :--- |
| Pode identificar a dobra correta mesmo com baixa identidade de sequência. | Dependente de uma biblioteca de dobras conhecidas; não prevê novas. |
| Útil para detectar relações de homologia remota. | O alinhamento sequência-estrutura pode ser impreciso. |
| Mais poderoso que a homologia quando não há templates óbvios. | A qualidade do modelo final pode ser variável. |

*   **Aplicação Principal:** Útil para proteínas que não possuem homólogos de sequência detectáveis, mas que podem compartilhar uma dobra estrutural com uma proteína de função completamente diferente.
*   **Servidor Principal:** O **[I-TASSER](https://zhanggroup.org/I-TASSER/)** é um dos serviços mais famosos e bem-sucedidos. Ele é um método híbrido: primeiro, usa Threading para identificar possíveis templates e, em seguida, aplica técnicas de montagem de fragmentos para construir e refinar o modelo final.

### 3. Modelagem *Ab Initio*

Este é o "Santo Graal" da modelagem clássica: prever a estrutura de uma proteína a partir unicamente de sua sequência de aminoácidos, sem usar nenhum template. A ideia é simular o processo de enovelamento físico, buscando a conformação de menor energia livre.

*   **Como Funciona:** Algoritmos como o **Rosetta** exploram o vasto espaço conformacional de uma proteína. Ele utiliza uma biblioteca de pequenos fragmentos estruturais (de 3 a 9 resíduos) retirados de proteínas conhecidas e os monta de diferentes maneiras, usando um algoritmo de busca estocástica (como o Monte Carlo) para encontrar o arranjo de menor energia.

| Vantagens (Prós) | Desvantagens (Contras) |
| :--- | :--- |
| Única abordagem clássica capaz de prever dobras totalmente novas. | Extremamente caro e lento em termos computacionais. |
| Fundamental para o design de proteínas *de novo*. | Precisão geralmente inferior aos outros métodos. |
| Não depende de nenhum template estrutural. | Limitado a proteínas relativamente pequenas (geralmente <150 resíduos). |

*   **TOP-7 e o Nobel de 2024:** O poder do Rosetta não está apenas na predição, mas no design. Em 2003, o grupo de David Baker usou o Rosetta para projetar do zero a **Top7**, uma proteína com uma dobra jamais vista na natureza. Esse feito foi um marco e uma das contribuições que levaram ao **Prêmio Nobel de Química de 2024**.
*   **Aplicação Principal:** É a única abordagem clássica para prever estruturas de proteínas com **dobras completamente novas** e para o design de novas proteínas.

---

## Módulo 3: A Revolução do Aprendizado de Máquina e a Nova Era da Biologia Estrutural

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

Se os métodos clássicos foram a base da modelagem molecular por décadas, a chegada do aprendizado de máquina (Deep Learning) não foi apenas uma melhoria: foi um evento transformador que redefiniu os limites do que é possível na biologia estrutural computacional.

### Contexto Histórico: A Longa Estrada do CASP e a Promessa do AlphaFold 1

Por anos, a comunidade científica mediu o progresso na predição de estruturas através do **CASP (Critical Assessment of protein Structure Prediction)**, uma competição bienal onde grupos de pesquisa de todo o mundo tentavam prever estruturas de proteínas que haviam sido resolvidas experimentalmente, mas ainda não publicadas. Por muito tempo, o progresso foi incremental.

Em 2018, no CASP13, a DeepMind (uma subsidiária da Google) apresentou o **AlphaFold 1**. Ele superou significativamente todos os outros competidores, demonstrando que redes neurais profundas podiam analisar padrões co-evolutivos em alinhamentos de múltiplas sequências (MSAs) para prever distâncias entre resíduos com uma precisão inédita. Embora ainda não atingisse qualidade experimental, o AlphaFold 1 foi a prova de conceito fundamental: o Deep Learning era o caminho a seguir. Ele preparou o terreno para a verdadeira revolução que estava por vir.

### O Ponto de Inflexão: AlphaFold 2 e o "Problema Resolvido? Nem tanto"

No CASP14 em 2020, o **AlphaFold 2** foi apresentado, e os resultados chocaram a comunidade científica. O novo modelo alcançou uma precisão mediana de GDT_TS de 92.4, um score onde 100 representa um encaixe perfeito com a estrutura experimental. Pela primeira vez, um método computacional conseguia, em muitos casos, gerar modelos com precisão comparável à de técnicas experimentais como a cristalografia de raios-X. A revista *Nature* declarou que ele havia "resolvido" o problema do enovelamento de proteínas, um desafio de 50 anos.

O impacto do AlphaFold 2 foi amplificado por uma decisão crucial da DeepMind: **tornar o código-fonte e os pesos do modelo totalmente abertos**. Isso desencadeou uma explosão de inovação. Pesquisadores de todo o mundo puderam não apenas usar a ferramenta, mas também dissecá-la, entendê-la e criar novas ferramentas inspiradas em seus módulos, como o **RoseTTAFold** e o **ESMFold**. O AlphaFold 2 democratizou a predição de alta precisão e mudou para sempre a forma como biólogos moleculares abordam seus sistemas de estudo.

### A Próxima Geração: AlphaFold 3 e o Paradoxo do Código Fechado 

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

> Críticas científicas significativas foram direcionadas à publicação do AlphaFold 3 na revista Nature, principalmente devido à falta de transparência e ao acesso restrito ao código-fonte do modelo. Os críticos argumentam que isso viola os princípios da ciência aberta, dificultando a verificação independente, a reprodutibilidade e a realização de pesquisas em larga escala pela comunidade científica em geral. Isso levou pesquisadores a desenvolverem alternativas. <a href="https://www.science.org/content/article/limits-access-deepmind-s-new-protein-program-trigger-backlash" target="_blank">Limits on access to DeepMind’s new protein program trigger backlash.</a>

Em 2024, a DeepMind e a Isomorphic Labs lançaram o **AlphaFold 3**. A nova versão representa outro salto monumental, expandindo suas capacidades para muito além de proteínas isoladas. Suas principais melhorias incluem:
*   **Maior Acurácia:** Predições ainda mais precisas para estruturas proteicas.
*   **Modelagem de Interações Universais:** Capacidade de modelar complexos contendo **DNA, RNA, ligantes, íons e lipídios**, transformando-o de um preditor de dobras para um preditor de interações moleculares.
*   **Predição de Multímeros:** Modelagem precisa de complexos homo e hetero-multiméricos.

No entanto, a chegada do AlphaFold 3 veio com uma mudança de filosofia drástica: **ele não é open source**. Embora um servidor web permita o uso para pesquisa não-comercial, a comunidade não tem acesso ao código-fonte. Isso impede que outros grupos de pesquisa aprendam com seus avanços arquitetônicos e criem ferramentas derivadas, como aconteceu com o AlphaFold 2. Essa decisão limita o ritmo da inovação comunitária e centraliza o poder de predição em uma única ferramenta "caixa-preta", marcando um contraste acentuado com a era de colaboração aberta inaugurada por seu predecessor.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Comparativo de Ferramentas de Aprendizado de Máquina
| Ferramenta | Descrição | Aplicação Principal | Referência |
|:---|:---|:---|:---|
| **AlphaFold 2** | Modelo revolucionário que usa MSAs e uma arquitetura baseada em atenção para prever estruturas monoméricas com precisão quase experimental. **(Open Source)** | Predição de alta precisão de estruturas de proteínas monoméricas. | <a href="https://www.nature.com/articles/s41586-021-03819-2" target="_blank">Artigo Nature (2021)</a> |
| **AlphaFold-Multimer** | Extensão do AlphaFold 2, otimizada para prever a estrutura de complexos proteicos. **(Open Source)** | Predição de interações e montagem de complexos proteína-proteína. | <a href="https://www.biorxiv.org/content/10.1101/2021.10.04.463034v1" target="_blank">Preprint bioRxiv (2021)</a> |
| **AlphaFold 3** | Modelo de última geração que prevê a estrutura de complexos envolvendo proteínas, ácidos nucleicos, íons e ligantes. **(Código Fechado)** | Modelagem de sistemas biomoleculares complexos e interações. | <a href="https://www.nature.com/articles/s41586-024-07487-w" target="_blank">Artigo Nature (2024)</a> |
| **RoseTTAFold** | Desenvolvido pelo Baker Lab, foi a primeira ferramenta a "mimetizar" com sucesso a arquitetura geral do AlphaFold 2, validando seus princípios. **(Open Source)** | Predição estrutural de monômeros e multímeros. | <a href="https://robetta.bakerlab.org/" target="_blank">Servidor Robetta</a> |
| **ESMFold** | Abordagem que dispensa MSAs, usando um modelo de linguagem de proteína (ESM-2) para prever estruturas muito mais rapidamente. **(Open Source)** | Predição ultrarrápida de estruturas, ideal para metagenômica. | <a href="https://esmatlas.com/about#esmf" target="_blank">Sobre o ESMFold</a> |
| **ESM Atlas** | Vasto banco de dados com centenas de milhões de estruturas previstas pelo ESMFold, cobrindo o espaço de proteínas metagenômicas. | Exploração de estruturas em escala metagenômica e busca por homólogos estruturais. | <a href="https://esmatlas.com/" target="_blank">Site Oficial</a> |
| **ESM Cambrian** | Modelo de linguagem de próxima geração da família ESM, com maior acurácia e capacidade de generalização. **(Acesso limitado)** | Geração de modelos e predição de estruturas e interações complexas. | <a href="https://www.biorxiv.org/content/10.1101/2024.06.11.598687v1" target="_blank">Preprint bioRxiv (2024)</a> |

---

## Métodos Clássicos vs. Métodos de ML/DL? Quando usar?

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Extra 1: Estudando a Dinâmica e Variações Estruturais

O AlphaFold é treinado para prever a conformação de mais baixa energia de uma proteína, resultando em uma estrutura estática de alta confiança. No entanto, a função biológica frequentemente reside na dinâmica e na capacidade da proteína de assumir múltiplos estados.

#### Extra 1.1: Modelagem de Mutações Pontuais

Se você já possui uma estrutura experimental de alta resolução (ex: PDB) e quer entender o impacto de uma pequena mutação, a **modelagem por homologia** usando a estrutura original como template é ideal. Este método preserva a integridade da estrutura experimental e foca apenas na alteração local, oferecendo um controle fino que o AlphaFold (que reconstrói tudo do zero) não fornece.

#### Extra 1.2: Estudo de Diferentes Estados Conformacionais

Muitas proteínas funcionam alternando entre estados (ex: um canal iônico "aberto" vs. "fechado"). Se você possui templates experimentais para esses múltiplos estados, pode usar a **modelagem por homologia** para gerar modelos da sua proteína em cada uma dessas conformações relevantes. O AlphaFold geralmente fornecerá apenas uma delas, não necessariamente a que você deseja estudar.

### Extra 2: Modelagem de Sítios Ativos com Ligantes e Cofatores

Historicamente, esta era uma grande vantagem dos métodos clássicos. O cenário mudou com o AlphaFold 3, mas a nuance é importante.

*   **Cenário Pré-AlphaFold 3:** Ferramentas como **SWISS-MODEL** se destacam por sua capacidade de transferir automaticamente ligantes, íons e cofatores do template para o modelo final. Isso é crucial para estudos de sítios ativos e docking molecular.

*   **Cenário Pós-AlphaFold 3:** O **AlphaFold 3** agora pode prever interações com ligantes, DNA e RNA. No entanto, a modelagem por homologia ainda é extremamente valiosa quando se parte de um template com um ligante já co-cristalizado. A transferência direta das coordenadas do ligante garante uma posição de partida quimicamente e estruturalmente validada, o que pode ser mais confiável do que uma predição *de novo*.

### Extra 3: Design de Proteínas (*De Novo*)

Aqui a distinção é fundamental: predição vs. criação.

*   **AlphaFold** é um modelo **preditivo**: ele foi treinado com milhões de exemplos da natureza para prever como uma sequência *dada* irá se enovelar.
*   **Rosetta** (base da modelagem *ab initio*) é um modelo **generativo**: ele usa princípios físicos para construir e avaliar estruturas que podem nunca ter existido na natureza. Por isso, Rosetta e ferramentas similares são o padrão-ouro para o design de novas proteínas com funções inéditas, um feito que contribuiu para o Prêmio Nobel de Química de 2024.

> Alguns autores sugerem validar os modelos teóricos (como os gerados por Rosetta e AlphaFold) comparando-os com dados experimentais. No entanto, é fundamental distinguir as diferentes escalas de validação, custo e limitações das técnicas: O Dicroísmo Circular (CD) se enquadra na validação de baixa resolução e baixo custo. Ele é usado para estimar o conteúdo de estrutura secundária (ex: o percentual de alfa-hélices e folhas-beta) e avaliar o enovelamento global ou a estabilidade térmica. O CD *não* possui uma limitação de tamanho (massa molecular) severa; é possível obter espectros de proteínas muito grandes (ex: >150 kDa), mas o sinal resultante será uma média de toda a estrutura. Em contrapartida, a Ressonância Magnética Nuclear (RMN) é um método de validação de alta resolução e alto custo, frequentemente exigindo marcação isotópica (<sup>15</sup>N, <sup>13</sup>C). Ela pode fornecer dados em nível atômico (ex: NOEs) para uma validação precisa do modelo. A RMN é *fortemente* limitada pelo tamanho da proteína; o limite prático rotineiro para a determinação estrutural ou atribuição de resíduos é de aproximadamente **30-40 kDa**. Acima desse limite, o tempo de relaxamento transversal (T<sub>2</sub>) diminui drasticamente, alargando os sinais a ponto de torná-los indetectáveis.

### Extra 4: Velocidade, Acessibilidade e Recursos Computacionais

Nem toda pergunta de pesquisa exige o poder (e o custo computacional) do AlphaFold.

*   Para uma consulta rápida, como obter um modelo de boa qualidade para uma proteína com um homólogo claro (>50% de identidade), um servidor web como o **SWISS-MODEL** é imbatível. Ele entrega um resultado em minutos e não requer nenhum hardware especializado. Em contraste, executar o AlphaFold localmente exige GPUs potentes e tempo considerável.

### Tabela Resumo: Quando Usar Qual Ferramenta?

| Cenário de Pesquisa | Método Clássico Recomendado | Método de Deep Learning Recomendado | Justificativa |
|:---|:---|:---|:---|
| **Análise de mutação pontual** (com estrutura *wild-type* conhecida) | Refinamento local / Mutagênese *in silico* (ex: FoldX, Rosetta ddG) | AlphaFold 2 (para re-predição) | Ferramentas clássicas avaliam o impacto energético ($\Delta\Delta G$); AF2 pode prever a estrutura do mutante para comparação. |
| **Predição de um novo fold** (sem homólogos) | Modelagem *Ab Initio* (Rosetta) | **AlphaFold 2/3** | AlphaFold é ordens de magnitude mais preciso; *Ab initio* é usado se o design é o objetivo. |
| **Modelagem com ligantes** (com template co-cristalizado) | Modelagem por Homologia (SWISS-MODEL) | **AlphaFold 3** | Homologia permite transferência direta e validada do ligante; AF3 prevê a interação do zero. |
| **Estudo de múltiplos estados conformacionais** | Modelagem por Homologia (com múltiplos templates) | N/A (ou amostragem de AF2) | Permite gerar modelos para cada estado funcional específico capturado nos templates. |
| **Design de proteínas *de novo*** | **Modelagem *Ab Initio* (Rosetta)** | N/A (Foco em predição) | Ferramentas como Rosetta são projetadas para criar novas estruturas, não apenas prever as existentes. |
| **Modelagem rápida e exploratória** (com bom template) | **Modelagem por Homologia (SWISS-MODEL)** | ESMFold | SWISS-MODEL é extremamente rápido e preciso neste cenário; ESMFold é a alternativa de DL mais veloz. |

> Vale ressaltar que, para qualquer modelo teórico gerado, simulações de dinâmica molecular (MD) são frequentemente recomendadas para validar a estabilidade estrutural, analisar a dinâmica e refinar as interações em solução.

---

## Módulo 4: Análise, Validação e Interpretação de Modelos Estruturais

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Ferramentas de Visualização Molecular
*   **[PyMOL](https://pymol.org/2/ "Download PyMOL")**: Padrão para geração de figuras de alta qualidade.
*   **[VMD](https://www.ks.uiuc.edu/Research/vmd/ "Download VMD")**: Excelente para análise de trajetórias de dinâmica molecular.
*   **[ChimeraX](https://www.cgl.ucsf.edu/chimerax/ "Download ChimeraX")**: Poderoso e extensível, com ótima integração com bancos de dados.

### Análise Comparativa: RMSD e sua Importância

O **Root Mean Square Deviation (RMSD)** quantifica a diferença média entre as posições dos átomos correspondentes em duas estruturas alinhadas. A fórmula é:

$$
RMSD = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} \delta_i^2 }
$$

onde $N$ é o número de átomos e $\delta_i$ é a distância entre o átomo *i* em cada estrutura.

É crucial em:
*   **Dinâmica Molecular:** Para avaliar a estabilidade de uma simulação (um RMSD baixo e estável indica que a proteína não está se "desfazendo").
*   **Docking Molecular:** Para validar um protocolo (re-docking) e avaliar a similaridade entre poses de ligantes geradas.

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

### Servidores de Validação de Estrutura

| Servidor | Descrição Detalhada |
|:---|:---|
| **[SAVES](https://saves.mbi.ucla.edu/ "Abrir em nova aba")** | Um meta-servidor que executa um conjunto de ferramentas clássicas de validação. As principais incluem: **PROCHECK** (análise estereoquímica e Gráfico de Ramachandran), **ERRAT** (analisa estatísticas de interações atômicas não-ligadas), e **Verify3D** (avalia a compatibilidade do ambiente 3D de cada resíduo com sua sequência). |
| **[MolProbity](http://molprobity.biochem.duke.edu/ "Abrir em nova aba")** | Focado intensamente na geometria de "todos-os-átomos" (all-atom). É excelente para identificar problemas de alta resolução, como "clashes" estéricos (sobreposições), geometria incorreta de ligações/ângulos, e rotâmeros de cadeias laterais desfavoráveis (ex: "outliers" de C$\beta$ ou Ramachandran). |
| **[QMEANDisCo](https://swissmodel.expasy.org/qmean/ "Abrir em nova aba")** | Parte do pipeline SWISS-MODEL. Fornece o **QMEAN**, um "score de consenso" que avalia a qualidade global do modelo, e o **QMEANDisCo**, um score local (por resíduo) que estima a confiabilidade, indicando regiões problemáticas. |

---

### Métricas Chave de Validação Explicadas

Abaixo estão os conceitos por trás das principais métricas fornecidas por esses servidores:

#### 1. Gráfico de Ramachandran (PROCHECK / MolProbity)

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

O Gráfico de Ramachandran é a ferramenta fundamental para avaliar a qualidade estereoquímica da cadeia principal (backbone) de uma proteína.

* **Como Funciona:** Ele plota os ângulos de torção (diedros) $\phi$ (phi) e $\psi$ (psi) de cada resíduo da proteína. Devido a restrições estéricas (impedimento entre os átomos da cadeia principal e lateral), apenas certas combinações de $\phi$ e $\psi$ são energeticamente favoráveis.
* **Interpretação:**
    * **Regiões "Favorecidas" (Core):** As áreas mais densamente povoadas, correspondendo a conformações estáveis (ex: centros de $\alpha$-hélices e folhas-$\beta$). Um bom modelo deve ter >90% (idealmente >95%) dos resíduos aqui.
    * **Regiões "Permitidas" (Allowed):** Conformações menos ideais, mas ainda fisicamente possíveis.
    * **Regiões "Não Permitidas" (Disallowed/Outliers):** Conformações energeticamente muito desfavoráveis (causando "clashes" atômicos). Resíduos nestas regiões (exceto Glicina ou Prolina em posições específicas) são quase sempre erros de modelagem e devem ser inspecionados.

#### 2. Z-score (Ex: ProSA-web, parte do SAVES)

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

O Z-score (neste contexto, geralmente do ProSA) mede a qualidade global do modelo em termos de energia.

* **Como Funciona:** Ele utiliza um "potencial de conhecimento" (knowledge-based potential). A energia do modelo é calculada com base nas distâncias observadas entre pares de resíduos em um banco de dados de estruturas experimentais de alta resolução. O Z-score, então, compara a energia do *seu* modelo com a distribuição de energias de proteínas nativas de tamanho similar (obtidas por X-ray ou RMN).
* **Interpretação:**
    * O servidor mostra um gráfico com as distribuições de Z-scores para proteínas de X-ray (geralmente em azul) e RMN (em verde).
    * **Z-scores Negativos:** São melhores. Um Z-score que cai *dentro* da faixa observada para proteínas nativas de tamanho similar (ex: dentro da nuvem de pontos azul) sugere que o "fold" (enovelamento) global do modelo é plausível e semelhante ao de uma proteína real.
    * **Z-scores Positivos:** Indicam um modelo problemático, cuja energia é muito menos favorável do que a média das estruturas experimentais, sugerindo um enovelamento incorreto.

#### 3. QMEAN (QMEANDisCo)

[ADICIONAR IMAGEM EXPLICATIVA AQUI]

O QMEAN (Quality Model Energy ANalysis) é um "score de consenso" (ou *scoring function*) que combina múltiplas métricas diferentes para gerar uma única estimativa de qualidade global.

* **Como Funciona:** Em vez de focar em apenas um aspecto (como o Ramachandran) ou na energia de pares (como o ProSA), o QMEAN combina vários descritores estruturais e estatísticos. Estes incluem:
    1.  Potenciais de interação baseados em distância (nível de C$\beta$ e "all-atom").
    2.  Potenciais de torção ($\phi$/$\psi$).
    3.  Previsão de acessibilidade ao solvente.
* **Interpretação:**
    * **Global (QMEAN Score):** O score é normalizado para variar entre 0 e 1. Quanto mais próximo de 1, maior a qualidade e mais o modelo se assemelha a uma estrutura experimental de alta resolução. Um score > 0.6 ou 0.7 é geralmente considerado bom.
    * **Local (QMEANDisCo Score):** O servidor também fornece um gráfico que colore o modelo por resíduo, mostrando a "confiança" local (também de 0 a 1). Isso é extremamente útil para identificar quais partes específicas do modelo (ex: loops, ou um domínio) são menos confiáveis que o restante.
---

## Referências e Leituras Recomendadas

<sub>Pauling, L., Corey, R. B., & Branson, H. R. (1951). [The structure of proteins: Two hydrogen-bonded helical configurations of the polypeptide chain](https://www.pnas.org/doi/10.1073/pnas.37.4.205). *Proceedings of the National Academy of Sciences, 37(4)*, 205–211.</sub>

<sub>Miller, S. L. (1953). [A Production of Amino Acids Under Possible Primitive Earth Conditions](https://www.science.org/doi/10.1126/science.117.3046.528). *Science, 117(3046)*, 528–529.</sub>

<sub>Ramachandran, G. N., Ramakrishnan, C., & Sasisekharan, V. (1963). [Stereochemistry of polypeptide chain configurations](https://doi.org/10.1016/S0022-2836(63)80023-6). *Journal of Molecular Biology, 7*, 95–99.</sub>
<sub>Anfinsen, C. B. (1973). [Principles that govern the- folding of protein chains](https://www.science.org/doi/10.1126/science.181.4096.223). *Science, 181(4096)*, 223–230.</sub>

<sub>Šali, A., & Blundell, T. L. (1993). [Comparative protein modelling by satisfaction of spatial restraints](https://doi.org/10.1016/0022-2836(93)90134-Y). *Journal of Molecular Biology, 234(3)*, 779–815.</sub>

<sub>Kuhlman, B., Dantas, G., et al. (2003). [Design of a novel globular protein fold with atomic-level accuracy](https://www.science.org/doi/10.1126/science.1089427). *Science, 302(5649)*, 1364–1368.</sub>

<sub>Chen, V. B., Arendall, W. B., et al. (2010). [MolProbity: all-atom structure validation for macromolecular crystallography](https://doi.org/10.1107/S0907444909042073). *Acta Crystallographica Section D, 66(1)*, 12–21.</sub>
<sub>Dill, K. A., & MacCallum, J. L. (2012). [The Protein-Folding Problem, 50 Years On](https://www.science.org/doi/10.1126/science.1219021). *Science, 338(6110)*, 1042–1046.</sub>

<sub>[Nobel Prize in Chemistry 2013 - Popular Information](https://www.nobelprize.org/prizes/chemistry/2013/popular-information/) (Fundamentos da modelagem multiescala / Dinâmica Molecular)</sub>

<sub>Yang, J., et al. (2015). [The I-TASSER Suite: protein structure and function prediction](https://doi.org/10.1038/nmeth.3213). *Nature Methods, 12(1)*, 7–8.</sub>

<sub>Jumper, J. et al. (2021). [Highly accurate protein structure prediction with AlphaFold](https://doi.org/10.1038/s41586-021-03819-2). *Nature, 596(7873)*, 583–589.</sub>

<sub>Baek, M., DiMaio, F., et al. (2021). [Accurate prediction of protein structures and interactions using a three-track neural network](https://www.science.org/doi/10.1126/science.abj8754). *Science, 373(6557)*, 871–876.</sub>

<sub>[Nobel Prize in Chemistry 2024 - Popular Information](https://www.nobelprize.org/prizes/chemistry/2024/popular-information/) (Design computacional e predição de estrutura)</sub>

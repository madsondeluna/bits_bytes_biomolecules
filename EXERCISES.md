# Bits, Bytes e Biomoléculas - Exercícios Práticos

**Instrutor:** Madson Aragão (Estudante de PhD @ UFMG, MSc em Genética e Biologia Molecular @ UFPE)

**Monitor:** Saulo Penna (BSc em Biomedicina @ UFPE, Pesquisador no LGBV/UFPE)

**Evento:** XV Jornada PPGGBM - 19 de Novembro de 2025

**Contato:** madsondeluna@gmail.com; saulo.rmpenna@ufpe.br

**Portfólio:** <a href="https://madsondeluna.github.io/" target="_blank" rel="noopener noreferrer">https://madsondeluna.github.io/</a>

**Projetos:** <a href="https://github.com/madsondeluna" target="_blank" rel="noopener noreferrer">https://github.com/madsondeluna</a>

---

> **Proteína-Alvo:** p53 (Guardiã do Genoma)

Este repositório contém o material prático do curso de Biologia Estrutural Computacional, utilizando a proteína supressora de tumor p53 como sistema modelo para explorar diferentes métodos de predição e análise estrutural.

---

## Índice

- [Bits, Bytes e Biomoléculas - Exercícios Práticos](#bits-bytes-e-biomoléculas---exercícios-práticos)
  - [Índice](#índice)
  - [Sobre a Proteína p53](#sobre-a-proteína-p53)
    - [Relevância Científica](#relevância-científica)
    - [Dados de Referência](#dados-de-referência)
    - [Sequência FASTA](#sequência-fasta)
  - [🔧 Pré-requisitos](#-pré-requisitos)
    - [Software Local](#software-local)
    - [Software Online](#software-online)
    - [Requisitos do Sistema](#requisitos-do-sistema)
  - [Instalação do PyMOL](#instalação-do-pymol)
    - [A. Obtenção da Licença de Estudante (Gratuita)](#a-obtenção-da-licença-de-estudante-gratuita)
    - [B. Download e Instalação](#b-download-e-instalação)
    - [C. Ativação da Licença](#c-ativação-da-licença)
  - [Módulos Práticos](#módulos-práticos)
    - [Módulo 1: Análise de Sequências e Propriedades](#módulo-1-análise-de-sequências-e-propriedades)
      - [Bancos de Dados](#bancos-de-dados)
      - [Ferramentas de Predição](#ferramentas-de-predição)
    - [Módulo 2: Modelagem por Homologia e Threading](#módulo-2-modelagem-por-homologia-e-threading)
      - [Modelagem por Homologia](#modelagem-por-homologia)
      - [Modelagem por Threading/Ab Initio](#modelagem-por-threadingab-initio)
      - [Primeira Validação](#primeira-validação)
- [Perguntas:](#perguntas)
    - [Módulo 3: Predição por Deep Learning (AF2, AF3 e ESM)](#módulo-3-predição-por-deep-learning-af2-af3-e-esm)
      - [Plataformas de Deep Learning](#plataformas-de-deep-learning)
      - [Métricas de Confiança](#métricas-de-confiança)
    - [Módulo 4: Análise Comparativa, Validação e Visualização](#módulo-4-análise-comparativa-validação-e-visualização)
      - [Servidores de Validação de Dobramento e Termodinâmica](#servidores-de-validação-de-dobramento-e-termodinâmica)
      - [Análise Estrutural no PyMOL](#análise-estrutural-no-pymol)
  - [Referências Teórico (Atividades Práticas)](#referências-teórico-atividades-práticas)
    - [Bases de Dados](#bases-de-dados)
    - [Ferramentas de Predição](#ferramentas-de-predição-1)
    - [Modelagem Estrutural](#modelagem-estrutural)
    - [Validação](#validação)
    - [Visualização](#visualização)
  - [Licença](#licença)
  - [Recursos Úteis](#recursos-úteis)

---

## Sobre a Proteína p53

A **p53** (derivada do gene TP53) é um dos mais importantes supressores de tumor, frequentemente referida como **"a guardiã do genoma"**[web:6][web:9]. Esta proteína é crucial para a regulação do ciclo celular e prevenção do câncer[web:6].

### Relevância Científica

- Mutada em **mais de 50% de todos os cânceres humanos**[web:6]
- Proteína mais estudada na história da oncologia[web:6]
- Alvo ideal para comparar diferentes métodos de modelagem computacional[web:9]

### Dados de Referência

| Informação | Valor/Link |
|------------|------------|
| **ID UniProt** | [P04637](https://www.uniprot.org/uniprotkb/P04637/) |
| **PDB Experimental** | [1TUP](https://www.rcsb.org/structure/1tup) (Domínio central complexado com DNA) |
| **Massa Molecular** | ~43.7 kDa (aparece como 53 kDa em SDS-PAGE)[web:9] |
| **Domínios** | 7 domínios funcionais (TAD, AD2, PRD, DBD, NLS, OD, CTD)[web:6][web:9] |

### Sequência FASTA

```bash
sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens OX=9606 GN=TP53 PE=1 SV=4
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```


---

## 🔧 Pré-requisitos

### Software Local
- **PyMOL** (Incentive PyMOL - Licença Educacional Gratuita)[web:7][web:10]

### Software Online
Todos os demais passos utilizarão **servidores web** (não requerem instalação)[web:2].

### Requisitos do Sistema
- Acesso à internet
- E-mail institucional (.edu ou similar) para licença acadêmica[web:7]
- Sistema operacional: Windows, macOS ou Linux

---

## Instalação do PyMOL

O PyMOL é o único software que precisará ser instalado localmente para este curso. Utilizaremos a versão **Incentive PyMOL**, gratuita para estudantes e educadores.

### A. Obtenção da Licença de Estudante (Gratuita)

1. Acesse o portal educacional da Schrödinger: [https://pymol.org/edu/](https://pymol.org/edu/).
2. Clique em **"Register for an Account"**
3. **IMPORTANTE:** Utilize seu **e-mail institucional** (ex: `seu.usuario@ufpe.br`).
   - A licença acadêmica está vinculada à verificação de um domínio educacional
4. Siga as instruções de verificação enviadas ao seu e-mail
5. Após aprovação, faça o download do arquivo de licença (`license.lic`).
6. Salve o arquivo em um local de fácil acesso (ex: Área de Trabalho).

### B. Download e Instalação

Na página de downloads da sua conta Schrödinger, baixe o instalador apropriado para seu sistema operacional pelo site [https://pymol.org/edu/](https://pymol.org/edu/)


### C. Ativação da Licença

1. Inicie o PyMOL pela primeira vez.
2. O programa solicitará a ativação.
3. Escolha a opção **"I have a license file"**.
4. Navegue até o local do arquivo `license.lic` e selecione-o.
5. O PyMOL será ativado e estará pronto para uso.

---

## Módulos Práticos

### Módulo 1: Análise de Sequências e Propriedades

**Objetivos:**
- Navegar e extrair dados da p53 em bancos de dados estruturais.
- Utilizar ferramentas web para predição de características bioquímicas.

#### Bancos de Dados

| Recurso | URL | Descrição |
|---------|-----|-----------|
| **UniProt** | [https://www.uniprot.org/](https://www.uniprot.org/) | Informações de sequência e anotações funcionais |
| **PDB** | [https://www.rcsb.org/](https://www.rcsb.org/) | Estruturas tridimensionais experimentais |

#### Ferramentas de Predição

Utilize a sequência FASTA da p53 nas seguintes ferramentas.

```bash
sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens OX=9606 GN=TP53 PE=1 SV=4
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

| Ferramenta | URL | Função |
|------------|-----|---------|
| **ProtParam** | [https://web.expasy.org/protparam/](https://web.expasy.org/protparam/) | Parâmetros físico-químicos |
| **SignalP 6.0** | [https://services.healthtech.dtu.dk/services/SignalP-6.0/](https://services.healthtech.dtu.dk/services/SignalP-6.0/) | Predição de peptídeos de sinal |
| **InterProScan** | [https://www.ebi.ac.uk/interpro/search/sequence/](https://www.ebi.ac.uk/interpro/search/sequence/) | Identificação de domínios e famílias |
| **PROSITE** | [https://prosite.expasy.org/](https://prosite.expasy.org/) | Identificação de sítios funcionais |

> Agora vamos discutir os resultados obtidos e suas implicações biológicas? 

---

### Módulo 2: Modelagem por Homologia e Threading

**Objetivos:**
- Construir modelos da p53 utilizando diferentes abordagens.
- Analisar alinhamentos sequência-molde e métricas de confiança.

#### Modelagem por Homologia

**Plataforma:** SWISS-MODEL  
**URL:** [https://swissmodel.expasy.org/](https://swissmodel.expasy.org/)

**Análise:**
- Avaliar alinhamentos sequência-molde
- Examinar cobertura e identidade de sequência

#### Modelagem por Threading/Ab Initio

**Plataforma:** I-TASSER  
**URL:** [https://zhanggroup.org/I-TASSER/](https://zhanggroup.org/I-TASSER/)

**Métricas:**
- **C-score:** Confiança da predição (-5 a 2, valores mais altos = melhor)
- **TM-score:** Similaridade estrutural

#### Primeira Validação

# Perguntas:

- Qual seria o melhor modelo obtido entre SWISS-MODEL e I-TASSER? Justifique com base nas métricas apresentadas.
- O tipo de construção (homologia vs threading) influenciou a qualidade do modelo? Explique...
- Vamos revidar os métodos utilizados até aqui. Quais são as vantagens e limitações de cada abordagem?
- Ainda não alinhamos as estruturas obtidas até aqui, mas conseguem identificar diferenças visuais entre os modelos gerados?

> Nos próximos módulos, vamos avaliar se o dobramento por cada método foi feito da corretamente. Bem como alinhar estrturalmente os modelos obtidos, calculando RMSD para comparação detalhada.

---

### Módulo 3: Predição por Deep Learning (AF2, AF3 e ESM)

> Vamos discutir como esses modelos funcionam mais uma vez, focando em suas arquiteturas baseadas em aprendizado profundo?

**Objetivos:**
- Utilizar métodos de aprendizado profundo para predição estrutural.
- Interpretar métricas de confiança específicas (pLDDT, PAE).

> O **pLDDT (predicted Local Distance Difference Test)** é uma métrica de confiança por resíduo (0-100) que avalia a precisão da predição da estrutura *local* ao redor de cada aminoácido, sendo alta para regiões bem dobradas e baixa para regiões desordenadas.

> O **PAE (Predicted Aligned Error)** é uma métrica inter-resíduo (medida em Ångströms, $\AA$) que avalia a confiança na *orientação relativa* e global entre diferentes domínios ou pares de resíduos, indicando se a montagem 3D geral está correta.

> Em resumo, o pLDDT mede a confiança no dobramento *local* de um resíduo, enquanto o PAE mede a confiança na posição *global* desse resíduo em relação a todos os outros na estrutura.

#### Plataformas de Deep Learning

| Método | URL | Descrição |
|--------|-----|-----------|
| **ColabFold** | [AlphaFold2 Notebook](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb) | Baseado em AlphaFold2 (Google Colab) |
| **AlphaFold 3 Server** | [https://alphafoldserver.com/](https://alphafoldserver.com/) | Versão mais recente do AlphaFold |
| **ESMFold** | [https://esmatlas.com/resources](https://esmatlas.com/resources) | Baseado em Modelo de Linguagem de Proteína |

#### Métricas de Confiança

- **pLDDT** (predicted Local Distance Difference Test): 0-100, >90 = alta confiança
- **PAE** (Predicted Aligned Error): Confiança na posição relativa entre resíduos

---

### Módulo 4: Análise Comparativa, Validação e Visualização

> Tamos modelos gerados por homologia, threading e deep learning. Agora vamos baixar um modelos experimental da p53 para comparar todos os modelos gerados. Lembrando que a extrutura experimental sempre será o nosso padrão-ouro para comparação.

> Baixar a estrutura experimental da p53 (PDB ID: 1TUP) do RCSB PDB para servir como referência na comparação dos modelos preditos. Link: [https://www.rcsb.org/structure/1tup](https://www.rcsb.org/structure/1tup)

> Baixe a estrtura limpa e pronta para análise (sem água, ligantes ou íons) aqui: ADD LINK DO DRIVE 

**Objetivos:**
- Comparar todos os modelos gerados.
- Realizar análise estrutural comparativa no PyMOL.
- Quantificar diferenças estruturais via RMSD.

#### Servidores de Validação de Dobramento e Termodinâmica

| Servidor | URL | Métrica Avaliada |
|----------|-----|------------------|
| **MolProbity (SAVES)** | [https://saves.mbi.ucla.edu/](https://saves.mbi.ucla.edu/) | Gráfico de Ramachandran, geometria |
| **QMEAN** | [https://swissmodel.expasy.org/qmean/](https://swissmodel.expasy.org/qmean/) | Qualidade global |
| **ProSA-web** | [https://prosa.services.came.sbg.ac.at/prosa.php](https://prosa.services.came.sbg.ac.at/prosa.php) | Z-score (energia do enovelamento) |

#### Análise Estrutural no PyMOL

**Modelos para Comparação:**
- SWISS-MODEL (Homologia)
- I-TASSER (Threading)
- ColabFold (AlphaFold2)
- AlphaFold 3 Server
- ESMFold
- **1TUP** (Estrutura experimental de referência - X-ray)[web:6]

---

1. **Carregar estruturas**
  
- Abra o PyMOL e carregue todos os modelos preditos e a estrutura experimental fornecida.

2. **Cálculo de RMSD**
- Quantificar divergência estrutural de cada modelo vs. 1TUP[.
- Registrar valores de RMSD para comparação e discutir o que seria um valor aceitável de RMSD para modelos preditos.

4. **Inspeção visual**
- Identificar regiões de convergência (alta similaridade).
- Identificar regiões de divergência (loops, cadeias laterais).
- Destacar sítios ativos e domínio de ligação ao DNA.

5. **Geração de figuras**
- Criar representações ilustrativas das diferenças/similaridades.
- Destacar regiões de interesse estrutural.

---

## Referências Teórico (Atividades Práticas)

### Bases de Dados
- UniProt: [https://www.uniprot.org/](https://www.uniprot.org/)
- RCSB PDB: [https://www.rcsb.org/](https://www.rcsb.org/)

### Ferramentas de Predição
- ExPASy ProtParam
- SignalP 6.0
- InterProScan
- PROSITE

### Modelagem Estrutural
- SWISS-MODEL
- I-TASSER
- ColabFold
- AlphaFold 3 Server
- ESMFold

### Validação
- MolProbity/SAVES
- QMEAN
- ProSA-web

### Visualização
- PyMOL (Schrödinger)

---

## Licença

Material educacional - Uso acadêmico.

---

## Recursos Úteis

[README Principal](README.md)
[Repositório do Curso](https://github.com/madsondeluna/bits_bytes_biomolecules)
[Página Web do Curso](https://madsondeluna.github.io/bits_bytes_biomolecules/)


---

<br>

> Ninhuma dúvida é boba... Qualquer dúvida ou sugestão, sinta-se à vontade para entrar em contato conosco pelos e-mails fornecidos acima. Bom desemprenho e aproveitem os exercícios! 

<br>
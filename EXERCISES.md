# Bits, Bytes e Biomoléculas - Exercícios Práticos

**Instrutor:** Madson Aragão (Estudante de PhD @ UFMG, MSc em Genética e Biologia Molecular @ UFPE)

**Monitor:** Saulo Penna (BSc em Biomedicina @ UFPE, Pesquisador no LGBV/UFPE)

**Evento:** XV Jornada PPGGBM - 19 de Novembro de 2025

**Contato:** madsondeluna@gmail.com; saulo.rmpenna@ufpe.br

**Portfólio:** <a href="https://madsondeluna.github.io/" target="_blank" rel="noopener noreferrer">https://madsondeluna.github.io/</a>

**Projetos:** <a href="https://github.com/madsondeluna" target="_blank" rel="noopener noreferrer">https://github.com/madsondeluna</a>

---

 **Proteína-Alvo:** p53 (*TP53*))

Este repositório contém o material prático do curso de Biologia Estrutural Computacional, utilizando a proteína supressora de tumor p53 como sistema modelo para explorar diferentes métodos de predição e análise estrutural.

<figure class="figure-center">
  <img src="imgs/p53.png" alt="XXXXX" width="550">
</figure>

Eestrutura tridimensional da p53, em complexo com uma estrtura de DNA. As subunidades da p53, mostradas em azul e roxo, são visualizadas usando uma combinação de representação "cartoon", que revela a estrutura secundária de hélices alfa e fitas beta, e uma "superfície" molecular translúcida, que indica o volume de e a forma da proteína. A p53 é mostrada interagindo diretamente com a dupla hélice do DNA, representada em laranja, através de seu domínio de ligação ao DNA (DBD). A presença de esferas (íons de zinco, em verde) destaca componentes cruciais para a estabilidade estrutural do DBD, formando os zinc fingers. Esta interação é fundamental para a função da p53, permitindo que ela se ligue a regiões específicas do genoma para regular a expressão de genes envolvidos no controle do ciclo celular, no reparo de danos ao DNA e na indução da apoptose, prevenindo assim a oncogênese e assim, mantendo a homestase celular.

---

# Sobre a Proteína p53

A **p53** (derivada do gene *TP53*) é um dos mais importantes supressores de tumor, frequentemente referida como **"a guardiã do genoma"**. Esta proteína é crucial para a regulação do ciclo celular e prevenção do câncer.

### Relevância Científica

- Mutada em **mais de 50% de todos os cânceres humanos**
- Proteína mais estudada na história da oncologia.
- Alvo ideal para comparar diferentes métodos de modelagem computacional.

<figure class="figure-center">
  <img src="imgs/adobe.gif" alt="XXXXX" width="500">
</figure>

> Fonte: Criado por Madson Aragão no VMD.

### Dados de Referência

| Informação | Valor/Link |
|------------|------------|
| **ID UniProt** | <a href="https://www.uniprot.org/uniprotkb/P04637/" target="_blank">P04637 (WT)</a> |
| **PDB Experimental** | <a href="https://www.rcsb.org/structure/1tup" target="_blank">1TUP (DNA Binding Domain)</a> |
| **Massa Molecular** | ~43.7 kDa (aparece como 53 kDa em SDS-PAGE) |
| **Domínios** | 7 domínios funcionais (TAD, AD2, PRD, DBD, NLS, OD, CTD) |


## Pré-requisitos

### Software Local
- **PyMOL** (Incentive PyMOL - Licença Educacional Gratuita).

### Software Online
Todos os demais passos utilizarão **servidores web** (não requerem instalação).

### Requisitos do Sistema
- Acesso à internet
- E-mail institucional (.edu ou similar) para licença acadêmica.
- Sistema operacional: Windows, macOS ou Linux

---

## Instalação do PyMOL

O PyMOL é o único software que precisará ser instalado localmente para este curso. Utilizaremos a versão **Incentive PyMOL**, gratuita para estudantes e educadores.

### A. Obtenção da Licença de Estudante (Gratuita)

1. Acesse o portal educacional da Schrödinger: <a href="https://pymol.org/edu/" target="_blank">https://pymol.org/edu/</a>.
2. Clique em **"Register for an Account"**
3. **IMPORTANTE:** Utilize seu **e-mail institucional** (ex: `seu.usuario@ufpe.br`).
   - A licença acadêmica está vinculada à verificação de um domínio educacional
4. Siga as instruções de verificação enviadas ao seu e-mail
5. Após aprovação, faça o download do arquivo de licença (`license.lic`).
6. Salve o arquivo em um local de fácil acesso (ex: Área de Trabalho).

### B. Download e Instalação

Na página de downloads da sua conta Schrödinger, baixe o instalador apropriado para seu sistema operacional pelo site <a href="https://pymol.org/edu/" target="_blank">https://pymol.org/edu/</a>


### C. Ativação da Licença

1. Inicie o PyMOL pela primeira vez.
2. O programa solicitará a ativação.
3. Escolha a opção **"I have a license file"**.
4. Navegue até o local do arquivo `license.lic` e selecione-o.
5. O PyMOL será ativado e estará pronto para uso.

---

# Módulos Práticos

### Módulo 1: Análise de Sequências e Propriedades

**Objetivos:**
- Navegar e extrair dados da p53 em bancos de dados estruturais.
- Utilizar ferramentas web para predição de características bioquímicas.

#### Bancos de Dados

| Recurso | URL | Descrição |
|---------|-----|-----------|
| **UniProt** | <a href="https://www.uniprot.org/" target="_blank">https://www.uniprot.org/</a> | Informações de sequência e anotações funcionais |
| **PDB** | <a href="https://www.rcsb.org/" target="_blank">https://www.rcsb.org/</a> | Estruturas tridimensionais experimentais |

---

#### Ferramentas de Predição

As ferramentas abaixo serão utilizadas para analisar propriedades físico-químicas e funcionais utilizando sequências FASTA de proteínas e peptídeos, é uma abordagem exploratória para entender melhor como o seu sistema é representado em termos de características bioquímicas e funcionais.

| Ferramenta | URL | Função |
|------------|-----|---------|
| **ProtParam** | <a href="https://web.expasy.org/protparam/" target="_blank">https://web.expasy.org/protparam/</a> | Parâmetros físico-químicos |
| **SignalP 6.0** | <a href="https://services.healthtech.dtu.dk/services/SignalP-6.0/" target="_blank">https://services.healthtech.dtu.dk/services/SignalP-6.0/</a> | Predição de peptídeos de sinal |
| **InterProScan** | <a href="https://www.ebi.ac.uk/interpro/search/sequence/" target="_blank">https://www.ebi.ac.uk/interpro/search/sequence/</a> | Identificação de domínios e famílias |
| **WoLFPSORT** | <a href="https://wolfpsort.hgc.jp/" target="_blank">https://wolfpsort.hgc.jp/</a> | Identificação de localização celular |

> Agora vamos discutir os resultados obtidos e suas implicações biológicas?

# Atividade 1

**Alinhamento 1TUP vs. Sequência Completa (WT):** Temos as sequências FASTA do domíde ligação ao DNA da p53 e sua sequenência completa (WT), e, juntos, executaremos o alinhamento múltiplo no <a href="https://www.ebi.ac.uk/jdispatcher/msa/clustalo" target="_blank" rel="noopener noreferrer">Clustal Omega</a>. Analise quais regiões se alinham diretamente, discuta as diferenças e vamos entender as implicações biológicas dessas variações. Ter apenas "uma parte" da proteína pode ser suficiente para algumas análises? Isso depende do contexto biológico? 

> Baixe aqui o arquivo multiFASTA com as 2 sequências: <a href="https://drive.google.com/file/d/1qILbrqhwLmvImiNK1Wg469DPcJgOx047/view?usp=sharing" target="_blank">multiFASTA_p53_1TUP_vs_WT.fasta</a>

> Sequências FASTA do domínio ligador de DNA da p53, cristalizado por X-ray (PDB ID: 1TUP):

```bash
>1TUP_3|Chains C[auth A] |PROTEIN (P53 TUMOR SUPPRESSOR )|Homo sapiens (9606)
SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPP
GTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFR
HSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVR
VCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNT
```

> Sequência completa da p53 (UNIPROT ID: P04637):

```bash
>sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens OX=9606 GN=TP53
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

### Perguntas:

- Em quais trechos o domínio 1TUP se alinha diretamente com a sequência completa e quais regiões ficam sem correspondência?
- Os limites N- e C-terminais do domínio cristalizado aparecem contíguos no alinhamento ou revelam lacunas/extensions relevantes para estabilidade?
- Há resíduos-chave do sítio de ligação ao DNA presentes apenas na sequência completa? O que isso implica para os modelos baseados no domínio?
- Considerando identidade e similaridade ponto a ponto, qual argumento favorece trabalhar com o domínio isolado ou com a proteína completa nas próximas etapas?

---

# Atividade 2 


> **Atividade (EXTRA):** Temos 5 sequências da p53 (1 referência *wild-type* e 4 variantes associadas a neoplasias) e, juntos, executaremos o alinhamento múltiplo no <a href="https://www.ebi.ac.uk/jdispatcher/msa/clustalo" target="_blank" rel="noopener noreferrer">Clustal Omega</a>. Analise quais substituições coincidem com domínios funcionais críticos, discuta como essas mudanças podem impactar estabilidade e interação com DNA e, por fim, decidam coletivamente qual variante seguirá para aprofundamento nas etapas práticas.

> Baixe aqui o arquivo multiFASTA com as 5 sequências: <a href="https://drive.google.com/file/d/1qpbnbvNjTRcvvG-UsXdiJYXvynkdvxYw/view?usp=sharing" target="_blank">multiFASTA_p53_variants.fasta</a>

## Wild-Type (Sequência Canônica - 393 aa)

```
>sp|P04637|P53_HUMAN_WT Cellular tumor antigen p53
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

## Mutações Cancer-Associadas

### R175H (Hotspot - Contato com Zinco)

```
>sp|P04637|P53_HUMAN_R175H Cellular tumor antigen p53 (R175H mutation)
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTHVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

**Mudança na posição 175: R → H** 

### R248Q (Hotspot - Contato Direto com DNA)

```
>sp|P04637|P53_HUMAN_R248Q Cellular tumor antigen p53 (R248Q mutation)
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNQRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

**Mudança na posição 248: R → Q** 

### Y220C (Cavidade Hidrofóbica)

```
>sp|P04637|P53_HUMAN_Y220C Cellular tumor antigen p53 (Y220C mutation)
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVECLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

**Mudança na posição 220: Y → C** 

### R273H (Hotspot - Contato Direto com DNA)

```
>sp|P04637|P53_HUMAN_R273H Cellular tumor antigen p53 (R273H mutation)
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGHNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

**Mudança na posição 273: R → H** 

---

**Não vale clicar nesse link antes de fazer o alinhamento proposto acima**, mas se você já fez, está mais que permitido: <a href="https://drive.google.com/file/d/1zSzitu4daGhJwSUpWxuzzTzBVwkqMo1h/view?usp=sharing" target="_blank">Alinhamento Clustal Omega - multiFASTA_p53_variants.fasta</a>, colorido por percentual de conservação. Podemos ver as mutações destacadas no alinhamento e nas suas a perda da identidade em relação à sequência *wild-type*. Além disso o alinhamento com também mostra um histograma de conservação na parte inferior, onde podemos observar que as posições das mutações são altamente conservadas na família das p53.

> O que vocês acharam desse alinhamento? Vamos discutir as possieveis implicações biológicas dessas mutações?

> Para relembrar, abaixo temos uma tambela com todos os aminoácidos e suas características físico-químicas, caso queiram consultar durante a análise das mutações.

<p align="justify">
  <img src="imgs/aas.png" alt="Amino acids width="1000">
</p>

> Fonte: JPT Peptide Technologies.

---

## Localização das Mutações no Domínio de Ligação ao DNA (aa 102-292)

| Mutação | Posição | Região | AA WT | AA Mut | Contexto |
|---------|---------|--------|-------|--------|----------|
| **R175H** | 175 | Loop L2 | R | H | `...GTR**V**RAM...` → `...GTH**V**RAM...` |
| **Y220C** | 220 | Loop L3 | Y | C | `...RVE**Y**LDD...` → `...RVE**C**LDD...` |
| **R248Q** | 248 | Loop L3 | R | Q | `...GMN**R**RPI...` → `...GMN**Q**RPI...` |
| **R273H** | 273 | Folha β | R | H | `...LLG**R**NSF...` → `...LLG**H**NSF...` |

Aqui trago um resumo das mutações mais comuns da p53 associadas ao câncer, localizadas no domínio de ligação ao DNA (DBD). Essas mutações são conhecidas por afetar a capacidade da p53 de se ligar ao DNA e exercer sua função supressora de tumor.

---

## Notas Importantes

1. **Todas as sequências têm exatamente 393 aminoácidos**
2. As mutações estão localizadas no **DNA-binding domain (DBD)** entre os resíduos 102-292
3. Estas são as mutações mais frequentes em cânceres humanos (hotspots)
4. A numeração segue a sequência canônica do UniProt P04637 (isoforma 1)

## Verificação das Mutações

Para confirmar as posições exatas:
- **R175H**: Resíduo 175 (Arginina → Histidina)
- **Y220C**: Resíduo 220 (Tirosina → Cisteína)  
- **R248Q**: Resíduo 248 (Arginina → Glutamina)
- **R273H**: Resíduo 273 (Arginina → Histidina)

### Perguntas:

- Em quais posições do alinhamento múltiplo surgem substituições e essas posições são conservadas na sequência *wild-type*?
- As mutações identificadas representam trocas conservativas ou drásticas em termos de propriedades físico-químicas (ex.: troca de polar para hidrofóbico)?
- Alguma das substituições cria ou elimina motivos funcionais conhecidos (ex.: sítios de fosforilação, ligações a DNA) sugeridos pelo alinhamento?
- Comparando as quatro variantes mutadas entre si, existe um padrão recorrente de substituições que aponte para um hotspot funcional?

---

# Módulo 2: Modelagem por Homologia e Threading

Sequência FASTA completa da p53 (UNIPROT ID: P04637), que utilizaremos nas atividades práticas de modelagem estrutural:

```bash
>sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens OX=9606 GN=TP53
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

---

**Objetivos:**
- Construir modelos da p53 utilizando diferentes abordagens.
- Analisar alinhamentos sequência-molde e métricas de confiança.

### Modelagem por Homologia

**Plataforma:** SWISS-MODEL  
**URL:** <a href="https://swissmodel.expasy.org/" target="_blank">https://swissmodel.expasy.org/</a>

**Análise:**
- Avaliar alinhamentos sequência-molde
- Examinar cobertura e identidade de sequência

### Modelagem por Threading/Ab Initio

**Plataforma:** I-TASSER  
**URL:** <a href="https://zhanggroup.org/I-TASSER/" target="_blank">https://zhanggroup.org/I-TASSER/</a>

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

# Módulo 3: Predição por Deep Learning (AF2, AF3 e ESM3)

Sequência FASTA completa da p53 (UNIPROT ID: P04637), que utilizaremos nas atividades práticas de modelagem estrutural:

```bash
>sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens OX=9606 GN=TP53
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
PGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPG
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

---

> Vamos discutir como esses modelos funcionam mais uma vez, focando em suas arquiteturas baseadas em aprendizado profundo?

**Objetivos:**
- Utilizar métodos de aprendizado profundo para predição estrutural.
- Interpretar métricas de confiança específicas (pLDDT, PAE).

> O **pLDDT (predicted Local Distance Difference Test)** é uma métrica de confiança por resíduo (0-100) que avalia a precisão da predição da estrutura *local* ao redor de cada aminoácido, sendo alta para regiões bem dobradas e baixa para regiões desordenadas.

> O **PAE (Predicted Aligned Error)** é uma métrica inter-resíduo (medida em Ångströms) que avalia a confiança na *orientação relativa* e global entre diferentes domínios ou pares de resíduos, indicando se a montagem 3D geral está correta.

> Em resumo, o pLDDT mede a confiança no dobramento *local* de um resíduo, enquanto o PAE mede a confiança na posição *global* desse resíduo em relação a todos os outros na estrutura.

### Plataformas de Deep Learning

| Método | URL | Descrição |
|--------|-----|-----------|
| **AlphaFold2 / ColabFold** | <a href="https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb" target="_blank">AlphaFold2 Notebook</a> | Baseado em AlphaFold2 (Google Colab) |
| **AlphaFold 3 Server** | <a href="https://alphafoldserver.com/" target="_blank">https://alphafoldserver.com/</a> | Versão mais recente do AlphaFold |
| **ESM3** | <a href="https://forge.evolutionaryscale.ai/" target="_blank">https://forge.evolutionaryscale.ai/</a> | Baseado em Modelo de Linguagem de Proteína e Dados Evolutivos  |

### Métricas de Confiança

- **pLDDT** (predicted Local Distance Difference Test): 0-100, >90 = alta confiança
- **PAE** (Predicted Aligned Error): Confiança na posição relativa entre resíduos

### Perguntas:

- Como os valores de pLDDT distribuídos ao longo da cadeia ajudam a distinguir regiões estruturadas de segmentos desordenados na p53 predita?
- Ao comparar os mapas de PAE dos diferentes servidores, quais domínios apresentam maior incerteza relativa e como isso impacta a confiança global do modelo?
- Quais diferenças você espera observar entre as predições de AF2/ColabFold, AF3 e ESM3 em termos de conformação global e métricas de confiança?
- Se você tivesse de priorizar um único modelo para a próxima etapa de análise comparativa, quais critérios baseados nas saídas desses métodos sustentariam sua escolha?

---

# Módulo 4: Análise Comparativa, Validação e Visualização

* Agora que temos os modelos gerados por homologia, threading e deep learning. Vamos baixar um modelos experimental, obtido por cristalografia de x-ray, da p53 para comparar os modelos teóricos. Lembrando que a extrutura experimental sempre será o nosso padrão-ouro de comparação.

**Baixe aqui o arquivo PDB da estrutura cristalina da p53 (PDB ID: 1TUP) para utilizar como referência na comparação dos modelos preditos:** <a href="https://drive.google.com/file/d/1p0liOriRtvaYrY2CvTDCWpMGHIO1zfoq/view?usp=sharing" target="_blank">1TUP_cleaned.pdb</a>.

> Sugiro fortemente que utilize este arquivo para evitar problemas de formatação ou erros por conta de heteroátomos.

> Opicional: Baixar a estrutura experimental da p53 (PDB ID: 1TUP) do RCSB PDB para servir como referência na comparação dos modelos preditos. No entanto, além da proteína, o arquivo possuí íons, águas e ligantes. Link: <a href="https://www.rcsb.org/structure/1tup" target="_blank">https://www.rcsb.org/structure/1tup</a>

**Objetivos:**
- Comparar todos os modelos gerados.
- Realizar análise estrutural comparativa no PyMOL.
- Quantificar diferenças estruturais via RMSD.

**Servidores de Validação de Dobramento e Termodinâmica**

| Servidor | URL | Métrica Avaliada |
|----------|-----|------------------|
| **MolProbity (SAVES)** | <a href="https://saves.mbi.ucla.edu/" target="_blank">https://saves.mbi.ucla.edu/</a> | Gráfico de Ramachandran, geometria |
| **QMEAN** | <a href="https://swissmodel.expasy.org/qmean/" target="_blank">https://swissmodel.expasy.org/qmean/</a> | Qualidade global |
| **ProSA-web** | <a href="https://prosa.services.came.sbg.ac.at/prosa.php" target="_blank">https://prosa.services.came.sbg.ac.at/prosa.php</a> | Z-score (energia do enovelamento) |

### Análise Estrutural no PyMOL

**Modelos para Comparação:**
- SWISS-MODEL (Homologia)
- I-TASSER (Threading)
- AlphaFold 2 (ColabFold)
- AlphaFold 3 Server
- ESM3
- **1TUP** (Estrutura experimental de referência - X-ray).

---

1. **Carregar estruturas**
  
- Abra o PyMOL e carregue todos os modelos preditos e a estrutura experimental fornecida.

2. **Cálculo de RMSD**
- Quantificar divergência estrutural de cada modelo vs. 1TUP.
- Registrar valores de RMSD para comparação e discutir o que seria um valor aceitável de RMSD para modelos preditos.

1. **Inspeção visual**
- Identificar regiões de convergência (alta similaridade).
- Identificar regiões de divergência (loops, cadeias laterais).
- Destacar sítios ativos e domínio de ligação ao DNA.

1. **Geração de figuras**
- Criar representações ilustrativas das diferenças/similaridades.
- Destacar regiões de interesse estrutural.

### Perguntas:

- Quais modelos apresentam RMSD mais baixo em relação à estrutura experimental e o que isso revela sobre a qualidade geral de cada predição?
- Ao inspecionar as sobreposições no PyMOL, quais regiões da p53 mantêm conformação consistente entre todos os modelos e quais divergem com mais intensidade?
- Como as métricas de validação (MolProbity, QMEAN, ProSA-web) complementam os resultados de RMSD para justificar a seleção de um modelo confiável?
- De que modo as figuras geradas podem comunicar melhor as diferenças funcionais potenciais entre os modelos analisados?

---

# Referências Teórico (Atividades Práticas)

### Bases de Dados
- <a href="https://www.uniprot.org/" target="_blank" rel="noopener noreferrer">UniProt</a>
- <a href="https://www.rcsb.org/" target="_blank" rel="noopener noreferrer">RCSB PDB</a>

### Ferramentas de Predição
- <a href="https://web.expasy.org/protparam/" target="_blank" rel="noopener noreferrer">ExPASy ProtParam</a>
- <a href="https://services.healthtech.dtu.dk/service.php?SignalP-6.0" target="_blank" rel="noopener noreferrer">SignalP 6.0</a>
- <a href="https://www.ebi.ac.uk/interpro/search/sequence/" target="_blank" rel="noopener noreferrer">InterProScan</a>
- <a href="https://prosite.expasy.org/" target="_blank" rel="noopener noreferrer">PROSITE</a>

### Modelagem Estrutural
- <a href="https://swissmodel.expasy.org/" target="_blank" rel="noopener noreferrer">SWISS-MODEL</a>
- <a href="https://zhanggroup.org/I-TASSER/" target="_blank" rel="noopener noreferrer">I-TASSER</a>
- <a href="https://colabfold.com/" target="_blank" rel="noopener noreferrer">AlphaFold 2 (ColabFold)</a>
- <a href="https://alphafoldserver.com/" target="_blank" rel="noopener noreferrer">AlphaFold 3 Server</a>
- <a href="https://esm.metademolab.com/esm3" target="_blank" rel="noopener noreferrer">ESM3</a>

### Validação
- <a href="http://molprobity.biochem.duke.edu/" target="_blank" rel="noopener noreferrer">MolProbity</a> / <a href="https://saves.mbi.ucla.edu/" target="_blank" rel="noopener noreferrer">SAVES</a>
- <a href="https://swissmodel.expasy.org/qmean/" target="_blank" rel="noopener noreferrer">QMEAN</a>
- <a href="https://prosa.services.came.sbg.ac.at/prosa.php" target="_blank" rel="noopener noreferrer">ProSA-web</a>

### Visualização
- <a href="https://pymol.org/2/" target="_blank" rel="noopener noreferrer">PyMOL (Schrödinger)</a>

---

# Licença

Uso extriitamente educacional e acadêmico. Proibida a utilização comercial sem autorização prévia dos autores.
Para qualquer outro tipo de uso, entre em contato com os autores pelos e-mails fornecidos acima.

---

# Recursos Úteis

<a href="https://github.com/madsondeluna/bits_bytes_biomolecules" target="_blank">Repositório do Curso</a>
<a href="https://madsondeluna.github.io/bits_bytes_biomolecules/" target="_blank">Página Web do Curso</a>


---

<br>

> Ninhuma dúvida é boba... Qualquer dúvida ou sugestão, sinta-se à vontade para entrar em contato conosco pelos e-mails fornecidos acima. Bom desemprenho e aproveitem os exercícios! 

<br>

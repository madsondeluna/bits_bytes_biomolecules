# Exercícios Práticos

**Instrutor I:** Madson A. de Luna Aragão 

**Instrutor II:** André S. Lira de Lucena

**Evento:** Curso de Férias em Bioinformática - 02 à 06 de março de 2026

**Contato:** madsondeluna@gmail.com; andresllucena@gmail.com

**Outros Projetos:** <a href="https://github.com/madsondeluna" target="_blank" rel="noopener noreferrer">https://github.com/madsondeluna</a>

**Slides das aulas:**

<a href="aulas/aula_dia1.pdf" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Aula%20Dia%201-PDF-blue?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Aula Dia 1"></a>

<a href="aulas/aula_dia2.pdf" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Aula%20Dia%202-PDF-blue?style=for-the-badge&logo=adobeacrobatreader&logoColor=white" alt="Aula Dia 2"></a> 

---
# Momento I

## Ferramentas de Predição

As ferramentas abaixo serão utilizadas para analisar propriedades físico-químicas e funcionais utilizando sequências FASTA de proteínas e peptídeos, é uma abordagem exploratória para entender melhor como o seu sistema é representado em termos de características bioquímicas e funcionais.

| Ferramenta | URL | Descrição |
|------------|-----|-----------|
| **ProtParam** | <a href="https://web.expasy.org/protparam/" target="_blank">https://web.expasy.org/protparam/</a> | Parâmetros físico-químicos |
| **SignalP 6.0** | <a href="https://services.healthtech.dtu.dk/services/SignalP-6.0/" target="_blank">https://services.healthtech.dtu.dk/services/SignalP-6.0/</a> | Predição de peptídeos de sinal |
| **CD-Search** | <a href="https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi" target="_blank">https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi</a> | Identificação de peptídeos de sinal e caracterização de domínios conservados via busca em bases como CDD, Pfam e TIGRFAM |
| **InterProScan** | <a href="https://www.ebi.ac.uk/interpro/search/sequence/" target="_blank">https://www.ebi.ac.uk/interpro/search/sequence/</a> | Identificação integrada de domínios e famílias proteicas; engloba o Pfam e outras bases como PANTHER, HAMAP, PRINTS, ProSite e SFLD |
| **WoLFPSORT** | <a href="https://wolfpsort.hgc.jp/" target="_blank">https://wolfpsort.hgc.jp/</a> | Identificação de localização celular |

> Agora vamos discutir os resultados obtidos e suas implicações biológicas?

---

# Atividade 1: Caracterização de Proteínas a partir da Sequência Primária

**Objetivo:** Utilizar as ferramentas de predição apresentadas para caracterizar cinco proteínas humanas com propriedades bem documentadas, comparar os resultados obtidos entre elas e discutir as implicações biológicas de cada *feature* identificada. Esta atividade é o ponto de partida do nosso fluxo de trabalho: toda modelagem estrutural confiável começa com a compreensão profunda da sequência primária.

**Proteínas selecionadas:** as cinco proteínas abaixo foram escolhidas por representarem contextos biológicos distintos, diferentes localizações subcelulares, presença ou ausência de peptídeo de sinal, variação de pI, tamanho e repertório de domínios, permitindo interpretar e comparar resultados de forma rica e contextualizada.

| # | Proteína | Gene | UniProt | Características esperadas |
|:-:|:---------|:-----|:-------:|:--------------------------|
| 1 | Albumina sérica humana | *ALB* | <a href="https://www.uniprot.org/uniprotkb/P02768" target="_blank">P02768</a> | Peptídeo sinal + propeptídeo, proteína secretada, pI ácido (~4,9), estável, sem TM, transportadora |
| 2 | Antígeno tumoral p53 | *TP53* | <a href="https://www.uniprot.org/uniprotkb/P04637" target="_blank">P04637</a> | Sem peptídeo sinal, localização nuclear (NLS), pI ~6,3, instável (*in vivo*), domínios TAD/DBD/OD/CTD |
| 3 | Pré-pró-insulina | *INS* | <a href="https://www.uniprot.org/uniprotkb/P01308" target="_blank">P01308</a> | Peptídeo sinal + propeptídeo (C-peptídeo), pequena hormona secretada, rica em Cys (pontes S-S) |
| 4 | Subunidade alfa-1 da hemoglobina | *HBA1* | <a href="https://www.uniprot.org/uniprotkb/P69905" target="_blank">P69905</a> | Sem peptídeo sinal, citoplasmática (eritrócito), pI básico (~8,7), domínio globina, carreadora de O₂ |
| 5 | Lisozima C | *LYZ* | <a href="https://www.uniprot.org/uniprotkb/P00698" target="_blank">P00698</a> | Peptídeo sinal, secretada (saliva, lágrimas, leite), pI básico (~9,3), enzima (glicosídeo hidrolase), rica em Cys |

---

## Sequências FASTA (incluindo peptídeo de sinal quando presente)

> **Importante:** As sequências abaixo correspondem às proteínas completas, incluindo o peptídeo de sinal e propeptídeos onde existem. Essa é a sequência que será reconhecida pelas ferramentas SignalP, CD-Search e InterProScan.

### Proteína 1 - Albumina sérica humana (P02768 · 609 aa)
> Peptídeo sinal: resíduos 1–18 · Propeptídeo: resíduos 19–24 · Proteína madura: resíduos 25–609

```
>sp|P02768|ALBU_HUMAN Albumin OS=Homo sapiens OX=9606 GN=ALB PE=1 SV=2
MKWVTFISLLFLFSSAYSRGVFRRDTHKSEIAHRFKDLGEENFKALVLIAFAQYLQQCP
FEDHVKLVNEVTEFAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQ
EPERNECFLQHKDDNPNLPRLVRPEVDVMCTAFHDNEETFLKKYLYEIARRHPYFYAPE
LLFFAKRYKAAFTECCQAADKAACLLPKLDELRDEGKASSAKQRLKCASLQKFGERAFKA
WAVARLSQRFPKAEFAEVSKLVTDLTKVHTECCHGDLLECADDRADLAKYICENQDSISS
KLKECCEKPLLEKSHCIAEVENDEMPADLPSLAADFVESKDVCKNYAEAKDVFLGMFLYE
YARRHPDYSVVLLLRLAKTYETTLEKCCAADDPHECYAKVFDEFKPLVEEPQNLIKQNCE
LFEQLGEYKFQNALLVRYTKKVPQVSTPTLVEVSRNLGKVGSKCCKHPEAKRMPCAEDYL
SVVLNQLCVLHEKTPVSEKVTKCCTESLVNRRPCFSALEVDETYVPKEFNAETFTFHADI
CTLPDTEKQIKKQTALVELVKHKPKATAEQLKTVMENFVAFVDKCCAADDKEACFAVEGP
KLVVSTQTALA
```

### Proteína 2 - Antígeno tumoral p53 (P04637 · 393 aa)
> Sem peptídeo de sinal. Proteína nuclear; NLS localizado na região C-terminal do DBD.

```
>sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens OX=9606 GN=TP53 PE=1 SV=4
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

### Proteína 3 - Pré-pró-insulina (P01308 · 110 aa)
> Peptídeo sinal: resíduos 1–24 · Cadeia B: 25–54 · C-peptídeo: 57–87 · Cadeia A: 90–110

```
>sp|P01308|INS_HUMAN Insulin OS=Homo sapiens OX=9606 GN=INS PE=1 SV=1
MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAED
LQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN
```

### Proteína 4 - Subunidade alfa-1 da hemoglobina (P69905 · 142 aa)
> Sem peptídeo de sinal. Proteína citoplasmática (eritrócitos); sem passagem transmembrana.

```
>sp|P69905|HBA_HUMAN Hemoglobin subunit alpha OS=Homo sapiens OX=9606 GN=HBA1 PE=1 SV=2
MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHG
KKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTP
AVHASLDKFLASVSTVLTSKYR
```

### Proteína 5 - Lisozima C (P00698 · 148 aa)
> Peptídeo sinal: resíduos 1–18 · Proteína madura: resíduos 19–148 · Enzima antimicrobiana secretada.

```
>sp|P00698|LYC_HUMAN Lysozyme C OS=Homo sapiens OX=9606 GN=LYZ PE=1 SV=1
MKALIVLGLVLLSVTVQGKVFERCELTRTLKRLGMDGYRGISLANWMCLAKWMSGYNTRA
TNYNADGRSTDYGIFQINSRYWCNDGKTPGAVNACHLSCSALLQDNIADAVACAKRVVRDP
QGIRAWVAWRNRFCQNRDVRQYVQGCGV
```

---

## Passo a Passo - Ferramentas de Predição

Para **cada uma das 5 proteínas**, repita o roteiro abaixo. Registre os resultados na tabela ao final desta seção antes de responder às perguntas.

### Passo 1 - ProtParam (Propriedades físico-químicas)

O **ProtParam** (ExPASy) calcula parâmetros físico-químicos diretamente a partir da sequência de aminoácidos, sem necessidade de estrutura 3D. Usaremos essa ferramenta para obter massa molecular, ponto isoelétrico (pI), índice de instabilidade, índice GRAVY e coeficiente de extinção molar de cada proteína. Esses parâmetros são essenciais para compreender o comportamento da proteína em solução, sua estabilidade *in vivo* e suas possíveis interações com outras moléculas, informações que fundamentam qualquer análise estrutural posterior.

1. Acesse <a href="https://web.expasy.org/protparam/" target="_blank">https://web.expasy.org/protparam/</a>.
2. Cole a sequência de aminoácidos (apenas a sequência, sem o cabeçalho FASTA) na caixa de texto e clique em **"Compute parameters"**.
3. Registre os seguintes valores:
   - **Número de aminoácidos** (confira se bate com o tamanho esperado)
   - **Massa molecular** (em Da)
   - **pI teórico**
   - **Índice de instabilidade** (< 40 = estável; > 40 = instável)
   - **Índice GRAVY** (negativo = hidrofílica; positivo = hidrofóbica)
   - **Coeficiente de extinção molar** a 280 nm

> **Dica:** Para a albumina e a pré-pró-insulina, rode o ProtParam com a sequência completa (incluindo peptídeo sinal). Anote se há diferença relevante no pI ao comparar precursor e proteína madura.

---

### Passo 2 - SignalP 6.0 (Peptídeo de sinal)

O **SignalP 6.0** (DTU Health Tech) utiliza redes neurais profundas para predizer se uma proteína possui peptídeo de sinal N-terminal e, caso possua, identifica com precisão o sítio de clivagem. O peptídeo de sinal é a sequência que direciona a proteína recém-sintetizada para o retículo endoplasmático rugoso e, consequentemente, para a via secretória. Identificá-lo é fundamental para determinar a sequência da proteína madura e para compreender o destino celular de cada proteína analisada.

1. Acesse <a href="https://services.healthtech.dtu.dk/services/SignalP-6.0/" target="_blank">https://services.healthtech.dtu.dk/services/SignalP-6.0/</a>.
2. Cole a sequência FASTA completa (incluindo cabeçalho `>`) na caixa de texto.
3. Selecione o organismo: **Eukarya**.
4. Clique em **"Submit"** e aguarde o resultado.
5. Registre:
   - **Tipo predito** (SP = peptídeo sinal clássico, OTHER = ausente, LIPO, TAT etc.)
   - **Probabilidade máxima de SP** (se aplicável)
   - **Posição do sítio de clivagem (CS)**, o primeiro resíduo da proteína madura

> **Atenção:** Para proteínas sem peptídeo de sinal (p53 e hemoglobina), o resultado esperado é tipo **OTHER** com probabilidade baixa de SP. Um resultado inesperado merece discussão.

---

### Passo 3 - CD-Search/NCBI (Domínios conservados)

O **CD-Search** (NCBI) realiza buscas de similaridade entre a sequência-consulta e perfis de domínios conservados presentes na *Conserved Domain Database* (CDD), que integra bancos como Pfam, TIGRFAM e SMART. Domínios conservados são regiões da sequência com função e estrutura preservadas ao longo da evolução. Identificá-los permite inferir a função molecular de uma proteína, delimitar regiões estruturais importantes e comparar repertórios de domínios entre proteínas distintas, algo que faremos em seguida com o InterProScan para avaliar consistência entre ferramentas.

1. Acesse <a href="https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi" target="_blank">https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi</a>.
2. Cole a sequência FASTA completa na caixa de texto.
3. Em **"Database"**, selecione **CDD v3** (padrão, inclui entradas do Pfam, TIGRFAM e SMART).
4. Clique em **"Submit"** e aguarde.
5. Na aba de resultados, observe o **mapa gráfico de domínios** e a tabela de *hits*. Registre:
   - Nome e ID de cada domínio identificado (*Specific hits* prioritariamente)
   - Posição de início e fim de cada domínio na sequência
   - E-value de cada hit
   - Presença de regiões de baixa complexidade (Low-complexity regions)

---

### Passo 4 - InterProScan (Integração multi-banco)

O **InterProScan** (EMBL-EBI) é uma plataforma integradora que consulta simultaneamente múltiplos bancos de dados de famílias e domínios proteicos, incluindo Pfam, PANTHER, HAMAP, PRINTS, ProSite e SFLD. Ao contrário do CD-Search, que foca na CDD, o InterProScan oferece cobertura mais ampla e associa automaticamente às entradas identificadas os **termos Gene Ontology (GO)**, que descrevem função molecular, processo biológico e componente celular. Usar ambas as ferramentas permite avaliar a concordância dos resultados e capturar domínios ou motivos que poderiam passar despercebidos em um único banco.

1. Acesse <a href="https://www.ebi.ac.uk/interpro/search/sequence/" target="_blank">https://www.ebi.ac.uk/interpro/search/sequence/</a>.
2. Cole a sequência FASTA completa na caixa de texto e clique em **"Search"**.
3. Aguarde o processamento (pode levar 1–3 minutos).
4. Explore o **mapa de domínios** interativo e a lista de entradas identificadas. Registre:
   - Bancos de dados que identificaram domínios (Pfam, PANTHER, HAMAP etc.)
   - Nome dos domínios e seus intervalos na sequência
   - **GO terms** associados (Função Molecular, Processo Biológico, Componente Celular)
   - Compare com o resultado do CD-Search: há domínios detectados em um servidor mas não no outro?

---

### Passo 5 - WoLFPSORT (Localização subcelular)

O **WoLFPSORT** prediz a localização subcelular de uma proteína a partir de sua sequência de aminoácidos, analisando sinais de tráfego (como peptídeo de sinal, NLS e sequências de ancoragem a membranas) e composição aminoacídica global. Conhecer a localização subcelular é fundamental para contextualizar a função de uma proteína: uma enzima citoplasmática, uma proteína secretada e um fator de transcrição nuclear operam em ambientes completamente distintos. Utilizaremos essa ferramenta como validação complementar ao SignalP e ao InterProScan, verificando se a localização predita é consistente com a anotação experimental do UniProt.

1. Acesse <a href="https://wolfpsort.hgc.jp/" target="_blank">https://wolfpsort.hgc.jp/</a>.
2. Cole a sequência de aminoácidos (apenas a sequência) na caixa.
3. Selecione **"animal"** como tipo de organismo e clique em **"predict!"**.
4. Registre:
   - Localização subcelular predita com maior escore
   - Escores das localizações alternativas
   - Compare com a localização anotada no UniProt: o resultado é consistente?

---

## Tabela de Registro de Resultados

Preencha a tabela abaixo ao longo da atividade:

| Proteína | Massa (kDa) | pI | Instabilidade | GRAVY | Peptídeo sinal? | CS (posição) | Domínios principais (CD-Search) | GO: Componente celular (InterPro) | Localização (WoLFPSORT) |
|:---------|:-----------:|:--:|:-------------:|:-----:|:---------------:|:------------:|:--------------------------------|:----------------------------------|:-----------------------:|
| Albumina (P02768) | 69222.50 | 5.73 | 39.02 | -0.329 | Sec/SPI | 18 and 19 | ALBUMIN domain | extracellular space (GO:0005615) | extr |
| p53 (P04637) | 36910.59 | 6.07 | 78.83 | -0.677 | Other | - | TAD1, TAD2, P53 Binding domain | nucleus (GO:0005634) | cyto_nucl |
| Insulina (P01308) | 11980.91 | 5.22 | 40.33 | 0.193 | Sec/SPI | 24 and 25 | I/IGF_like superfamily | extracellular region (GO:0005576) | extr |
| Hemoglobina α (P69905) | 15257.55 | 8.72 | 6.97 | 0.048 | Other | - | Globin-like superfamily | hemoglobin complex (GO:0005833) | cyto |
| Lisozima C (P00698) | 16716.30 | 9.50 | 30.78 | -0.155 | Sec/SPI | 18 and 19 | Lyz-like superfamily | None | extr |

**Legenda**

| Campo | Ferramenta |
|:------|:-----------|
| Massa (kDa) | **ProtParam** → parâmetro *Molecular weight* |
| pI | **ProtParam** → parâmetro *Theoretical pI* |
| Instabilidade | **ProtParam** → parâmetro *Instability index* |
| GRAVY | **ProtParam** → parâmetro *Grand average of hydropathicity (GRAVY)* |
| Peptídeo sinal? | **SignalP 6.0** → coluna *Prediction* (SP = sim; OTHER = não) |
| CS (posição) | **SignalP 6.0** → coluna *CS Position* (posição do sítio de clivagem) |
| Domínios principais (CD-Search) | **CD-Search** → aba *Domain hits*, coluna *Superfamily/Name* |
| GO: Componente celular (InterPro) | **InterProScan** → aba *Gene Ontology*, categoria *Cellular component* |
| Localização (WoLFPSORT) | **WoLFPSORT** → coluna *Localization* (ex.: *nucl*, *cyto*, *extr*) |

---

## Perguntas para Discussão

---

### Pergunta 1: Peptídeo de sinal e destino celular

O SignalP classificou cada proteína como **SP** (peptídeo de sinal clássico) ou **OTHER**? Monte uma tabela com os resultados das 5 proteínas e identifique quais são secretadas e quais permanecem intracelulares. Para as proteínas sem peptídeo de sinal, p53 e hemoglobina α, como cada uma é direcionada ao seu compartimento correto (núcleo vs. citoplasma)?

> **Resposta:**
>
> A tabela abaixo resume o resultado do SignalP para cada proteína:
>
> | Proteína | SignalP | Sítio de Clivagem | Destino |
> |:---------|:-------:|:-----------------:|:-------:|
> | Albumina | Sec/SPI | Entre aa 18 e 19 | Secretada (plasma sanguíneo) |
> | p53 | Other | — | Intracelular (núcleo) |
> | Insulina | Sec/SPI | Entre aa 24 e 25 | Secretada (corrente sanguínea) |
> | Hemoglobina α | Other | — | Intracelular (citoplasma) |
> | Lisozima C | Sec/SPI | Entre aa 18 e 19 | Secretada (saliva, lágrimas) |
>
> Albumina, insulina e lisozima C possuem peptídeo de sinal clássico (Sec/SPI) e seguem a **via secretória clássica**: o peptídeo de sinal é reconhecido pelo complexo SRP (*Signal Recognition Particle*) ainda durante a tradução, a proteína é inserida no retículo endoplasmático rugoso, o peptídeo é clivado pela peptidase de sinal e a proteína madura segue para o Complexo de Golgi e depois para o meio extracelular.
>
> A **p53** não possui peptídeo de sinal. Ela é sintetizada em ribossomos livres no citoplasma e é direcionada ao núcleo por meio de **sequências de localização nuclear (NLS, do inglês *Nuclear Localization Signals*)**, presentes na região C-terminal do domínio de ligação ao DNA. Essas sequências são reconhecidas por proteínas chamadas importinas, que transportam a p53 através do poro nuclear de forma ativa e dependente de energia.
>
> A **hemoglobina α** também não possui peptídeo de sinal. Ela é sintetizada em ribossomos livres e **permanece no citoplasma** dos eritrócitos, exatamente onde exerce sua função de transporte de oxigênio. A ausência de qualquer sinal de direcionamento a mantém no compartimento padrão de síntese proteica, que é o citosol.

---

### Pergunta 2: Ponto isoelétrico e função biológica

Compare os valores de pI obtidos pelo ProtParam para as 5 proteínas. Albumina, p53, hemoglobina α e lisozima operam no mesmo ambiente fisiológico (pH ≈ 7,4), mas com cargas líquidas diferentes. Como o pI de cada proteína se relaciona com sua função ou com os parceiros moleculares com que ela interage?

> **Resposta:**
>
> O pI indica o pH no qual a proteína tem carga líquida zero. Em pH fisiológico (7,4), proteínas com pI abaixo de 7,4 são carregadas negativamente, e proteínas com pI acima de 7,4 são carregadas positivamente. Essa carga não é um detalhe físico-químico trivial: ela influencia diretamente a solubilidade, a estabilidade e as interações da proteína com seus parceiros moleculares.
>
> | Proteína | pI | Carga em pH 7,4 | Relevância funcional |
> |:---------|:--:|:---------------:|:---------------------|
> | Albumina | 5,73 | Negativa | Transportadora de ligantes catiônicos (drogas, metais, ácidos graxos) |
> | p53 | 6,07 | Negativa | Fator de transcrição; liga DNA carregado negativamente via resíduos básicos |
> | Insulina | 5,22 | Negativa | Hormônio secretado; interage com receptor na membrana celular |
> | Hemoglobina α | 8,72 | Positiva | Carreadora de O₂; interage com grupo heme e subunidade β |
> | Lisozima C | 9,50 | Positiva | Enzima antimicrobiana; age sobre superfície bacteriana carregada negativamente |
>
> A **albumina** (pI 5,73) é carregada negativamente, o que favorece a interação eletrostática com moléculas catiônicas como ácidos graxos, bilirrubina, íons metálicos e fármacos. Essa carga negativa também contribui para sua longa meia-vida no plasma sanguíneo.
>
> A **p53** (pI 6,07) também é levemente negativa. Apesar disso, ela se liga ao DNA (que é altamente negativo) por meio de resíduos de arginina e lisina positivos localizados no domínio de ligação ao DNA. A carga global levemente negativa não impede essa ligação, pois o contato é mediado por regiões específicas e não pela carga global da proteína.
>
> A **insulina** (pI 5,22) é a mais ácida entre as cinco. Em pH fisiológico, é bastante negativa, o que favorece sua solubilidade no sangue e a interação com regiões específicas do receptor de insulina.
>
> A **hemoglobina α** (pI 8,72) é carregada positivamente em pH 7,4. Isso é relevante para a interação com o grupo heme (que possui carga negativa) e para a associação com a subunidade β da hemoglobina, que possui pI mais ácido, criando complementaridade eletrostática na interface das subunidades.
>
> A **lisozima C** (pI 9,50) é a mais básica das cinco. Sua alta carga positiva em pH fisiológico permite a interação eletrostática com a parede celular bacteriana, que é carregada negativamente devido ao peptideoglicano e aos lipopolissacarídeos. Essa afinidade eletrostática é parte essencial do mecanismo de ação antimicrobiana da proteína.

---

### Pergunta 3: Índice GRAVY e solubilidade

Registre o índice GRAVY para as 5 proteínas. Proteínas solúveis tendem a ter GRAVY negativo, enquanto proteínas de membrana tendem a valores positivos. Os resultados obtidos são consistentes com as localizações subcelulares preditas pelo WoLFPSORT? Alguma proteína destoa do padrão esperado?

> **Resposta:**
>
> O índice GRAVY (*Grand Average of Hydropathicity*) mede o caráter hidrofóbico médio da sequência. Valores negativos indicam proteína hidrofílica e solúvel; valores positivos indicam maior hidrofobicidade, característica comum em proteínas de membrana ou com regiões transmembrana.
>
> | Proteína | GRAVY | Caráter | Localização (WoLFPSORT) | Consistente? |
> |:---------|:-----:|:-------:|:-----------------------:|:------------:|
> | Albumina | -0,329 | Hidrofílica | extr | Sim |
> | p53 | -0,677 | Muito hidrofílica | cyto_nucl | Sim |
> | Insulina | +0,193 | Levemente hidrofóbica | extr | Atenção |
> | Hemoglobina α | +0,048 | Quase neutro | cyto | Sim |
> | Lisozima C | -0,155 | Levemente hidrofílica | extr | Sim |
>
> A **albumina** e a **p53** apresentam os valores mais negativos, confirmando seu caráter hidrofílico e solúvel, consistente com as localizações no plasma e no núcleo, respectivamente.
>
> A **lisozima C** também é levemente hidrofílica, coerente com sua localização extracelular em fluidos biológicos.
>
> A **hemoglobina α** apresenta GRAVY quase neutro (+0,048). Isso reflete a presença de bolsões hidrofóbicos no interior da proteína, necessários para acomodar o grupo heme, combinada com uma superfície externa hidrofílica que garante a solubilidade no citoplasma dos eritrócitos. A localização citoplasmática predita pelo WoLFPSORT é consistente.
>
> A **insulina** é a proteína que mais destoa do padrão esperado: GRAVY positivo (+0,193), mas com localização extracelular. Isso pode ser explicado pelo fato de que o cálculo do GRAVY é feito sobre a **sequência completa da pré-pro-insulina** (110 resíduos), que inclui regiões hidrofóbicas do peptídeo sinal e do peptídeo C. A insulina madura (cadeias A e B, 51 resíduos) tem caráter mais hidrofílico. Portanto, o valor positivo não indica uma inconsistência biológica real, mas sim um artefato do uso da sequência precursora completa no cálculo.

---

### Pergunta 4: Estabilidade e meia-vida *in vivo*

O índice de instabilidade do ProtParam distingue proteínas estáveis (< 40) de instáveis (> 40). Compare os valores das 5 proteínas. A p53 apresenta valor elevado, biologicamente, por que faz sentido que um supressor de tumor seja uma proteína de curta duração? Qual das 5 proteínas é a mais estável segundo esse índice?

> **Resposta:**
>
> | Proteína | Índice de Instabilidade | Classificação |
> |:---------|:-----------------------:|:-------------:|
> | Albumina | 39,02 | Estável (< 40) |
> | p53 | 78,83 | Muito instável (>> 40) |
> | Insulina | 40,33 | Levemente instável (> 40) |
> | Hemoglobina α | 6,97 | Muito estável (<< 40) |
> | Lisozima C | 30,78 | Estável (< 40) |
>
> A **hemoglobina α** é a proteína mais estável, com índice de instabilidade de apenas 6,97. Isso é biologicamente coerente: os eritrócitos não possuem núcleo nem maquinaria de síntese proteica, portanto as proteínas do citoplasma precisam ser extremamente estáveis para durar os aproximadamente 120 dias de vida útil do eritrócito sem serem renovadas.
>
> A **albumina** e a **lisozima C** também são estáveis (índice abaixo de 40), o que faz sentido pois ambas precisam manter sua atividade no ambiente extracelular por períodos prolongados.
>
> A **insulina** fica ligeiramente acima do limiar de 40, o que é aceitável: hormônios secretados são produzidos em pulsos e degradados após exercerem seu efeito, não necessitando de estabilidade extrema.
>
> A **p53** apresenta o valor mais elevado (78,83), indicando alta instabilidade *in vivo*. Isso é biologicamente essencial: a p53 é um supressor de tumor que, se acumulada de forma descontrolada em células saudáveis, poderia induzir apoptose ou parada do ciclo celular de forma inadequada. Em condições normais, a proteína MDM2 se liga à p53 e a direciona para ubiquitinação e degradação pelo proteassoma, mantendo seus níveis muito baixos. Apenas em resposta a danos no DNA ou estresse celular, a degradação é inibida e os níveis de p53 sobem rapidamente. Ou seja, a **curta meia-vida da p53 é um mecanismo de segurança** que permite um controle rígido e rápido da resposta ao dano genômico. Uma proteína de longa duração nesse papel seria perigosa para a célula.

---

### Pergunta 5: Domínios conservados: CD-Search vs. InterProScan

Para cada proteína, quantos domínios foram reportados por cada ferramenta? Monte uma tabela comparativa indicando o domínio principal identificado e as bases de dados que o capturaram (Pfam, PANTHER, CDD, PRINTS etc.). Para quais proteínas as duas ferramentas apresentaram maior concordância e para quais divergiram mais? O que pode explicar essas diferenças?

> **Resposta:**
>
> | Proteína | Domínio principal (CD-Search) | GO Celular (InterPro) | Concordância |
> |:---------|:------------------------------|:----------------------|:------------:|
> | Albumina | ALBUMIN domain | Espaço extracelular (GO:0005615) | Alta |
> | p53 | TAD1, TAD2, P53 Binding domain | Núcleo (GO:0005634) | Alta |
> | Insulina | I/IGF_like superfamily | Região extracelular (GO:0005576) | Alta |
> | Hemoglobina α | Globin-like superfamily | Complexo hemoglobina (GO:0005833) | Alta |
> | Lisozima C | Lyz-like superfamily | None | Parcial |
>
> A maior concordância entre CD-Search e InterProScan ocorre para **albumina**, **p53** e **hemoglobina α**, pois são proteínas com domínios bem caracterizados em múltiplas bases de dados (Pfam, CDD, PANTHER). Ambas as ferramentas identificam as famílias corretas e as anotações GO são coerentes com o domínio identificado.
>
> A maior divergência ocorre para a **lisozima C**: o CD-Search identificou o domínio Lyz-like, mas o InterProScan não retornou nenhum componente celular GO. Isso pode ocorrer por limitações de cobertura da base de dados ou porque a anotação GO de componente celular para a lisozima é menos específica, já que ela é encontrada em vários fluidos biológicos distintos.
>
> Do ponto de vista metodológico, o **CD-Search** usa principalmente a base CDD (*Conserved Domain Database*) com extensões de Pfam e TIGRFAM, enquanto o **InterProScan** integra Pfam, PANTHER, HAMAP, PRINTS, ProSite e outras. Quando as bases concordam, a confiança na anotação é maior. Quando divergem, pode indicar que o domínio é bem conservado apenas em algumas famílias, que a proteína possui características únicas não capturadas igualmente por todas as bases, ou simplesmente que a cobertura das bases de dados é diferente para aquela família específica.

---

### Pergunta 6: Localização subcelular predita vs. experimental

O WoLFPSORT prediz a localização de cada proteína. Compare as predições com a localização experimental descrita no UniProt. Quantas e quais predições estão corretas? Para os casos incorretos ou ambíguos, qual característica de sequência pode ter induzido o erro?

> **Resposta:**
>
> | Proteína | Predito (WoLFPSORT) | Experimental (UniProt) | Correto? |
> |:---------|:-------------------:|:-----------------------:|:--------:|
> | Albumina | extr | Plasma / extracelular | Sim |
> | p53 | cyto_nucl | Núcleo | Parcialmente |
> | Insulina | extr | Extracelular (sangue) | Sim |
> | Hemoglobina α | cyto | Citoplasma (eritrócito) | Sim |
> | Lisozima C | extr | Secretada (saliva, lágrimas) | Sim |
>
> Quatro das cinco predições estão totalmente corretas. Para a **p53**, o WoLFPSORT predisse localização dupla (cyto_nucl), enquanto a localização experimental primária é o núcleo. Essa predição dupla é compreensível: a p53 é sintetizada no citoplasma e importada para o núcleo, portanto a sequência contém características que levam o algoritmo a pontuar ambos os compartimentos. Não se trata de um erro, mas de uma ambiguidade que reflete o trajeto real da proteína na célula.
>
> O WoLFPSORT utiliza características da sequência primária (composição de aminoácidos, presença de sinais de localização) sem considerar contexto celular, mecanismos de importação nuclear ativos nem dados evolutivos. Isso explica por que proteínas com sinais de localização múltiplos ou que transitam entre compartimentos podem gerar predições ambíguas. No caso da p53, a presença do NLS (sinal de localização nuclear) combinada com a composição aminoacídica compatível com proteínas citoplasmáticas induz o algoritmo a reportar os dois compartimentos simultaneamente.

---

### Pergunta 7: Processamento proteolítico e modelagem estrutural

Albumina, pré-pró-insulina e lisozima passam por clivagem proteolítica após a tradução. Para cada uma, identifique: (a) o sítio de clivagem predito pelo SignalP, (b) o tamanho da proteína madura resultante e (c) se o SignalP identificou corretamente o sítio em relação à anotação UniProt. Se você fosse modelar estruturalmente essas proteínas, usaria a sequência completa ou apenas a cadeia madura? Justifique.

> **Resposta:**
>
> | Proteína | Sítio de clivagem (SignalP) | Proteína madura | Correto vs. UniProt? |
> |:---------|:--------------------------:|:---------------:|:--------------------:|
> | Albumina | Entre aa 18 e 19 | 585 aa (resíduos 25-609, após remoção do sinal + propeptídeo) | Sim |
> | Insulina | Entre aa 24 e 25 | Cadeias A + B (51 aa, após remoção do sinal e do peptídeo C) | Sim |
> | Lisozima C | Entre aa 18 e 19 | 130 aa (resíduos 19-148) | Sim |
>
> A **albumina** possui peptídeo de sinal (aa 1-18) e propeptídeo (aa 19-24). O SignalP identificou corretamente o sítio de clivagem entre os resíduos 18 e 19. A proteína madura começa no resíduo 25 e tem 585 aminoácidos, consistente com a anotação UniProt.
>
> A **insulina** representa o caso mais complexo: a pré-pro-insulina (110 aa) possui peptídeo de sinal (aa 1-24), cadeia B (aa 25-54), peptídeo C (aa 57-87) e cadeia A (aa 90-110). O SignalP identificou corretamente o sítio de clivagem do peptídeo de sinal entre os resíduos 24 e 25. Após isso, a pró-insulina (cadeia B + peptídeo C + cadeia A) é processada por endopeptidases nas grânulas secretoras, removendo o peptídeo C. A insulina madura é formada pelas cadeias A e B unidas por duas pontes dissulfeto, totalizando 51 aminoácidos.
>
> A **lisozima C** possui peptídeo de sinal de 18 aminoácidos. O SignalP identificou corretamente o sítio entre os resíduos 18 e 19. A proteína madura tem 130 aminoácidos e é secretada em fluidos biológicos.
>
> Para a **modelagem estrutural**, deve-se usar **apenas a sequência da proteína madura**, sem o peptídeo de sinal e sem propeptídeos. O motivo é direto: o peptídeo de sinal é uma sequência transitória que não faz parte da estrutura funcional final da proteína. Sua inclusão introduziria regiões desordenadas no modelo que não existem na proteína biologicamente ativa, comprometendo a qualidade da modelagem, a interpretação do modelo e potencialmente os experimentos de *docking* e dinâmica molecular realizados a partir dele.

---

### Pergunta 8: Domínio funcional e estrutura experimental

O InterProScan identifica o domínio de ligação ao DNA (DBD) da p53 entre quais resíduos? Compare esses limites com a região cristalizada no PDB (entrada **1TUP**, resíduos 94-292). Da mesma forma, o CD-Search ou InterProScan fazem referência ao bolsão de ligação ao heme na hemoglobina α? O que essa comparação entre predição *in silico* e estrutura experimental revela sobre a utilidade e as limitações dessas ferramentas?

> **Resposta:**
>
> O InterProScan identifica o domínio de ligação ao DNA (DBD) da p53 em uma região que coincide aproximadamente com os resíduos 94-292, exatamente a região cristalizada na estrutura experimental depositada no PDB sob o código **1TUP**. Essa concordância é um exemplo de como as ferramentas de bioinformática são eficazes para identificar domínios evolutivamente conservados e funcionalmente essenciais, como o DBD da p53, que é altamente conservado entre vertebrados e amplamente representado nas bases de dados.
>
> Para a **hemoglobina α**, tanto o CD-Search quanto o InterProScan identificam o domínio *Globin-like superfamily*, que é o domínio estrutural correto da família. Porém, **nenhuma das ferramentas descreve explicitamente o bolsão de ligação ao grupo heme** como um domínio separado. Isso ocorre porque esse bolsão é formado pela conformação tridimensional da proteína, especificamente pelos resíduos de histidina proximal e distal que coordenam o ferro do grupo heme. Esse tipo de característica funcional não corresponde a uma sequência linear conservada independente, mas sim a uma estrutura espacial que emerge apenas quando a proteína está dobrada.
>
> Essa comparação revela dois pontos importantes sobre o uso de ferramentas *in silico*:
>
> **Ponto forte:** as ferramentas são muito eficazes para identificar domínios com sequências conservadas ao longo da evolução, como famílias de fatores de transcrição, domínios enzimáticos e famílias estruturais bem caracterizadas com perfis HMM (*Hidden Markov Models*) robustos em bases como Pfam e PANTHER.
>
> **Limitação:** as ferramentas têm desempenho reduzido quando a função depende de características estruturais tridimensionais, como bolsões de ligação a ligantes pequenos (heme, ATP, zinco), interfaces de oligomerização e regiões intrinsecamente desordenadas que adquirem estrutura apenas ao interagir com parceiros moleculares. Para esses casos, a complementação com dados estruturais experimentais obtidos por cristalografia de raios X, crioEM ou NMR continua sendo insubstituível.

---

# Momento II

**Proteína-Alvo:** p53 (*TP53*)

Este repositório contém o material prático do curso de Biologia Estrutural Computacional, utilizando a proteína supressora de tumor p53 como sistema modelo para explorar diferentes métodos de predição e análise estrutural.

<figure class="figure-center">
  <img src="imgs/p53.png" alt="XXXXX" width="550">
</figure>

Estrutura tridimensional da p53, em complexo com uma estrutura de DNA. As subunidades da p53, mostradas em azul e roxo, são visualizadas usando uma combinação de representação "cartoon", que revela a estrutura secundária de hélices alfa e fitas beta, e uma "superfície" molecular translúcida, que indica o volume de e a forma da proteína. A p53 é mostrada interagindo diretamente com a dupla hélice do DNA, representada em laranja, através de seu domínio de ligação ao DNA (DBD). A presença de esferas (íons de zinco, em verde) destaca componentes cruciais para a estabilidade estrutural do DBD, formando os zinc fingers. Esta interação é fundamental para a função da p53, permitindo que ela se ligue a regiões específicas do genoma para regular a expressão de genes envolvidos no controle do ciclo celular, no reparo de danos ao DNA e na indução da apoptose, prevenindo assim a oncogênese e assim, mantendo a homeostase celular.

---

# Sobre a Proteína p53

A **p53** (derivada do gene *TP53*) é um dos mais importantes supressores de tumor, frequentemente referida como **"a guardiã do genoma"**. Esta proteína é crucial para a regulação do ciclo celular e prevenção do câncer.

## Relevância Científica

- Mutada em **mais de 50% de todos os cânceres humanos**
- Proteína mais estudada na história da oncologia.
- Alvo ideal para comparar diferentes métodos de modelagem computacional.

<figure class="figure-center">
  <img src="imgs/adobe.gif" alt="XXXXX" width="500">
</figure>

> Fonte: Criado por Madson Aragão no VMD.

## Dados de Importantes

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

# Instalação do PyMOL

O PyMOL é o único software que precisará ser instalado localmente para este curso. Utilizaremos a versão **Incentive PyMOL**, gratuita para estudantes e educadores.

## A. Obtenção da Licença de Estudante (Gratuita)

1. Acesse o portal educacional da Schrödinger: <a href="https://pymol.org/edu/" target="_blank">https://pymol.org/edu/</a>.
2. Clique em **"Register for an Account"**
3. **IMPORTANTE:** Utilize seu **e-mail institucional** (ex: `seu.usuario@ufpe.br`).
   - A licença acadêmica está vinculada à verificação de um domínio educacional
4. Siga as instruções de verificação enviadas ao seu e-mail
5. Após aprovação, faça o download do arquivo de licença (`license.lic`).
6. Salve o arquivo em um local de fácil acesso (ex: Área de Trabalho).

## B. Download e Instalação

Na página de downloads da sua conta Schrödinger, baixe o instalador apropriado para seu sistema operacional pelo site <a href="https://pymol.org/edu/" target="_blank">https://pymol.org/edu/</a>


## C. Ativação da Licença

1. Inicie o PyMOL pela primeira vez.
2. O programa solicitará a ativação.
3. Escolha a opção **"I have a license file"**.
4. Navegue até o local do arquivo `license.lic` e selecione-o.
5. O PyMOL será ativado e estará pronto para uso.

---

# Análise Exploratória

**Objetivos:**
- Navegar e extrair dados da p53 em bancos de dados estruturais.
- Utilizar ferramentas web para predição de características bioquímicas.

## Bancos de Dados

| Recurso | URL | Descrição |
|---------|-----|-----------|
| **UniProt** | <a href="https://www.uniprot.org/" target="_blank">https://www.uniprot.org/</a> | Informações de sequência e anotações funcionais |
| **PDB** | <a href="https://www.rcsb.org/" target="_blank">https://www.rcsb.org/</a> | Estruturas tridimensionais experimentais |

---

# Modelagem Tridimensional 

## Alinhamento 1TUP vs. Sequência Completa

**Alinhamento 1TUP vs. Sequência Completa (WT):** Temos as sequências FASTA do domínio de ligação ao DNA da p53 e sua sequência completa (WT), e, juntos, executaremos o alinhamento múltiplo no <a href="https://www.ebi.ac.uk/jdispatcher/msa/clustalo" target="_blank" rel="noopener noreferrer">Clustal Omega</a>. Analise quais regiões se alinham diretamente, discuta as diferenças e vamos entender as implicações biológicas dessas variações. Ter apenas "uma parte" da proteína pode ser suficiente para algumas análises? Isso depende do contexto biológico?

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
GSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
```

## Perguntas:

- Em quais trechos o domínio 1TUP se alinha diretamente com a sequência completa e quais regiões ficam sem correspondência?
- Os limites N- e C-terminais do domínio cristalizado aparecem contíguos no alinhamento ou revelam lacunas/extensions relevantes para estabilidade?
- Há resíduos-chave do sítio de ligação ao DNA presentes apenas na sequência completa? O que isso implica para os modelos baseados no domínio?

> **Respostas:**
>
> **Quais trechos se alinham e quais ficam sem correspondência?**
>
> O domínio cristalizado na estrutura 1TUP corresponde ao DBD (DNA-Binding Domain) da p53, que cobre aproximadamente os resíduos 94 a 292 da sequência completa (393 aa). No alinhamento múltiplo executado no Clustal Omega, você verá que a sequência do 1TUP se alinha diretamente com essa região central da proteína completa. As regiões **sem correspondência** com o 1TUP são:
>
> | Domínio | Resíduos (UniProt) | Presente no 1TUP? |
> |:--------|:-----------------:|:-----------------:|
> | TAD1 (domínio de ativação transcricio nal 1) | 1-40 | Não |
> | TAD2 (domínio de ativação transcricional 2) | 41-67 | Não |
> | PRD (domínio rico em prolina) | 68-93 | Não |
> | **DBD (domínio de ligação ao DNA)** | **94-292** | **Sim** |
> | NLS (sinal de localização nuclear) | 293-325 | Não |
> | OD (domínio de oligomerização) | 326-356 | Não |
> | CTD (domínio C-terminal regulatório) | 357-393 | Não |
>
> Isso significa que, no alinhamento, a sequência do 1TUP aparece com gaps (inserções de "-") nos terminais N e C, enquanto o corpo central se alinha perfeitamente com a sequência completa.
>
> **Os limites do domínio cristalizado revelam lacunas relevantes?**
>
> Sim. O limite N-terminal do 1TUP começa abruptamente na região do DBD, sem nenhuma das sequências N-terminais de ativação transcricional (TAD1, TAD2 e PRD). O limite C-terminal termina logo após o final do DBD, antes do domínio de oligomerização (OD). Essa ausência tem implicações estruturais importantes: o OD é responsável pela formação do tetrâmero funcional da p53 (quatro subunidades), e o CTD possui sítios de ubiquitinação e acetilação que regulam a atividade da proteína. Portanto, a estrutura cristalizada no 1TUP captura apenas o "coração" funcional da p53 para a ligação ao DNA, mas não a proteína completa.
>
> **Há resíduos-chave do sítio de ligação ao DNA presentes apenas na sequência completa?**
>
> Não exatamente. Os resíduos que fazem contato direto com o DNA (como R248 e R273, presentes no Loop L3, e K120, S241, R248, presente nas fitas beta do DBD) estão todos dentro da janela do 1TUP (resíduos 94-292). Portanto, a estrutura cristalizada contém todos os resíduos essenciais para a ligação ao DNA.
>
> Porém, modelos baseados **apenas no domínio** do 1TUP têm limitações importantes: não é possível modelar a oligomerização (sem o OD, a proteína não forma o tetrâmero), não é possível analisar a regulação pelo CTD (sítios de modificação pós-traducional), e as regiões TAD1 e TAD2 que recrutam cofatores transcricionais ficam completamente ausentes. Portanto, para estudar a ligação ao DNA, o fragmento do 1TUP é suficiente; para estudar a regulação e a função completa da p53, é necessária a sequência *full-length*.

---

# Atividade 3: Análise de Mutações Oncogênicas

> **Atividade (EXTRA):** Temos 5 sequências da p53 (1 referência *wild-type* e 4 variantes associadas a neoplasias) e, juntos, executaremos o alinhamento múltiplo no <a href="https://www.ebi.ac.uk/jdispatcher/msa/clustalo" target="_blank" rel="noopener noreferrer">Clustal Omega</a>. Analise quais substituições coincidem com domínios funcionais críticos, discuta como essas mudanças podem impactar estabilidade e interação com DNA e, por fim, decidam coletivamente qual variante seguirá para aprofundamento nas etapas práticas.

> Baixe aqui o arquivo multiFASTA com as 5 sequências: <a href="https://drive.google.com/file/d/1qpbnbvNjTRcvvG-UsXdiJYXvynkdvxYw/view?usp=sharing" target="_blank">multiFASTA_p53_variants.fasta</a>

## Sequências para Análise

### Wild-Type (Sequência Canônica - 393 aa)

```
>sp|P04637|P53_HUMAN_WT Cellular tumor antigen p53
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGP
DEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAK
SVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHE
RCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNS
SCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELP
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

> O que vocês acharam desse alinhamento? Vamos discutir as possíveis implicações biológicas dessas mutações?

> Para relembrar, abaixo temos uma tabela com todos os aminoácidos e suas características físico-químicas, caso queiram consultar durante a análise das mutações.

<p align="justify">
  <img src="imgs/aas.png" alt="Amino acids width="1000">
</p>

> Fonte: JPT Peptide Technologies.

---

## Localização das Mutações no Domínio de Ligação ao DNA (aa 102-292)

| Mutação | Posição | Região | AA WT | AA Mut | Contexto | Caráter WT | Caráter Mut | Carga WT | Carga Mut | Volume WT | Volume Mut |
|---------|---------|--------|-------|--------|----------|------------|-------------|----------|-----------|-----------|------------|
| **R175H** | 175 | Loop L2 | R | H | `...GTR**V**RAM...` → `...GTH**V**RAM...` | Básico forte | Básico fraco | Positiva (+) | Parcial/pH-dependente | 148 Å³ | 118 Å³ (-40%) |
| **Y220C** | 220 | Loop L3 | Y | C | `...RVE**Y**LDD...` → `...RVE**C**LDD...` | Aromático polar | Polar alifático (tiol) | Neutro | Neutro | 141 Å³ | 86 Å³ (-65%) |
| **R248Q** | 248 | Loop L3 | R | Q | `...GMN**R**RPI...` → `...GMN**Q**RPI...` | Básico forte | Polar neutro | Positiva (+) | Neutro | 148 Å³ | 114 Å³ (-15%) |
| **R273H** | 273 | Folha β | R | H | `...LLG**R**NSF...` → `...LLG**H**NSF...` | Básico forte | Básico fraco | Positiva (+) | Parcial/pH-dependente | 148 Å³ | 118 Å³ (-40%) |

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
  

## Representação das Mutações (Cadeias Laterais)

### Mutação R175H (Arginina → Histidina)

**ANTES: Arginina (R)**
```
        NH₂⁺
        |
        C=NH₂⁺
        |
        NH
        |
        (CH₂)₃
        |
    Cα--C
```
- **Carga**: Positiva (+1)
- **pKa**: ~12.5
- **Características**: Básica, hidrofílica, longa cadeia alifática

**DEPOIS: Histidina (H)**
```
        NH⁺
       /  \
      HC   CH
       \\  /
        N—C
        |
        CH₂
        |
    Cα--C
```
- **Carga**: Positiva/Neutra (dependente do pH)
- **pKa**: ~6.0
- **Características**: Básica fraca, imidazol, menor carga que Arg

**Impacto**: Perda de carga positiva forte → Afeta interação com DNA

---

### Mutação Y220C (Tirosina → Cisteína)

**ANTES: Tirosina (Y)**
```
        OH
        |
       C6H4 (anel benzênico)
        |
        CH₂
        |
    Cα--C
```
- **Carga**: Neutra (polar)
- **Características**: Aromática, volumosa, hidroxila fenólica
- **Ligações**: π-π stacking, pontes de hidrogênio

**DEPOIS: Cisteína (C)**
```
        SH
        |
        CH₂
        |
    Cα--C
```
- **Carga**: Neutra
- **Características**: Pequena, tiol reativo, forma pontes dissulfeto
- **Potencial**: S-S (dimerização ou oxidação)

**Impacto**: Perda de aromático volumoso → Instabilidade estrutural

---

### Mutação R248Q (Arginina → Glutamina)

**ANTES: Arginina (R)**
```
        NH₂⁺
        |
        C=NH₂⁺
        |
        NH
        |
        (CH₂)₃
        |
    Cα--C
```
- **Carga**: Positiva (+1)
- **pKa**: ~12.5
- **Características**: Básica, guanidina carregada

**DEPOIS: Glutamina (Q)**
```
        O
        ‖
        C—NH₂
        |
        CH₂
        |
        CH₂
        |
    Cα--C
```
- **Carga**: Neutra
- **Características**: Polar, amida não carregada
- **Potencial**: Pontes de hidrogênio fracas

**Impacto**: Perda completa de carga positiva → Perda de contato com DNA

---

### Mutação R273H (Arginina → Histidina)

**ANTES: Arginina (R)**
```
        NH₂⁺
        |
        C=NH₂⁺
        |
        NH
        |
        (CH₂)₃
        |
    Cα--C
```
- **Carga**: Positiva (+1)
- **pKa**: ~12.5
- **Características**: Longa, flexível, sempre protonada em pH fisiológico

**DEPOIS: Histidina (H)**
```
        NH⁺/N
       /  \
      HC   CH
       \\  /
        N—C
        |
        CH₂
        |
    Cα--C
```
- **Carga**: Variável (pH dependente)
- **pKa**: ~6.0
- **Características**: Anel imidazol, protonação reversível

**Impacto**: Troca de carga permanente por carga pH-dependente

---

## Perguntas para Discussão:

- Em quais posições do alinhamento múltiplo surgem substituições e essas posições são conservadas na sequência *wild-type*?
- As mutações identificadas representam trocas conservativas ou drásticas em termos de propriedades físico-químicas (ex.: troca de polar para hidrofóbico)?
- Alguma das substituições cria ou elimina motivos funcionais conhecidos (ex.: sítios de fosforilação, ligações a DNA) sugeridos pelo alinhamento?
- Comparando as quatro variantes mutadas entre si, existe um padrão recorrente de substituições que aponte para um hotspot funcional?

> **Respostas:**
>
> **Em quais posições surgem substituições e elas são conservadas?**
>
> As substituições surgem exatamente nas posições 175, 220, 248 e 273 do alinhamento, todas localizadas dentro do DBD (resíduos 102-292). Essas posições são altamente conservadas na sequência *wild-type* e entre os ortólogos da p53 em diferentes espécies de vertebrados. No histograma de conservação do Clustal Omega, essas colunas aparecem com marcação de conservação máxima na sequência de referência WT, o que significa que a pressão evolutiva manteve esses resíduos inalterados por milhões de anos em organismos saudáveis. Encontrá-los substituídos em tumores humanos é, portanto, biologicamente muito significativo.
>
> **As mutações são conservativas ou drásticas?**
>
> | Mutação | Troca | Tipo de mudança | Impacto esperado |
> |:--------|:-----:|:---------------:|:-----------------|
> | R175H | Arg (básico, +1) → His (básico fraco, pH-dep.) | Moderadamente drástica | Perda de carga permanente, desestabilização do domínio |
> | Y220C | Tyr (aromático, polar) → Cys (tiol reativo, pequeno) | Muito drástica | Perda do aromático volumoso, criação de tiol livre reativo |
> | R248Q | Arg (básico, +1) → Gln (polar neutro) | Muito drástica | Perda completa de carga; R248 faz contato direto com o DNA |
> | R273H | Arg (básico, +1) → His (básico fraco, pH-dep.) | Moderadamente drástica | Perda de carga permanente; R273 faz contato direto com o DNA |
>
> Nenhuma das quatro mutações é conservativa: todas alteram de forma significativa a carga, o volume ou a reatividade química do resíduo original. Isso contrasta com mutações conservativas típicas, como Asp → Glu (ambos ácidos) ou Val → Ile (ambos alifáticos).
>
> **Alguma substituição elimina motivos funcionais conhecidos?**
>
> Sim, e de forma direta. As mutações R248Q e R273H eliminam dois dos principais contatos da p53 com o DNA. O resíduo R248 insere sua cadeia lateral no sulco menor do DNA e faz pontes de hidrogênio com bases específicas da sequência reconhecida pela p53. Ao ser substituído por Gln (glutamina), a carga positiva e a geometria de ligação são perdidas completamente, abolindo o contato com o DNA. O mesmo vale para R273, que faz contato com o esqueleto fosfato do DNA.
>
> A mutação R175H, embora não seja um contato direto com o DNA, afeta a coordenação estrutural de um íon zinco (Zn²+) no DBD. O zinco é coordenado por resíduos C176, H179, C238 e C242, e a arginina 175 está próxima a esse sítio. A substituição por histidina desestabiliza a estrutura tridimensional do DBD inteiro, o que indiretamente elimina o sítio de ligação ao DNA mesmo sem mudar um resíduo de contato.
>
> A mutação Y220C cria um tiol livre (grupo -SH da cisteína), que pode formar pontes dissulfeto aberrantes com outras cisteínas do DBD, contribuindo para agregação proteica, uma característica frequentemente observada em células tumorais com p53 mutante.
>
> **Existe um padrão recorrente entre as quatro variantes?**
>
> Sim, e é bastante evidente. Três das quatro mutações (R175H, R248Q e R273H) envolvem a substituição de uma **arginina** por um aminoácido de carga reduzida ou neutra. A arginina possui o pKa mais alto entre todos os aminoácidos (~12,5) e permanece carregada positivamente em praticamente todo pH fisiológico. Ela é o aminoácido ideal para fazer contato eletrostático com o DNA (carregado negativamente) e para estabilizar estruturas pelo seu grupo guanidínio altamente versátil em pontes de hidrogênio.
>
> Esse padrão aponta para um **hotspot funcional de argininas críticas** no DBD da p53. Não por acaso, as posições 175, 248 e 273 estão entre as mutações mais frequentes em tumores humanos catalogadas no banco de dados IARC TP53. Isso revela que a evolução dos tumores não é aleatória: ela seleciona positivamente mutações que inativam especificamente os resíduos mais essenciais para a função supressora da p53.

---

# Modelagem por Homologia e Threading

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

## Modelagem por Homologia (SWISS-MODEL)

**Plataforma:** SWISS-MODEL  
**URL:** <a href="https://swissmodel.expasy.org/" target="_blank">https://swissmodel.expasy.org/</a>

**Análise:**
- Avaliar alinhamentos sequência-molde
- Examinar cobertura e identidade de sequência

---

## Atividade Prática: SWISS-MODEL

Nesta parte da atividade iremos utilizar o <a href="https://swissmodel.expasy.org/" target="_blank">https://swissmodel.expasy.org/</a> umas das plataformas mais populares para modelagem por homologia. O SWISS-MODEL é um servidor web automatizado para a construção de modelos tridimensionais de proteínas com base em sequências de aminoácidos. Ele utiliza uma abordagem de modelagem por homologia, onde a estrutura de uma proteína alvo é prevista com base na similaridade com proteínas de estrutura conhecida (modelos).

Existem outras plataformas populares para modelagem por homologia, como o Phyre2 (<a href="http://www.sbg.bio.ic.ac.uk/phyre2/html/page.cgi?id=index" target="_blank">http://www.sbg.bio.ic.ac.uk/phyre2/html/page.cgi?id=index</a>) e o MODELLER (<a href="https://salilab.org/modeller/" target="_blank">https://salilab.org/modeller/</a>), cada uma com suas próprias características e algoritmos.

Mas nesta atividade, focaremos no SWISS-MODEL devido à sua interface amigável e ampla aceitação na comunidade científica as excelentes métricas de avaliação de modelos que ele fornece, além de ser online e gratuito para uso acadêmico.

<p align="justify">
  <img src="imgs/swissssss.png" alt="Amino acids width="1000">
</p>

> Fonte: Recorte de tela do SWISS-MODEL em uso. 

---

## Modelagem por Threading (I-TASSER)

**Plataforma:** I-TASSER  
**URL:** <a href="https://zhanggroup.org/I-TASSER/" target="_blank">https://zhanggroup.org/I-TASSER/</a>


<p align="justify">
  <img src="imgs/itasser.png" alt="Amino acids width="1000">
</p>

> I-TASSER Server Interface. Fonte: <a href="https://zhanggroup.org/I-TASSER/" target="_blank">https://zhanggroup.org/I-TASSER/</a>.

O I-TASSER (Iterative Threading ASSEmbly Refinement) é um conjunto de métodos para predição de estrutura e função de proteínas. Ele utiliza uma abordagem hierárquica que combina métodos de *threading* e simulações *ab initio* de refinamento.

Devido ao alto custo computacional dos algoritmos e ao tempo de espera significativo em servidores públicos (decorrente de filas de processamento), a sequência da **p53 humana completa** (*full-length*) foi submetida previamente.

O cálculo utilizando threading no I-TASSER levou aproximadamente **48 horas** para ser concluído. Por isso, adiantei o processo para que possamos focar na análise dos resultados. Mas vou mostrar rapidamente como foi feita a submissão no <a href="https://zhanggroup.org/I-TASSER/" target="_blank">https://zhanggroup.org/I-TASSER/</a>.

Os resultados completos da predição estão disponíveis no servidor do I-TASSER por 30 dias, sob o **Job ID: S814816**.

> Acessível em: https://aideepmed.com/I-TASSER/output/S820553/

Nesta seção, o foco não será a submissão ou a espera pelo processamento, mas sim a análise detalhada dos resultados gerados. Discutiremos o processo de construção da estrutura, a geração de múltiplos modelos (Top 5) e a interpretação das métricas de confiança, como o **C-score** (Confidence Score) e o **TM-score** (Template Modeling score), para avaliar a qualidade e a topologia de cada modelo predito.

<figure class="figure-center">
  <img src="imgs/denovo.png" alt="XXXXX" width="600">
</figure>

> Uma ilustração do processo de comparação a cada passo que um fragmento (k=3 ou k=9) é extraído da sequência alvo e alinhado a uma estrutura de proteína conhecida. Fonte: Chen, J.; Siu, S.W.I. Machine Learning Approaches for Quality Assessment of Protein Structures. Biomolecules 2020, 10, 626. https://doi.org/10.3390/biom10040626

**Métricas:**
- **C-score:** Confiança da predição (-5 a 2, valores mais altos = melhor)
- **TM-score:** Similaridade estrutural

---

## Primeira Validação

### Perguntas:

- Qual seria o melhor modelo obtido entre SWISS-MODEL e I-TASSER? Justifique com base nas métricas apresentadas.
- O tipo de construção (homologia vs threading) influenciou a qualidade do modelo? Explique...
- Vamos revisar os métodos utilizados até aqui. Quais são as vantagens e limitações de cada abordagem?
- Ainda não alinhamos as estruturas obtidas até aqui, mas conseguem identificar diferenças visuais entre os modelos gerados?

> **Respostas:**
>
> **Qual seria o melhor modelo entre SWISS-MODEL e I-TASSER?**
>
> Para responder com base em métricas, precisamos comparar os valores reportados por cada ferramenta. O SWISS-MODEL fornece o **GMQE** (*Global Model Quality Estimation*, 0 a 1, quanto maior melhor) e o **QMEANDisCo** (0 a 1, baseado em consenso com estruturas do PDB). O I-TASSER fornece o **C-score** (-5 a 2, quanto maior melhor) e estimativas de **TM-score** e **RMSD** em relação a estruturas similares.
>
> Para a p53 *full-length*, é esperado que o **SWISS-MODEL produza um modelo parcial** (cobrindo principalmente o DBD, onde existe molde experimental de alta qualidade como o 1TUP), enquanto o **I-TASSER gera um modelo completo** da cadeia inteira usando threading e montagem por fragmentos. Portanto, a comparação direta deve considerar a cobertura de sequência: um modelo de alta qualidade que cobre apenas 60% da proteína pode ser menos útil do que um modelo de qualidade moderada que cobre 100%.
>
> Em termos de GMQE e QMEANDisCo, um modelo do DBD pelo SWISS-MODEL tende a ter valores altos (próximos de 0,8-0,9) porque existe um molde experimental excelente (1TUP). Já o TM-score predito pelo I-TASSER para a p53 completa costuma ficar entre 0,6 e 0,8, indicando dobramento correto na topologia geral mas com imprecisões em loops e regiões desordenadas.
>
> **O tipo de abordagem influenciou a qualidade do modelo?**
>
> Sim, de forma significativa. A modelagem por **homologia** (SWISS-MODEL) depende diretamente da existência de um molde estrutural com alta identidade de sequência. Para o DBD da p53, que possui dezenas de estruturas experimentais depositadas no PDB, o SWISS-MODEL encontra moldes excelentes e produz modelos de alta fidelidade para essa região. No entanto, para as regiões N-terminais (TAD1, TAD2, PRD) e C-terminais (OD, CTD), que são naturalmente desordenadas ou possuem poucos moldes, o SWISS-MODEL não consegue construir um modelo confiável.
>
> O **threading** (I-TASSER) não depende de identidade de sequência direta: ele alinha fragmentos da sequência a perfis de estruturas do PDB mesmo com baixa similaridade, o que permite cobrir toda a cadeia. O resultado é um modelo completo, mas com regiões de confiança variável ao longo da sequência, especialmente nas regiões intrinsecamente desordenadas da p53.
>
> **Vantagens e limitações de cada abordagem:**
>
> | Critério | Homologia (SWISS-MODEL) | Threading (I-TASSER) |
> |:---------|:-----------------------:|:--------------------:|
> | Cobertura | Parcial (depende do molde) | Total da sequência |
> | Qualidade do núcleo estrutural | Alta (quando molde existe) | Moderada a boa |
> | Regiões sem molde | Não modela | Modela com menor confiança |
> | Velocidade | Minutos | Horas a dias |
> | Interpretação das métricas | GMQE, QMEANDisCo | C-score, TM-score estimado |
>
> **Diferenças visuais esperadas entre os modelos:**
>
> Mesmo antes de calcular o RMSD, é possível identificar diferenças visuais ao inspecionar os modelos no PyMOL. O modelo do SWISS-MODEL deve apresentar o DBD bem estruturado com folhas beta e alças definidas, mas com cadeias N e C-terminais ausentes ou como extensões desordenadas. O modelo do I-TASSER deve apresentar a proteína completa, mas com regiões TAD1, TAD2 e CTD em conformações estendidas ou aleatórias, refletindo o caráter intrinsecamente desordenado dessas regiões. O núcleo do DBD deve ter topologia similar nos dois modelos, mas com diferenças na posição das alças laterais e na orientação das cadeias terminais.

> Nos próximos módulos, vamos avaliar se o dobramento por cada método foi feito da corretamente. Bem como alinhar estruturalmente os modelos obtidos, calculando RMSD para comparação detalhada.

---

# E o *Ab Initio*?

O Rosetta revolucionou a biologia estrutural computacional ao introduzir métodos inovadores para a predição de estruturas de proteínas. Desenvolvido inicialmente por David Baker e sua equipe na Universidade de Washington, o Rosetta utiliza uma abordagem baseada em fragmentos para construir modelos tridimensionais de proteínas a partir de suas sequências de aminoácidos. 

A proteína Top-7, projetada computacionalmente usando Rosetta, é um exemplo notável de como a modelagem *ab initio* pode ser eficaz. Esta proteína foi criada para ter uma estrutura estável e bem definida, demonstrando a capacidade do Rosetta de prever estruturas de proteínas que não possuem homólogos conhecidos na natureza. **Ela foi a primeira proteína projetada inteiramente por métodos computacionais a ser cristalizada e ter sua estrutura determinada experimentalmente, validando a precisão das predições do Rosetta.**

A Top-7 possui uma estrutura composta por hélices alfa e folhas beta, formando um núcleo hidrofóbico compacto. Sua criação envolveu a seleção cuidadosa de fragmentos estruturais, a otimização da sequência para estabilidade e a validação experimental através de cristalografia de raios X.

Foi (e ainda é) um marco na engenharia de proteínas, ilustrando o potencial da modelagem computacional para projetar novas proteínas com funções específicas, abrindo caminho para avanços em biotecnologia e medicina.

> Kuhlman B, Dantas G, Ireton GC, Varani G, Stoddard BL, Baker D. Design of a novel globular protein fold with atomic-level accuracy. Science. 2003 Nov 21;302(5649):1364-8. doi: 10.1126/science.1089427. PMID: 14631033.

> Baixem o paper descrevendo a Top-7 pela primeira vez aqui: <a href="https://drive.google.com/file/d/1i55VKkRIEOy2FjWYRb8AQYZoN1JDNSzE/view?usp=sharing" target="_blank">Design of a novel globular protein fold with atomic-level accuracy.</a>

<figure class="figure-center">
  <img src="imgs/scafold.png" alt="XXXXX" width="650">
</figure>

> A imagem, no quadro superior, mostra a densidade eletrostática da superfície da proteína Top-7, destacando suas características estruturais de alta acurácia na obtenção por cristalografia de raios X. No quadro inferior, a representação em fita ilustra a topologia da proteína, evidenciando suas hélices alfa e folhas beta organizadas de forma compacta. Fonte: Baker, D. et al., Science, 2003.

**A Top-7 serve como uma scaffold sintético** com duas alças, fitas beta e hélices alfa, podem ser substituídas por sequências que tenham a mesma topologia, mas com diferentes propriedades funcionais. Transformando a Top-7 em uma plataforma versátil para engenharia de proteínas.

Seu nome *Top-7* faz referência á sua topologia, composta por 7 elementos secundários (4 hélices alfa e 3 fitas beta) organizados em uma estrutura globular estável.

<figure class="figure-center">
  <img src="imgs/1qys_TOP7_design_rib.png" alt="XXXXX" width="450">
</figure>

> Fonte: Jane Shelby Richardson, Duke University, 2014

Hoje o David Baker é dono de um dos maiores legados da biologia estrutural computacional, e foi laureado com Nobel de Química em 2023, junto com outros dois cientistas (DeepMind, AlphaFold), por suas contribuições revolucionárias para a predição e design de estruturas de proteínas.

## Sobre o Rosetta

Até agora no curso, utilizamos métodos de modelagem baseados em homologia e threading. Mas e o *ab initio*? Existem pacotes que utilizam essa abordagem para prever estruturas de proteínas sem depender de modelos conhecidos. O  Rosetta é a referência nessa área, e por anos, foi o padrão ouro para predição de estruturas de proteínas quando não havia modelos experimentais disponíveis. 

| Recurso | URL | Descrição |
|---------|-----|-----------|
| **Rosetta** | <a href="https://www.rosettacommons.org/software/license-and-download" target="_blank">https://www.rosettacommons.org/software/license-and-download</a> | pacote de engenharia de proteínas e predição de estruturas |
| **Robetta** | <a href="http://robetta.bakerlab.org/" target="_blank">http://robetta.bakerlab.org/</a> | Servidor web para predição de estruturas com Rosetta |
| **PyRosetta** | <a href="https://www.pyrosetta.org/" target="_blank">https://www.pyrosetta.org/</a> | Interface Python para Rosetta |

<br> 

<figure class="figure-center">
  <img src="imgs/folding_movie-ezgif.com-speed.gif" alt="XXXXX" width="500">
</figure>

> Animação do processo de dobramento guiado representação de grafos. Modelo meramente ilustrativo. Fonte: Veit Elser, Professor of Physics at Cornell University

> Disclaimer (Pessoal): Utilizei o *ab initio* do Rosetta de 2015 a 2019 durante meus projetos de pesquisa que envolviam engenharia de proteínas e predição estrutural. É uma ferramenta poderosa, mas o tempo de computação e a complexidade de configuração podem ser desafiadores para iniciantes. Por isso, optei por não incluir uma atividade prática com Rosetta neste curso introdutório. No entanto, encorajo os interessados a explorar essa ferramenta, para quem se interessar.

O Rosetta funciona através de terminal, via CLI (Command Line Interface) e requer instalação local. Portanto, não é tão acessível quanto os servidores web que utilizamos até agora. E se utilize de dois tipos de abordagens principais: Linha de comando, scripts em XML (linki para mosrar exemplo) e PyRosetta (interface Python).

Para os interessados, deixei disponível o tutorial comentando do Rosetta *ab initio* que utilizei: https://docs.rosettacommons.org/demos/latest/tutorials/denovo_structure_prediction/Denovo_structure_prediction

Construir um Rosetta Script (XML) é uma tarefa que exige conhecimento prévio sobre a sintaxe e os módulos disponíveis na suíte Rosetta. Ele é o alicerce para definir como sua predição será conduzida, seja para modelagem de estruturas, docking molecular ou design de proteínas. Segue o protocolo de boas práticas para criar um script XML eficaz: https://docs.rosettacommons.org/docs/latest/scripting_documentation/RosettaScripts/RosettaScripts

Aqui temos um exemplo como é um script XML para predição *ab initio* com Rosetta, que eu usei há alguns anos atrás:

<br>

```xml
<ROSETTASCRIPTS>
    <!-- FUNÇÕES DE PONTUAÇÃO (SCOREFXNS) -->
    <!-- Define as funções de energia utilizadas durante a predição -->
    <SCOREFXNS>
        <!-- Score0-5: funções progressivamente mais detalhadas usadas no ab initio -->
        <ScoreFunction name="score0" weights="score0.wts"/>
        <ScoreFunction name="score1" weights="score1.wts"/>
        <ScoreFunction name="score2" weights="score2.wts"/>
        <ScoreFunction name="score3" weights="score3.wts"/>
        <ScoreFunction name="score5" weights="score5.wts"/>
        <!-- Função de energia completa para refinamento final -->
        <ScoreFunction name="fullatom" weights="ref2015.wts"/>
    </SCOREFXNS>

    <!-- SELETORES DE RESÍDUOS (RESIDUE_SELECTORS) -->
    <!-- Define quais resíduos serão manipulados -->
    <RESIDUE_SELECTORS>
        <!-- Seleciona toda a cadeia (1-100) para uma proteína de 100 aminoácidos -->
        <Index name="full_protein" resnums="1-100"/>
    </RESIDUE_SELECTORS>

    <!-- FÁBRICAS DE MAPAS DE MOVIMENTO (MOVE_MAP_FACTORIES) -->
    <!-- Controla quais graus de liberdade podem se mover durante a otimização -->
    <MOVE_MAP_FACTORIES>
        <!-- Permite movimento de backbone (bb) e ângulos laterais (chi) de todos os resíduos -->
        <MoveMapFactory name="movemap_full" bb="1" chi="1">
            <Backbone residue_selector="full_protein"/>
            <Chi residue_selector="full_protein"/>
        </MoveMapFactory>
    </MOVE_MAP_FACTORIES>

    <!-- MÉTRICAS SIMPLES (SIMPLE_METRICS) -->
    <!-- Ferramentas para análise e validação do modelo gerado -->
    <SIMPLE_METRICS>
        <!-- Tempo de execução do protocolo -->
        <TimingProfileMetric name="timing"/>
        <!-- RMSD do backbone em relação à estrutura nativa (se disponível) -->
        <RMSDMetric name="rmsd_backbone" rmsd_type="rmsd_protein_bb_heavy" 
                    residue_selector="full_protein" use_native="1"/>
        <!-- Sequência dos resíduos selecionados -->
        <SequenceMetric name="sequence" residue_selector="full_protein"/>
        <!-- Estrutura secundária predita (H=hélice, E=folha, L=loop) -->
        <SecondaryStructureMetric name="secondary_structure" residue_selector="full_protein"/>
        <!-- Energia total da estrutura -->
        <TotalEnergyMetric name="total_energy" scorefxn="fullatom"/>
    </SIMPLE_METRICS>

    <!-- MOVERS -->
    <!-- Operações que modificam a estrutura da proteína -->
    <MOVERS>
        <!-- PROTOCOLO AB INITIO CLÁSSICO -->
        <!-- Gera estrutura 3D a partir de fragmentos estruturais e otimização progressiva -->
        <!-- Requer arquivos de fragmentos (3-mer e 9-mer) gerados previamente -->
        <ClassicAbinitio name="abinitio" 
                        score_stage1="score0"
                        score_stage2="score1"
                        score_stage3a="score2"
                        score_stage3b="score5"
                        score_stage4="score3"
                        frag_small="/caminho/para/frags.200.3mers"
                        frag_large="/caminho/para/frags.200.9mers"
                        cycles="1000"
                        use_filters="true"
                        number_3mer_frags="200"
                        number_9mer_frags="25"/>

        <!-- REFINAMENTO EM FULLATOM -->
        <!-- Converte o modelo centroide para fullatom e refina a estrutura -->
        <FastRelax name="refine" 
                   scorefxn="fullatom" 
                   movemap_factory="movemap_full"
                   repeats="5"/>

        <!-- MINIMIZAÇÃO FINAL -->
        <!-- Otimização local para remover choques estéricos residuais -->
        <MinMover name="minimize" 
                  scorefxn="fullatom" 
                  movemap_factory="movemap_full" 
                  tolerance="0.01" 
                  max_iter="200"/>

        <!-- COLETA DE MÉTRICAS -->
        <!-- Executa as métricas definidas anteriormente -->
        <RunSimpleMetrics name="run_metrics_initial" 
                          metrics="sequence,secondary_structure" 
                          prefix="initial_"/>
        <RunSimpleMetrics name="run_metrics_final" 
                          metrics="rmsd_backbone,total_energy,timing,secondary_structure" 
                          prefix="final_"/>
    </MOVERS>

    <!-- PROTOCOLO DE EXECUÇÃO (PROTOCOLS) -->
    <!-- Ordem sequencial das operações -->
    <PROTOCOLS>
        <!-- 1. Coleta métricas iniciais -->
        <Add mover_name="run_metrics_initial"/>
        
        <!-- 2. Executa ab initio para gerar modelo inicial -->
        <Add mover_name="abinitio"/>
        
        <!-- 3. Refina o modelo em fullatom -->
        <Add mover_name="refine"/>
        
        <!-- 4. Minimização final -->
        <Add mover_name="minimize"/>
        
        <!-- 5. Coleta métricas finais para validação -->
        <Add mover_name="run_metrics_final"/>
    </PROTOCOLS>
</ROSETTASCRIPTS>
```

<br>

Vamos discutir as vantagens e desvantagens do *ab initio* em comparação com os métodos que utilizamos até agora?

<figure class="figure-center">
  <img src="imgs/folding_funnels.png" alt="XXXXX" width="600">
</figure>

> Rosetta Commons. Fonte: https://www.rosettacommons.org/docs/latest/application_documentation/demos/denovo_structure_prediction


## Quantidade de Simulações Necessárias

É possível realizar execuções de enovelamento em domínios separados de até aproximadamente 200 aminoácidos de comprimento, mas é amplamente relatado na literatura que o protocolo ab initio do Rosetta é mais eficaz para proteínas menores, tipicamente abaixo de 100-150 resíduos.

Para proteínas de tamanho moderado **(50-100 resíduos)**, recomenda-se gerar entre **5.000 e 50.000** decoys para garantir amostragem suficiente do espaço conformacional. **A presença de um folding funnel característico, evidenciado pela convergência de estruturas de baixo RMSD e baixa energia (REU - Rosetta Energy Units)**, indica que o protocolo conseguiu identificar a região do estado nativo da proteína.

No gráfico à esquerda (**com formação de funil**), observa-se a **formação clara de um funil energético**: **as estruturas convergem para uma região de baixo RMSD (< 2 Å) e baixo score (~-195 REU)**, sugerindo que o algoritmo identificou corretamente o estado enovelado. **Este padrão é o resultado desejado e indica alta confiabilidade dos modelos de menor energia.**

Por outro lado, **o gráfico à direita (sem funil formado)** demonstra um **cenário problemático** onde **não há convergência aparente**. **As estruturas estão dispersas em uma ampla faixa de RMSD (0-6 Å) sem correlação clara com a energia**, indicando que **o protocolo falhou em identificar o estado nativo ou que a proteína não possui um único estado enovelado bem definido**.

## Critérios de Seleção do Modelo Final

Após a geração dos decoys, os modelos candidatos são selecionados com base em:

1. **Energia (REU)**: modelos no percentil inferior de energia (tipicamente top 1-5%)
2. **Clustering estrutural**: agrupamento por similaridade estrutural (RMSD) para identificar conformações consenso
3. **Presença do funil**: modelos na região de convergência energia-RMSD
4. **Validação estrutural**: análise de Ramachandran, Verify3D, ProSA-web

O modelo final geralmente corresponde ao centroide do maior cluster de baixa energia localizado no fundo do folding funnel.

---

## Take Home Message

### Perguntas:

- Acham que tem algo em comum entre nas metodologias de threading e *ab initio*?
- Quais são as principais vantagens e limitações do método *ab initio* em comparação com homologia e threading?
- Em que situações o *ab initio* seria a abordagem preferida para predição estrutural?
- Como a quantidade de resíduos influencia a eficácia do *ab initio*? Spoiler: Proteínas pequenas são melhores candidatas, devido a uma melhor sobreposição dos da bibliotecas de fragmentos e para os dezenas de calculos de angulos torsionais necessários.

> **Respostas:**
>
> **O que threading e *ab initio* têm em comum?**
>
> Apesar de serem abordagens distintas, threading e *ab initio* compartilham uma característica fundamental: **nenhum dos dois depende de um único molde com alta identidade de sequência**, ao contrário da modelagem por homologia clássica. Ambos buscam explorar o espaço conformacional da proteína de forma mais abrangente.
>
> O threading alinha fragmentos da sequência a perfis estruturais de proteínas do PDB mesmo sem similaridade de sequência evidente, usando funções de energia para avaliar a compatibilidade de cada alinhamento. O *ab initio* faz algo conceitualmente similar ao nível de fragmentos curtos (3-mers e 9-mers): ele extrai fragmentos estruturais de proteínas conhecidas e os monta iterativamente, guiado por uma função de pontuação energética. Em ambos os casos, o conhecimento estrutural acumulado no PDB é explorado indiretamente, seja como perfis de threading ou como biblioteca de fragmentos.
>
> A diferença central está em como esse conhecimento é utilizado: o threading busca um molde global completo; o *ab initio* utiliza apenas fragmentos locais e reconstrói a estrutura global a partir deles.
>
> **Vantagens e limitações do *ab initio* em comparação com homologia e threading:**
>
> | Critério | Homologia | Threading | *Ab initio* |
> |:---------|:---------:|:---------:|:-----------:|
> | Dependência de molde | Alta | Baixa | Nenhuma |
> | Cobertura de proteínas sem homólogos | Baixa | Moderada | Alta |
> | Qualidade para proteínas com molde | Muito alta | Alta | Moderada |
> | Custo computacional | Baixo | Moderado | Muito alto |
> | Limitação de tamanho | Sem molde = sem modelo | Moderada | Forte (< 150 aa) |
> | Amostragem conformacional | Restrita ao molde | Semi-restrita | Ampla |
>
> A maior vantagem do *ab initio* é a independência total de estruturas homólogas conhecidas, o que o torna a única opção viável para proteínas sem nenhum parente estrutural no PDB. Sua maior limitação é o custo computacional exponencial com o aumento da cadeia, além da dificuldade de gerar um *folding funnel* claro para proteínas maiores.
>
> **Em que situações o *ab initio* seria a abordagem preferida?**
>
> O *ab initio* é a abordagem preferida quando:
>
> 1. A proteína-alvo não possui nenhum homólogo estrutural conhecido no PDB (cobertura de threading abaixo de 10-20%).
> 2. O objetivo é explorar conformações alternativas que não estejam presentes em moldes conhecidos, como estruturas de proteínas intrinsecamente desordenadas que adquirem estrutura em condições específicas.
> 3. A proteína é pequena (idealmente abaixo de 100-150 resíduos), tornando a amostragem conformacional computacionalmente viável.
> 4. O pesquisador quer projetar uma proteína com nova topologia, como foi feito com a Top-7 descrita nesta seção.
>
> **Como o tamanho da proteína influencia a eficácia do *ab initio*?**
>
> O número de graus de liberdade conformacionais cresce rapidamente com o tamanho da proteína. Cada resíduo possui ao menos dois ângulos de torção da cadeia principal (phi e psi), e o número de combinações possíveis é exponencial. Para uma proteína de 50 resíduos, é computacionalmente viável gerar e avaliar dezenas de milhares de conformações (decoys). Para uma proteína de 393 resíduos como a p53 *full-length*, o espaço conformacional é astronomicamente maior.
>
> Além disso, a biblioteca de fragmentos do Rosetta é construída para fragmentos de 3 e 9 resíduos extraídos do PDB. Para proteínas pequenas, esses fragmentos cobrem proporcionalmente mais da estrutura total, levando a uma montagem mais coerente. Para proteínas grandes, os fragmentos cobrem menos contexto local e os erros se acumulam ao longo da montagem. Por isso, proteínas acima de 150-200 resíduos raramente produzem *folding funnels* claros com *ab initio* clássico, e os resultados tendem a ter RMSD elevado em relação à estrutura nativa.

---

# Predição por Deep Learning (AF2, AF3 e ESM3)

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

## Métricas de Confiança

- **pLDDT** (predicted Local Distance Difference Test): 0-100, >90 = alta confiança
- **PAE** (Predicted Aligned Error): Confiança na posição relativa entre resíduos

## Perguntas:

- Como os valores de pLDDT distribuídos ao longo da cadeia ajudam a distinguir regiões estruturadas de segmentos desordenados na p53 predita?
- Ao comparar os mapas de PAE dos diferentes servidores, quais domínios apresentam maior incerteza relativa e como isso impacta a confiança global do modelo?
- Quais diferenças você espera observar entre as predições de AF2/ColabFold, AF3 e ESM3 em termos de conformação global e métricas de confiança?
- Se você tivesse de priorizar um único modelo para a próxima etapa de análise comparativa, quais critérios baseados nas saídas desses métodos sustentariam sua escolha?

> **Respostas:**
>
> **Como o pLDDT ajuda a distinguir regiões estruturadas de desordenadas?**
>
> O pLDDT (*predicted Local Distance Difference Test*) é atribuído individualmente a cada resíduo e reflete a confiança do modelo no dobramento local daquele aminoácido. Valores acima de 90 indicam alta confiança e correspondem a regiões bem estruturadas; valores entre 70 e 90 indicam confiança moderada; valores abaixo de 50 indicam que o modelo não conseguiu prever uma conformação local consistente, o que geralmente corresponde a regiões intrinsecamente desordenadas (*IDRs, intrinsically disordered regions*).
>
> Para a p53, o perfil de pLDDT ao longo da cadeia é bastante informativo. O DBD (resíduos 94-292) deve apresentar os valores mais altos de pLDDT (tipicamente acima de 85-90), pois é uma região compacta e bem estruturada com muitos moldes no PDB. As regiões TAD1 (1-40), TAD2 (41-67) e PRD (68-93) devem apresentar pLDDT baixo (abaixo de 50-60), pois são regiões naturalmente desordenadas que se estruturam apenas ao interagir com parceiros como MDM2, CBP/p300 e o complexo geral de transcrição. O OD (326-356) deve apresentar valores intermediários a altos, e o CTD (357-393) deve apresentar valores baixos por ser desordenado.
>
> Essa distribuição é biologicamente coerente: as regiões de pLDDT baixo na p53 não representam falhas do AlphaFold, mas sim regiões que genuinamente não possuem estrutura tridimensional definida em solução.
>
> **Quais domínios apresentam maior incerteza no mapa de PAE?**
>
> O PAE (*Predicted Aligned Error*) mede a incerteza na posição relativa entre pares de resíduos, sendo expresso em Ångströms. Um mapa de PAE ideal mostraria valores baixos (azul escuro) ao longo de toda a diagonal e em blocos correspondentes a cada domínio, indicando que as posições relativas dentro de cada domínio são bem preditas. Valores altos fora da diagonal (cores quentes) indicam incerteza na orientação relativa entre regiões distantes.
>
> Para a p53, espera-se que:
> - O bloco do DBD (resíduos ~94-292) apresente PAE baixo internamente, indicando alta confiança na estrutura do domínio.
> - As regiões TAD1, TAD2, PRD e CTD apresentem PAE alto tanto internamente quanto em relação ao DBD, indicando que a orientação dessas regiões em relação ao núcleo estrutural é incerta.
> - O OD apresente PAE baixo internamente mas PAE alto em relação ao DBD, pois são domínios independentes ligados por um *linker* flexível.
>
> Isso impacta a confiança global do modelo: embora o DBD seja predito com alta confiança, a orientação dos domínios terminais em relação a ele é incerta, e os modelos de diferentes servidores provavelmente mostrarão conformações variadas para essas regiões.
>
> **Diferenças esperadas entre AF2/ColabFold, AF3 e ESM3:**
>
> O **AlphaFold2 (ColabFold)** e o **AlphaFold3** utilizam alinhamentos de sequências múltiplas (MSA) como entrada principal, explorando a co-evolução entre resíduos para inferir contatos. O AF3 adiciona mecanismos de atenção mais sofisticados e suporte nativo a complexos proteína-DNA/RNA/ligantes. Para a p53 isolada, ambos devem gerar predições semelhantes no DBD, com pLDDT alto e PAE baixo nessa região. As diferenças devem aparecer principalmente nas regiões desordenadas: o AF3 tende a representar regiões desordenadas de forma mais diversa entre os modelos gerados, refletindo melhor o ensemble conformacional dessas regiões.
>
> O **ESM3** parte de uma abordagem diferente: ele é um modelo de linguagem de proteínas treinado em sequências e estruturas sem usar MSA explícito, capturando padrões evolutivos diretamente na representação aprendida. Para proteínas bem estudadas como a p53, o ESM3 geralmente produz resultados comparáveis aos modelos AlphaFold no DBD. Nas regiões desordenadas, o ESM3 pode divergir mais, pois não utiliza a informação de co-evolução de forma tão explícita.
>
> **Qual critério usar para priorizar um modelo?**
>
> Para a próxima etapa de análise comparativa (alinhamento estrutural e cálculo de RMSD contra o 1TUP experimental), o modelo prioritário deve ser selecionado com base em:
>
> 1. **pLDDT médio do DBD**: priorizar o modelo com pLDDT mais alto na região 94-292, pois é ela que será comparada com o 1TUP.
> 2. **PAE baixo dentro do DBD**: confirmar que a estrutura interna do domínio é confiante.
> 3. **Cobertura de sequência**: garantir que o modelo inclui toda a região a ser comparada.
> 4. **Consistência com o 1TUP visualmente**: verificar no PyMOL se a topologia geral (folhas beta, alças) é compatível antes de calcular RMSD.
>
> Com base nesses critérios, qualquer um dos modelos AlphaFold (AF2 ou AF3) tende a ser o melhor candidato para comparação com o 1TUP, dado que utilizam MSA e possuem excelente desempenho em domínios bem conservados como o DBD da p53.

---

# Módulo 4: Análise Comparativa, Validação e Visualização

* Agora que temos os modelos gerados por homologia, threading e deep learning. Vamos baixar um modelos experimental, obtido por cristalografia de x-ray, da p53 para comparar os modelos teóricos. Lembrando que a estrutura experimental sempre será o nosso padrão-ouro de comparação.

**Baixe aqui o arquivo PDB da estrutura cristalina da p53 (PDB ID: 1TUP) para utilizar como referência na comparação dos modelos preditos:** <a href="https://drive.google.com/file/d/1p0liOriRtvaYrY2CvTDCWpMGHIO1zfoq/view?usp=sharing" target="_blank">1TUP_cleaned.pdb</a>.

> Sugiro fortemente que utilize este arquivo para evitar problemas de formatação ou erros por conta de heteroátomos.

> Opicional: Baixar a estrutura experimental da p53 (PDB ID: 1TUP) do RCSB PDB para servir como referência na comparação dos modelos preditos. No entanto, além da proteína, o arquivo possuí íons, águas e ligantes. Link: <a href="https://www.rcsb.org/structure/1tup" target="_blank">https://www.rcsb.org/structure/1tup</a>

**Objetivos:**
- Comparar todos os modelos gerados.
- Realizar análise estrutural comparativa no PyMOL.
- Quantificar diferenças estruturais via RMSD.

## Servidores de Validação de Dobramento e Termodinâmica

| Servidor | URL | Métrica Avaliada |
|----------|-----|------------------|
| **MolProbity (SAVES)** | <a href="https://saves.mbi.ucla.edu/" target="_blank">https://saves.mbi.ucla.edu/</a> | Gráfico de Ramachandran, geometria |
| **QMEAN** | <a href="https://swissmodel.expasy.org/qmean/" target="_blank">https://swissmodel.expasy.org/qmean/</a> | Qualidade global |
| **ProSA-web** | <a href="https://prosa.services.came.sbg.ac.at/prosa.php" target="_blank">https://prosa.services.came.sbg.ac.at/prosa.php</a> | Z-score (energia do enovelamento) |

## Análise Estrutural no PyMOL

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

## Perguntas:

- Quais modelos apresentam RMSD mais baixo em relação à estrutura experimental e o que isso revela sobre a qualidade geral de cada predição?
- Ao inspecionar as sobreposições no PyMOL, quais regiões da p53 mantêm conformação consistente entre todos os modelos e quais divergem com mais intensidade?
- Como as métricas de validação (MolProbity, ProSA, QMEAN, ProSA-web) complementam os resultados de RMSD para justificar a seleção de um modelo confiável?
- De que modo as figuras geradas podem comunicar melhor as diferenças funcionais potenciais entre os modelos analisados?

> **Respostas:**
>
> **Quais modelos apresentam RMSD mais baixo e o que isso revela?**
>
> O RMSD (*Root Mean Square Deviation*) quantifica a distância média entre átomos equivalentes de duas estruturas sobrepostas, expresso em Ångströms (Å). Para a comparação com o 1TUP, que cobre apenas o DBD (resíduos 94-292), o RMSD deve ser calculado sobre os Cα dessa região, excluindo os terminais desordenados que não existem no cristal.
>
> A hierarquia de RMSD esperada para o DBD da p53 (do menor para o maior) é:
>
> 1. **SWISS-MODEL**: RMSD entre 0,8 e 1,5 Å, pois usa diretamente estruturas como o 1TUP como molde.
> 2. **AlphaFold2/ColabFold** e **AlphaFold3**: RMSD entre 1,0 e 2,0 Å, refletindo a excelência no DBD.
> 3. **ESM3**: RMSD entre 1,5 e 3,0 Å, ligeiramente maior por não usar MSA explícito.
> 4. **I-TASSER**: RMSD entre 2,0 e 4,0 Å, pois o threading acumula mais imprecisões locais.
>
> Um RMSD abaixo de 2 Å para o Cα do DBD é considerado excelente. Entre 2 e 4 Å indica dobramento correto com desvios em loops. Acima de 4 Å sugere erros de topologia mais sérios.
>
> **Quais regiões são consistentes e quais divergem entre os modelos?**
>
> Ao sobrepor todos os modelos no PyMOL com o comando `align` ou `super`, o comportamento esperado é:
>
> **Regiões de alta consistência (baixo RMSD entre modelos):**
>
> - As folhas beta centrais do DBD, que formam o núcleo hidrofóbico do domínio sanduiche beta.
> - As hélices H1 e H2 do DBD.
> - A região do sítio de coordenação do zinco (C176, H179, C238, C242).
>
> **Regiões de alta divergência (alto RMSD entre modelos):**
>
> - As alças L1, L2 e L3, que fazem contato direto com o DNA e são mais flexíveis.
> - Os terminais N e C da cadeia completa (TAD1, TAD2, PRD, CTD), que são intrinsecamente desordenados.
> - O linker entre o DBD e o OD, que é flexível e não possui conformação definida.
>
> **Como MolProbity, QMEAN e ProSA-web complementam o RMSD?**
>
> O RMSD mede apenas a semelhança topológica global entre dois modelos, mas não avalia se a geometria interna do modelo é quimicamente razoável. Um modelo pode ter RMSD baixo em relação ao 1TUP e ainda conter erros de geometria local. Por isso, as métricas de validação são complementares e essenciais:
>
> O **MolProbity** (via SAVES) avalia a geometria da cadeia principal pelo gráfico de Ramachandran. Modelos de alta qualidade devem ter mais de 95% dos resíduos nas regiões favoráveis. Também avalia clashes estéricos entre átomos. Um modelo com RMSD baixo mas muitos resíduos fora das regiões favoráveis pode ter erros locais que comprometem interpretações funcionais.
>
> O **QMEAN** fornece um escore global de qualidade (0 a 1) por comparação com estruturas do PDB de tamanho similar, além de um perfil de qualidade por resíduo para identificar regiões com geometria problemática.
>
> O **ProSA-web** calcula o Z-score, que mede o quanto a energia do modelo se desvia da energia média de estruturas experimentais no PDB. Um Z-score dentro do intervalo esperado para proteínas de tamanho similar (-5 a -10 para a p53) indica dobramento energeticamente plausível.
>
> A combinação RMSD + Ramachandran + QMEAN + Z-score fornece uma avaliação multidimensional: o RMSD avalia a semelhança topológica global, o Ramachandran avalia a geometria local, o QMEAN avalia o consenso com estruturas experimentais, e o Z-score avalia a plausibilidade energética. Um modelo confiável deve ter bons resultados em todas essas métricas simultaneamente.
>
> **Como as figuras comunicam diferenças funcionais entre os modelos?**
>
> Figuras estruturais bem elaboradas transmitem informação que tabelas de RMSD não conseguem comunicar visualmente. Algumas estratégias eficazes no PyMOL:
>
> - **Colorir por RMSD por resíduo**: usar espectro de cores para mapear a variação ao longo da cadeia. Regiões em azul (baixo desvio) identificam o núcleo conservado; regiões em vermelho (alto desvio) destacam loops variáveis, que frequentemente correspondem a regiões de contato com o DNA.
> - **Sobrepor todos os modelos em representação cartoon**: a dispersão visual das conformações dos loops L1, L2 e L3 mostra imediatamente quão incertas são as regiões de contato com DNA.
> - **Destacar resíduos de contato com DNA**: mostrar as cadeias laterais de R248, R273, K120 e S241 em *sticks* em todos os modelos sobrepostos revela se os modelos reproduzem a geometria de ligação observada no 1TUP.
> - **Comparar superfície eletrostática**: gerar mapas de potencial eletrostático (via plugin APBS no PyMOL) para cada modelo e comparar a distribuição de cargas na interface de ligação ao DNA. Diferenças na superfície eletrostática podem ter implicações diretas na afinidade e especificidade de ligação.

---

# Referências (Atividades Práticas)

## Bases de Dados
- <a href="https://www.uniprot.org/" target="_blank" rel="noopener noreferrer">UniProt</a>
- <a href="https://www.rcsb.org/" target="_blank" rel="noopener noreferrer">RCSB PDB</a>

## Ferramentas de Predição
- <a href="https://web.expasy.org/protparam/" target="_blank" rel="noopener noreferrer">ExPASy ProtParam</a>
- <a href="https://services.healthtech.dtu.dk/service.php?SignalP-6.0" target="_blank" rel="noopener noreferrer">SignalP 6.0</a>
- <a href="https://www.ebi.ac.uk/interpro/search/sequence/" target="_blank" rel="noopener noreferrer">InterProScan</a>
- <a href="https://prosite.expasy.org/" target="_blank" rel="noopener noreferrer">PROSITE</a>

## Modelagem Estrutural
- <a href="https://swissmodel.expasy.org/" target="_blank" rel="noopener noreferrer">SWISS-MODEL</a>
- <a href="https://zhanggroup.org/I-TASSER/" target="_blank" rel="noopener noreferrer">I-TASSER</a>
- <a href="https://colabfold.com/" target="_blank" rel="noopener noreferrer">AlphaFold 2 (ColabFold)</a>
- <a href="https://alphafoldserver.com/" target="_blank" rel="noopener noreferrer">AlphaFold 3 Server</a>
- <a href="https://esm.metademolab.com/esm3" target="_blank" rel="noopener noreferrer">ESM3</a>

## Validação
- <a href="http://molprobity.biochem.duke.edu/" target="_blank" rel="noopener noreferrer">MolProbity</a> / <a href="https://saves.mbi.ucla.edu/" target="_blank" rel="noopener noreferrer">SAVES</a>
- <a href="https://swissmodel.expasy.org/qmean/" target="_blank" rel="noopener noreferrer">QMEAN</a>
- <a href="https://prosa.services.came.sbg.ac.at/prosa.php" target="_blank" rel="noopener noreferrer">ProSA-web</a>

## Visualização
- <a href="https://pymol.org/2/" target="_blank" rel="noopener noreferrer">PyMOL (Schrödinger)</a>

---

# Licença

Uso estritamente educacional e acadêmico. Proibida a utilização comercial sem autorização prévia dos autores.
Para qualquer outro tipo de uso, entre em contato com os autores pelos e-mails fornecidos acima.

---

# Recursos Úteis

<a href="https://github.com/madsondeluna/bits_bytes_biomolecules" target="_blank">Repositório do Curso</a>
<a href="https://madsondeluna.github.io/bits_bytes_biomolecules/" target="_blank">Página Web do Curso</a>


---

<br>

> Nenhuma dúvida é boba... Qualquer dúvida ou sugestão, sinta-se à vontade para entrar em contato conosco pelos e-mails fornecidos acima. Bom desempenho e aproveitem os exercícios!

<br>

---

<!--
# Extra: Ferramenta Educacional CLI - Tradução de Proteínas

Esta seção apresenta um **script educacional interativo** que demonstra, passo a passo, o processo de **tradução de proteínas** via linha de comando (CLI). Esta ferramenta foi desenvolvida para complementar o aprendizado sobre o **Dogma Central da Biologia Molecular**, oferecendo uma visualização didática e interativa de como o mRNA é convertido em proteínas.

### Sobre o Script

<figure class="figure-center">
  <img src="imgs/prot-translation.png" alt="Screenshot do script de tradução de proteínas em execução" width="1000">
</figure>

> Exemplo de execução do script educacional de tradução de proteínas mostrando a fase de iniciação, com animações ASCII representando o ribossomo, mRNA e os fatores de iniciação (eIF4E, eIF4G, PABP). O script utiliza arte ASCII e efeitos de digitação para demonstrar interativamente cada etapa do processo de tradução proteica.

O script utiliza **animações em terminal** e **arte ASCII** para ilustrar:
- O **Dogma Central** (DNA → RNA → Proteína)
- A **maquinaria de tradução** (ribossomos, tRNA, mRNA)
- As **três fases da tradução**: Iniciação, Elongação e Terminação
- O **dobramento proteico** e modificações pós-traducionais
- **Relevância clínica** e aplicações terapêuticas

### Script Disponível

**Ferramenta de Tradução de Proteínas** 

- [Baixar domrnaparaproteina.py](https://raw.githubusercontent.com/madsondeluna/bits_bytes_biomolecules/main/protein-translation_CLI/domrnaparaproteina.py)
- [Ver código no repositório](protein-translation_CLI/domrnaparaproteina.py)

#### Como Baixar

Você pode baixar o script de **três formas**:

**Opção 1: Download Direto**
- Clique no link "Baixar domrnaparaproteina.py" acima
- O arquivo será baixado automaticamente
- Salve em uma pasta de fácil acesso

**Opção 2: Clonar o Repositório Completo**
```bash
git clone https://github.com/madsondeluna/bits_bytes_biomolecules.git
cd bits_bytes_biomolecules/protein-translation_CLI
```

**Opção 3: Download via Terminal (Linux/macOS)**

```bash
curl -O https://raw.githubusercontent.com/madsondeluna/bits_bytes_biomolecules/main/protein-translation_CLI/domrnaparaproteina.py
chmod +x domrnaparaproteina.py
```

### Como Executar

#### Pré-requisitos
- **Python 3.6+** instalado no sistema
- Terminal compatível (Linux, macOS, Windows Terminal, ou PowerShell)

#### Instruções de Execução

**1. Via Terminal (qualquer sistema operacional)**

```bash
cd protein-translation_CLI
python3 domrnaparaproteina.py
```

**2. Execução Direta (Linux/macOS)**

O script possui permissão de execução. Você pode executá-lo diretamente:

```bash
./protein-translation_CLI/domrnaparaproteina.py
```

**3. No Windows (PowerShell ou CMD)**

```powershell
cd protein-translation_CLI
python domrnaparaproteina.py
```

### Conteúdo Abordado

Os scripts cobrem os seguintes tópicos de forma interativa:

1. **Introdução ao Dogma Central**
   - Fluxo de informação: DNA → RNA → Proteína

2. **Maquinaria Molecular da Tradução**
   - Ribossomos (subunidades 40S e 60S)
   - tRNA e aminoácidos
   - Fatores de iniciação e elongação

3. **Fase de Iniciação**
   - Reconhecimento do cap 5' por eIF4E
   - Recrutamento da subunidade 40S
   - Identificação do códon de início (AUG)

4. **Fase de Elongação**
   - Entrada do aminoacil-tRNA no sítio A
   - Formação da ligação peptídica
   - Translocação do ribossomo

5. **Fase de Terminação**
   - Reconhecimento de códons de parada (UAA, UAG, UGA)
   - Fatores de liberação (eRF1/eRF3)
   - Desmontagem do ribossomo

6. **Dobramento Proteico**
   - Estrutura 3D funcional
   - Chaperonas moleculares
   - Modificações pós-traducionais

7. **Relevância Clínica**
   - Doenças neurodegenerativas (Alzheimer, Parkinson)
   - Câncer e desregulação da tradução
   - Estratégias terapêuticas (inibidores de mTOR, eIF4E)

8. **Técnicas de Pesquisa**
   - Ribosome profiling (Ribo-seq)
- Proteômica por espectrometria de massa
- Abordagens de célula única

### Características Técnicas

- **Animações suaves** com efeito de digitação
- **Arte ASCII** para representar moléculas e processos
- **Interatividade**: pressione ENTER para avançar entre as etapas
- **Código limpo e bem documentado** para uso educacional
- **Interrupção segura**: use `Ctrl+C` para sair a qualquer momento

### Uso Educacional Recomendado

- **Aulas introdutórias** sobre biologia molecular
- **Revisão visual** de conceitos de tradução proteica
- **Complemento** aos exercícios práticos de modelagem
- **Demonstrações interativas** em sala de aula ou workshops

### Autoria

**Desenvolvido por:** Madson Aragão @ UFMG

-->

# Reporte de Erros

Se você identificou algum **erro conceitual**, **ambiguidade científica** ou **imprecisão** neste material, ficarei **muito feliz** em corrigir e saber que pessoas atentas estão lendo e contribuindo para a qualidade deste conteúdo.

## Como reportar um problema:
1. Acesse o repositório oficial do curso: <a href="https://github.com/madsondeluna/bits_bytes_biomolecules" target="_blank">https://github.com/madsondeluna/bits_bytes_biomolecules</a>

2. Clique na aba **"Issues"** (no topo da página do repositório)

3. Clique no botão verde **"New issue"** (Nova issue)

4. Preencha o formulário com as seguintes informações:
   - **Título**: Descreva brevemente o problema (ex: "Erro conceitual na seção de Elongação")
   - **Descrição**: Explique detalhadamente:
     - Onde está o erro (arquivo e seção)
     - Qual é o problema identificado
     - Sugestão de correção (se possível)
     - Referências bibliográficas que sustentam a correção (opcional, mas muito apreciado)

5. Clique em **"Submit new issue"** para enviar

Suas contribuições são extremamente valiosas para manter este material atualizado e cientificamente preciso. Obrigado por dedicar seu tempo para melhorar este recurso educacional!

<br>

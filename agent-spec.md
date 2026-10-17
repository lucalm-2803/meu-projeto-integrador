# agent-spec.md — modelo do meu agente

<!--
Este arquivo é para preencher, não para ler e devolver. As perguntas de cada
seção estão em comentário como este: elas não aparecem na pré-visualização,
aparecem no editor. Responda ABAIXO de cada seção, apagando nada delas.

As seções que ainda não foram vistas em aula ficam de pé, com a linha
"quando se preenche" dizendo o encontro em que isso acontece. O documento
cresce a cada laboratório — o de hoje é o primeiro.

Preencha com exemplos concretos do SEU domínio. Uma linha que funcionaria
para qualquer empresa é uma linha genérica — o exemplo do seu segmento
(agente-spec-exemplo.pdf, no mesmo pacote) mostra o contraste.
-->

**Domínio:** [título curto do domínio, do dominio.md da D1]
**Autor(a):** [seu nome] · **Última revisão:** [data]

---

## 1. PEAS

<!-- Perguntas que guiam o preenchimento:
  - Performance: o que conta como sucesso, em uma fórmula? Sobre o quê se
    conta, sobre qual conjunto, quanto é sucesso? Qual termo impede a
    trapaça mais óbvia (fechar rápido sem resolver)?
  - Environment: onde o agente opera? O que existe lá — sistemas, pessoas,
    documentos, ruído? Cite elementos concretos.
  - Actuators: o que o agente pode FAZER? Inclua comunicar e escalar:
    informar a decisão é uma ação, e passar adiante também é.
  - Sensors: o que o agente consegue PERCEBER? Só o que ele enxerga existe
    para ele.
  Um PEAS que menciona tecnologia de solução (banco vetorial, nome de modelo)
  está descrevendo a solução — o PEAS descreve o problema.
-->
**Quando se preenche:** no Laboratório 01, hoje. Refinado na Atividade Orientada.

**Performance:**

`Taxa de Retrabalho (%) = (Ordens reabertas em até 30 dias / Total de ordens fechadas) × 100`


**Medida, conjunto e limiar:** Proporção de ordens de serviço reabertas em até 30 dias sobre o total de ordens fechadas, medida nas 200 ordens do último trimestre, com meta de ficar abaixo de 5%.

**Controle antitrapaça:** Contabilizar a reabertura em 30 dias impede a trapaça de fechar ordens rapidamente sem avaliar o risco real de falha da máquina ou sem aplicar os procedimentos de segurança exigidos.

**Environment:**

Planta industrial com máquinas de produção monitoradas por sensores sob ruído e pressão de tempo operacional; sistema de ordens de serviço (preventivas e corretivas); histórico de sensores e falhas (dataset AI4I 2020, 10.000 registros); acervo de normas regulamentares em PDF (NR-10, NR-12 e NR-35 do portal gov.br); técnicos de manutenção (usuários primários que decidem a execução) e supervisores de segurança (usuários secundários que auditam as decisões).

**Actuators:**

Classificar o nível de risco de falha da máquina (baixo, médio ou alto); apontar as normas aplicáveis à intervenção (NR-10, NR-12, NR-35); definir a obrigatoriedade de bloqueio e etiquetagem (LOTO); comunicar ao técnico uma resposta curta e justificada em português (via objeto validado AvaliacaoRisco); e registrar/escalar a recomendação para auditoria do supervisor de segurança.

**Sensors:**

Leituras numéricas atuais dos sensores da máquina (temperatura, rotação, torque e desgaste de ferramenta); dados da ordem de serviço aberta (identificação da máquina e descrição da intervenção em linguagem natural); registros históricos de falhas (AI4I 2020, 14 colunas); e textos normativos das NRs (NR-10, NR-12 e NR-35).

---

## 2. O ambiente em sete dimensões

<!--
Perguntas que guiam o preenchimento (uma por dimensão):
  - Observabilidade: existe algo que muda a decisão e o agente não mede?
  - Número de agentes: existe alguém cujas ações mudam o seu resultado?
    Um humano que reage ao agente conta.
  - Determinismo: a mesma ação no mesmo estado dá sempre o mesmo efeito?
  - Episódico ou sequencial: a decisão de agora afeta as decisões seguintes?
  - Estático ou dinâmico: o ambiente muda enquanto o agente delibera?
  - Discreto ou contínuo: estados e ações são contáveis?
  - Conhecido ou desconhecido: o agente sabe de antemão as regras? (Trata do
    que ele SABE, não do que ele VÊ.)
  Cada classificação vem com uma frase de justificativa — a etiqueta sozinha
  não vale nada.
-->
**Quando se preenche:** no Laboratório 02, no sábado (encontro 2).

[uma linha por dimensão: a classificação e a frase de
justificativa — começando por observabilidade e determinismo]

---

## 3. Tipo de agente pretendido

<!--
Perguntas que guiam o preenchimento:
  - O tipo mais simples que resolve: reativo simples, baseado em modelo,
    baseado em objetivos, baseado em utilidade, ou um deles com aprendizagem?
  - A caracterização do ambiente (seção 2) é que decide — parcialmente
    observável elimina o reativo simples.
  - Justifique com a dimensão do ambiente que obriga a escolha.
-->
**Quando se preenche:** no sábado (encontro 2, manhã).

[o tipo mais simples que resolve, justificado pela dimensão
do ambiente que o obriga]

---

## 4. Medida de desempenho

<!--
Perguntas que guiam o preenchimento:
  - A fórmula do campo Performance, agora em definição operacional: como se
    calcula, passo a passo, sem ambiguidade?
  - Métrica primária e duas secundárias. As secundárias pegam o que a
    primária deixa passar (custo, latência, reabertura).
  - O conjunto de casos: de onde vêm, quantos são, de que período.
  - O limiar de sucesso e o valor de hoje.
-->
**Quando se preenche:** a fórmula começa no Laboratório 01; a definição
operacional completa — primária, secundárias, conjunto e limiar — é item da
Atividade Orientada.

[métrica primária e duas secundárias, cada uma com: como se
calcula, sobre qual conjunto, qual o limiar de sucesso e o
valor de hoje]

---

## 5. Restrições

<!--
Perguntas que guiam o preenchimento:
  - Latência aceitável: a partir de quantos segundos a resposta perde valor?
  - Custo aceitável: quanto pode custar cada resolução?
  - O que o agente jamais pode fazer: a ação irreversível que ele não executa
    sozinho. Esta linha vira política em D12.
  - A troca que você aceita: quanto de qualidade por quanto de custo?
    Um exemplo numérico vale mais que a fórmula.
-->
**Quando se preenche:** na Atividade Orientada.

[latência aceitável, custo aceitável, o que o agente jamais
pode fazer sozinho, e a troca qualidade × custo que você
aceita — com um exemplo numérico]

---

## 6. Catálogo de ações

<!--
Perguntas que guiam o preenchimento:
  - Para cada ação: nome, entrada, saída, é reversível?, qual o risco se
    errar? As quatro colunas são obrigatórias — "baixo" não é descrição de
    risco.
  - Ações de leitura E de escrita: as que alteram o mundo são as que exigem
    cuidado, e são justamente as que mais ficam de fora.
  - Este catálogo é, literalmente, a lista de ferramentas que você vai
    implementar em D10.
-->
**Quando se preenche:** na Atividade Orientada — o pacote `D2-07` traz o
modelo da tabela e dois exemplos preenchidos.

[tabela: nome · entrada · saída · é reversível? · risco se
errar — ações de leitura e de escrita]

---

## 7. Formulação por busca

<!--
Perguntas que guiam o preenchimento:
  - Qual fatia do problema é um espaço de estados? (Nem toda fatia é — e
    reconhecer a que não é vale tanto quanto formular a que é.)
  - Os cinco componentes: estado inicial, ações, modelo de transição, teste
    de objetivo, custo de caminho. Comece pelo teste de objetivo.
  - O estado descreve a SITUAÇÃO, não a história de como se chegou nela.
-->
**Quando se preenche:** no Laboratório 03, sábado à tarde (encontro 2).

[os cinco componentes do seu subproblema: estado inicial,
ações, transição, teste de objetivo, custo]

## As respostas do meu domínio

**Domínio:** AMS · Assistente de Manutenção Segura

| Dimensão | Minha classificação | Justificativa (uma frase) |
|---|---|---|
| Observabilidade | Parcialmente observável | Os sensores medem apenas quatro variáveis físicas e o texto da ordem é sucinto, não capturando fadiga oculta da máquina nem condições reais omitidas do chão de fábrica. |
| Número de agentes | Multiagente | O técnico de manutenção (que decide a execução final) e o supervisor de segurança (que audita) reagem às recomendações do agente e afetam diretamente o resultado operacional. |
| Determinismo | Estocástico | A ocorrência real de falha mecânica é probabilística, a execução humana varia e a geração de resposta pelo modelo de linguagem (LLM) é estocástica por natureza. |
| Episódico ou sequencial | Episódico (por OS) | Cada ordem de serviço é avaliada de forma independente para gerar o objeto `AvaliacaoRisco`, embora no longo prazo o desgaste físico da máquina na planta seja cumulativo. |
| Estático ou dinâmico | Semidinâmico | A ordem de serviço e as normas não mudam durante a análise, mas o técnico atua sob pressão de tempo entre intervenções, fazendo a demora degradar o valor da recomendação. |
| Discreto ou contínuo | Contínuo (estado) / Discreto (ações) | As leituras dos sensores (temperatura, rotação, torque e desgaste) são grandezas contínuas, enquanto as saídas do agente (3 níveis de risco, 3 NRs e LOTO) são discretas. |
| Conhecido ou desconhecido | Conhecido (normas) / Aprendido em dados (falhas) | As regras de segurança estão documentadas nas NRs (NR-10, NR-12, NR-35), enquanto a relação probabilística entre sensores e falha é extraída do histórico (*AI4I 2020*). |

**O que a tabela de consequências obriga no meu projeto:**

- **O que se aplica (exigências obrigatórias):**
  - *Parcialmente observável* → Exige **estado interno, memória e contexto** (elimina o agente reativo simples e requer engenharia de contexto/RAG para cruzar ordem, sensores e normas).
  - *Multiagente* → Exige **protocolo de comunicação e previsão do outro** (saída estruturada em `AvaliacaoRisco`, curta, justificada em português e auditável pelo técnico e pelo supervisor).
  - *Estocástico* → Exige **cálculo de valor esperado (risco), nova tentativa (retry de validação) e tempo máximo (timeout)** nas chamadas ao modelo.
  - *Semidinâmico* → Exige **prazo de resposta (latência controlada)** e resposta parcial/fallback seguro para não travar o técnico em campo.
  - *Contínuo* → Exige **discretização declarada com granularidade justificada**, convertendo leituras contínuas e probabilidades nos níveis de risco `baixo`, `médio` e `alto`.
- **O que NÃO se aplica (economia de arquitetura):**
  - *Episódico (no recorte por OS)* → **Dispensa avaliação de trajetória inteira**, permitindo avaliar o agente com conjuntos de casos independentes.
  - *Conhecido (nas regras normativas)* → **Dispensa fase de exploração cega no mundo físico**, pois o conhecimento vem do corpus oficial (NRs) e do dataset histórico (*AI4I 2020*).

## Resultado obtido no terminal para o D02-Lab03 (Formular como busca)
Problema escolhido:
Consulta (consultas.py)

(.venv) luciano (D02) meu-projeto-integrador $ python verificar-formulacao.py comum/problemas/consultas.py:PEQUENA
verificar-formulacao — teste de sanidade da formulação de busca

— comum/problemas/consultas.py:PEQUENA
  1. estado é hashable ✅
  2. transição é função ✅
  3. ações estáveis na ordem ✅
  4. custo é positivo ou zero ✅
  5. objetivo é alcançável ✅
  6. estado não guarda o caminho ✅
  resumo: 6 ✅ · 0 ⚠️ · 0 ❌

Seis verificações verdes — a formulação pode ir para o agent-spec.md e para o lab-04.
(.venv) luciano (D02) meu-projeto-integrador $ python verificar-formulacao.py comum/problemas/consultas.py:MAIOR
verificar-formulacao — teste de sanidade da formulação de busca

— comum/problemas/consultas.py:MAIOR
  1. estado é hashable ✅
  2. transição é função ✅
  3. ações estáveis na ordem ✅
  4. custo é positivo ou zero ✅
  5. objetivo é alcançável ✅
  6. estado não guarda o caminho ✅
  resumo: 6 ✅ · 0 ⚠️ · 0 ❌

Seis verificações verdes — a formulação pode ir para o agent-spec.md e para o lab-04.
(.venv) luciano (D02) meu-projeto-integrador $ 
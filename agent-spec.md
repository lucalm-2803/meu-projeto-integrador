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

**Domínio:** AMS · Assistente de Manutenção Segura
**Autor(a):** Luciano Mendes Almeida e assistente de IA · **Última revisão:** 02/11/2026

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

**Revisão N2 — o que mudou e por quê:** não houve devolutiva do E3. Mantive a meta de retrabalho já definida e esclareci que a acurácia dos 30 casos do baseline é uma medida proxy, não a taxa de reabertura em ordens reais.

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

| Dimensão | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Sensores e descrição da OS não mostram toda a condição da máquina; falhas futuras e fatores omitidos não são percebidos antes da decisão. |
| Número de agentes | Multiagente | Técnico e supervisor recebem ou auditam a recomendação e suas decisões afetam o resultado operacional. |
| Determinismo | Estocástico | Falhas, execução humana e respostas do modelo podem variar mesmo com dados semelhantes. |
| Episódico ou sequencial | Episódico por OS, com histórico | Cada OS recebe um parecer próprio, mas a memória de falhas recentes pode influenciar avaliações seguintes. |
| Estático ou dinâmico | Semidinâmico | A OS não muda durante a análise, mas a demora reduz o valor da recomendação para o técnico. |
| Discreto ou contínuo | Estado contínuo; ações discretas | Leituras de sensores são contínuas; classes de risco, normas e decisões são saídas discretas. |
| Conhecido ou desconhecido | Regras conhecidas; risco aprendido | As NRs são documentadas, mas a relação entre leituras e falhas precisa ser estimada a partir de dados. |

**Revisão N2 — o que mudou e por quê:** explicitei que a avaliação é por OS, mas o histórico conecta decisões sucessivas, para compatibilizar o recorte episódico com a memória do baseline.

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

O tipo mais simples adequado é um agente baseado em modelo, com estado interno: a observabilidade parcial faz a leitura atual ser insuficiente, e o agente precisa guardar as falhas recentemente observadas. A ação final continua sendo recomendação ao técnico. A busca é aplicável ao subproblema de ordenar verificações, não substitui a memória nem a avaliação de risco da OS.

**Revisão N2 — o que mudou e por quê:** confirmei a escolha com os erros C07/C08, que mostram a importância do histórico, e delimitei a busca ao subproblema efetivamente medido nos laboratórios.

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

**Primária — taxa de retrabalho:** (OS reabertas em até 30 dias ÷ OS fechadas) × 100, sobre 200 OS do último trimestre; sucesso abaixo de 5%. Valor atual: não medido, pois o projeto ainda não dispõe dessas OS com acompanhamento de 30 dias.

**Secundária 1 — sensibilidade para parada:** casos rotulados `parar_para_manutencao` decididos como parada ÷ total de casos rotulados para parada. No conjunto do D2-06: 8/8 = 100%; limiar de segurança: 100%.

**Secundária 2 — latência:** percentil 95 do tempo entre receber a OS e emitir o parecer; limite técnico atual de 30 s, conforme timeout da chamada ao modelo. Valor medido: não disponível no experimento do baseline, que não registra latência.

**Medida complementar do baseline:** acerto exato da decisão = decisões iguais ao rótulo ÷ 30 casos rotulados. Resultado atual: 25/30 = 83,33%, em `D2-06-agente-baseline/dados/meus_casos.csv` (01 a 16/04/2026; 16 seguir, 8 parar e 6 inspecionar). Esse conjunto não mede a métrica primária de retrabalho.

**Revisão N2 — o que mudou e por quê:** separei a meta operacional de retrabalho do acerto medido em casos rotulados e registrei os valores indisponíveis em vez de inferi-los do baseline.

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

**Latência:** timeout técnico de 30 s na chamada ao modelo; o p95 ainda precisa ser medido em OS representativas para validar que esse limite atende ao técnico.

**Custo:** não há teto monetário por OS definido nos registros do projeto; acompanhar o custo por avaliação e a cota do provedor é requisito antes de ampliar o uso.

**Ações vedadas sem humano:** comandar parada/partida, executar ou remover LOTO, ou declarar a máquina liberada. O agente recomenda e escala; profissional autorizado executa.

**Troca qualidade × custo:** priorizar não deixar passar uma condição que exige parada ou inspeção; quando dados conflitarem ou a confiança for insuficiente, escalar ao técnico/supervisor em vez de produzir uma liberação automática. O limiar monetário e a latência de negócio permanecem para validação com usuários.

**Revisão N2 — o que mudou e por quê:** registrei o timeout já implementado e distingui-o de um SLA validado; não inventei teto de custo nem deleguei ao agente ações físicas.

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

A tabela completa com entradas, saídas, reversibilidade, riscos e ações de leitura e escrita está no [catálogo de ações](D2-07-catalogo-de-acoes/catalogo-de-acoes-modelo.md). Ela inclui consulta à OS, histórico e normas; avaliação, comunicação, registro e escalonamento; e deixa a execução física do LOTO exclusivamente com profissional autorizado.

**Revisão N2 — o que mudou e por quê:** vinculei o catálogo já preenchido, que é a fonte detalhada das ações, para evitar manter duas tabelas divergentes.

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

**Subproblema:** ordenar as verificações de um diagnóstico de manutenção, conforme `comum/problemas/diagnostico_ams.py:MAIOR`.

- **Estado inicial:** nenhuma verificação feita e nenhum resultado positivo.
- **Ações:** executar uma verificação ainda não feita.
- **Transição:** acrescentar a verificação ao conjunto das feitas e, quando aplicável, ao conjunto das positivas; estado é função do estado e da ação.
- **Teste de objetivo:** todas as 11 verificações essenciais foram feitas.
- **Custo:** soma dos tempos das verificações executadas.

A formulação passou os seis testes de sanidade (estado hashable, transição funcional, ações estáveis, custo não negativo, objetivo alcançável e estado sem histórico do caminho).

**Revisão N2 — o que mudou e por quê:** acrescentei os cinco componentes e o resultado de sanidade do Lab-03 para ligar a formulação aos números dos Labs 04 e 05.

## Implicações da caracterização do ambiente

As classificações completas estão na seção 2; as consequências para a arquitetura são:

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
Diagnóstico (diagnostico_ams.py)

(.venv) luciano (D02 *) meu-projeto-integrador $ python verificar-formulacao.py comum/problemas/diagnostico_ams.py:PEQUENA
verificar-formulacao — teste de sanidade da formulação de busca

— comum/problemas/diagnostico_ams.py:PEQUENA
  1. estado é hashable ✅
  2. transição é função ✅
  3. ações estáveis na ordem ✅
  4. custo é positivo ou zero ✅
  5. objetivo é alcançável ✅
  6. estado não guarda o caminho ✅
  resumo: 6 ✅ · 0 ⚠️ · 0 ❌

Seis verificações verdes — a formulação pode ir para o agent-spec.md e para o lab-04.


(.venv) luciano (D02 *) meu-projeto-integrador $ python verificar-formulacao.py comum/problemas/diagnostico_ams.py:MAIOR
verificar-formulacao — teste de sanidade da formulação de busca

— comum/problemas/diagnostico_ams.py:MAIOR
  1. estado é hashable ✅
  2. transição é função ✅
  3. ações estáveis na ordem ✅
  4. custo é positivo ou zero ✅
  5. objetivo é alcançável ✅
  6. estado não guarda o caminho ✅
  resumo: 6 ✅ · 0 ⚠️ · 0 ❌

Seis verificações verdes — a formulação pode ir para o agent-spec.md e para o lab-04.
(.venv) luciano (D02 *) meu-projeto-integrador $ 
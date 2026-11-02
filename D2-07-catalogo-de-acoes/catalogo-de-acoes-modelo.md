# Catálogo de ações — AMS · Assistente de Manutenção Segura

O catálogo descreve o repertório necessário para avaliar uma ordem de serviço
industrial e apoiar o técnico. O AMS recomenda; não substitui a decisão do
técnico nem controla diretamente a máquina. As ações de consulta e análise são
reversíveis porque não alteram a planta; comunicação, registro e execução
operacional têm os riscos e limites descritos abaixo.

| Ação | Entrada | Saída | É reversível? | Risco se errar |
|---|---|---|---|---|
| Consultar a ordem de serviço e as leituras atuais | Identificador da OS ou da máquina; leitura disponível dos sensores | Identificação da máquina, descrição da intervenção e leituras atuais validadas (temperatura, rotação, torque e desgaste) | Sim — apenas consulta dados | Associar a leitura à máquina errada ou usar leitura desatualizada pode produzir uma avaliação falsamente segura ou atrasar a manutenção |
| Consultar o histórico de falhas disponível | Identificador da máquina e registros históricos disponíveis | Falhas e padrões relevantes encontrados, com indicação de lacunas ou ausência de histórico específico da máquina | Sim — apenas consulta dados | Histórico incompleto ou não representativo pode ocultar um padrão de falha e reduzir indevidamente o risco estimado |
| Consultar os requisitos das normas aplicáveis | Descrição da intervenção, contexto informado e corpus vigente das NR-10, NR-12 e NR-35 | Requisitos e trechos de referência pertinentes; normas aplicáveis ou indicação explícita de que nenhuma foi identificada | Sim — apenas consulta documentos | Omitir ou interpretar incorretamente um requisito pode levar o técnico a iniciar uma intervenção sem a proteção exigida |
| Avaliar o risco e preparar o parecer de segurança | OS, leituras validadas, histórico disponível e requisitos normativos encontrados | Nível de risco (baixo, médio ou alto), justificativa, confiança, normas aplicáveis e indicação de necessidade de bloqueio e etiquetagem (LOTO) | Sim — calcula uma recomendação, sem alterar a máquina | Falso risco baixo pode expor o técnico a uma falha ou condição insegura; falso risco alto pode provocar parada e manutenção desnecessárias |
| Comunicar o parecer ao técnico | Parecer validado, identificador da OS e evidências que o sustentam | Recomendação curta em português, com justificativa, normas identificadas e indicação de LOTO | Parcialmente — uma correção pode ser enviada, mas a mensagem original já pode ter sido lida e influenciado a decisão | Uma recomendação incorreta ou ambígua pode induzir uma intervenção insegura, uma parada desnecessária ou o descumprimento de uma norma |
| Registrar a avaliação para auditoria | OS, dados e evidências usados, parecer, data e versão das fontes/regras | Registro rastreável da avaliação e de sua justificativa | Parcialmente — um registro incorreto pode ser corrigido por adendo, mas não deve desaparecer do histórico | Registro associado à OS errada ou sem as evidências pode comprometer a auditoria e decisões posteriores |
| Escalar um caso ao supervisor de segurança | Parecer e motivo de escalonamento, como risco alto, baixa confiança, dados conflitantes ou requisito não localizado | Solicitação de revisão humana com a OS, as evidências e a dúvida identificada | Parcialmente — a solicitação pode ser encerrada ou redirecionada, mas o aviso já foi recebido | Escalonamento excessivo gera fadiga e atraso; deixar de escalar um caso incerto pode permitir uma decisão insegura |
| Executar o bloqueio e a etiquetagem (LOTO) da máquina | Máquina e fontes de energia identificadas, procedimento aplicável e autorização do responsável | Máquina isolada e bloqueada, com identificação e confirmação da execução pelo profissional responsável | Não — remover o bloqueio exige procedimento autorizado; o risco ou a exposição causados por uma execução errada não são desfeitos por um clique | Bloquear a máquina errada interrompe a produção; deixar uma fonte de energia ativa ou remover o bloqueio indevidamente pode causar acidente grave durante a intervenção |

**Quem executa cada ação:** o agente pode consultar os dados e documentos
disponíveis, preparar o parecer e registrar a avaliação. Ele comunica a
recomendação ao técnico; casos incertos ou de risco alto são encaminhados ao
supervisor. O técnico avalia e decide como proceder. O LOTO é executado e
confirmado exclusivamente por profissional autorizado, conforme o procedimento
de segurança aplicável — não pelo agente.

**O que o agente JAMAIS executa sozinho:** comandar a parada ou a partida da
máquina, isolar ou reenergizar fontes de energia, aplicar ou remover cadeados e
etiquetas, nem declarar a máquina liberada para intervenção. O agente pode
indicar que o LOTO é necessário e solicitar confirmação humana; a execução
física e a autorização permanecem com profissionais responsáveis.

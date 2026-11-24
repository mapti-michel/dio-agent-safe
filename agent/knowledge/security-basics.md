# Fundamentos de Segurança da Informação

## Vulnerabilidade

Uma vulnerabilidade é uma falha ou fraqueza em um sistema, aplicação, rede ou processo que pode ser explorada por uma ameaça, comprometendo a segurança dos ativos.

Exemplos:
- Falhas de validação de entrada;
- SQL Injection;
- Configurações inadequadas;
- Software desatualizado;
- Credenciais expostas.

## Ameaça

Uma ameaça representa uma circunstância, evento ou agente com potencial para explorar uma vulnerabilidade e causar danos a sistemas, informações ou organizações.

Exemplos:
- Atacantes mal-intencionados;
- Malware;
- Engenharia social;
- Ameaças internas;
- Desastres naturais.

## Risco

Risco de segurança é a possibilidade de uma ameaça explorar uma vulnerabilidade e causar impactos negativos a um ativo ou organização.

Sua avaliação considera principalmente:
- **Probabilidade:** possibilidade de ocorrência do incidente;
- **Impacto:** consequências caso o incidente aconteça.

A classificação do risco deve considerar o contexto, a exposição do ativo e os controles de segurança existentes. Não se deve atribuir uma pontuação sem critérios justificáveis.

## Princípios de Segurança — Tríade CIA

### Confidencialidade

Garantir que informações sejam acessadas somente por pessoas, processos ou sistemas autorizados.

### Integridade

Garantir que informações e sistemas não sejam alterados, destruídos ou manipulados indevidamente.

### Disponibilidade

Garantir que informações e serviços estejam acessíveis quando necessários por usuários autorizados.

## Classificação e Referências de Vulnerabilidades

### CWE — Common Weakness Enumeration

Catálogo que identifica e classifica tipos de fraquezas em software e hardware.

Exemplo:
- CWE-89: Improper Neutralization of Special Elements used in an SQL Command (SQL Injection).

### OWASP Top 10

Documento de referência que apresenta categorias relevantes de riscos de segurança em aplicações web.

Exemplo:
- A03:2021 — Injection.

O agente deve utilizar referências técnicas pertinentes e evitar classificações incorretas ou desatualizadas.

## Boas Práticas de Segurança

- Manter sistemas, bibliotecas e dependências atualizados;
- Utilizar autenticação forte;
- Armazenar senhas utilizando algoritmos apropriados de hash, como Argon2id;
- Aplicar o princípio do menor privilégio;
- Validar entradas e utilizar consultas parametrizadas;
- Monitorar e registrar eventos relevantes;
- Realizar backups periódicos e testar sua restauração;
- Corrigir vulnerabilidades conhecidas;
- Revisar configurações e permissões;
- Adotar práticas de segurança durante todo o ciclo de desenvolvimento.

## Diretrizes para Análise de Segurança

Ao identificar uma possível vulnerabilidade, o agente deve:

1. Descrever a vulnerabilidade identificada.
2. Explicar sua causa técnica.
3. Identificar os ativos e componentes afetados.
4. Avaliar probabilidade e impacto, justificando a classificação.
5. Apresentar evidências que sustentem a análise.
6. Recomendar medidas de correção e prevenção.
7. Informar limitações e incertezas da análise.

Toda análise prática deve respeitar os limites de autorização, priorizando ambientes controlados e testes não destrutivos.
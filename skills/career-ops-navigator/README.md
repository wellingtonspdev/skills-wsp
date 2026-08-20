# career-ops-navigator

> Guia interativo e assistente de workflow para o projeto **career-ops**, projetado para simplificar a utilização do sistema em múltiplos agentes de IA (Antigravity CLI, Claude Code, Codex, OpenCode e Copilot CLI).

## O que esta skill faz

Esta skill elimina a necessidade de memorizar os dezenas de comandos, scripts `npm` e subcomandos do `career-ops`. Ela traduz os objetivos do usuário em linguagem natural diretamente para a sequência correta de comandos e validações.

## Como utilizar

Basta digitar uma pergunta ou objetivo em linguagem natural em qualquer CLI suportado:

- `"Como usar o career-ops?"`
- `"Quero buscar novas vagas"`
- `"Como me preparar para a entrevista da Empresa X?"`
- `"Qual a ordem dos comandos para me candidatar?"`
- `"Avaliar esta vaga: https://link-da-vaga.com"`

## Estrutura do Projeto

- `SKILL.md`: Roteador principal de intenções, matriz de comandos e salvaguardas.
- Suporta integração com `.agents/`, `.claude/`, `.codex/` e `.github/`.

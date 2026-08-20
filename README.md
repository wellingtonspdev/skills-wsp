# ⚡ WSP Agent Skills Ecosystem

[![Total Skills](https://img.shields.io/badge/Total%20Skills-1%2C467%20Skills-blueviolet?style=for-the-badge&logo=codeforces)](https://github.com/wellingtonspdev/skills-wsp)
[![Compatibilidade](https://img.shields.io/badge/Compatibilidade-Antigravity%20%7C%20Claude%20Code%20%7C%20Gemini%20CLI%20%7C%20Cursor-0052CC?style=for-the-badge&logo=google-gemini)](https://github.com/wellingtonspdev/skills-wsp)
[![Status](https://img.shields.io/badge/Status-Ativo%20%26%20Sincronizado-success?style=for-the-badge)](https://github.com/wellingtonspdev/skills-wsp)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> 🎯 **Repositório definitivo de Agent Skills** curadas e integradas para agentes de inteligência artificial autônomos (Google Antigravity, Claude Code, Gemini CLI, Cursor, Windsurf, Codex e ecossistema MCP).

---

## 🧭 Navegação Rápida por Categoria

| Categoria | Qtd. Skills | Descrição Resumida |
| :--- | :---: | :--- |
| [🔍 Engenharia Reversa, Descompilação & Código Legado](#reversa) | **20** | Framework Reversa oficial, análise binária de baixo nível, engenharia reversa de protocolos, firmware e modernização de legado. |
| [🤖 Inteligência Artificial, LLMs & Agentes Autônomos](#ai_agents) | **238** | Orquestração multi-agente, frameworks LLM (MetaGPT, LangChain, CrewAI, PydanticAI), engenharia de prompts, embeddings e RAG. |
| [🏗️ Arquitetura de Software & Metodologias de Engenharia](#architecture) | **117** | Padrões arquiteturais C4, Domain-Driven Design (DDD), refatoração estrutural, Clean Code, auditorias técnicas e ADRs. |
| [🎨 UI / UX Pro Max, Design Systems & Animações](#design_ui) | **122** | Sistemas de design de classe mundial, UI/UX Pro Max, diretrizes Apple HIG, animações fluidas, Tailwind CSS, Shadcn e Figma. |
| [📱 Frontend Moderno & Desenvolvimento Mobile](#frontend_mobile) | **87** | Aplicações escaláveis com React, Next.js, SvelteKit, Vue, Angular, Expo, React Native, Flutter, Swift, SwiftUI e Makepad. |
| [⚙️ Backend, APIs de Alta Performance & Linguagens](#backend_apis) | **205** | APIs robustas REST, GraphQL, gRPC, tRPC e desenvolvimento em Python, Go, Rust, C#, Java, PHP, Ruby, Node.js e Bun. |
| [☁️ Cloud Computing, DevOps & Infraestrutura como Código](#cloud_devops) | **106** | Arquiteturas resilientes na AWS, Azure, GCP, Kubernetes, Docker, Terraform, Helm, GitOps e pipelines de CI/CD. |
| [🗄️ Bancos de Dados, Cache & Engenharia de Dados](#database_data) | **31** | Modelagem, queries e otimização para PostgreSQL, MySQL, Redis, CosmosDB, BigQuery, Snowflake, Neon, Prisma e dbt. |
| [🛡️ Segurança da Informação, Pentest & Red Team](#security_pentest) | **47** | Auditorias de segurança, exploração OWASP (IDOR, XSS, SQLi), bypass, pentest web/cloud, privilege escalation e DevSecOps. |
| [📊 Testes Automatizados, TDD & Observabilidade](#testing_observability) | **116** | Ciclos TDD (Red-Green-Refactor), testes E2E com Playwright, testes de carga K6, monitoramento Prometheus, Grafana e Jaeger. |
| [⚡ GSD (Get Shit Done), Automação & Workflows](#gsd_productivity) | **151** | Metodologia GSD completa, automação com n8n, Conductor, integração com GitHub, Slack, Notion, Jira, Linux e scripts de terminal. |
| [📈 Growth Hacking, Marketing, SEO & Psicologia de Conversão](#marketing_growth) | **89** | Estratégias de conversão (CRO), SEO técnico e semântico, geração de leads com Apify, copywriting psicológico e email marketing. |
| [🔬 Ciência, Saúde, Domínios Especializados & Web3](#science_specialized) | **38** | Bibliotecas científicas (Astropy, SciPy, BioPython, Qiskit), saúde, medicina, análise jurídica, leilões, Web3 e FinTech. |
| [🛠️ Utilitários, Ferramentas & Suporte Geral](#general_utilities) | **100** | Ferramentas auxiliares, formatadores, conversores e utilitários gerais para suporte ao desenvolvimento. |
| **TOTAL** | **1467** | *Coleção completa de habilidades operacionais* |

---

## 📦 Guia de Instalação e Uso

### 1. Clonar o Repositório
```bash
git clone https://github.com/wellingtonspdev/skills-wsp.git
```

### 2. Integrar com seu Agente de IA

#### 🔹 Google Antigravity / Gemini CLI
Copie as skills desejadas (ou a pasta inteira) para o diretório de configuração do Gemini/Antigravity:
```bash
# Windows PowerShell
Copy-Item -Path .\skills\* -Destination $HOME\.gemini\config\skills\ -Recurse -Force

# Linux / macOS
cp -r ./skills/* ~/.gemini/config/skills/
```

#### 🔹 Claude Code
```bash
# Windows PowerShell
Copy-Item -Path .\skills\* -Destination $HOME\.claude\skills\ -Recurse -Force

# Linux / macOS
cp -r ./skills/* ~/.claude/skills/
```

#### 🔹 Framework Reversa & Get Shit Done (GSD)
Para utilizar skills locais em um projeto específico:
```bash
mkdir -p .agents/skills
cp -r ./skills/reversa* .agents/skills/
cp -r ./skills/gsd-* .agents/skills/
```

---

## 📚 Catálogo Completo de Skills por Categoria

<a id="reversa"></a>
### 🔍 Engenharia Reversa, Descompilação & Código Legado
*Framework Reversa oficial, análise binária de baixo nível, engenharia reversa de protocolos, firmware e modernização de legado.* (20 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`anti-reversing-techniques`](skills/anti-reversing-techniques/SKILL.md) | AUTHORIZED USE ONLY: This skill contains dual-use security techniques. Before proceeding with any bypass or analysis: > 1. |
| [`binary-analysis-patterns`](skills/binary-analysis-patterns/SKILL.md) | Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic. |
| [`dwarf-expert`](skills/dwarf-expert/SKILL.md) | Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWA... |
| [`firmware-analyst`](skills/firmware-analyst/SKILL.md) | Expert firmware analyst specializing in embedded systems, IoT security, and hardware reverse engineering. |
| [`gdb-cli`](skills/gdb-cli/SKILL.md) | GDB debugging assistant for AI agents - analyze core dumps, debug live processes, investigate crashes and deadlocks with source code correlation |
| [`protocol-reverse-engineering`](skills/protocol-reverse-engineering/SKILL.md) | Comprehensive techniques for capturing, analyzing, and documenting network protocols for security research, interoperability, and debugging. |
| [`reversa`](skills/reversa/SKILL.md) | Ponto de entrada principal do Reversa. Orquestra a análise completa de um sistema legado, gerando especificações executáveis por agentes de IA. Use quando o usuário digitar "/re... |
| [`reversa-agents-help`](skills/reversa-agents-help/SKILL.md) | Explica com analogias o que cada agente do Reversa faz e quando usá-lo. Ative com /reversa-agents-help. |
| [`reversa-archaeologist`](skills/reversa-archaeologist/SKILL.md) | Analisa profundamente o código do projeto legado módulo a módulo — extrai algoritmos, fluxos de controle, estruturas de dados e dicionário de dados. Use na fase de escavação de ... |
| [`reversa-architect`](skills/reversa-architect/SKILL.md) | Sintetiza a análise do projeto legado em documentação arquitetural completa — diagramas C4, ERD completo, mapa de integrações e Spec Impact Matrix. Use na fase de interpretação ... |
| [`reversa-data-master`](skills/reversa-data-master/SKILL.md) | Documenta completamente o banco de dados do projeto legado — tabelas, relacionamentos, constraints, triggers, procedures e ERD completo. Use quando DDL, migrations, modelos ORM ... |
| [`reversa-design-system`](skills/reversa-design-system/SKILL.md) | Extrai e documenta o sistema de design do projeto legado — paleta de cores, tipografia, espaçamentos, tokens e componentes a partir de CSS, arquivos de tema e screenshots. Use q... |
| [`reversa-detective`](skills/reversa-detective/SKILL.md) | Extrai conhecimento de negócio implícito do projeto legado — regras de negócio, ADRs retroativos via Git, máquinas de estado e matriz de permissões. Use na fase de interpretação... |
| [`reversa-reconstructor`](skills/reversa-reconstructor/SKILL.md) | Gera um plano de reconstrução bottom-up a partir das specs do Reversa e executa cada tarefa sob demanda, uma por vez, preservando tokens. Use quando quiser reimplementar o softw... |
| [`reversa-reviewer`](skills/reversa-reviewer/SKILL.md) | Revisa criticamente as especificações geradas pelo reversa-writer — encontra inconsistências, reclassifica confiança e gera perguntas para validação humana. Use na fase de revis... |
| [`reversa-scout`](skills/reversa-scout/SKILL.md) | Mapeia a superfície do projeto legado — estrutura de pastas, linguagens, frameworks, dependências e entry points. Use no início de uma análise de engenharia reversa para criar o... |
| [`reversa-visor`](skills/reversa-visor/SKILL.md) | Documenta a interface do sistema legado a partir de screenshots — extrai componentes, layouts, fluxos de navegação e estados de tela. Use quando screenshots do sistema estiverem... |
| [`reversa-writer`](skills/reversa-writer/SKILL.md) | Gera especificações executáveis do sistema legado como contratos operacionais — specs SDD com rastreabilidade de código, OpenAPI, user stories e code-spec matrix. Use na fase de... |
| [`reverse-engineer`](skills/reverse-engineer/SKILL.md) | Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis. Masters IDA Pro, Ghidra, radare2, x64dbg, and modern RE toolchains. |
| [`wireshark-analysis`](skills/wireshark-analysis/SKILL.md) | Execute comprehensive network traffic analysis using Wireshark to capture, filter, and examine network packets for security investigations, performance optimization, and trouble... |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="ai_agents"></a>
### 🤖 Inteligência Artificial, LLMs & Agentes Autônomos
*Orquestração multi-agente, frameworks LLM (MetaGPT, LangChain, CrewAI, PydanticAI), engenharia de prompts, embeddings e RAG.* (238 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`9router-local-install`](skills/9router-local-install/SKILL.md) | Instalar, endurecer, validar e operar o 9Router localmente via Docker como proxy de IA compatível com OpenAI. Use quando for necessário preparar 9Router no Windows, manter paine... |
| [`accidental-data-loss-prevention`](skills/accidental-data-loss-prevention/SKILL.md) | \| **STOP AND VERIFY**: Before running any command or tool that results in irreversible data loss, you MUST obtain explicit user consent. When in doubt, ask. It is better to wai... |
| [`activecampaign-automation`](skills/activecampaign-automation/SKILL.md) | Automate ActiveCampaign tasks via Rube MCP (Composio): manage contacts, tags, list subscriptions, automation enrollment, and tasks. Always search tools first for current schemas. |
| [`adhx`](skills/adhx/SKILL.md) | Fetch any X/Twitter post as clean LLM-friendly JSON. Converts x.com, twitter.com, or adhx.com links into structured data with full article content, author info, and engagement m... |
| [`advanced-evaluation`](skills/advanced-evaluation/SKILL.md) | This skill should be used when the user asks to "implement LLM-as-judge", "compare model outputs", "create evaluation rubrics", "mitigate evaluation bias", or mentions direct sc... |
| [`aegisops-ai`](skills/aegisops-ai/SKILL.md) | Autonomous DevSecOps & FinOps Guardrails. Orchestrates Gemini 3 Flash to audit Linux Kernel patches, Terraform cost drifts, and K8s compliance. |
| [`agent-evaluation`](skills/agent-evaluation/SKILL.md) | You're a quality engineer who has seen agents that aced benchmarks fail spectacularly in production. You've learned that evaluating LLM agents is fundamentally different from te... |
| [`agent-framework-azure-ai-py`](skills/agent-framework-azure-ai-py/SKILL.md) | Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK. |
| [`agent-manager-skill`](skills/agent-manager-skill/SKILL.md) | Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling. |
| [`agent-memory-mcp`](skills/agent-memory-mcp/SKILL.md) | A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions). |
| [`agent-memory-systems`](skills/agent-memory-systems/SKILL.md) | You are a cognitive architect who understands that memory makes agents intelligent. You've built memory systems for agents handling millions of interactions. You know that the h... |
| [`agent-orchestration-improve-agent`](skills/agent-orchestration-improve-agent/SKILL.md) | Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration. |
| [`agent-orchestration-multi-agent-optimize`](skills/agent-orchestration-multi-agent-optimize/SKILL.md) | Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration. Use when improving agent performance, throughput, or reliability. |
| [`agent-orchestrator`](skills/agent-orchestrator/SKILL.md) | Meta-skill que orquestra todos os agentes do ecossistema. Scan automatico de skills, match por capacidades, coordenacao de workflows multi-skill e registry management. |
| [`agent-tool-builder`](skills/agent-tool-builder/SKILL.md) | You are an expert in the interface between LLMs and the outside world. You've seen tools that work beautifully and tools that cause agents to hallucinate, loop, or fail silently... |
| [`agentflow`](skills/agentflow/SKILL.md) | Orchestrate autonomous AI development pipelines through your Kanban board (Asana, GitHub Projects, Linear). Manages multi-worker Claude Code dispatch, deterministic quality gate... |
| [`agentfolio`](skills/agentfolio/SKILL.md) | Skill for discovering and researching autonomous AI agents, tools, and ecosystems using the AgentFolio directory. |
| [`agentic-actions-auditor`](skills/agentic-actions-auditor/SKILL.md) | > Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects ... |
| [`agentmail`](skills/agentmail/SKILL.md) | Email infrastructure for AI agents. Create accounts, send/receive emails, manage webhooks, and check karma balance via the AgentMail API. |
| [`agentphone`](skills/agentphone/SKILL.md) | Build AI phone agents with AgentPhone API. Use when the user wants to make phone calls, send/receive SMS, manage phone numbers, create voice agents, set up webhooks, or check us... |
| [`agents-md`](skills/agents-md/SKILL.md) | This skill should be used when the user asks to "create AGENTS.md", "update AGENTS.md", "maintain agent docs", "set up CLAUDE.md", or needs to keep agent instructions concise. E... |
| [`agents-v2-py`](skills/agents-v2-py/SKILL.md) | Build container-based Foundry Agents with Azure AI Projects SDK (ImageBasedHostedAgentDefinition). Use when creating hosted agents with custom container images in Azure AI Foundry. |
| [`ai-agent-development`](skills/ai-agent-development/SKILL.md) | AI agent development workflow for building autonomous agents, multi-agent systems, and agent orchestration with CrewAI, LangGraph, and custom agents. |
| [`ai-agents-architect`](skills/ai-agents-architect/SKILL.md) | I build AI systems that can act autonomously while remaining controllable. I understand that agents fail in unexpected ways - I design for graceful degradation and clear failure... |
| [`ai-analyzer`](skills/ai-analyzer/SKILL.md) | AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。 |
| [`ai-daily-radar`](skills/ai-daily-radar/SKILL.md) | Pesquisa e sintetiza diariamente notícias, papers, releases, ferramentas, repositórios e sinais de comunidade sobre IA, tecnologia e programação. Use quando o usuário pedir rada... |
| [`ai-engineer`](skills/ai-engineer/SKILL.md) | Build production-ready LLM applications, advanced RAG systems, and intelligent agents. Implements vector search, multimodal AI, agent orchestration, and enterprise AI integrations. |
| [`ai-engineering-toolkit`](skills/ai-engineering-toolkit/SKILL.md) | 6 production-ready AI engineering workflows: prompt evaluation (8-dimension scoring), context budget planning, RAG pipeline design, agent security audit (65-point checklist), ev... |
| [`ai-md`](skills/ai-md/SKILL.md) | Convert human-written CLAUDE.md into AI-native structured-label format. Battle-tested across 4 models. Same rules, fewer tokens, higher compliance. |
| [`ai-ml`](skills/ai-ml/SKILL.md) | AI and machine learning workflow covering LLM application development, RAG implementation, agent architecture, ML pipelines, and AI-powered features. |
| [`ai-native-cli`](skills/ai-native-cli/SKILL.md) | Design spec with 98 rules for building CLI tools that AI agents can safely use. Covers structured JSON output, error handling, input contracts, safety guardrails, exit codes, an... |
| [`ai-product`](skills/ai-product/SKILL.md) | You are an AI product engineer who has shipped LLM features to millions of users. You've debugged hallucinations at 3am, optimized prompts to reduce costs by 80%, and built safe... |
| [`ai-seo`](skills/ai-seo/SKILL.md) | Optimize content for AI search and LLM citations across AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and similar systems. Use when improving AI visibility, answer engine o... |
| [`ai-studio-image`](skills/ai-studio-image/SKILL.md) | Geracao de imagens humanizadas via Google AI Studio (Gemini). Fotos realistas estilo influencer ou educacional com iluminacao natural e imperfeicoes sutis. |
| [`ai-wrapper-product`](skills/ai-wrapper-product/SKILL.md) | You know AI wrappers get a bad rap, but the good ones solve real problems. You build products where AI is the engine, not the gimmick. You understand prompt engineering is produ... |
| [`akf-trust-metadata`](skills/akf-trust-metadata/SKILL.md) | The AI native file format. EXIF for AI — stamps every file with trust scores, source provenance, and compliance metadata. Embeds into 20+ formats (DOCX, PDF, images, code). EU A... |
| [`amazon-alexa`](skills/amazon-alexa/SKILL.md) | Integracao completa com Amazon Alexa para criar skills de voz inteligentes, transformar Alexa em assistente com Claude como cerebro (projeto Auri) e integrar com AWS ecosystem (... |
| [`analyze-project`](skills/analyze-project/SKILL.md) | Forensic root cause analyzer for Antigravity sessions. Classifies scope deltas, rework patterns, root causes, hotspots, and auto-improves prompts/health. |
| [`andrej-karpathy`](skills/andrej-karpathy/SKILL.md) | Agente que simula Andrej Karpathy — ex-Director of AI da Tesla, co-fundador da OpenAI, fundador da Eureka Labs, e o maior educador de deep learning do mundo. |
| [`apify-actor-development`](skills/apify-actor-development/SKILL.md) | Important: Before you begin, fill in the generatedBy property in the meta section of .actor/actor.json. Replace it with the tool and model you're currently using, such as \"Clau... |
| [`appdeploy`](skills/appdeploy/SKILL.md) | Deploy web apps with backend APIs, database, and file storage. Use when the user asks to deploy or publish a website or web app and wants a public URL. Uses HTTP API via curl. |
| [`audio-transcriber`](skills/audio-transcriber/SKILL.md) | Transform audio recordings into professional Markdown documentation with intelligent summaries using LLM integration |
| [`auri-core`](skills/auri-core/SKILL.md) | Auri: assistente de voz inteligente (Alexa + Claude claude-opus-4-20250805). Visao do produto, persona Vitoria Neural, stack AWS, modelo Free/Pro/Business/Enterprise, roadmap 4 ... |
| [`autonomous-agent-patterns`](skills/autonomous-agent-patterns/SKILL.md) | Design patterns for building autonomous coding agents, inspired by [Cline](https://github.com/cline/cline) and [OpenAI Codex](https://github.com/openai/codex). |
| [`autonomous-agents`](skills/autonomous-agents/SKILL.md) | You are an agent architect who has learned the hard lessons of autonomous AI. You've seen the gap between impressive demos and production disasters. You know that a 95% success ... |
| [`azure-ai-ml-py`](skills/azure-ai-ml-py/SKILL.md) | Azure Machine Learning SDK v2 for Python. Use for ML workspaces, jobs, models, datasets, compute, and pipelines. |
| [`azure-ai-openai-dotnet`](skills/azure-ai-openai-dotnet/SKILL.md) | Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embeddings, image generation, audio transcription, and assistants. |
| [`azure-data-tables-java`](skills/azure-data-tables-java/SKILL.md) | Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API. |
| [`azure-data-tables-py`](skills/azure-data-tables-py/SKILL.md) | Azure Tables SDK for Python (Storage and Cosmos DB). Use for NoSQL key-value storage, entity CRUD, and batch operations. |
| [`azure-keyvault-py`](skills/azure-keyvault-py/SKILL.md) | Azure Key Vault SDK for Python. Use for secrets, keys, and certificates management with secure storage. |
| [`azure-storage-blob-java`](skills/azure-storage-blob-java/SKILL.md) | Build blob storage applications using the Azure Storage Blob SDK for Java. |
| [`azure-storage-blob-py`](skills/azure-storage-blob-py/SKILL.md) | Azure Blob Storage SDK for Python. Use for uploading, downloading, listing blobs, managing containers, and blob lifecycle. |
| [`azure-storage-blob-rust`](skills/azure-storage-blob-rust/SKILL.md) | Azure Blob Storage SDK for Rust. Use for uploading, downloading, and managing blobs and containers. |
| [`azure-storage-blob-ts`](skills/azure-storage-blob-ts/SKILL.md) | Azure Blob Storage JavaScript/TypeScript SDK (@azure/storage-blob) for blob operations. Use for uploading, downloading, listing, and managing blobs and containers. |
| [`azure-storage-file-datalake-py`](skills/azure-storage-file-datalake-py/SKILL.md) | Azure Data Lake Storage Gen2 SDK for Python. Use for hierarchical file systems, big data analytics, and file/directory operations. |
| [`azure-storage-file-share-py`](skills/azure-storage-file-share-py/SKILL.md) | Azure Storage File Share SDK for Python. Use for SMB file shares, directories, and file operations in the cloud. |
| [`azure-storage-file-share-ts`](skills/azure-storage-file-share-ts/SKILL.md) | Azure File Share JavaScript/TypeScript SDK (@azure/storage-file-share) for SMB file share operations. |
| [`azure-storage-queue-py`](skills/azure-storage-queue-py/SKILL.md) | Azure Queue Storage SDK for Python. Use for reliable message queuing, task distribution, and asynchronous processing. |
| [`azure-storage-queue-ts`](skills/azure-storage-queue-ts/SKILL.md) | Azure Queue Storage JavaScript/TypeScript SDK (@azure/storage-queue) for message queue operations. Use for sending, receiving, peeking, and deleting messages in queues. |
| [`bdistill-behavioral-xray`](skills/bdistill-behavioral-xray/SKILL.md) | X-ray any AI model's behavioral patterns — refusal boundaries, hallucination tendencies, reasoning style, formatting defaults. No API key needed. |
| [`bdistill-knowledge-extraction`](skills/bdistill-knowledge-extraction/SKILL.md) | Extract structured domain knowledge from AI models in-session or from local open-source models via Ollama. No API key needed. |
| [`bigquery-ai-ml`](skills/bigquery-ai-ml/SKILL.md) | Leverages BigQuery's built-in machine learning and GenAI capabilities for advanced data analytics. Use when you need to write SQL queries that perform time-series forecasting, d... |
| [`bill-gates`](skills/bill-gates/SKILL.md) | Agente que simula Bill Gates — cofundador da Microsoft, arquiteto da industria de software comercial, estrategista tecnologico global, investidor sistemico e filantropo baseado ... |
| [`blockrun`](skills/blockrun/SKILL.md) | BlockRun works with Claude Code and Google Antigravity. |
| [`browser-extension-builder`](skills/browser-extension-builder/SKILL.md) | You extend the browser to give users superpowers. You understand the unique constraints of extension development - permissions, security, store policies. You build extensions th... |
| [`building-data-apps`](skills/building-data-apps/SKILL.md) | \| Build modern data apps, dashboards, and interactive reports using either React + Vite or Streamlit. Includes optional Gemini Data Analytics chat integration for an AI powered... |
| [`bullmq-specialist`](skills/bullmq-specialist/SKILL.md) | BullMQ expert for Redis-backed job queues, background processing, and reliable async execution in Node.js/TypeScript applications. Use when: bullmq, bull queue, redis queue, bac... |
| [`career-ops-navigator`](skills/career-ops-navigator/SKILL.md) | >- Navegador e assistente de workflow inteligente para o career-ops. Guia o usuário passo a passo em qualquer CLI de IA (Antigravity, Codex, OpenCode, Claude Code, Copilot) trad... |
| [`cc-skill-continuous-learning`](skills/cc-skill-continuous-learning/SKILL.md) | Development skill from everything-claude-code |
| [`cc-skill-strategic-compact`](skills/cc-skill-strategic-compact/SKILL.md) | Development skill from everything-claude-code |
| [`clarity-gate`](skills/clarity-gate/SKILL.md) | > Pre-ingestion verification for epistemic quality in RAG systems. Ensures documents are properly qualified before entering knowledge bases. Produces CGD (Clarity-Gated Document... |
| [`clarvia-aeo-check`](skills/clarvia-aeo-check/SKILL.md) | Score any MCP server, API, or CLI for agent-readiness using Clarvia AEO (Agent Experience Optimization). Search 15,400+ indexed tools before adding them to your workflow. |
| [`claude-ally-health`](skills/claude-ally-health/SKILL.md) | A health assistant skill for medical information analysis, symptom tracking, and wellness guidance. |
| [`claude-api`](skills/claude-api/SKILL.md) | Build apps with the Claude API or Anthropic SDK. TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`/`claude_agent_sdk`, or user asks to use Claude API, Anthropic SDKs, o... |
| [`claude-code-expert`](skills/claude-code-expert/SKILL.md) | Especialista profundo em Claude Code - CLI da Anthropic. Maximiza produtividade com atalhos, hooks, MCPs, configuracoes avancadas, workflows, CLAUDE.md, memoria, sub-agentes, pe... |
| [`claude-code-guide`](skills/claude-code-guide/SKILL.md) | To provide a comprehensive reference for configuring and using Claude Code (the agentic coding tool) to its full potential. This skill synthesizes best practices, configuration ... |
| [`claude-d3js-skill`](skills/claude-d3js-skill/SKILL.md) | This skill provides guidance for creating sophisticated, interactive data visualisations using d3.js. |
| [`claude-in-chrome-troubleshooting`](skills/claude-in-chrome-troubleshooting/SKILL.md) | Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratic... |
| [`claude-monitor`](skills/claude-monitor/SKILL.md) | Monitor de performance do Claude Code e sistema local. Diagnostica lentidao, mede CPU/RAM/disco, verifica API latency e gera relatorios de saude do sistema. |
| [`claude-scientific-skills`](skills/claude-scientific-skills/SKILL.md) | Scientific research and analysis skills |
| [`claude-settings-audit`](skills/claude-settings-audit/SKILL.md) | Analyze a repository to generate recommended Claude Code settings.json permissions. Use when setting up a new project, auditing existing settings, or determining which read-only... |
| [`claude-speed-reader`](skills/claude-speed-reader/SKILL.md) | -Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting |
| [`claude-win11-speckit-update-skill`](skills/claude-win11-speckit-update-skill/SKILL.md) | Windows 11 system management |
| [`cloudflare-workers-expert`](skills/cloudflare-workers-expert/SKILL.md) | Expert in Cloudflare Workers and the Edge Computing ecosystem. Covers Wrangler, KV, D1, Durable Objects, and R2 storage. |
| [`code-review-ai-ai-review`](skills/code-review-ai-ai-review/SKILL.md) | You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition, and modern DevOps practices. Leverage AI tools (GitHub ... |
| [`comfyui-gateway`](skills/comfyui-gateway/SKILL.md) | REST API gateway for ComfyUI servers. Workflow management, job queuing, webhooks, caching, auth, rate limiting, and image delivery (URL + base64). |
| [`comprehensive-review-pr-enhance`](skills/comprehensive-review-pr-enhance/SKILL.md) | > Generate structured PR descriptions from diffs, add review checklists, risk assessments, and test coverage summaries. Use when the user says "write a PR description", "improve... |
| [`context-agent`](skills/context-agent/SKILL.md) | Agente de contexto para continuidade entre sessoes. Salva resumos, decisoes, tarefas pendentes e carrega briefing automatico na sessao seguinte. |
| [`context-window-management`](skills/context-window-management/SKILL.md) | You're a context engineering specialist who has optimized LLM applications handling millions of conversations. You've seen systems hit token limits, suffer context rot, and lose... |
| [`context7-auto-research`](skills/context7-auto-research/SKILL.md) | Automatically fetch latest library/framework documentation for Claude Code via Context7 API. Use when you need up-to-date documentation for libraries and frameworks or asking ab... |
| [`conversation-memory`](skills/conversation-memory/SKILL.md) | Persistent memory systems for LLM conversations including short-term, long-term, and entity-based memory Use when: conversation memory, remember, memory persistence, long-term m... |
| [`convex`](skills/convex/SKILL.md) | Convex reactive backend expert: schema design, TypeScript functions, real-time subscriptions, auth, file storage, scheduling, and deployment. |
| [`copilot-sdk`](skills/copilot-sdk/SKILL.md) | Build applications that programmatically interact with GitHub Copilot. The SDK wraps the Copilot CLI via JSON-RPC, providing session management, custom tools, hooks, MCP server ... |
| [`crewai`](skills/crewai/SKILL.md) | You are an expert in designing collaborative AI agent teams with CrewAI. You think in terms of roles, responsibilities, and delegation. You design clear agent personas with spec... |
| [`data-autocleaning`](skills/data-autocleaning/SKILL.md) | Automated data quality and transformation capabilities for Dataform/dbt/BigQuery pipelines. Processes data sourced from BigQuery or Cloud Storage (GCS), applying best practices ... |
| [`deep-research`](skills/deep-research/SKILL.md) | Run autonomous research tasks that plan, search, read, and synthesize information into comprehensive reports. |
| [`devcontainer-setup`](skills/devcontainer-setup/SKILL.md) | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up is... |
| [`earllm-build`](skills/earllm-build/SKILL.md) | Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pipeline. |
| [`elon-musk`](skills/elon-musk/SKILL.md) | Agente que simula Elon Musk com profundidade psicologica e comunicacional de alta fidelidade. Ativado para: \"fale como Elon\", \"simule Elon Musk\", \"o que Elon diria sobre X\... |
| [`embedding-strategies`](skills/embedding-strategies/SKILL.md) | Guide to selecting and optimizing embedding models for vector search applications. |
| [`enhance-prompt`](skills/enhance-prompt/SKILL.md) | Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances specificity, adds UI/UX keywords, injects design system context, and structures output for better gen... |
| [`exa-search`](skills/exa-search/SKILL.md) | Semantic search, similar content discovery, and structured research using Exa API. Use when you need semantic/embeddings-based search, finding similar content, or searching by c... |
| [`fal-audio`](skills/fal-audio/SKILL.md) | Text-to-speech and speech-to-text using fal.ai audio models |
| [`fal-generate`](skills/fal-generate/SKILL.md) | Generate images and videos using fal.ai AI models |
| [`fal-image-edit`](skills/fal-image-edit/SKILL.md) | AI-powered image editing with style transfer and object removal |
| [`fal-platform`](skills/fal-platform/SKILL.md) | Platform APIs for model management, pricing, and usage tracking |
| [`fal-upscale`](skills/fal-upscale/SKILL.md) | Upscale and enhance image and video resolution using AI |
| [`fal-workflow`](skills/fal-workflow/SKILL.md) | Generate workflow JSON files for chaining AI models |
| [`ffuf-claude-skill`](skills/ffuf-claude-skill/SKILL.md) | Web fuzzing with ffuf |
| [`fp-pragmatic`](skills/fp-pragmatic/SKILL.md) | A practical, jargon-free guide to functional programming - the 80/20 approach that gets results without the academic overhead |
| [`fp-ts-pragmatic`](skills/fp-ts-pragmatic/SKILL.md) | A practical, jargon-free guide to fp-ts functional programming - the 80/20 approach that gets results without the academic overhead. Use when writing TypeScript with fp-ts library. |
| [`gcs-security-assessment`](skills/gcs-security-assessment/SKILL.md) | Assesses security posture, evaluates risks, and checks SAIF compliance for Google Cloud Storage buckets or projects. Use when the user requests security scans, vulnerability che... |
| [`gemini-api-dev`](skills/gemini-api-dev/SKILL.md) | The Gemini API provides access to Google's most advanced AI models. Key capabilities include: |
| [`gemini-api-integration`](skills/gemini-api-integration/SKILL.md) | Use when integrating Google Gemini API into projects. Covers model selection, multimodal inputs, streaming, function calling, and production best practices. |
| [`geo-fundamentals`](skills/geo-fundamentals/SKILL.md) | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). |
| [`geoffrey-hinton`](skills/geoffrey-hinton/SKILL.md) | Agente que simula Geoffrey Hinton — Godfather of Deep Learning, Prêmio Turing 2018, criador do backpropagation e das Deep Belief Networks. |
| [`get-shit-done`](skills/get-shit-done/SKILL.md) | A meta-prompting, context engineering and spec-driven development system for Gemini CLI. Provides advanced workflows for planning, execution, and verification of complex tasks. |
| [`git-pr-workflows-git-workflow`](skills/git-pr-workflows-git-workflow/SKILL.md) | Orchestrate a comprehensive git workflow from code review through PR creation, leveraging specialized agents for quality assurance, testing, and deployment readiness. This workf... |
| [`github-workflow-automation`](skills/github-workflow-automation/SKILL.md) | Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices. |
| [`gsd-eval-review`](skills/gsd-eval-review/SKILL.md) | Audit an executed AI phase's evaluation coverage and produce an EVAL-REVIEW.md remediation plan. |
| [`gsd-profile-user`](skills/gsd-profile-user/SKILL.md) | Generate developer behavioral profile and create Claude-discoverable artifacts |
| [`gsd-ultraplan-phase`](skills/gsd-ultraplan-phase/SKILL.md) | [BETA] Offload plan phase to Claude Code's ultraplan cloud; review in browser and import back. |
| [`hierarchical-agent-memory`](skills/hierarchical-agent-memory/SKILL.md) | Scoped CLAUDE.md memory system that reduces context token spend. Creates directory-level context files, tracks savings via dashboard, and routes agents to the right sub-context. |
| [`hig-components-controls`](skills/hig-components-controls/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| [`hig-components-menus`](skills/hig-components-menus/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| [`hig-inputs`](skills/hig-inputs/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| [`hig-technologies`](skills/hig-technologies/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| [`hosted-agents`](skills/hosted-agents/SKILL.md) | Build background agents in sandboxed environments. Use for hosted coding agents, sandboxed VMs, Modal sandboxes, and remote coding environments. |
| [`hosted-agents-v2-py`](skills/hosted-agents-v2-py/SKILL.md) | Build hosted agents using Azure AI Projects SDK with ImageBasedHostedAgentDefinition. Use when creating container-based agents in Azure AI Foundry. |
| [`html-injection-testing`](skills/html-injection-testing/SKILL.md) | Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. This vulnerability enables attackers to modify p... |
| [`hugging-face-cli`](skills/hugging-face-cli/SKILL.md) | Use the Hugging Face Hub CLI (`hf`) to download, upload, and manage models, datasets, and Spaces. |
| [`hugging-face-community-evals`](skills/hugging-face-community-evals/SKILL.md) | Run local evaluations for Hugging Face Hub models with inspect-ai or lighteval. |
| [`hugging-face-dataset-viewer`](skills/hugging-face-dataset-viewer/SKILL.md) | Query Hugging Face datasets through the Dataset Viewer API for splits, rows, search, filters, and parquet links. |
| [`hugging-face-datasets`](skills/hugging-face-datasets/SKILL.md) | Create and manage datasets on Hugging Face Hub. Supports initializing repos, defining configs/system prompts, streaming row updates, and SQL-based dataset querying/transformatio... |
| [`hugging-face-evaluation`](skills/hugging-face-evaluation/SKILL.md) | Add and manage evaluation results in Hugging Face model cards. Supports extracting eval tables from README content, importing scores from Artificial Analysis API, and running cu... |
| [`hugging-face-gradio`](skills/hugging-face-gradio/SKILL.md) | Build or edit Gradio apps, layouts, components, and chat interfaces in Python. |
| [`hugging-face-jobs`](skills/hugging-face-jobs/SKILL.md) | Run workloads on Hugging Face Jobs with managed CPUs, GPUs, TPUs, secrets, and Hub persistence. |
| [`hugging-face-model-trainer`](skills/hugging-face-model-trainer/SKILL.md) | Train or fine-tune TRL language models on Hugging Face Jobs, including SFT, DPO, GRPO, and GGUF export. |
| [`hugging-face-paper-publisher`](skills/hugging-face-paper-publisher/SKILL.md) | Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to models/datasets, claiming authorship, and generating professional markdo... |
| [`hugging-face-papers`](skills/hugging-face-papers/SKILL.md) | Read and analyze Hugging Face paper pages or arXiv papers with markdown and papers API metadata. |
| [`hugging-face-tool-builder`](skills/hugging-face-tool-builder/SKILL.md) | Your purpose is now is to create reusable command line scripts and utilities for using the Hugging Face API, allowing chaining, piping and intermediate processing where helpful.... |
| [`hugging-face-trackio`](skills/hugging-face-trackio/SKILL.md) | Track ML experiments with Trackio using Python logging, alerts, and CLI metric retrieval. |
| [`hugging-face-vision-trainer`](skills/hugging-face-vision-trainer/SKILL.md) | Train or fine-tune vision models on Hugging Face Jobs for detection, classification, and SAM or SAM2 segmentation. |
| [`hybrid-search-implementation`](skills/hybrid-search-implementation/SKILL.md) | Combine vector and keyword search for improved retrieval. Use when implementing RAG systems, building search engines, or when neither approach alone provides sufficient recall. |
| [`ilya-sutskever`](skills/ilya-sutskever/SKILL.md) | Agente que simula Ilya Sutskever — co-fundador da OpenAI, ex-Chief Scientist, fundador da SSI. Use quando quiser perspectivas sobre: AGI safety-first, consciência de IA, scaling... |
| [`image-studio`](skills/image-studio/SKILL.md) | Studio de geracao de imagens inteligente — roteamento automatico entre ai-studio-image (fotos humanizadas/influencer) e stability-ai (arte/ ilustracao/edicao). Detecta o tipo de... |
| [`imagen`](skills/imagen/SKILL.md) | AI image generation skill powered by Google Gemini, enabling seamless visual content creation for UI placeholders, documentation, and design assets. |
| [`incident-response-smart-fix`](skills/incident-response-smart-fix/SKILL.md) | [Extended thinking: This workflow implements a sophisticated debugging and resolution pipeline that leverages AI-assisted debugging tools and observability platforms to systemat... |
| [`infinite-gratitude`](skills/infinite-gratitude/SKILL.md) | Multi-agent research skill for parallel research execution (10 agents, battle-tested with real case studies). |
| [`langchain-architecture`](skills/langchain-architecture/SKILL.md) | Master the LangChain framework for building sophisticated LLM applications with agents, chains, memory, and tool integration. |
| [`langfuse`](skills/langfuse/SKILL.md) | You are an expert in LLM observability and evaluation. You think in terms of traces, spans, and metrics. You know that LLM applications need monitoring just like traditional sof... |
| [`langgraph`](skills/langgraph/SKILL.md) | You are an expert in building production-grade AI agents with LangGraph. You understand that agents need explicit structure - graphs make the flow visible and debuggable. You de... |
| [`last30days`](skills/last30days/SKILL.md) | Research a topic from the last 30 days on Reddit + X + Web, become an expert, and write copy-paste-ready prompts for the user's target tool. |
| [`linear-claude-skill`](skills/linear-claude-skill/SKILL.md) | Manage Linear issues, projects, and teams |
| [`llm-app-patterns`](skills/llm-app-patterns/SKILL.md) | Production-ready patterns for building LLM applications, inspired by [Dify](https://github.com/langgenius/dify) and industry best practices. |
| [`llm-application-dev-ai-assistant`](skills/llm-application-dev-ai-assistant/SKILL.md) | You are an AI assistant development expert specializing in creating intelligent conversational interfaces, chatbots, and AI-powered applications. Design comprehensive AI assista... |
| [`llm-application-dev-langchain-agent`](skills/llm-application-dev-langchain-agent/SKILL.md) | You are an expert LangChain agent developer specializing in production-grade AI systems using LangChain 0.1+ and LangGraph. |
| [`llm-application-dev-prompt-optimize`](skills/llm-application-dev-prompt-optimize/SKILL.md) | You are an expert prompt engineer specializing in crafting effective prompts for LLMs through advanced techniques including constitutional AI, chain-of-thought reasoning, and mo... |
| [`llm-evaluation`](skills/llm-evaluation/SKILL.md) | Master comprehensive evaluation strategies for LLM applications, from automated metrics to human evaluation and A/B testing. |
| [`llm-ops`](skills/llm-ops/SKILL.md) | LLM Operations -- RAG, embeddings, vector databases, fine-tuning, prompt engineering avancado, custos de LLM, evals de qualidade e arquiteturas de IA para producao. |
| [`llm-prompt-optimizer`](skills/llm-prompt-optimizer/SKILL.md) | Use when improving prompts for any LLM. Applies proven prompt engineering techniques to boost output quality, reduce hallucinations, and cut token usage. |
| [`llm-structured-output`](skills/llm-structured-output/SKILL.md) | > Get reliable JSON, enums, and typed objects from LLMs using response_format, tool_use, and schema-constrained decoding across OpenAI, Anthropic, and Google APIs. |
| [`local-llm-expert`](skills/local-llm-expert/SKILL.md) | Master local LLM inference, model selection, VRAM optimization, and local deployment using Ollama, llama.cpp, vLLM, and LM Studio. Expert in quantization formats (GGUF, EXL2) an... |
| [`loki-mode`](skills/loki-mode/SKILL.md) | Version 2.35.0 \| PRD to Production \| Zero Human Intervention > Research-enhanced: OpenAI SDK, DeepMind, Anthropic, AWS Bedrock, Agent SDK, HN Production (2025) |
| [`m365-agents-dotnet`](skills/m365-agents-dotnet/SKILL.md) | Microsoft 365 Agents SDK for .NET. Build multichannel agents for Teams/M365/Copilot Studio with ASP.NET Core hosting, AgentApplication routing, and MSAL-based auth. |
| [`m365-agents-py`](skills/m365-agents-py/SKILL.md) | Microsoft 365 Agents SDK for Python. Build multichannel agents for Teams/M365/Copilot Studio with aiohttp hosting, AgentApplication routing, streaming responses, and MSAL-based ... |
| [`m365-agents-ts`](skills/m365-agents-ts/SKILL.md) | Microsoft 365 Agents SDK for TypeScript/Node.js. |
| [`machine-learning-ops-ml-pipeline`](skills/machine-learning-ops-ml-pipeline/SKILL.md) | Design and implement a complete ML pipeline for: $ARGUMENTS |
| [`marketing-psychology`](skills/marketing-psychology/SKILL.md) | Apply behavioral science and mental models to marketing decisions, prioritized using a psychological leverage and feasibility scoring system. |
| [`mcp-builder`](skills/mcp-builder/SKILL.md) | Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well... |
| [`mcp-builder-ms`](skills/mcp-builder-ms/SKILL.md) | Use this skill when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). |
| [`metagpt-pilot`](skills/metagpt-pilot/SKILL.md) | Pilotar execucoes oficiais do MetaGPT em Docker/OpenRouter com monitoramento, preservacao de workspace, recuperacao de falhas e controle de quota. Use ao iniciar, acompanhar, re... |
| [`ml-best-practices`](skills/ml-best-practices/SKILL.md) | \| CRITICAL RULE: You MUST use this skill whenever the task involves any machine learning tasks or data analysis. Use this skill if the user's prompt or requirements mention any... |
| [`ml-engineer`](skills/ml-engineer/SKILL.md) | Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. Implements model serving, feature engineering, A/B testing, and monitoring. |
| [`ml-pipeline-workflow`](skills/ml-pipeline-workflow/SKILL.md) | Complete end-to-end MLOps pipeline orchestration from data preparation through model deployment. |
| [`model-orchestrator`](skills/model-orchestrator/SKILL.md) | Operate Traycer-led Codex orchestration with mandatory worktree, privacy, budget, capability-discovery, OpenCode worker, artifact-handoff, conflict, and independent-review gates... |
| [`molykit`](skills/molykit/SKILL.md) | \| CRITICAL: Use for MolyKit AI chat toolkit. Triggers on: BotClient, OpenAI, SSE streaming, AI chat, molykit, PlatformSend, spawn(), ThreadToken, cross-platform async, Chat wid... |
| [`n8n-mcp-tools-expert`](skills/n8n-mcp-tools-expert/SKILL.md) | Expert guide for using n8n-mcp MCP tools effectively. Use when searching for nodes, validating configurations, accessing templates, managing workflows, or using any n8n-mcp tool... |
| [`nerdzao-elite-gemini-high`](skills/nerdzao-elite-gemini-high/SKILL.md) | Modo Elite Coder + UX Pixel-Perfect otimizado especificamente para Gemini 3.1 Pro High. Workflow completo com foco em qualidade máxima e eficiência de tokens. |
| [`notebooklm`](skills/notebooklm/SKILL.md) | Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. Each question opens a fresh browser session, retrieves the answer exclusively from ... |
| [`odoo-backup-strategy`](skills/odoo-backup-strategy/SKILL.md) | Complete Odoo backup and restore strategy: database dumps, filestore backup, automated scheduling, cloud storage upload, and tested restore procedures. |
| [`odoo-ecommerce-configurator`](skills/odoo-ecommerce-configurator/SKILL.md) | Expert guide for Odoo eCommerce and Website: product catalog, payment providers, shipping methods, SEO, and order-to-fulfillment workflow. |
| [`odoo-rpc-api`](skills/odoo-rpc-api/SKILL.md) | Expert on Odoo's external JSON-RPC and XML-RPC APIs. Covers authentication, model calls, record CRUD, and real-world integration examples in Python, JavaScript, and curl. |
| [`odoo-xml-views-builder`](skills/odoo-xml-views-builder/SKILL.md) | Expert at building Odoo XML views: Form, List, Kanban, Search, Calendar, and Graph. Generates correct XML for Odoo 14-17 with proper visibility syntax. |
| [`performance-testing-review-ai-review`](skills/performance-testing-review-ai-review/SKILL.md) | You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition, and modern DevOps practices. Leverage AI tools (GitHub ... |
| [`pipecat-friday-agent`](skills/pipecat-friday-agent/SKILL.md) | Build a low-latency, Iron Man-inspired tactical voice assistant (F.R.I.D.A.Y.) using Pipecat, Gemini, and OpenAI. |
| [`podcast-generation`](skills/podcast-generation/SKILL.md) | Generate real audio narratives from text content using Azure OpenAI's Realtime API. |
| [`project-development`](skills/project-development/SKILL.md) | This skill covers the principles for identifying tasks suited to LLM processing, designing effective project architectures, and iterating rapidly using agent-assisted development. |
| [`prompt-caching`](skills/prompt-caching/SKILL.md) | You're a caching specialist who has reduced LLM costs by 90% through strategic caching. You've implemented systems that cache at multiple levels: prompt prefixes, full responses... |
| [`prompt-engineer`](skills/prompt-engineer/SKILL.md) | Transforms user prompts into optimized prompts using frameworks (RTF, RISEN, Chain of Thought, RODES, Chain of Density, RACE, RISE, STAR, SOAP, CLEAR, GROW) |
| [`prompt-engineering`](skills/prompt-engineering/SKILL.md) | Expert guide on prompt engineering patterns, best practices, and optimization techniques. Use when user wants to improve prompts, learn prompting strategies, or debug agent beha... |
| [`prompt-engineering-patterns`](skills/prompt-engineering-patterns/SKILL.md) | Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability. |
| [`prompt-library`](skills/prompt-library/SKILL.md) | A comprehensive collection of battle-tested prompts inspired by [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) and community best practices. |
| [`pydantic-ai`](skills/pydantic-ai/SKILL.md) | Build production-ready AI agents with PydanticAI — type-safe tool use, structured outputs, dependency injection, and multi-model support. |
| [`quant-analyst`](skills/quant-analyst/SKILL.md) | Build financial models, backtest trading strategies, and analyze market data. Implements risk metrics, portfolio optimization, and statistical arbitrage. |
| [`rag-engineer`](skills/rag-engineer/SKILL.md) | I bridge the gap between raw documents and LLM understanding. I know that retrieval quality determines generation quality - garbage in, garbage out. I obsess over chunking bound... |
| [`rag-implementation`](skills/rag-implementation/SKILL.md) | RAG (Retrieval-Augmented Generation) implementation workflow covering embedding selection, vector database setup, chunking strategies, and retrieval optimization. |
| [`recallmax`](skills/recallmax/SKILL.md) | FREE — God-tier long-context memory for AI agents. Injects 500K-1M clean tokens, auto-summarizes with tone/intent preservation, compresses 14-turn history into 800 tokens. |
| [`red-team-tools`](skills/red-team-tools/SKILL.md) | Implement proven methodologies and tool workflows from top security researchers for effective reconnaissance, vulnerability discovery, and bug bounty hunting. Automate common ta... |
| [`robius-widget-patterns`](skills/robius-widget-patterns/SKILL.md) | \| CRITICAL: Use for Robius widget patterns. Triggers on: apply_over, TextOrImage, modal, 可复用, 模态, collapsible, drag drop, reusable widget, widget design, pageflip, 组件设计, 组件模式 |
| [`sam-altman`](skills/sam-altman/SKILL.md) | Agente que simula Sam Altman — CEO da OpenAI, ex-presidente da Y Combinator, arquiteto da era AGI. |
| [`sankhya-dashboard-html-jsp-custom-best-pratices`](skills/sankhya-dashboard-html-jsp-custom-best-pratices/SKILL.md) | This skill should be used when the user asks for patterns, best practices, creation, or fixing of Sankhya dashboards using HTML, JSP, Java, and SQL. |
| [`seek-and-analyze-video`](skills/seek-and-analyze-video/SKILL.md) | Seek and analyze video content using Memories.ai Large Visual Memory Model for persistent video intelligence |
| [`seo-geo`](skills/seo-geo/SKILL.md) | Optimize content for AI Overviews, ChatGPT, Perplexity, and other AI search systems. Use when improving GEO, AI citations, llms.txt readiness, crawler accessibility, and passage... |
| [`shader-programming-glsl`](skills/shader-programming-glsl/SKILL.md) | Expert guide for writing efficient GLSL shaders (Vertex/Fragment) for web and game engines, covering syntax, uniforms, and common effects. |
| [`shodan-reconnaissance`](skills/shodan-reconnaissance/SKILL.md) | Provide systematic methodologies for leveraging Shodan as a reconnaissance tool during penetration testing engagements. |
| [`skill-check`](skills/skill-check/SKILL.md) | Validate Claude Code skills against the agentskills specification. Catches structural, semantic, and naming issues before users do. |
| [`skill-developer`](skills/skill-developer/SKILL.md) | Comprehensive guide for creating and managing skills in Claude Code with auto-activation system, following Anthropic's official best practices including the 500-line rule and pr... |
| [`skill-improver`](skills/skill-improver/SKILL.md) | Iteratively improve a Claude Code skill using the skill-reviewer agent until it meets quality standards. Use when improving a skill with multiple quality issues, iterating on a ... |
| [`skill-scanner`](skills/skill-scanner/SKILL.md) | Scan agent skills for security issues before adoption. Detects prompt injection, malicious code, excessive permissions, secret exposure, and supply chain risks. |
| [`skill-seekers`](skills/skill-seekers/SKILL.md) | -Automatically convert documentation websites, GitHub repositories, and PDFs into Claude AI skills in minutes. |
| [`spline-3d-integration`](skills/spline-3d-integration/SKILL.md) | Use when adding interactive 3D scenes from Spline.design to web projects, including React embedding and runtime control API. |
| [`stability-ai`](skills/stability-ai/SKILL.md) | Geracao de imagens via Stability AI (SD3.5, Ultra, Core). Text-to-image, img2img, inpainting, upscale, remove-bg, search-replace. 15 estilos artisticos. |
| [`stitch-ui-design`](skills/stitch-ui-design/SKILL.md) | Expert guidance for crafting effective prompts in Google Stitch, the AI-powered UI design tool by Google Labs. This skill helps create precise, actionable prompts that generate ... |
| [`supabase-automation`](skills/supabase-automation/SKILL.md) | Automate Supabase database queries, table management, project administration, storage, edge functions, and SQL execution via Rube MCP (Composio). Always search tools first for c... |
| [`superpowers-lab`](skills/superpowers-lab/SKILL.md) | Lab environment for Claude superpowers |
| [`threejs-shaders`](skills/threejs-shaders/SKILL.md) | Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing fragment shaders, or extending built-in m... |
| [`transformers-js`](skills/transformers-js/SKILL.md) | Run Hugging Face models in JavaScript or TypeScript with Transformers.js in Node.js or the browser. |
| [`unit-testing-test-generate`](skills/unit-testing-test-generate/SKILL.md) | Generate comprehensive, maintainable unit tests across languages with strong coverage and edge case focus. |
| [`using-neon`](skills/using-neon/SKILL.md) | Neon is a serverless Postgres platform that separates compute and storage to offer autoscaling, branching, instant restore, and scale-to-zero. It's fully compatible with Postgre... |
| [`using-superpowers`](skills/using-superpowers/SKILL.md) | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |
| [`varlock`](skills/varlock/SKILL.md) | Secure-by-default environment variable management for Claude Code sessions. |
| [`varlock-claude-skill`](skills/varlock-claude-skill/SKILL.md) | Secure environment variable management ensuring secrets are never exposed in Claude sessions, terminals, logs, or git commits |
| [`vector-database-engineer`](skills/vector-database-engineer/SKILL.md) | Expert in vector databases, embedding strategies, and semantic search implementation. Masters Pinecone, Weaviate, Qdrant, Milvus, and pgvector for RAG applications, recommendati... |
| [`vexor`](skills/vexor/SKILL.md) | Vector-powered CLI for semantic file search with a Claude/Codex skill |
| [`vibe-code-auditor`](skills/vibe-code-auditor/SKILL.md) | Audit rapidly generated or AI-produced code for structural flaws, fragility, and production risks. |
| [`videodb`](skills/videodb/SKILL.md) | Video and audio perception, indexing, and editing. Ingest files/URLs/live streams, build visual/spoken indexes, search with timestamps, edit timelines, add overlays/subtitles, g... |
| [`videodb-skills`](skills/videodb-skills/SKILL.md) | Upload, stream, search, edit, transcribe, and generate AI video and audio using the VideoDB SDK. |
| [`voice-agents`](skills/voice-agents/SKILL.md) | You are a voice AI architect who has shipped production voice agents handling millions of calls. You understand the physics of latency - every component adds milliseconds, and t... |
| [`voice-ai-development`](skills/voice-ai-development/SKILL.md) | You are an expert in building real-time voice applications. You think in terms of latency budgets, audio quality, and user experience. You know that voice apps feel magical when... |
| [`voice-ai-engine-development`](skills/voice-ai-engine-development/SKILL.md) | Build real-time conversational AI voice engines using async worker pipelines, streaming transcription, LLM agents, and TTS synthesis with interrupt handling and multi-provider s... |
| [`web-artifacts-builder`](skills/web-artifacts-builder/SKILL.md) | To build powerful frontend claude.ai artifacts, follow these steps: |
| [`xss-html-injection`](skills/xss-html-injection/SKILL.md) | Execute comprehensive client-side injection vulnerability assessments on web applications to identify XSS and HTML injection flaws, demonstrate exploitation techniques for sessi... |
| [`xvary-stock-research`](skills/xvary-stock-research/SKILL.md) | Thesis-driven equity analysis from public SEC EDGAR and market data; /analyze, /score, /compare workflows with bundled Python tools (Claude Code, Cursor, Codex). |
| [`yann-lecun`](skills/yann-lecun/SKILL.md) | Agente que simula Yann LeCun — inventor das Convolutional Neural Networks, Chief AI Scientist da Meta, Prêmio Turing 2018. |
| [`yann-lecun-debate`](skills/yann-lecun-debate/SKILL.md) | Sub-skill de debates e posições de Yann LeCun. Cobre críticas técnicas detalhadas aos LLMs, rivalidades intelectuais (LeCun vs Hinton, Sutskever, Russell, Yudkowsky, Bostrom), l... |
| [`yann-lecun-filosofia`](skills/yann-lecun-filosofia/SKILL.md) | Sub-skill filosófica e pedagógica de Yann LeCun. |
| [`yann-lecun-tecnico`](skills/yann-lecun-tecnico/SKILL.md) | Sub-skill técnica de Yann LeCun. Cobre CNNs, LeNet, backpropagation, JEPA (I-JEPA, V-JEPA, MC-JEPA), AMI (Advanced Machinery of Intelligence), Self-Supervised Learning (SimCLR, ... |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="architecture"></a>
### 🏗️ Arquitetura de Software & Metodologias de Engenharia
*Padrões arquiteturais C4, Domain-Driven Design (DDD), refatoração estrutural, Clean Code, auditorias técnicas e ADRs.* (117 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`angular-best-practices`](skills/angular-best-practices/SKILL.md) | Angular performance optimization and best practices guide. Use when writing, reviewing, or refactoring Angular code for optimal performance, bundle size, and rendering efficiency. |
| [`architect-review`](skills/architect-review/SKILL.md) | Master software architect specializing in modern architecture |
| [`architecture`](skills/architecture/SKILL.md) | Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design. |
| [`architecture-decision-records`](skills/architecture-decision-records/SKILL.md) | Comprehensive patterns for creating, maintaining, and managing Architecture Decision Records (ADRs) that capture the context and rationale behind significant technical decisions. |
| [`architecture-patterns`](skills/architecture-patterns/SKILL.md) | Master proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design to build maintainable, testable, and scalable systems. |
| [`astro`](skills/astro/SKILL.md) | Build content-focused websites with Astro — zero JS by default, islands architecture, multi-framework components, and Markdown/MDX support. |
| [`audit-context-building`](skills/audit-context-building/SKILL.md) | Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding. |
| [`aws-skills`](skills/aws-skills/SKILL.md) | AWS development with infrastructure automation and cloud architecture patterns |
| [`azure-eventgrid-dotnet`](skills/azure-eventgrid-dotnet/SKILL.md) | Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use for event-driven architectures, pub/sub messaging, CloudEvents, and ... |
| [`azure-eventgrid-py`](skills/azure-eventgrid-py/SKILL.md) | Azure Event Grid SDK for Python. Use for publishing events, handling CloudEvents, and event-driven architectures. |
| [`azure-eventhub-java`](skills/azure-eventhub-java/SKILL.md) | Build real-time streaming applications with Azure Event Hubs SDK for Java. Use when implementing event streaming, high-throughput data ingestion, or building event-driven archit... |
| [`backend-architect`](skills/backend-architect/SKILL.md) | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. |
| [`backend-dev-guidelines`](skills/backend-dev-guidelines/SKILL.md) | You are a senior backend engineer operating production-grade services under strict architectural and reliability constraints. Use when routes, controllers, services, repositorie... |
| [`bdi-mental-states`](skills/bdi-mental-states/SKILL.md) | This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create belief-desire-intention models", "transform RDF to beliefs", "... |
| [`brainstorming`](skills/brainstorming/SKILL.md) | Use before creative or constructive work (features, architecture, behavior). Transforms vague ideas into validated designs through disciplined reasoning and collaboration. |
| [`c4-architecture-c4-architecture`](skills/c4-architecture-c4-architecture/SKILL.md) | Generate comprehensive C4 architecture documentation for an existing repository/codebase using a bottom-up analysis approach. |
| [`c4-code`](skills/c4-code/SKILL.md) | Expert C4 Code-level documentation specialist. Analyzes code directories to create comprehensive C4 code-level documentation including function signatures, arguments, dependenci... |
| [`c4-component`](skills/c4-component/SKILL.md) | Expert C4 Component-level documentation specialist. Synthesizes C4 Code-level documentation into Component-level architecture, defining component boundaries, interfaces, and rel... |
| [`c4-container`](skills/c4-container/SKILL.md) | Expert C4 Container-level documentation specialist. |
| [`c4-context`](skills/c4-context/SKILL.md) | Expert C4 Context-level documentation specialist. Creates high-level system context diagrams, documents personas, user journeys, system features, and external dependencies. |
| [`cc-skill-backend-patterns`](skills/cc-skill-backend-patterns/SKILL.md) | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. |
| [`clean-code`](skills/clean-code/SKILL.md) | This skill embodies the principles of \"Clean Code\" by Robert C. Martin (Uncle Bob). Use it to transform \"code that works\" into \"code that is clean.\ |
| [`cloud-architect`](skills/cloud-architect/SKILL.md) | Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural... |
| [`code-documentation-doc-generate`](skills/code-documentation-doc-generate/SKILL.md) | You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical... |
| [`code-refactoring-context-restore`](skills/code-refactoring-context-restore/SKILL.md) | Use when working with code refactoring context restore |
| [`code-refactoring-refactor-clean`](skills/code-refactoring-refactor-clean/SKILL.md) | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. Analyze and refactor the provided... |
| [`code-refactoring-tech-debt`](skills/code-refactoring-tech-debt/SKILL.md) | You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. Analyze the codebase to uncover debt, assess its ... |
| [`code-review-checklist`](skills/code-review-checklist/SKILL.md) | Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability |
| [`code-review-excellence`](skills/code-review-excellence/SKILL.md) | Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement. |
| [`code-reviewer`](skills/code-reviewer/SKILL.md) | Elite code review expert specializing in modern AI-powered code |
| [`codebase-audit-pre-push`](skills/codebase-audit-pre-push/SKILL.md) | Deep audit before GitHub push: removes junk files, dead code, security holes, and optimization issues. Checks every file line-by-line for production readiness. |
| [`codebase-cleanup-refactor-clean`](skills/codebase-cleanup-refactor-clean/SKILL.md) | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. Analyze and refactor the provided... |
| [`codebase-cleanup-tech-debt`](skills/codebase-cleanup-tech-debt/SKILL.md) | You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. Analyze the codebase to uncover debt, assess its ... |
| [`codex-review`](skills/codex-review/SKILL.md) | Professional code review with auto CHANGELOG generation, integrated with Codex AI. Use when you want professional code review before commits, you need automatic CHANGELOG genera... |
| [`computer-use-agents`](skills/computer-use-agents/SKILL.md) | The fundamental architecture of computer use agents: observe screen, reason about next action, execute action, repeat. This loop integrates vision models with action execution t... |
| [`cqrs-implementation`](skills/cqrs-implementation/SKILL.md) | Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing query performance, or building event-sourced... |
| [`data-engineer`](skills/data-engineer/SKILL.md) | Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. Implements Apache Spark, dbt, Airflow, and cloud-native data platforms. |
| [`data-engineering-data-pipeline`](skills/data-engineering-data-pipeline/SKILL.md) | You are a data pipeline architecture expert specializing in scalable, reliable, and cost-effective data pipelines for batch and streaming data processing. |
| [`database-architect`](skills/database-architect/SKILL.md) | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database architectures. |
| [`database-cloud-optimization-cost-optimize`](skills/database-cloud-optimization-cost-optimize/SKILL.md) | You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability. Analyze cloud spending, identify savings... |
| [`database-optimizer`](skills/database-optimizer/SKILL.md) | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. |
| [`ddd-context-mapping`](skills/ddd-context-mapping/SKILL.md) | Map relationships between bounded contexts and define integration contracts using DDD context mapping patterns. |
| [`ddd-strategic-design`](skills/ddd-strategic-design/SKILL.md) | Design DDD strategic artifacts including subdomains, bounded contexts, and ubiquitous language for complex business domains. |
| [`ddd-tactical-patterns`](skills/ddd-tactical-patterns/SKILL.md) | Apply DDD tactical patterns in code using entities, value objects, aggregates, repositories, and domain events with explicit invariants. |
| [`deployment-pipeline-design`](skills/deployment-pipeline-design/SKILL.md) | Architecture patterns for multi-stage CI/CD pipelines with approval gates and deployment strategies. |
| [`discord-bot-architect`](skills/discord-bot-architect/SKILL.md) | Specialized skill for building production-ready Discord bots. Covers Discord.js (JavaScript) and Pycord (Python), gateway intents, slash commands, interactive components, rate l... |
| [`django-pro`](skills/django-pro/SKILL.md) | Master Django 5.x with async views, DRF, Celery, and Django Channels. Build scalable web applications with proper architecture, testing, and deployment. |
| [`docs-architect`](skills/docs-architect/SKILL.md) | Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details to produce long-form technical manuals ... |
| [`documentation`](skills/documentation/SKILL.md) | Documentation generation workflow covering API docs, architecture docs, README files, code comments, and technical writing. |
| [`documentation-generation-doc-generate`](skills/documentation-generation-doc-generate/SKILL.md) | You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical... |
| [`domain-driven-design`](skills/domain-driven-design/SKILL.md) | Plan and route Domain-Driven Design work from strategic modeling to tactical implementation and evented architecture patterns. |
| [`dotnet-architect`](skills/dotnet-architect/SKILL.md) | Expert .NET backend architect specializing in C#, ASP.NET Core, Entity Framework, Dapper, and enterprise application patterns. |
| [`electron-development`](skills/electron-development/SKILL.md) | Master Electron desktop app development with secure IPC, contextIsolation, preload scripts, multi-process architecture, electron-builder packaging, code signing, and auto-update. |
| [`event-sourcing-architect`](skills/event-sourcing-architect/SKILL.md) | Expert in event sourcing, CQRS, and event-driven architecture patterns. Masters event store design, projection building, saga orchestration, and eventual consistency patterns. U... |
| [`fp-refactor`](skills/fp-refactor/SKILL.md) | Comprehensive guide for refactoring imperative TypeScript code to fp-ts functional patterns |
| [`frontend-dev-guidelines`](skills/frontend-dev-guidelines/SKILL.md) | You are a senior frontend engineer operating under strict architectural and performance standards. Use when creating components or pages, adding new features, or fetching or mut... |
| [`frontend-developer`](skills/frontend-developer/SKILL.md) | Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern frontend architecture. |
| [`frontend-mobile-development-component-scaffold`](skills/frontend-mobile-development-component-scaffold/SKILL.md) | You are a React component architecture expert specializing in scaffolding production-ready, accessible, and performant components. Generate complete component implementations wi... |
| [`git-pr-workflows-onboard`](skills/git-pr-workflows-onboard/SKILL.md) | You are an **expert onboarding specialist and knowledge transfer architect** with deep experience in remote-first organizations, technical team integration, and accelerated lear... |
| [`graphql-architect`](skills/graphql-architect/SKILL.md) | Master modern GraphQL with federation, performance optimization, and enterprise security. Build scalable schemas, implement advanced caching, and design real-time systems. |
| [`gsd-code-review`](skills/gsd-code-review/SKILL.md) | Review source files changed during a phase for bugs, security issues, and code quality problems |
| [`hybrid-cloud-architect`](skills/hybrid-cloud-architect/SKILL.md) | Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware). |
| [`javascript-typescript-typescript-scaffold`](skills/javascript-typescript-typescript-scaffold/SKILL.md) | You are a TypeScript project architecture expert specializing in scaffolding production-ready Node.js and frontend applications. Generate complete project structures with modern... |
| [`kubernetes-architect`](skills/kubernetes-architect/SKILL.md) | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration. |
| [`laravel-expert`](skills/laravel-expert/SKILL.md) | Senior Laravel Engineer role for production-grade, maintainable, and idiomatic Laravel solutions. Focuses on clean architecture, security, performance, and modern standards (Lar... |
| [`legacy-modernizer`](skills/legacy-modernizer/SKILL.md) | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and backward compatibility. |
| [`lightning-architecture-review`](skills/lightning-architecture-review/SKILL.md) | Review Bitcoin Lightning Network protocol designs, compare channel factory approaches, and analyze Layer 2 scaling tradeoffs. Covers trust models, on-chain footprint, consensus ... |
| [`lightning-channel-factories`](skills/lightning-channel-factories/SKILL.md) | Technical reference on Lightning Network channel factories, multi-party channels, LSP architectures, and Bitcoin Layer 2 scaling without soft forks. Covers Decker-Wattenhofer, t... |
| [`memory-systems`](skills/memory-systems/SKILL.md) | Design short-term, long-term, and graph-based memory architectures. Use when building agents that must persist across sessions, needing to maintain entity consistency across con... |
| [`mermaid-expert`](skills/mermaid-expert/SKILL.md) | Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. Masters syntax for all diagram types and styling. |
| [`microservices-patterns`](skills/microservices-patterns/SKILL.md) | Master microservices architecture patterns including service boundaries, inter-service communication, data management, and resilience patterns for building distributed systems. |
| [`mobile-developer`](skills/mobile-developer/SKILL.md) | Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integrations, offline sync, and app store opti... |
| [`monorepo-architect`](skills/monorepo-architect/SKILL.md) | Expert in monorepo architecture, build systems, and dependency management at scale. Masters Nx, Turborepo, Bazel, and Lerna for efficient multi-project development. Use PROACTIV... |
| [`multi-agent-patterns`](skills/multi-agent-patterns/SKILL.md) | This skill should be used when the user asks to "design multi-agent system", "implement supervisor pattern", "create swarm architecture", "coordinate multiple agents", or mentio... |
| [`multi-cloud-architecture`](skills/multi-cloud-architecture/SKILL.md) | Decision framework and patterns for architecting applications across AWS, Azure, and GCP. |
| [`multi-platform-apps-multi-platform`](skills/multi-platform-apps-multi-platform/SKILL.md) | Build and deploy the same feature consistently across web, mobile, and desktop platforms using API-first architecture and parallel implementation strategies. |
| [`n8n-workflow-patterns`](skills/n8n-workflow-patterns/SKILL.md) | Proven architectural patterns for building n8n workflows. |
| [`nerdzao-elite`](skills/nerdzao-elite/SKILL.md) | Senior Elite Software Engineer (15+) and Senior Product Designer. Full workflow with planning, architecture, TDD, clean code, and pixel-perfect UX validation. |
| [`nestjs-expert`](skills/nestjs-expert/SKILL.md) | You are an expert in Nest.js with deep knowledge of enterprise-grade Node.js application architecture, dependency injection patterns, decorators, middleware, guards, interceptor... |
| [`network-engineer`](skills/network-engineer/SKILL.md) | Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. |
| [`nextjs-app-router-patterns`](skills/nextjs-app-router-patterns/SKILL.md) | Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development. |
| [`nodejs-backend-patterns`](skills/nodejs-backend-patterns/SKILL.md) | Comprehensive guidance for building scalable, maintainable, and production-ready Node.js backend applications with modern frameworks, architectural patterns, and best practices. |
| [`nodejs-best-practices`](skills/nodejs-best-practices/SKILL.md) | Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying. |
| [`plan-writing`](skills/plan-writing/SKILL.md) | Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-step work. |
| [`production-code-audit`](skills/production-code-audit/SKILL.md) | Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically transform it to production-grade, corporate-level professional qua... |
| [`python-development-python-scaffold`](skills/python-development-python-scaffold/SKILL.md) | You are a Python project architecture expert specializing in scaffolding production-ready Python applications. Generate complete project structures with modern tooling (uv, Fast... |
| [`react-flow-architect`](skills/react-flow-architect/SKILL.md) | Build production-ready ReactFlow applications with hierarchical navigation, performance optimization, and advanced state management. |
| [`react-native-architecture`](skills/react-native-architecture/SKILL.md) | Production-ready patterns for React Native development with Expo, including navigation, state management, native modules, and offline-first architecture. |
| [`receiving-code-review`](skills/receiving-code-review/SKILL.md) | Code review requires technical evaluation, not emotional performance. |
| [`requesting-code-review`](skills/requesting-code-review/SKILL.md) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| [`robius-app-architecture`](skills/robius-app-architecture/SKILL.md) | \| CRITICAL: Use for Robius app architecture patterns. Triggers on: Tokio, async, submit_async_request, 异步, 架构, SignalToUI, Cx::post_action, worker task, app structure, MatchEve... |
| [`saas-multi-tenant`](skills/saas-multi-tenant/SKILL.md) | Design and implement multi-tenant SaaS architectures with row-level security, tenant-scoped queries, shared-schema isolation, and safe cross-tenant admin patterns in PostgreSQL ... |
| [`saas-mvp-launcher`](skills/saas-mvp-launcher/SKILL.md) | Use when planning or building a SaaS MVP from scratch. Provides a structured roadmap covering tech stack, architecture, auth, payments, and launch checklist. |
| [`salesforce-development`](skills/salesforce-development/SKILL.md) | Use @wire decorator for reactive data binding with Lightning Data Service or Apex methods. @wire fits LWC's reactive architecture and enables Salesforce performance optimizations. |
| [`scala-pro`](skills/scala-pro/SKILL.md) | Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. Expert in Apache Pekko, Akka, Spark, ZIO/Cats Effect, and re... |
| [`senior-architect`](skills/senior-architect/SKILL.md) | Complete toolkit for senior architect with modern tools and best practices. |
| [`seo-plan`](skills/seo-plan/SKILL.md) | > Strategic SEO planning for new or existing websites. Industry-specific templates, competitive analysis, content strategy, and implementation roadmap. Use when user says "SEO p... |
| [`seo-structure-architect`](skills/seo-structure-architect/SKILL.md) | Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. Creates search-friendly content organization. |
| [`service-mesh-expert`](skills/service-mesh-expert/SKILL.md) | Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, observability integration, and... |
| [`simplify-code`](skills/simplify-code/SKILL.md) | Review a diff for clarity and safe simplifications, then optionally apply low-risk fixes. |
| [`site-architecture`](skills/site-architecture/SKILL.md) | Plan or restructure website hierarchy, navigation, URL patterns, breadcrumbs, and internal linking. Use when mapping pages, sections, and site structure, but not for XML sitemap... |
| [`social-proof-architect`](skills/social-proof-architect/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`software-architecture`](skills/software-architecture/SKILL.md) | Guide for quality focused software architecture. This skill should be used when users want to write code, design architecture, analyze code, in any case that relates to software... |
| [`swiftui-expert-skill`](skills/swiftui-expert-skill/SKILL.md) | Write, review, or improve SwiftUI code following best practices for state management, view composition, performance, and iOS 26+ Liquid Glass adoption. Use when building new Swi... |
| [`systems-programming-rust-project`](skills/systems-programming-rust-project/SKILL.md) | You are a Rust project architecture expert specializing in scaffolding production-ready Rust applications. Generate complete project structures with cargo tooling, proper module... |
| [`tailwind-patterns`](skills/tailwind-patterns/SKILL.md) | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. |
| [`threat-modeling-expert`](skills/threat-modeling-expert/SKILL.md) | Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extraction. Use PROACTI... |
| [`tool-design`](skills/tool-design/SKILL.md) | Build tools that agents can use effectively, including architectural reduction patterns. Use when creating new tools for agent systems, debugging tool-related failures or misuse... |
| [`uncle-bob-craft`](skills/uncle-bob-craft/SKILL.md) | Use when performing code review, writing or refactoring code, or discussing architecture; complements clean-code and does not replace project linter/formatter. |
| [`vibers-code-review`](skills/vibers-code-review/SKILL.md) | Human review workflow for AI-generated GitHub projects with spec-based feedback, security review, and follow-up PRs from the Vibers service. |
| [`wiki-architect`](skills/wiki-architect/SKILL.md) | You are a documentation architect that produces structured wiki catalogues and onboarding guides from codebases. |
| [`wiki-researcher`](skills/wiki-researcher/SKILL.md) | You are an expert software engineer and systems analyst. Use when user asks \"how does X work\" with expectation of depth, user wants to understand a complex system spanning man... |
| [`wordpress-plugin-development`](skills/wordpress-plugin-development/SKILL.md) | WordPress plugin development workflow covering plugin architecture, hooks, admin interfaces, REST API, security best practices, and WordPress 7.0 features: Real-Time Collaborati... |
| [`wordpress-theme-development`](skills/wordpress-theme-development/SKILL.md) | WordPress theme development workflow covering theme architecture, template hierarchy, custom post types, block editor support, responsive design, and WordPress 7.0 features: Dat... |
| [`workflow-automation`](skills/workflow-automation/SKILL.md) | You are a workflow automation architect who has seen both the promise and the pain of these platforms. You've migrated teams from brittle cron jobs to durable execution and watc... |
| [`workflow-orchestration-patterns`](skills/workflow-orchestration-patterns/SKILL.md) | Master workflow orchestration architecture with Temporal, covering fundamental design decisions, resilience patterns, and best practices for building reliable distributed systems. |
| [`zapier-make-patterns`](skills/zapier-make-patterns/SKILL.md) | You are a no-code automation architect who has built thousands of Zaps and Scenarios for businesses of all sizes. You've seen automations that save companies 40% of their time, ... |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="design_ui"></a>
### 🎨 UI / UX Pro Max, Design Systems & Animações
*Sistemas de design de classe mundial, UI/UX Pro Max, diretrizes Apple HIG, animações fluidas, Tailwind CSS, Shadcn e Figma.* (122 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`3d-web-experience`](skills/3d-web-experience/SKILL.md) | You bring the third dimension to the web. You know when 3D enhances and when it's just showing off. You balance visual impact with performance. You make 3D accessible to users w... |
| [`accessibility-compliance-accessibility-audit`](skills/accessibility-compliance-accessibility-audit/SKILL.md) | You are an accessibility expert specializing in WCAG compliance, inclusive design, and assistive technology compatibility. Conduct audits, identify barriers, and provide remedia... |
| [`analytics-tracking`](skills/analytics-tracking/SKILL.md) | Design, audit, and improve analytics tracking systems that produce reliable, decision-ready data. |
| [`android-jetpack-compose-expert`](skills/android-jetpack-compose-expert/SKILL.md) | Expert guidance for building modern Android UIs with Jetpack Compose, covering state management, navigation, performance, and Material Design 3. |
| [`angular-ui-patterns`](skills/angular-ui-patterns/SKILL.md) | Modern Angular UI patterns for loading states, error handling, and data display. Use when building UI components, handling async data, or managing component states. |
| [`animejs-animation`](skills/animejs-animation/SKILL.md) | Advanced JavaScript animation library skill for creating complex, high-performance web animations. |
| [`antigravity-design-expert`](skills/antigravity-design-expert/SKILL.md) | Core UI/UX engineering skill for building highly interactive, spatial, weightless, and glassmorphism-based web interfaces using GSAP and 3D CSS. |
| [`api-design-principles`](skills/api-design-principles/SKILL.md) | Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers and stand the test of time. |
| [`api-patterns`](skills/api-patterns/SKILL.md) | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. |
| [`api-security-best-practices`](skills/api-security-best-practices/SKILL.md) | Implement secure API design patterns including authentication, authorization, input validation, rate limiting, and protection against common API vulnerabilities |
| [`api-testing-observability-api-mock`](skills/api-testing-observability-api-mock/SKILL.md) | You are an API mocking expert specializing in realistic mock services for development, testing, and demos. Design mocks that simulate real API behavior and enable parallel devel... |
| [`baseline-ui`](skills/baseline-ui/SKILL.md) | Validates animation durations, enforces typography scale, checks component accessibility, and prevents layout anti-patterns in Tailwind CSS projects. Use when building UI compon... |
| [`bigquery-sql`](skills/bigquery-sql/SKILL.md) | Provides BigQuery SQL query optimization techniques, execution best practices, and performance tuning rules for high-efficiency querying. Use when optimizing BigQuery SQL querie... |
| [`building-native-ui`](skills/building-native-ui/SKILL.md) | Complete guide for building beautiful apps with Expo Router. Covers fundamentals, styling, components, navigation, animations, patterns, and native tabs. |
| [`canva-automation`](skills/canva-automation/SKILL.md) | Automate Canva tasks via Rube MCP (Composio): designs, exports, folders, brand templates, autofill. Always search tools first for current schemas. |
| [`canvas-design`](skills/canvas-design/SKILL.md) | These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY. Output only .md files, .pdf files, and .png files. |
| [`cdk-patterns`](skills/cdk-patterns/SKILL.md) | Common AWS CDK patterns and constructs for building cloud infrastructure with TypeScript, Python, or Java. Use when designing reusable CDK stacks and L3 constructs. |
| [`cicd-automation-workflow-automate`](skills/cicd-automation-workflow-automate/SKILL.md) | You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes. Design and implement auto... |
| [`cirq`](skills/cirq/SKILL.md) | Cirq is Google Quantum AI's open-source framework for designing, simulating, and running quantum circuits on quantum computers and simulators. |
| [`context-degradation`](skills/context-degradation/SKILL.md) | Language models exhibit predictable degradation patterns as context length increases. Understanding these patterns is essential for diagnosing failures and designing resilient s... |
| [`core-components`](skills/core-components/SKILL.md) | Core component library and design system patterns. Use when building UI, using design tokens, or working with the component library. |
| [`database`](skills/database/SKILL.md) | Database development and operations workflow covering SQL, NoSQL, database design, migrations, optimization, and data engineering. |
| [`database-design`](skills/database-design/SKILL.md) | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. |
| [`design-md`](skills/design-md/SKILL.md) | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files |
| [`design-orchestration`](skills/design-orchestration/SKILL.md) | Orchestrates design workflows by routing work through brainstorming, multi-agent review, and execution readiness in the correct order. |
| [`design-spells`](skills/design-spells/SKILL.md) | Curated micro-interactions and design details that add "magic" and personality to websites and apps. |
| [`drizzle-orm-expert`](skills/drizzle-orm-expert/SKILL.md) | Expert in Drizzle ORM for TypeScript — schema design, relational queries, migrations, and serverless database integration. Use when building type-safe database layers with Drizzle. |
| [`emotional-arc-designer`](skills/emotional-arc-designer/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`event-store-design`](skills/event-store-design/SKILL.md) | Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store technologies, or implementing event persistenc... |
| [`expo-tailwind-setup`](skills/expo-tailwind-setup/SKILL.md) | Set up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling |
| [`expo-ui-jetpack-compose`](skills/expo-ui-jetpack-compose/SKILL.md) | expo-ui-jetpack-compose |
| [`expo-ui-swift-ui`](skills/expo-ui-swift-ui/SKILL.md) | expo-ui-swift-ui |
| [`favicon`](skills/favicon/SKILL.md) | Generate favicons from a source image |
| [`figma-automation`](skills/figma-automation/SKILL.md) | Automate Figma tasks via Rube MCP (Composio): files, components, design tokens, comments, exports. Always search tools first for current schemas. |
| [`fixing-metadata`](skills/fixing-metadata/SKILL.md) | Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, JSON-LD structured data, and robots directives. U... |
| [`fixing-motion-performance`](skills/fixing-motion-performance/SKILL.md) | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. Use when animations stutter, transitions ja... |
| [`frontend-design`](skills/frontend-design/SKILL.md) | You are a frontend designer-engineer, not a layout generator. |
| [`frontend-slides`](skills/frontend-slides/SKILL.md) | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. |
| [`frontend-ui-dark-ts`](skills/frontend-ui-dark-ts/SKILL.md) | A modern dark-themed React UI system using Tailwind CSS and Framer Motion. Designed for dashboards, admin panels, and data-rich applications with glassmorphism effects and taste... |
| [`grpc-golang`](skills/grpc-golang/SKILL.md) | Build production-ready gRPC services in Go with mTLS, streaming, and observability. Use when designing Protobuf contracts with Buf or implementing secure service-to-service tran... |
| [`gsd-ai-integration-phase`](skills/gsd-ai-integration-phase/SKILL.md) | Generate an AI-SPEC.md design contract for phases that involve building AI systems. |
| [`gsd-sketch`](skills/gsd-sketch/SKILL.md) | Sketch UI/design ideas with throwaway HTML mockups, or propose what to sketch next (frontier mode) |
| [`gsd-ui-phase`](skills/gsd-ui-phase/SKILL.md) | Generate UI design contract (UI-SPEC.md) for frontend phases |
| [`gsd-ui-review`](skills/gsd-ui-review/SKILL.md) | Retroactive 6-pillar visual audit of implemented frontend code |
| [`hig-components-content`](skills/hig-components-content/SKILL.md) | Apple Human Interface Guidelines for content display components. |
| [`hig-components-dialogs`](skills/hig-components-dialogs/SKILL.md) | Apple HIG guidance for presentation components including alerts, action sheets, popovers, sheets, and digit entry views. |
| [`hig-components-layout`](skills/hig-components-layout/SKILL.md) | Apple Human Interface Guidelines for layout and navigation components. |
| [`hig-components-search`](skills/hig-components-search/SKILL.md) | Apple HIG guidance for navigation-related components including search fields, page controls, and path controls. |
| [`hig-components-status`](skills/hig-components-status/SKILL.md) | Apple HIG guidance for status and progress UI components including progress indicators, status bars, and activity rings. |
| [`hig-components-system`](skills/hig-components-system/SKILL.md) | Apple HIG guidance for system experience components: widgets, live activities, notifications, complications, home screen quick actions, top shelf, watch faces, app clips, and ap... |
| [`hig-foundations`](skills/hig-foundations/SKILL.md) | Apple Human Interface Guidelines design foundations. |
| [`hig-patterns`](skills/hig-patterns/SKILL.md) | Apple Human Interface Guidelines interaction and UX patterns. |
| [`hig-platforms`](skills/hig-platforms/SKILL.md) | Apple Human Interface Guidelines for platform-specific design. |
| [`hig-project-context`](skills/hig-project-context/SKILL.md) | Create or update a shared Apple design context document that other HIG skills use to tailor guidance. |
| [`iconsax-library`](skills/iconsax-library/SKILL.md) | Extensive icon library and AI-driven icon generation skill for premium UI/UX design. |
| [`json-canvas`](skills/json-canvas/SKILL.md) | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files, creating visual canvases, mind maps, flowcharts, or ... |
| [`k8s-manifest-generator`](skills/k8s-manifest-generator/SKILL.md) | Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims. |
| [`kpi-dashboard-design`](skills/kpi-dashboard-design/SKILL.md) | Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions. |
| [`landing-page-generator`](skills/landing-page-generator/SKILL.md) | Generates high-converting Next.js/React landing pages with Tailwind CSS. Uses PAS, AIDA, and BAB frameworks for optimized copy/components (Heroes, Features, Pricing). Focuses on... |
| [`lead-magnets`](skills/lead-magnets/SKILL.md) | Plan and optimize lead magnets for email capture and lead generation. Use when designing gated content, checklists, templates, downloadable resources, or other offers that conve... |
| [`loss-aversion-designer`](skills/loss-aversion-designer/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`magic-animator`](skills/magic-animator/SKILL.md) | AI-powered animation tool for creating motion in logos, UI, icons, and social media assets. |
| [`magic-ui-generator`](skills/magic-ui-generator/SKILL.md) | Utilizes Magic by 21st.dev to generate, compare, and integrate multiple production-ready UI component variations. |
| [`makepad-animation`](skills/makepad-animation/SKILL.md) | \| CRITICAL: Use for Makepad animation system. Triggers on: makepad animation, makepad animator, makepad hover, makepad state, makepad transition, "from: { all: Forward", makepa... |
| [`makepad-basics`](skills/makepad-basics/SKILL.md) | \| CRITICAL: Use for Makepad getting started and app structure. Triggers on: makepad, makepad getting started, makepad tutorial, live_design!, app_main!, makepad project setup, ... |
| [`makepad-dsl`](skills/makepad-dsl/SKILL.md) | \| CRITICAL: Use for Makepad DSL syntax and inheritance. Triggers on: makepad dsl, live_design, makepad inheritance, makepad prototype, "<Widget>", "Foo = { }", makepad object, ... |
| [`makepad-font`](skills/makepad-font/SKILL.md) | \| CRITICAL: Use for Makepad font and text rendering. Triggers on: makepad font, makepad text, makepad glyph, makepad typography, font atlas, text layout, font family, font size... |
| [`mobile-design`](skills/mobile-design/SKILL.md) | (Mobile-First · Touch-First · Platform-Respectful) |
| [`multi-agent-brainstorming`](skills/multi-agent-brainstorming/SKILL.md) | Simulate a structured peer-review process using multiple specialized agents to validate designs, surface hidden assumptions, and identify failure modes before implementation. |
| [`nosql-expert`](skills/nosql-expert/SKILL.md) | Expert guidance for distributed NoSQL databases (Cassandra, DynamoDB). Focuses on mental models, query-first modeling, single-table design, and avoiding hot partitions in high-s... |
| [`observability-monitoring-slo-implement`](skills/observability-monitoring-slo-implement/SKILL.md) | You are an SLO (Service Level Objective) expert specializing in implementing reliability standards and error budget-based engineering practices. Design comprehensive SLO framewo... |
| [`openapi-spec-generation`](skills/openapi-spec-generation/SKILL.md) | Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. Use when creating API documentation, generating SDKs, or ensuring API co... |
| [`pakistan-payments-stack`](skills/pakistan-payments-stack/SKILL.md) | Design and implement production-grade Pakistani payment integrations (JazzCash, Easypaisa, bank/PSP rails, optional Raast) for SaaS with PKR billing, webhook reliability, and re... |
| [`postgres-best-practices`](skills/postgres-best-practices/SKILL.md) | Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configura... |
| [`postgresql`](skills/postgresql/SKILL.md) | Design a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performance patterns, and advanced features |
| [`pricing-strategy`](skills/pricing-strategy/SKILL.md) | Design pricing, packaging, and monetization strategies based on value, customer willingness to pay, and growth objectives. |
| [`prisma-expert`](skills/prisma-expert/SKILL.md) | You are an expert in Prisma ORM with deep knowledge of schema design, migrations, query optimization, relations modeling, and database operations across PostgreSQL, MySQL, and S... |
| [`privacy-by-design`](skills/privacy-by-design/SKILL.md) | Use when building apps that collect user data. Ensures privacy protections are built in from the start—data minimization, consent, encryption. |
| [`product-design`](skills/product-design/SKILL.md) | Design de produto nivel Apple — sistemas visuais, UX flows, acessibilidade, linguagem visual proprietaria, design tokens, prototipagem e handoff. Cobre Figma, design systems, ti... |
| [`product-inventor`](skills/product-inventor/SKILL.md) | Product Inventor e Design Alchemist de nivel maximo — combina Product Thinking, Design Systems, UI Engineering, Psicologia Cognitiva, Storytelling e execucao impecavel nivel Job... |
| [`programmatic-seo`](skills/programmatic-seo/SKILL.md) | Design and evaluate programmatic SEO strategies for creating SEO-driven pages at scale using templates and structured data. |
| [`radix-ui-design-system`](skills/radix-ui-design-system/SKILL.md) | Build accessible design systems with Radix UI primitives. Headless component customization, theming strategies, and compound component patterns for production-grade UI libraries. |
| [`react-nextjs-development`](skills/react-nextjs-development/SKILL.md) | React and Next.js 14+ application development with App Router, Server Components, TypeScript, Tailwind CSS, and modern frontend patterns. |
| [`react-ui-patterns`](skills/react-ui-patterns/SKILL.md) | Modern React UI patterns for loading states, error handling, and data fetching. Use when building UI components, handling async data, or managing UI states. |
| [`referral-program`](skills/referral-program/SKILL.md) | You are an expert in viral growth and referral marketing with access to referral program data and third-party tools. Your goal is to help design and optimize programs that turn ... |
| [`remotion`](skills/remotion/SKILL.md) | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays |
| [`revops`](skills/revops/SKILL.md) | Design and improve revenue operations, lead lifecycle rules, scoring, routing, handoffs, and CRM process automation. Use when marketing, sales, and customer success workflows ne... |
| [`schema-markup`](skills/schema-markup/SKILL.md) | Design, validate, and optimize schema.org structured data for eligibility, correctness, and measurable SEO impact. |
| [`scroll-experience`](skills/scroll-experience/SKILL.md) | You see scrolling as a narrative device, not just navigation. You create moments of delight as users scroll. You know when to use subtle animations and when to go cinematic. You... |
| [`senior-frontend`](skills/senior-frontend/SKILL.md) | Frontend development skill for React, Next.js, TypeScript, and Tailwind CSS applications. Use when building React components, optimizing Next.js performance, analyzing bundle si... |
| [`seo-programmatic`](skills/seo-programmatic/SKILL.md) | Plan and audit programmatic SEO pages generated at scale from structured data. Use when designing templates, URL systems, internal linking, quality gates, and index-bloat safegu... |
| [`shadcn`](skills/shadcn/SKILL.md) | Manages shadcn/ui components and projects, providing context, documentation, and usage patterns for building modern design systems. |
| [`slack-gif-creator`](skills/slack-gif-creator/SKILL.md) | A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack. |
| [`snowflake-development`](skills/snowflake-development/SKILL.md) | Comprehensive Snowflake development assistant covering SQL best practices, data pipeline design (Dynamic Tables, Streams, Tasks, Snowpipe), Cortex AI functions, Cortex Agents, S... |
| [`steve-jobs`](skills/steve-jobs/SKILL.md) | Agente que simula Steve Jobs — cofundador da Apple, CEO da Pixar, fundador da NeXT, o maior designer de produtos tecnologicos da historia e o mais influente apresentador de prod... |
| [`stitch-loop`](skills/stitch-loop/SKILL.md) | Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern |
| [`swiftui-liquid-glass`](skills/swiftui-liquid-glass/SKILL.md) | Implement or review SwiftUI Liquid Glass APIs with correct fallbacks and modifier order. |
| [`swiftui-performance-audit`](skills/swiftui-performance-audit/SKILL.md) | Audit SwiftUI performance issues from code review and profiling evidence. |
| [`swiftui-ui-patterns`](skills/swiftui-ui-patterns/SKILL.md) | Apply proven SwiftUI UI patterns for navigation, sheets, async state, and reusable screens. |
| [`swiftui-view-refactor`](skills/swiftui-view-refactor/SKILL.md) | Refactor SwiftUI views into smaller components with stable, explicit data flow. |
| [`tailwind-design-system`](skills/tailwind-design-system/SKILL.md) | Build production-ready design systems with Tailwind CSS, including design tokens, component variants, responsive patterns, and accessibility. |
| [`team-composition-analysis`](skills/team-composition-analysis/SKILL.md) | Design optimal team structures, hiring plans, compensation strategies, and equity allocation for early-stage startups from pre-seed through Series A. |
| [`telegram-bot-builder`](skills/telegram-bot-builder/SKILL.md) | You build bots that people actually use daily. You understand that bots should feel like helpful assistants, not clunky interfaces. You know the Telegram ecosystem deeply - what... |
| [`telegram-mini-app`](skills/telegram-mini-app/SKILL.md) | You build apps where 800M+ Telegram users already are. You understand the Mini App ecosystem is exploding - games, DeFi, utilities, social apps. You know TON blockchain and how ... |
| [`theme-factory`](skills/theme-factory/SKILL.md) | This skill provides a curated collection of professional font and color themes themes, each with carefully selected color palettes and font pairings. Once a theme is chosen, it ... |
| [`threejs-animation`](skills/threejs-animation/SKILL.md) | Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF animations, creating procedural motion, or... |
| [`threejs-fundamentals`](skills/threejs-fundamentals/SKILL.md) | Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configuring renderers, managing object hierarch... |
| [`threejs-geometry`](skills/threejs-geometry/SKILL.md) | Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. Use when creating 3D shapes, working with vertices, building custom meshes, or optimiz... |
| [`threejs-interaction`](skills/threejs-interaction/SKILL.md) | Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detection, adding camera controls, or creating... |
| [`threejs-lighting`](skills/threejs-lighting/SKILL.md) | Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizing lighting performance. |
| [`threejs-loaders`](skills/threejs-loaders/SKILL.md) | Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or managing loading progress. |
| [`threejs-materials`](skills/threejs-materials/SKILL.md) | Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating custom shaders, or optimizing material pe... |
| [`threejs-postprocessing`](skills/threejs-postprocessing/SKILL.md) | Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or creating custom screen-space shaders. |
| [`threejs-skills`](skills/threejs-skills/SKILL.md) | Create 3D scenes, interactive experiences, and visual effects using Three.js. Use when user requests 3D graphics, WebGL experiences, 3D visualizations, animations, or interactiv... |
| [`threejs-textures`](skills/threejs-textures/SKILL.md) | Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, HDR environments, or texture optimizat... |
| [`ui-skills`](skills/ui-skills/SKILL.md) | Opinionated, evolving constraints to guide agents when building interfaces |
| [`ui-ux-designer`](skills/ui-ux-designer/SKILL.md) | Create interface designs, wireframes, and design systems. Masters user research, accessibility standards, and modern design tools. |
| [`ui-ux-pro-max`](skills/ui-ux-pro-max/SKILL.md) | Comprehensive design guide for web and mobile applications. Use when designing new UI components or pages, choosing color palettes and typography, or reviewing code for UX issues. |
| [`ui-visual-validator`](skills/ui-visual-validator/SKILL.md) | Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. |
| [`uxui-principles`](skills/uxui-principles/SKILL.md) | Evaluate interfaces against 168 research-backed UX/UI principles, detect antipatterns, and inject UX context into AI coding sessions. |
| [`vizcom`](skills/vizcom/SKILL.md) | AI-powered product design tool for transforming sketches into full-fidelity 3D renders. |
| [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | Review files for compliance with Web Interface Guidelines. |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="frontend_mobile"></a>
### 📱 Frontend Moderno & Desenvolvimento Mobile
*Aplicações escaláveis com React, Next.js, SvelteKit, Vue, Angular, Expo, React Native, Flutter, Swift, SwiftUI e Makepad.* (87 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`algolia-search`](skills/algolia-search/SKILL.md) | Expert patterns for Algolia search implementation, indexing strategies, React InstantSearch, and relevance tuning Use when: adding search to, algolia, instantsearch, search api,... |
| [`android_ui_verification`](skills/android_ui_verification/SKILL.md) | Automated end-to-end UI testing and verification on an Android Emulator using ADB. |
| [`angular`](skills/angular/SKILL.md) | Modern Angular (v20+) expert with deep knowledge of Signals, Standalone Components, Zoneless applications, SSR/Hydration, and reactive patterns. |
| [`angular-migration`](skills/angular-migration/SKILL.md) | Master AngularJS to Angular migration, including hybrid apps, component conversion, dependency injection changes, and routing migration. |
| [`angular-state-management`](skills/angular-state-management/SKILL.md) | Master modern Angular state management with Signals, NgRx, and RxJS. Use when setting up global state, managing component stores, choosing between state solutions, or migrating ... |
| [`app-store-optimization`](skills/app-store-optimization/SKILL.md) | Complete App Store Optimization (ASO) toolkit for researching, optimizing, and tracking mobile app performance on Apple App Store and Google Play Store |
| [`application-performance-performance-optimization`](skills/application-performance-performance-optimization/SKILL.md) | Optimize end-to-end application performance with profiling, observability, and backend/frontend tuning. Use when coordinating performance optimization across the stack. |
| [`astropy`](skills/astropy/SKILL.md) | Astropy is the core Python package for astronomy, providing essential functionality for astronomical research and data analysis. |
| [`attack-tree-construction`](skills/attack-tree-construction/SKILL.md) | Build comprehensive attack trees to visualize threat paths. Use when mapping attack scenarios, identifying defense gaps, or communicating security risks to stakeholders. |
| [`audit-skills`](skills/audit-skills/SKILL.md) | Expert security auditor for AI Skills and Bundles. Performs non-intrusive static analysis to identify malicious patterns, data leaks, system stability risks, and obfuscated payl... |
| [`avalonia-layout-zafiro`](skills/avalonia-layout-zafiro/SKILL.md) | Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing shared styles, generic components, and avoiding XAML redundancy. |
| [`avalonia-viewmodels-zafiro`](skills/avalonia-viewmodels-zafiro/SKILL.md) | Optimal ViewModel and Wizard creation patterns for Avalonia using Zafiro and ReactiveUI. |
| [`avalonia-zafiro-development`](skills/avalonia-zafiro-development/SKILL.md) | Mandatory skills, conventions, and behavioral rules for Avalonia UI development using the Zafiro toolkit. |
| [`awt-e2e-testing`](skills/awt-e2e-testing/SKILL.md) | AI-powered E2E web testing — eyes and hands for AI coding tools. Declarative YAML scenarios, Playwright execution, visual matching (OpenCV + OCR), platform auto-detection (Flutt... |
| [`azd-deployment`](skills/azd-deployment/SKILL.md) | Deploy containerized frontend + backend applications to Azure Container Apps with remote builds, managed identity, and idempotent infrastructure. |
| [`azure-cosmos-java`](skills/azure-cosmos-java/SKILL.md) | Azure Cosmos DB SDK for Java. NoSQL database operations with global distribution, multi-model support, and reactive patterns. |
| [`azure-monitor-opentelemetry-exporter-java`](skills/azure-monitor-opentelemetry-exporter-java/SKILL.md) | Azure Monitor OpenTelemetry Exporter for Java. Export OpenTelemetry traces, metrics, and logs to Azure Monitor/Application Insights. |
| [`azure-monitor-opentelemetry-exporter-py`](skills/azure-monitor-opentelemetry-exporter-py/SKILL.md) | Azure Monitor OpenTelemetry Exporter for Python. Use for low-level OpenTelemetry export to Application Insights. |
| [`bigquery-data-transfer-service`](skills/bigquery-data-transfer-service/SKILL.md) | Discovers and inspects BigQuery Data Transfer Service (DTS) configurations. Use this to identify existing ingestion pipelines and extract datasource or transfer config metadata ... |
| [`carrier-relationship-management`](skills/carrier-relationship-management/SKILL.md) | Codified expertise for managing carrier portfolios, negotiating freight rates, tracking carrier performance, allocating freight, and maintaining strategic carrier relationships. |
| [`cc-skill-coding-standards`](skills/cc-skill-coding-standards/SKILL.md) | Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development. |
| [`cc-skill-frontend-patterns`](skills/cc-skill-frontend-patterns/SKILL.md) | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. |
| [`development`](skills/development/SKILL.md) | Comprehensive web, mobile, and backend development workflow bundling frontend, backend, full-stack, and mobile development skills for end-to-end application delivery. |
| [`discord-automation`](skills/discord-automation/SKILL.md) | Automate Discord tasks via Rube MCP (Composio): messages, channels, roles, webhooks, reactions. Always search tools first for current schemas. |
| [`docs`](skills/docs/SKILL.md) | Instruções e utilitários especializados para docs. |
| [`evolution`](skills/evolution/SKILL.md) | This skill enables makepad-skills to self-improve continuously during development. |
| [`expo-api-routes`](skills/expo-api-routes/SKILL.md) | Guidelines for creating API routes in Expo Router with EAS Hosting |
| [`expo-cicd-workflows`](skills/expo-cicd-workflows/SKILL.md) | Helps understand and write EAS workflow YAML files for Expo projects. Use this skill when the user asks about CI/CD or workflows in an Expo or EAS context, mentions .eas/workflo... |
| [`expo-deployment`](skills/expo-deployment/SKILL.md) | Deploy Expo apps to production |
| [`expo-dev-client`](skills/expo-dev-client/SKILL.md) | Build and distribute Expo development clients locally or via TestFlight |
| [`flutter-expert`](skills/flutter-expert/SKILL.md) | Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment. |
| [`fp-react`](skills/fp-react/SKILL.md) | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Works with React 18/19, Next.js 14/15. |
| [`fp-ts-react`](skills/fp-ts-react/SKILL.md) | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Use when building React apps with functional programming patterns. Works with React 18/19, Ne... |
| [`frontend-mobile-security-xss-scan`](skills/frontend-mobile-security-xss-scan/SKILL.md) | You are a frontend security specialist focusing on Cross-Site Scripting (XSS) vulnerability detection and prevention. Analyze React, Vue, Angular, and vanilla JavaScript code to... |
| [`frontend-security-coder`](skills/frontend-security-coder/SKILL.md) | Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns. |
| [`godot-4-migration`](skills/godot-4-migration/SKILL.md) | Specialized guide for migrating Godot 3.x projects to Godot 4 (GDScript 2.0), covering syntax changes, Tweens, and exports. |
| [`hono`](skills/hono/SKILL.md) | Build ultra-fast web APIs and full-stack apps with Hono — runs on Cloudflare Workers, Deno, Bun, Node.js, and any WinterCG-compatible runtime. |
| [`instagram`](skills/instagram/SKILL.md) | Integracao completa com Instagram via Graph API. Publicacao, analytics, comentarios, DMs, hashtags, agendamento, templates e gestao de contas Business/Creator. |
| [`ios-debugger-agent`](skills/ios-debugger-agent/SKILL.md) | Debug the current iOS project on a booted simulator with XcodeBuildMCP. |
| [`ios-developer`](skills/ios-developer/SKILL.md) | Develop native iOS applications with Swift/SwiftUI. Masters iOS 18, SwiftUI, UIKit integration, Core Data, networking, and App Store optimization. |
| [`junta-leiloeiros`](skills/junta-leiloeiros/SKILL.md) | Coleta e consulta dados de leiloeiros oficiais de todas as 27 Juntas Comerciais do Brasil. Scraper multi-UF, banco SQLite, API FastAPI e exportacao CSV/JSON. |
| [`k6-load-testing`](skills/k6-load-testing/SKILL.md) | Comprehensive k6 load testing skill for API, browser, and scalability testing. Write realistic load scenarios, analyze results, and integrate with CI/CD. |
| [`leiloeiro-risco`](skills/leiloeiro-risco/SKILL.md) | Analise de risco em leiloes de imoveis. Score 36 pontos, riscos juridicos/financeiros/operacionais, stress test 4 cenarios e ROI ponderado por risco. |
| [`libreoffice`](skills/libreoffice/SKILL.md) | Instruções e utilitários especializados para libreoffice. |
| [`macos-menubar-tuist-app`](skills/macos-menubar-tuist-app/SKILL.md) | Build, refactor, or review SwiftUI macOS menubar apps that use Tuist. |
| [`macos-spm-app-packaging`](skills/macos-spm-app-packaging/SKILL.md) | Scaffold, build, sign, and package SwiftPM macOS apps without Xcode projects. |
| [`makepad-deployment`](skills/makepad-deployment/SKILL.md) | \| CRITICAL: Use for Makepad packaging and deployment. Triggers on: deploy, package, APK, IPA, 打包, 部署, cargo-packager, cargo-makepad, WASM, Android, iOS, distribution, installer... |
| [`makepad-event-action`](skills/makepad-event-action/SKILL.md) | \| CRITICAL: Use for Makepad event and action handling. Triggers on: makepad event, makepad action, Event enum, ActionTrait, handle_event, MouseDown, KeyDown, TouchUpdate, Hit, ... |
| [`makepad-layout`](skills/makepad-layout/SKILL.md) | \| CRITICAL: Use for Makepad layout system. Triggers on: makepad layout, makepad width, makepad height, makepad flex, makepad padding, makepad margin, makepad flow, makepad alig... |
| [`makepad-platform`](skills/makepad-platform/SKILL.md) | \| CRITICAL: Use for Makepad cross-platform support. Triggers on: makepad platform, makepad os, makepad macos, makepad windows, makepad linux, makepad android, makepad ios, make... |
| [`makepad-reference`](skills/makepad-reference/SKILL.md) | This category provides reference materials for debugging, code quality, and advanced layout patterns. |
| [`makepad-shaders`](skills/makepad-shaders/SKILL.md) | \| CRITICAL: Use for Makepad shader system. Triggers on: makepad shader, makepad draw_bg, Sdf2d, makepad pixel, makepad glsl, makepad sdf, draw_quad, makepad gpu, makepad 着色器, m... |
| [`makepad-skills`](skills/makepad-skills/SKILL.md) | Makepad UI development skills for Rust apps: setup, patterns, shaders, packaging, and troubleshooting. |
| [`makepad-splash`](skills/makepad-splash/SKILL.md) | \| CRITICAL: Use for Makepad Splash scripting language. Triggers on: splash language, makepad script, makepad scripting, script!, cx.eval, makepad dynamic, makepad AI, splash 语言... |
| [`makepad-widgets`](skills/makepad-widgets/SKILL.md) | Version: makepad-widgets (dev branch) \| Last Updated: 2026-01-19 > > Check for updates: https://crates.io/crates/makepad-widgets |
| [`native-data-fetching`](skills/native-data-fetching/SKILL.md) | Use when implementing or debugging ANY network request, API call, or data fetching. Covers fetch API, React Query, SWR, error handling, caching, offline support, and Expo Router... |
| [`nextjs-best-practices`](skills/nextjs-best-practices/SKILL.md) | Next.js App Router principles. Server Components, data fetching, routing patterns. |
| [`nextjs-supabase-auth`](skills/nextjs-supabase-auth/SKILL.md) | Expert integration of Supabase Auth with Next.js App Router Use when: supabase auth next, authentication next.js, login supabase, auth middleware, protected route. |
| [`nx-workspace-patterns`](skills/nx-workspace-patterns/SKILL.md) | Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands. |
| [`odoo-edi-connector`](skills/odoo-edi-connector/SKILL.md) | Guide for implementing EDI (Electronic Data Interchange) with Odoo: X12, EDIFACT document mapping, partner onboarding, and automated order processing. |
| [`progressive-web-app`](skills/progressive-web-app/SKILL.md) | Build Progressive Web Apps (PWAs) with offline support, installability, and caching strategies. Trigger whenever the user mentions PWA, service workers, web app manifests, Workb... |
| [`react-best-practices`](skills/react-best-practices/SKILL.md) | Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. Use when writing new React components or Next.js pages, implementing data ... |
| [`react-component-performance`](skills/react-component-performance/SKILL.md) | Diagnose slow React components and suggest targeted performance fixes. |
| [`react-flow-node-ts`](skills/react-flow-node-ts/SKILL.md) | Create React Flow node components following established patterns with proper TypeScript types and store integration. |
| [`react-modernization`](skills/react-modernization/SKILL.md) | Master React version upgrades, class to hooks migration, concurrent features adoption, and codemods for automated transformation. |
| [`react-patterns`](skills/react-patterns/SKILL.md) | Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices. |
| [`react-state-management`](skills/react-state-management/SKILL.md) | Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing server state, or choosing between state mana... |
| [`remotion-best-practices`](skills/remotion-best-practices/SKILL.md) | Best practices for Remotion - Video creation in React |
| [`robius-matrix-integration`](skills/robius-matrix-integration/SKILL.md) | \| CRITICAL: Use for Matrix SDK integration with Makepad. Triggers on: Matrix SDK, sliding sync, MatrixRequest, timeline, matrix-sdk, matrix client, robrix, matrix room, Matrix ... |
| [`security`](skills/security/SKILL.md) | Instruções e utilitários especializados para security. |
| [`shopify-apps`](skills/shopify-apps/SKILL.md) | Modern Shopify app template with React Router |
| [`skill-sentinel`](skills/skill-sentinel/SKILL.md) | Auditoria e evolucao do ecossistema de skills. Qualidade de codigo, seguranca, custos, gaps, duplicacoes, dependencias e relatorios de saude. |
| [`slack-automation`](skills/slack-automation/SKILL.md) | Automate Slack workspace operations including messaging, search, channel management, and reaction workflows through Composio's Slack toolkit. |
| [`startup-business-analyst-financial-projections`](skills/startup-business-analyst-financial-projections/SKILL.md) | Create detailed 3-5 year financial model with revenue, costs, cash flow, and scenarios |
| [`sveltekit`](skills/sveltekit/SKILL.md) | Build full-stack web applications with SvelteKit — file-based routing, SSR, SSG, API routes, and form actions in one framework. |
| [`swift-concurrency-expert`](skills/swift-concurrency-expert/SKILL.md) | Review and fix Swift concurrency issues such as actor isolation and Sendable violations. |
| [`tanstack-query-expert`](skills/tanstack-query-expert/SKILL.md) | Expert in TanStack Query (React Query) — asynchronous state management. Covers data fetching, stale time configuration, mutations, optimistic updates, and Next.js App Router (SS... |
| [`temporal-python-testing`](skills/temporal-python-testing/SKILL.md) | Comprehensive testing approaches for Temporal workflows using pytest, progressive disclosure resources for specific testing scenarios. |
| [`trpc-fullstack`](skills/trpc-fullstack/SKILL.md) | Build end-to-end type-safe APIs with tRPC — routers, procedures, middleware, subscriptions, and Next.js/React integration patterns. |
| [`turborepo-caching`](skills/turborepo-caching/SKILL.md) | Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelines, or implementing distributed caching. |
| [`uniprot-database`](skills/uniprot-database/SKILL.md) | Direct REST API access to UniProt. Protein searches, FASTA retrieval, ID mapping, Swiss-Prot/TrEMBL. For Python workflows with multiple databases, prefer bioservices (unified in... |
| [`upgrading-expo`](skills/upgrading-expo/SKILL.md) | Upgrade Expo SDK versions |
| [`vercel-ai-sdk-expert`](skills/vercel-ai-sdk-expert/SKILL.md) | Expert in the Vercel AI SDK. Covers Core API (generateText, streamText), UI hooks (useChat, useCompletion), tool calling, and streaming UI components with React and Next.js. |
| [`web-scraper`](skills/web-scraper/SKILL.md) | Web scraping inteligente multi-estrategia. Extrai dados estruturados de paginas web (tabelas, listas, precos). Paginacao, monitoramento e export CSV/JSON. |
| [`windows-privilege-escalation`](skills/windows-privilege-escalation/SKILL.md) | Instruções e utilitários especializados para windows-privilege-escalation. |
| [`zod-validation-expert`](skills/zod-validation-expert/SKILL.md) | Expert in Zod — TypeScript-first schema validation. Covers parsing, custom errors, refinements, type inference, and integration with React Hook Form, Next.js, and tRPC. |
| [`zustand-store-ts`](skills/zustand-store-ts/SKILL.md) | Create Zustand stores following established patterns with proper TypeScript types and middleware. |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="backend_apis"></a>
### ⚙️ Backend, APIs de Alta Performance & Linguagens
*APIs robustas REST, GraphQL, gRPC, tRPC e desenvolvimento em Python, Go, Rust, C#, Java, PHP, Ruby, Node.js e Bun.* (205 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`api-documentation`](skills/api-documentation/SKILL.md) | API documentation workflow for generating OpenAPI specs, creating developer guides, and maintaining comprehensive API documentation. |
| [`api-documentation-generator`](skills/api-documentation-generator/SKILL.md) | Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices |
| [`api-documenter`](skills/api-documenter/SKILL.md) | Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate SDKs, and build comprehensive developer... |
| [`api-endpoint-builder`](skills/api-endpoint-builder/SKILL.md) | Builds production-ready REST API endpoints with validation, error handling, authentication, and documentation. Follows best practices for security and scalability. |
| [`api-fuzzing-bug-bounty`](skills/api-fuzzing-bug-bounty/SKILL.md) | Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements. Covers vulnerability discovery, authenti... |
| [`api-security-testing`](skills/api-security-testing/SKILL.md) | API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and security best practices. |
| [`apify-actorization`](skills/apify-actorization/SKILL.md) | Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-... |
| [`apify-audience-analysis`](skills/apify-audience-analysis/SKILL.md) | Understand audience demographics, preferences, behavior patterns, and engagement quality across Facebook, Instagram, YouTube, and TikTok. |
| [`apify-brand-reputation-monitoring`](skills/apify-brand-reputation-monitoring/SKILL.md) | Scrape reviews, ratings, and brand mentions from multiple platforms using Apify Actors. |
| [`apify-competitor-intelligence`](skills/apify-competitor-intelligence/SKILL.md) | Analyze competitor strategies, content, pricing, ads, and market positioning across Google Maps, Booking.com, Facebook, Instagram, YouTube, and TikTok. |
| [`apify-content-analytics`](skills/apify-content-analytics/SKILL.md) | Track engagement metrics, measure campaign ROI, and analyze content performance across Instagram, Facebook, YouTube, and TikTok. |
| [`apify-ecommerce`](skills/apify-ecommerce/SKILL.md) | Extract product data, prices, reviews, and seller information from any e-commerce platform using Apify's E-commerce Scraping Tool. |
| [`apify-influencer-discovery`](skills/apify-influencer-discovery/SKILL.md) | Find and evaluate influencers for brand partnerships, verify authenticity, and track collaboration performance across Instagram, Facebook, YouTube, and TikTok. |
| [`apify-lead-generation`](skills/apify-lead-generation/SKILL.md) | Scrape leads from multiple platforms using Apify Actors. |
| [`apify-market-research`](skills/apify-market-research/SKILL.md) | Analyze market conditions, geographic opportunities, pricing, consumer behavior, and product validation across Google Maps, Facebook, Instagram, Booking.com, and TripAdvisor. |
| [`apify-trend-analysis`](skills/apify-trend-analysis/SKILL.md) | Discover and track emerging trends across Google Trends, Instagram, Facebook, YouTube, and TikTok to inform content strategy. |
| [`apify-ultimate-scraper`](skills/apify-ultimate-scraper/SKILL.md) | AI-driven data extraction from 55+ Actors across all major platforms. This skill automatically selects the best Actor for your task. |
| [`auth-implementation-patterns`](skills/auth-implementation-patterns/SKILL.md) | Build secure, scalable authentication and authorization systems using industry-standard patterns and modern best practices. |
| [`azure-ai-agents-persistent-dotnet`](skills/azure-ai-agents-persistent-dotnet/SKILL.md) | Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| [`azure-ai-document-intelligence-dotnet`](skills/azure-ai-document-intelligence-dotnet/SKILL.md) | Azure AI Document Intelligence SDK for .NET. Extract text, tables, and structured data from documents using prebuilt and custom models. |
| [`azure-ai-projects-dotnet`](skills/azure-ai-projects-dotnet/SKILL.md) | Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections, datasets, deployments, evaluations, and indexes. |
| [`azure-ai-voicelive-dotnet`](skills/azure-ai-voicelive-dotnet/SKILL.md) | Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication. |
| [`azure-ai-voicelive-java`](skills/azure-ai-voicelive-java/SKILL.md) | Azure AI VoiceLive SDK for Java. Real-time bidirectional voice conversations with AI assistants using WebSocket. |
| [`azure-ai-voicelive-py`](skills/azure-ai-voicelive-py/SKILL.md) | Build real-time voice AI applications with bidirectional WebSocket communication. |
| [`azure-ai-voicelive-ts`](skills/azure-ai-voicelive-ts/SKILL.md) | Azure AI Voice Live SDK for JavaScript/TypeScript. Build real-time voice AI applications with bidirectional WebSocket communication. |
| [`azure-communication-common-java`](skills/azure-communication-common-java/SKILL.md) | Azure Communication Services common utilities for Java. Use when working with CommunicationTokenCredential, user identifiers, token refresh, or shared authentication across ACS ... |
| [`azure-cosmos-py`](skills/azure-cosmos-py/SKILL.md) | Azure Cosmos DB SDK for Python (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| [`azure-cosmos-rust`](skills/azure-cosmos-rust/SKILL.md) | Azure Cosmos DB SDK for Rust (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| [`azure-eventhub-dotnet`](skills/azure-eventhub-dotnet/SKILL.md) | Azure Event Hubs SDK for .NET. |
| [`azure-eventhub-rust`](skills/azure-eventhub-rust/SKILL.md) | Azure Event Hubs SDK for Rust. Use for sending and receiving events, streaming data ingestion. |
| [`azure-functions`](skills/azure-functions/SKILL.md) | Modern .NET execution model with process isolation |
| [`azure-identity-dotnet`](skills/azure-identity-dotnet/SKILL.md) | Azure Identity SDK for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use for DefaultAzureCredential, managed identity, service principals, and dev... |
| [`azure-identity-java`](skills/azure-identity-java/SKILL.md) | Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD). |
| [`azure-identity-py`](skills/azure-identity-py/SKILL.md) | Azure Identity SDK for Python authentication. Use for DefaultAzureCredential, managed identity, service principals, and token caching. |
| [`azure-identity-rust`](skills/azure-identity-rust/SKILL.md) | Azure Identity SDK for Rust authentication. Use for DeveloperToolsCredential, ManagedIdentityCredential, ClientSecretCredential, and token-based authentication. |
| [`azure-identity-ts`](skills/azure-identity-ts/SKILL.md) | Authenticate to Azure services with various credential types. |
| [`azure-keyvault-certificates-rust`](skills/azure-keyvault-certificates-rust/SKILL.md) | Azure Key Vault Certificates SDK for Rust. Use for creating, importing, and managing certificates. |
| [`azure-keyvault-keys-rust`](skills/azure-keyvault-keys-rust/SKILL.md) | Azure Key Vault Keys SDK for Rust. Use for creating, managing, and using cryptographic keys. Triggers: "keyvault keys rust", "KeyClient rust", "create key rust", "encrypt rust",... |
| [`azure-keyvault-secrets-rust`](skills/azure-keyvault-secrets-rust/SKILL.md) | Azure Key Vault Secrets SDK for Rust. Use for storing and retrieving secrets, passwords, and API keys. Triggers: "keyvault secrets rust", "SecretClient rust", "get secret rust",... |
| [`azure-maps-search-dotnet`](skills/azure-maps-search-dotnet/SKILL.md) | Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and weather. Use for address search, directions, map tiles, IP geolocation... |
| [`azure-messaging-webpubsub-java`](skills/azure-messaging-webpubsub-java/SKILL.md) | Build real-time web applications with Azure Web PubSub SDK for Java. Use when implementing WebSocket-based messaging, live updates, chat applications, or server-to-client push n... |
| [`azure-messaging-webpubsubservice-py`](skills/azure-messaging-webpubsubservice-py/SKILL.md) | Azure Web PubSub Service SDK for Python. Use for real-time messaging, WebSocket connections, and pub/sub patterns. |
| [`azure-mgmt-apicenter-dotnet`](skills/azure-mgmt-apicenter-dotnet/SKILL.md) | Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery. |
| [`azure-mgmt-apicenter-py`](skills/azure-mgmt-apicenter-py/SKILL.md) | Azure API Center Management SDK for Python. Use for managing API inventory, metadata, and governance across your organization. |
| [`azure-mgmt-apimanagement-dotnet`](skills/azure-mgmt-apimanagement-dotnet/SKILL.md) | Azure Resource Manager SDK for API Management in .NET. |
| [`azure-mgmt-apimanagement-py`](skills/azure-mgmt-apimanagement-py/SKILL.md) | Azure API Management SDK for Python. Use for managing APIM services, APIs, products, subscriptions, and policies. |
| [`azure-mgmt-applicationinsights-dotnet`](skills/azure-mgmt-applicationinsights-dotnet/SKILL.md) | Azure Application Insights SDK for .NET. Application performance monitoring and observability resource management. |
| [`azure-mgmt-arizeaiobservabilityeval-dotnet`](skills/azure-mgmt-arizeaiobservabilityeval-dotnet/SKILL.md) | Azure Resource Manager SDK for Arize AI Observability and Evaluation (.NET). |
| [`azure-mgmt-botservice-dotnet`](skills/azure-mgmt-botservice-dotnet/SKILL.md) | Azure Resource Manager SDK for Bot Service in .NET. Management plane operations for creating and managing Azure Bot resources, channels (Teams, DirectLine, Slack), and connectio... |
| [`azure-mgmt-fabric-dotnet`](skills/azure-mgmt-fabric-dotnet/SKILL.md) | Azure Resource Manager SDK for Fabric in .NET. |
| [`azure-mgmt-mongodbatlas-dotnet`](skills/azure-mgmt-mongodbatlas-dotnet/SKILL.md) | Manage MongoDB Atlas Organizations as Azure ARM resources with unified billing through Azure Marketplace. |
| [`azure-mgmt-weightsandbiases-dotnet`](skills/azure-mgmt-weightsandbiases-dotnet/SKILL.md) | Azure Weights & Biases SDK for .NET. ML experiment tracking and model management via Azure Marketplace. Use for creating W&B instances, managing SSO, marketplace integration, an... |
| [`azure-monitor-ingestion-py`](skills/azure-monitor-ingestion-py/SKILL.md) | Azure Monitor Ingestion SDK for Python. Use for sending custom logs to Log Analytics workspace via Logs Ingestion API. |
| [`azure-monitor-opentelemetry-ts`](skills/azure-monitor-opentelemetry-ts/SKILL.md) | Auto-instrument Node.js applications with distributed tracing, metrics, and logs. |
| [`azure-postgres-ts`](skills/azure-postgres-ts/SKILL.md) | Connect to Azure Database for PostgreSQL Flexible Server from Node.js/TypeScript using the pg (node-postgres) package. |
| [`azure-resource-manager-cosmosdb-dotnet`](skills/azure-resource-manager-cosmosdb-dotnet/SKILL.md) | Azure Resource Manager SDK for Cosmos DB in .NET. |
| [`azure-resource-manager-durabletask-dotnet`](skills/azure-resource-manager-durabletask-dotnet/SKILL.md) | Azure Resource Manager SDK for Durable Task Scheduler in .NET. |
| [`azure-resource-manager-mysql-dotnet`](skills/azure-resource-manager-mysql-dotnet/SKILL.md) | Azure MySQL Flexible Server SDK for .NET. Database management for MySQL Flexible Server deployments. |
| [`azure-resource-manager-playwright-dotnet`](skills/azure-resource-manager-playwright-dotnet/SKILL.md) | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET. |
| [`azure-resource-manager-postgresql-dotnet`](skills/azure-resource-manager-postgresql-dotnet/SKILL.md) | Azure PostgreSQL Flexible Server SDK for .NET. Database management for PostgreSQL Flexible Server deployments. |
| [`azure-resource-manager-redis-dotnet`](skills/azure-resource-manager-redis-dotnet/SKILL.md) | Azure Resource Manager SDK for Redis in .NET. |
| [`azure-resource-manager-sql-dotnet`](skills/azure-resource-manager-sql-dotnet/SKILL.md) | Azure Resource Manager SDK for Azure SQL in .NET. |
| [`azure-search-documents-dotnet`](skills/azure-search-documents-dotnet/SKILL.md) | Azure AI Search SDK for .NET (Azure.Search.Documents). Use for building search applications with full-text, vector, semantic, and hybrid search. |
| [`azure-security-keyvault-keys-dotnet`](skills/azure-security-keyvault-keys-dotnet/SKILL.md) | Azure Key Vault Keys SDK for .NET. Client library for managing cryptographic keys in Azure Key Vault and Managed HSM. Use for key creation, rotation, encryption, decryption, sig... |
| [`azure-security-keyvault-secrets-java`](skills/azure-security-keyvault-secrets-java/SKILL.md) | Azure Key Vault Secrets Java SDK for secret management. Use when storing, retrieving, or managing passwords, API keys, connection strings, or other sensitive configuration data. |
| [`azure-servicebus-dotnet`](skills/azure-servicebus-dotnet/SKILL.md) | Azure Service Bus SDK for .NET. Enterprise messaging with queues, topics, subscriptions, and sessions. |
| [`azure-speech-to-text-rest-py`](skills/azure-speech-to-text-rest-py/SKILL.md) | Azure Speech to Text REST API for short audio (Python). Use for simple speech recognition of audio files up to 60 seconds without the Speech SDK. |
| [`azure-web-pubsub-ts`](skills/azure-web-pubsub-ts/SKILL.md) | Real-time messaging with WebSocket connections and pub/sub patterns. |
| [`backend-development-feature-development`](skills/backend-development-feature-development/SKILL.md) | Orchestrate end-to-end backend feature development from requirements to deployment. Use when coordinating multi-phase feature delivery across teams and services. |
| [`backend-security-coder`](skills/backend-security-coder/SKILL.md) | Expert in secure backend coding practices specializing in input validation, authentication, and API security. Use PROACTIVELY for backend security implementations or security co... |
| [`bevy-ecs-expert`](skills/bevy-ecs-expert/SKILL.md) | Master Bevy's Entity Component System (ECS) in Rust, covering Systems, Queries, Resources, and parallel scheduling. |
| [`bigquery-bigframes`](skills/bigquery-bigframes/SKILL.md) | Generates Python code using BigQuery DataFrames (BigFrames), the pandas/scikit-learn-style\ \ API over BigQuery. Use when writing BigFrames code or doing pandas-style dataframe/... |
| [`broken-authentication`](skills/broken-authentication/SKILL.md) | Identify and exploit authentication and session management vulnerabilities in web applications. Broken authentication consistently ranks in the OWASP Top 10 and can lead to acco... |
| [`bun-development`](skills/bun-development/SKILL.md) | Fast, modern JavaScript/TypeScript development with the Bun runtime, inspired by [oven-sh/bun](https://github.com/oven-sh/bun). |
| [`c-pro`](skills/c-pro/SKILL.md) | Write efficient C code with proper memory management, pointer |
| [`cc-skill-security-review`](skills/cc-skill-security-review/SKILL.md) | This skill ensures all code follows security best practices and identifies potential vulnerabilities. Use when implementing authentication or authorization, handling user input ... |
| [`churn-prevention`](skills/churn-prevention/SKILL.md) | Reduce voluntary and involuntary churn with cancel flows, save offers, dunning, win-back tactics, and retention strategy. Use when users are cancelling, failed payments are risi... |
| [`clerk-auth`](skills/clerk-auth/SKILL.md) | Expert patterns for Clerk auth implementation, middleware, organizations, webhooks, and user sync Use when: adding authentication, clerk auth, user authentication, sign in, sign... |
| [`content-strategy`](skills/content-strategy/SKILL.md) | Plan a content strategy, topic clusters, editorial roadmap, and content mix for traffic, authority, and lead generation. Use when deciding what to publish, what topics to priori... |
| [`context7`](skills/context7/SKILL.md) | Use Context7 for current, version-specific library and framework documentation. Trigger when the user asks about package APIs, framework setup, SDK usage, migrations, deprecatio... |
| [`cpp-pro`](skills/cpp-pro/SKILL.md) | Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. Handles templates, move semantics, and performance optimization. |
| [`csharp-pro`](skills/csharp-pro/SKILL.md) | Write modern C# code with advanced features like records, pattern matching, and async/await. Optimizes .NET applications, implements enterprise patterns, and ensures comprehensi... |
| [`customer-psychographic-profiler`](skills/customer-psychographic-profiler/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`data-structure-protocol`](skills/data-structure-protocol/SKILL.md) | Give agents persistent structural memory of a codebase — navigate dependencies, track public APIs, and understand why connections exist without re-reading the whole repo. |
| [`dbos-golang`](skills/dbos-golang/SKILL.md) | Guide for building reliable, fault-tolerant Go applications with DBOS durable workflows. Use when adding DBOS to existing Go code, creating workflows and steps, or using queues ... |
| [`dbos-python`](skills/dbos-python/SKILL.md) | Guide for building reliable, fault-tolerant Python applications with DBOS durable workflows. Use when adding DBOS to existing Python code, creating workflows and steps, or using... |
| [`dbos-typescript`](skills/dbos-typescript/SKILL.md) | Guide for building reliable, fault-tolerant TypeScript applications with DBOS durable workflows. Use when adding DBOS to existing TypeScript code, creating workflows and steps, ... |
| [`debugging-strategies`](skills/debugging-strategies/SKILL.md) | Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical approaches. |
| [`devops-troubleshooter`](skills/devops-troubleshooter/SKILL.md) | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. |
| [`distributed-tracing`](skills/distributed-tracing/SKILL.md) | Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices. |
| [`django-access-review`](skills/django-access-review/SKILL.md) | django-access-review |
| [`django-perf-review`](skills/django-perf-review/SKILL.md) | Django performance code review. Use when asked to "review Django performance", "find N+1 queries", "optimize Django", "check queryset performance", "database performance", "Djan... |
| [`doc-coauthoring`](skills/doc-coauthoring/SKILL.md) | This skill provides a structured workflow for guiding users through collaborative document creation. Act as an active guide, walking users through three stages: Context Gatherin... |
| [`documentation-templates`](skills/documentation-templates/SKILL.md) | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. |
| [`docusign-automation`](skills/docusign-automation/SKILL.md) | Automate DocuSign tasks via Rube MCP (Composio): templates, envelopes, signatures, document management. Always search tools first for current schemas. |
| [`dotnet-backend`](skills/dotnet-backend/SKILL.md) | Build ASP.NET Core 8+ backend services with EF Core, auth, background jobs, and production API patterns. |
| [`dotnet-backend-patterns`](skills/dotnet-backend-patterns/SKILL.md) | Master C#/.NET patterns for building production-grade APIs, MCP servers, and enterprise backends with modern best practices (2024/2025). |
| [`elixir-pro`](skills/elixir-pro/SKILL.md) | Write idiomatic Elixir code with OTP patterns, supervision trees, and Phoenix LiveView. Masters concurrency, fault tolerance, and distributed systems. |
| [`emblemai-crypto-wallet`](skills/emblemai-crypto-wallet/SKILL.md) | Crypto wallet management across 7 blockchains via EmblemAI Agent Hustle API. Balance checks, token swaps, portfolio analysis, and transaction execution for Solana, Ethereum, Bas... |
| [`ethical-hacking-methodology`](skills/ethical-hacking-methodology/SKILL.md) | Master the complete penetration testing lifecycle from reconnaissance through reporting. This skill covers the five stages of ethical hacking methodology, essential tools, attac... |
| [`fastapi-pro`](skills/fastapi-pro/SKILL.md) | Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Master microservices, WebSockets, and modern Python async patterns. |
| [`fastapi-router-py`](skills/fastapi-router-py/SKILL.md) | Create FastAPI routers following established patterns with proper authentication, response models, and HTTP status codes. |
| [`fastapi-templates`](skills/fastapi-templates/SKILL.md) | Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. Use when building new FastAPI applications or setting up ba... |
| [`ffuf-web-fuzzing`](skills/ffuf-web-fuzzing/SKILL.md) | Expert guidance for ffuf web fuzzing during penetration testing, including authenticated fuzzing with raw requests, auto-calibration, and result analysis |
| [`file-uploads`](skills/file-uploads/SKILL.md) | Careful about security and performance. Never trusts file extensions. Knows that large uploads need special handling. Prefers presigned URLs over server proxying. |
| [`firecrawl-scraper`](skills/firecrawl-scraper/SKILL.md) | Deep web scraping, screenshots, PDF parsing, and website crawling using Firecrawl API. Use when you need deep content extraction from web pages, page interaction is required (cl... |
| [`fp-async`](skills/fp-async/SKILL.md) | Practical async patterns using TaskEither - clean pipelines instead of try/catch hell, with real API examples |
| [`fp-backend`](skills/fp-backend/SKILL.md) | Functional programming patterns for Node.js/Deno backend development using fp-ts, ReaderTaskEither, and functional dependency injection |
| [`fp-data-transforms`](skills/fp-data-transforms/SKILL.md) | Everyday data transformations using functional patterns - arrays, objects, grouping, aggregation, and null-safe access |
| [`fp-either-ref`](skills/fp-either-ref/SKILL.md) | Quick reference for Either type. Use when user needs error handling, validation, or operations that can fail with typed errors. |
| [`fp-errors`](skills/fp-errors/SKILL.md) | Stop throwing everywhere - handle errors as values using Either and TaskEither for cleaner, more predictable code |
| [`fp-option-ref`](skills/fp-option-ref/SKILL.md) | Quick reference for Option type. Use when user needs to handle nullable values, optional data, or wants to avoid null checks. |
| [`fp-pipe-ref`](skills/fp-pipe-ref/SKILL.md) | Quick reference for pipe and flow. Use when user needs to chain functions, compose operations, or build data pipelines in fp-ts. |
| [`fp-taskeither-ref`](skills/fp-taskeither-ref/SKILL.md) | Quick reference for TaskEither. Use when user needs async error handling, API calls, or Promise-based operations that can fail. |
| [`fp-ts-errors`](skills/fp-ts-errors/SKILL.md) | Handle errors as values using fp-ts Either and TaskEither for cleaner, more predictable TypeScript code. Use when implementing error handling patterns with fp-ts. |
| [`fp-types-ref`](skills/fp-types-ref/SKILL.md) | Quick reference for fp-ts types. Use when user asks which type to use, needs Option/Either/Task decision help, or wants fp-ts imports. |
| [`gcloud-auth-verification`](skills/gcloud-auth-verification/SKILL.md) | Guidelines for identifying and resolving missing Google Cloud authentication and Application Default Credentials (ADC). Use this skill if `gcloud`, `bq`, `dataform`, or Python l... |
| [`gcp-cloud-run`](skills/gcp-cloud-run/SKILL.md) | When to use: ['Web applications and APIs', 'Need any runtime or library', 'Complex services with multiple endpoints', 'Stateless containerized workloads'] |
| [`github`](skills/github/SKILL.md) | Use the `gh` CLI for issues, pull requests, Actions runs, and GitHub API queries. |
| [`gmail-automation`](skills/gmail-automation/SKILL.md) | Lightweight Gmail integration with standalone OAuth authentication. No MCP server required. |
| [`go-rod-master`](skills/go-rod-master/SKILL.md) | Comprehensive guide for browser automation and web scraping with go-rod (Chrome DevTools Protocol) including stealth anti-bot-detection patterns. |
| [`golang-pro`](skills/golang-pro/SKILL.md) | Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices. |
| [`google-calendar-automation`](skills/google-calendar-automation/SKILL.md) | Lightweight Google Calendar integration with standalone OAuth authentication. No MCP server required. |
| [`google-docs-automation`](skills/google-docs-automation/SKILL.md) | Lightweight Google Docs integration with standalone OAuth authentication. No MCP server required. |
| [`google-drive-automation`](skills/google-drive-automation/SKILL.md) | Lightweight Google Drive integration with standalone OAuth authentication. No MCP server required. Full read/write access. |
| [`google-sheets-automation`](skills/google-sheets-automation/SKILL.md) | Lightweight Google Sheets integration with standalone OAuth authentication. No MCP server required. Full read/write access. |
| [`google-slides-automation`](skills/google-slides-automation/SKILL.md) | Lightweight Google Slides integration with standalone OAuth authentication. No MCP server required. Full read/write access. |
| [`graphql`](skills/graphql/SKILL.md) | You're a developer who has built GraphQL APIs at scale. You've seen the N+1 query problem bring down production servers. You've watched clients craft deeply nested queries that ... |
| [`haskell-pro`](skills/haskell-pro/SKILL.md) | Expert Haskell engineer specializing in advanced type systems, pure |
| [`hubspot-integration`](skills/hubspot-integration/SKILL.md) | Authentication for single-account integrations |
| [`incident-responder`](skills/incident-responder/SKILL.md) | Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management. |
| [`java-pro`](skills/java-pro/SKILL.md) | Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. Expert in the latest Java ecosystem including GraalVM, Project Loom, and cloud-... |
| [`javascript-pro`](skills/javascript-pro/SKILL.md) | Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility. |
| [`julia-pro`](skills/julia-pro/SKILL.md) | Master Julia 1.10+ with modern features, performance optimization, multiple dispatch, and production-ready practices. |
| [`laravel-security-audit`](skills/laravel-security-audit/SKILL.md) | Security auditor for Laravel applications. Analyzes code for vulnerabilities, misconfigurations, and insecure practices using OWASP standards and Laravel security best practices. |
| [`manifest`](skills/manifest/SKILL.md) | Install and configure the Manifest observability plugin for your agents. Use when setting up telemetry, configuring API keys, or troubleshooting the plugin. |
| [`metasploit-framework`](skills/metasploit-framework/SKILL.md) | ⚠️ AUTHORIZED USE ONLY > This skill is for educational purposes or authorized security assessments only. > You must have explicit, written permission from the system owner befor... |
| [`microsoft-azure-webjobs-extensions-authentication-events-dotnet`](skills/microsoft-azure-webjobs-extensions-authentication-events-dotnet/SKILL.md) | Microsoft Entra Authentication Events SDK for .NET. Azure Functions triggers for custom authentication extensions. |
| [`minecraft-bukkit-pro`](skills/minecraft-bukkit-pro/SKILL.md) | Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs. |
| [`monetization`](skills/monetization/SKILL.md) | Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments, freemium, upgrade flows, churn prevention, revenue optimization e ... |
| [`moodle-external-api-development`](skills/moodle-external-api-development/SKILL.md) | This skill guides you through creating custom external web service APIs for Moodle LMS, following Moodle's external API framework and coding standards. |
| [`mtls-configuration`](skills/mtls-configuration/SKILL.md) | Configure mutual TLS (mTLS) for zero-trust service-to-service communication. Use when implementing zero-trust networking, certificate management, or securing internal service co... |
| [`odoo-accounting-setup`](skills/odoo-accounting-setup/SKILL.md) | Expert guide for configuring Odoo Accounting: chart of accounts, journals, fiscal positions, taxes, payment terms, and bank reconciliation. |
| [`odoo-automated-tests`](skills/odoo-automated-tests/SKILL.md) | Write and run Odoo automated tests using TransactionCase, HttpCase, and browser tour tests. Covers test data setup, mocking, and CI integration. |
| [`odoo-docker-deployment`](skills/odoo-docker-deployment/SKILL.md) | Production-ready Docker and docker-compose setup for Odoo with PostgreSQL, persistent volumes, environment-based configuration, and Nginx reverse proxy. |
| [`odoo-hr-payroll-setup`](skills/odoo-hr-payroll-setup/SKILL.md) | Expert guide for Odoo HR and Payroll: salary structures, payslip rules, leave policies, employee contracts, and payroll journal entries. |
| [`odoo-inventory-optimizer`](skills/odoo-inventory-optimizer/SKILL.md) | Expert guide for Odoo Inventory: stock valuation (FIFO/AVCO), reordering rules, putaway strategies, routes, and multi-warehouse configuration. |
| [`odoo-l10n-compliance`](skills/odoo-l10n-compliance/SKILL.md) | Country-specific Odoo localization: tax configuration, e-invoicing (CFDI, FatturaPA, SAF-T), fiscal reporting, and country chart of accounts setup. |
| [`odoo-manufacturing-advisor`](skills/odoo-manufacturing-advisor/SKILL.md) | Expert guide for Odoo Manufacturing: Bills of Materials (BoM), Work Centers, routings, MRP planning, and production order workflows. |
| [`odoo-migration-helper`](skills/odoo-migration-helper/SKILL.md) | Step-by-step guide for migrating Odoo custom modules between versions (v14→v15→v16→v17). Covers API changes, deprecated methods, and view migration. |
| [`odoo-module-developer`](skills/odoo-module-developer/SKILL.md) | Expert guide for creating custom Odoo modules. Covers __manifest__.py, model inheritance, ORM patterns, and module structure best practices. |
| [`odoo-orm-expert`](skills/odoo-orm-expert/SKILL.md) | Master Odoo ORM patterns: search, browse, create, write, domain filters, computed fields, and performance-safe query techniques. |
| [`odoo-performance-tuner`](skills/odoo-performance-tuner/SKILL.md) | Expert guide for diagnosing and fixing Odoo performance issues: slow queries, worker configuration, memory limits, PostgreSQL tuning, and profiling tools. |
| [`odoo-project-timesheet`](skills/odoo-project-timesheet/SKILL.md) | Expert guide for Odoo Project and Timesheets: task stages, billable time tracking, timesheet approval, budget alerts, and invoicing from timesheets. |
| [`odoo-purchase-workflow`](skills/odoo-purchase-workflow/SKILL.md) | Expert guide for Odoo Purchase: RFQ → PO → Receipt → Vendor Bill workflow, purchase agreements, vendor price lists, and 3-way matching. |
| [`odoo-qweb-templates`](skills/odoo-qweb-templates/SKILL.md) | Expert in Odoo QWeb templating for PDF reports, email templates, and website pages. Covers t-if, t-foreach, t-field, and report actions. |
| [`odoo-sales-crm-expert`](skills/odoo-sales-crm-expert/SKILL.md) | Expert guide for Odoo Sales and CRM: pipeline stages, quotation templates, pricelists, sales teams, lead scoring, and forecasting. |
| [`odoo-security-rules`](skills/odoo-security-rules/SKILL.md) | Expert in Odoo access control: ir.model.access.csv, record rules (ir.rule), groups, and multi-company security patterns. |
| [`odoo-shopify-integration`](skills/odoo-shopify-integration/SKILL.md) | Connect Odoo with Shopify: sync products, inventory, orders, and customers using the Shopify API and Odoo's external API or connector modules. |
| [`odoo-upgrade-advisor`](skills/odoo-upgrade-advisor/SKILL.md) | Step-by-step Odoo version upgrade advisor: pre-upgrade checklist, community vs enterprise upgrade path, OCA module compatibility, and post-upgrade validation. |
| [`odoo-woocommerce-bridge`](skills/odoo-woocommerce-bridge/SKILL.md) | Sync Odoo with WooCommerce: products, inventory, orders, and customers via WooCommerce REST API and Odoo external API. |
| [`payment-integration`](skills/payment-integration/SKILL.md) | Integrate Stripe, PayPal, and payment processors. Handles checkout flows, subscriptions, webhooks, and PCI compliance. Use PROACTIVELY when implementing payments, billing, or su... |
| [`paypal-integration`](skills/paypal-integration/SKILL.md) | Master PayPal payment integration including Express Checkout, IPN handling, recurring billing, and refund workflows. |
| [`pci-compliance`](skills/pci-compliance/SKILL.md) | Master PCI DSS (Payment Card Industry Data Security Standard) compliance for secure payment processing and handling of cardholder data. |
| [`performance-optimizer`](skills/performance-optimizer/SKILL.md) | Identifies and fixes performance bottlenecks in code, databases, and APIs. Measures before and after to prove improvements. |
| [`php-pro`](skills/php-pro/SKILL.md) | Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features. Use PROACTIVELY for high-performance PHP applications. |
| [`plaid-fintech`](skills/plaid-fintech/SKILL.md) | Create a linktoken for Plaid Link, exchange publictoken for accesstoken. Link tokens are short-lived, one-time use. Access tokens don't expire but may need updating when users c... |
| [`polars`](skills/polars/SKILL.md) | Fast in-memory DataFrame library for datasets that fit in RAM. Use when pandas is too slow but data still fits in memory. Lazy evaluation, parallel execution, Apache Arrow backe... |
| [`popup-cro`](skills/popup-cro/SKILL.md) | Create and optimize popups, modals, overlays, slide-ins, and banners to increase conversions without harming user experience or brand trust. |
| [`projection-patterns`](skills/projection-patterns/SKILL.md) | Build read models and projections from event streams. Use when implementing CQRS read sides, building materialized views, or optimizing query performance in event-sourced systems. |
| [`pubmed-database`](skills/pubmed-database/SKILL.md) | Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workflows, prefer biopython (Bio.Entrez). Use... |
| [`pydantic-models-py`](skills/pydantic-models-py/SKILL.md) | Create Pydantic models following the multi-model pattern for clean API contracts. |
| [`python-fastapi-development`](skills/python-fastapi-development/SKILL.md) | Python FastAPI backend development with async patterns, SQLAlchemy, Pydantic, authentication, and production API patterns. |
| [`python-pro`](skills/python-pro/SKILL.md) | Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. Expert in the latest Python ecosystem including uv, ruff, ... |
| [`reference-builder`](skills/reference-builder/SKILL.md) | Creates exhaustive technical references and API documentation. Generates comprehensive parameter listings, configuration guides, and searchable reference materials. |
| [`returns-reverse-logistics`](skills/returns-reverse-logistics/SKILL.md) | Codified expertise for returns authorisation, receipt and inspection, disposition decisions, refund processing, fraud detection, and warranty claims management. |
| [`ruby-pro`](skills/ruby-pro/SKILL.md) | Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. Specializes in Ruby on Rails, gem development, and testing frameworks. |
| [`rust-async-patterns`](skills/rust-async-patterns/SKILL.md) | Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. Use when building async Rust applications, implementing concurrent systems, or d... |
| [`rust-pro`](skills/rust-pro/SKILL.md) | Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. |
| [`saga-orchestration`](skills/saga-orchestration/SKILL.md) | Patterns for managing distributed transactions and long-running business processes. |
| [`security-audit`](skills/security-audit/SKILL.md) | Comprehensive security auditing workflow covering web application testing, API security, penetration testing, vulnerability scanning, and security hardening. |
| [`seo-aeo-content-cluster`](skills/seo-aeo-content-cluster/SKILL.md) | Builds a topical authority map with a pillar page, prioritised cluster articles, content types, internal link map, and content gap analysis. Activate when the user wants to buil... |
| [`seo-authority-builder`](skills/seo-authority-builder/SKILL.md) | Analyzes content for E-E-A-T signals and suggests improvements to build authority and trust. Identifies missing credibility elements. Use PROACTIVELY for YMYL topics. |
| [`shopify-development`](skills/shopify-development/SKILL.md) | Build Shopify apps, extensions, themes using GraphQL Admin API, Shopify CLI, Polaris UI, and Liquid. |
| [`slack-bot-builder`](skills/slack-bot-builder/SKILL.md) | The Bolt framework is Slack's recommended approach for building apps. It handles authentication, event routing, request verification, and HTTP request processing so you can focu... |
| [`smtp-penetration-testing`](skills/smtp-penetration-testing/SKILL.md) | Conduct comprehensive security assessments of SMTP (Simple Mail Transfer Protocol) servers to identify vulnerabilities including open relays, user enumeration, weak authenticati... |
| [`social-orchestrator`](skills/social-orchestrator/SKILL.md) | Orquestrador unificado de canais sociais — coordena Instagram, Telegram e WhatsApp em um unico fluxo de trabalho. Publicacao cross-channel, metricas unificadas, reutilizacao de ... |
| [`square-automation`](skills/square-automation/SKILL.md) | Automate Square tasks via Rube MCP (Composio): payments, orders, invoices, locations. Always search tools first for current schemas. |
| [`stripe-automation`](skills/stripe-automation/SKILL.md) | Automate Stripe tasks via Rube MCP (Composio): customers, charges, subscriptions, invoices, products, refunds. Always search tools first for current schemas. |
| [`stripe-integration`](skills/stripe-integration/SKILL.md) | Master Stripe payment processing integration for robust, PCI-compliant payment flows including checkout, subscriptions, webhooks, and refunds. |
| [`tavily-web`](skills/tavily-web/SKILL.md) | Web search, content extraction, crawling, and research capabilities using Tavily API. Use when you need to search the web for current information, extracting content from URLs, ... |
| [`telegram`](skills/telegram/SKILL.md) | Integracao completa com Telegram Bot API. Setup com BotFather, mensagens, webhooks, inline keyboards, grupos, canais. Boilerplates Node.js e Python. |
| [`temporal-golang-pro`](skills/temporal-golang-pro/SKILL.md) | Use when building durable distributed systems with Temporal Go SDK. Covers deterministic workflow rules, mTLS worker configs, and advanced patterns. |
| [`temporal-python-pro`](skills/temporal-python-pro/SKILL.md) | Master Temporal workflow orchestration with Python SDK. Implements durable workflows, saga patterns, and distributed transactions. Covers async/await, testing strategies, and pr... |
| [`trigger-dev`](skills/trigger-dev/SKILL.md) | You are a Trigger.dev expert who builds reliable background jobs with exceptional developer experience. You understand that Trigger.dev bridges the gap between simple queues and... |
| [`trust-calibrator`](skills/trust-calibrator/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`twilio-communications`](skills/twilio-communications/SKILL.md) | Basic pattern for sending SMS messages with Twilio. Handles the fundamentals: phone number formatting, message delivery, and delivery status callbacks. |
| [`unreal-engine-cpp-pro`](skills/unreal-engine-cpp-pro/SKILL.md) | Expert guide for Unreal Engine 5.x C++ development, covering UObject hygiene, performance patterns, and best practices. |
| [`uv-package-manager`](skills/uv-package-manager/SKILL.md) | Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust, for modern Python project management and dependency workflows. |
| [`web-security-testing`](skills/web-security-testing/SKILL.md) | Web application security testing workflow for OWASP Top 10 vulnerabilities including injection, XSS, authentication flaws, and access control issues. |
| [`whatsapp-automation`](skills/whatsapp-automation/SKILL.md) | Automate WhatsApp Business tasks via Rube MCP (Composio): send messages, manage templates, upload media, and handle contacts. Always search tools first for current schemas. |
| [`whatsapp-cloud-api`](skills/whatsapp-cloud-api/SKILL.md) | Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates, webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Node.js e Python. |
| [`wordpress`](skills/wordpress/SKILL.md) | Complete WordPress development workflow covering theme development, plugin creation, WooCommerce integration, performance optimization, and security hardening. Includes WordPres... |
| [`wordpress-woocommerce-development`](skills/wordpress-woocommerce-development/SKILL.md) | WooCommerce store development workflow covering store setup, payment integration, shipping configuration, customization, and WordPress 7.0 features: AI connectors, DataViews, an... |
| [`zeroize-audit`](skills/zeroize-audit/SKILL.md) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verific... |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="cloud_devops"></a>
### ☁️ Cloud Computing, DevOps & Infraestrutura como Código
*Arquiteturas resilientes na AWS, Azure, GCP, Kubernetes, Docker, Terraform, Helm, GitOps e pipelines de CI/CD.* (106 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`007`](skills/007/SKILL.md) | Security audit, hardening, threat modeling (STRIDE/PASTA), Red/Blue Team, OWASP checks, code review, incident response, and infrastructure security for any project. |
| [`aws-cost-cleanup`](skills/aws-cost-cleanup/SKILL.md) | Automated cleanup of unused AWS resources to reduce costs |
| [`aws-cost-optimizer`](skills/aws-cost-optimizer/SKILL.md) | Comprehensive AWS cost analysis and optimization recommendations using AWS CLI and Cost Explorer |
| [`aws-penetration-testing`](skills/aws-penetration-testing/SKILL.md) | Provide comprehensive techniques for penetration testing AWS cloud environments. Covers IAM enumeration, privilege escalation, SSRF to metadata endpoint, S3 bucket exploitation,... |
| [`aws-serverless`](skills/aws-serverless/SKILL.md) | Proper Lambda function structure with error handling |
| [`azure-ai-agents-persistent-java`](skills/azure-ai-agents-persistent-java/SKILL.md) | Azure AI Agents Persistent SDK for Java. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| [`azure-ai-anomalydetector-java`](skills/azure-ai-anomalydetector-java/SKILL.md) | Build anomaly detection applications with Azure AI Anomaly Detector SDK for Java. Use when implementing univariate/multivariate anomaly detection, time-series analysis, or AI-po... |
| [`azure-ai-contentsafety-java`](skills/azure-ai-contentsafety-java/SKILL.md) | Build content moderation applications using the Azure AI Content Safety SDK for Java. |
| [`azure-ai-contentsafety-py`](skills/azure-ai-contentsafety-py/SKILL.md) | Azure AI Content Safety SDK for Python. Use for detecting harmful content in text and images with multi-severity classification. |
| [`azure-ai-contentsafety-ts`](skills/azure-ai-contentsafety-ts/SKILL.md) | Analyze text and images for harmful content with customizable blocklists. |
| [`azure-ai-contentunderstanding-py`](skills/azure-ai-contentunderstanding-py/SKILL.md) | Azure AI Content Understanding SDK for Python. Use for multimodal content extraction from documents, images, audio, and video. |
| [`azure-ai-document-intelligence-ts`](skills/azure-ai-document-intelligence-ts/SKILL.md) | Extract text, tables, and structured data from documents using prebuilt and custom models. |
| [`azure-ai-formrecognizer-java`](skills/azure-ai-formrecognizer-java/SKILL.md) | Build document analysis applications using the Azure AI Document Intelligence SDK for Java. |
| [`azure-ai-projects-java`](skills/azure-ai-projects-java/SKILL.md) | Azure AI Projects SDK for Java. High-level SDK for Azure AI Foundry project management including connections, datasets, indexes, and evaluations. |
| [`azure-ai-projects-py`](skills/azure-ai-projects-py/SKILL.md) | Build AI applications on Microsoft Foundry using the azure-ai-projects SDK. |
| [`azure-ai-projects-ts`](skills/azure-ai-projects-ts/SKILL.md) | High-level SDK for Azure AI Foundry projects with agents, connections, deployments, and evaluations. |
| [`azure-ai-textanalytics-py`](skills/azure-ai-textanalytics-py/SKILL.md) | Azure AI Text Analytics SDK for sentiment analysis, entity recognition, key phrases, language detection, PII, and healthcare NLP. Use for natural language processing on text. |
| [`azure-ai-transcription-py`](skills/azure-ai-transcription-py/SKILL.md) | Azure AI Transcription SDK for Python. Use for real-time and batch speech-to-text transcription with timestamps and diarization. |
| [`azure-ai-translation-document-py`](skills/azure-ai-translation-document-py/SKILL.md) | Azure AI Document Translation SDK for batch translation of documents with format preservation. Use for translating Word, PDF, Excel, PowerPoint, and other document formats at sc... |
| [`azure-ai-translation-text-py`](skills/azure-ai-translation-text-py/SKILL.md) | Azure AI Text Translation SDK for real-time text translation, transliteration, language detection, and dictionary lookup. Use for translating text content in applications. |
| [`azure-ai-translation-ts`](skills/azure-ai-translation-ts/SKILL.md) | Text and document translation with REST-style clients. |
| [`azure-ai-vision-imageanalysis-java`](skills/azure-ai-vision-imageanalysis-java/SKILL.md) | Build image analysis applications with Azure AI Vision SDK for Java. Use when implementing image captioning, OCR text extraction, object detection, tagging, or smart cropping. |
| [`azure-ai-vision-imageanalysis-py`](skills/azure-ai-vision-imageanalysis-py/SKILL.md) | Azure AI Vision Image Analysis SDK for captions, tags, objects, OCR, people detection, and smart cropping. Use for computer vision and image understanding tasks. |
| [`azure-appconfiguration-java`](skills/azure-appconfiguration-java/SKILL.md) | Azure App Configuration SDK for Java. Centralized application configuration management with key-value settings, feature flags, and snapshots. |
| [`azure-appconfiguration-py`](skills/azure-appconfiguration-py/SKILL.md) | Azure App Configuration SDK for Python. Use for centralized configuration management, feature flags, and dynamic settings. |
| [`azure-appconfiguration-ts`](skills/azure-appconfiguration-ts/SKILL.md) | Centralized configuration management with feature flags and dynamic refresh. |
| [`azure-communication-callautomation-java`](skills/azure-communication-callautomation-java/SKILL.md) | Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions. |
| [`azure-communication-callingserver-java`](skills/azure-communication-callingserver-java/SKILL.md) | ⚠️ DEPRECATED: This SDK has been renamed to Call Automation. For new projects, use azure-communication-callautomation instead. This skill is for maintaining legacy code only. |
| [`azure-communication-chat-java`](skills/azure-communication-chat-java/SKILL.md) | Build real-time chat applications with thread management, messaging, participants, and read receipts. |
| [`azure-communication-sms-java`](skills/azure-communication-sms-java/SKILL.md) | Send SMS messages with Azure Communication Services SMS Java SDK. Use when implementing SMS notifications, alerts, OTP delivery, bulk messaging, or delivery reports. |
| [`azure-compute-batch-java`](skills/azure-compute-batch-java/SKILL.md) | Azure Batch SDK for Java. Run large-scale parallel and HPC batch jobs with pools, jobs, tasks, and compute nodes. |
| [`azure-containerregistry-py`](skills/azure-containerregistry-py/SKILL.md) | Azure Container Registry SDK for Python. Use for managing container images, artifacts, and repositories. |
| [`azure-cosmos-db-py`](skills/azure-cosmos-db-py/SKILL.md) | Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles. |
| [`azure-cosmos-ts`](skills/azure-cosmos-ts/SKILL.md) | Azure Cosmos DB JavaScript/TypeScript SDK (@azure/cosmos) for data plane operations. Use for CRUD operations on documents, queries, bulk operations, and container management. |
| [`azure-eventgrid-java`](skills/azure-eventgrid-java/SKILL.md) | Build event-driven applications with Azure Event Grid SDK for Java. Use when publishing events, implementing pub/sub patterns, or integrating with Azure services via events. |
| [`azure-eventhub-py`](skills/azure-eventhub-py/SKILL.md) | Azure Event Hubs SDK for Python streaming. Use for high-throughput event ingestion, producers, consumers, and checkpointing. |
| [`azure-eventhub-ts`](skills/azure-eventhub-ts/SKILL.md) | High-throughput event streaming and real-time data ingestion. |
| [`azure-keyvault-keys-ts`](skills/azure-keyvault-keys-ts/SKILL.md) | Manage cryptographic keys using Azure Key Vault Keys SDK for JavaScript (@azure/keyvault-keys). Use when creating, encrypting/decrypting, signing, or rotating keys. |
| [`azure-keyvault-secrets-ts`](skills/azure-keyvault-secrets-ts/SKILL.md) | Manage secrets using Azure Key Vault Secrets SDK for JavaScript (@azure/keyvault-secrets). Use when storing and retrieving application secrets or configuration values. |
| [`azure-mgmt-botservice-py`](skills/azure-mgmt-botservice-py/SKILL.md) | Azure Bot Service Management SDK for Python. Use for creating, managing, and configuring Azure Bot Service resources. |
| [`azure-mgmt-fabric-py`](skills/azure-mgmt-fabric-py/SKILL.md) | Azure Fabric Management SDK for Python. Use for managing Microsoft Fabric capacities and resources. |
| [`azure-microsoft-playwright-testing-ts`](skills/azure-microsoft-playwright-testing-ts/SKILL.md) | Run Playwright tests at scale with cloud-hosted browsers and integrated Azure portal reporting. |
| [`azure-monitor-ingestion-java`](skills/azure-monitor-ingestion-java/SKILL.md) | Azure Monitor Ingestion SDK for Java. Send custom logs to Azure Monitor via Data Collection Rules (DCR) and Data Collection Endpoints (DCE). |
| [`azure-monitor-opentelemetry-py`](skills/azure-monitor-opentelemetry-py/SKILL.md) | Azure Monitor OpenTelemetry Distro for Python. Use for one-line Application Insights setup with auto-instrumentation. |
| [`azure-monitor-query-java`](skills/azure-monitor-query-java/SKILL.md) | Azure Monitor Query SDK for Java. Execute Kusto queries against Log Analytics workspaces and query metrics from Azure resources. |
| [`azure-monitor-query-py`](skills/azure-monitor-query-py/SKILL.md) | Azure Monitor Query SDK for Python. Use for querying Log Analytics workspaces and Azure Monitor metrics. |
| [`azure-search-documents-py`](skills/azure-search-documents-py/SKILL.md) | Azure AI Search SDK for Python. Use for vector search, hybrid search, semantic ranking, indexing, and skillsets. |
| [`azure-search-documents-ts`](skills/azure-search-documents-ts/SKILL.md) | Build search applications with vector, hybrid, and semantic search capabilities. |
| [`azure-security-keyvault-keys-java`](skills/azure-security-keyvault-keys-java/SKILL.md) | Azure Key Vault Keys Java SDK for cryptographic key management. Use when creating, managing, or using RSA/EC keys, performing encrypt/decrypt/sign/verify operations, or working ... |
| [`azure-servicebus-py`](skills/azure-servicebus-py/SKILL.md) | Azure Service Bus SDK for Python messaging. Use for queues, topics, subscriptions, and enterprise messaging patterns. |
| [`azure-servicebus-ts`](skills/azure-servicebus-ts/SKILL.md) | Enterprise messaging with queues, topics, and subscriptions. |
| [`bash-defensive-patterns`](skills/bash-defensive-patterns/SKILL.md) | Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or system utilities requiring fault tolerance ... |
| [`bash-pro`](skills/bash-pro/SKILL.md) | Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities. Expert in safe, portable, and testable shell scripts. |
| [`bats-testing-patterns`](skills/bats-testing-patterns/SKILL.md) | Master Bash Automated Testing System (Bats) for comprehensive shell script testing. Use when writing tests for shell scripts, CI/CD pipelines, or requiring test-driven developme... |
| [`circleci-automation`](skills/circleci-automation/SKILL.md) | Automate CircleCI tasks via Rube MCP (Composio): trigger pipelines, monitor workflows/jobs, retrieve artifacts and test metadata. Always search tools first for current schemas. |
| [`cloud-devops`](skills/cloud-devops/SKILL.md) | Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring, and cloud-native development. |
| [`cloud-penetration-testing`](skills/cloud-penetration-testing/SKILL.md) | Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP). |
| [`cloudformation-best-practices`](skills/cloudformation-best-practices/SKILL.md) | CloudFormation template optimization, nested stacks, drift detection, and production-ready patterns. Use when writing or reviewing CF templates. |
| [`cost-optimization`](skills/cost-optimization/SKILL.md) | Strategies and patterns for optimizing cloud costs across AWS, Azure, and GCP. |
| [`database-admin`](skills/database-admin/SKILL.md) | Expert database administrator specializing in modern cloud databases, automation, and reliability engineering. |
| [`database-migrations-migration-observability`](skills/database-migrations-migration-observability/SKILL.md) | Migration monitoring, CDC, and observability infrastructure |
| [`deployment-engineer`](skills/deployment-engineer/SKILL.md) | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. |
| [`devops-deploy`](skills/devops-deploy/SKILL.md) | DevOps e deploy de aplicacoes — Docker, CI/CD com GitHub Actions, AWS Lambda, SAM, Terraform, infraestrutura como codigo e monitoramento. |
| [`discovering-gcp-data-assets`](skills/discovering-gcp-data-assets/SKILL.md) | \| Finds and inspects data assets within Google Cloud. Relevant when any of the following conditions are true: 1. The user request involves finding, exploring, or inspecting dat... |
| [`docker-expert`](skills/docker-expert/SKILL.md) | You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization, security hardening, multi-stage builds, orchestration patte... |
| [`e2e-testing`](skills/e2e-testing/SKILL.md) | End-to-end testing workflow with Playwright for browser automation, visual regression, cross-browser testing, and CI/CD integration. |
| [`enforcing-resource-attribution`](skills/enforcing-resource-attribution/SKILL.md) | Enforces resource attribution for CLI commands. Use this skill whenever you are running `bq` or `gcloud` commands via `run_command`. It ensures mandatory labeling for supported ... |
| [`federate-lakehouse-catalog`](skills/federate-lakehouse-catalog/SKILL.md) | Sets up Google Cloud Lakehouse federated catalogs to remote Iceberg REST Catalogs. Currently supported catalogs: Databricks Unity, AWS Glue. Supported clouds hosting those catal... |
| [`gcp-composer-troubleshooting`](skills/gcp-composer-troubleshooting/SKILL.md) | Provides expert guidance for troubleshooting Cloud Composer (Apache Airflow) and Orchestration pipelines. Use this skill when the user asks to generate Root Cause Analysis (RCA)... |
| [`gcp-data-pipelines`](skills/gcp-data-pipelines/SKILL.md) | Primary entry point for building, managing, and orchestrating data pipelines on Google Cloud. Guides users to the appropriate skill for dbt, Dataflow (Apache Beam), Dataform, Sp... |
| [`gcp-dataflow`](skills/gcp-dataflow/SKILL.md) | \| Guides writing, packaging, executing, and troubleshooting Apache Beam pipelines on Dataflow. Use when creating new pipelines, configuring Flex Templates, or analyzing perform... |
| [`gcp-managed-airflow-migrations`](skills/gcp-managed-airflow-migrations/SKILL.md) | Provides guidance for migrating Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers migration to Airflow 2.11.1 (MSAA Gen 2 and 3) ... |
| [`gcp-pipeline-orchestration`](skills/gcp-pipeline-orchestration/SKILL.md) | This skill helps the agent generate or update orchestration pipeline definitions for Google Cloud Composer to initialize orchestration pipeline or update the orchestration defin... |
| [`gcp-pipeline-resource-provisioning`](skills/gcp-pipeline-resource-provisioning/SKILL.md) | \| Automates declarative resource creation and provisioning for data pipelines, supporting BigQuery, Dataform, Dataproc, BigQuery Data Transfer Service (DTS), and other resource... |
| [`gcp-spark`](skills/gcp-spark/SKILL.md) | \| Develops and executes Spark code on Dataproc Clusters and Serverless. Reads and writes data using BigLake Iceberg catalogs, BigQuery and Spanner. Debugs execution failures. U... |
| [`github-actions-templates`](skills/github-actions-templates/SKILL.md) | Production-ready GitHub Actions workflow patterns for testing, building, and deploying applications. |
| [`github-automation`](skills/github-automation/SKILL.md) | Automate GitHub repositories, issues, pull requests, branches, CI/CD, and permissions via Rube MCP (Composio). Manage code workflows, review PRs, search code, and handle deploym... |
| [`gitlab-ci-patterns`](skills/gitlab-ci-patterns/SKILL.md) | Comprehensive GitLab CI/CD pipeline patterns for automated testing, building, and deployment. |
| [`gitops-workflow`](skills/gitops-workflow/SKILL.md) | Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments. |
| [`helm-chart-scaffolding`](skills/helm-chart-scaffolding/SKILL.md) | Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications. |
| [`hybrid-cloud-networking`](skills/hybrid-cloud-networking/SKILL.md) | Configure secure, high-performance connectivity between on-premises and cloud environments using VPN, Direct Connect, and ExpressRoute. |
| [`inngest`](skills/inngest/SKILL.md) | You are an Inngest expert who builds reliable background processing without managing infrastructure. You understand that serverless doesn't mean you can't have durable, long-run... |
| [`istio-traffic-management`](skills/istio-traffic-management/SKILL.md) | Comprehensive guide to Istio traffic management for production service mesh deployments. |
| [`k8s-security-policies`](skills/k8s-security-policies/SKILL.md) | Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes. |
| [`kubernetes-deployment`](skills/kubernetes-deployment/SKILL.md) | Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations. |
| [`linkerd-patterns`](skills/linkerd-patterns/SKILL.md) | Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes. |
| [`render-automation`](skills/render-automation/SKILL.md) | Automate Render tasks via Rube MCP (Composio): services, deployments, projects. Always search tools first for current schemas. |
| [`secrets-management`](skills/secrets-management/SKILL.md) | Secure secrets management practices for CI/CD pipelines using Vault, AWS Secrets Manager, and other tools. |
| [`security-scanning-security-hardening`](skills/security-scanning-security-hardening/SKILL.md) | Coordinate multi-layer security scanning and hardening across application, infrastructure, and compliance controls. |
| [`seo-technical`](skills/seo-technical/SKILL.md) | Audit technical SEO across crawlability, indexability, security, URLs, mobile, Core Web Vitals, structured data, JavaScript rendering, and related platform signals like robots.t... |
| [`server-management`](skills/server-management/SKILL.md) | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands. |
| [`service-mesh-observability`](skills/service-mesh-observability/SKILL.md) | Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments. |
| [`shellcheck-configuration`](skills/shellcheck-configuration/SKILL.md) | Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing code issues, or ensuring script portability. |
| [`skill-creator-ms`](skills/skill-creator-ms/SKILL.md) | Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. Use when creating new skills or updating existing skills. |
| [`sql-injection-testing`](skills/sql-injection-testing/SKILL.md) | Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate exploitation techniques, and validate input sa... |
| [`sql-pro`](skills/sql-pro/SKILL.md) | Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. Expert in performance tuning, data modeling, and hybrid analytical systems. |
| [`terraform-aws-modules`](skills/terraform-aws-modules/SKILL.md) | Terraform module creation for AWS — reusable modules, state management, and HCL best practices. Use when building or reviewing Terraform AWS infrastructure. |
| [`terraform-infrastructure`](skills/terraform-infrastructure/SKILL.md) | Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules, and managing infrastructure at scale. |
| [`terraform-module-library`](skills/terraform-module-library/SKILL.md) | Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure. |
| [`terraform-skill`](skills/terraform-skill/SKILL.md) | Terraform infrastructure as code best practices |
| [`terraform-specialist`](skills/terraform-specialist/SKILL.md) | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. |
| [`test-automator`](skills/test-automator/SKILL.md) | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing strategies with advanced CI/CD integr... |
| [`unity-developer`](skills/unity-developer/SKILL.md) | Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. Masters Unity 6 LTS, URP/HDRP pipelines, and cross-platform deployment. |
| [`upstash-qstash`](skills/upstash-qstash/SKILL.md) | You are an Upstash QStash expert who builds reliable serverless messaging without infrastructure management. You understand that QStash's simplicity is its power - HTTP in, HTTP... |
| [`vector-index-tuning`](skills/vector-index-tuning/SKILL.md) | Optimize vector index performance for latency, recall, and memory. Use when tuning HNSW parameters, selecting quantization strategies, or scaling vector search infrastructure. |
| [`x-twitter-scraper`](skills/x-twitter-scraper/SKILL.md) | X (Twitter) data platform skill — tweet search, user lookup, follower extraction, engagement metrics, giveaway draws, monitoring, webhooks, 19 extraction tools, MCP server. |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="database_data"></a>
### 🗄️ Bancos de Dados, Cache & Engenharia de Dados
*Modelagem, queries e otimização para PostgreSQL, MySQL, Redis, CosmosDB, BigQuery, Snowflake, Neon, Prisma e dbt.* (31 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`airflow-dag-patterns`](skills/airflow-dag-patterns/SKILL.md) | Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. Use when creating data pipelines, orchestrating workflows, or schedulin... |
| [`bigquery-graph`](skills/bigquery-graph/SKILL.md) | Provides guidelines and best practices for querying and defining property graphs and semantic graphs in BigQuery using GQL (Graph Query Language). Use when creating property gra... |
| [`biopython`](skills/biopython/SKILL.md) | Biopython is a comprehensive set of freely available Python tools for biological computation. It provides functionality for sequence manipulation, file I/O, database access, str... |
| [`business-analyst`](skills/business-analyst/SKILL.md) | Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. Build comprehensive KPI frameworks, predictive models, and strategic r... |
| [`cc-skill-clickhouse-io`](skills/cc-skill-clickhouse-io/SKILL.md) | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. |
| [`claimable-postgres`](skills/claimable-postgres/SKILL.md) | Provision instant temporary Postgres databases via Claimable Postgres by Neon (pg.new). No login or credit card required. Use for quick Postgres environments and throwaway DATAB... |
| [`content-marketer`](skills/content-marketer/SKILL.md) | Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimization, and data-driven performance marketing. |
| [`context-manager`](skills/context-manager/SKILL.md) | Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory systems. |
| [`data-engineering-data-driven-feature`](skills/data-engineering-data-driven-feature/SKILL.md) | Build features guided by data insights, A/B testing, and continuous measurement using specialized agents for analysis, implementation, and experimentation. |
| [`data-quality-frameworks`](skills/data-quality-frameworks/SKILL.md) | Implement data quality validation with Great Expectations, dbt tests, and data contracts. Use when building data quality pipelines, implementing validation rules, or establishin... |
| [`data-scientist`](skills/data-scientist/SKILL.md) | Expert data scientist for advanced analytics, machine learning, and statistical modeling. Handles complex data analysis, predictive modeling, and business intelligence. |
| [`data-storytelling`](skills/data-storytelling/SKILL.md) | Transform raw data into compelling narratives that drive decisions and inspire action. |
| [`database-migration`](skills/database-migration/SKILL.md) | Master database schema and data migrations across ORMs (Sequelize, TypeORM, Prisma), including rollback strategies and zero-downtime deployments. |
| [`database-migrations-sql-migrations`](skills/database-migrations-sql-migrations/SKILL.md) | SQL database migrations with zero-downtime strategies for PostgreSQL, MySQL, and SQL Server. Focus on data integrity and rollback plans. |
| [`dataform-bigquery`](skills/dataform-bigquery/SKILL.md) | Expertise in generating clean, correct, and efficient Dataform pipeline code for BigQuery ELT. Use this when creating or modifying Dataform pipelines, actions, or source declara... |
| [`dbt-bigquery`](skills/dbt-bigquery/SKILL.md) | Expert guidance for creating, modifying, and optimizing dbt pipelines for BigQuery. Use this skill whenever user asks for generating or modifying a dbt model or project. Activat... |
| [`dbt-transformation-patterns`](skills/dbt-transformation-patterns/SKILL.md) | Production-ready patterns for dbt (data build tool) including model organization, testing strategies, documentation, and incremental processing. |
| [`debug-buttercup`](skills/debug-buttercup/SKILL.md) | All pods run in namespace crs. Use when pods in the crs namespace are in CrashLoopBackOff, OOMKilled, or restarting, multiple services restart simultaneously (cascade failure), ... |
| [`food-database-query`](skills/food-database-query/SKILL.md) | Food Database Query |
| [`gdpr-data-handling`](skills/gdpr-data-handling/SKILL.md) | Practical implementation guide for GDPR-compliant data processing, consent management, and privacy controls. |
| [`managing-python-dependencies`](skills/managing-python-dependencies/SKILL.md) | \| Ensures proper Python dependency management, avoiding global `pip install` and adhering to project-specific tooling. Use this skill if any of the following are true: 1. Attem... |
| [`neon-postgres`](skills/neon-postgres/SKILL.md) | Configure Prisma for Neon with connection pooling. |
| [`notebook-guidance`](skills/notebook-guidance/SKILL.md) | \|- This skill guides the use of Jupyter notebooks for data analysis, exploration, and visualization, particularly with BigQuery. It outlines best practices for notebook executi... |
| [`notion-automation`](skills/notion-automation/SKILL.md) | Automate Notion tasks via Rube MCP (Composio): pages, databases, blocks, comments, users. Always search tools first for current schemas. |
| [`obsidian-bases`](skills/obsidian-bases/SKILL.md) | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating database-like views of notes, or when the ... |
| [`postgresql-optimization`](skills/postgresql-optimization/SKILL.md) | PostgreSQL database optimization workflow for query tuning, indexing strategies, performance analysis, and production database management. |
| [`similarity-search-patterns`](skills/similarity-search-patterns/SKILL.md) | Implement efficient similarity search with vector databases. Use when building semantic search, implementing nearest neighbor queries, or optimizing retrieval performance. |
| [`spark-optimization`](skills/spark-optimization/SKILL.md) | Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. Use when improving Spark performance, debugging slow jobs, or scaling data proces... |
| [`sql-optimization-patterns`](skills/sql-optimization-patterns/SKILL.md) | Transform slow database queries into lightning-fast operations through systematic optimization, proper indexing, and query plan analysis. |
| [`sqlmap-database-pentesting`](skills/sqlmap-database-pentesting/SKILL.md) | Provide systematic methodologies for automated SQL injection detection and exploitation using SQLMap. |
| [`unity-ecs-patterns`](skills/unity-ecs-patterns/SKILL.md) | Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System, and Burst Compiler. |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="security_pentest"></a>
### 🛡️ Segurança da Informação, Pentest & Red Team
*Auditorias de segurança, exploração OWASP (IDOR, XSS, SQLi), bypass, pentest web/cloud, privilege escalation e DevSecOps.* (47 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`active-directory-attacks`](skills/active-directory-attacks/SKILL.md) | Provide comprehensive techniques for attacking Microsoft Active Directory environments. Covers reconnaissance, credential harvesting, Kerberos attacks, lateral movement, privile... |
| [`advogado-especialista`](skills/advogado-especialista/SKILL.md) | Advogado especialista em todas as areas do Direito brasileiro: familia, criminal, trabalhista, tributario, consumidor, imobiliario, empresarial, civil e constitucional. |
| [`antigravity-workflows`](skills/antigravity-workflows/SKILL.md) | Orchestrate multiple Antigravity skills through guided workflows for SaaS MVP delivery, security audits, AI agent builds, and browser QA. |
| [`burp-suite-testing`](skills/burp-suite-testing/SKILL.md) | Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic interception and modification, request analysis and replay, ... |
| [`burpsuite-project-parser`](skills/burpsuite-project-parser/SKILL.md) | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findin... |
| [`codebase-cleanup-deps-audit`](skills/codebase-cleanup-deps-audit/SKILL.md) | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependencies for known vulnerabilitie... |
| [`cred-omega`](skills/cred-omega/SKILL.md) | CISO operacional enterprise para gestao total de credenciais e segredos. |
| [`dependency-management-deps-audit`](skills/dependency-management-deps-audit/SKILL.md) | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependencies for known vulnerabilitie... |
| [`differential-review`](skills/differential-review/SKILL.md) | Security-focused code review for PRs, commits, and diffs. |
| [`file-path-traversal`](skills/file-path-traversal/SKILL.md) | Identify and exploit file path traversal (directory traversal) vulnerabilities that allow attackers to read arbitrary files on the server, potentially including sensitive config... |
| [`find-bugs`](skills/find-bugs/SKILL.md) | Find bugs, security vulnerabilities, and code quality issues in local branch changes. Use when asked to review changes, find bugs, security review, or audit code on the current ... |
| [`firebase`](skills/firebase/SKILL.md) | You're a developer who has shipped dozens of Firebase projects. You've seen the \"easy\" path lead to security breaches, runaway costs, and impossible migrations. You know Fireb... |
| [`gha-security-review`](skills/gha-security-review/SKILL.md) | Find exploitable vulnerabilities in GitHub Actions workflows. Every finding MUST include a concrete exploitation scenario — if you can't build the attack, don't report it. |
| [`gsd-ns-review`](skills/gsd-ns-review/SKILL.md) | quality gates \| code review debug audit security eval ui |
| [`gsd-secure-phase`](skills/gsd-secure-phase/SKILL.md) | Retroactively verify threat mitigations for a completed phase |
| [`idor-testing`](skills/idor-testing/SKILL.md) | Provide systematic methodologies for identifying and exploiting Insecure Direct Object Reference (IDOR) vulnerabilities in web applications. |
| [`legal-advisor`](skills/legal-advisor/SKILL.md) | Draft privacy policies, terms of service, disclaimers, and legal notices. Creates GDPR-compliant texts, cookie policies, and data processing agreements. |
| [`linux-privilege-escalation`](skills/linux-privilege-escalation/SKILL.md) | Execute systematic privilege escalation assessments on Linux systems to identify and exploit misconfigurations, vulnerable services, and security weaknesses that allow elevation... |
| [`linux-shell-scripting`](skills/linux-shell-scripting/SKILL.md) | Provide production-ready shell script templates for common Linux system administration tasks including backups, monitoring, user management, log analysis, and automation. These ... |
| [`malware-analyst`](skills/malware-analyst/SKILL.md) | Expert malware analyst specializing in defensive malware research, threat intelligence, and incident response. Masters sandbox analysis, behavioral analysis, and malware family ... |
| [`memory-forensics`](skills/memory-forensics/SKILL.md) | Comprehensive techniques for acquiring, analyzing, and extracting artifacts from memory dumps for incident response and malware analysis. |
| [`mobile-security-coder`](skills/mobile-security-coder/SKILL.md) | Expert in secure mobile coding practices specializing in input validation, WebView security, and mobile-specific security patterns. |
| [`network-101`](skills/network-101/SKILL.md) | Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice with service enumeration, log analysis, an... |
| [`pentest-checklist`](skills/pentest-checklist/SKILL.md) | Provide a comprehensive checklist for planning, executing, and following up on penetration tests. Ensure thorough preparation, proper scoping, and effective remediation of disco... |
| [`pentest-commands`](skills/pentest-commands/SKILL.md) | Provide a comprehensive command reference for penetration testing tools including network scanning, exploitation, password cracking, and web application testing. Enable quick co... |
| [`privilege-escalation-methods`](skills/privilege-escalation-methods/SKILL.md) | Provide comprehensive techniques for escalating privileges from a low-privileged user to root/administrator access on compromised Linux and Windows systems. Essential for penetr... |
| [`red-team-tactics`](skills/red-team-tactics/SKILL.md) | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. |
| [`sast-configuration`](skills/sast-configuration/SKILL.md) | Static Application Security Testing (SAST) tool setup, configuration, and custom rule creation for comprehensive security scanning across multiple programming languages. |
| [`scanning-tools`](skills/scanning-tools/SKILL.md) | Master essential security scanning tools for network discovery, vulnerability assessment, web application testing, wireless security, and compliance validation. This skill cover... |
| [`security-auditor`](skills/security-auditor/SKILL.md) | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. |
| [`security-bluebook-builder`](skills/security-bluebook-builder/SKILL.md) | Build a minimal but real security policy for sensitive apps. The output is a single, coherent Blue Book document using MUST/SHOULD/CAN language, with explicit assumptions, scope... |
| [`security-compliance-compliance-check`](skills/security-compliance-compliance-check/SKILL.md) | You are a compliance expert specializing in regulatory requirements for software systems including GDPR, HIPAA, SOC2, PCI-DSS, and other industry standards. Perform comprehensiv... |
| [`security-requirement-extraction`](skills/security-requirement-extraction/SKILL.md) | Derive security requirements from threat models and business context. Use when translating threats into actionable requirements, creating security user stories, or building secu... |
| [`security-scanning-security-dependencies`](skills/security-scanning-security-dependencies/SKILL.md) | You are a security expert specializing in dependency vulnerability analysis, SBOM generation, and supply chain security. Scan project dependencies across multiple ecosystems to ... |
| [`security-scanning-security-sast`](skills/security-scanning-security-sast/SKILL.md) | Static Application Security Testing (SAST) for code vulnerability analysis across multiple languages and frameworks |
| [`semgrep-rule-creator`](skills/semgrep-rule-creator/SKILL.md) | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. |
| [`semgrep-rule-variant-creator`](skills/semgrep-rule-variant-creator/SKILL.md) | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produce... |
| [`solidity-security`](skills/solidity-security/SKILL.md) | Master smart contract security best practices, vulnerability prevention, and secure Solidity development patterns. |
| [`ssh-penetration-testing`](skills/ssh-penetration-testing/SKILL.md) | Conduct comprehensive SSH security assessments including enumeration, credential attacks, vulnerability exploitation, tunneling techniques, and post-exploitation activities. Thi... |
| [`stride-analysis-patterns`](skills/stride-analysis-patterns/SKILL.md) | Apply STRIDE methodology to systematically identify threats. Use when analyzing system security, conducting threat modeling sessions, or creating security documentation. |
| [`supply-chain-risk-auditor`](skills/supply-chain-risk-auditor/SKILL.md) | Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagem... |
| [`threat-mitigation-mapping`](skills/threat-mitigation-mapping/SKILL.md) | Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediation plans, or validating control effectiven... |
| [`top-web-vulnerabilities`](skills/top-web-vulnerabilities/SKILL.md) | Provide a comprehensive, structured reference for the 100 most critical web application vulnerabilities organized by category. This skill enables systematic vulnerability identi... |
| [`variant-analysis`](skills/variant-analysis/SKILL.md) | Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabi... |
| [`vulnerability-scanner`](skills/vulnerability-scanner/SKILL.md) | Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization. |
| [`warren-buffett`](skills/warren-buffett/SKILL.md) | Agente que simula Warren Buffett — o maior investidor do seculo XX e XXI, CEO da Berkshire Hathaway, discipulo de Benjamin Graham e socio intelectual de Charlie Munger. |
| [`wordpress-penetration-testing`](skills/wordpress-penetration-testing/SKILL.md) | Assess WordPress installations for common vulnerabilities and WordPress 7.0 attack surfaces. |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="testing_observability"></a>
### 📊 Testes Automatizados, TDD & Observabilidade
*Ciclos TDD (Red-Green-Refactor), testes E2E com Playwright, testes de carga K6, monitoramento Prometheus, Grafana e Jaeger.* (116 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`ab-test-setup`](skills/ab-test-setup/SKILL.md) | Structured guide for setting up A/B tests with mandatory gates for hypothesis, metrics, and execution readiness. |
| [`ad-creative`](skills/ad-creative/SKILL.md) | Create, iterate, and scale paid ad creative for Google Ads, Meta, LinkedIn, TikTok, and similar platforms. Use when generating headlines, descriptions, primary text, or large se... |
| [`async-python-patterns`](skills/async-python-patterns/SKILL.md) | Comprehensive guidance for implementing asynchronous Python applications using asyncio, concurrent programming patterns, and async/await for building high-performance, non-block... |
| [`avoid-ai-writing`](skills/avoid-ai-writing/SKILL.md) | Audit and rewrite content to remove 21 categories of AI writing patterns with a 43-entry replacement table |
| [`backtesting-frameworks`](skills/backtesting-frameworks/SKILL.md) | Build robust, production-grade backtesting systems that avoid common pitfalls and produce reliable strategy performance estimates. |
| [`bash-scripting`](skills/bash-scripting/SKILL.md) | Bash scripting workflow for creating production-ready shell scripts with defensive patterns, error handling, and testing. |
| [`bazel-build-optimization`](skills/bazel-build-optimization/SKILL.md) | Optimize Bazel builds for large-scale monorepos. Use when configuring Bazel, implementing remote execution, or optimizing build performance for enterprise codebases. |
| [`blog-writing-guide`](skills/blog-writing-guide/SKILL.md) | This skill enforces Sentry's blog writing standards across every post — whether you're helping an engineer write their first blog post or a marketer draft a product announcement. |
| [`brand-guidelines`](skills/brand-guidelines/SKILL.md) | Write copy following Sentry brand guidelines. Use when writing UI text, error messages, empty states, onboarding flows, 404 pages, documentation, marketing copy, or any user-fac... |
| [`browser-automation`](skills/browser-automation/SKILL.md) | You are a browser automation expert who has debugged thousands of flaky tests and built scrapers that run for years without breaking. You've seen the evolution from Selenium to ... |
| [`bug-hunter`](skills/bug-hunter/SKILL.md) | Systematically finds and fixes bugs using proven debugging techniques. Traces from symptoms to root cause, implements fixes, and prevents regression. |
| [`commit`](skills/commit/SKILL.md) | ALWAYS use this skill when committing code changes — never commit directly without it. Creates commits following Sentry conventions with proper conventional commit format and is... |
| [`conductor-implement`](skills/conductor-implement/SKILL.md) | Execute tasks from a track's implementation plan following TDD workflow |
| [`create-branch`](skills/create-branch/SKILL.md) | Create a git branch following Sentry naming conventions. Use when asked to "create a branch", "new branch", "start a branch", "make a branch", "switch to a new branch", or when ... |
| [`create-pr`](skills/create-pr/SKILL.md) | Alias for sentry-skills:pr-writer. Use when users explicitly ask for "create-pr" or reference the legacy skill name. Redirects to the canonical PR writing workflow. |
| [`crypto-bd-agent`](skills/crypto-bd-agent/SKILL.md) | Production-tested patterns for building AI agents that autonomously discover, > evaluate, and acquire token listings for cryptocurrency exchanges. |
| [`datadog-automation`](skills/datadog-automation/SKILL.md) | Automate Datadog tasks via Rube MCP (Composio): query metrics, search logs, manage monitors/dashboards, create events and downtimes. Always search tools first for current schemas. |
| [`debugger`](skills/debugger/SKILL.md) | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. |
| [`debugging-toolkit-smart-debug`](skills/debugging-toolkit-smart-debug/SKILL.md) | Use when working with debugging toolkit smart debug |
| [`dependency-upgrade`](skills/dependency-upgrade/SKILL.md) | Master major dependency version upgrades, compatibility analysis, staged upgrade strategies, and comprehensive testing approaches. |
| [`deployment-validation-config-validate`](skills/deployment-validation-config-validate/SKILL.md) | You are a configuration management expert specializing in validating, testing, and ensuring the correctness of application configurations. Create comprehensive validation schema... |
| [`distributed-debugging-debug-trace`](skills/distributed-debugging-debug-trace/SKILL.md) | You are a debugging expert specializing in setting up comprehensive debugging environments, distributed tracing, and diagnostic tools. Configure debugging workflows, implement t... |
| [`e2e-testing-patterns`](skills/e2e-testing-patterns/SKILL.md) | Build reliable, fast, and maintainable end-to-end test suites that provide confidence to ship code quickly and catch regressions before users do. |
| [`error-debugging-error-analysis`](skills/error-debugging-error-analysis/SKILL.md) | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability so... |
| [`error-debugging-error-trace`](skills/error-debugging-error-trace/SKILL.md) | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error tracking systems, configure alerts, implem... |
| [`error-debugging-multi-agent-review`](skills/error-debugging-multi-agent-review/SKILL.md) | Use when working with error debugging multi agent review |
| [`error-detective`](skills/error-detective/SKILL.md) | Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes. |
| [`error-diagnostics-error-analysis`](skills/error-diagnostics-error-analysis/SKILL.md) | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability so... |
| [`error-diagnostics-error-trace`](skills/error-diagnostics-error-trace/SKILL.md) | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error tracking systems, configure alerts, implem... |
| [`error-diagnostics-smart-debug`](skills/error-diagnostics-smart-debug/SKILL.md) | Use when working with error diagnostics smart debug |
| [`error-handling-patterns`](skills/error-handling-patterns/SKILL.md) | Build resilient applications with robust error handling strategies that gracefully handle failures and provide excellent debugging experiences. |
| [`evaluation`](skills/evaluation/SKILL.md) | Build evaluation frameworks for agent systems. Use when testing agent performance systematically, validating context engineering choices, or measuring improvements over time. |
| [`fda-food-safety-auditor`](skills/fda-food-safety-auditor/SKILL.md) | Expert AI auditor for FDA Food Safety (FSMA), HACCP, and PCQI compliance. Reviews food facility records and preventive controls. |
| [`fda-medtech-compliance-auditor`](skills/fda-medtech-compliance-auditor/SKILL.md) | Expert AI auditor for Medical Device (SaMD) compliance, IEC 62304, and 21 CFR Part 820. Reviews DHFs, technical files, and software validation. |
| [`finishing-a-development-branch`](skills/finishing-a-development-branch/SKILL.md) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options fo... |
| [`fix-review`](skills/fix-review/SKILL.md) | Verify fix commits address audit findings without new bugs |
| [`fixing-accessibility`](skills/fixing-accessibility/SKILL.md) | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. Use when adding interactive controls, form... |
| [`framework-migration-deps-upgrade`](skills/framework-migration-deps-upgrade/SKILL.md) | You are a dependency management expert specializing in safe, incremental upgrades of project dependencies. Plan and execute dependency updates with minimal risk, proper testing,... |
| [`git-hooks-automation`](skills/git-hooks-automation/SKILL.md) | Master Git hooks setup with Husky, lint-staged, pre-commit framework, and commitlint. Automate code quality gates, formatting, linting, and commit message enforcement before cod... |
| [`go-concurrency-patterns`](skills/go-concurrency-patterns/SKILL.md) | Master Go concurrency with goroutines, channels, sync primitives, and context. Use when building concurrent Go applications, implementing worker pools, or debugging race conditi... |
| [`go-playwright`](skills/go-playwright/SKILL.md) | Expert capability for robust, stealthy, and efficient browser automation using Playwright Go. |
| [`grafana-dashboards`](skills/grafana-dashboards/SKILL.md) | Create and manage production-ready Grafana dashboards for comprehensive system observability. |
| [`gsd-add-tests`](skills/gsd-add-tests/SKILL.md) | Generate tests for a completed phase based on UAT criteria and implementation |
| [`gsd-audit-fix`](skills/gsd-audit-fix/SKILL.md) | Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit |
| [`gsd-audit-milestone`](skills/gsd-audit-milestone/SKILL.md) | Audit milestone completion against original intent before archiving |
| [`gsd-audit-uat`](skills/gsd-audit-uat/SKILL.md) | Cross-phase audit of all outstanding UAT and verification items |
| [`gsd-debug`](skills/gsd-debug/SKILL.md) | Systematic debugging with persistent state across context resets |
| [`gsd-ns-project`](skills/gsd-ns-project/SKILL.md) | project lifecycle \| milestones audits summary |
| [`gsd-update`](skills/gsd-update/SKILL.md) | Update GSD to latest version with changelog display |
| [`gsd-validate-phase`](skills/gsd-validate-phase/SKILL.md) | Retroactively audit and fill Nyquist validation gaps for a completed phase |
| [`hr-pro`](skills/hr-pro/SKILL.md) | Professional, ethical HR partner for hiring, onboarding/offboarding, PTO and leave, performance, compliant policies, and employee relations. |
| [`incident-response-incident-response`](skills/incident-response-incident-response/SKILL.md) | Use when working with incident response incident response |
| [`incident-runbook-templates`](skills/incident-runbook-templates/SKILL.md) | Production-ready templates for incident response runbooks covering detection, triage, mitigation, resolution, and communication. |
| [`internal-comms`](skills/internal-comms/SKILL.md) | Write internal communications such as status reports, leadership updates, 3P updates, newsletters, FAQs, incident reports, and project updates using repeatable internal formats. |
| [`javascript-testing-patterns`](skills/javascript-testing-patterns/SKILL.md) | Comprehensive guide for implementing robust testing strategies in JavaScript/TypeScript applications using modern testing frameworks and best practices. |
| [`kotlin-coroutines-expert`](skills/kotlin-coroutines-expert/SKILL.md) | Expert patterns for Kotlin Coroutines and Flow, covering structured concurrency, error handling, and testing. |
| [`leiloeiro-edital`](skills/leiloeiro-edital/SKILL.md) | Analise e auditoria de editais de leilao judicial e extrajudicial. Riscos ocultos, clausulas perigosas, debitos, ocupante e classificacao da oportunidade. |
| [`lint-and-validate`](skills/lint-and-validate/SKILL.md) | MANDATORY: Run appropriate validation tools after EVERY code change. Do not finish a task until the code is error-free. |
| [`linux-troubleshooting`](skills/linux-troubleshooting/SKILL.md) | Linux system troubleshooting workflow for diagnosing and resolving system issues, performance problems, and service failures. |
| [`local-legal-seo-audit`](skills/local-legal-seo-audit/SKILL.md) | Audit and improve local SEO for law firms, attorneys, forensic experts and legal/professional services sites with local presence, focusing on GBP, directories, E-E-A-T and pract... |
| [`observability-engineer`](skills/observability-engineer/SKILL.md) | Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and incident response workflows. |
| [`observability-monitoring-monitor-setup`](skills/observability-monitoring-monitor-setup/SKILL.md) | You are a monitoring and observability expert specializing in implementing comprehensive monitoring solutions. Set up metrics collection, distributed tracing, log aggregation, a... |
| [`on-call-handoff-patterns`](skills/on-call-handoff-patterns/SKILL.md) | Effective patterns for on-call shift transitions, ensuring continuity, context transfer, and reliable incident response across shifts. |
| [`openclaw-github-repo-commander`](skills/openclaw-github-repo-commander/SKILL.md) | 7-stage super workflow for GitHub repo audit, cleanup, PR review, and competitor analysis |
| [`os-scripting`](skills/os-scripting/SKILL.md) | Operating system and shell scripting troubleshooting workflow for Linux, macOS, and Windows. Covers bash scripting, system administration, debugging, and automation. |
| [`page-cro`](skills/page-cro/SKILL.md) | Analyze and optimize individual pages for conversion performance. |
| [`pagerduty-automation`](skills/pagerduty-automation/SKILL.md) | Automate PagerDuty tasks via Rube MCP (Composio): manage incidents, services, schedules, escalation policies, and on-call rotations. Always search tools first for current schemas. |
| [`paid-ads`](skills/paid-ads/SKILL.md) | You are an expert performance marketer with direct access to ad platform accounts. Your goal is to help create, optimize, and scale paid advertising campaigns that drive efficie... |
| [`performance-engineer`](skills/performance-engineer/SKILL.md) | Expert performance engineer specializing in modern observability, |
| [`performance-profiling`](skills/performance-profiling/SKILL.md) | Performance profiling principles. Measurement, analysis, and optimization techniques. |
| [`performance-testing-review-multi-agent-review`](skills/performance-testing-review-multi-agent-review/SKILL.md) | Use when working with performance testing review multi agent review |
| [`phase-gated-debugging`](skills/phase-gated-debugging/SKILL.md) | Use when debugging any bug. Enforces a 5-phase protocol where code edits are blocked until root cause is confirmed. Prevents premature fix attempts. |
| [`playwright-java`](skills/playwright-java/SKILL.md) | Scaffold, write, debug, and enhance enterprise-grade Playwright E2E tests in Java using Page Object Model, JUnit 5, Allure reporting, and parallel execution. |
| [`playwright-skill`](skills/playwright-skill/SKILL.md) | IMPORTANT - Path Resolution: This skill can be installed in different locations (plugin system, manual installation, global, or project-specific). Before executing any commands,... |
| [`postmortem-writing`](skills/postmortem-writing/SKILL.md) | Comprehensive guide to writing effective, blameless postmortems that drive organizational learning and prevent incident recurrence. |
| [`pr-writer`](skills/pr-writer/SKILL.md) | Create pull requests following Sentry's engineering practices. |
| [`project-skill-audit`](skills/project-skill-audit/SKILL.md) | Audit a project and recommend the highest-value skills to add or update. |
| [`prometheus-configuration`](skills/prometheus-configuration/SKILL.md) | Complete guide to Prometheus setup, metric collection, scrape configuration, and recording rules. |
| [`pypict-skill`](skills/pypict-skill/SKILL.md) | Pairwise test generation |
| [`python-performance-optimization`](skills/python-performance-optimization/SKILL.md) | Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, optimizing bottlenecks, or improving appl... |
| [`python-testing-patterns`](skills/python-testing-patterns/SKILL.md) | Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, setting up test suites, or implementing te... |
| [`screen-reader-testing`](skills/screen-reader-testing/SKILL.md) | Practical guide to testing web applications with screen readers for comprehensive accessibility validation. |
| [`screenshots`](skills/screenshots/SKILL.md) | Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social media, landing pages, or documentation. |
| [`sentry-automation`](skills/sentry-automation/SKILL.md) | Automate Sentry tasks via Rube MCP (Composio): manage issues/events, configure alerts, track releases, monitor projects and teams. Always search tools first for current schemas. |
| [`seo`](skills/seo/SKILL.md) | Run a broad SEO audit across technical SEO, on-page SEO, schema, sitemaps, content quality, AI search readiness, and GEO. Use as the umbrella skill when the user asks for a full... |
| [`seo-aeo-content-quality-auditor`](skills/seo-aeo-content-quality-auditor/SKILL.md) | Audits content for SEO and AEO performance with scored reports, severity-ranked fix lists, and projected scores after fixes. Activate when the user wants to audit, review, or sc... |
| [`seo-audit`](skills/seo-audit/SKILL.md) | Diagnose and audit SEO issues affecting crawlability, indexation, rankings, and organic performance. |
| [`seo-content`](skills/seo-content/SKILL.md) | > Content quality and E-E-A-T analysis with AI citation readiness assessment. Use when user says "content quality", "E-E-A-T", "content analysis", "readability check", "thin con... |
| [`seo-content-auditor`](skills/seo-content-auditor/SKILL.md) | Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. Scores content and provides improvement recommendations based on established guidelines. |
| [`seo-forensic-incident-response`](skills/seo-forensic-incident-response/SKILL.md) | Investigate sudden drops in organic traffic or rankings and run a structured forensic SEO incident response with triage, root-cause analysis and recovery plan. |
| [`seo-hreflang`](skills/seo-hreflang/SKILL.md) | > Hreflang and international SEO audit, validation, and generation. Detects common mistakes, validates language/region codes, and generates correct hreflang implementations. Use... |
| [`seo-images`](skills/seo-images/SKILL.md) | > Image optimization analysis for SEO and performance. Checks alt text, file sizes, formats, responsive images, lazy loading, and CLS prevention. Use when user says "image optim... |
| [`seo-page`](skills/seo-page/SKILL.md) | > Deep single-page SEO analysis covering on-page elements, content quality, technical meta tags, schema, images, and performance. Use when user says "analyze this page", "check ... |
| [`slo-implementation`](skills/slo-implementation/SKILL.md) | Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets. |
| [`spec-to-code-compliance`](skills/spec-to-code-compliance/SKILL.md) | Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, ... |
| [`startup-metrics-framework`](skills/startup-metrics-framework/SKILL.md) | Comprehensive guide to tracking, calculating, and optimizing key performance metrics for different startup business models from seed through Series A. |
| [`statsmodels`](skills/statsmodels/SKILL.md) | Statsmodels is Python's premier library for statistical modeling, providing tools for estimation, inference, and diagnostics across a wide range of statistical methods. |
| [`systematic-debugging`](skills/systematic-debugging/SKILL.md) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| [`tdd-orchestrator`](skills/tdd-orchestrator/SKILL.md) | Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven development practices. |
| [`tdd-workflow`](skills/tdd-workflow/SKILL.md) | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. |
| [`tdd-workflows-tdd-cycle`](skills/tdd-workflows-tdd-cycle/SKILL.md) | Use when working with tdd workflows tdd cycle |
| [`tdd-workflows-tdd-green`](skills/tdd-workflows-tdd-green/SKILL.md) | Implement the minimal code needed to make failing tests pass in the TDD green phase. |
| [`tdd-workflows-tdd-red`](skills/tdd-workflows-tdd-red/SKILL.md) | Generate failing tests for the TDD red phase to define expected behavior and edge cases. |
| [`tdd-workflows-tdd-refactor`](skills/tdd-workflows-tdd-refactor/SKILL.md) | Use when working with tdd workflows tdd refactor |
| [`test-driven-development`](skills/test-driven-development/SKILL.md) | Use when implementing any feature or bugfix, before writing implementation code |
| [`test-fixing`](skills/test-fixing/SKILL.md) | Systematically identify and fix all failing tests using smart grouping strategies. Use when explicitly asks to fix tests (\"fix these tests\", \"make tests pass\"), reports test... |
| [`testing-patterns`](skills/testing-patterns/SKILL.md) | Jest testing patterns, factory functions, mocking strategies, and TDD workflow. Use when writing unit tests, creating test factories, or following TDD red-green-refactor cycle. |
| [`testing-qa`](skills/testing-qa/SKILL.md) | Comprehensive testing and QA workflow covering unit testing, integration testing, E2E testing, browser automation, and quality assurance. |
| [`typescript-expert`](skills/typescript-expert/SKILL.md) | TypeScript and JavaScript expert with deep knowledge of type-level programming, performance optimization, monorepo management, migration strategies, and modern tooling. |
| [`wcag-audit-patterns`](skills/wcag-audit-patterns/SKILL.md) | Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies. |
| [`web-performance-optimization`](skills/web-performance-optimization/SKILL.md) | Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance |
| [`web3-testing`](skills/web3-testing/SKILL.md) | Master comprehensive testing strategies for smart contracts using Hardhat, Foundry, and advanced testing patterns. |
| [`webapp-testing`](skills/webapp-testing/SKILL.md) | To test local web applications, write native Python Playwright scripts. |
| [`wiki-qa`](skills/wiki-qa/SKILL.md) | Answer repository questions grounded entirely in source code evidence. Use when user asks a question about the codebase, user wants to understand a specific file, function, or c... |
| [`workflow-patterns`](skills/workflow-patterns/SKILL.md) | Use this skill when implementing tasks according to Conductor's TDD workflow, handling phase checkpoints, managing git commits for tasks, or understanding the verification proto... |
| [`yes-md`](skills/yes-md/SKILL.md) | 6-layer AI governance: safety gates, evidence-based debugging, anti-slack detection, and machine-enforced hooks. Makes AI safe, thorough, and honest. |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="gsd_productivity"></a>
### ⚡ GSD (Get Shit Done), Automação & Workflows
*Metodologia GSD completa, automação com n8n, Conductor, integração com GitHub, Slack, Notion, Jira, Linux e scripts de terminal.* (151 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`address-github-comments`](skills/address-github-comments/SKILL.md) | Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI. |
| [`airtable-automation`](skills/airtable-automation/SKILL.md) | Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views. Always search tools first for current schemas. |
| [`asana-automation`](skills/asana-automation/SKILL.md) | Automate Asana tasks via Rube MCP (Composio): tasks, projects, sections, teams, workspaces. Always search tools first for current schemas. |
| [`bamboohr-automation`](skills/bamboohr-automation/SKILL.md) | Automate BambooHR tasks via Rube MCP (Composio): employees, time-off, benefits, dependents, employee updates. Always search tools first for current schemas. |
| [`bash-linux`](skills/bash-linux/SKILL.md) | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems. |
| [`blueprint`](skills/blueprint/SKILL.md) | Turn a one-line objective into a step-by-step construction plan any coding agent can execute cold. Each step has a self-contained context brief — a fresh agent in a new session ... |
| [`box-automation`](skills/box-automation/SKILL.md) | Automate Box operations including file upload/download, content search, folder management, collaboration, metadata queries, and sign requests through Composio's Box toolkit. |
| [`busybox-on-windows`](skills/busybox-on-windows/SKILL.md) | How to use a Win32 build of BusyBox to run many of the standard UNIX command line tools on Windows. |
| [`cal-com-automation`](skills/cal-com-automation/SKILL.md) | Automate Cal.com tasks via Rube MCP (Composio): manage bookings, check availability, configure webhooks, and handle teams. Always search tools first for current schemas. |
| [`calendly-automation`](skills/calendly-automation/SKILL.md) | Automate Calendly scheduling, event management, invitee tracking, availability checks, and organization administration via Rube MCP (Composio). Always search tools first for cur... |
| [`changelog-automation`](skills/changelog-automation/SKILL.md) | Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. Use when setting up release workflows, generating release notes, or standardizin... |
| [`clickup-automation`](skills/clickup-automation/SKILL.md) | Automate ClickUp project management including tasks, spaces, folders, lists, comments, and team operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`close-automation`](skills/close-automation/SKILL.md) | Automate Close CRM tasks via Rube MCP (Composio): create leads, manage calls/SMS, handle tasks, and track notes. Always search tools first for current schemas. |
| [`coda-automation`](skills/coda-automation/SKILL.md) | Automate Coda tasks via Rube MCP (Composio): manage docs, pages, tables, rows, formulas, permissions, and publishing. Always search tools first for current schemas. |
| [`code-documentation-code-explain`](skills/code-documentation-code-explain/SKILL.md) | You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. Transform difficult concepts into... |
| [`concise-planning`](skills/concise-planning/SKILL.md) | Use when a user asks for a plan for a coding task, to generate a clear, actionable, and atomic checklist. |
| [`conductor-manage`](skills/conductor-manage/SKILL.md) | Manage track lifecycle: archive, restore, delete, rename, and cleanup |
| [`conductor-new-track`](skills/conductor-new-track/SKILL.md) | Create a new track with specification and phased implementation plan |
| [`conductor-revert`](skills/conductor-revert/SKILL.md) | Git-aware undo by logical work unit (track, phase, or task) |
| [`conductor-setup`](skills/conductor-setup/SKILL.md) | Configure a Rails project to work with Conductor (parallel coding agents) |
| [`conductor-status`](skills/conductor-status/SKILL.md) | Display project status, active tracks, and next actions |
| [`conductor-validator`](skills/conductor-validator/SKILL.md) | Validates Conductor project artifacts for completeness, consistency, and correctness. Use after setup, when diagnosing issues, or before implementation to verify project context. |
| [`context-compression`](skills/context-compression/SKILL.md) | When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach is aggressive compression to minimize tokens per request. |
| [`context-driven-development`](skills/context-driven-development/SKILL.md) | Guide for implementing and maintaining context as a managed artifact alongside code, enabling consistent AI interactions and team alignment through structured project documentat... |
| [`context-fundamentals`](skills/context-fundamentals/SKILL.md) | Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, too... |
| [`context-guardian`](skills/context-guardian/SKILL.md) | Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao. |
| [`context-management-context-restore`](skills/context-management-context-restore/SKILL.md) | Use when working with context management context restore |
| [`context-management-context-save`](skills/context-management-context-save/SKILL.md) | Use when working with context management context save |
| [`context-optimization`](skills/context-optimization/SKILL.md) | Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and partitioning. The goal is not to magically in... |
| [`deployment-procedures`](skills/deployment-procedures/SKILL.md) | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts. |
| [`diary`](skills/diary/SKILL.md) | Unified Diary System: A context-preserving automated logger for multi-project development. |
| [`docx-official`](skills/docx-official/SKILL.md) | A user may ask you to create, edit, or analyze the contents of a .docx file. A .docx file is essentially a ZIP archive containing XML files and other resources that you can read... |
| [`dropbox-automation`](skills/dropbox-automation/SKILL.md) | Automate Dropbox file management, sharing, search, uploads, downloads, and folder operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`dx-optimizer`](skills/dx-optimizer/SKILL.md) | Developer Experience specialist. Improves tooling, setup, and workflows. Use PROACTIVELY when setting up new projects, after team feedback, or when development friction is noticed. |
| [`executing-plans`](skills/executing-plans/SKILL.md) | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| [`framework-migration-code-migrate`](skills/framework-migration-code-migrate/SKILL.md) | You are a code migration expert specializing in transitioning codebases between frameworks, languages, versions, and platforms. Generate comprehensive migration plans, automated... |
| [`free-tool-strategy`](skills/free-tool-strategy/SKILL.md) | You are an expert in engineering-as-marketing strategy. Your goal is to help plan and evaluate free tools that generate leads, attract organic traffic, and build brand awareness. |
| [`freshdesk-automation`](skills/freshdesk-automation/SKILL.md) | Automate Freshdesk helpdesk operations including tickets, contacts, companies, notes, and replies via Rube MCP (Composio). Always search tools first for current schemas. |
| [`freshservice-automation`](skills/freshservice-automation/SKILL.md) | Automate Freshservice ITSM tasks via Rube MCP (Composio): create/update tickets, bulk operations, service requests, and outbound emails. Always search tools first for current sc... |
| [`gh-review-requests`](skills/gh-review-requests/SKILL.md) | Fetch unread GitHub notifications for open PRs where review is requested from a specified team or opened by a team member. Use when asked to "find PRs I need to review", "show m... |
| [`git-advanced-workflows`](skills/git-advanced-workflows/SKILL.md) | Master advanced Git techniques to maintain clean history, collaborate effectively, and recover from any situation with confidence. |
| [`git-pr-workflows-pr-enhance`](skills/git-pr-workflows-pr-enhance/SKILL.md) | You are a PR optimization expert specializing in creating high-quality pull requests that facilitate efficient code reviews. Generate comprehensive PR descriptions, automate rev... |
| [`git-pushing`](skills/git-pushing/SKILL.md) | Stage all changes, create a conventional commit, and push to the remote branch. Use when explicitly asks to push changes (\"push this\", \"commit and push\"), mentions saving wo... |
| [`github-issue-creator`](skills/github-issue-creator/SKILL.md) | Turn error logs, screenshots, voice notes, and rough bug reports into crisp, developer-ready GitHub issues with repro steps, impact, and evidence. |
| [`gitlab-automation`](skills/gitlab-automation/SKILL.md) | Automate GitLab project management, issues, merge requests, pipelines, branches, and user operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`google-analytics-automation`](skills/google-analytics-automation/SKILL.md) | Automate Google Analytics tasks via Rube MCP (Composio): run reports, list accounts/properties, funnels, pivots, key events. Always search tools first for current schemas. |
| [`gsd-autonomous`](skills/gsd-autonomous/SKILL.md) | Run all remaining phases autonomously — discuss→plan→execute per phase |
| [`gsd-capture`](skills/gsd-capture/SKILL.md) | Capture ideas, tasks, notes, and seeds to their destination |
| [`gsd-cleanup`](skills/gsd-cleanup/SKILL.md) | Archive accumulated phase directories from completed milestones |
| [`gsd-complete-milestone`](skills/gsd-complete-milestone/SKILL.md) | Archive completed milestone and prepare for next version |
| [`gsd-config`](skills/gsd-config/SKILL.md) | Configure GSD settings — workflow toggles, advanced knobs, integrations, and model profile |
| [`gsd-discuss-phase`](skills/gsd-discuss-phase/SKILL.md) | Gather phase context through adaptive questioning before planning. |
| [`gsd-docs-update`](skills/gsd-docs-update/SKILL.md) | Generate or update project documentation verified against the codebase |
| [`gsd-execute-phase`](skills/gsd-execute-phase/SKILL.md) | Execute all plans in a phase with wave-based parallelization |
| [`gsd-explore`](skills/gsd-explore/SKILL.md) | Socratic ideation and idea routing — think through ideas before committing to plans |
| [`gsd-extract-learnings`](skills/gsd-extract-learnings/SKILL.md) | Extract decisions, lessons, patterns, and surprises from completed phase artifacts |
| [`gsd-fast`](skills/gsd-fast/SKILL.md) | Execute a trivial task inline — no subagents, no planning overhead |
| [`gsd-forensics`](skills/gsd-forensics/SKILL.md) | Post-mortem investigation for failed GSD workflows — diagnoses what went wrong. |
| [`gsd-graphify`](skills/gsd-graphify/SKILL.md) | Build, query, and inspect the project knowledge graph in .planning/graphs/ |
| [`gsd-health`](skills/gsd-health/SKILL.md) | Diagnose planning directory health and optionally repair issues |
| [`gsd-help`](skills/gsd-help/SKILL.md) | Show available GSD commands and usage guide |
| [`gsd-import`](skills/gsd-import/SKILL.md) | Ingest external plans with conflict detection against project decisions before writing anything. |
| [`gsd-inbox`](skills/gsd-inbox/SKILL.md) | Triage and review open GitHub issues and PRs against project templates and contribution guidelines. |
| [`gsd-ingest-docs`](skills/gsd-ingest-docs/SKILL.md) | Bootstrap or merge a .planning/ setup from existing ADRs, PRDs, SPECs, and docs in a repo. |
| [`gsd-manager`](skills/gsd-manager/SKILL.md) | Interactive command center for managing multiple phases from one terminal |
| [`gsd-map-codebase`](skills/gsd-map-codebase/SKILL.md) | Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents |
| [`gsd-milestone-summary`](skills/gsd-milestone-summary/SKILL.md) | Generate a comprehensive project summary from milestone artifacts for team onboarding and review |
| [`gsd-mvp-phase`](skills/gsd-mvp-phase/SKILL.md) | Plan a phase as a vertical MVP slice — user story, SPIDR splitting, then plan-phase |
| [`gsd-new-milestone`](skills/gsd-new-milestone/SKILL.md) | Start a new milestone cycle — update PROJECT.md and route to requirements |
| [`gsd-new-project`](skills/gsd-new-project/SKILL.md) | Initialize a new project with deep context gathering and PROJECT.md |
| [`gsd-ns-context`](skills/gsd-ns-context/SKILL.md) | codebase intelligence \| map graphify docs learnings |
| [`gsd-ns-ideate`](skills/gsd-ns-ideate/SKILL.md) | exploration capture \| explore sketch spike spec capture |
| [`gsd-ns-manage`](skills/gsd-ns-manage/SKILL.md) | config workspace \| workstreams thread update ship inbox |
| [`gsd-ns-workflow`](skills/gsd-ns-workflow/SKILL.md) | workflow \| discuss plan execute verify phase progress |
| [`gsd-pause-work`](skills/gsd-pause-work/SKILL.md) | Create context handoff when pausing work mid-phase |
| [`gsd-phase`](skills/gsd-phase/SKILL.md) | CRUD for phases in ROADMAP.md — add, insert, remove, or edit phases |
| [`gsd-plan-phase`](skills/gsd-plan-phase/SKILL.md) | Create detailed phase plan (PLAN.md) with verification loop |
| [`gsd-plan-review-convergence`](skills/gsd-plan-review-convergence/SKILL.md) | Cross-AI plan convergence loop — replan with review feedback until no HIGH concerns remain. |
| [`gsd-pr-branch`](skills/gsd-pr-branch/SKILL.md) | Create a clean PR branch by filtering out .planning/ commits — ready for code review |
| [`gsd-progress`](skills/gsd-progress/SKILL.md) | Check progress, advance workflow, or dispatch freeform intent — the unified GSD situational command |
| [`gsd-quick`](skills/gsd-quick/SKILL.md) | Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents |
| [`gsd-resume-work`](skills/gsd-resume-work/SKILL.md) | Resume work from previous session with full context restoration |
| [`gsd-review`](skills/gsd-review/SKILL.md) | Request cross-AI peer review of phase plans from external AI CLIs |
| [`gsd-review-backlog`](skills/gsd-review-backlog/SKILL.md) | Review and promote backlog items to active milestone |
| [`gsd-settings`](skills/gsd-settings/SKILL.md) | Configure GSD workflow toggles and model profile |
| [`gsd-ship`](skills/gsd-ship/SKILL.md) | Create PR, run review, and prepare for merge after verification passes |
| [`gsd-spec-phase`](skills/gsd-spec-phase/SKILL.md) | Clarify WHAT a phase delivers with ambiguity scoring; produces a SPEC.md before discuss-phase. |
| [`gsd-spike`](skills/gsd-spike/SKILL.md) | Spike an idea through experiential exploration, or propose what to spike next (frontier mode) |
| [`gsd-stats`](skills/gsd-stats/SKILL.md) | Display project statistics — phases, plans, requirements, git metrics, and timeline |
| [`gsd-surface`](skills/gsd-surface/SKILL.md) | Toggle which skills are surfaced — apply a profile, list, or disable a cluster without reinstall |
| [`gsd-thread`](skills/gsd-thread/SKILL.md) | Manage persistent context threads for cross-session work |
| [`gsd-undo`](skills/gsd-undo/SKILL.md) | Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks. |
| [`gsd-verify-work`](skills/gsd-verify-work/SKILL.md) | Validate built features through conversational UAT |
| [`gsd-workspace`](skills/gsd-workspace/SKILL.md) | Manage GSD workspaces — create, list, or remove isolated workspace environments |
| [`gsd-workstreams`](skills/gsd-workstreams/SKILL.md) | Manage parallel workstreams — list, create, switch, status, progress, complete, and resume |
| [`helpdesk-automation`](skills/helpdesk-automation/SKILL.md) | Automate HelpDesk tasks via Rube MCP (Composio): list tickets, manage views, use canned responses, and configure custom fields. Always search tools first for current schemas. |
| [`humanize-chinese`](skills/humanize-chinese/SKILL.md) | Detect and rewrite AI-like Chinese text with a practical workflow for scoring, humanization, academic AIGC reduction, and style conversion. Use when the user asks to 去AI味, 降AIGC... |
| [`inventory-demand-planning`](skills/inventory-demand-planning/SKILL.md) | Codified expertise for demand forecasting, safety stock optimisation, replenishment planning, and promotional lift estimation at multi-location retailers. |
| [`issues`](skills/issues/SKILL.md) | Interact with GitHub issues - create, list, and view issues. |
| [`javascript-mastery`](skills/javascript-mastery/SKILL.md) | 33+ essential JavaScript concepts every developer should know, inspired by [33-js-concepts](https://github.com/leonardomso/33-js-concepts). |
| [`jira-automation`](skills/jira-automation/SKILL.md) | Automate Jira tasks via Rube MCP (Composio): issues, projects, sprints, boards, comments, users. Always search tools first for current schemas. |
| [`jq`](skills/jq/SKILL.md) | Expert jq usage for JSON querying, filtering, transformation, and pipeline integration. Practical patterns for real shell workflows. |
| [`kaizen`](skills/kaizen/SKILL.md) | Guide for continuous improvement, error proofing, and standardization. Use this skill when the user wants to improve code quality, refactor, or discuss process improvements. |
| [`launch-strategy`](skills/launch-strategy/SKILL.md) | You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capture attention, and convert interest into ... |
| [`linear-automation`](skills/linear-automation/SKILL.md) | Automate Linear tasks via Rube MCP (Composio): issues, projects, cycles, teams, labels. Always search tools first for current schemas. |
| [`make-automation`](skills/make-automation/SKILL.md) | Automate Make (Integromat) tasks via Rube MCP (Composio): operations, enums, language and timezone lookups. Always search tools first for current schemas. |
| [`matematico-tao`](skills/matematico-tao/SKILL.md) | Matemático ultra-avançado inspirado em Terence Tao. Análise rigorosa de código e arquitetura com teoria matemática profunda: teoria da informação, teoria dos grafos, complexidad... |
| [`monday-automation`](skills/monday-automation/SKILL.md) | Automate Monday.com work management including boards, items, columns, groups, subitems, and updates via Rube MCP (Composio). Always search tools first for current schemas. |
| [`n8n-code-javascript`](skills/n8n-code-javascript/SKILL.md) | Write JavaScript code in n8n Code nodes. Use when writing JavaScript in n8n, using $input/$json/$node syntax, making HTTP requests with $helpers, working with dates using DateTi... |
| [`n8n-code-python`](skills/n8n-code-python/SKILL.md) | Write Python code in n8n Code nodes. Use when writing Python in n8n, using _input/_json/_node syntax, working with standard library, or need to understand Python limitations in ... |
| [`n8n-expression-syntax`](skills/n8n-expression-syntax/SKILL.md) | Validate n8n expression syntax and fix common errors. Use when writing n8n expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting expression errors, or... |
| [`n8n-node-configuration`](skills/n8n-node-configuration/SKILL.md) | Operation-aware node configuration guidance. Use when configuring nodes, understanding property dependencies, determining required fields, choosing between get_node detail level... |
| [`n8n-validation-expert`](skills/n8n-validation-expert/SKILL.md) | Expert guide for interpreting and fixing n8n validation errors. |
| [`notion-template-business`](skills/notion-template-business/SKILL.md) | You know templates are real businesses that can generate serious income. You've seen creators make six figures selling Notion templates. You understand it's not about the templa... |
| [`obsidian-cli`](skills/obsidian-cli/SKILL.md) | Use the Obsidian CLI to read, create, search, and manage vault content, or to develop and debug Obsidian plugins and themes from the command line. |
| [`obsidian-clipper-template-creator`](skills/obsidian-clipper-template-creator/SKILL.md) | Guide for creating templates for the Obsidian Web Clipper. Use when you want to create a new clipping template, understand available variables, or format clipped content. |
| [`obsidian-markdown`](skills/obsidian-markdown/SKILL.md) | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when working with .md files in Obsidian, or when... |
| [`office-productivity`](skills/office-productivity/SKILL.md) | Office productivity workflow covering document creation, spreadsheet automation, presentation generation, and integration with LibreOffice and Microsoft Office formats. |
| [`orchestrate-batch-refactor`](skills/orchestrate-batch-refactor/SKILL.md) | Plan and execute large refactors with dependency-aware work packets and parallel analysis. |
| [`outlook-automation`](skills/outlook-automation/SKILL.md) | Automate Outlook tasks via Rube MCP (Composio): emails, calendar, contacts, folders, attachments. Always search tools first for current schemas. |
| [`outlook-calendar-automation`](skills/outlook-calendar-automation/SKILL.md) | Automate Outlook Calendar tasks via Rube MCP (Composio): create events, manage attendees, find meeting times, and handle invitations. Always search tools first for current schemas. |
| [`pipedrive-automation`](skills/pipedrive-automation/SKILL.md) | Automate Pipedrive CRM operations including deals, contacts, organizations, activities, notes, and pipeline management via Rube MCP (Composio). Always search tools first for cur... |
| [`planning-with-files`](skills/planning-with-files/SKILL.md) | Work like Manus: Use persistent markdown files as your \"working memory on disk.\ |
| [`plotly`](skills/plotly/SKILL.md) | Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static pu... |
| [`posix-shell-pro`](skills/posix-shell-pro/SKILL.md) | Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. Specializes in shell scripts that run on any POSIX-compliant shell (dash, ash, sh, bash --p... |
| [`postmark-automation`](skills/postmark-automation/SKILL.md) | Automate Postmark email delivery tasks via Rube MCP (Composio): send templated emails, manage templates, monitor delivery stats and bounces. Always search tools first for curren... |
| [`powershell-windows`](skills/powershell-windows/SKILL.md) | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. |
| [`pptx-official`](skills/pptx-official/SKILL.md) | A user may ask you to create, edit, or analyze the contents of a .pptx file. A .pptx file is essentially a ZIP archive containing XML files and other resources that you can read... |
| [`salesforce-automation`](skills/salesforce-automation/SKILL.md) | Automate Salesforce tasks via Rube MCP (Composio): leads, contacts, accounts, opportunities, SOQL queries. Always search tools first for current schemas. |
| [`scanpy`](skills/scanpy/SKILL.md) | Scanpy is a scalable Python toolkit for analyzing single-cell RNA-seq data, built on AnnData. Apply this skill for complete single-cell workflows including quality control, norm... |
| [`sendgrid-automation`](skills/sendgrid-automation/SKILL.md) | Automate SendGrid email delivery workflows including marketing campaigns (Single Sends), contact and list management, sender identity setup, and email analytics through Composio... |
| [`seo-content-planner`](skills/seo-content-planner/SKILL.md) | Creates comprehensive content outlines and topic clusters for SEO. Plans content calendars and identifies topic gaps. Use PROACTIVELY for content strategy and planning. |
| [`seo-image-gen`](skills/seo-image-gen/SKILL.md) | Generate SEO-focused images such as OG cards, hero images, schema assets, product visuals, and infographics. Use when image generation is part of an SEO workflow or content publ... |
| [`skill-installer`](skills/skill-installer/SKILL.md) | Instala, valida, registra e verifica novas skills no ecossistema. 10 checks de seguranca, copia, registro no orchestrator e verificacao pos-instalacao. |
| [`speed`](skills/speed/SKILL.md) | Launch RSVP speed reader for text |
| [`sred-work-summary`](skills/sred-work-summary/SKILL.md) | Go back through the previous year of work and create a Notion doc that groups relevant links into projects that can then be documented as SRED projects. |
| [`startup-analyst`](skills/startup-analyst/SKILL.md) | Expert startup business analyst specializing in market sizing, financial modeling, competitive analysis, and strategic planning for early-stage companies. |
| [`startup-financial-modeling`](skills/startup-financial-modeling/SKILL.md) | Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for early-stage startups. |
| [`subagent-driven-development`](skills/subagent-driven-development/SKILL.md) | Use when executing implementation plans with independent tasks in the current session |
| [`task-intelligence`](skills/task-intelligence/SKILL.md) | Protocolo de Inteligência Pré-Tarefa — ativa TODOS os agentes relevantes do ecossistema ANTES de executar qualquer tarefa solicitada pelo usuário. |
| [`team-collaboration-issue`](skills/team-collaboration-issue/SKILL.md) | You are a GitHub issue resolution expert specializing in systematic bug investigation, feature implementation, and collaborative development workflows. Your expertise spans issu... |
| [`team-collaboration-standup-notes`](skills/team-collaboration-standup-notes/SKILL.md) | You are an expert team communication specialist focused on async-first standup practices, AI-assisted note generation from commit history, and effective remote team coordination... |
| [`tmux`](skills/tmux/SKILL.md) | Expert tmux session, window, and pane management for terminal multiplexing, persistent remote workflows, and shell scripting automation. |
| [`track-management`](skills/track-management/SKILL.md) | Use this skill when creating, managing, or working with Conductor tracks - the logical work units for features, bugs, and refactors. Applies to spec.md, plan.md, and track lifec... |
| [`trello-automation`](skills/trello-automation/SKILL.md) | Automate Trello boards, cards, and workflows via Rube MCP (Composio). Create cards, manage lists, assign members, and search across boards programmatically. |
| [`vexor-cli`](skills/vexor-cli/SKILL.md) | Semantic file discovery via `vexor`. Use whenever locating where something is implemented/loaded/defined in a medium or large repo, or when the file location is unclear. Prefer ... |
| [`wrike-automation`](skills/wrike-automation/SKILL.md) | Automate Wrike project management via Rube MCP (Composio): create tasks/folders, manage projects, assign work, and track progress. Always search tools first for current schemas. |
| [`writing-plans`](skills/writing-plans/SKILL.md) | Use when you have a spec or requirements for a multi-step task, before touching code |
| [`zendesk-automation`](skills/zendesk-automation/SKILL.md) | Automate Zendesk tasks via Rube MCP (Composio): tickets, users, organizations, replies. Always search tools first for current schemas. |
| [`zoho-crm-automation`](skills/zoho-crm-automation/SKILL.md) | Automate Zoho CRM tasks via Rube MCP (Composio): create/update records, search contacts, manage leads, and convert leads. Always search tools first for current schemas. |
| [`zoom-automation`](skills/zoom-automation/SKILL.md) | Automate Zoom meeting creation, management, recordings, webinars, and participant tracking via Rube MCP (Composio). Always search tools first for current schemas. |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="marketing_growth"></a>
### 📈 Growth Hacking, Marketing, SEO & Psicologia de Conversão
*Estratégias de conversão (CRO), SEO técnico e semântico, geração de leads com Apify, copywriting psicológico e email marketing.* (89 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`amplitude-automation`](skills/amplitude-automation/SKILL.md) | Automate Amplitude tasks via Rube MCP (Composio): events, user activity, cohorts, user identification. Always search tools first for current schemas. |
| [`analytics-product`](skills/analytics-product/SKILL.md) | Analytics de produto — PostHog, Mixpanel, eventos, funnels, cohorts, retencao, north star metric, OKRs e dashboards de produto. |
| [`app-store-changelog`](skills/app-store-changelog/SKILL.md) | Generate user-facing App Store release notes from git history since the last tag. |
| [`arm-cortex-expert`](skills/arm-cortex-expert/SKILL.md) | Senior embedded software engineer specializing in firmware and driver development for ARM Cortex-M microcontrollers (Teensy, STM32, nRF52, SAMD). |
| [`awareness-stage-mapper`](skills/awareness-stage-mapper/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`brand-guidelines-anthropic`](skills/brand-guidelines-anthropic/SKILL.md) | To access Anthropic's official brand identity and style resources, use this skill. |
| [`brand-guidelines-community`](skills/brand-guidelines-community/SKILL.md) | To access Anthropic's official brand identity and style resources, use this skill. |
| [`brand-perception-psychologist`](skills/brand-perception-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`brevo-automation`](skills/brevo-automation/SKILL.md) | Automate Brevo (formerly Sendinblue) email marketing operations through Composio's Brevo toolkit via Rube MCP. |
| [`chat-widget`](skills/chat-widget/SKILL.md) | Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff. Use when the user wants live chat, customer support chat, real-t... |
| [`chrome-extension-developer`](skills/chrome-extension-developer/SKILL.md) | Expert in building Chrome Extensions using Manifest V3. Covers background scripts, service workers, content scripts, and cross-context communication. |
| [`closed-loop-delivery`](skills/closed-loop-delivery/SKILL.md) | Use when a coding task must be completed against explicit acceptance criteria with minimal user re-intervention across implementation, review feedback, deployment, and runtime v... |
| [`cold-email`](skills/cold-email/SKILL.md) | Write B2B cold emails and follow-up sequences that earn replies. Use when creating outbound prospecting emails, SDR outreach, personalized opening lines, subject lines, CTAs, an... |
| [`computer-vision-expert`](skills/computer-vision-expert/SKILL.md) | SOTA Computer Vision Expert (2026). Specialized in YOLO26, Segment Anything 3 (SAM 3), Vision Language Models, and real-time spatial analysis. |
| [`confluence-automation`](skills/confluence-automation/SKILL.md) | Automate Confluence page creation, content search, space management, labels, and hierarchy navigation via Rube MCP (Composio). Always search tools first for current schemas. |
| [`content-creator`](skills/content-creator/SKILL.md) | Professional-grade brand voice analysis, SEO optimization, and platform-specific content frameworks. |
| [`convertkit-automation`](skills/convertkit-automation/SKILL.md) | Automate ConvertKit (Kit) tasks via Rube MCP (Composio): manage subscribers, tags, broadcasts, and broadcast stats. Always search tools first for current schemas. |
| [`copy-editing`](skills/copy-editing/SKILL.md) | You are an expert copy editor specializing in marketing and conversion copy. Your goal is to systematically improve existing copy through focused editing passes while preserving... |
| [`copywriting`](skills/copywriting/SKILL.md) | Write rigorous, conversion-focused marketing copy for landing pages and emails. Enforces brief confirmation and strict no-fabrication rules. |
| [`copywriting-psychologist`](skills/copywriting-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`customer-support`](skills/customer-support/SKILL.md) | Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support experiences. |
| [`customs-trade-compliance`](skills/customs-trade-compliance/SKILL.md) | Codified expertise for customs documentation, tariff classification, duty optimisation, restricted party screening, and regulatory compliance across multiple jurisdictions. |
| [`daily-news-report`](skills/daily-news-report/SKILL.md) | Scrapes content based on a preset URL list, filters high-quality technical information, and generates daily Markdown reports. |
| [`defuddle`](skills/defuddle/SKILL.md) | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch when the user provides a URL to read or... |
| [`email-sequence`](skills/email-sequence/SKILL.md) | You are an expert in email marketing and automation. Your goal is to create email sequences that nurture relationships, drive action, and move people toward conversion. |
| [`email-systems`](skills/email-systems/SKILL.md) | You are an email systems engineer who has maintained 99.9% deliverability across millions of emails. You've debugged SPF/DKIM/DMARC, dealt with blacklists, and optimized for inb... |
| [`form-cro`](skills/form-cro/SKILL.md) | Optimize any form that is NOT signup or account registration — including lead capture, contact, demo request, application, survey, quote, and checkout forms. |
| [`growth-engine`](skills/growth-engine/SKILL.md) | Motor de crescimento para produtos digitais -- growth hacking, SEO, ASO, viral loops, email marketing, CRM, referral programs e aquisicao organica. |
| [`headline-psychologist`](skills/headline-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`hubspot-automation`](skills/hubspot-automation/SKILL.md) | Automate HubSpot CRM operations (contacts, companies, deals, tickets, properties) via Rube MCP using Composio integration. |
| [`instagram-automation`](skills/instagram-automation/SKILL.md) | Automate Instagram tasks via Rube MCP (Composio): create posts, carousels, manage media, get insights, and publishing limits. Always search tools first for current schemas. |
| [`intercom-automation`](skills/intercom-automation/SKILL.md) | Automate Intercom tasks via Rube MCP (Composio): conversations, contacts, companies, segments, admins. Always search tools first for current schemas. |
| [`jobs-to-be-done-analyst`](skills/jobs-to-be-done-analyst/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`keyword-extractor`](skills/keyword-extractor/SKILL.md) | > Extracts up to 50 highly relevant SEO keywords from text. Use when user wants to generate or extract keywords for given text. |
| [`klaviyo-automation`](skills/klaviyo-automation/SKILL.md) | Automate Klaviyo tasks via Rube MCP (Composio): manage email/SMS campaigns, inspect campaign messages, track tags, and monitor send jobs. Always search tools first for current s... |
| [`lex`](skills/lex/SKILL.md) | Centralized 'Truth Engine' for cross-jurisdictional legal context (US, EU, CA) and contract scaffolding. |
| [`lightning-factory-explainer`](skills/lightning-factory-explainer/SKILL.md) | Explain Bitcoin Lightning channel factories and the SuperScalar protocol — scalable Lightning onboarding using shared UTXOs, Decker-Wattenhofer trees, timeout-signature trees, M... |
| [`linkedin-automation`](skills/linkedin-automation/SKILL.md) | Automate LinkedIn tasks via Rube MCP (Composio): create posts, manage profile, company info, comments, and image uploads. Always search tools first for current schemas. |
| [`linkedin-cli`](skills/linkedin-cli/SKILL.md) | Use when automating LinkedIn via CLI: fetch profiles, search people/companies, send messages, manage connections, create posts, and Sales Navigator. |
| [`mailchimp-automation`](skills/mailchimp-automation/SKILL.md) | Automate Mailchimp email marketing including campaigns, audiences, subscribers, segments, and analytics via Rube MCP (Composio). Always search tools first for current schemas. |
| [`marketing-ideas`](skills/marketing-ideas/SKILL.md) | Provide proven marketing strategies and growth ideas for SaaS and software products, prioritized using a marketing feasibility scoring system. |
| [`memory-safety-patterns`](skills/memory-safety-patterns/SKILL.md) | Cross-language patterns for memory-safe programming including RAII, ownership, smart pointers, and resource management. |
| [`micro-saas-launcher`](skills/micro-saas-launcher/SKILL.md) | You ship fast and iterate. You know the difference between a side project and a business. You've seen what works in the indie hacker community. You help people go from idea to p... |
| [`microsoft-teams-automation`](skills/microsoft-teams-automation/SKILL.md) | Automate Microsoft Teams tasks via Rube MCP (Composio): send messages, manage channels, create meetings, handle chats, and search messages. Always search tools first for current... |
| [`mixpanel-automation`](skills/mixpanel-automation/SKILL.md) | Automate Mixpanel tasks via Rube MCP (Composio): events, segmentation, funnels, cohorts, user profiles, JQL queries. Always search tools first for current schemas. |
| [`monorepo-management`](skills/monorepo-management/SKILL.md) | Build efficient, scalable monorepos that enable code sharing, consistent tooling, and atomic changes across multiple packages and applications. |
| [`onboarding-cro`](skills/onboarding-cro/SKILL.md) | You are an expert in user onboarding and activation. Your goal is to help users reach their \"aha moment\" as quickly as possible and establish habits that lead to long-term ret... |
| [`onboarding-psychologist`](skills/onboarding-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`paywall-upgrade-cro`](skills/paywall-upgrade-cro/SKILL.md) | You are an expert in in-app paywalls and upgrade flows. Your goal is to convert free users to paid, or upgrade users to higher tiers, at moments when they've experienced enough ... |
| [`pitch-psychologist`](skills/pitch-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`posthog-automation`](skills/posthog-automation/SKILL.md) | Automate PostHog tasks via Rube MCP (Composio): events, feature flags, projects, user profiles, annotations. Always search tools first for current schemas. |
| [`price-psychology-strategist`](skills/price-psychology-strategist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`product-marketing-context`](skills/product-marketing-context/SKILL.md) | Create or update a reusable product marketing context document with positioning, audience, ICP, use cases, and messaging. Use at the start of a project to avoid repeating core m... |
| [`reddit-automation`](skills/reddit-automation/SKILL.md) | Automate Reddit tasks via Rube MCP (Composio): search subreddits, create posts, manage comments, and browse top content. Always search tools first for current schemas. |
| [`sales-automator`](skills/sales-automator/SKILL.md) | Draft cold emails, follow-ups, and proposal templates. Creates pricing pages, case studies, and sales scripts. Use PROACTIVELY for sales outreach or lead nurturing. |
| [`scarcity-urgency-psychologist`](skills/scarcity-urgency-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`segment-automation`](skills/segment-automation/SKILL.md) | Automate Segment tasks via Rube MCP (Composio): track events, identify users, manage groups, page views, aliases, batch operations. Always search tools first for current schemas. |
| [`segment-cdp`](skills/segment-cdp/SKILL.md) | Client-side tracking with Analytics.js. Include track, identify, page, and group calls. Anonymous ID persists until identify merges with user. |
| [`seo-aeo-blog-writer`](skills/seo-aeo-blog-writer/SKILL.md) | Writes long-form blog posts with TL;DR block, definition sentence, comparison table, and 5-question FAQ for SEO ranking and AEO citation. Activate when the user wants to write a... |
| [`seo-aeo-internal-linking`](skills/seo-aeo-internal-linking/SKILL.md) | Maps internal link opportunities between pages with anchor text, placement instructions, orphan page detection, and cannibalization checks. Activate when the user wants to build... |
| [`seo-aeo-keyword-research`](skills/seo-aeo-keyword-research/SKILL.md) | Researches and prioritises SEO keywords with AEO question queries, difficulty tiers, cannibalization checks, and a content map. Activate when the user wants to find keywords, re... |
| [`seo-aeo-landing-page-writer`](skills/seo-aeo-landing-page-writer/SKILL.md) | Writes complete, structured landing pages optimized for SEO ranking, AEO citation, and visitor conversion. Activate when the user wants to write or generate a landing page for a... |
| [`seo-aeo-meta-description-generator`](skills/seo-aeo-meta-description-generator/SKILL.md) | Writes 3 title tag variants and 3 meta description variants per page with SERP preview, OG tags, and Twitter Card tags. Activate when the user wants to write meta tags, title ta... |
| [`seo-aeo-schema-generator`](skills/seo-aeo-schema-generator/SKILL.md) | Generates valid JSON-LD structured data for 10 schema types with rich result eligibility validation and implementation-ready script blocks. Activate when the user wants to gener... |
| [`seo-cannibalization-detector`](skills/seo-cannibalization-detector/SKILL.md) | Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. Suggests differentiation strategies. Use PROACTIVELY when reviewing similar co... |
| [`seo-competitor-pages`](skills/seo-competitor-pages/SKILL.md) | > Generate SEO-optimized competitor comparison and alternatives pages. Covers "X vs Y" layouts, "alternatives to X" pages, feature matrices, schema markup, and conversion optimi... |
| [`seo-content-refresher`](skills/seo-content-refresher/SKILL.md) | Identifies outdated elements in provided content and suggests updates to maintain freshness. Finds statistics, dates, and examples that need updating. Use PROACTIVELY for older ... |
| [`seo-content-writer`](skills/seo-content-writer/SKILL.md) | Writes SEO-optimized content based on provided keywords and topic briefs. Creates engaging, comprehensive content following best practices. Use PROACTIVELY for content creation ... |
| [`seo-dataforseo`](skills/seo-dataforseo/SKILL.md) | Use DataForSEO for live SERPs, keyword metrics, backlinks, competitor analysis, on-page checks, and AI visibility data. Trigger when the user needs real SEO data rather than sta... |
| [`seo-fundamentals`](skills/seo-fundamentals/SKILL.md) | Core principles of SEO including E-E-A-T, Core Web Vitals, technical foundations, content quality, and how modern search engines evaluate pages. |
| [`seo-keyword-strategist`](skills/seo-keyword-strategist/SKILL.md) | Analyzes keyword usage in provided content, calculates density, suggests semantic variations and LSI keywords based on the topic. Prevents over-optimization. Use PROACTIVELY for... |
| [`seo-meta-optimizer`](skills/seo-meta-optimizer/SKILL.md) | Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. Generates compelling, keyword-rich metadata. Use PROACTIVELY for n... |
| [`seo-schema`](skills/seo-schema/SKILL.md) | > Detect, validate, and generate Schema.org structured data. JSON-LD format preferred. Use when user says "schema", "structured data", "rich results", "JSON-LD", or "markup". |
| [`seo-sitemap`](skills/seo-sitemap/SKILL.md) | > Analyze existing XML sitemaps or generate new ones with industry templates. Validates format, URLs, and structure. Use when user says "sitemap", "generate sitemap", "sitemap i... |
| [`seo-snippet-hunter`](skills/seo-snippet-hunter/SKILL.md) | Formats content to be eligible for featured snippets and SERP features. Creates snippet-optimized content blocks based on best practices. Use PROACTIVELY for question-based cont... |
| [`sequence-psychologist`](skills/sequence-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`shopify-automation`](skills/shopify-automation/SKILL.md) | Automate Shopify tasks via Rube MCP (Composio): products, orders, customers, inventory, collections. Always search tools first for current schemas. |
| [`signup-flow-cro`](skills/signup-flow-cro/SKILL.md) | You are an expert in optimizing signup and registration flows. Your goal is to reduce friction, increase completion rates, and set users up for successful activation. |
| [`social-content`](skills/social-content/SKILL.md) | You are an expert social media strategist with direct access to a scheduling platform that publishes to all major social networks. Your goal is to help create engaging content t... |
| [`subject-line-psychologist`](skills/subject-line-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`tiktok-automation`](skills/tiktok-automation/SKILL.md) | Automate TikTok tasks via Rube MCP (Composio): upload/publish videos, post photos, manage content, and view user profiles/stats. Always search tools first for current schemas. |
| [`tutorial-engineer`](skills/tutorial-engineer/SKILL.md) | Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with hands-on examples. |
| [`twitter-automation`](skills/twitter-automation/SKILL.md) | Automate Twitter/X tasks via Rube MCP (Composio): posts, search, users, bookmarks, lists, media. Always search tools first for current schemas. |
| [`viboscope`](skills/viboscope/SKILL.md) | Psychological compatibility matching — find cofounders, collaborators, and friends through validated psychometrics |
| [`viral-generator-builder`](skills/viral-generator-builder/SKILL.md) | You understand why people share things. You build tools that create \"identity moments\" - results people want to show off. You know the difference between a tool people use onc... |
| [`wiki-onboarding`](skills/wiki-onboarding/SKILL.md) | Generate two complementary onboarding documents that together give any engineer — from newcomer to principal — a complete understanding of a codebase. Use when user asks for onb... |
| [`x-article-publisher-skill`](skills/x-article-publisher-skill/SKILL.md) | Publish articles to X/Twitter |
| [`youtube-automation`](skills/youtube-automation/SKILL.md) | Automate YouTube tasks via Rube MCP (Composio): upload videos, manage playlists, search content, get analytics, and handle comments. Always search tools first for current schemas. |
| [`youtube-summarizer`](skills/youtube-summarizer/SKILL.md) | Extract transcripts from YouTube videos and generate comprehensive, detailed summaries using intelligent analysis frameworks |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="science_specialized"></a>
### 🔬 Ciência, Saúde, Domínios Especializados & Web3
*Bibliotecas científicas (Astropy, SciPy, BioPython, Qiskit), saúde, medicina, análise jurídica, leilões, Web3 e FinTech.* (38 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`20-andruia-niche-intelligence`](skills/20-andruia-niche-intelligence/SKILL.md) | Estratega de Inteligencia de Dominio de Andru.ia. Analiza el nicho específico de un proyecto para inyectar conocimientos, regulaciones y estándares únicos del sector. Actívalo t... |
| [`advogado-criminal`](skills/advogado-criminal/SKILL.md) | Advogado criminalista especializado em Maria da Penha, violencia domestica, feminicidio, direito penal brasileiro, medidas protetivas, inquerito policial e acao penal. |
| [`blockchain-developer`](skills/blockchain-developer/SKILL.md) | Build production-ready Web3 applications, smart contracts, and decentralized systems. Implements DeFi protocols, NFT platforms, DAOs, and enterprise blockchain integrations. |
| [`defi-protocol-templates`](skills/defi-protocol-templates/SKILL.md) | Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and lending systems. Use when building decentralized finance applications or smart contra... |
| [`employment-contract-templates`](skills/employment-contract-templates/SKILL.md) | Templates and patterns for creating legally sound employment documentation including contracts, offer letters, and HR policies. |
| [`energy-procurement`](skills/energy-procurement/SKILL.md) | Codified expertise for electricity and gas procurement, tariff optimisation, demand charge management, renewable PPA evaluation, and multi-facility energy cost management. |
| [`family-health-analyzer`](skills/family-health-analyzer/SKILL.md) | 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议 |
| [`fitness-analyzer`](skills/fitness-analyzer/SKILL.md) | 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。 |
| [`game-development`](skills/game-development/SKILL.md) | Game development orchestrator. Routes to platform-specific skills based on project needs. |
| [`godot-gdscript-patterns`](skills/godot-gdscript-patterns/SKILL.md) | Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. Use when building Godot games, implementing game systems, or learning GDScript best... |
| [`health-trend-analyzer`](skills/health-trend-analyzer/SKILL.md) | 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体重/BMI、症状、药物依从性、化验结果、情绪睡眠），相关性分析，变化检测，以及交互式HTML可视化报告（EChart... |
| [`internal-comms-community`](skills/internal-comms-community/SKILL.md) | To write internal communications, use this skill for: |
| [`leiloeiro-avaliacao`](skills/leiloeiro-avaliacao/SKILL.md) | Avaliacao pericial de imoveis em leilao. Valor de mercado, liquidacao forcada, ABNT NBR 14653, metodos comparativo/renda/custo, CUB e margem de seguranca. |
| [`leiloeiro-ia`](skills/leiloeiro-ia/SKILL.md) | Especialista em leiloes judiciais e extrajudiciais de imoveis. Analise juridica, pericial e de mercado integrada. Orquestra os 5 modulos especializados. |
| [`leiloeiro-juridico`](skills/leiloeiro-juridico/SKILL.md) | Analise juridica de leiloes: nulidades, bem de familia, alienacao fiduciaria, CPC arts 829-903, Lei 9514/97, onus reais, embargos e jurisprudencia. |
| [`leiloeiro-mercado`](skills/leiloeiro-mercado/SKILL.md) | Analise de mercado imobiliario para leiloes. Liquidez, desagio tipico, ROI, estrategias de saida (flip/reforma/renda), Selic 2025 e benchmark CDI/FII. |
| [`logistics-exception-management`](skills/logistics-exception-management/SKILL.md) | Codified expertise for handling freight exceptions, shipment delays, damages, losses, and carrier disputes. Informed by logistics professionals with 15+ years operational experi... |
| [`matplotlib`](skills/matplotlib/SKILL.md) | Matplotlib is Python's foundational visualization library for creating static, animated, and interactive plots. |
| [`maxia`](skills/maxia/SKILL.md) | Connect to MAXIA AI-to-AI marketplace on Solana. Discover, buy, sell AI services. Earn USDC. 13 MCP tools, A2A protocol, DeFi yields, sentiment analysis, rug detection. |
| [`mental-health-analyzer`](skills/mental-health-analyzer/SKILL.md) | 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。 |
| [`networkx`](skills/networkx/SKILL.md) | NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs. |
| [`nft-standards`](skills/nft-standards/SKILL.md) | Master ERC-721 and ERC-1155 NFT standards, metadata best practices, and advanced NFT features. |
| [`nutrition-analyzer`](skills/nutrition-analyzer/SKILL.md) | 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。 |
| [`occupational-health-analyzer`](skills/occupational-health-analyzer/SKILL.md) | 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。 |
| [`oral-health-analyzer`](skills/oral-health-analyzer/SKILL.md) | 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。 |
| [`qiskit`](skills/qiskit/SKILL.md) | Qiskit is the world's most popular open-source quantum computing framework with 13M+ downloads. Build quantum circuits, optimize for hardware, execute on simulators or real quan... |
| [`rehabilitation-analyzer`](skills/rehabilitation-analyzer/SKILL.md) | 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议 |
| [`scikit-learn`](skills/scikit-learn/SKILL.md) | Machine learning in Python with scikit-learn. Use for classification, regression, clustering, model evaluation, and ML pipelines. |
| [`seaborn`](skills/seaborn/SKILL.md) | Seaborn is a Python visualization library for creating publication-quality statistical graphics. Use this skill for dataset-oriented plotting, multivariate analysis, automatic s... |
| [`sexual-health-analyzer`](skills/sexual-health-analyzer/SKILL.md) | Sexual Health Analyzer |
| [`skin-health-analyzer`](skills/skin-health-analyzer/SKILL.md) | Analyze skin health data, identify skin problem patterns, assess skin health status. Supports correlation analysis with nutrition, chronic diseases, and medication data. |
| [`sleep-analyzer`](skills/sleep-analyzer/SKILL.md) | 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。 |
| [`sred-project-organizer`](skills/sred-project-organizer/SKILL.md) | Take a list of projects and their related documentation, and organize them into the SRED format for submission. |
| [`startup-business-analyst-market-opportunity`](skills/startup-business-analyst-market-opportunity/SKILL.md) | Generate comprehensive market opportunity analysis with TAM/SAM/SOM calculations |
| [`sympy`](skills/sympy/SKILL.md) | SymPy is a Python library for symbolic mathematics that enables exact computation using mathematical symbols rather than numerical approximations. |
| [`travel-health-analyzer`](skills/travel-health-analyzer/SKILL.md) | 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。 |
| [`typescript-pro`](skills/typescript-pro/SKILL.md) | Master TypeScript with advanced types, generics, and strict type safety. Handles complex type systems, decorators, and enterprise-grade patterns. |
| [`wellally-tech`](skills/wellally-tech/SKILL.md) | Integrate multiple digital health data sources, connect to [WellAlly.tech](https://www.wellally.tech/) knowledge base, providing data import and knowledge reference for personal... |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

<a id="general_utilities"></a>
### 🛠️ Utilitários, Ferramentas & Suporte Geral
*Ferramentas auxiliares, formatadores, conversores e utilitários gerais para suporte ao desenvolvimento.* (100 skills)

| Skill | Descrição e Propósito Operacional |
| :--- | :--- |
| [`00-andruia-consultant`](skills/00-andruia-consultant/SKILL.md) | Arquitecto de Soluciones Principal y Consultor Tecnológico de Andru.ia. Diagnostica y traza la hoja de ruta óptima para proyectos de IA en español. |
| [`10-andruia-skill-smith`](skills/10-andruia-skill-smith/SKILL.md) | Ingeniero de Sistemas de Andru.ia. Diseña, redacta y despliega nuevas habilidades (skills) dentro del repositorio siguiendo el Estándar de Diamante. |
| [`acceptance-orchestrator`](skills/acceptance-orchestrator/SKILL.md) | Use when a coding task should be driven end-to-end from issue intake through implementation, review, deployment, and acceptance verification with minimal human re-intervention. |
| [`algorithmic-art`](skills/algorithmic-art/SKILL.md) | Algorithmic philosophies are computational aesthetic movements that are then expressed through code. Output .md files (philosophy), .html files (interactive viewer), and .js fil... |
| [`alpha-vantage`](skills/alpha-vantage/SKILL.md) | Access 20+ years of global financial data: equities, options, forex, crypto, commodities, economic indicators, and 50+ technical indicators. |
| [`antigravity-skill-orchestrator`](skills/antigravity-skill-orchestrator/SKILL.md) | A meta-skill that understands task requirements, dynamically selects appropriate skills, tracks successful skill combinations using agent-memory-mcp, and prevents skill overuse ... |
| [`app-builder`](skills/app-builder/SKILL.md) | Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates agents. |
| [`ask-questions-if-underspecified`](skills/ask-questions-if-underspecified/SKILL.md) | Clarify requirements before implementing. Use when serious doubts arise. |
| [`basecamp-automation`](skills/basecamp-automation/SKILL.md) | Automate Basecamp project management, to-dos, messages, people, and to-do list organization via Rube MCP (Composio). Always search tools first for current schemas. |
| [`beautiful-prose`](skills/beautiful-prose/SKILL.md) | A hard-edged writing style contract for timeless, forceful English prose without modern AI tics. Use when users ask for prose or rewrites that must be clean, exact, concrete, an... |
| [`behavioral-modes`](skills/behavioral-modes/SKILL.md) | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type. |
| [`billing-automation`](skills/billing-automation/SKILL.md) | Master automated billing systems including recurring billing, invoice generation, dunning management, proration, and tax calculation. |
| [`bitbucket-automation`](skills/bitbucket-automation/SKILL.md) | Automate Bitbucket repositories, pull requests, branches, issues, and workspace management via Rube MCP (Composio). Always search tools first for current schemas. |
| [`build`](skills/build/SKILL.md) | build |
| [`cc-skill-project-guidelines-example`](skills/cc-skill-project-guidelines-example/SKILL.md) | Project Guidelines Skill (Example) |
| [`citation-management`](skills/citation-management/SKILL.md) | Manage citations systematically throughout the research and writing process. |
| [`code-simplifier`](skills/code-simplifier/SKILL.md) | Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Use when asked to "simplify code", "clean up code", "refactor for c... |
| [`competitive-landscape`](skills/competitive-landscape/SKILL.md) | Comprehensive frameworks for analyzing competition, identifying differentiation opportunities, and developing winning market positioning strategies. |
| [`competitor-alternatives`](skills/competitor-alternatives/SKILL.md) | You are an expert in creating competitor comparison and alternative pages. Your goal is to build pages that rank for competitive search terms, provide genuine value to evaluator... |
| [`comprehensive-review-full-review`](skills/comprehensive-review-full-review/SKILL.md) | Use when working with comprehensive review full review |
| [`constant-time-analysis`](skills/constant-time-analysis/SKILL.md) | Analyze cryptographic code to detect operations that leak secret data through execution timing variations. |
| [`create-issue-gate`](skills/create-issue-gate/SKILL.md) | Use when starting a new implementation task and an issue must be created with strict acceptance criteria gating before execution. |
| [`daily`](skills/daily/SKILL.md) | Documentation and capabilities reference for Daily |
| [`dispatching-parallel-agents`](skills/dispatching-parallel-agents/SKILL.md) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| [`emergency-card`](skills/emergency-card/SKILL.md) | 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。 |
| [`environment-setup-guide`](skills/environment-setup-guide/SKILL.md) | Guide developers through setting up development environments with proper tools, dependencies, and configurations |
| [`explain-like-socrates`](skills/explain-like-socrates/SKILL.md) | > Explains concepts using Socratic-style dialogue. Use when the user asks to explain, teach or help understand a concept like socrates. |
| [`file-organizer`](skills/file-organizer/SKILL.md) | 6. Reduces Clutter: Identifies old files you probably don't need anymore |
| [`filesystem-context`](skills/filesystem-context/SKILL.md) | Use for file-based context management, dynamic context discovery, and reducing context window bloat. Offload context to files for just-in-time loading. |
| [`framework-migration-legacy-modernize`](skills/framework-migration-legacy-modernize/SKILL.md) | Orchestrate a comprehensive legacy system modernization using the strangler fig pattern, enabling gradual replacement of outdated components while maintaining continuous busines... |
| [`full-stack-orchestration-full-stack-feature`](skills/full-stack-orchestration-full-stack-feature/SKILL.md) | Use when working with full stack orchestration full stack feature |
| [`goal-analyzer`](skills/goal-analyzer/SKILL.md) | 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| [`googlesheets-automation`](skills/googlesheets-automation/SKILL.md) | Automate Google Sheets operations (read, write, format, filter, manage spreadsheets) via Rube MCP (Composio). Read/write data, manage tabs, apply formatting, and search rows pro... |
| [`i18n-localization`](skills/i18n-localization/SKILL.md) | Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support. |
| [`identity-mirror`](skills/identity-mirror/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`interactive-portfolio`](skills/interactive-portfolio/SKILL.md) | You know a portfolio isn't a resume - it's a first impression that needs to convert. You balance creativity with usability. You understand that hiring managers spend 30 seconds ... |
| [`internal-comms-anthropic`](skills/internal-comms-anthropic/SKILL.md) | To write internal communications, use this skill for: |
| [`interview-coach`](skills/interview-coach/SKILL.md) | Full job search coaching system — JD decoding, resume, storybank, mock interviews, transcript analysis, comp negotiation. 23 commands, persistent state. |
| [`iterate-pr`](skills/iterate-pr/SKILL.md) | Iterate on a PR until CI passes. Use when you need to fix CI failures, address review feedback, or continuously push fixes until all checks are green. Automates the feedback-fix... |
| [`jobgpt`](skills/jobgpt/SKILL.md) | Job search automation, auto apply, resume generation, application tracking, salary intelligence, and recruiter outreach using the JobGPT MCP server. |
| [`latex-paper-conversion`](skills/latex-paper-conversion/SKILL.md) | This skill should be used when the user asks to convert an academic paper in LaTeX from one format (e.g., Springer, IPOL) to another format (e.g., MDPI, IEEE, Nature). It automa... |
| [`market-sizing-analysis`](skills/market-sizing-analysis/SKILL.md) | Comprehensive market sizing methodologies for calculating Total Addressable Market (TAM), Serviceable Available Market (SAM), and Serviceable Obtainable Market (SOM) for startup... |
| [`miro-automation`](skills/miro-automation/SKILL.md) | Automate Miro tasks via Rube MCP (Composio): boards, items, sticky notes, frames, sharing, connectors. Always search tools first for current schemas. |
| [`mlops-engineer`](skills/mlops-engineer/SKILL.md) | Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools. |
| [`modern-javascript-patterns`](skills/modern-javascript-patterns/SKILL.md) | Comprehensive guide for mastering modern JavaScript (ES6+) features, functional programming patterns, and best practices for writing clean, maintainable, and performant code. |
| [`moyu`](skills/moyu/SKILL.md) | > Anti-over-engineering guardrail that activates when an AI coding agent expands scope, adds abstractions, or changes files the user did not request. |
| [`multi-advisor`](skills/multi-advisor/SKILL.md) | Conselho de especialistas — consulta multiplos agentes do ecossistema em paralelo para analise multi-perspectiva de qualquer topico. Ativa personas, especialistas e agentes tecn... |
| [`nanobanana-ppt-skills`](skills/nanobanana-ppt-skills/SKILL.md) | AI-powered PPT generation with document analysis and styled images |
| [`new-rails-project`](skills/new-rails-project/SKILL.md) | Create a new Rails project |
| [`objection-preemptor`](skills/objection-preemptor/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`one-drive-automation`](skills/one-drive-automation/SKILL.md) | Automate OneDrive file management, search, uploads, downloads, sharing, permissions, and folder operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`oss-hunter`](skills/oss-hunter/SKILL.md) | Automatically hunt for high-impact OSS contribution opportunities in trending repositories. |
| [`parallel-agents`](skills/parallel-agents/SKILL.md) | Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis requires multiple perspectives. |
| [`pdf-official`](skills/pdf-official/SKILL.md) | This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see refe... |
| [`personal-tool-builder`](skills/personal-tool-builder/SKILL.md) | You believe the best tools come from real problems. You've built dozens of personal tools - some stayed personal, others became products used by thousands. You know that buildin... |
| [`product-manager`](skills/product-manager/SKILL.md) | Senior PM agent with 6 knowledge domains, 30+ frameworks, 12 templates, and 32 SaaS metrics with formulas. Pure Markdown, zero scripts. |
| [`product-manager-toolkit`](skills/product-manager-toolkit/SKILL.md) | Essential tools and frameworks for modern product management, from discovery to delivery. |
| [`production-scheduling`](skills/production-scheduling/SKILL.md) | Codified expertise for production scheduling, job sequencing, line balancing, changeover optimisation, and bottleneck resolution in discrete and batch manufacturing. |
| [`professional-proofreader`](skills/professional-proofreader/SKILL.md) | > Use when a user asks to "proofread", "review and correct", "fix grammar", "improve readability while keeping my voice", and to proofread a document file and save an updated ve... |
| [`progressive-estimation`](skills/progressive-estimation/SKILL.md) | Estimate AI-assisted and hybrid human+agent development work with research-backed PERT statistics and calibration feedback loops |
| [`python-packaging`](skills/python-packaging/SKILL.md) | Comprehensive guide to creating, structuring, and distributing Python packages using modern packaging tools, pyproject.toml, and publishing to PyPI. |
| [`python-patterns`](skills/python-patterns/SKILL.md) | Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not copying. |
| [`quality-nonconformance`](skills/quality-nonconformance/SKILL.md) | Codified expertise for quality control, non-conformance investigation, root cause analysis, corrective action, and supplier quality management in regulated manufacturing. |
| [`readme`](skills/readme/SKILL.md) | You are an expert technical writer creating comprehensive project documentation. Your goal is to write a README.md that is absurdly thorough—the kind of documentation you wish e... |
| [`risk-manager`](skills/risk-manager/SKILL.md) | Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and implements stop-losses. |
| [`risk-metrics-calculation`](skills/risk-metrics-calculation/SKILL.md) | Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or building risk monit... |
| [`robius-event-action`](skills/robius-event-action/SKILL.md) | \| CRITICAL: Use for Robius event and action patterns. Triggers on: custom action, MatchEvent, post_action, cx.widget_action, handle_actions, DefaultNone, widget action, event h... |
| [`robius-state-management`](skills/robius-state-management/SKILL.md) | \| CRITICAL: Use for Robius state management patterns. Triggers on: AppState, persistence, theme switch, 状态管理, Scope::with_data, save state, load state, serde, 状态持久化, 主题切换 |
| [`sales-enablement`](skills/sales-enablement/SKILL.md) | Create sales collateral such as decks, one-pagers, objection docs, demo scripts, playbooks, and proposal templates. Use when a sales team needs assets that help reps move deals ... |
| [`scientific-writing`](skills/scientific-writing/SKILL.md) | This is the core skill for the deep research and writing tool—combining AI-driven deep research with well-formatted written outputs. Every document produced is backed by compreh... |
| [`search-specialist`](skills/search-specialist/SKILL.md) | Expert web researcher using advanced search techniques and |
| [`senior-fullstack`](skills/senior-fullstack/SKILL.md) | Complete toolkit for senior fullstack with modern tools and best practices. |
| [`sharp-edges`](skills/sharp-edges/SKILL.md) | sharp-edges |
| [`skill-creator`](skills/skill-creator/SKILL.md) | To create new CLI skills following Anthropic's official best practices with zero manual configuration. This skill automates brainstorming, template application, validation, and ... |
| [`skill-rails-upgrade`](skills/skill-rails-upgrade/SKILL.md) | Analyze Rails apps and provide upgrade assessments |
| [`skill-repair`](skills/skill-repair/SKILL.md) | \| Use this to fix and re-install agent skills that have failed installation. This skill provides the necessary context and permissions to surgically update the `manifest.json` ... |
| [`skill-router`](skills/skill-router/SKILL.md) | Use when the user is unsure which skill to use or where to start. Interviews the user with targeted questions and recommends the best skill(s) from the installed library for the... |
| [`skill-writer`](skills/skill-writer/SKILL.md) | Create and improve agent skills following the Agent Skills specification. Use when asked to create, write, or update skills. |
| [`speckit-updater`](skills/speckit-updater/SKILL.md) | SpecKit Safe Update |
| [`startup-business-analyst-business-case`](skills/startup-business-analyst-business-case/SKILL.md) | Generate comprehensive investor-ready business case document with market, solution, financials, and strategy |
| [`tcm-constitution-analyzer`](skills/tcm-constitution-analyzer/SKILL.md) | 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| [`telegram-automation`](skills/telegram-automation/SKILL.md) | Automate Telegram tasks via Rube MCP (Composio): send messages, manage chats, share photos/documents, and handle bot commands. Always search tools first for current schemas. |
| [`todoist-automation`](skills/todoist-automation/SKILL.md) | Automate Todoist task management, projects, sections, filtering, and bulk operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`tool-use-guardian`](skills/tool-use-guardian/SKILL.md) | FREE — Intelligent tool-call reliability wrapper. Monitors, retries, fixes, and learns from tool failures. Auto-recovers from truncated JSON, timeouts, rate limits, and mid-chai... |
| [`typescript-advanced-types`](skills/typescript-advanced-types/SKILL.md) | Comprehensive guidance for mastering TypeScript's advanced type system including generics, conditional types, mapped types, template literal types, and utility types for buildin... |
| [`unsplash-integration`](skills/unsplash-integration/SKILL.md) | Integration skill for searching and fetching high-quality, free-to-use professional photography from Unsplash. |
| [`using-git-worktrees`](skills/using-git-worktrees/SKILL.md) | Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching. |
| [`ux-persuasion-engineer`](skills/ux-persuasion-engineer/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`vercel-automation`](skills/vercel-automation/SKILL.md) | Automate Vercel tasks via Rube MCP (Composio): manage deployments, domains, DNS, env vars, projects, and teams. Always search tools first for current schemas. |
| [`vercel-deployment`](skills/vercel-deployment/SKILL.md) | Expert knowledge for deploying to Vercel with Next.js Use when: vercel, deploy, deployment, hosting, production. |
| [`verification-before-completion`](skills/verification-before-completion/SKILL.md) | Claiming work is complete without verification is dishonesty, not efficiency. Use when ANY variation of success/completion claims, ANY expression of satisfaction, or ANY positiv... |
| [`visual-emotion-engineer`](skills/visual-emotion-engineer/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`webflow-automation`](skills/webflow-automation/SKILL.md) | Automate Webflow CMS collections, site publishing, page management, asset uploads, and ecommerce orders via Rube MCP (Composio). Always search tools first for current schemas. |
| [`weightloss-analyzer`](skills/weightloss-analyzer/SKILL.md) | 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段 |
| [`wiki-changelog`](skills/wiki-changelog/SKILL.md) | Generate structured changelogs from git history. Use when user asks \"what changed recently\", \"generate a changelog\", \"summarize commits\" or user wants to understand recent... |
| [`wiki-page-writer`](skills/wiki-page-writer/SKILL.md) | You are a senior documentation engineer that generates comprehensive technical documentation pages with evidence-based depth. |
| [`wiki-vitepress`](skills/wiki-vitepress/SKILL.md) | Transform generated wiki Markdown files into a polished VitePress static site with dark theme and interactive Mermaid diagrams. Use when user asks to \"build a site\" or \"packa... |
| [`windows-shell-reliability`](skills/windows-shell-reliability/SKILL.md) | Reliable command execution on Windows: paths, encoding, and common binary pitfalls. |
| [`writing-skills`](skills/writing-skills/SKILL.md) | Use when creating, updating, or improving agent skills. |
| [`xlsx-official`](skills/xlsx-official/SKILL.md) | Unless otherwise stated by the user or existing template |

[⬆ Voltar ao Topo](#-wsp-agent-skills-ecosystem)

---

## 🔤 Índice Alfabético Completo (A-Z)

Consulte rapidamente qualquer skill pelo seu identificador único:

[A](#indice-a) [B](#indice-b) [C](#indice-c) [D](#indice-d) [E](#indice-e) [F](#indice-f) [G](#indice-g) [H](#indice-h) [I](#indice-i) [J](#indice-j) [K](#indice-k) [L](#indice-l) [M](#indice-m) [N](#indice-n) [O](#indice-o) [P](#indice-p) [Q](#indice-q) [R](#indice-r) [S](#indice-s) [T](#indice-t) [U](#indice-u) [V](#indice-v) [W](#indice-w) [X](#indice-x) [Y](#indice-y) [Z](#indice-z) [#](#indice-num)

<a id="indice-a"></a>
### Letra A (239 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`ab-test-setup`](skills/ab-test-setup/SKILL.md) | Structured guide for setting up A/B tests with mandatory gates for hypothesis, metrics, and execution readiness. |
| [`acceptance-orchestrator`](skills/acceptance-orchestrator/SKILL.md) | Use when a coding task should be driven end-to-end from issue intake through implementation, review, deployment, and acceptance verification with minimal human re-intervention. |
| [`accessibility-compliance-accessibility-audit`](skills/accessibility-compliance-accessibility-audit/SKILL.md) | You are an accessibility expert specializing in WCAG compliance, inclusive design, and assistive technology compatibility. Conduct audits, identify barriers, and provide remedia... |
| [`accidental-data-loss-prevention`](skills/accidental-data-loss-prevention/SKILL.md) | \| **STOP AND VERIFY**: Before running any command or tool that results in irreversible data loss, you MUST obtain explicit user consent. When in doubt, ask. It is better to wai... |
| [`active-directory-attacks`](skills/active-directory-attacks/SKILL.md) | Provide comprehensive techniques for attacking Microsoft Active Directory environments. Covers reconnaissance, credential harvesting, Kerberos attacks, lateral movement, privile... |
| [`activecampaign-automation`](skills/activecampaign-automation/SKILL.md) | Automate ActiveCampaign tasks via Rube MCP (Composio): manage contacts, tags, list subscriptions, automation enrollment, and tasks. Always search tools first for current schemas. |
| [`ad-creative`](skills/ad-creative/SKILL.md) | Create, iterate, and scale paid ad creative for Google Ads, Meta, LinkedIn, TikTok, and similar platforms. Use when generating headlines, descriptions, primary text, or large se... |
| [`address-github-comments`](skills/address-github-comments/SKILL.md) | Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI. |
| [`adhx`](skills/adhx/SKILL.md) | Fetch any X/Twitter post as clean LLM-friendly JSON. Converts x.com, twitter.com, or adhx.com links into structured data with full article content, author info, and engagement m... |
| [`advanced-evaluation`](skills/advanced-evaluation/SKILL.md) | This skill should be used when the user asks to "implement LLM-as-judge", "compare model outputs", "create evaluation rubrics", "mitigate evaluation bias", or mentions direct sc... |
| [`advogado-criminal`](skills/advogado-criminal/SKILL.md) | Advogado criminalista especializado em Maria da Penha, violencia domestica, feminicidio, direito penal brasileiro, medidas protetivas, inquerito policial e acao penal. |
| [`advogado-especialista`](skills/advogado-especialista/SKILL.md) | Advogado especialista em todas as areas do Direito brasileiro: familia, criminal, trabalhista, tributario, consumidor, imobiliario, empresarial, civil e constitucional. |
| [`aegisops-ai`](skills/aegisops-ai/SKILL.md) | Autonomous DevSecOps & FinOps Guardrails. Orchestrates Gemini 3 Flash to audit Linux Kernel patches, Terraform cost drifts, and K8s compliance. |
| [`agent-evaluation`](skills/agent-evaluation/SKILL.md) | You're a quality engineer who has seen agents that aced benchmarks fail spectacularly in production. You've learned that evaluating LLM agents is fundamentally different from te... |
| [`agent-framework-azure-ai-py`](skills/agent-framework-azure-ai-py/SKILL.md) | Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK. |
| [`agent-manager-skill`](skills/agent-manager-skill/SKILL.md) | Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling. |
| [`agent-memory-mcp`](skills/agent-memory-mcp/SKILL.md) | A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions). |
| [`agent-memory-systems`](skills/agent-memory-systems/SKILL.md) | You are a cognitive architect who understands that memory makes agents intelligent. You've built memory systems for agents handling millions of interactions. You know that the h... |
| [`agent-orchestration-improve-agent`](skills/agent-orchestration-improve-agent/SKILL.md) | Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration. |
| [`agent-orchestration-multi-agent-optimize`](skills/agent-orchestration-multi-agent-optimize/SKILL.md) | Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration. Use when improving agent performance, throughput, or reliability. |
| [`agent-orchestrator`](skills/agent-orchestrator/SKILL.md) | Meta-skill que orquestra todos os agentes do ecossistema. Scan automatico de skills, match por capacidades, coordenacao de workflows multi-skill e registry management. |
| [`agent-tool-builder`](skills/agent-tool-builder/SKILL.md) | You are an expert in the interface between LLMs and the outside world. You've seen tools that work beautifully and tools that cause agents to hallucinate, loop, or fail silently... |
| [`agentflow`](skills/agentflow/SKILL.md) | Orchestrate autonomous AI development pipelines through your Kanban board (Asana, GitHub Projects, Linear). Manages multi-worker Claude Code dispatch, deterministic quality gate... |
| [`agentfolio`](skills/agentfolio/SKILL.md) | Skill for discovering and researching autonomous AI agents, tools, and ecosystems using the AgentFolio directory. |
| [`agentic-actions-auditor`](skills/agentic-actions-auditor/SKILL.md) | > Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects ... |
| [`agentmail`](skills/agentmail/SKILL.md) | Email infrastructure for AI agents. Create accounts, send/receive emails, manage webhooks, and check karma balance via the AgentMail API. |
| [`agentphone`](skills/agentphone/SKILL.md) | Build AI phone agents with AgentPhone API. Use when the user wants to make phone calls, send/receive SMS, manage phone numbers, create voice agents, set up webhooks, or check us... |
| [`agents-md`](skills/agents-md/SKILL.md) | This skill should be used when the user asks to "create AGENTS.md", "update AGENTS.md", "maintain agent docs", "set up CLAUDE.md", or needs to keep agent instructions concise. E... |
| [`agents-v2-py`](skills/agents-v2-py/SKILL.md) | Build container-based Foundry Agents with Azure AI Projects SDK (ImageBasedHostedAgentDefinition). Use when creating hosted agents with custom container images in Azure AI Foundry. |
| [`ai-agent-development`](skills/ai-agent-development/SKILL.md) | AI agent development workflow for building autonomous agents, multi-agent systems, and agent orchestration with CrewAI, LangGraph, and custom agents. |
| [`ai-agents-architect`](skills/ai-agents-architect/SKILL.md) | I build AI systems that can act autonomously while remaining controllable. I understand that agents fail in unexpected ways - I design for graceful degradation and clear failure... |
| [`ai-analyzer`](skills/ai-analyzer/SKILL.md) | AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。 |
| [`ai-daily-radar`](skills/ai-daily-radar/SKILL.md) | Pesquisa e sintetiza diariamente notícias, papers, releases, ferramentas, repositórios e sinais de comunidade sobre IA, tecnologia e programação. Use quando o usuário pedir rada... |
| [`ai-engineer`](skills/ai-engineer/SKILL.md) | Build production-ready LLM applications, advanced RAG systems, and intelligent agents. Implements vector search, multimodal AI, agent orchestration, and enterprise AI integrations. |
| [`ai-engineering-toolkit`](skills/ai-engineering-toolkit/SKILL.md) | 6 production-ready AI engineering workflows: prompt evaluation (8-dimension scoring), context budget planning, RAG pipeline design, agent security audit (65-point checklist), ev... |
| [`ai-md`](skills/ai-md/SKILL.md) | Convert human-written CLAUDE.md into AI-native structured-label format. Battle-tested across 4 models. Same rules, fewer tokens, higher compliance. |
| [`ai-ml`](skills/ai-ml/SKILL.md) | AI and machine learning workflow covering LLM application development, RAG implementation, agent architecture, ML pipelines, and AI-powered features. |
| [`ai-native-cli`](skills/ai-native-cli/SKILL.md) | Design spec with 98 rules for building CLI tools that AI agents can safely use. Covers structured JSON output, error handling, input contracts, safety guardrails, exit codes, an... |
| [`ai-product`](skills/ai-product/SKILL.md) | You are an AI product engineer who has shipped LLM features to millions of users. You've debugged hallucinations at 3am, optimized prompts to reduce costs by 80%, and built safe... |
| [`ai-seo`](skills/ai-seo/SKILL.md) | Optimize content for AI search and LLM citations across AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and similar systems. Use when improving AI visibility, answer engine o... |
| [`ai-studio-image`](skills/ai-studio-image/SKILL.md) | Geracao de imagens humanizadas via Google AI Studio (Gemini). Fotos realistas estilo influencer ou educacional com iluminacao natural e imperfeicoes sutis. |
| [`ai-wrapper-product`](skills/ai-wrapper-product/SKILL.md) | You know AI wrappers get a bad rap, but the good ones solve real problems. You build products where AI is the engine, not the gimmick. You understand prompt engineering is produ... |
| [`airflow-dag-patterns`](skills/airflow-dag-patterns/SKILL.md) | Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. Use when creating data pipelines, orchestrating workflows, or schedulin... |
| [`airtable-automation`](skills/airtable-automation/SKILL.md) | Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views. Always search tools first for current schemas. |
| [`akf-trust-metadata`](skills/akf-trust-metadata/SKILL.md) | The AI native file format. EXIF for AI — stamps every file with trust scores, source provenance, and compliance metadata. Embeds into 20+ formats (DOCX, PDF, images, code). EU A... |
| [`algolia-search`](skills/algolia-search/SKILL.md) | Expert patterns for Algolia search implementation, indexing strategies, React InstantSearch, and relevance tuning Use when: adding search to, algolia, instantsearch, search api,... |
| [`algorithmic-art`](skills/algorithmic-art/SKILL.md) | Algorithmic philosophies are computational aesthetic movements that are then expressed through code. Output .md files (philosophy), .html files (interactive viewer), and .js fil... |
| [`alpha-vantage`](skills/alpha-vantage/SKILL.md) | Access 20+ years of global financial data: equities, options, forex, crypto, commodities, economic indicators, and 50+ technical indicators. |
| [`amazon-alexa`](skills/amazon-alexa/SKILL.md) | Integracao completa com Amazon Alexa para criar skills de voz inteligentes, transformar Alexa em assistente com Claude como cerebro (projeto Auri) e integrar com AWS ecosystem (... |
| [`amplitude-automation`](skills/amplitude-automation/SKILL.md) | Automate Amplitude tasks via Rube MCP (Composio): events, user activity, cohorts, user identification. Always search tools first for current schemas. |
| [`analytics-product`](skills/analytics-product/SKILL.md) | Analytics de produto — PostHog, Mixpanel, eventos, funnels, cohorts, retencao, north star metric, OKRs e dashboards de produto. |
| [`analytics-tracking`](skills/analytics-tracking/SKILL.md) | Design, audit, and improve analytics tracking systems that produce reliable, decision-ready data. |
| [`analyze-project`](skills/analyze-project/SKILL.md) | Forensic root cause analyzer for Antigravity sessions. Classifies scope deltas, rework patterns, root causes, hotspots, and auto-improves prompts/health. |
| [`andrej-karpathy`](skills/andrej-karpathy/SKILL.md) | Agente que simula Andrej Karpathy — ex-Director of AI da Tesla, co-fundador da OpenAI, fundador da Eureka Labs, e o maior educador de deep learning do mundo. |
| [`android-jetpack-compose-expert`](skills/android-jetpack-compose-expert/SKILL.md) | Expert guidance for building modern Android UIs with Jetpack Compose, covering state management, navigation, performance, and Material Design 3. |
| [`android_ui_verification`](skills/android_ui_verification/SKILL.md) | Automated end-to-end UI testing and verification on an Android Emulator using ADB. |
| [`angular`](skills/angular/SKILL.md) | Modern Angular (v20+) expert with deep knowledge of Signals, Standalone Components, Zoneless applications, SSR/Hydration, and reactive patterns. |
| [`angular-best-practices`](skills/angular-best-practices/SKILL.md) | Angular performance optimization and best practices guide. Use when writing, reviewing, or refactoring Angular code for optimal performance, bundle size, and rendering efficiency. |
| [`angular-migration`](skills/angular-migration/SKILL.md) | Master AngularJS to Angular migration, including hybrid apps, component conversion, dependency injection changes, and routing migration. |
| [`angular-state-management`](skills/angular-state-management/SKILL.md) | Master modern Angular state management with Signals, NgRx, and RxJS. Use when setting up global state, managing component stores, choosing between state solutions, or migrating ... |
| [`angular-ui-patterns`](skills/angular-ui-patterns/SKILL.md) | Modern Angular UI patterns for loading states, error handling, and data display. Use when building UI components, handling async data, or managing component states. |
| [`animejs-animation`](skills/animejs-animation/SKILL.md) | Advanced JavaScript animation library skill for creating complex, high-performance web animations. |
| [`anti-reversing-techniques`](skills/anti-reversing-techniques/SKILL.md) | AUTHORIZED USE ONLY: This skill contains dual-use security techniques. Before proceeding with any bypass or analysis: > 1. |
| [`antigravity-design-expert`](skills/antigravity-design-expert/SKILL.md) | Core UI/UX engineering skill for building highly interactive, spatial, weightless, and glassmorphism-based web interfaces using GSAP and 3D CSS. |
| [`antigravity-skill-orchestrator`](skills/antigravity-skill-orchestrator/SKILL.md) | A meta-skill that understands task requirements, dynamically selects appropriate skills, tracks successful skill combinations using agent-memory-mcp, and prevents skill overuse ... |
| [`antigravity-workflows`](skills/antigravity-workflows/SKILL.md) | Orchestrate multiple Antigravity skills through guided workflows for SaaS MVP delivery, security audits, AI agent builds, and browser QA. |
| [`api-design-principles`](skills/api-design-principles/SKILL.md) | Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers and stand the test of time. |
| [`api-documentation`](skills/api-documentation/SKILL.md) | API documentation workflow for generating OpenAPI specs, creating developer guides, and maintaining comprehensive API documentation. |
| [`api-documentation-generator`](skills/api-documentation-generator/SKILL.md) | Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices |
| [`api-documenter`](skills/api-documenter/SKILL.md) | Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate SDKs, and build comprehensive developer... |
| [`api-endpoint-builder`](skills/api-endpoint-builder/SKILL.md) | Builds production-ready REST API endpoints with validation, error handling, authentication, and documentation. Follows best practices for security and scalability. |
| [`api-fuzzing-bug-bounty`](skills/api-fuzzing-bug-bounty/SKILL.md) | Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements. Covers vulnerability discovery, authenti... |
| [`api-patterns`](skills/api-patterns/SKILL.md) | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. |
| [`api-security-best-practices`](skills/api-security-best-practices/SKILL.md) | Implement secure API design patterns including authentication, authorization, input validation, rate limiting, and protection against common API vulnerabilities |
| [`api-security-testing`](skills/api-security-testing/SKILL.md) | API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and security best practices. |
| [`api-testing-observability-api-mock`](skills/api-testing-observability-api-mock/SKILL.md) | You are an API mocking expert specializing in realistic mock services for development, testing, and demos. Design mocks that simulate real API behavior and enable parallel devel... |
| [`apify-actor-development`](skills/apify-actor-development/SKILL.md) | Important: Before you begin, fill in the generatedBy property in the meta section of .actor/actor.json. Replace it with the tool and model you're currently using, such as \"Clau... |
| [`apify-actorization`](skills/apify-actorization/SKILL.md) | Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs packaged as Docker images that accept well-... |
| [`apify-audience-analysis`](skills/apify-audience-analysis/SKILL.md) | Understand audience demographics, preferences, behavior patterns, and engagement quality across Facebook, Instagram, YouTube, and TikTok. |
| [`apify-brand-reputation-monitoring`](skills/apify-brand-reputation-monitoring/SKILL.md) | Scrape reviews, ratings, and brand mentions from multiple platforms using Apify Actors. |
| [`apify-competitor-intelligence`](skills/apify-competitor-intelligence/SKILL.md) | Analyze competitor strategies, content, pricing, ads, and market positioning across Google Maps, Booking.com, Facebook, Instagram, YouTube, and TikTok. |
| [`apify-content-analytics`](skills/apify-content-analytics/SKILL.md) | Track engagement metrics, measure campaign ROI, and analyze content performance across Instagram, Facebook, YouTube, and TikTok. |
| [`apify-ecommerce`](skills/apify-ecommerce/SKILL.md) | Extract product data, prices, reviews, and seller information from any e-commerce platform using Apify's E-commerce Scraping Tool. |
| [`apify-influencer-discovery`](skills/apify-influencer-discovery/SKILL.md) | Find and evaluate influencers for brand partnerships, verify authenticity, and track collaboration performance across Instagram, Facebook, YouTube, and TikTok. |
| [`apify-lead-generation`](skills/apify-lead-generation/SKILL.md) | Scrape leads from multiple platforms using Apify Actors. |
| [`apify-market-research`](skills/apify-market-research/SKILL.md) | Analyze market conditions, geographic opportunities, pricing, consumer behavior, and product validation across Google Maps, Facebook, Instagram, Booking.com, and TripAdvisor. |
| [`apify-trend-analysis`](skills/apify-trend-analysis/SKILL.md) | Discover and track emerging trends across Google Trends, Instagram, Facebook, YouTube, and TikTok to inform content strategy. |
| [`apify-ultimate-scraper`](skills/apify-ultimate-scraper/SKILL.md) | AI-driven data extraction from 55+ Actors across all major platforms. This skill automatically selects the best Actor for your task. |
| [`app-builder`](skills/app-builder/SKILL.md) | Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates agents. |
| [`app-store-changelog`](skills/app-store-changelog/SKILL.md) | Generate user-facing App Store release notes from git history since the last tag. |
| [`app-store-optimization`](skills/app-store-optimization/SKILL.md) | Complete App Store Optimization (ASO) toolkit for researching, optimizing, and tracking mobile app performance on Apple App Store and Google Play Store |
| [`appdeploy`](skills/appdeploy/SKILL.md) | Deploy web apps with backend APIs, database, and file storage. Use when the user asks to deploy or publish a website or web app and wants a public URL. Uses HTTP API via curl. |
| [`application-performance-performance-optimization`](skills/application-performance-performance-optimization/SKILL.md) | Optimize end-to-end application performance with profiling, observability, and backend/frontend tuning. Use when coordinating performance optimization across the stack. |
| [`architect-review`](skills/architect-review/SKILL.md) | Master software architect specializing in modern architecture |
| [`architecture`](skills/architecture/SKILL.md) | Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design. |
| [`architecture-decision-records`](skills/architecture-decision-records/SKILL.md) | Comprehensive patterns for creating, maintaining, and managing Architecture Decision Records (ADRs) that capture the context and rationale behind significant technical decisions. |
| [`architecture-patterns`](skills/architecture-patterns/SKILL.md) | Master proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design to build maintainable, testable, and scalable systems. |
| [`arm-cortex-expert`](skills/arm-cortex-expert/SKILL.md) | Senior embedded software engineer specializing in firmware and driver development for ARM Cortex-M microcontrollers (Teensy, STM32, nRF52, SAMD). |
| [`asana-automation`](skills/asana-automation/SKILL.md) | Automate Asana tasks via Rube MCP (Composio): tasks, projects, sections, teams, workspaces. Always search tools first for current schemas. |
| [`ask-questions-if-underspecified`](skills/ask-questions-if-underspecified/SKILL.md) | Clarify requirements before implementing. Use when serious doubts arise. |
| [`astro`](skills/astro/SKILL.md) | Build content-focused websites with Astro — zero JS by default, islands architecture, multi-framework components, and Markdown/MDX support. |
| [`astropy`](skills/astropy/SKILL.md) | Astropy is the core Python package for astronomy, providing essential functionality for astronomical research and data analysis. |
| [`async-python-patterns`](skills/async-python-patterns/SKILL.md) | Comprehensive guidance for implementing asynchronous Python applications using asyncio, concurrent programming patterns, and async/await for building high-performance, non-block... |
| [`attack-tree-construction`](skills/attack-tree-construction/SKILL.md) | Build comprehensive attack trees to visualize threat paths. Use when mapping attack scenarios, identifying defense gaps, or communicating security risks to stakeholders. |
| [`audio-transcriber`](skills/audio-transcriber/SKILL.md) | Transform audio recordings into professional Markdown documentation with intelligent summaries using LLM integration |
| [`audit-context-building`](skills/audit-context-building/SKILL.md) | Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding. |
| [`audit-skills`](skills/audit-skills/SKILL.md) | Expert security auditor for AI Skills and Bundles. Performs non-intrusive static analysis to identify malicious patterns, data leaks, system stability risks, and obfuscated payl... |
| [`auri-core`](skills/auri-core/SKILL.md) | Auri: assistente de voz inteligente (Alexa + Claude claude-opus-4-20250805). Visao do produto, persona Vitoria Neural, stack AWS, modelo Free/Pro/Business/Enterprise, roadmap 4 ... |
| [`auth-implementation-patterns`](skills/auth-implementation-patterns/SKILL.md) | Build secure, scalable authentication and authorization systems using industry-standard patterns and modern best practices. |
| [`autonomous-agent-patterns`](skills/autonomous-agent-patterns/SKILL.md) | Design patterns for building autonomous coding agents, inspired by [Cline](https://github.com/cline/cline) and [OpenAI Codex](https://github.com/openai/codex). |
| [`autonomous-agents`](skills/autonomous-agents/SKILL.md) | You are an agent architect who has learned the hard lessons of autonomous AI. You've seen the gap between impressive demos and production disasters. You know that a 95% success ... |
| [`avalonia-layout-zafiro`](skills/avalonia-layout-zafiro/SKILL.md) | Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing shared styles, generic components, and avoiding XAML redundancy. |
| [`avalonia-viewmodels-zafiro`](skills/avalonia-viewmodels-zafiro/SKILL.md) | Optimal ViewModel and Wizard creation patterns for Avalonia using Zafiro and ReactiveUI. |
| [`avalonia-zafiro-development`](skills/avalonia-zafiro-development/SKILL.md) | Mandatory skills, conventions, and behavioral rules for Avalonia UI development using the Zafiro toolkit. |
| [`avoid-ai-writing`](skills/avoid-ai-writing/SKILL.md) | Audit and rewrite content to remove 21 categories of AI writing patterns with a 43-entry replacement table |
| [`awareness-stage-mapper`](skills/awareness-stage-mapper/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`aws-cost-cleanup`](skills/aws-cost-cleanup/SKILL.md) | Automated cleanup of unused AWS resources to reduce costs |
| [`aws-cost-optimizer`](skills/aws-cost-optimizer/SKILL.md) | Comprehensive AWS cost analysis and optimization recommendations using AWS CLI and Cost Explorer |
| [`aws-penetration-testing`](skills/aws-penetration-testing/SKILL.md) | Provide comprehensive techniques for penetration testing AWS cloud environments. Covers IAM enumeration, privilege escalation, SSRF to metadata endpoint, S3 bucket exploitation,... |
| [`aws-serverless`](skills/aws-serverless/SKILL.md) | Proper Lambda function structure with error handling |
| [`aws-skills`](skills/aws-skills/SKILL.md) | AWS development with infrastructure automation and cloud architecture patterns |
| [`awt-e2e-testing`](skills/awt-e2e-testing/SKILL.md) | AI-powered E2E web testing — eyes and hands for AI coding tools. Declarative YAML scenarios, Playwright execution, visual matching (OpenCV + OCR), platform auto-detection (Flutt... |
| [`azd-deployment`](skills/azd-deployment/SKILL.md) | Deploy containerized frontend + backend applications to Azure Container Apps with remote builds, managed identity, and idempotent infrastructure. |
| [`azure-ai-agents-persistent-dotnet`](skills/azure-ai-agents-persistent-dotnet/SKILL.md) | Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| [`azure-ai-agents-persistent-java`](skills/azure-ai-agents-persistent-java/SKILL.md) | Azure AI Agents Persistent SDK for Java. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| [`azure-ai-anomalydetector-java`](skills/azure-ai-anomalydetector-java/SKILL.md) | Build anomaly detection applications with Azure AI Anomaly Detector SDK for Java. Use when implementing univariate/multivariate anomaly detection, time-series analysis, or AI-po... |
| [`azure-ai-contentsafety-java`](skills/azure-ai-contentsafety-java/SKILL.md) | Build content moderation applications using the Azure AI Content Safety SDK for Java. |
| [`azure-ai-contentsafety-py`](skills/azure-ai-contentsafety-py/SKILL.md) | Azure AI Content Safety SDK for Python. Use for detecting harmful content in text and images with multi-severity classification. |
| [`azure-ai-contentsafety-ts`](skills/azure-ai-contentsafety-ts/SKILL.md) | Analyze text and images for harmful content with customizable blocklists. |
| [`azure-ai-contentunderstanding-py`](skills/azure-ai-contentunderstanding-py/SKILL.md) | Azure AI Content Understanding SDK for Python. Use for multimodal content extraction from documents, images, audio, and video. |
| [`azure-ai-document-intelligence-dotnet`](skills/azure-ai-document-intelligence-dotnet/SKILL.md) | Azure AI Document Intelligence SDK for .NET. Extract text, tables, and structured data from documents using prebuilt and custom models. |
| [`azure-ai-document-intelligence-ts`](skills/azure-ai-document-intelligence-ts/SKILL.md) | Extract text, tables, and structured data from documents using prebuilt and custom models. |
| [`azure-ai-formrecognizer-java`](skills/azure-ai-formrecognizer-java/SKILL.md) | Build document analysis applications using the Azure AI Document Intelligence SDK for Java. |
| [`azure-ai-ml-py`](skills/azure-ai-ml-py/SKILL.md) | Azure Machine Learning SDK v2 for Python. Use for ML workspaces, jobs, models, datasets, compute, and pipelines. |
| [`azure-ai-openai-dotnet`](skills/azure-ai-openai-dotnet/SKILL.md) | Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embeddings, image generation, audio transcription, and assistants. |
| [`azure-ai-projects-dotnet`](skills/azure-ai-projects-dotnet/SKILL.md) | Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections, datasets, deployments, evaluations, and indexes. |
| [`azure-ai-projects-java`](skills/azure-ai-projects-java/SKILL.md) | Azure AI Projects SDK for Java. High-level SDK for Azure AI Foundry project management including connections, datasets, indexes, and evaluations. |
| [`azure-ai-projects-py`](skills/azure-ai-projects-py/SKILL.md) | Build AI applications on Microsoft Foundry using the azure-ai-projects SDK. |
| [`azure-ai-projects-ts`](skills/azure-ai-projects-ts/SKILL.md) | High-level SDK for Azure AI Foundry projects with agents, connections, deployments, and evaluations. |
| [`azure-ai-textanalytics-py`](skills/azure-ai-textanalytics-py/SKILL.md) | Azure AI Text Analytics SDK for sentiment analysis, entity recognition, key phrases, language detection, PII, and healthcare NLP. Use for natural language processing on text. |
| [`azure-ai-transcription-py`](skills/azure-ai-transcription-py/SKILL.md) | Azure AI Transcription SDK for Python. Use for real-time and batch speech-to-text transcription with timestamps and diarization. |
| [`azure-ai-translation-document-py`](skills/azure-ai-translation-document-py/SKILL.md) | Azure AI Document Translation SDK for batch translation of documents with format preservation. Use for translating Word, PDF, Excel, PowerPoint, and other document formats at sc... |
| [`azure-ai-translation-text-py`](skills/azure-ai-translation-text-py/SKILL.md) | Azure AI Text Translation SDK for real-time text translation, transliteration, language detection, and dictionary lookup. Use for translating text content in applications. |
| [`azure-ai-translation-ts`](skills/azure-ai-translation-ts/SKILL.md) | Text and document translation with REST-style clients. |
| [`azure-ai-vision-imageanalysis-java`](skills/azure-ai-vision-imageanalysis-java/SKILL.md) | Build image analysis applications with Azure AI Vision SDK for Java. Use when implementing image captioning, OCR text extraction, object detection, tagging, or smart cropping. |
| [`azure-ai-vision-imageanalysis-py`](skills/azure-ai-vision-imageanalysis-py/SKILL.md) | Azure AI Vision Image Analysis SDK for captions, tags, objects, OCR, people detection, and smart cropping. Use for computer vision and image understanding tasks. |
| [`azure-ai-voicelive-dotnet`](skills/azure-ai-voicelive-dotnet/SKILL.md) | Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication. |
| [`azure-ai-voicelive-java`](skills/azure-ai-voicelive-java/SKILL.md) | Azure AI VoiceLive SDK for Java. Real-time bidirectional voice conversations with AI assistants using WebSocket. |
| [`azure-ai-voicelive-py`](skills/azure-ai-voicelive-py/SKILL.md) | Build real-time voice AI applications with bidirectional WebSocket communication. |
| [`azure-ai-voicelive-ts`](skills/azure-ai-voicelive-ts/SKILL.md) | Azure AI Voice Live SDK for JavaScript/TypeScript. Build real-time voice AI applications with bidirectional WebSocket communication. |
| [`azure-appconfiguration-java`](skills/azure-appconfiguration-java/SKILL.md) | Azure App Configuration SDK for Java. Centralized application configuration management with key-value settings, feature flags, and snapshots. |
| [`azure-appconfiguration-py`](skills/azure-appconfiguration-py/SKILL.md) | Azure App Configuration SDK for Python. Use for centralized configuration management, feature flags, and dynamic settings. |
| [`azure-appconfiguration-ts`](skills/azure-appconfiguration-ts/SKILL.md) | Centralized configuration management with feature flags and dynamic refresh. |
| [`azure-communication-callautomation-java`](skills/azure-communication-callautomation-java/SKILL.md) | Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions. |
| [`azure-communication-callingserver-java`](skills/azure-communication-callingserver-java/SKILL.md) | ⚠️ DEPRECATED: This SDK has been renamed to Call Automation. For new projects, use azure-communication-callautomation instead. This skill is for maintaining legacy code only. |
| [`azure-communication-chat-java`](skills/azure-communication-chat-java/SKILL.md) | Build real-time chat applications with thread management, messaging, participants, and read receipts. |
| [`azure-communication-common-java`](skills/azure-communication-common-java/SKILL.md) | Azure Communication Services common utilities for Java. Use when working with CommunicationTokenCredential, user identifiers, token refresh, or shared authentication across ACS ... |
| [`azure-communication-sms-java`](skills/azure-communication-sms-java/SKILL.md) | Send SMS messages with Azure Communication Services SMS Java SDK. Use when implementing SMS notifications, alerts, OTP delivery, bulk messaging, or delivery reports. |
| [`azure-compute-batch-java`](skills/azure-compute-batch-java/SKILL.md) | Azure Batch SDK for Java. Run large-scale parallel and HPC batch jobs with pools, jobs, tasks, and compute nodes. |
| [`azure-containerregistry-py`](skills/azure-containerregistry-py/SKILL.md) | Azure Container Registry SDK for Python. Use for managing container images, artifacts, and repositories. |
| [`azure-cosmos-db-py`](skills/azure-cosmos-db-py/SKILL.md) | Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles. |
| [`azure-cosmos-java`](skills/azure-cosmos-java/SKILL.md) | Azure Cosmos DB SDK for Java. NoSQL database operations with global distribution, multi-model support, and reactive patterns. |
| [`azure-cosmos-py`](skills/azure-cosmos-py/SKILL.md) | Azure Cosmos DB SDK for Python (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| [`azure-cosmos-rust`](skills/azure-cosmos-rust/SKILL.md) | Azure Cosmos DB SDK for Rust (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| [`azure-cosmos-ts`](skills/azure-cosmos-ts/SKILL.md) | Azure Cosmos DB JavaScript/TypeScript SDK (@azure/cosmos) for data plane operations. Use for CRUD operations on documents, queries, bulk operations, and container management. |
| [`azure-data-tables-java`](skills/azure-data-tables-java/SKILL.md) | Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API. |
| [`azure-data-tables-py`](skills/azure-data-tables-py/SKILL.md) | Azure Tables SDK for Python (Storage and Cosmos DB). Use for NoSQL key-value storage, entity CRUD, and batch operations. |
| [`azure-eventgrid-dotnet`](skills/azure-eventgrid-dotnet/SKILL.md) | Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use for event-driven architectures, pub/sub messaging, CloudEvents, and ... |
| [`azure-eventgrid-java`](skills/azure-eventgrid-java/SKILL.md) | Build event-driven applications with Azure Event Grid SDK for Java. Use when publishing events, implementing pub/sub patterns, or integrating with Azure services via events. |
| [`azure-eventgrid-py`](skills/azure-eventgrid-py/SKILL.md) | Azure Event Grid SDK for Python. Use for publishing events, handling CloudEvents, and event-driven architectures. |
| [`azure-eventhub-dotnet`](skills/azure-eventhub-dotnet/SKILL.md) | Azure Event Hubs SDK for .NET. |
| [`azure-eventhub-java`](skills/azure-eventhub-java/SKILL.md) | Build real-time streaming applications with Azure Event Hubs SDK for Java. Use when implementing event streaming, high-throughput data ingestion, or building event-driven archit... |
| [`azure-eventhub-py`](skills/azure-eventhub-py/SKILL.md) | Azure Event Hubs SDK for Python streaming. Use for high-throughput event ingestion, producers, consumers, and checkpointing. |
| [`azure-eventhub-rust`](skills/azure-eventhub-rust/SKILL.md) | Azure Event Hubs SDK for Rust. Use for sending and receiving events, streaming data ingestion. |
| [`azure-eventhub-ts`](skills/azure-eventhub-ts/SKILL.md) | High-throughput event streaming and real-time data ingestion. |
| [`azure-functions`](skills/azure-functions/SKILL.md) | Modern .NET execution model with process isolation |
| [`azure-identity-dotnet`](skills/azure-identity-dotnet/SKILL.md) | Azure Identity SDK for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use for DefaultAzureCredential, managed identity, service principals, and dev... |
| [`azure-identity-java`](skills/azure-identity-java/SKILL.md) | Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD). |
| [`azure-identity-py`](skills/azure-identity-py/SKILL.md) | Azure Identity SDK for Python authentication. Use for DefaultAzureCredential, managed identity, service principals, and token caching. |
| [`azure-identity-rust`](skills/azure-identity-rust/SKILL.md) | Azure Identity SDK for Rust authentication. Use for DeveloperToolsCredential, ManagedIdentityCredential, ClientSecretCredential, and token-based authentication. |
| [`azure-identity-ts`](skills/azure-identity-ts/SKILL.md) | Authenticate to Azure services with various credential types. |
| [`azure-keyvault-certificates-rust`](skills/azure-keyvault-certificates-rust/SKILL.md) | Azure Key Vault Certificates SDK for Rust. Use for creating, importing, and managing certificates. |
| [`azure-keyvault-keys-rust`](skills/azure-keyvault-keys-rust/SKILL.md) | Azure Key Vault Keys SDK for Rust. Use for creating, managing, and using cryptographic keys. Triggers: "keyvault keys rust", "KeyClient rust", "create key rust", "encrypt rust",... |
| [`azure-keyvault-keys-ts`](skills/azure-keyvault-keys-ts/SKILL.md) | Manage cryptographic keys using Azure Key Vault Keys SDK for JavaScript (@azure/keyvault-keys). Use when creating, encrypting/decrypting, signing, or rotating keys. |
| [`azure-keyvault-py`](skills/azure-keyvault-py/SKILL.md) | Azure Key Vault SDK for Python. Use for secrets, keys, and certificates management with secure storage. |
| [`azure-keyvault-secrets-rust`](skills/azure-keyvault-secrets-rust/SKILL.md) | Azure Key Vault Secrets SDK for Rust. Use for storing and retrieving secrets, passwords, and API keys. Triggers: "keyvault secrets rust", "SecretClient rust", "get secret rust",... |
| [`azure-keyvault-secrets-ts`](skills/azure-keyvault-secrets-ts/SKILL.md) | Manage secrets using Azure Key Vault Secrets SDK for JavaScript (@azure/keyvault-secrets). Use when storing and retrieving application secrets or configuration values. |
| [`azure-maps-search-dotnet`](skills/azure-maps-search-dotnet/SKILL.md) | Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and weather. Use for address search, directions, map tiles, IP geolocation... |
| [`azure-messaging-webpubsub-java`](skills/azure-messaging-webpubsub-java/SKILL.md) | Build real-time web applications with Azure Web PubSub SDK for Java. Use when implementing WebSocket-based messaging, live updates, chat applications, or server-to-client push n... |
| [`azure-messaging-webpubsubservice-py`](skills/azure-messaging-webpubsubservice-py/SKILL.md) | Azure Web PubSub Service SDK for Python. Use for real-time messaging, WebSocket connections, and pub/sub patterns. |
| [`azure-mgmt-apicenter-dotnet`](skills/azure-mgmt-apicenter-dotnet/SKILL.md) | Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery. |
| [`azure-mgmt-apicenter-py`](skills/azure-mgmt-apicenter-py/SKILL.md) | Azure API Center Management SDK for Python. Use for managing API inventory, metadata, and governance across your organization. |
| [`azure-mgmt-apimanagement-dotnet`](skills/azure-mgmt-apimanagement-dotnet/SKILL.md) | Azure Resource Manager SDK for API Management in .NET. |
| [`azure-mgmt-apimanagement-py`](skills/azure-mgmt-apimanagement-py/SKILL.md) | Azure API Management SDK for Python. Use for managing APIM services, APIs, products, subscriptions, and policies. |
| [`azure-mgmt-applicationinsights-dotnet`](skills/azure-mgmt-applicationinsights-dotnet/SKILL.md) | Azure Application Insights SDK for .NET. Application performance monitoring and observability resource management. |
| [`azure-mgmt-arizeaiobservabilityeval-dotnet`](skills/azure-mgmt-arizeaiobservabilityeval-dotnet/SKILL.md) | Azure Resource Manager SDK for Arize AI Observability and Evaluation (.NET). |
| [`azure-mgmt-botservice-dotnet`](skills/azure-mgmt-botservice-dotnet/SKILL.md) | Azure Resource Manager SDK for Bot Service in .NET. Management plane operations for creating and managing Azure Bot resources, channels (Teams, DirectLine, Slack), and connectio... |
| [`azure-mgmt-botservice-py`](skills/azure-mgmt-botservice-py/SKILL.md) | Azure Bot Service Management SDK for Python. Use for creating, managing, and configuring Azure Bot Service resources. |
| [`azure-mgmt-fabric-dotnet`](skills/azure-mgmt-fabric-dotnet/SKILL.md) | Azure Resource Manager SDK for Fabric in .NET. |
| [`azure-mgmt-fabric-py`](skills/azure-mgmt-fabric-py/SKILL.md) | Azure Fabric Management SDK for Python. Use for managing Microsoft Fabric capacities and resources. |
| [`azure-mgmt-mongodbatlas-dotnet`](skills/azure-mgmt-mongodbatlas-dotnet/SKILL.md) | Manage MongoDB Atlas Organizations as Azure ARM resources with unified billing through Azure Marketplace. |
| [`azure-mgmt-weightsandbiases-dotnet`](skills/azure-mgmt-weightsandbiases-dotnet/SKILL.md) | Azure Weights & Biases SDK for .NET. ML experiment tracking and model management via Azure Marketplace. Use for creating W&B instances, managing SSO, marketplace integration, an... |
| [`azure-microsoft-playwright-testing-ts`](skills/azure-microsoft-playwright-testing-ts/SKILL.md) | Run Playwright tests at scale with cloud-hosted browsers and integrated Azure portal reporting. |
| [`azure-monitor-ingestion-java`](skills/azure-monitor-ingestion-java/SKILL.md) | Azure Monitor Ingestion SDK for Java. Send custom logs to Azure Monitor via Data Collection Rules (DCR) and Data Collection Endpoints (DCE). |
| [`azure-monitor-ingestion-py`](skills/azure-monitor-ingestion-py/SKILL.md) | Azure Monitor Ingestion SDK for Python. Use for sending custom logs to Log Analytics workspace via Logs Ingestion API. |
| [`azure-monitor-opentelemetry-exporter-java`](skills/azure-monitor-opentelemetry-exporter-java/SKILL.md) | Azure Monitor OpenTelemetry Exporter for Java. Export OpenTelemetry traces, metrics, and logs to Azure Monitor/Application Insights. |
| [`azure-monitor-opentelemetry-exporter-py`](skills/azure-monitor-opentelemetry-exporter-py/SKILL.md) | Azure Monitor OpenTelemetry Exporter for Python. Use for low-level OpenTelemetry export to Application Insights. |
| [`azure-monitor-opentelemetry-py`](skills/azure-monitor-opentelemetry-py/SKILL.md) | Azure Monitor OpenTelemetry Distro for Python. Use for one-line Application Insights setup with auto-instrumentation. |
| [`azure-monitor-opentelemetry-ts`](skills/azure-monitor-opentelemetry-ts/SKILL.md) | Auto-instrument Node.js applications with distributed tracing, metrics, and logs. |
| [`azure-monitor-query-java`](skills/azure-monitor-query-java/SKILL.md) | Azure Monitor Query SDK for Java. Execute Kusto queries against Log Analytics workspaces and query metrics from Azure resources. |
| [`azure-monitor-query-py`](skills/azure-monitor-query-py/SKILL.md) | Azure Monitor Query SDK for Python. Use for querying Log Analytics workspaces and Azure Monitor metrics. |
| [`azure-postgres-ts`](skills/azure-postgres-ts/SKILL.md) | Connect to Azure Database for PostgreSQL Flexible Server from Node.js/TypeScript using the pg (node-postgres) package. |
| [`azure-resource-manager-cosmosdb-dotnet`](skills/azure-resource-manager-cosmosdb-dotnet/SKILL.md) | Azure Resource Manager SDK for Cosmos DB in .NET. |
| [`azure-resource-manager-durabletask-dotnet`](skills/azure-resource-manager-durabletask-dotnet/SKILL.md) | Azure Resource Manager SDK for Durable Task Scheduler in .NET. |
| [`azure-resource-manager-mysql-dotnet`](skills/azure-resource-manager-mysql-dotnet/SKILL.md) | Azure MySQL Flexible Server SDK for .NET. Database management for MySQL Flexible Server deployments. |
| [`azure-resource-manager-playwright-dotnet`](skills/azure-resource-manager-playwright-dotnet/SKILL.md) | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET. |
| [`azure-resource-manager-postgresql-dotnet`](skills/azure-resource-manager-postgresql-dotnet/SKILL.md) | Azure PostgreSQL Flexible Server SDK for .NET. Database management for PostgreSQL Flexible Server deployments. |
| [`azure-resource-manager-redis-dotnet`](skills/azure-resource-manager-redis-dotnet/SKILL.md) | Azure Resource Manager SDK for Redis in .NET. |
| [`azure-resource-manager-sql-dotnet`](skills/azure-resource-manager-sql-dotnet/SKILL.md) | Azure Resource Manager SDK for Azure SQL in .NET. |
| [`azure-search-documents-dotnet`](skills/azure-search-documents-dotnet/SKILL.md) | Azure AI Search SDK for .NET (Azure.Search.Documents). Use for building search applications with full-text, vector, semantic, and hybrid search. |
| [`azure-search-documents-py`](skills/azure-search-documents-py/SKILL.md) | Azure AI Search SDK for Python. Use for vector search, hybrid search, semantic ranking, indexing, and skillsets. |
| [`azure-search-documents-ts`](skills/azure-search-documents-ts/SKILL.md) | Build search applications with vector, hybrid, and semantic search capabilities. |
| [`azure-security-keyvault-keys-dotnet`](skills/azure-security-keyvault-keys-dotnet/SKILL.md) | Azure Key Vault Keys SDK for .NET. Client library for managing cryptographic keys in Azure Key Vault and Managed HSM. Use for key creation, rotation, encryption, decryption, sig... |
| [`azure-security-keyvault-keys-java`](skills/azure-security-keyvault-keys-java/SKILL.md) | Azure Key Vault Keys Java SDK for cryptographic key management. Use when creating, managing, or using RSA/EC keys, performing encrypt/decrypt/sign/verify operations, or working ... |
| [`azure-security-keyvault-secrets-java`](skills/azure-security-keyvault-secrets-java/SKILL.md) | Azure Key Vault Secrets Java SDK for secret management. Use when storing, retrieving, or managing passwords, API keys, connection strings, or other sensitive configuration data. |
| [`azure-servicebus-dotnet`](skills/azure-servicebus-dotnet/SKILL.md) | Azure Service Bus SDK for .NET. Enterprise messaging with queues, topics, subscriptions, and sessions. |
| [`azure-servicebus-py`](skills/azure-servicebus-py/SKILL.md) | Azure Service Bus SDK for Python messaging. Use for queues, topics, subscriptions, and enterprise messaging patterns. |
| [`azure-servicebus-ts`](skills/azure-servicebus-ts/SKILL.md) | Enterprise messaging with queues, topics, and subscriptions. |
| [`azure-speech-to-text-rest-py`](skills/azure-speech-to-text-rest-py/SKILL.md) | Azure Speech to Text REST API for short audio (Python). Use for simple speech recognition of audio files up to 60 seconds without the Speech SDK. |
| [`azure-storage-blob-java`](skills/azure-storage-blob-java/SKILL.md) | Build blob storage applications using the Azure Storage Blob SDK for Java. |
| [`azure-storage-blob-py`](skills/azure-storage-blob-py/SKILL.md) | Azure Blob Storage SDK for Python. Use for uploading, downloading, listing blobs, managing containers, and blob lifecycle. |
| [`azure-storage-blob-rust`](skills/azure-storage-blob-rust/SKILL.md) | Azure Blob Storage SDK for Rust. Use for uploading, downloading, and managing blobs and containers. |
| [`azure-storage-blob-ts`](skills/azure-storage-blob-ts/SKILL.md) | Azure Blob Storage JavaScript/TypeScript SDK (@azure/storage-blob) for blob operations. Use for uploading, downloading, listing, and managing blobs and containers. |
| [`azure-storage-file-datalake-py`](skills/azure-storage-file-datalake-py/SKILL.md) | Azure Data Lake Storage Gen2 SDK for Python. Use for hierarchical file systems, big data analytics, and file/directory operations. |
| [`azure-storage-file-share-py`](skills/azure-storage-file-share-py/SKILL.md) | Azure Storage File Share SDK for Python. Use for SMB file shares, directories, and file operations in the cloud. |
| [`azure-storage-file-share-ts`](skills/azure-storage-file-share-ts/SKILL.md) | Azure File Share JavaScript/TypeScript SDK (@azure/storage-file-share) for SMB file share operations. |
| [`azure-storage-queue-py`](skills/azure-storage-queue-py/SKILL.md) | Azure Queue Storage SDK for Python. Use for reliable message queuing, task distribution, and asynchronous processing. |
| [`azure-storage-queue-ts`](skills/azure-storage-queue-ts/SKILL.md) | Azure Queue Storage JavaScript/TypeScript SDK (@azure/storage-queue) for message queue operations. Use for sending, receiving, peeking, and deleting messages in queues. |
| [`azure-web-pubsub-ts`](skills/azure-web-pubsub-ts/SKILL.md) | Real-time messaging with WebSocket connections and pub/sub patterns. |

<a id="indice-b"></a>
### Letra B (54 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`backend-architect`](skills/backend-architect/SKILL.md) | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. |
| [`backend-dev-guidelines`](skills/backend-dev-guidelines/SKILL.md) | You are a senior backend engineer operating production-grade services under strict architectural and reliability constraints. Use when routes, controllers, services, repositorie... |
| [`backend-development-feature-development`](skills/backend-development-feature-development/SKILL.md) | Orchestrate end-to-end backend feature development from requirements to deployment. Use when coordinating multi-phase feature delivery across teams and services. |
| [`backend-security-coder`](skills/backend-security-coder/SKILL.md) | Expert in secure backend coding practices specializing in input validation, authentication, and API security. Use PROACTIVELY for backend security implementations or security co... |
| [`backtesting-frameworks`](skills/backtesting-frameworks/SKILL.md) | Build robust, production-grade backtesting systems that avoid common pitfalls and produce reliable strategy performance estimates. |
| [`bamboohr-automation`](skills/bamboohr-automation/SKILL.md) | Automate BambooHR tasks via Rube MCP (Composio): employees, time-off, benefits, dependents, employee updates. Always search tools first for current schemas. |
| [`basecamp-automation`](skills/basecamp-automation/SKILL.md) | Automate Basecamp project management, to-dos, messages, people, and to-do list organization via Rube MCP (Composio). Always search tools first for current schemas. |
| [`baseline-ui`](skills/baseline-ui/SKILL.md) | Validates animation durations, enforces typography scale, checks component accessibility, and prevents layout anti-patterns in Tailwind CSS projects. Use when building UI compon... |
| [`bash-defensive-patterns`](skills/bash-defensive-patterns/SKILL.md) | Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or system utilities requiring fault tolerance ... |
| [`bash-linux`](skills/bash-linux/SKILL.md) | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems. |
| [`bash-pro`](skills/bash-pro/SKILL.md) | Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities. Expert in safe, portable, and testable shell scripts. |
| [`bash-scripting`](skills/bash-scripting/SKILL.md) | Bash scripting workflow for creating production-ready shell scripts with defensive patterns, error handling, and testing. |
| [`bats-testing-patterns`](skills/bats-testing-patterns/SKILL.md) | Master Bash Automated Testing System (Bats) for comprehensive shell script testing. Use when writing tests for shell scripts, CI/CD pipelines, or requiring test-driven developme... |
| [`bazel-build-optimization`](skills/bazel-build-optimization/SKILL.md) | Optimize Bazel builds for large-scale monorepos. Use when configuring Bazel, implementing remote execution, or optimizing build performance for enterprise codebases. |
| [`bdi-mental-states`](skills/bdi-mental-states/SKILL.md) | This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create belief-desire-intention models", "transform RDF to beliefs", "... |
| [`bdistill-behavioral-xray`](skills/bdistill-behavioral-xray/SKILL.md) | X-ray any AI model's behavioral patterns — refusal boundaries, hallucination tendencies, reasoning style, formatting defaults. No API key needed. |
| [`bdistill-knowledge-extraction`](skills/bdistill-knowledge-extraction/SKILL.md) | Extract structured domain knowledge from AI models in-session or from local open-source models via Ollama. No API key needed. |
| [`beautiful-prose`](skills/beautiful-prose/SKILL.md) | A hard-edged writing style contract for timeless, forceful English prose without modern AI tics. Use when users ask for prose or rewrites that must be clean, exact, concrete, an... |
| [`behavioral-modes`](skills/behavioral-modes/SKILL.md) | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type. |
| [`bevy-ecs-expert`](skills/bevy-ecs-expert/SKILL.md) | Master Bevy's Entity Component System (ECS) in Rust, covering Systems, Queries, Resources, and parallel scheduling. |
| [`bigquery-ai-ml`](skills/bigquery-ai-ml/SKILL.md) | Leverages BigQuery's built-in machine learning and GenAI capabilities for advanced data analytics. Use when you need to write SQL queries that perform time-series forecasting, d... |
| [`bigquery-bigframes`](skills/bigquery-bigframes/SKILL.md) | Generates Python code using BigQuery DataFrames (BigFrames), the pandas/scikit-learn-style\ \ API over BigQuery. Use when writing BigFrames code or doing pandas-style dataframe/... |
| [`bigquery-data-transfer-service`](skills/bigquery-data-transfer-service/SKILL.md) | Discovers and inspects BigQuery Data Transfer Service (DTS) configurations. Use this to identify existing ingestion pipelines and extract datasource or transfer config metadata ... |
| [`bigquery-graph`](skills/bigquery-graph/SKILL.md) | Provides guidelines and best practices for querying and defining property graphs and semantic graphs in BigQuery using GQL (Graph Query Language). Use when creating property gra... |
| [`bigquery-sql`](skills/bigquery-sql/SKILL.md) | Provides BigQuery SQL query optimization techniques, execution best practices, and performance tuning rules for high-efficiency querying. Use when optimizing BigQuery SQL querie... |
| [`bill-gates`](skills/bill-gates/SKILL.md) | Agente que simula Bill Gates — cofundador da Microsoft, arquiteto da industria de software comercial, estrategista tecnologico global, investidor sistemico e filantropo baseado ... |
| [`billing-automation`](skills/billing-automation/SKILL.md) | Master automated billing systems including recurring billing, invoice generation, dunning management, proration, and tax calculation. |
| [`binary-analysis-patterns`](skills/binary-analysis-patterns/SKILL.md) | Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic. |
| [`biopython`](skills/biopython/SKILL.md) | Biopython is a comprehensive set of freely available Python tools for biological computation. It provides functionality for sequence manipulation, file I/O, database access, str... |
| [`bitbucket-automation`](skills/bitbucket-automation/SKILL.md) | Automate Bitbucket repositories, pull requests, branches, issues, and workspace management via Rube MCP (Composio). Always search tools first for current schemas. |
| [`blockchain-developer`](skills/blockchain-developer/SKILL.md) | Build production-ready Web3 applications, smart contracts, and decentralized systems. Implements DeFi protocols, NFT platforms, DAOs, and enterprise blockchain integrations. |
| [`blockrun`](skills/blockrun/SKILL.md) | BlockRun works with Claude Code and Google Antigravity. |
| [`blog-writing-guide`](skills/blog-writing-guide/SKILL.md) | This skill enforces Sentry's blog writing standards across every post — whether you're helping an engineer write their first blog post or a marketer draft a product announcement. |
| [`blueprint`](skills/blueprint/SKILL.md) | Turn a one-line objective into a step-by-step construction plan any coding agent can execute cold. Each step has a self-contained context brief — a fresh agent in a new session ... |
| [`box-automation`](skills/box-automation/SKILL.md) | Automate Box operations including file upload/download, content search, folder management, collaboration, metadata queries, and sign requests through Composio's Box toolkit. |
| [`brainstorming`](skills/brainstorming/SKILL.md) | Use before creative or constructive work (features, architecture, behavior). Transforms vague ideas into validated designs through disciplined reasoning and collaboration. |
| [`brand-guidelines`](skills/brand-guidelines/SKILL.md) | Write copy following Sentry brand guidelines. Use when writing UI text, error messages, empty states, onboarding flows, 404 pages, documentation, marketing copy, or any user-fac... |
| [`brand-guidelines-anthropic`](skills/brand-guidelines-anthropic/SKILL.md) | To access Anthropic's official brand identity and style resources, use this skill. |
| [`brand-guidelines-community`](skills/brand-guidelines-community/SKILL.md) | To access Anthropic's official brand identity and style resources, use this skill. |
| [`brand-perception-psychologist`](skills/brand-perception-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`brevo-automation`](skills/brevo-automation/SKILL.md) | Automate Brevo (formerly Sendinblue) email marketing operations through Composio's Brevo toolkit via Rube MCP. |
| [`broken-authentication`](skills/broken-authentication/SKILL.md) | Identify and exploit authentication and session management vulnerabilities in web applications. Broken authentication consistently ranks in the OWASP Top 10 and can lead to acco... |
| [`browser-automation`](skills/browser-automation/SKILL.md) | You are a browser automation expert who has debugged thousands of flaky tests and built scrapers that run for years without breaking. You've seen the evolution from Selenium to ... |
| [`browser-extension-builder`](skills/browser-extension-builder/SKILL.md) | You extend the browser to give users superpowers. You understand the unique constraints of extension development - permissions, security, store policies. You build extensions th... |
| [`bug-hunter`](skills/bug-hunter/SKILL.md) | Systematically finds and fixes bugs using proven debugging techniques. Traces from symptoms to root cause, implements fixes, and prevents regression. |
| [`build`](skills/build/SKILL.md) | build |
| [`building-data-apps`](skills/building-data-apps/SKILL.md) | \| Build modern data apps, dashboards, and interactive reports using either React + Vite or Streamlit. Includes optional Gemini Data Analytics chat integration for an AI powered... |
| [`building-native-ui`](skills/building-native-ui/SKILL.md) | Complete guide for building beautiful apps with Expo Router. Covers fundamentals, styling, components, navigation, animations, patterns, and native tabs. |
| [`bullmq-specialist`](skills/bullmq-specialist/SKILL.md) | BullMQ expert for Redis-backed job queues, background processing, and reliable async execution in Node.js/TypeScript applications. Use when: bullmq, bull queue, redis queue, bac... |
| [`bun-development`](skills/bun-development/SKILL.md) | Fast, modern JavaScript/TypeScript development with the Bun runtime, inspired by [oven-sh/bun](https://github.com/oven-sh/bun). |
| [`burp-suite-testing`](skills/burp-suite-testing/SKILL.md) | Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic interception and modification, request analysis and replay, ... |
| [`burpsuite-project-parser`](skills/burpsuite-project-parser/SKILL.md) | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findin... |
| [`business-analyst`](skills/business-analyst/SKILL.md) | Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. Build comprehensive KPI frameworks, predictive models, and strategic r... |
| [`busybox-on-windows`](skills/busybox-on-windows/SKILL.md) | How to use a Win32 build of BusyBox to run many of the standard UNIX command line tools on Windows. |

<a id="indice-c"></a>
### Letra C (125 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`c-pro`](skills/c-pro/SKILL.md) | Write efficient C code with proper memory management, pointer |
| [`c4-architecture-c4-architecture`](skills/c4-architecture-c4-architecture/SKILL.md) | Generate comprehensive C4 architecture documentation for an existing repository/codebase using a bottom-up analysis approach. |
| [`c4-code`](skills/c4-code/SKILL.md) | Expert C4 Code-level documentation specialist. Analyzes code directories to create comprehensive C4 code-level documentation including function signatures, arguments, dependenci... |
| [`c4-component`](skills/c4-component/SKILL.md) | Expert C4 Component-level documentation specialist. Synthesizes C4 Code-level documentation into Component-level architecture, defining component boundaries, interfaces, and rel... |
| [`c4-container`](skills/c4-container/SKILL.md) | Expert C4 Container-level documentation specialist. |
| [`c4-context`](skills/c4-context/SKILL.md) | Expert C4 Context-level documentation specialist. Creates high-level system context diagrams, documents personas, user journeys, system features, and external dependencies. |
| [`cal-com-automation`](skills/cal-com-automation/SKILL.md) | Automate Cal.com tasks via Rube MCP (Composio): manage bookings, check availability, configure webhooks, and handle teams. Always search tools first for current schemas. |
| [`calendly-automation`](skills/calendly-automation/SKILL.md) | Automate Calendly scheduling, event management, invitee tracking, availability checks, and organization administration via Rube MCP (Composio). Always search tools first for cur... |
| [`canva-automation`](skills/canva-automation/SKILL.md) | Automate Canva tasks via Rube MCP (Composio): designs, exports, folders, brand templates, autofill. Always search tools first for current schemas. |
| [`canvas-design`](skills/canvas-design/SKILL.md) | These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY. Output only .md files, .pdf files, and .png files. |
| [`career-ops-navigator`](skills/career-ops-navigator/SKILL.md) | >- Navegador e assistente de workflow inteligente para o career-ops. Guia o usuário passo a passo em qualquer CLI de IA (Antigravity, Codex, OpenCode, Claude Code, Copilot) trad... |
| [`carrier-relationship-management`](skills/carrier-relationship-management/SKILL.md) | Codified expertise for managing carrier portfolios, negotiating freight rates, tracking carrier performance, allocating freight, and maintaining strategic carrier relationships. |
| [`cc-skill-backend-patterns`](skills/cc-skill-backend-patterns/SKILL.md) | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. |
| [`cc-skill-clickhouse-io`](skills/cc-skill-clickhouse-io/SKILL.md) | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. |
| [`cc-skill-coding-standards`](skills/cc-skill-coding-standards/SKILL.md) | Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development. |
| [`cc-skill-continuous-learning`](skills/cc-skill-continuous-learning/SKILL.md) | Development skill from everything-claude-code |
| [`cc-skill-frontend-patterns`](skills/cc-skill-frontend-patterns/SKILL.md) | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. |
| [`cc-skill-project-guidelines-example`](skills/cc-skill-project-guidelines-example/SKILL.md) | Project Guidelines Skill (Example) |
| [`cc-skill-security-review`](skills/cc-skill-security-review/SKILL.md) | This skill ensures all code follows security best practices and identifies potential vulnerabilities. Use when implementing authentication or authorization, handling user input ... |
| [`cc-skill-strategic-compact`](skills/cc-skill-strategic-compact/SKILL.md) | Development skill from everything-claude-code |
| [`cdk-patterns`](skills/cdk-patterns/SKILL.md) | Common AWS CDK patterns and constructs for building cloud infrastructure with TypeScript, Python, or Java. Use when designing reusable CDK stacks and L3 constructs. |
| [`changelog-automation`](skills/changelog-automation/SKILL.md) | Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. Use when setting up release workflows, generating release notes, or standardizin... |
| [`chat-widget`](skills/chat-widget/SKILL.md) | Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff. Use when the user wants live chat, customer support chat, real-t... |
| [`chrome-extension-developer`](skills/chrome-extension-developer/SKILL.md) | Expert in building Chrome Extensions using Manifest V3. Covers background scripts, service workers, content scripts, and cross-context communication. |
| [`churn-prevention`](skills/churn-prevention/SKILL.md) | Reduce voluntary and involuntary churn with cancel flows, save offers, dunning, win-back tactics, and retention strategy. Use when users are cancelling, failed payments are risi... |
| [`cicd-automation-workflow-automate`](skills/cicd-automation-workflow-automate/SKILL.md) | You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes. Design and implement auto... |
| [`circleci-automation`](skills/circleci-automation/SKILL.md) | Automate CircleCI tasks via Rube MCP (Composio): trigger pipelines, monitor workflows/jobs, retrieve artifacts and test metadata. Always search tools first for current schemas. |
| [`cirq`](skills/cirq/SKILL.md) | Cirq is Google Quantum AI's open-source framework for designing, simulating, and running quantum circuits on quantum computers and simulators. |
| [`citation-management`](skills/citation-management/SKILL.md) | Manage citations systematically throughout the research and writing process. |
| [`claimable-postgres`](skills/claimable-postgres/SKILL.md) | Provision instant temporary Postgres databases via Claimable Postgres by Neon (pg.new). No login or credit card required. Use for quick Postgres environments and throwaway DATAB... |
| [`clarity-gate`](skills/clarity-gate/SKILL.md) | > Pre-ingestion verification for epistemic quality in RAG systems. Ensures documents are properly qualified before entering knowledge bases. Produces CGD (Clarity-Gated Document... |
| [`clarvia-aeo-check`](skills/clarvia-aeo-check/SKILL.md) | Score any MCP server, API, or CLI for agent-readiness using Clarvia AEO (Agent Experience Optimization). Search 15,400+ indexed tools before adding them to your workflow. |
| [`claude-ally-health`](skills/claude-ally-health/SKILL.md) | A health assistant skill for medical information analysis, symptom tracking, and wellness guidance. |
| [`claude-api`](skills/claude-api/SKILL.md) | Build apps with the Claude API or Anthropic SDK. TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`/`claude_agent_sdk`, or user asks to use Claude API, Anthropic SDKs, o... |
| [`claude-code-expert`](skills/claude-code-expert/SKILL.md) | Especialista profundo em Claude Code - CLI da Anthropic. Maximiza produtividade com atalhos, hooks, MCPs, configuracoes avancadas, workflows, CLAUDE.md, memoria, sub-agentes, pe... |
| [`claude-code-guide`](skills/claude-code-guide/SKILL.md) | To provide a comprehensive reference for configuring and using Claude Code (the agentic coding tool) to its full potential. This skill synthesizes best practices, configuration ... |
| [`claude-d3js-skill`](skills/claude-d3js-skill/SKILL.md) | This skill provides guidance for creating sophisticated, interactive data visualisations using d3.js. |
| [`claude-in-chrome-troubleshooting`](skills/claude-in-chrome-troubleshooting/SKILL.md) | Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratic... |
| [`claude-monitor`](skills/claude-monitor/SKILL.md) | Monitor de performance do Claude Code e sistema local. Diagnostica lentidao, mede CPU/RAM/disco, verifica API latency e gera relatorios de saude do sistema. |
| [`claude-scientific-skills`](skills/claude-scientific-skills/SKILL.md) | Scientific research and analysis skills |
| [`claude-settings-audit`](skills/claude-settings-audit/SKILL.md) | Analyze a repository to generate recommended Claude Code settings.json permissions. Use when setting up a new project, auditing existing settings, or determining which read-only... |
| [`claude-speed-reader`](skills/claude-speed-reader/SKILL.md) | -Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting |
| [`claude-win11-speckit-update-skill`](skills/claude-win11-speckit-update-skill/SKILL.md) | Windows 11 system management |
| [`clean-code`](skills/clean-code/SKILL.md) | This skill embodies the principles of \"Clean Code\" by Robert C. Martin (Uncle Bob). Use it to transform \"code that works\" into \"code that is clean.\ |
| [`clerk-auth`](skills/clerk-auth/SKILL.md) | Expert patterns for Clerk auth implementation, middleware, organizations, webhooks, and user sync Use when: adding authentication, clerk auth, user authentication, sign in, sign... |
| [`clickup-automation`](skills/clickup-automation/SKILL.md) | Automate ClickUp project management including tasks, spaces, folders, lists, comments, and team operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`close-automation`](skills/close-automation/SKILL.md) | Automate Close CRM tasks via Rube MCP (Composio): create leads, manage calls/SMS, handle tasks, and track notes. Always search tools first for current schemas. |
| [`closed-loop-delivery`](skills/closed-loop-delivery/SKILL.md) | Use when a coding task must be completed against explicit acceptance criteria with minimal user re-intervention across implementation, review feedback, deployment, and runtime v... |
| [`cloud-architect`](skills/cloud-architect/SKILL.md) | Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural... |
| [`cloud-devops`](skills/cloud-devops/SKILL.md) | Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring, and cloud-native development. |
| [`cloud-penetration-testing`](skills/cloud-penetration-testing/SKILL.md) | Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP). |
| [`cloudflare-workers-expert`](skills/cloudflare-workers-expert/SKILL.md) | Expert in Cloudflare Workers and the Edge Computing ecosystem. Covers Wrangler, KV, D1, Durable Objects, and R2 storage. |
| [`cloudformation-best-practices`](skills/cloudformation-best-practices/SKILL.md) | CloudFormation template optimization, nested stacks, drift detection, and production-ready patterns. Use when writing or reviewing CF templates. |
| [`coda-automation`](skills/coda-automation/SKILL.md) | Automate Coda tasks via Rube MCP (Composio): manage docs, pages, tables, rows, formulas, permissions, and publishing. Always search tools first for current schemas. |
| [`code-documentation-code-explain`](skills/code-documentation-code-explain/SKILL.md) | You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. Transform difficult concepts into... |
| [`code-documentation-doc-generate`](skills/code-documentation-doc-generate/SKILL.md) | You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical... |
| [`code-refactoring-context-restore`](skills/code-refactoring-context-restore/SKILL.md) | Use when working with code refactoring context restore |
| [`code-refactoring-refactor-clean`](skills/code-refactoring-refactor-clean/SKILL.md) | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. Analyze and refactor the provided... |
| [`code-refactoring-tech-debt`](skills/code-refactoring-tech-debt/SKILL.md) | You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. Analyze the codebase to uncover debt, assess its ... |
| [`code-review-ai-ai-review`](skills/code-review-ai-ai-review/SKILL.md) | You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition, and modern DevOps practices. Leverage AI tools (GitHub ... |
| [`code-review-checklist`](skills/code-review-checklist/SKILL.md) | Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability |
| [`code-review-excellence`](skills/code-review-excellence/SKILL.md) | Transform code reviews from gatekeeping to knowledge sharing through constructive feedback, systematic analysis, and collaborative improvement. |
| [`code-reviewer`](skills/code-reviewer/SKILL.md) | Elite code review expert specializing in modern AI-powered code |
| [`code-simplifier`](skills/code-simplifier/SKILL.md) | Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Use when asked to "simplify code", "clean up code", "refactor for c... |
| [`codebase-audit-pre-push`](skills/codebase-audit-pre-push/SKILL.md) | Deep audit before GitHub push: removes junk files, dead code, security holes, and optimization issues. Checks every file line-by-line for production readiness. |
| [`codebase-cleanup-deps-audit`](skills/codebase-cleanup-deps-audit/SKILL.md) | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependencies for known vulnerabilitie... |
| [`codebase-cleanup-refactor-clean`](skills/codebase-cleanup-refactor-clean/SKILL.md) | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best practices. Analyze and refactor the provided... |
| [`codebase-cleanup-tech-debt`](skills/codebase-cleanup-tech-debt/SKILL.md) | You are a technical debt expert specializing in identifying, quantifying, and prioritizing technical debt in software projects. Analyze the codebase to uncover debt, assess its ... |
| [`codex-review`](skills/codex-review/SKILL.md) | Professional code review with auto CHANGELOG generation, integrated with Codex AI. Use when you want professional code review before commits, you need automatic CHANGELOG genera... |
| [`cold-email`](skills/cold-email/SKILL.md) | Write B2B cold emails and follow-up sequences that earn replies. Use when creating outbound prospecting emails, SDR outreach, personalized opening lines, subject lines, CTAs, an... |
| [`comfyui-gateway`](skills/comfyui-gateway/SKILL.md) | REST API gateway for ComfyUI servers. Workflow management, job queuing, webhooks, caching, auth, rate limiting, and image delivery (URL + base64). |
| [`commit`](skills/commit/SKILL.md) | ALWAYS use this skill when committing code changes — never commit directly without it. Creates commits following Sentry conventions with proper conventional commit format and is... |
| [`competitive-landscape`](skills/competitive-landscape/SKILL.md) | Comprehensive frameworks for analyzing competition, identifying differentiation opportunities, and developing winning market positioning strategies. |
| [`competitor-alternatives`](skills/competitor-alternatives/SKILL.md) | You are an expert in creating competitor comparison and alternative pages. Your goal is to build pages that rank for competitive search terms, provide genuine value to evaluator... |
| [`comprehensive-review-full-review`](skills/comprehensive-review-full-review/SKILL.md) | Use when working with comprehensive review full review |
| [`comprehensive-review-pr-enhance`](skills/comprehensive-review-pr-enhance/SKILL.md) | > Generate structured PR descriptions from diffs, add review checklists, risk assessments, and test coverage summaries. Use when the user says "write a PR description", "improve... |
| [`computer-use-agents`](skills/computer-use-agents/SKILL.md) | The fundamental architecture of computer use agents: observe screen, reason about next action, execute action, repeat. This loop integrates vision models with action execution t... |
| [`computer-vision-expert`](skills/computer-vision-expert/SKILL.md) | SOTA Computer Vision Expert (2026). Specialized in YOLO26, Segment Anything 3 (SAM 3), Vision Language Models, and real-time spatial analysis. |
| [`concise-planning`](skills/concise-planning/SKILL.md) | Use when a user asks for a plan for a coding task, to generate a clear, actionable, and atomic checklist. |
| [`conductor-implement`](skills/conductor-implement/SKILL.md) | Execute tasks from a track's implementation plan following TDD workflow |
| [`conductor-manage`](skills/conductor-manage/SKILL.md) | Manage track lifecycle: archive, restore, delete, rename, and cleanup |
| [`conductor-new-track`](skills/conductor-new-track/SKILL.md) | Create a new track with specification and phased implementation plan |
| [`conductor-revert`](skills/conductor-revert/SKILL.md) | Git-aware undo by logical work unit (track, phase, or task) |
| [`conductor-setup`](skills/conductor-setup/SKILL.md) | Configure a Rails project to work with Conductor (parallel coding agents) |
| [`conductor-status`](skills/conductor-status/SKILL.md) | Display project status, active tracks, and next actions |
| [`conductor-validator`](skills/conductor-validator/SKILL.md) | Validates Conductor project artifacts for completeness, consistency, and correctness. Use after setup, when diagnosing issues, or before implementation to verify project context. |
| [`confluence-automation`](skills/confluence-automation/SKILL.md) | Automate Confluence page creation, content search, space management, labels, and hierarchy navigation via Rube MCP (Composio). Always search tools first for current schemas. |
| [`constant-time-analysis`](skills/constant-time-analysis/SKILL.md) | Analyze cryptographic code to detect operations that leak secret data through execution timing variations. |
| [`content-creator`](skills/content-creator/SKILL.md) | Professional-grade brand voice analysis, SEO optimization, and platform-specific content frameworks. |
| [`content-marketer`](skills/content-marketer/SKILL.md) | Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimization, and data-driven performance marketing. |
| [`content-strategy`](skills/content-strategy/SKILL.md) | Plan a content strategy, topic clusters, editorial roadmap, and content mix for traffic, authority, and lead generation. Use when deciding what to publish, what topics to priori... |
| [`context-agent`](skills/context-agent/SKILL.md) | Agente de contexto para continuidade entre sessoes. Salva resumos, decisoes, tarefas pendentes e carrega briefing automatico na sessao seguinte. |
| [`context-compression`](skills/context-compression/SKILL.md) | When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach is aggressive compression to minimize tokens per request. |
| [`context-degradation`](skills/context-degradation/SKILL.md) | Language models exhibit predictable degradation patterns as context length increases. Understanding these patterns is essential for diagnosing failures and designing resilient s... |
| [`context-driven-development`](skills/context-driven-development/SKILL.md) | Guide for implementing and maintaining context as a managed artifact alongside code, enabling consistent AI interactions and team alignment through structured project documentat... |
| [`context-fundamentals`](skills/context-fundamentals/SKILL.md) | Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, too... |
| [`context-guardian`](skills/context-guardian/SKILL.md) | Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao. |
| [`context-management-context-restore`](skills/context-management-context-restore/SKILL.md) | Use when working with context management context restore |
| [`context-management-context-save`](skills/context-management-context-save/SKILL.md) | Use when working with context management context save |
| [`context-manager`](skills/context-manager/SKILL.md) | Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory systems. |
| [`context-optimization`](skills/context-optimization/SKILL.md) | Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and partitioning. The goal is not to magically in... |
| [`context-window-management`](skills/context-window-management/SKILL.md) | You're a context engineering specialist who has optimized LLM applications handling millions of conversations. You've seen systems hit token limits, suffer context rot, and lose... |
| [`context7`](skills/context7/SKILL.md) | Use Context7 for current, version-specific library and framework documentation. Trigger when the user asks about package APIs, framework setup, SDK usage, migrations, deprecatio... |
| [`context7-auto-research`](skills/context7-auto-research/SKILL.md) | Automatically fetch latest library/framework documentation for Claude Code via Context7 API. Use when you need up-to-date documentation for libraries and frameworks or asking ab... |
| [`conversation-memory`](skills/conversation-memory/SKILL.md) | Persistent memory systems for LLM conversations including short-term, long-term, and entity-based memory Use when: conversation memory, remember, memory persistence, long-term m... |
| [`convertkit-automation`](skills/convertkit-automation/SKILL.md) | Automate ConvertKit (Kit) tasks via Rube MCP (Composio): manage subscribers, tags, broadcasts, and broadcast stats. Always search tools first for current schemas. |
| [`convex`](skills/convex/SKILL.md) | Convex reactive backend expert: schema design, TypeScript functions, real-time subscriptions, auth, file storage, scheduling, and deployment. |
| [`copilot-sdk`](skills/copilot-sdk/SKILL.md) | Build applications that programmatically interact with GitHub Copilot. The SDK wraps the Copilot CLI via JSON-RPC, providing session management, custom tools, hooks, MCP server ... |
| [`copy-editing`](skills/copy-editing/SKILL.md) | You are an expert copy editor specializing in marketing and conversion copy. Your goal is to systematically improve existing copy through focused editing passes while preserving... |
| [`copywriting`](skills/copywriting/SKILL.md) | Write rigorous, conversion-focused marketing copy for landing pages and emails. Enforces brief confirmation and strict no-fabrication rules. |
| [`copywriting-psychologist`](skills/copywriting-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`core-components`](skills/core-components/SKILL.md) | Core component library and design system patterns. Use when building UI, using design tokens, or working with the component library. |
| [`cost-optimization`](skills/cost-optimization/SKILL.md) | Strategies and patterns for optimizing cloud costs across AWS, Azure, and GCP. |
| [`cpp-pro`](skills/cpp-pro/SKILL.md) | Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. Handles templates, move semantics, and performance optimization. |
| [`cqrs-implementation`](skills/cqrs-implementation/SKILL.md) | Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing query performance, or building event-sourced... |
| [`create-branch`](skills/create-branch/SKILL.md) | Create a git branch following Sentry naming conventions. Use when asked to "create a branch", "new branch", "start a branch", "make a branch", "switch to a new branch", or when ... |
| [`create-issue-gate`](skills/create-issue-gate/SKILL.md) | Use when starting a new implementation task and an issue must be created with strict acceptance criteria gating before execution. |
| [`create-pr`](skills/create-pr/SKILL.md) | Alias for sentry-skills:pr-writer. Use when users explicitly ask for "create-pr" or reference the legacy skill name. Redirects to the canonical PR writing workflow. |
| [`cred-omega`](skills/cred-omega/SKILL.md) | CISO operacional enterprise para gestao total de credenciais e segredos. |
| [`crewai`](skills/crewai/SKILL.md) | You are an expert in designing collaborative AI agent teams with CrewAI. You think in terms of roles, responsibilities, and delegation. You design clear agent personas with spec... |
| [`crypto-bd-agent`](skills/crypto-bd-agent/SKILL.md) | Production-tested patterns for building AI agents that autonomously discover, > evaluate, and acquire token listings for cryptocurrency exchanges. |
| [`csharp-pro`](skills/csharp-pro/SKILL.md) | Write modern C# code with advanced features like records, pattern matching, and async/await. Optimizes .NET applications, implements enterprise patterns, and ensures comprehensi... |
| [`customer-psychographic-profiler`](skills/customer-psychographic-profiler/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`customer-support`](skills/customer-support/SKILL.md) | Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel support experiences. |
| [`customs-trade-compliance`](skills/customs-trade-compliance/SKILL.md) | Codified expertise for customs documentation, tariff classification, duty optimisation, restricted party screening, and regulatory compliance across multiple jurisdictions. |

<a id="indice-d"></a>
### Letra D (77 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`daily`](skills/daily/SKILL.md) | Documentation and capabilities reference for Daily |
| [`daily-news-report`](skills/daily-news-report/SKILL.md) | Scrapes content based on a preset URL list, filters high-quality technical information, and generates daily Markdown reports. |
| [`data-autocleaning`](skills/data-autocleaning/SKILL.md) | Automated data quality and transformation capabilities for Dataform/dbt/BigQuery pipelines. Processes data sourced from BigQuery or Cloud Storage (GCS), applying best practices ... |
| [`data-engineer`](skills/data-engineer/SKILL.md) | Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. Implements Apache Spark, dbt, Airflow, and cloud-native data platforms. |
| [`data-engineering-data-driven-feature`](skills/data-engineering-data-driven-feature/SKILL.md) | Build features guided by data insights, A/B testing, and continuous measurement using specialized agents for analysis, implementation, and experimentation. |
| [`data-engineering-data-pipeline`](skills/data-engineering-data-pipeline/SKILL.md) | You are a data pipeline architecture expert specializing in scalable, reliable, and cost-effective data pipelines for batch and streaming data processing. |
| [`data-quality-frameworks`](skills/data-quality-frameworks/SKILL.md) | Implement data quality validation with Great Expectations, dbt tests, and data contracts. Use when building data quality pipelines, implementing validation rules, or establishin... |
| [`data-scientist`](skills/data-scientist/SKILL.md) | Expert data scientist for advanced analytics, machine learning, and statistical modeling. Handles complex data analysis, predictive modeling, and business intelligence. |
| [`data-storytelling`](skills/data-storytelling/SKILL.md) | Transform raw data into compelling narratives that drive decisions and inspire action. |
| [`data-structure-protocol`](skills/data-structure-protocol/SKILL.md) | Give agents persistent structural memory of a codebase — navigate dependencies, track public APIs, and understand why connections exist without re-reading the whole repo. |
| [`database`](skills/database/SKILL.md) | Database development and operations workflow covering SQL, NoSQL, database design, migrations, optimization, and data engineering. |
| [`database-admin`](skills/database-admin/SKILL.md) | Expert database administrator specializing in modern cloud databases, automation, and reliability engineering. |
| [`database-architect`](skills/database-architect/SKILL.md) | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database architectures. |
| [`database-cloud-optimization-cost-optimize`](skills/database-cloud-optimization-cost-optimize/SKILL.md) | You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability. Analyze cloud spending, identify savings... |
| [`database-design`](skills/database-design/SKILL.md) | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. |
| [`database-migration`](skills/database-migration/SKILL.md) | Master database schema and data migrations across ORMs (Sequelize, TypeORM, Prisma), including rollback strategies and zero-downtime deployments. |
| [`database-migrations-migration-observability`](skills/database-migrations-migration-observability/SKILL.md) | Migration monitoring, CDC, and observability infrastructure |
| [`database-migrations-sql-migrations`](skills/database-migrations-sql-migrations/SKILL.md) | SQL database migrations with zero-downtime strategies for PostgreSQL, MySQL, and SQL Server. Focus on data integrity and rollback plans. |
| [`database-optimizer`](skills/database-optimizer/SKILL.md) | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. |
| [`datadog-automation`](skills/datadog-automation/SKILL.md) | Automate Datadog tasks via Rube MCP (Composio): query metrics, search logs, manage monitors/dashboards, create events and downtimes. Always search tools first for current schemas. |
| [`dataform-bigquery`](skills/dataform-bigquery/SKILL.md) | Expertise in generating clean, correct, and efficient Dataform pipeline code for BigQuery ELT. Use this when creating or modifying Dataform pipelines, actions, or source declara... |
| [`dbos-golang`](skills/dbos-golang/SKILL.md) | Guide for building reliable, fault-tolerant Go applications with DBOS durable workflows. Use when adding DBOS to existing Go code, creating workflows and steps, or using queues ... |
| [`dbos-python`](skills/dbos-python/SKILL.md) | Guide for building reliable, fault-tolerant Python applications with DBOS durable workflows. Use when adding DBOS to existing Python code, creating workflows and steps, or using... |
| [`dbos-typescript`](skills/dbos-typescript/SKILL.md) | Guide for building reliable, fault-tolerant TypeScript applications with DBOS durable workflows. Use when adding DBOS to existing TypeScript code, creating workflows and steps, ... |
| [`dbt-bigquery`](skills/dbt-bigquery/SKILL.md) | Expert guidance for creating, modifying, and optimizing dbt pipelines for BigQuery. Use this skill whenever user asks for generating or modifying a dbt model or project. Activat... |
| [`dbt-transformation-patterns`](skills/dbt-transformation-patterns/SKILL.md) | Production-ready patterns for dbt (data build tool) including model organization, testing strategies, documentation, and incremental processing. |
| [`ddd-context-mapping`](skills/ddd-context-mapping/SKILL.md) | Map relationships between bounded contexts and define integration contracts using DDD context mapping patterns. |
| [`ddd-strategic-design`](skills/ddd-strategic-design/SKILL.md) | Design DDD strategic artifacts including subdomains, bounded contexts, and ubiquitous language for complex business domains. |
| [`ddd-tactical-patterns`](skills/ddd-tactical-patterns/SKILL.md) | Apply DDD tactical patterns in code using entities, value objects, aggregates, repositories, and domain events with explicit invariants. |
| [`debug-buttercup`](skills/debug-buttercup/SKILL.md) | All pods run in namespace crs. Use when pods in the crs namespace are in CrashLoopBackOff, OOMKilled, or restarting, multiple services restart simultaneously (cascade failure), ... |
| [`debugger`](skills/debugger/SKILL.md) | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. |
| [`debugging-strategies`](skills/debugging-strategies/SKILL.md) | Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical approaches. |
| [`debugging-toolkit-smart-debug`](skills/debugging-toolkit-smart-debug/SKILL.md) | Use when working with debugging toolkit smart debug |
| [`deep-research`](skills/deep-research/SKILL.md) | Run autonomous research tasks that plan, search, read, and synthesize information into comprehensive reports. |
| [`defi-protocol-templates`](skills/defi-protocol-templates/SKILL.md) | Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and lending systems. Use when building decentralized finance applications or smart contra... |
| [`defuddle`](skills/defuddle/SKILL.md) | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch when the user provides a URL to read or... |
| [`dependency-management-deps-audit`](skills/dependency-management-deps-audit/SKILL.md) | You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependencies for known vulnerabilitie... |
| [`dependency-upgrade`](skills/dependency-upgrade/SKILL.md) | Master major dependency version upgrades, compatibility analysis, staged upgrade strategies, and comprehensive testing approaches. |
| [`deployment-engineer`](skills/deployment-engineer/SKILL.md) | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. |
| [`deployment-pipeline-design`](skills/deployment-pipeline-design/SKILL.md) | Architecture patterns for multi-stage CI/CD pipelines with approval gates and deployment strategies. |
| [`deployment-procedures`](skills/deployment-procedures/SKILL.md) | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts. |
| [`deployment-validation-config-validate`](skills/deployment-validation-config-validate/SKILL.md) | You are a configuration management expert specializing in validating, testing, and ensuring the correctness of application configurations. Create comprehensive validation schema... |
| [`design-md`](skills/design-md/SKILL.md) | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files |
| [`design-orchestration`](skills/design-orchestration/SKILL.md) | Orchestrates design workflows by routing work through brainstorming, multi-agent review, and execution readiness in the correct order. |
| [`design-spells`](skills/design-spells/SKILL.md) | Curated micro-interactions and design details that add "magic" and personality to websites and apps. |
| [`devcontainer-setup`](skills/devcontainer-setup/SKILL.md) | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up is... |
| [`development`](skills/development/SKILL.md) | Comprehensive web, mobile, and backend development workflow bundling frontend, backend, full-stack, and mobile development skills for end-to-end application delivery. |
| [`devops-deploy`](skills/devops-deploy/SKILL.md) | DevOps e deploy de aplicacoes — Docker, CI/CD com GitHub Actions, AWS Lambda, SAM, Terraform, infraestrutura como codigo e monitoramento. |
| [`devops-troubleshooter`](skills/devops-troubleshooter/SKILL.md) | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. |
| [`diary`](skills/diary/SKILL.md) | Unified Diary System: A context-preserving automated logger for multi-project development. |
| [`differential-review`](skills/differential-review/SKILL.md) | Security-focused code review for PRs, commits, and diffs. |
| [`discord-automation`](skills/discord-automation/SKILL.md) | Automate Discord tasks via Rube MCP (Composio): messages, channels, roles, webhooks, reactions. Always search tools first for current schemas. |
| [`discord-bot-architect`](skills/discord-bot-architect/SKILL.md) | Specialized skill for building production-ready Discord bots. Covers Discord.js (JavaScript) and Pycord (Python), gateway intents, slash commands, interactive components, rate l... |
| [`discovering-gcp-data-assets`](skills/discovering-gcp-data-assets/SKILL.md) | \| Finds and inspects data assets within Google Cloud. Relevant when any of the following conditions are true: 1. The user request involves finding, exploring, or inspecting dat... |
| [`dispatching-parallel-agents`](skills/dispatching-parallel-agents/SKILL.md) | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| [`distributed-debugging-debug-trace`](skills/distributed-debugging-debug-trace/SKILL.md) | You are a debugging expert specializing in setting up comprehensive debugging environments, distributed tracing, and diagnostic tools. Configure debugging workflows, implement t... |
| [`distributed-tracing`](skills/distributed-tracing/SKILL.md) | Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices. |
| [`django-access-review`](skills/django-access-review/SKILL.md) | django-access-review |
| [`django-perf-review`](skills/django-perf-review/SKILL.md) | Django performance code review. Use when asked to "review Django performance", "find N+1 queries", "optimize Django", "check queryset performance", "database performance", "Djan... |
| [`django-pro`](skills/django-pro/SKILL.md) | Master Django 5.x with async views, DRF, Celery, and Django Channels. Build scalable web applications with proper architecture, testing, and deployment. |
| [`doc-coauthoring`](skills/doc-coauthoring/SKILL.md) | This skill provides a structured workflow for guiding users through collaborative document creation. Act as an active guide, walking users through three stages: Context Gatherin... |
| [`docker-expert`](skills/docker-expert/SKILL.md) | You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization, security hardening, multi-stage builds, orchestration patte... |
| [`docs`](skills/docs/SKILL.md) | Instruções e utilitários especializados para docs. |
| [`docs-architect`](skills/docs-architect/SKILL.md) | Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details to produce long-form technical manuals ... |
| [`documentation`](skills/documentation/SKILL.md) | Documentation generation workflow covering API docs, architecture docs, README files, code comments, and technical writing. |
| [`documentation-generation-doc-generate`](skills/documentation-generation-doc-generate/SKILL.md) | You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical... |
| [`documentation-templates`](skills/documentation-templates/SKILL.md) | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. |
| [`docusign-automation`](skills/docusign-automation/SKILL.md) | Automate DocuSign tasks via Rube MCP (Composio): templates, envelopes, signatures, document management. Always search tools first for current schemas. |
| [`docx-official`](skills/docx-official/SKILL.md) | A user may ask you to create, edit, or analyze the contents of a .docx file. A .docx file is essentially a ZIP archive containing XML files and other resources that you can read... |
| [`domain-driven-design`](skills/domain-driven-design/SKILL.md) | Plan and route Domain-Driven Design work from strategic modeling to tactical implementation and evented architecture patterns. |
| [`dotnet-architect`](skills/dotnet-architect/SKILL.md) | Expert .NET backend architect specializing in C#, ASP.NET Core, Entity Framework, Dapper, and enterprise application patterns. |
| [`dotnet-backend`](skills/dotnet-backend/SKILL.md) | Build ASP.NET Core 8+ backend services with EF Core, auth, background jobs, and production API patterns. |
| [`dotnet-backend-patterns`](skills/dotnet-backend-patterns/SKILL.md) | Master C#/.NET patterns for building production-grade APIs, MCP servers, and enterprise backends with modern best practices (2024/2025). |
| [`drizzle-orm-expert`](skills/drizzle-orm-expert/SKILL.md) | Expert in Drizzle ORM for TypeScript — schema design, relational queries, migrations, and serverless database integration. Use when building type-safe database layers with Drizzle. |
| [`dropbox-automation`](skills/dropbox-automation/SKILL.md) | Automate Dropbox file management, sharing, search, uploads, downloads, and folder operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`dwarf-expert`](skills/dwarf-expert/SKILL.md) | Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWA... |
| [`dx-optimizer`](skills/dx-optimizer/SKILL.md) | Developer Experience specialist. Improves tooling, setup, and workflows. Use PROACTIVELY when setting up new projects, after team feedback, or when development friction is noticed. |

<a id="indice-e"></a>
### Letra E (40 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`e2e-testing`](skills/e2e-testing/SKILL.md) | End-to-end testing workflow with Playwright for browser automation, visual regression, cross-browser testing, and CI/CD integration. |
| [`e2e-testing-patterns`](skills/e2e-testing-patterns/SKILL.md) | Build reliable, fast, and maintainable end-to-end test suites that provide confidence to ship code quickly and catch regressions before users do. |
| [`earllm-build`](skills/earllm-build/SKILL.md) | Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pipeline. |
| [`electron-development`](skills/electron-development/SKILL.md) | Master Electron desktop app development with secure IPC, contextIsolation, preload scripts, multi-process architecture, electron-builder packaging, code signing, and auto-update. |
| [`elixir-pro`](skills/elixir-pro/SKILL.md) | Write idiomatic Elixir code with OTP patterns, supervision trees, and Phoenix LiveView. Masters concurrency, fault tolerance, and distributed systems. |
| [`elon-musk`](skills/elon-musk/SKILL.md) | Agente que simula Elon Musk com profundidade psicologica e comunicacional de alta fidelidade. Ativado para: \"fale como Elon\", \"simule Elon Musk\", \"o que Elon diria sobre X\... |
| [`email-sequence`](skills/email-sequence/SKILL.md) | You are an expert in email marketing and automation. Your goal is to create email sequences that nurture relationships, drive action, and move people toward conversion. |
| [`email-systems`](skills/email-systems/SKILL.md) | You are an email systems engineer who has maintained 99.9% deliverability across millions of emails. You've debugged SPF/DKIM/DMARC, dealt with blacklists, and optimized for inb... |
| [`embedding-strategies`](skills/embedding-strategies/SKILL.md) | Guide to selecting and optimizing embedding models for vector search applications. |
| [`emblemai-crypto-wallet`](skills/emblemai-crypto-wallet/SKILL.md) | Crypto wallet management across 7 blockchains via EmblemAI Agent Hustle API. Balance checks, token swaps, portfolio analysis, and transaction execution for Solana, Ethereum, Bas... |
| [`emergency-card`](skills/emergency-card/SKILL.md) | 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。 |
| [`emotional-arc-designer`](skills/emotional-arc-designer/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`employment-contract-templates`](skills/employment-contract-templates/SKILL.md) | Templates and patterns for creating legally sound employment documentation including contracts, offer letters, and HR policies. |
| [`energy-procurement`](skills/energy-procurement/SKILL.md) | Codified expertise for electricity and gas procurement, tariff optimisation, demand charge management, renewable PPA evaluation, and multi-facility energy cost management. |
| [`enforcing-resource-attribution`](skills/enforcing-resource-attribution/SKILL.md) | Enforces resource attribution for CLI commands. Use this skill whenever you are running `bq` or `gcloud` commands via `run_command`. It ensures mandatory labeling for supported ... |
| [`enhance-prompt`](skills/enhance-prompt/SKILL.md) | Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances specificity, adds UI/UX keywords, injects design system context, and structures output for better gen... |
| [`environment-setup-guide`](skills/environment-setup-guide/SKILL.md) | Guide developers through setting up development environments with proper tools, dependencies, and configurations |
| [`error-debugging-error-analysis`](skills/error-debugging-error-analysis/SKILL.md) | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability so... |
| [`error-debugging-error-trace`](skills/error-debugging-error-trace/SKILL.md) | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error tracking systems, configure alerts, implem... |
| [`error-debugging-multi-agent-review`](skills/error-debugging-multi-agent-review/SKILL.md) | Use when working with error debugging multi agent review |
| [`error-detective`](skills/error-detective/SKILL.md) | Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes. |
| [`error-diagnostics-error-analysis`](skills/error-diagnostics-error-analysis/SKILL.md) | You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and implementing comprehensive observability so... |
| [`error-diagnostics-error-trace`](skills/error-diagnostics-error-trace/SKILL.md) | You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error tracking systems, configure alerts, implem... |
| [`error-diagnostics-smart-debug`](skills/error-diagnostics-smart-debug/SKILL.md) | Use when working with error diagnostics smart debug |
| [`error-handling-patterns`](skills/error-handling-patterns/SKILL.md) | Build resilient applications with robust error handling strategies that gracefully handle failures and provide excellent debugging experiences. |
| [`ethical-hacking-methodology`](skills/ethical-hacking-methodology/SKILL.md) | Master the complete penetration testing lifecycle from reconnaissance through reporting. This skill covers the five stages of ethical hacking methodology, essential tools, attac... |
| [`evaluation`](skills/evaluation/SKILL.md) | Build evaluation frameworks for agent systems. Use when testing agent performance systematically, validating context engineering choices, or measuring improvements over time. |
| [`event-sourcing-architect`](skills/event-sourcing-architect/SKILL.md) | Expert in event sourcing, CQRS, and event-driven architecture patterns. Masters event store design, projection building, saga orchestration, and eventual consistency patterns. U... |
| [`event-store-design`](skills/event-store-design/SKILL.md) | Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store technologies, or implementing event persistenc... |
| [`evolution`](skills/evolution/SKILL.md) | This skill enables makepad-skills to self-improve continuously during development. |
| [`exa-search`](skills/exa-search/SKILL.md) | Semantic search, similar content discovery, and structured research using Exa API. Use when you need semantic/embeddings-based search, finding similar content, or searching by c... |
| [`executing-plans`](skills/executing-plans/SKILL.md) | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| [`explain-like-socrates`](skills/explain-like-socrates/SKILL.md) | > Explains concepts using Socratic-style dialogue. Use when the user asks to explain, teach or help understand a concept like socrates. |
| [`expo-api-routes`](skills/expo-api-routes/SKILL.md) | Guidelines for creating API routes in Expo Router with EAS Hosting |
| [`expo-cicd-workflows`](skills/expo-cicd-workflows/SKILL.md) | Helps understand and write EAS workflow YAML files for Expo projects. Use this skill when the user asks about CI/CD or workflows in an Expo or EAS context, mentions .eas/workflo... |
| [`expo-deployment`](skills/expo-deployment/SKILL.md) | Deploy Expo apps to production |
| [`expo-dev-client`](skills/expo-dev-client/SKILL.md) | Build and distribute Expo development clients locally or via TestFlight |
| [`expo-tailwind-setup`](skills/expo-tailwind-setup/SKILL.md) | Set up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling |
| [`expo-ui-jetpack-compose`](skills/expo-ui-jetpack-compose/SKILL.md) | expo-ui-jetpack-compose |
| [`expo-ui-swift-ui`](skills/expo-ui-swift-ui/SKILL.md) | expo-ui-swift-ui |

<a id="indice-f"></a>
### Letra F (64 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`fal-audio`](skills/fal-audio/SKILL.md) | Text-to-speech and speech-to-text using fal.ai audio models |
| [`fal-generate`](skills/fal-generate/SKILL.md) | Generate images and videos using fal.ai AI models |
| [`fal-image-edit`](skills/fal-image-edit/SKILL.md) | AI-powered image editing with style transfer and object removal |
| [`fal-platform`](skills/fal-platform/SKILL.md) | Platform APIs for model management, pricing, and usage tracking |
| [`fal-upscale`](skills/fal-upscale/SKILL.md) | Upscale and enhance image and video resolution using AI |
| [`fal-workflow`](skills/fal-workflow/SKILL.md) | Generate workflow JSON files for chaining AI models |
| [`family-health-analyzer`](skills/family-health-analyzer/SKILL.md) | 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议 |
| [`fastapi-pro`](skills/fastapi-pro/SKILL.md) | Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Master microservices, WebSockets, and modern Python async patterns. |
| [`fastapi-router-py`](skills/fastapi-router-py/SKILL.md) | Create FastAPI routers following established patterns with proper authentication, response models, and HTTP status codes. |
| [`fastapi-templates`](skills/fastapi-templates/SKILL.md) | Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. Use when building new FastAPI applications or setting up ba... |
| [`favicon`](skills/favicon/SKILL.md) | Generate favicons from a source image |
| [`fda-food-safety-auditor`](skills/fda-food-safety-auditor/SKILL.md) | Expert AI auditor for FDA Food Safety (FSMA), HACCP, and PCQI compliance. Reviews food facility records and preventive controls. |
| [`fda-medtech-compliance-auditor`](skills/fda-medtech-compliance-auditor/SKILL.md) | Expert AI auditor for Medical Device (SaMD) compliance, IEC 62304, and 21 CFR Part 820. Reviews DHFs, technical files, and software validation. |
| [`federate-lakehouse-catalog`](skills/federate-lakehouse-catalog/SKILL.md) | Sets up Google Cloud Lakehouse federated catalogs to remote Iceberg REST Catalogs. Currently supported catalogs: Databricks Unity, AWS Glue. Supported clouds hosting those catal... |
| [`ffuf-claude-skill`](skills/ffuf-claude-skill/SKILL.md) | Web fuzzing with ffuf |
| [`ffuf-web-fuzzing`](skills/ffuf-web-fuzzing/SKILL.md) | Expert guidance for ffuf web fuzzing during penetration testing, including authenticated fuzzing with raw requests, auto-calibration, and result analysis |
| [`figma-automation`](skills/figma-automation/SKILL.md) | Automate Figma tasks via Rube MCP (Composio): files, components, design tokens, comments, exports. Always search tools first for current schemas. |
| [`file-organizer`](skills/file-organizer/SKILL.md) | 6. Reduces Clutter: Identifies old files you probably don't need anymore |
| [`file-path-traversal`](skills/file-path-traversal/SKILL.md) | Identify and exploit file path traversal (directory traversal) vulnerabilities that allow attackers to read arbitrary files on the server, potentially including sensitive config... |
| [`file-uploads`](skills/file-uploads/SKILL.md) | Careful about security and performance. Never trusts file extensions. Knows that large uploads need special handling. Prefers presigned URLs over server proxying. |
| [`filesystem-context`](skills/filesystem-context/SKILL.md) | Use for file-based context management, dynamic context discovery, and reducing context window bloat. Offload context to files for just-in-time loading. |
| [`find-bugs`](skills/find-bugs/SKILL.md) | Find bugs, security vulnerabilities, and code quality issues in local branch changes. Use when asked to review changes, find bugs, security review, or audit code on the current ... |
| [`finishing-a-development-branch`](skills/finishing-a-development-branch/SKILL.md) | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options fo... |
| [`firebase`](skills/firebase/SKILL.md) | You're a developer who has shipped dozens of Firebase projects. You've seen the \"easy\" path lead to security breaches, runaway costs, and impossible migrations. You know Fireb... |
| [`firecrawl-scraper`](skills/firecrawl-scraper/SKILL.md) | Deep web scraping, screenshots, PDF parsing, and website crawling using Firecrawl API. Use when you need deep content extraction from web pages, page interaction is required (cl... |
| [`firmware-analyst`](skills/firmware-analyst/SKILL.md) | Expert firmware analyst specializing in embedded systems, IoT security, and hardware reverse engineering. |
| [`fitness-analyzer`](skills/fitness-analyzer/SKILL.md) | 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。 |
| [`fix-review`](skills/fix-review/SKILL.md) | Verify fix commits address audit findings without new bugs |
| [`fixing-accessibility`](skills/fixing-accessibility/SKILL.md) | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. Use when adding interactive controls, form... |
| [`fixing-metadata`](skills/fixing-metadata/SKILL.md) | Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, JSON-LD structured data, and robots directives. U... |
| [`fixing-motion-performance`](skills/fixing-motion-performance/SKILL.md) | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. Use when animations stutter, transitions ja... |
| [`flutter-expert`](skills/flutter-expert/SKILL.md) | Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment. |
| [`food-database-query`](skills/food-database-query/SKILL.md) | Food Database Query |
| [`form-cro`](skills/form-cro/SKILL.md) | Optimize any form that is NOT signup or account registration — including lead capture, contact, demo request, application, survey, quote, and checkout forms. |
| [`fp-async`](skills/fp-async/SKILL.md) | Practical async patterns using TaskEither - clean pipelines instead of try/catch hell, with real API examples |
| [`fp-backend`](skills/fp-backend/SKILL.md) | Functional programming patterns for Node.js/Deno backend development using fp-ts, ReaderTaskEither, and functional dependency injection |
| [`fp-data-transforms`](skills/fp-data-transforms/SKILL.md) | Everyday data transformations using functional patterns - arrays, objects, grouping, aggregation, and null-safe access |
| [`fp-either-ref`](skills/fp-either-ref/SKILL.md) | Quick reference for Either type. Use when user needs error handling, validation, or operations that can fail with typed errors. |
| [`fp-errors`](skills/fp-errors/SKILL.md) | Stop throwing everywhere - handle errors as values using Either and TaskEither for cleaner, more predictable code |
| [`fp-option-ref`](skills/fp-option-ref/SKILL.md) | Quick reference for Option type. Use when user needs to handle nullable values, optional data, or wants to avoid null checks. |
| [`fp-pipe-ref`](skills/fp-pipe-ref/SKILL.md) | Quick reference for pipe and flow. Use when user needs to chain functions, compose operations, or build data pipelines in fp-ts. |
| [`fp-pragmatic`](skills/fp-pragmatic/SKILL.md) | A practical, jargon-free guide to functional programming - the 80/20 approach that gets results without the academic overhead |
| [`fp-react`](skills/fp-react/SKILL.md) | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Works with React 18/19, Next.js 14/15. |
| [`fp-refactor`](skills/fp-refactor/SKILL.md) | Comprehensive guide for refactoring imperative TypeScript code to fp-ts functional patterns |
| [`fp-taskeither-ref`](skills/fp-taskeither-ref/SKILL.md) | Quick reference for TaskEither. Use when user needs async error handling, API calls, or Promise-based operations that can fail. |
| [`fp-ts-errors`](skills/fp-ts-errors/SKILL.md) | Handle errors as values using fp-ts Either and TaskEither for cleaner, more predictable TypeScript code. Use when implementing error handling patterns with fp-ts. |
| [`fp-ts-pragmatic`](skills/fp-ts-pragmatic/SKILL.md) | A practical, jargon-free guide to fp-ts functional programming - the 80/20 approach that gets results without the academic overhead. Use when writing TypeScript with fp-ts library. |
| [`fp-ts-react`](skills/fp-ts-react/SKILL.md) | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Use when building React apps with functional programming patterns. Works with React 18/19, Ne... |
| [`fp-types-ref`](skills/fp-types-ref/SKILL.md) | Quick reference for fp-ts types. Use when user asks which type to use, needs Option/Either/Task decision help, or wants fp-ts imports. |
| [`framework-migration-code-migrate`](skills/framework-migration-code-migrate/SKILL.md) | You are a code migration expert specializing in transitioning codebases between frameworks, languages, versions, and platforms. Generate comprehensive migration plans, automated... |
| [`framework-migration-deps-upgrade`](skills/framework-migration-deps-upgrade/SKILL.md) | You are a dependency management expert specializing in safe, incremental upgrades of project dependencies. Plan and execute dependency updates with minimal risk, proper testing,... |
| [`framework-migration-legacy-modernize`](skills/framework-migration-legacy-modernize/SKILL.md) | Orchestrate a comprehensive legacy system modernization using the strangler fig pattern, enabling gradual replacement of outdated components while maintaining continuous busines... |
| [`free-tool-strategy`](skills/free-tool-strategy/SKILL.md) | You are an expert in engineering-as-marketing strategy. Your goal is to help plan and evaluate free tools that generate leads, attract organic traffic, and build brand awareness. |
| [`freshdesk-automation`](skills/freshdesk-automation/SKILL.md) | Automate Freshdesk helpdesk operations including tickets, contacts, companies, notes, and replies via Rube MCP (Composio). Always search tools first for current schemas. |
| [`freshservice-automation`](skills/freshservice-automation/SKILL.md) | Automate Freshservice ITSM tasks via Rube MCP (Composio): create/update tickets, bulk operations, service requests, and outbound emails. Always search tools first for current sc... |
| [`frontend-design`](skills/frontend-design/SKILL.md) | You are a frontend designer-engineer, not a layout generator. |
| [`frontend-dev-guidelines`](skills/frontend-dev-guidelines/SKILL.md) | You are a senior frontend engineer operating under strict architectural and performance standards. Use when creating components or pages, adding new features, or fetching or mut... |
| [`frontend-developer`](skills/frontend-developer/SKILL.md) | Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern frontend architecture. |
| [`frontend-mobile-development-component-scaffold`](skills/frontend-mobile-development-component-scaffold/SKILL.md) | You are a React component architecture expert specializing in scaffolding production-ready, accessible, and performant components. Generate complete component implementations wi... |
| [`frontend-mobile-security-xss-scan`](skills/frontend-mobile-security-xss-scan/SKILL.md) | You are a frontend security specialist focusing on Cross-Site Scripting (XSS) vulnerability detection and prevention. Analyze React, Vue, Angular, and vanilla JavaScript code to... |
| [`frontend-security-coder`](skills/frontend-security-coder/SKILL.md) | Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns. |
| [`frontend-slides`](skills/frontend-slides/SKILL.md) | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. |
| [`frontend-ui-dark-ts`](skills/frontend-ui-dark-ts/SKILL.md) | A modern dark-themed React UI system using Tailwind CSS and Framer Motion. Designed for dashboards, admin panels, and data-rich applications with glassmorphism effects and taste... |
| [`full-stack-orchestration-full-stack-feature`](skills/full-stack-orchestration-full-stack-feature/SKILL.md) | Use when working with full stack orchestration full stack feature |

<a id="indice-g"></a>
### Letra G (121 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`game-development`](skills/game-development/SKILL.md) | Game development orchestrator. Routes to platform-specific skills based on project needs. |
| [`gcloud-auth-verification`](skills/gcloud-auth-verification/SKILL.md) | Guidelines for identifying and resolving missing Google Cloud authentication and Application Default Credentials (ADC). Use this skill if `gcloud`, `bq`, `dataform`, or Python l... |
| [`gcp-cloud-run`](skills/gcp-cloud-run/SKILL.md) | When to use: ['Web applications and APIs', 'Need any runtime or library', 'Complex services with multiple endpoints', 'Stateless containerized workloads'] |
| [`gcp-composer-troubleshooting`](skills/gcp-composer-troubleshooting/SKILL.md) | Provides expert guidance for troubleshooting Cloud Composer (Apache Airflow) and Orchestration pipelines. Use this skill when the user asks to generate Root Cause Analysis (RCA)... |
| [`gcp-data-pipelines`](skills/gcp-data-pipelines/SKILL.md) | Primary entry point for building, managing, and orchestrating data pipelines on Google Cloud. Guides users to the appropriate skill for dbt, Dataflow (Apache Beam), Dataform, Sp... |
| [`gcp-dataflow`](skills/gcp-dataflow/SKILL.md) | \| Guides writing, packaging, executing, and troubleshooting Apache Beam pipelines on Dataflow. Use when creating new pipelines, configuring Flex Templates, or analyzing perform... |
| [`gcp-managed-airflow-migrations`](skills/gcp-managed-airflow-migrations/SKILL.md) | Provides guidance for migrating Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers migration to Airflow 2.11.1 (MSAA Gen 2 and 3) ... |
| [`gcp-pipeline-orchestration`](skills/gcp-pipeline-orchestration/SKILL.md) | This skill helps the agent generate or update orchestration pipeline definitions for Google Cloud Composer to initialize orchestration pipeline or update the orchestration defin... |
| [`gcp-pipeline-resource-provisioning`](skills/gcp-pipeline-resource-provisioning/SKILL.md) | \| Automates declarative resource creation and provisioning for data pipelines, supporting BigQuery, Dataform, Dataproc, BigQuery Data Transfer Service (DTS), and other resource... |
| [`gcp-spark`](skills/gcp-spark/SKILL.md) | \| Develops and executes Spark code on Dataproc Clusters and Serverless. Reads and writes data using BigLake Iceberg catalogs, BigQuery and Spanner. Debugs execution failures. U... |
| [`gcs-security-assessment`](skills/gcs-security-assessment/SKILL.md) | Assesses security posture, evaluates risks, and checks SAIF compliance for Google Cloud Storage buckets or projects. Use when the user requests security scans, vulnerability che... |
| [`gdb-cli`](skills/gdb-cli/SKILL.md) | GDB debugging assistant for AI agents - analyze core dumps, debug live processes, investigate crashes and deadlocks with source code correlation |
| [`gdpr-data-handling`](skills/gdpr-data-handling/SKILL.md) | Practical implementation guide for GDPR-compliant data processing, consent management, and privacy controls. |
| [`gemini-api-dev`](skills/gemini-api-dev/SKILL.md) | The Gemini API provides access to Google's most advanced AI models. Key capabilities include: |
| [`gemini-api-integration`](skills/gemini-api-integration/SKILL.md) | Use when integrating Google Gemini API into projects. Covers model selection, multimodal inputs, streaming, function calling, and production best practices. |
| [`geo-fundamentals`](skills/geo-fundamentals/SKILL.md) | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). |
| [`geoffrey-hinton`](skills/geoffrey-hinton/SKILL.md) | Agente que simula Geoffrey Hinton — Godfather of Deep Learning, Prêmio Turing 2018, criador do backpropagation e das Deep Belief Networks. |
| [`get-shit-done`](skills/get-shit-done/SKILL.md) | A meta-prompting, context engineering and spec-driven development system for Gemini CLI. Provides advanced workflows for planning, execution, and verification of complex tasks. |
| [`gh-review-requests`](skills/gh-review-requests/SKILL.md) | Fetch unread GitHub notifications for open PRs where review is requested from a specified team or opened by a team member. Use when asked to "find PRs I need to review", "show m... |
| [`gha-security-review`](skills/gha-security-review/SKILL.md) | Find exploitable vulnerabilities in GitHub Actions workflows. Every finding MUST include a concrete exploitation scenario — if you can't build the attack, don't report it. |
| [`git-advanced-workflows`](skills/git-advanced-workflows/SKILL.md) | Master advanced Git techniques to maintain clean history, collaborate effectively, and recover from any situation with confidence. |
| [`git-hooks-automation`](skills/git-hooks-automation/SKILL.md) | Master Git hooks setup with Husky, lint-staged, pre-commit framework, and commitlint. Automate code quality gates, formatting, linting, and commit message enforcement before cod... |
| [`git-pr-workflows-git-workflow`](skills/git-pr-workflows-git-workflow/SKILL.md) | Orchestrate a comprehensive git workflow from code review through PR creation, leveraging specialized agents for quality assurance, testing, and deployment readiness. This workf... |
| [`git-pr-workflows-onboard`](skills/git-pr-workflows-onboard/SKILL.md) | You are an **expert onboarding specialist and knowledge transfer architect** with deep experience in remote-first organizations, technical team integration, and accelerated lear... |
| [`git-pr-workflows-pr-enhance`](skills/git-pr-workflows-pr-enhance/SKILL.md) | You are a PR optimization expert specializing in creating high-quality pull requests that facilitate efficient code reviews. Generate comprehensive PR descriptions, automate rev... |
| [`git-pushing`](skills/git-pushing/SKILL.md) | Stage all changes, create a conventional commit, and push to the remote branch. Use when explicitly asks to push changes (\"push this\", \"commit and push\"), mentions saving wo... |
| [`github`](skills/github/SKILL.md) | Use the `gh` CLI for issues, pull requests, Actions runs, and GitHub API queries. |
| [`github-actions-templates`](skills/github-actions-templates/SKILL.md) | Production-ready GitHub Actions workflow patterns for testing, building, and deploying applications. |
| [`github-automation`](skills/github-automation/SKILL.md) | Automate GitHub repositories, issues, pull requests, branches, CI/CD, and permissions via Rube MCP (Composio). Manage code workflows, review PRs, search code, and handle deploym... |
| [`github-issue-creator`](skills/github-issue-creator/SKILL.md) | Turn error logs, screenshots, voice notes, and rough bug reports into crisp, developer-ready GitHub issues with repro steps, impact, and evidence. |
| [`github-workflow-automation`](skills/github-workflow-automation/SKILL.md) | Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices. |
| [`gitlab-automation`](skills/gitlab-automation/SKILL.md) | Automate GitLab project management, issues, merge requests, pipelines, branches, and user operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`gitlab-ci-patterns`](skills/gitlab-ci-patterns/SKILL.md) | Comprehensive GitLab CI/CD pipeline patterns for automated testing, building, and deployment. |
| [`gitops-workflow`](skills/gitops-workflow/SKILL.md) | Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments. |
| [`gmail-automation`](skills/gmail-automation/SKILL.md) | Lightweight Gmail integration with standalone OAuth authentication. No MCP server required. |
| [`go-concurrency-patterns`](skills/go-concurrency-patterns/SKILL.md) | Master Go concurrency with goroutines, channels, sync primitives, and context. Use when building concurrent Go applications, implementing worker pools, or debugging race conditi... |
| [`go-playwright`](skills/go-playwright/SKILL.md) | Expert capability for robust, stealthy, and efficient browser automation using Playwright Go. |
| [`go-rod-master`](skills/go-rod-master/SKILL.md) | Comprehensive guide for browser automation and web scraping with go-rod (Chrome DevTools Protocol) including stealth anti-bot-detection patterns. |
| [`goal-analyzer`](skills/goal-analyzer/SKILL.md) | 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| [`godot-4-migration`](skills/godot-4-migration/SKILL.md) | Specialized guide for migrating Godot 3.x projects to Godot 4 (GDScript 2.0), covering syntax changes, Tweens, and exports. |
| [`godot-gdscript-patterns`](skills/godot-gdscript-patterns/SKILL.md) | Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. Use when building Godot games, implementing game systems, or learning GDScript best... |
| [`golang-pro`](skills/golang-pro/SKILL.md) | Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices. |
| [`google-analytics-automation`](skills/google-analytics-automation/SKILL.md) | Automate Google Analytics tasks via Rube MCP (Composio): run reports, list accounts/properties, funnels, pivots, key events. Always search tools first for current schemas. |
| [`google-calendar-automation`](skills/google-calendar-automation/SKILL.md) | Lightweight Google Calendar integration with standalone OAuth authentication. No MCP server required. |
| [`google-docs-automation`](skills/google-docs-automation/SKILL.md) | Lightweight Google Docs integration with standalone OAuth authentication. No MCP server required. |
| [`google-drive-automation`](skills/google-drive-automation/SKILL.md) | Lightweight Google Drive integration with standalone OAuth authentication. No MCP server required. Full read/write access. |
| [`google-sheets-automation`](skills/google-sheets-automation/SKILL.md) | Lightweight Google Sheets integration with standalone OAuth authentication. No MCP server required. Full read/write access. |
| [`google-slides-automation`](skills/google-slides-automation/SKILL.md) | Lightweight Google Slides integration with standalone OAuth authentication. No MCP server required. Full read/write access. |
| [`googlesheets-automation`](skills/googlesheets-automation/SKILL.md) | Automate Google Sheets operations (read, write, format, filter, manage spreadsheets) via Rube MCP (Composio). Read/write data, manage tabs, apply formatting, and search rows pro... |
| [`grafana-dashboards`](skills/grafana-dashboards/SKILL.md) | Create and manage production-ready Grafana dashboards for comprehensive system observability. |
| [`graphql`](skills/graphql/SKILL.md) | You're a developer who has built GraphQL APIs at scale. You've seen the N+1 query problem bring down production servers. You've watched clients craft deeply nested queries that ... |
| [`graphql-architect`](skills/graphql-architect/SKILL.md) | Master modern GraphQL with federation, performance optimization, and enterprise security. Build scalable schemas, implement advanced caching, and design real-time systems. |
| [`growth-engine`](skills/growth-engine/SKILL.md) | Motor de crescimento para produtos digitais -- growth hacking, SEO, ASO, viral loops, email marketing, CRM, referral programs e aquisicao organica. |
| [`grpc-golang`](skills/grpc-golang/SKILL.md) | Build production-ready gRPC services in Go with mTLS, streaming, and observability. Use when designing Protobuf contracts with Buf or implementing secure service-to-service tran... |
| [`gsd-add-tests`](skills/gsd-add-tests/SKILL.md) | Generate tests for a completed phase based on UAT criteria and implementation |
| [`gsd-ai-integration-phase`](skills/gsd-ai-integration-phase/SKILL.md) | Generate an AI-SPEC.md design contract for phases that involve building AI systems. |
| [`gsd-audit-fix`](skills/gsd-audit-fix/SKILL.md) | Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit |
| [`gsd-audit-milestone`](skills/gsd-audit-milestone/SKILL.md) | Audit milestone completion against original intent before archiving |
| [`gsd-audit-uat`](skills/gsd-audit-uat/SKILL.md) | Cross-phase audit of all outstanding UAT and verification items |
| [`gsd-autonomous`](skills/gsd-autonomous/SKILL.md) | Run all remaining phases autonomously — discuss→plan→execute per phase |
| [`gsd-capture`](skills/gsd-capture/SKILL.md) | Capture ideas, tasks, notes, and seeds to their destination |
| [`gsd-cleanup`](skills/gsd-cleanup/SKILL.md) | Archive accumulated phase directories from completed milestones |
| [`gsd-code-review`](skills/gsd-code-review/SKILL.md) | Review source files changed during a phase for bugs, security issues, and code quality problems |
| [`gsd-complete-milestone`](skills/gsd-complete-milestone/SKILL.md) | Archive completed milestone and prepare for next version |
| [`gsd-config`](skills/gsd-config/SKILL.md) | Configure GSD settings — workflow toggles, advanced knobs, integrations, and model profile |
| [`gsd-debug`](skills/gsd-debug/SKILL.md) | Systematic debugging with persistent state across context resets |
| [`gsd-discuss-phase`](skills/gsd-discuss-phase/SKILL.md) | Gather phase context through adaptive questioning before planning. |
| [`gsd-docs-update`](skills/gsd-docs-update/SKILL.md) | Generate or update project documentation verified against the codebase |
| [`gsd-eval-review`](skills/gsd-eval-review/SKILL.md) | Audit an executed AI phase's evaluation coverage and produce an EVAL-REVIEW.md remediation plan. |
| [`gsd-execute-phase`](skills/gsd-execute-phase/SKILL.md) | Execute all plans in a phase with wave-based parallelization |
| [`gsd-explore`](skills/gsd-explore/SKILL.md) | Socratic ideation and idea routing — think through ideas before committing to plans |
| [`gsd-extract-learnings`](skills/gsd-extract-learnings/SKILL.md) | Extract decisions, lessons, patterns, and surprises from completed phase artifacts |
| [`gsd-fast`](skills/gsd-fast/SKILL.md) | Execute a trivial task inline — no subagents, no planning overhead |
| [`gsd-forensics`](skills/gsd-forensics/SKILL.md) | Post-mortem investigation for failed GSD workflows — diagnoses what went wrong. |
| [`gsd-graphify`](skills/gsd-graphify/SKILL.md) | Build, query, and inspect the project knowledge graph in .planning/graphs/ |
| [`gsd-health`](skills/gsd-health/SKILL.md) | Diagnose planning directory health and optionally repair issues |
| [`gsd-help`](skills/gsd-help/SKILL.md) | Show available GSD commands and usage guide |
| [`gsd-import`](skills/gsd-import/SKILL.md) | Ingest external plans with conflict detection against project decisions before writing anything. |
| [`gsd-inbox`](skills/gsd-inbox/SKILL.md) | Triage and review open GitHub issues and PRs against project templates and contribution guidelines. |
| [`gsd-ingest-docs`](skills/gsd-ingest-docs/SKILL.md) | Bootstrap or merge a .planning/ setup from existing ADRs, PRDs, SPECs, and docs in a repo. |
| [`gsd-manager`](skills/gsd-manager/SKILL.md) | Interactive command center for managing multiple phases from one terminal |
| [`gsd-map-codebase`](skills/gsd-map-codebase/SKILL.md) | Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents |
| [`gsd-milestone-summary`](skills/gsd-milestone-summary/SKILL.md) | Generate a comprehensive project summary from milestone artifacts for team onboarding and review |
| [`gsd-mvp-phase`](skills/gsd-mvp-phase/SKILL.md) | Plan a phase as a vertical MVP slice — user story, SPIDR splitting, then plan-phase |
| [`gsd-new-milestone`](skills/gsd-new-milestone/SKILL.md) | Start a new milestone cycle — update PROJECT.md and route to requirements |
| [`gsd-new-project`](skills/gsd-new-project/SKILL.md) | Initialize a new project with deep context gathering and PROJECT.md |
| [`gsd-ns-context`](skills/gsd-ns-context/SKILL.md) | codebase intelligence \| map graphify docs learnings |
| [`gsd-ns-ideate`](skills/gsd-ns-ideate/SKILL.md) | exploration capture \| explore sketch spike spec capture |
| [`gsd-ns-manage`](skills/gsd-ns-manage/SKILL.md) | config workspace \| workstreams thread update ship inbox |
| [`gsd-ns-project`](skills/gsd-ns-project/SKILL.md) | project lifecycle \| milestones audits summary |
| [`gsd-ns-review`](skills/gsd-ns-review/SKILL.md) | quality gates \| code review debug audit security eval ui |
| [`gsd-ns-workflow`](skills/gsd-ns-workflow/SKILL.md) | workflow \| discuss plan execute verify phase progress |
| [`gsd-pause-work`](skills/gsd-pause-work/SKILL.md) | Create context handoff when pausing work mid-phase |
| [`gsd-phase`](skills/gsd-phase/SKILL.md) | CRUD for phases in ROADMAP.md — add, insert, remove, or edit phases |
| [`gsd-plan-phase`](skills/gsd-plan-phase/SKILL.md) | Create detailed phase plan (PLAN.md) with verification loop |
| [`gsd-plan-review-convergence`](skills/gsd-plan-review-convergence/SKILL.md) | Cross-AI plan convergence loop — replan with review feedback until no HIGH concerns remain. |
| [`gsd-pr-branch`](skills/gsd-pr-branch/SKILL.md) | Create a clean PR branch by filtering out .planning/ commits — ready for code review |
| [`gsd-profile-user`](skills/gsd-profile-user/SKILL.md) | Generate developer behavioral profile and create Claude-discoverable artifacts |
| [`gsd-progress`](skills/gsd-progress/SKILL.md) | Check progress, advance workflow, or dispatch freeform intent — the unified GSD situational command |
| [`gsd-quick`](skills/gsd-quick/SKILL.md) | Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents |
| [`gsd-resume-work`](skills/gsd-resume-work/SKILL.md) | Resume work from previous session with full context restoration |
| [`gsd-review`](skills/gsd-review/SKILL.md) | Request cross-AI peer review of phase plans from external AI CLIs |
| [`gsd-review-backlog`](skills/gsd-review-backlog/SKILL.md) | Review and promote backlog items to active milestone |
| [`gsd-secure-phase`](skills/gsd-secure-phase/SKILL.md) | Retroactively verify threat mitigations for a completed phase |
| [`gsd-settings`](skills/gsd-settings/SKILL.md) | Configure GSD workflow toggles and model profile |
| [`gsd-ship`](skills/gsd-ship/SKILL.md) | Create PR, run review, and prepare for merge after verification passes |
| [`gsd-sketch`](skills/gsd-sketch/SKILL.md) | Sketch UI/design ideas with throwaway HTML mockups, or propose what to sketch next (frontier mode) |
| [`gsd-spec-phase`](skills/gsd-spec-phase/SKILL.md) | Clarify WHAT a phase delivers with ambiguity scoring; produces a SPEC.md before discuss-phase. |
| [`gsd-spike`](skills/gsd-spike/SKILL.md) | Spike an idea through experiential exploration, or propose what to spike next (frontier mode) |
| [`gsd-stats`](skills/gsd-stats/SKILL.md) | Display project statistics — phases, plans, requirements, git metrics, and timeline |
| [`gsd-surface`](skills/gsd-surface/SKILL.md) | Toggle which skills are surfaced — apply a profile, list, or disable a cluster without reinstall |
| [`gsd-thread`](skills/gsd-thread/SKILL.md) | Manage persistent context threads for cross-session work |
| [`gsd-ui-phase`](skills/gsd-ui-phase/SKILL.md) | Generate UI design contract (UI-SPEC.md) for frontend phases |
| [`gsd-ui-review`](skills/gsd-ui-review/SKILL.md) | Retroactive 6-pillar visual audit of implemented frontend code |
| [`gsd-ultraplan-phase`](skills/gsd-ultraplan-phase/SKILL.md) | [BETA] Offload plan phase to Claude Code's ultraplan cloud; review in browser and import back. |
| [`gsd-undo`](skills/gsd-undo/SKILL.md) | Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks. |
| [`gsd-update`](skills/gsd-update/SKILL.md) | Update GSD to latest version with changelog display |
| [`gsd-validate-phase`](skills/gsd-validate-phase/SKILL.md) | Retroactively audit and fill Nyquist validation gaps for a completed phase |
| [`gsd-verify-work`](skills/gsd-verify-work/SKILL.md) | Validate built features through conversational UAT |
| [`gsd-workspace`](skills/gsd-workspace/SKILL.md) | Manage GSD workspaces — create, list, or remove isolated workspace environments |
| [`gsd-workstreams`](skills/gsd-workstreams/SKILL.md) | Manage parallel workstreams — list, create, switch, status, progress, complete, and resume |

<a id="indice-h"></a>
### Letra H (44 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`haskell-pro`](skills/haskell-pro/SKILL.md) | Expert Haskell engineer specializing in advanced type systems, pure |
| [`headline-psychologist`](skills/headline-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`health-trend-analyzer`](skills/health-trend-analyzer/SKILL.md) | 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体重/BMI、症状、药物依从性、化验结果、情绪睡眠），相关性分析，变化检测，以及交互式HTML可视化报告（EChart... |
| [`helm-chart-scaffolding`](skills/helm-chart-scaffolding/SKILL.md) | Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications. |
| [`helpdesk-automation`](skills/helpdesk-automation/SKILL.md) | Automate HelpDesk tasks via Rube MCP (Composio): list tickets, manage views, use canned responses, and configure custom fields. Always search tools first for current schemas. |
| [`hierarchical-agent-memory`](skills/hierarchical-agent-memory/SKILL.md) | Scoped CLAUDE.md memory system that reduces context token spend. Creates directory-level context files, tracks savings via dashboard, and routes agents to the right sub-context. |
| [`hig-components-content`](skills/hig-components-content/SKILL.md) | Apple Human Interface Guidelines for content display components. |
| [`hig-components-controls`](skills/hig-components-controls/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| [`hig-components-dialogs`](skills/hig-components-dialogs/SKILL.md) | Apple HIG guidance for presentation components including alerts, action sheets, popovers, sheets, and digit entry views. |
| [`hig-components-layout`](skills/hig-components-layout/SKILL.md) | Apple Human Interface Guidelines for layout and navigation components. |
| [`hig-components-menus`](skills/hig-components-menus/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| [`hig-components-search`](skills/hig-components-search/SKILL.md) | Apple HIG guidance for navigation-related components including search fields, page controls, and path controls. |
| [`hig-components-status`](skills/hig-components-status/SKILL.md) | Apple HIG guidance for status and progress UI components including progress indicators, status bars, and activity rings. |
| [`hig-components-system`](skills/hig-components-system/SKILL.md) | Apple HIG guidance for system experience components: widgets, live activities, notifications, complications, home screen quick actions, top shelf, watch faces, app clips, and ap... |
| [`hig-foundations`](skills/hig-foundations/SKILL.md) | Apple Human Interface Guidelines design foundations. |
| [`hig-inputs`](skills/hig-inputs/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| [`hig-patterns`](skills/hig-patterns/SKILL.md) | Apple Human Interface Guidelines interaction and UX patterns. |
| [`hig-platforms`](skills/hig-platforms/SKILL.md) | Apple Human Interface Guidelines for platform-specific design. |
| [`hig-project-context`](skills/hig-project-context/SKILL.md) | Create or update a shared Apple design context document that other HIG skills use to tailor guidance. |
| [`hig-technologies`](skills/hig-technologies/SKILL.md) | Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered. |
| [`hono`](skills/hono/SKILL.md) | Build ultra-fast web APIs and full-stack apps with Hono — runs on Cloudflare Workers, Deno, Bun, Node.js, and any WinterCG-compatible runtime. |
| [`hosted-agents`](skills/hosted-agents/SKILL.md) | Build background agents in sandboxed environments. Use for hosted coding agents, sandboxed VMs, Modal sandboxes, and remote coding environments. |
| [`hosted-agents-v2-py`](skills/hosted-agents-v2-py/SKILL.md) | Build hosted agents using Azure AI Projects SDK with ImageBasedHostedAgentDefinition. Use when creating container-based agents in Azure AI Foundry. |
| [`hr-pro`](skills/hr-pro/SKILL.md) | Professional, ethical HR partner for hiring, onboarding/offboarding, PTO and leave, performance, compliant policies, and employee relations. |
| [`html-injection-testing`](skills/html-injection-testing/SKILL.md) | Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. This vulnerability enables attackers to modify p... |
| [`hubspot-automation`](skills/hubspot-automation/SKILL.md) | Automate HubSpot CRM operations (contacts, companies, deals, tickets, properties) via Rube MCP using Composio integration. |
| [`hubspot-integration`](skills/hubspot-integration/SKILL.md) | Authentication for single-account integrations |
| [`hugging-face-cli`](skills/hugging-face-cli/SKILL.md) | Use the Hugging Face Hub CLI (`hf`) to download, upload, and manage models, datasets, and Spaces. |
| [`hugging-face-community-evals`](skills/hugging-face-community-evals/SKILL.md) | Run local evaluations for Hugging Face Hub models with inspect-ai or lighteval. |
| [`hugging-face-dataset-viewer`](skills/hugging-face-dataset-viewer/SKILL.md) | Query Hugging Face datasets through the Dataset Viewer API for splits, rows, search, filters, and parquet links. |
| [`hugging-face-datasets`](skills/hugging-face-datasets/SKILL.md) | Create and manage datasets on Hugging Face Hub. Supports initializing repos, defining configs/system prompts, streaming row updates, and SQL-based dataset querying/transformatio... |
| [`hugging-face-evaluation`](skills/hugging-face-evaluation/SKILL.md) | Add and manage evaluation results in Hugging Face model cards. Supports extracting eval tables from README content, importing scores from Artificial Analysis API, and running cu... |
| [`hugging-face-gradio`](skills/hugging-face-gradio/SKILL.md) | Build or edit Gradio apps, layouts, components, and chat interfaces in Python. |
| [`hugging-face-jobs`](skills/hugging-face-jobs/SKILL.md) | Run workloads on Hugging Face Jobs with managed CPUs, GPUs, TPUs, secrets, and Hub persistence. |
| [`hugging-face-model-trainer`](skills/hugging-face-model-trainer/SKILL.md) | Train or fine-tune TRL language models on Hugging Face Jobs, including SFT, DPO, GRPO, and GGUF export. |
| [`hugging-face-paper-publisher`](skills/hugging-face-paper-publisher/SKILL.md) | Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to models/datasets, claiming authorship, and generating professional markdo... |
| [`hugging-face-papers`](skills/hugging-face-papers/SKILL.md) | Read and analyze Hugging Face paper pages or arXiv papers with markdown and papers API metadata. |
| [`hugging-face-tool-builder`](skills/hugging-face-tool-builder/SKILL.md) | Your purpose is now is to create reusable command line scripts and utilities for using the Hugging Face API, allowing chaining, piping and intermediate processing where helpful.... |
| [`hugging-face-trackio`](skills/hugging-face-trackio/SKILL.md) | Track ML experiments with Trackio using Python logging, alerts, and CLI metric retrieval. |
| [`hugging-face-vision-trainer`](skills/hugging-face-vision-trainer/SKILL.md) | Train or fine-tune vision models on Hugging Face Jobs for detection, classification, and SAM or SAM2 segmentation. |
| [`humanize-chinese`](skills/humanize-chinese/SKILL.md) | Detect and rewrite AI-like Chinese text with a practical workflow for scoring, humanization, academic AIGC reduction, and style conversion. Use when the user asks to 去AI味, 降AIGC... |
| [`hybrid-cloud-architect`](skills/hybrid-cloud-architect/SKILL.md) | Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware). |
| [`hybrid-cloud-networking`](skills/hybrid-cloud-networking/SKILL.md) | Configure secure, high-performance connectivity between on-premises and cloud environments using VPN, Direct Connect, and ExpressRoute. |
| [`hybrid-search-implementation`](skills/hybrid-search-implementation/SKILL.md) | Combine vector and keyword search for improved retrieval. Use when implementing RAG systems, building search engines, or when neither approach alone provides sufficient recall. |

<a id="indice-i"></a>
### Letra I (27 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`i18n-localization`](skills/i18n-localization/SKILL.md) | Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support. |
| [`iconsax-library`](skills/iconsax-library/SKILL.md) | Extensive icon library and AI-driven icon generation skill for premium UI/UX design. |
| [`identity-mirror`](skills/identity-mirror/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`idor-testing`](skills/idor-testing/SKILL.md) | Provide systematic methodologies for identifying and exploiting Insecure Direct Object Reference (IDOR) vulnerabilities in web applications. |
| [`ilya-sutskever`](skills/ilya-sutskever/SKILL.md) | Agente que simula Ilya Sutskever — co-fundador da OpenAI, ex-Chief Scientist, fundador da SSI. Use quando quiser perspectivas sobre: AGI safety-first, consciência de IA, scaling... |
| [`image-studio`](skills/image-studio/SKILL.md) | Studio de geracao de imagens inteligente — roteamento automatico entre ai-studio-image (fotos humanizadas/influencer) e stability-ai (arte/ ilustracao/edicao). Detecta o tipo de... |
| [`imagen`](skills/imagen/SKILL.md) | AI image generation skill powered by Google Gemini, enabling seamless visual content creation for UI placeholders, documentation, and design assets. |
| [`incident-responder`](skills/incident-responder/SKILL.md) | Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management. |
| [`incident-response-incident-response`](skills/incident-response-incident-response/SKILL.md) | Use when working with incident response incident response |
| [`incident-response-smart-fix`](skills/incident-response-smart-fix/SKILL.md) | [Extended thinking: This workflow implements a sophisticated debugging and resolution pipeline that leverages AI-assisted debugging tools and observability platforms to systemat... |
| [`incident-runbook-templates`](skills/incident-runbook-templates/SKILL.md) | Production-ready templates for incident response runbooks covering detection, triage, mitigation, resolution, and communication. |
| [`infinite-gratitude`](skills/infinite-gratitude/SKILL.md) | Multi-agent research skill for parallel research execution (10 agents, battle-tested with real case studies). |
| [`inngest`](skills/inngest/SKILL.md) | You are an Inngest expert who builds reliable background processing without managing infrastructure. You understand that serverless doesn't mean you can't have durable, long-run... |
| [`instagram`](skills/instagram/SKILL.md) | Integracao completa com Instagram via Graph API. Publicacao, analytics, comentarios, DMs, hashtags, agendamento, templates e gestao de contas Business/Creator. |
| [`instagram-automation`](skills/instagram-automation/SKILL.md) | Automate Instagram tasks via Rube MCP (Composio): create posts, carousels, manage media, get insights, and publishing limits. Always search tools first for current schemas. |
| [`interactive-portfolio`](skills/interactive-portfolio/SKILL.md) | You know a portfolio isn't a resume - it's a first impression that needs to convert. You balance creativity with usability. You understand that hiring managers spend 30 seconds ... |
| [`intercom-automation`](skills/intercom-automation/SKILL.md) | Automate Intercom tasks via Rube MCP (Composio): conversations, contacts, companies, segments, admins. Always search tools first for current schemas. |
| [`internal-comms`](skills/internal-comms/SKILL.md) | Write internal communications such as status reports, leadership updates, 3P updates, newsletters, FAQs, incident reports, and project updates using repeatable internal formats. |
| [`internal-comms-anthropic`](skills/internal-comms-anthropic/SKILL.md) | To write internal communications, use this skill for: |
| [`internal-comms-community`](skills/internal-comms-community/SKILL.md) | To write internal communications, use this skill for: |
| [`interview-coach`](skills/interview-coach/SKILL.md) | Full job search coaching system — JD decoding, resume, storybank, mock interviews, transcript analysis, comp negotiation. 23 commands, persistent state. |
| [`inventory-demand-planning`](skills/inventory-demand-planning/SKILL.md) | Codified expertise for demand forecasting, safety stock optimisation, replenishment planning, and promotional lift estimation at multi-location retailers. |
| [`ios-debugger-agent`](skills/ios-debugger-agent/SKILL.md) | Debug the current iOS project on a booted simulator with XcodeBuildMCP. |
| [`ios-developer`](skills/ios-developer/SKILL.md) | Develop native iOS applications with Swift/SwiftUI. Masters iOS 18, SwiftUI, UIKit integration, Core Data, networking, and App Store optimization. |
| [`issues`](skills/issues/SKILL.md) | Interact with GitHub issues - create, list, and view issues. |
| [`istio-traffic-management`](skills/istio-traffic-management/SKILL.md) | Comprehensive guide to Istio traffic management for production service mesh deployments. |
| [`iterate-pr`](skills/iterate-pr/SKILL.md) | Iterate on a PR until CI passes. Use when you need to fix CI failures, address review feedback, or continuously push fixes until all checks are green. Automates the feedback-fix... |

<a id="indice-j"></a>
### Letra J (12 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`java-pro`](skills/java-pro/SKILL.md) | Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. Expert in the latest Java ecosystem including GraalVM, Project Loom, and cloud-... |
| [`javascript-mastery`](skills/javascript-mastery/SKILL.md) | 33+ essential JavaScript concepts every developer should know, inspired by [33-js-concepts](https://github.com/leonardomso/33-js-concepts). |
| [`javascript-pro`](skills/javascript-pro/SKILL.md) | Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility. |
| [`javascript-testing-patterns`](skills/javascript-testing-patterns/SKILL.md) | Comprehensive guide for implementing robust testing strategies in JavaScript/TypeScript applications using modern testing frameworks and best practices. |
| [`javascript-typescript-typescript-scaffold`](skills/javascript-typescript-typescript-scaffold/SKILL.md) | You are a TypeScript project architecture expert specializing in scaffolding production-ready Node.js and frontend applications. Generate complete project structures with modern... |
| [`jira-automation`](skills/jira-automation/SKILL.md) | Automate Jira tasks via Rube MCP (Composio): issues, projects, sprints, boards, comments, users. Always search tools first for current schemas. |
| [`jobgpt`](skills/jobgpt/SKILL.md) | Job search automation, auto apply, resume generation, application tracking, salary intelligence, and recruiter outreach using the JobGPT MCP server. |
| [`jobs-to-be-done-analyst`](skills/jobs-to-be-done-analyst/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`jq`](skills/jq/SKILL.md) | Expert jq usage for JSON querying, filtering, transformation, and pipeline integration. Practical patterns for real shell workflows. |
| [`json-canvas`](skills/json-canvas/SKILL.md) | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files, creating visual canvases, mind maps, flowcharts, or ... |
| [`julia-pro`](skills/julia-pro/SKILL.md) | Master Julia 1.10+ with modern features, performance optimization, multiple dispatch, and production-ready practices. |
| [`junta-leiloeiros`](skills/junta-leiloeiros/SKILL.md) | Coleta e consulta dados de leiloeiros oficiais de todas as 27 Juntas Comerciais do Brasil. Scraper multi-UF, banco SQLite, API FastAPI e exportacao CSV/JSON. |

<a id="indice-k"></a>
### Letra K (10 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`k6-load-testing`](skills/k6-load-testing/SKILL.md) | Comprehensive k6 load testing skill for API, browser, and scalability testing. Write realistic load scenarios, analyze results, and integrate with CI/CD. |
| [`k8s-manifest-generator`](skills/k8s-manifest-generator/SKILL.md) | Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims. |
| [`k8s-security-policies`](skills/k8s-security-policies/SKILL.md) | Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes. |
| [`kaizen`](skills/kaizen/SKILL.md) | Guide for continuous improvement, error proofing, and standardization. Use this skill when the user wants to improve code quality, refactor, or discuss process improvements. |
| [`keyword-extractor`](skills/keyword-extractor/SKILL.md) | > Extracts up to 50 highly relevant SEO keywords from text. Use when user wants to generate or extract keywords for given text. |
| [`klaviyo-automation`](skills/klaviyo-automation/SKILL.md) | Automate Klaviyo tasks via Rube MCP (Composio): manage email/SMS campaigns, inspect campaign messages, track tags, and monitor send jobs. Always search tools first for current s... |
| [`kotlin-coroutines-expert`](skills/kotlin-coroutines-expert/SKILL.md) | Expert patterns for Kotlin Coroutines and Flow, covering structured concurrency, error handling, and testing. |
| [`kpi-dashboard-design`](skills/kpi-dashboard-design/SKILL.md) | Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions. |
| [`kubernetes-architect`](skills/kubernetes-architect/SKILL.md) | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise container orchestration. |
| [`kubernetes-deployment`](skills/kubernetes-deployment/SKILL.md) | Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations. |

<a id="indice-l"></a>
### Letra L (45 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`landing-page-generator`](skills/landing-page-generator/SKILL.md) | Generates high-converting Next.js/React landing pages with Tailwind CSS. Uses PAS, AIDA, and BAB frameworks for optimized copy/components (Heroes, Features, Pricing). Focuses on... |
| [`langchain-architecture`](skills/langchain-architecture/SKILL.md) | Master the LangChain framework for building sophisticated LLM applications with agents, chains, memory, and tool integration. |
| [`langfuse`](skills/langfuse/SKILL.md) | You are an expert in LLM observability and evaluation. You think in terms of traces, spans, and metrics. You know that LLM applications need monitoring just like traditional sof... |
| [`langgraph`](skills/langgraph/SKILL.md) | You are an expert in building production-grade AI agents with LangGraph. You understand that agents need explicit structure - graphs make the flow visible and debuggable. You de... |
| [`laravel-expert`](skills/laravel-expert/SKILL.md) | Senior Laravel Engineer role for production-grade, maintainable, and idiomatic Laravel solutions. Focuses on clean architecture, security, performance, and modern standards (Lar... |
| [`laravel-security-audit`](skills/laravel-security-audit/SKILL.md) | Security auditor for Laravel applications. Analyzes code for vulnerabilities, misconfigurations, and insecure practices using OWASP standards and Laravel security best practices. |
| [`last30days`](skills/last30days/SKILL.md) | Research a topic from the last 30 days on Reddit + X + Web, become an expert, and write copy-paste-ready prompts for the user's target tool. |
| [`latex-paper-conversion`](skills/latex-paper-conversion/SKILL.md) | This skill should be used when the user asks to convert an academic paper in LaTeX from one format (e.g., Springer, IPOL) to another format (e.g., MDPI, IEEE, Nature). It automa... |
| [`launch-strategy`](skills/launch-strategy/SKILL.md) | You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capture attention, and convert interest into ... |
| [`lead-magnets`](skills/lead-magnets/SKILL.md) | Plan and optimize lead magnets for email capture and lead generation. Use when designing gated content, checklists, templates, downloadable resources, or other offers that conve... |
| [`legacy-modernizer`](skills/legacy-modernizer/SKILL.md) | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, and backward compatibility. |
| [`legal-advisor`](skills/legal-advisor/SKILL.md) | Draft privacy policies, terms of service, disclaimers, and legal notices. Creates GDPR-compliant texts, cookie policies, and data processing agreements. |
| [`leiloeiro-avaliacao`](skills/leiloeiro-avaliacao/SKILL.md) | Avaliacao pericial de imoveis em leilao. Valor de mercado, liquidacao forcada, ABNT NBR 14653, metodos comparativo/renda/custo, CUB e margem de seguranca. |
| [`leiloeiro-edital`](skills/leiloeiro-edital/SKILL.md) | Analise e auditoria de editais de leilao judicial e extrajudicial. Riscos ocultos, clausulas perigosas, debitos, ocupante e classificacao da oportunidade. |
| [`leiloeiro-ia`](skills/leiloeiro-ia/SKILL.md) | Especialista em leiloes judiciais e extrajudiciais de imoveis. Analise juridica, pericial e de mercado integrada. Orquestra os 5 modulos especializados. |
| [`leiloeiro-juridico`](skills/leiloeiro-juridico/SKILL.md) | Analise juridica de leiloes: nulidades, bem de familia, alienacao fiduciaria, CPC arts 829-903, Lei 9514/97, onus reais, embargos e jurisprudencia. |
| [`leiloeiro-mercado`](skills/leiloeiro-mercado/SKILL.md) | Analise de mercado imobiliario para leiloes. Liquidez, desagio tipico, ROI, estrategias de saida (flip/reforma/renda), Selic 2025 e benchmark CDI/FII. |
| [`leiloeiro-risco`](skills/leiloeiro-risco/SKILL.md) | Analise de risco em leiloes de imoveis. Score 36 pontos, riscos juridicos/financeiros/operacionais, stress test 4 cenarios e ROI ponderado por risco. |
| [`lex`](skills/lex/SKILL.md) | Centralized 'Truth Engine' for cross-jurisdictional legal context (US, EU, CA) and contract scaffolding. |
| [`libreoffice`](skills/libreoffice/SKILL.md) | Instruções e utilitários especializados para libreoffice. |
| [`lightning-architecture-review`](skills/lightning-architecture-review/SKILL.md) | Review Bitcoin Lightning Network protocol designs, compare channel factory approaches, and analyze Layer 2 scaling tradeoffs. Covers trust models, on-chain footprint, consensus ... |
| [`lightning-channel-factories`](skills/lightning-channel-factories/SKILL.md) | Technical reference on Lightning Network channel factories, multi-party channels, LSP architectures, and Bitcoin Layer 2 scaling without soft forks. Covers Decker-Wattenhofer, t... |
| [`lightning-factory-explainer`](skills/lightning-factory-explainer/SKILL.md) | Explain Bitcoin Lightning channel factories and the SuperScalar protocol — scalable Lightning onboarding using shared UTXOs, Decker-Wattenhofer trees, timeout-signature trees, M... |
| [`linear-automation`](skills/linear-automation/SKILL.md) | Automate Linear tasks via Rube MCP (Composio): issues, projects, cycles, teams, labels. Always search tools first for current schemas. |
| [`linear-claude-skill`](skills/linear-claude-skill/SKILL.md) | Manage Linear issues, projects, and teams |
| [`linkedin-automation`](skills/linkedin-automation/SKILL.md) | Automate LinkedIn tasks via Rube MCP (Composio): create posts, manage profile, company info, comments, and image uploads. Always search tools first for current schemas. |
| [`linkedin-cli`](skills/linkedin-cli/SKILL.md) | Use when automating LinkedIn via CLI: fetch profiles, search people/companies, send messages, manage connections, create posts, and Sales Navigator. |
| [`linkerd-patterns`](skills/linkerd-patterns/SKILL.md) | Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes. |
| [`lint-and-validate`](skills/lint-and-validate/SKILL.md) | MANDATORY: Run appropriate validation tools after EVERY code change. Do not finish a task until the code is error-free. |
| [`linux-privilege-escalation`](skills/linux-privilege-escalation/SKILL.md) | Execute systematic privilege escalation assessments on Linux systems to identify and exploit misconfigurations, vulnerable services, and security weaknesses that allow elevation... |
| [`linux-shell-scripting`](skills/linux-shell-scripting/SKILL.md) | Provide production-ready shell script templates for common Linux system administration tasks including backups, monitoring, user management, log analysis, and automation. These ... |
| [`linux-troubleshooting`](skills/linux-troubleshooting/SKILL.md) | Linux system troubleshooting workflow for diagnosing and resolving system issues, performance problems, and service failures. |
| [`llm-app-patterns`](skills/llm-app-patterns/SKILL.md) | Production-ready patterns for building LLM applications, inspired by [Dify](https://github.com/langgenius/dify) and industry best practices. |
| [`llm-application-dev-ai-assistant`](skills/llm-application-dev-ai-assistant/SKILL.md) | You are an AI assistant development expert specializing in creating intelligent conversational interfaces, chatbots, and AI-powered applications. Design comprehensive AI assista... |
| [`llm-application-dev-langchain-agent`](skills/llm-application-dev-langchain-agent/SKILL.md) | You are an expert LangChain agent developer specializing in production-grade AI systems using LangChain 0.1+ and LangGraph. |
| [`llm-application-dev-prompt-optimize`](skills/llm-application-dev-prompt-optimize/SKILL.md) | You are an expert prompt engineer specializing in crafting effective prompts for LLMs through advanced techniques including constitutional AI, chain-of-thought reasoning, and mo... |
| [`llm-evaluation`](skills/llm-evaluation/SKILL.md) | Master comprehensive evaluation strategies for LLM applications, from automated metrics to human evaluation and A/B testing. |
| [`llm-ops`](skills/llm-ops/SKILL.md) | LLM Operations -- RAG, embeddings, vector databases, fine-tuning, prompt engineering avancado, custos de LLM, evals de qualidade e arquiteturas de IA para producao. |
| [`llm-prompt-optimizer`](skills/llm-prompt-optimizer/SKILL.md) | Use when improving prompts for any LLM. Applies proven prompt engineering techniques to boost output quality, reduce hallucinations, and cut token usage. |
| [`llm-structured-output`](skills/llm-structured-output/SKILL.md) | > Get reliable JSON, enums, and typed objects from LLMs using response_format, tool_use, and schema-constrained decoding across OpenAI, Anthropic, and Google APIs. |
| [`local-legal-seo-audit`](skills/local-legal-seo-audit/SKILL.md) | Audit and improve local SEO for law firms, attorneys, forensic experts and legal/professional services sites with local presence, focusing on GBP, directories, E-E-A-T and pract... |
| [`local-llm-expert`](skills/local-llm-expert/SKILL.md) | Master local LLM inference, model selection, VRAM optimization, and local deployment using Ollama, llama.cpp, vLLM, and LM Studio. Expert in quantization formats (GGUF, EXL2) an... |
| [`logistics-exception-management`](skills/logistics-exception-management/SKILL.md) | Codified expertise for handling freight exceptions, shipment delays, damages, losses, and carrier disputes. Informed by logistics professionals with 15+ years operational experi... |
| [`loki-mode`](skills/loki-mode/SKILL.md) | Version 2.35.0 \| PRD to Production \| Zero Human Intervention > Research-enhanced: OpenAI SDK, DeepMind, Anthropic, AWS Bedrock, Agent SDK, HN Production (2025) |
| [`loss-aversion-designer`](skills/loss-aversion-designer/SKILL.md) | One sentence - what this skill does and when to invoke it |

<a id="indice-m"></a>
### Letra M (70 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`m365-agents-dotnet`](skills/m365-agents-dotnet/SKILL.md) | Microsoft 365 Agents SDK for .NET. Build multichannel agents for Teams/M365/Copilot Studio with ASP.NET Core hosting, AgentApplication routing, and MSAL-based auth. |
| [`m365-agents-py`](skills/m365-agents-py/SKILL.md) | Microsoft 365 Agents SDK for Python. Build multichannel agents for Teams/M365/Copilot Studio with aiohttp hosting, AgentApplication routing, streaming responses, and MSAL-based ... |
| [`m365-agents-ts`](skills/m365-agents-ts/SKILL.md) | Microsoft 365 Agents SDK for TypeScript/Node.js. |
| [`machine-learning-ops-ml-pipeline`](skills/machine-learning-ops-ml-pipeline/SKILL.md) | Design and implement a complete ML pipeline for: $ARGUMENTS |
| [`macos-menubar-tuist-app`](skills/macos-menubar-tuist-app/SKILL.md) | Build, refactor, or review SwiftUI macOS menubar apps that use Tuist. |
| [`macos-spm-app-packaging`](skills/macos-spm-app-packaging/SKILL.md) | Scaffold, build, sign, and package SwiftPM macOS apps without Xcode projects. |
| [`magic-animator`](skills/magic-animator/SKILL.md) | AI-powered animation tool for creating motion in logos, UI, icons, and social media assets. |
| [`magic-ui-generator`](skills/magic-ui-generator/SKILL.md) | Utilizes Magic by 21st.dev to generate, compare, and integrate multiple production-ready UI component variations. |
| [`mailchimp-automation`](skills/mailchimp-automation/SKILL.md) | Automate Mailchimp email marketing including campaigns, audiences, subscribers, segments, and analytics via Rube MCP (Composio). Always search tools first for current schemas. |
| [`make-automation`](skills/make-automation/SKILL.md) | Automate Make (Integromat) tasks via Rube MCP (Composio): operations, enums, language and timezone lookups. Always search tools first for current schemas. |
| [`makepad-animation`](skills/makepad-animation/SKILL.md) | \| CRITICAL: Use for Makepad animation system. Triggers on: makepad animation, makepad animator, makepad hover, makepad state, makepad transition, "from: { all: Forward", makepa... |
| [`makepad-basics`](skills/makepad-basics/SKILL.md) | \| CRITICAL: Use for Makepad getting started and app structure. Triggers on: makepad, makepad getting started, makepad tutorial, live_design!, app_main!, makepad project setup, ... |
| [`makepad-deployment`](skills/makepad-deployment/SKILL.md) | \| CRITICAL: Use for Makepad packaging and deployment. Triggers on: deploy, package, APK, IPA, 打包, 部署, cargo-packager, cargo-makepad, WASM, Android, iOS, distribution, installer... |
| [`makepad-dsl`](skills/makepad-dsl/SKILL.md) | \| CRITICAL: Use for Makepad DSL syntax and inheritance. Triggers on: makepad dsl, live_design, makepad inheritance, makepad prototype, "<Widget>", "Foo = { }", makepad object, ... |
| [`makepad-event-action`](skills/makepad-event-action/SKILL.md) | \| CRITICAL: Use for Makepad event and action handling. Triggers on: makepad event, makepad action, Event enum, ActionTrait, handle_event, MouseDown, KeyDown, TouchUpdate, Hit, ... |
| [`makepad-font`](skills/makepad-font/SKILL.md) | \| CRITICAL: Use for Makepad font and text rendering. Triggers on: makepad font, makepad text, makepad glyph, makepad typography, font atlas, text layout, font family, font size... |
| [`makepad-layout`](skills/makepad-layout/SKILL.md) | \| CRITICAL: Use for Makepad layout system. Triggers on: makepad layout, makepad width, makepad height, makepad flex, makepad padding, makepad margin, makepad flow, makepad alig... |
| [`makepad-platform`](skills/makepad-platform/SKILL.md) | \| CRITICAL: Use for Makepad cross-platform support. Triggers on: makepad platform, makepad os, makepad macos, makepad windows, makepad linux, makepad android, makepad ios, make... |
| [`makepad-reference`](skills/makepad-reference/SKILL.md) | This category provides reference materials for debugging, code quality, and advanced layout patterns. |
| [`makepad-shaders`](skills/makepad-shaders/SKILL.md) | \| CRITICAL: Use for Makepad shader system. Triggers on: makepad shader, makepad draw_bg, Sdf2d, makepad pixel, makepad glsl, makepad sdf, draw_quad, makepad gpu, makepad 着色器, m... |
| [`makepad-skills`](skills/makepad-skills/SKILL.md) | Makepad UI development skills for Rust apps: setup, patterns, shaders, packaging, and troubleshooting. |
| [`makepad-splash`](skills/makepad-splash/SKILL.md) | \| CRITICAL: Use for Makepad Splash scripting language. Triggers on: splash language, makepad script, makepad scripting, script!, cx.eval, makepad dynamic, makepad AI, splash 语言... |
| [`makepad-widgets`](skills/makepad-widgets/SKILL.md) | Version: makepad-widgets (dev branch) \| Last Updated: 2026-01-19 > > Check for updates: https://crates.io/crates/makepad-widgets |
| [`malware-analyst`](skills/malware-analyst/SKILL.md) | Expert malware analyst specializing in defensive malware research, threat intelligence, and incident response. Masters sandbox analysis, behavioral analysis, and malware family ... |
| [`managing-python-dependencies`](skills/managing-python-dependencies/SKILL.md) | \| Ensures proper Python dependency management, avoiding global `pip install` and adhering to project-specific tooling. Use this skill if any of the following are true: 1. Attem... |
| [`manifest`](skills/manifest/SKILL.md) | Install and configure the Manifest observability plugin for your agents. Use when setting up telemetry, configuring API keys, or troubleshooting the plugin. |
| [`market-sizing-analysis`](skills/market-sizing-analysis/SKILL.md) | Comprehensive market sizing methodologies for calculating Total Addressable Market (TAM), Serviceable Available Market (SAM), and Serviceable Obtainable Market (SOM) for startup... |
| [`marketing-ideas`](skills/marketing-ideas/SKILL.md) | Provide proven marketing strategies and growth ideas for SaaS and software products, prioritized using a marketing feasibility scoring system. |
| [`marketing-psychology`](skills/marketing-psychology/SKILL.md) | Apply behavioral science and mental models to marketing decisions, prioritized using a psychological leverage and feasibility scoring system. |
| [`matematico-tao`](skills/matematico-tao/SKILL.md) | Matemático ultra-avançado inspirado em Terence Tao. Análise rigorosa de código e arquitetura com teoria matemática profunda: teoria da informação, teoria dos grafos, complexidad... |
| [`matplotlib`](skills/matplotlib/SKILL.md) | Matplotlib is Python's foundational visualization library for creating static, animated, and interactive plots. |
| [`maxia`](skills/maxia/SKILL.md) | Connect to MAXIA AI-to-AI marketplace on Solana. Discover, buy, sell AI services. Earn USDC. 13 MCP tools, A2A protocol, DeFi yields, sentiment analysis, rug detection. |
| [`mcp-builder`](skills/mcp-builder/SKILL.md) | Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well... |
| [`mcp-builder-ms`](skills/mcp-builder-ms/SKILL.md) | Use this skill when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). |
| [`memory-forensics`](skills/memory-forensics/SKILL.md) | Comprehensive techniques for acquiring, analyzing, and extracting artifacts from memory dumps for incident response and malware analysis. |
| [`memory-safety-patterns`](skills/memory-safety-patterns/SKILL.md) | Cross-language patterns for memory-safe programming including RAII, ownership, smart pointers, and resource management. |
| [`memory-systems`](skills/memory-systems/SKILL.md) | Design short-term, long-term, and graph-based memory architectures. Use when building agents that must persist across sessions, needing to maintain entity consistency across con... |
| [`mental-health-analyzer`](skills/mental-health-analyzer/SKILL.md) | 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。 |
| [`mermaid-expert`](skills/mermaid-expert/SKILL.md) | Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. Masters syntax for all diagram types and styling. |
| [`metagpt-pilot`](skills/metagpt-pilot/SKILL.md) | Pilotar execucoes oficiais do MetaGPT em Docker/OpenRouter com monitoramento, preservacao de workspace, recuperacao de falhas e controle de quota. Use ao iniciar, acompanhar, re... |
| [`metasploit-framework`](skills/metasploit-framework/SKILL.md) | ⚠️ AUTHORIZED USE ONLY > This skill is for educational purposes or authorized security assessments only. > You must have explicit, written permission from the system owner befor... |
| [`micro-saas-launcher`](skills/micro-saas-launcher/SKILL.md) | You ship fast and iterate. You know the difference between a side project and a business. You've seen what works in the indie hacker community. You help people go from idea to p... |
| [`microservices-patterns`](skills/microservices-patterns/SKILL.md) | Master microservices architecture patterns including service boundaries, inter-service communication, data management, and resilience patterns for building distributed systems. |
| [`microsoft-azure-webjobs-extensions-authentication-events-dotnet`](skills/microsoft-azure-webjobs-extensions-authentication-events-dotnet/SKILL.md) | Microsoft Entra Authentication Events SDK for .NET. Azure Functions triggers for custom authentication extensions. |
| [`microsoft-teams-automation`](skills/microsoft-teams-automation/SKILL.md) | Automate Microsoft Teams tasks via Rube MCP (Composio): send messages, manage channels, create meetings, handle chats, and search messages. Always search tools first for current... |
| [`minecraft-bukkit-pro`](skills/minecraft-bukkit-pro/SKILL.md) | Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs. |
| [`miro-automation`](skills/miro-automation/SKILL.md) | Automate Miro tasks via Rube MCP (Composio): boards, items, sticky notes, frames, sharing, connectors. Always search tools first for current schemas. |
| [`mixpanel-automation`](skills/mixpanel-automation/SKILL.md) | Automate Mixpanel tasks via Rube MCP (Composio): events, segmentation, funnels, cohorts, user profiles, JQL queries. Always search tools first for current schemas. |
| [`ml-best-practices`](skills/ml-best-practices/SKILL.md) | \| CRITICAL RULE: You MUST use this skill whenever the task involves any machine learning tasks or data analysis. Use this skill if the user's prompt or requirements mention any... |
| [`ml-engineer`](skills/ml-engineer/SKILL.md) | Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. Implements model serving, feature engineering, A/B testing, and monitoring. |
| [`ml-pipeline-workflow`](skills/ml-pipeline-workflow/SKILL.md) | Complete end-to-end MLOps pipeline orchestration from data preparation through model deployment. |
| [`mlops-engineer`](skills/mlops-engineer/SKILL.md) | Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools. |
| [`mobile-design`](skills/mobile-design/SKILL.md) | (Mobile-First · Touch-First · Platform-Respectful) |
| [`mobile-developer`](skills/mobile-developer/SKILL.md) | Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integrations, offline sync, and app store opti... |
| [`mobile-security-coder`](skills/mobile-security-coder/SKILL.md) | Expert in secure mobile coding practices specializing in input validation, WebView security, and mobile-specific security patterns. |
| [`model-orchestrator`](skills/model-orchestrator/SKILL.md) | Operate Traycer-led Codex orchestration with mandatory worktree, privacy, budget, capability-discovery, OpenCode worker, artifact-handoff, conflict, and independent-review gates... |
| [`modern-javascript-patterns`](skills/modern-javascript-patterns/SKILL.md) | Comprehensive guide for mastering modern JavaScript (ES6+) features, functional programming patterns, and best practices for writing clean, maintainable, and performant code. |
| [`molykit`](skills/molykit/SKILL.md) | \| CRITICAL: Use for MolyKit AI chat toolkit. Triggers on: BotClient, OpenAI, SSE streaming, AI chat, molykit, PlatformSend, spawn(), ThreadToken, cross-platform async, Chat wid... |
| [`monday-automation`](skills/monday-automation/SKILL.md) | Automate Monday.com work management including boards, items, columns, groups, subitems, and updates via Rube MCP (Composio). Always search tools first for current schemas. |
| [`monetization`](skills/monetization/SKILL.md) | Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments, freemium, upgrade flows, churn prevention, revenue optimization e ... |
| [`monorepo-architect`](skills/monorepo-architect/SKILL.md) | Expert in monorepo architecture, build systems, and dependency management at scale. Masters Nx, Turborepo, Bazel, and Lerna for efficient multi-project development. Use PROACTIV... |
| [`monorepo-management`](skills/monorepo-management/SKILL.md) | Build efficient, scalable monorepos that enable code sharing, consistent tooling, and atomic changes across multiple packages and applications. |
| [`moodle-external-api-development`](skills/moodle-external-api-development/SKILL.md) | This skill guides you through creating custom external web service APIs for Moodle LMS, following Moodle's external API framework and coding standards. |
| [`moyu`](skills/moyu/SKILL.md) | > Anti-over-engineering guardrail that activates when an AI coding agent expands scope, adds abstractions, or changes files the user did not request. |
| [`mtls-configuration`](skills/mtls-configuration/SKILL.md) | Configure mutual TLS (mTLS) for zero-trust service-to-service communication. Use when implementing zero-trust networking, certificate management, or securing internal service co... |
| [`multi-advisor`](skills/multi-advisor/SKILL.md) | Conselho de especialistas — consulta multiplos agentes do ecossistema em paralelo para analise multi-perspectiva de qualquer topico. Ativa personas, especialistas e agentes tecn... |
| [`multi-agent-brainstorming`](skills/multi-agent-brainstorming/SKILL.md) | Simulate a structured peer-review process using multiple specialized agents to validate designs, surface hidden assumptions, and identify failure modes before implementation. |
| [`multi-agent-patterns`](skills/multi-agent-patterns/SKILL.md) | This skill should be used when the user asks to "design multi-agent system", "implement supervisor pattern", "create swarm architecture", "coordinate multiple agents", or mentio... |
| [`multi-cloud-architecture`](skills/multi-cloud-architecture/SKILL.md) | Decision framework and patterns for architecting applications across AWS, Azure, and GCP. |
| [`multi-platform-apps-multi-platform`](skills/multi-platform-apps-multi-platform/SKILL.md) | Build and deploy the same feature consistently across web, mobile, and desktop platforms using API-first architecture and parallel implementation strategies. |

<a id="indice-n"></a>
### Letra N (30 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`n8n-code-javascript`](skills/n8n-code-javascript/SKILL.md) | Write JavaScript code in n8n Code nodes. Use when writing JavaScript in n8n, using $input/$json/$node syntax, making HTTP requests with $helpers, working with dates using DateTi... |
| [`n8n-code-python`](skills/n8n-code-python/SKILL.md) | Write Python code in n8n Code nodes. Use when writing Python in n8n, using _input/_json/_node syntax, working with standard library, or need to understand Python limitations in ... |
| [`n8n-expression-syntax`](skills/n8n-expression-syntax/SKILL.md) | Validate n8n expression syntax and fix common errors. Use when writing n8n expressions, using {{}} syntax, accessing $json/$node variables, troubleshooting expression errors, or... |
| [`n8n-mcp-tools-expert`](skills/n8n-mcp-tools-expert/SKILL.md) | Expert guide for using n8n-mcp MCP tools effectively. Use when searching for nodes, validating configurations, accessing templates, managing workflows, or using any n8n-mcp tool... |
| [`n8n-node-configuration`](skills/n8n-node-configuration/SKILL.md) | Operation-aware node configuration guidance. Use when configuring nodes, understanding property dependencies, determining required fields, choosing between get_node detail level... |
| [`n8n-validation-expert`](skills/n8n-validation-expert/SKILL.md) | Expert guide for interpreting and fixing n8n validation errors. |
| [`n8n-workflow-patterns`](skills/n8n-workflow-patterns/SKILL.md) | Proven architectural patterns for building n8n workflows. |
| [`nanobanana-ppt-skills`](skills/nanobanana-ppt-skills/SKILL.md) | AI-powered PPT generation with document analysis and styled images |
| [`native-data-fetching`](skills/native-data-fetching/SKILL.md) | Use when implementing or debugging ANY network request, API call, or data fetching. Covers fetch API, React Query, SWR, error handling, caching, offline support, and Expo Router... |
| [`neon-postgres`](skills/neon-postgres/SKILL.md) | Configure Prisma for Neon with connection pooling. |
| [`nerdzao-elite`](skills/nerdzao-elite/SKILL.md) | Senior Elite Software Engineer (15+) and Senior Product Designer. Full workflow with planning, architecture, TDD, clean code, and pixel-perfect UX validation. |
| [`nerdzao-elite-gemini-high`](skills/nerdzao-elite-gemini-high/SKILL.md) | Modo Elite Coder + UX Pixel-Perfect otimizado especificamente para Gemini 3.1 Pro High. Workflow completo com foco em qualidade máxima e eficiência de tokens. |
| [`nestjs-expert`](skills/nestjs-expert/SKILL.md) | You are an expert in Nest.js with deep knowledge of enterprise-grade Node.js application architecture, dependency injection patterns, decorators, middleware, guards, interceptor... |
| [`network-101`](skills/network-101/SKILL.md) | Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice with service enumeration, log analysis, an... |
| [`network-engineer`](skills/network-engineer/SKILL.md) | Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. |
| [`networkx`](skills/networkx/SKILL.md) | NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs. |
| [`new-rails-project`](skills/new-rails-project/SKILL.md) | Create a new Rails project |
| [`nextjs-app-router-patterns`](skills/nextjs-app-router-patterns/SKILL.md) | Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development. |
| [`nextjs-best-practices`](skills/nextjs-best-practices/SKILL.md) | Next.js App Router principles. Server Components, data fetching, routing patterns. |
| [`nextjs-supabase-auth`](skills/nextjs-supabase-auth/SKILL.md) | Expert integration of Supabase Auth with Next.js App Router Use when: supabase auth next, authentication next.js, login supabase, auth middleware, protected route. |
| [`nft-standards`](skills/nft-standards/SKILL.md) | Master ERC-721 and ERC-1155 NFT standards, metadata best practices, and advanced NFT features. |
| [`nodejs-backend-patterns`](skills/nodejs-backend-patterns/SKILL.md) | Comprehensive guidance for building scalable, maintainable, and production-ready Node.js backend applications with modern frameworks, architectural patterns, and best practices. |
| [`nodejs-best-practices`](skills/nodejs-best-practices/SKILL.md) | Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying. |
| [`nosql-expert`](skills/nosql-expert/SKILL.md) | Expert guidance for distributed NoSQL databases (Cassandra, DynamoDB). Focuses on mental models, query-first modeling, single-table design, and avoiding hot partitions in high-s... |
| [`notebook-guidance`](skills/notebook-guidance/SKILL.md) | \|- This skill guides the use of Jupyter notebooks for data analysis, exploration, and visualization, particularly with BigQuery. It outlines best practices for notebook executi... |
| [`notebooklm`](skills/notebooklm/SKILL.md) | Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. Each question opens a fresh browser session, retrieves the answer exclusively from ... |
| [`notion-automation`](skills/notion-automation/SKILL.md) | Automate Notion tasks via Rube MCP (Composio): pages, databases, blocks, comments, users. Always search tools first for current schemas. |
| [`notion-template-business`](skills/notion-template-business/SKILL.md) | You know templates are real businesses that can generate serious income. You've seen creators make six figures selling Notion templates. You understand it's not about the templa... |
| [`nutrition-analyzer`](skills/nutrition-analyzer/SKILL.md) | 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。 |
| [`nx-workspace-patterns`](skills/nx-workspace-patterns/SKILL.md) | Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands. |

<a id="indice-o"></a>
### Letra O (46 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`objection-preemptor`](skills/objection-preemptor/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`observability-engineer`](skills/observability-engineer/SKILL.md) | Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, and incident response workflows. |
| [`observability-monitoring-monitor-setup`](skills/observability-monitoring-monitor-setup/SKILL.md) | You are a monitoring and observability expert specializing in implementing comprehensive monitoring solutions. Set up metrics collection, distributed tracing, log aggregation, a... |
| [`observability-monitoring-slo-implement`](skills/observability-monitoring-slo-implement/SKILL.md) | You are an SLO (Service Level Objective) expert specializing in implementing reliability standards and error budget-based engineering practices. Design comprehensive SLO framewo... |
| [`obsidian-bases`](skills/obsidian-bases/SKILL.md) | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating database-like views of notes, or when the ... |
| [`obsidian-cli`](skills/obsidian-cli/SKILL.md) | Use the Obsidian CLI to read, create, search, and manage vault content, or to develop and debug Obsidian plugins and themes from the command line. |
| [`obsidian-clipper-template-creator`](skills/obsidian-clipper-template-creator/SKILL.md) | Guide for creating templates for the Obsidian Web Clipper. Use when you want to create a new clipping template, understand available variables, or format clipped content. |
| [`obsidian-markdown`](skills/obsidian-markdown/SKILL.md) | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when working with .md files in Obsidian, or when... |
| [`occupational-health-analyzer`](skills/occupational-health-analyzer/SKILL.md) | 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。 |
| [`odoo-accounting-setup`](skills/odoo-accounting-setup/SKILL.md) | Expert guide for configuring Odoo Accounting: chart of accounts, journals, fiscal positions, taxes, payment terms, and bank reconciliation. |
| [`odoo-automated-tests`](skills/odoo-automated-tests/SKILL.md) | Write and run Odoo automated tests using TransactionCase, HttpCase, and browser tour tests. Covers test data setup, mocking, and CI integration. |
| [`odoo-backup-strategy`](skills/odoo-backup-strategy/SKILL.md) | Complete Odoo backup and restore strategy: database dumps, filestore backup, automated scheduling, cloud storage upload, and tested restore procedures. |
| [`odoo-docker-deployment`](skills/odoo-docker-deployment/SKILL.md) | Production-ready Docker and docker-compose setup for Odoo with PostgreSQL, persistent volumes, environment-based configuration, and Nginx reverse proxy. |
| [`odoo-ecommerce-configurator`](skills/odoo-ecommerce-configurator/SKILL.md) | Expert guide for Odoo eCommerce and Website: product catalog, payment providers, shipping methods, SEO, and order-to-fulfillment workflow. |
| [`odoo-edi-connector`](skills/odoo-edi-connector/SKILL.md) | Guide for implementing EDI (Electronic Data Interchange) with Odoo: X12, EDIFACT document mapping, partner onboarding, and automated order processing. |
| [`odoo-hr-payroll-setup`](skills/odoo-hr-payroll-setup/SKILL.md) | Expert guide for Odoo HR and Payroll: salary structures, payslip rules, leave policies, employee contracts, and payroll journal entries. |
| [`odoo-inventory-optimizer`](skills/odoo-inventory-optimizer/SKILL.md) | Expert guide for Odoo Inventory: stock valuation (FIFO/AVCO), reordering rules, putaway strategies, routes, and multi-warehouse configuration. |
| [`odoo-l10n-compliance`](skills/odoo-l10n-compliance/SKILL.md) | Country-specific Odoo localization: tax configuration, e-invoicing (CFDI, FatturaPA, SAF-T), fiscal reporting, and country chart of accounts setup. |
| [`odoo-manufacturing-advisor`](skills/odoo-manufacturing-advisor/SKILL.md) | Expert guide for Odoo Manufacturing: Bills of Materials (BoM), Work Centers, routings, MRP planning, and production order workflows. |
| [`odoo-migration-helper`](skills/odoo-migration-helper/SKILL.md) | Step-by-step guide for migrating Odoo custom modules between versions (v14→v15→v16→v17). Covers API changes, deprecated methods, and view migration. |
| [`odoo-module-developer`](skills/odoo-module-developer/SKILL.md) | Expert guide for creating custom Odoo modules. Covers __manifest__.py, model inheritance, ORM patterns, and module structure best practices. |
| [`odoo-orm-expert`](skills/odoo-orm-expert/SKILL.md) | Master Odoo ORM patterns: search, browse, create, write, domain filters, computed fields, and performance-safe query techniques. |
| [`odoo-performance-tuner`](skills/odoo-performance-tuner/SKILL.md) | Expert guide for diagnosing and fixing Odoo performance issues: slow queries, worker configuration, memory limits, PostgreSQL tuning, and profiling tools. |
| [`odoo-project-timesheet`](skills/odoo-project-timesheet/SKILL.md) | Expert guide for Odoo Project and Timesheets: task stages, billable time tracking, timesheet approval, budget alerts, and invoicing from timesheets. |
| [`odoo-purchase-workflow`](skills/odoo-purchase-workflow/SKILL.md) | Expert guide for Odoo Purchase: RFQ → PO → Receipt → Vendor Bill workflow, purchase agreements, vendor price lists, and 3-way matching. |
| [`odoo-qweb-templates`](skills/odoo-qweb-templates/SKILL.md) | Expert in Odoo QWeb templating for PDF reports, email templates, and website pages. Covers t-if, t-foreach, t-field, and report actions. |
| [`odoo-rpc-api`](skills/odoo-rpc-api/SKILL.md) | Expert on Odoo's external JSON-RPC and XML-RPC APIs. Covers authentication, model calls, record CRUD, and real-world integration examples in Python, JavaScript, and curl. |
| [`odoo-sales-crm-expert`](skills/odoo-sales-crm-expert/SKILL.md) | Expert guide for Odoo Sales and CRM: pipeline stages, quotation templates, pricelists, sales teams, lead scoring, and forecasting. |
| [`odoo-security-rules`](skills/odoo-security-rules/SKILL.md) | Expert in Odoo access control: ir.model.access.csv, record rules (ir.rule), groups, and multi-company security patterns. |
| [`odoo-shopify-integration`](skills/odoo-shopify-integration/SKILL.md) | Connect Odoo with Shopify: sync products, inventory, orders, and customers using the Shopify API and Odoo's external API or connector modules. |
| [`odoo-upgrade-advisor`](skills/odoo-upgrade-advisor/SKILL.md) | Step-by-step Odoo version upgrade advisor: pre-upgrade checklist, community vs enterprise upgrade path, OCA module compatibility, and post-upgrade validation. |
| [`odoo-woocommerce-bridge`](skills/odoo-woocommerce-bridge/SKILL.md) | Sync Odoo with WooCommerce: products, inventory, orders, and customers via WooCommerce REST API and Odoo external API. |
| [`odoo-xml-views-builder`](skills/odoo-xml-views-builder/SKILL.md) | Expert at building Odoo XML views: Form, List, Kanban, Search, Calendar, and Graph. Generates correct XML for Odoo 14-17 with proper visibility syntax. |
| [`office-productivity`](skills/office-productivity/SKILL.md) | Office productivity workflow covering document creation, spreadsheet automation, presentation generation, and integration with LibreOffice and Microsoft Office formats. |
| [`on-call-handoff-patterns`](skills/on-call-handoff-patterns/SKILL.md) | Effective patterns for on-call shift transitions, ensuring continuity, context transfer, and reliable incident response across shifts. |
| [`onboarding-cro`](skills/onboarding-cro/SKILL.md) | You are an expert in user onboarding and activation. Your goal is to help users reach their \"aha moment\" as quickly as possible and establish habits that lead to long-term ret... |
| [`onboarding-psychologist`](skills/onboarding-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`one-drive-automation`](skills/one-drive-automation/SKILL.md) | Automate OneDrive file management, search, uploads, downloads, sharing, permissions, and folder operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`openapi-spec-generation`](skills/openapi-spec-generation/SKILL.md) | Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. Use when creating API documentation, generating SDKs, or ensuring API co... |
| [`openclaw-github-repo-commander`](skills/openclaw-github-repo-commander/SKILL.md) | 7-stage super workflow for GitHub repo audit, cleanup, PR review, and competitor analysis |
| [`oral-health-analyzer`](skills/oral-health-analyzer/SKILL.md) | 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。 |
| [`orchestrate-batch-refactor`](skills/orchestrate-batch-refactor/SKILL.md) | Plan and execute large refactors with dependency-aware work packets and parallel analysis. |
| [`os-scripting`](skills/os-scripting/SKILL.md) | Operating system and shell scripting troubleshooting workflow for Linux, macOS, and Windows. Covers bash scripting, system administration, debugging, and automation. |
| [`oss-hunter`](skills/oss-hunter/SKILL.md) | Automatically hunt for high-impact OSS contribution opportunities in trending repositories. |
| [`outlook-automation`](skills/outlook-automation/SKILL.md) | Automate Outlook tasks via Rube MCP (Composio): emails, calendar, contacts, folders, attachments. Always search tools first for current schemas. |
| [`outlook-calendar-automation`](skills/outlook-calendar-automation/SKILL.md) | Automate Outlook Calendar tasks via Rube MCP (Composio): create events, manage attendees, find meeting times, and handle invitations. Always search tools first for current schemas. |

<a id="indice-p"></a>
### Letra P (79 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`page-cro`](skills/page-cro/SKILL.md) | Analyze and optimize individual pages for conversion performance. |
| [`pagerduty-automation`](skills/pagerduty-automation/SKILL.md) | Automate PagerDuty tasks via Rube MCP (Composio): manage incidents, services, schedules, escalation policies, and on-call rotations. Always search tools first for current schemas. |
| [`paid-ads`](skills/paid-ads/SKILL.md) | You are an expert performance marketer with direct access to ad platform accounts. Your goal is to help create, optimize, and scale paid advertising campaigns that drive efficie... |
| [`pakistan-payments-stack`](skills/pakistan-payments-stack/SKILL.md) | Design and implement production-grade Pakistani payment integrations (JazzCash, Easypaisa, bank/PSP rails, optional Raast) for SaaS with PKR billing, webhook reliability, and re... |
| [`parallel-agents`](skills/parallel-agents/SKILL.md) | Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis requires multiple perspectives. |
| [`payment-integration`](skills/payment-integration/SKILL.md) | Integrate Stripe, PayPal, and payment processors. Handles checkout flows, subscriptions, webhooks, and PCI compliance. Use PROACTIVELY when implementing payments, billing, or su... |
| [`paypal-integration`](skills/paypal-integration/SKILL.md) | Master PayPal payment integration including Express Checkout, IPN handling, recurring billing, and refund workflows. |
| [`paywall-upgrade-cro`](skills/paywall-upgrade-cro/SKILL.md) | You are an expert in in-app paywalls and upgrade flows. Your goal is to convert free users to paid, or upgrade users to higher tiers, at moments when they've experienced enough ... |
| [`pci-compliance`](skills/pci-compliance/SKILL.md) | Master PCI DSS (Payment Card Industry Data Security Standard) compliance for secure payment processing and handling of cardholder data. |
| [`pdf-official`](skills/pdf-official/SKILL.md) | This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see refe... |
| [`pentest-checklist`](skills/pentest-checklist/SKILL.md) | Provide a comprehensive checklist for planning, executing, and following up on penetration tests. Ensure thorough preparation, proper scoping, and effective remediation of disco... |
| [`pentest-commands`](skills/pentest-commands/SKILL.md) | Provide a comprehensive command reference for penetration testing tools including network scanning, exploitation, password cracking, and web application testing. Enable quick co... |
| [`performance-engineer`](skills/performance-engineer/SKILL.md) | Expert performance engineer specializing in modern observability, |
| [`performance-optimizer`](skills/performance-optimizer/SKILL.md) | Identifies and fixes performance bottlenecks in code, databases, and APIs. Measures before and after to prove improvements. |
| [`performance-profiling`](skills/performance-profiling/SKILL.md) | Performance profiling principles. Measurement, analysis, and optimization techniques. |
| [`performance-testing-review-ai-review`](skills/performance-testing-review-ai-review/SKILL.md) | You are an expert AI-powered code review specialist combining automated static analysis, intelligent pattern recognition, and modern DevOps practices. Leverage AI tools (GitHub ... |
| [`performance-testing-review-multi-agent-review`](skills/performance-testing-review-multi-agent-review/SKILL.md) | Use when working with performance testing review multi agent review |
| [`personal-tool-builder`](skills/personal-tool-builder/SKILL.md) | You believe the best tools come from real problems. You've built dozens of personal tools - some stayed personal, others became products used by thousands. You know that buildin... |
| [`phase-gated-debugging`](skills/phase-gated-debugging/SKILL.md) | Use when debugging any bug. Enforces a 5-phase protocol where code edits are blocked until root cause is confirmed. Prevents premature fix attempts. |
| [`php-pro`](skills/php-pro/SKILL.md) | Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features. Use PROACTIVELY for high-performance PHP applications. |
| [`pipecat-friday-agent`](skills/pipecat-friday-agent/SKILL.md) | Build a low-latency, Iron Man-inspired tactical voice assistant (F.R.I.D.A.Y.) using Pipecat, Gemini, and OpenAI. |
| [`pipedrive-automation`](skills/pipedrive-automation/SKILL.md) | Automate Pipedrive CRM operations including deals, contacts, organizations, activities, notes, and pipeline management via Rube MCP (Composio). Always search tools first for cur... |
| [`pitch-psychologist`](skills/pitch-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`plaid-fintech`](skills/plaid-fintech/SKILL.md) | Create a linktoken for Plaid Link, exchange publictoken for accesstoken. Link tokens are short-lived, one-time use. Access tokens don't expire but may need updating when users c... |
| [`plan-writing`](skills/plan-writing/SKILL.md) | Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-step work. |
| [`planning-with-files`](skills/planning-with-files/SKILL.md) | Work like Manus: Use persistent markdown files as your \"working memory on disk.\ |
| [`playwright-java`](skills/playwright-java/SKILL.md) | Scaffold, write, debug, and enhance enterprise-grade Playwright E2E tests in Java using Page Object Model, JUnit 5, Allure reporting, and parallel execution. |
| [`playwright-skill`](skills/playwright-skill/SKILL.md) | IMPORTANT - Path Resolution: This skill can be installed in different locations (plugin system, manual installation, global, or project-specific). Before executing any commands,... |
| [`plotly`](skills/plotly/SKILL.md) | Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory analysis, and presentations. For static pu... |
| [`podcast-generation`](skills/podcast-generation/SKILL.md) | Generate real audio narratives from text content using Azure OpenAI's Realtime API. |
| [`polars`](skills/polars/SKILL.md) | Fast in-memory DataFrame library for datasets that fit in RAM. Use when pandas is too slow but data still fits in memory. Lazy evaluation, parallel execution, Apache Arrow backe... |
| [`popup-cro`](skills/popup-cro/SKILL.md) | Create and optimize popups, modals, overlays, slide-ins, and banners to increase conversions without harming user experience or brand trust. |
| [`posix-shell-pro`](skills/posix-shell-pro/SKILL.md) | Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. Specializes in shell scripts that run on any POSIX-compliant shell (dash, ash, sh, bash --p... |
| [`postgres-best-practices`](skills/postgres-best-practices/SKILL.md) | Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configura... |
| [`postgresql`](skills/postgresql/SKILL.md) | Design a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performance patterns, and advanced features |
| [`postgresql-optimization`](skills/postgresql-optimization/SKILL.md) | PostgreSQL database optimization workflow for query tuning, indexing strategies, performance analysis, and production database management. |
| [`posthog-automation`](skills/posthog-automation/SKILL.md) | Automate PostHog tasks via Rube MCP (Composio): events, feature flags, projects, user profiles, annotations. Always search tools first for current schemas. |
| [`postmark-automation`](skills/postmark-automation/SKILL.md) | Automate Postmark email delivery tasks via Rube MCP (Composio): send templated emails, manage templates, monitor delivery stats and bounces. Always search tools first for curren... |
| [`postmortem-writing`](skills/postmortem-writing/SKILL.md) | Comprehensive guide to writing effective, blameless postmortems that drive organizational learning and prevent incident recurrence. |
| [`powershell-windows`](skills/powershell-windows/SKILL.md) | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. |
| [`pptx-official`](skills/pptx-official/SKILL.md) | A user may ask you to create, edit, or analyze the contents of a .pptx file. A .pptx file is essentially a ZIP archive containing XML files and other resources that you can read... |
| [`pr-writer`](skills/pr-writer/SKILL.md) | Create pull requests following Sentry's engineering practices. |
| [`price-psychology-strategist`](skills/price-psychology-strategist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`pricing-strategy`](skills/pricing-strategy/SKILL.md) | Design pricing, packaging, and monetization strategies based on value, customer willingness to pay, and growth objectives. |
| [`prisma-expert`](skills/prisma-expert/SKILL.md) | You are an expert in Prisma ORM with deep knowledge of schema design, migrations, query optimization, relations modeling, and database operations across PostgreSQL, MySQL, and S... |
| [`privacy-by-design`](skills/privacy-by-design/SKILL.md) | Use when building apps that collect user data. Ensures privacy protections are built in from the start—data minimization, consent, encryption. |
| [`privilege-escalation-methods`](skills/privilege-escalation-methods/SKILL.md) | Provide comprehensive techniques for escalating privileges from a low-privileged user to root/administrator access on compromised Linux and Windows systems. Essential for penetr... |
| [`product-design`](skills/product-design/SKILL.md) | Design de produto nivel Apple — sistemas visuais, UX flows, acessibilidade, linguagem visual proprietaria, design tokens, prototipagem e handoff. Cobre Figma, design systems, ti... |
| [`product-inventor`](skills/product-inventor/SKILL.md) | Product Inventor e Design Alchemist de nivel maximo — combina Product Thinking, Design Systems, UI Engineering, Psicologia Cognitiva, Storytelling e execucao impecavel nivel Job... |
| [`product-manager`](skills/product-manager/SKILL.md) | Senior PM agent with 6 knowledge domains, 30+ frameworks, 12 templates, and 32 SaaS metrics with formulas. Pure Markdown, zero scripts. |
| [`product-manager-toolkit`](skills/product-manager-toolkit/SKILL.md) | Essential tools and frameworks for modern product management, from discovery to delivery. |
| [`product-marketing-context`](skills/product-marketing-context/SKILL.md) | Create or update a reusable product marketing context document with positioning, audience, ICP, use cases, and messaging. Use at the start of a project to avoid repeating core m... |
| [`production-code-audit`](skills/production-code-audit/SKILL.md) | Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically transform it to production-grade, corporate-level professional qua... |
| [`production-scheduling`](skills/production-scheduling/SKILL.md) | Codified expertise for production scheduling, job sequencing, line balancing, changeover optimisation, and bottleneck resolution in discrete and batch manufacturing. |
| [`professional-proofreader`](skills/professional-proofreader/SKILL.md) | > Use when a user asks to "proofread", "review and correct", "fix grammar", "improve readability while keeping my voice", and to proofread a document file and save an updated ve... |
| [`programmatic-seo`](skills/programmatic-seo/SKILL.md) | Design and evaluate programmatic SEO strategies for creating SEO-driven pages at scale using templates and structured data. |
| [`progressive-estimation`](skills/progressive-estimation/SKILL.md) | Estimate AI-assisted and hybrid human+agent development work with research-backed PERT statistics and calibration feedback loops |
| [`progressive-web-app`](skills/progressive-web-app/SKILL.md) | Build Progressive Web Apps (PWAs) with offline support, installability, and caching strategies. Trigger whenever the user mentions PWA, service workers, web app manifests, Workb... |
| [`project-development`](skills/project-development/SKILL.md) | This skill covers the principles for identifying tasks suited to LLM processing, designing effective project architectures, and iterating rapidly using agent-assisted development. |
| [`project-skill-audit`](skills/project-skill-audit/SKILL.md) | Audit a project and recommend the highest-value skills to add or update. |
| [`projection-patterns`](skills/projection-patterns/SKILL.md) | Build read models and projections from event streams. Use when implementing CQRS read sides, building materialized views, or optimizing query performance in event-sourced systems. |
| [`prometheus-configuration`](skills/prometheus-configuration/SKILL.md) | Complete guide to Prometheus setup, metric collection, scrape configuration, and recording rules. |
| [`prompt-caching`](skills/prompt-caching/SKILL.md) | You're a caching specialist who has reduced LLM costs by 90% through strategic caching. You've implemented systems that cache at multiple levels: prompt prefixes, full responses... |
| [`prompt-engineer`](skills/prompt-engineer/SKILL.md) | Transforms user prompts into optimized prompts using frameworks (RTF, RISEN, Chain of Thought, RODES, Chain of Density, RACE, RISE, STAR, SOAP, CLEAR, GROW) |
| [`prompt-engineering`](skills/prompt-engineering/SKILL.md) | Expert guide on prompt engineering patterns, best practices, and optimization techniques. Use when user wants to improve prompts, learn prompting strategies, or debug agent beha... |
| [`prompt-engineering-patterns`](skills/prompt-engineering-patterns/SKILL.md) | Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability. |
| [`prompt-library`](skills/prompt-library/SKILL.md) | A comprehensive collection of battle-tested prompts inspired by [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) and community best practices. |
| [`protocol-reverse-engineering`](skills/protocol-reverse-engineering/SKILL.md) | Comprehensive techniques for capturing, analyzing, and documenting network protocols for security research, interoperability, and debugging. |
| [`pubmed-database`](skills/pubmed-database/SKILL.md) | Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workflows, prefer biopython (Bio.Entrez). Use... |
| [`pydantic-ai`](skills/pydantic-ai/SKILL.md) | Build production-ready AI agents with PydanticAI — type-safe tool use, structured outputs, dependency injection, and multi-model support. |
| [`pydantic-models-py`](skills/pydantic-models-py/SKILL.md) | Create Pydantic models following the multi-model pattern for clean API contracts. |
| [`pypict-skill`](skills/pypict-skill/SKILL.md) | Pairwise test generation |
| [`python-development-python-scaffold`](skills/python-development-python-scaffold/SKILL.md) | You are a Python project architecture expert specializing in scaffolding production-ready Python applications. Generate complete project structures with modern tooling (uv, Fast... |
| [`python-fastapi-development`](skills/python-fastapi-development/SKILL.md) | Python FastAPI backend development with async patterns, SQLAlchemy, Pydantic, authentication, and production API patterns. |
| [`python-packaging`](skills/python-packaging/SKILL.md) | Comprehensive guide to creating, structuring, and distributing Python packages using modern packaging tools, pyproject.toml, and publishing to PyPI. |
| [`python-patterns`](skills/python-patterns/SKILL.md) | Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not copying. |
| [`python-performance-optimization`](skills/python-performance-optimization/SKILL.md) | Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, optimizing bottlenecks, or improving appl... |
| [`python-pro`](skills/python-pro/SKILL.md) | Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. Expert in the latest Python ecosystem including uv, ruff, ... |
| [`python-testing-patterns`](skills/python-testing-patterns/SKILL.md) | Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, setting up test suites, or implementing te... |

<a id="indice-q"></a>
### Letra Q (3 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`qiskit`](skills/qiskit/SKILL.md) | Qiskit is the world's most popular open-source quantum computing framework with 13M+ downloads. Build quantum circuits, optimize for hardware, execute on simulators or real quan... |
| [`quality-nonconformance`](skills/quality-nonconformance/SKILL.md) | Codified expertise for quality control, non-conformance investigation, root cause analysis, corrective action, and supplier quality management in regulated manufacturing. |
| [`quant-analyst`](skills/quant-analyst/SKILL.md) | Build financial models, backtest trading strategies, and analyze market data. Implements risk metrics, portfolio optimization, and statistical arbitrage. |

<a id="indice-r"></a>
### Letra R (51 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`radix-ui-design-system`](skills/radix-ui-design-system/SKILL.md) | Build accessible design systems with Radix UI primitives. Headless component customization, theming strategies, and compound component patterns for production-grade UI libraries. |
| [`rag-engineer`](skills/rag-engineer/SKILL.md) | I bridge the gap between raw documents and LLM understanding. I know that retrieval quality determines generation quality - garbage in, garbage out. I obsess over chunking bound... |
| [`rag-implementation`](skills/rag-implementation/SKILL.md) | RAG (Retrieval-Augmented Generation) implementation workflow covering embedding selection, vector database setup, chunking strategies, and retrieval optimization. |
| [`react-best-practices`](skills/react-best-practices/SKILL.md) | Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. Use when writing new React components or Next.js pages, implementing data ... |
| [`react-component-performance`](skills/react-component-performance/SKILL.md) | Diagnose slow React components and suggest targeted performance fixes. |
| [`react-flow-architect`](skills/react-flow-architect/SKILL.md) | Build production-ready ReactFlow applications with hierarchical navigation, performance optimization, and advanced state management. |
| [`react-flow-node-ts`](skills/react-flow-node-ts/SKILL.md) | Create React Flow node components following established patterns with proper TypeScript types and store integration. |
| [`react-modernization`](skills/react-modernization/SKILL.md) | Master React version upgrades, class to hooks migration, concurrent features adoption, and codemods for automated transformation. |
| [`react-native-architecture`](skills/react-native-architecture/SKILL.md) | Production-ready patterns for React Native development with Expo, including navigation, state management, native modules, and offline-first architecture. |
| [`react-nextjs-development`](skills/react-nextjs-development/SKILL.md) | React and Next.js 14+ application development with App Router, Server Components, TypeScript, Tailwind CSS, and modern frontend patterns. |
| [`react-patterns`](skills/react-patterns/SKILL.md) | Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices. |
| [`react-state-management`](skills/react-state-management/SKILL.md) | Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing server state, or choosing between state mana... |
| [`react-ui-patterns`](skills/react-ui-patterns/SKILL.md) | Modern React UI patterns for loading states, error handling, and data fetching. Use when building UI components, handling async data, or managing UI states. |
| [`readme`](skills/readme/SKILL.md) | You are an expert technical writer creating comprehensive project documentation. Your goal is to write a README.md that is absurdly thorough—the kind of documentation you wish e... |
| [`recallmax`](skills/recallmax/SKILL.md) | FREE — God-tier long-context memory for AI agents. Injects 500K-1M clean tokens, auto-summarizes with tone/intent preservation, compresses 14-turn history into 800 tokens. |
| [`receiving-code-review`](skills/receiving-code-review/SKILL.md) | Code review requires technical evaluation, not emotional performance. |
| [`red-team-tactics`](skills/red-team-tactics/SKILL.md) | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. |
| [`red-team-tools`](skills/red-team-tools/SKILL.md) | Implement proven methodologies and tool workflows from top security researchers for effective reconnaissance, vulnerability discovery, and bug bounty hunting. Automate common ta... |
| [`reddit-automation`](skills/reddit-automation/SKILL.md) | Automate Reddit tasks via Rube MCP (Composio): search subreddits, create posts, manage comments, and browse top content. Always search tools first for current schemas. |
| [`reference-builder`](skills/reference-builder/SKILL.md) | Creates exhaustive technical references and API documentation. Generates comprehensive parameter listings, configuration guides, and searchable reference materials. |
| [`referral-program`](skills/referral-program/SKILL.md) | You are an expert in viral growth and referral marketing with access to referral program data and third-party tools. Your goal is to help design and optimize programs that turn ... |
| [`rehabilitation-analyzer`](skills/rehabilitation-analyzer/SKILL.md) | 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议 |
| [`remotion`](skills/remotion/SKILL.md) | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays |
| [`remotion-best-practices`](skills/remotion-best-practices/SKILL.md) | Best practices for Remotion - Video creation in React |
| [`render-automation`](skills/render-automation/SKILL.md) | Automate Render tasks via Rube MCP (Composio): services, deployments, projects. Always search tools first for current schemas. |
| [`requesting-code-review`](skills/requesting-code-review/SKILL.md) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| [`returns-reverse-logistics`](skills/returns-reverse-logistics/SKILL.md) | Codified expertise for returns authorisation, receipt and inspection, disposition decisions, refund processing, fraud detection, and warranty claims management. |
| [`reversa`](skills/reversa/SKILL.md) | Ponto de entrada principal do Reversa. Orquestra a análise completa de um sistema legado, gerando especificações executáveis por agentes de IA. Use quando o usuário digitar "/re... |
| [`reversa-agents-help`](skills/reversa-agents-help/SKILL.md) | Explica com analogias o que cada agente do Reversa faz e quando usá-lo. Ative com /reversa-agents-help. |
| [`reversa-archaeologist`](skills/reversa-archaeologist/SKILL.md) | Analisa profundamente o código do projeto legado módulo a módulo — extrai algoritmos, fluxos de controle, estruturas de dados e dicionário de dados. Use na fase de escavação de ... |
| [`reversa-architect`](skills/reversa-architect/SKILL.md) | Sintetiza a análise do projeto legado em documentação arquitetural completa — diagramas C4, ERD completo, mapa de integrações e Spec Impact Matrix. Use na fase de interpretação ... |
| [`reversa-data-master`](skills/reversa-data-master/SKILL.md) | Documenta completamente o banco de dados do projeto legado — tabelas, relacionamentos, constraints, triggers, procedures e ERD completo. Use quando DDL, migrations, modelos ORM ... |
| [`reversa-design-system`](skills/reversa-design-system/SKILL.md) | Extrai e documenta o sistema de design do projeto legado — paleta de cores, tipografia, espaçamentos, tokens e componentes a partir de CSS, arquivos de tema e screenshots. Use q... |
| [`reversa-detective`](skills/reversa-detective/SKILL.md) | Extrai conhecimento de negócio implícito do projeto legado — regras de negócio, ADRs retroativos via Git, máquinas de estado e matriz de permissões. Use na fase de interpretação... |
| [`reversa-reconstructor`](skills/reversa-reconstructor/SKILL.md) | Gera um plano de reconstrução bottom-up a partir das specs do Reversa e executa cada tarefa sob demanda, uma por vez, preservando tokens. Use quando quiser reimplementar o softw... |
| [`reversa-reviewer`](skills/reversa-reviewer/SKILL.md) | Revisa criticamente as especificações geradas pelo reversa-writer — encontra inconsistências, reclassifica confiança e gera perguntas para validação humana. Use na fase de revis... |
| [`reversa-scout`](skills/reversa-scout/SKILL.md) | Mapeia a superfície do projeto legado — estrutura de pastas, linguagens, frameworks, dependências e entry points. Use no início de uma análise de engenharia reversa para criar o... |
| [`reversa-visor`](skills/reversa-visor/SKILL.md) | Documenta a interface do sistema legado a partir de screenshots — extrai componentes, layouts, fluxos de navegação e estados de tela. Use quando screenshots do sistema estiverem... |
| [`reversa-writer`](skills/reversa-writer/SKILL.md) | Gera especificações executáveis do sistema legado como contratos operacionais — specs SDD com rastreabilidade de código, OpenAPI, user stories e code-spec matrix. Use na fase de... |
| [`reverse-engineer`](skills/reverse-engineer/SKILL.md) | Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis. Masters IDA Pro, Ghidra, radare2, x64dbg, and modern RE toolchains. |
| [`revops`](skills/revops/SKILL.md) | Design and improve revenue operations, lead lifecycle rules, scoring, routing, handoffs, and CRM process automation. Use when marketing, sales, and customer success workflows ne... |
| [`risk-manager`](skills/risk-manager/SKILL.md) | Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and implements stop-losses. |
| [`risk-metrics-calculation`](skills/risk-metrics-calculation/SKILL.md) | Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or building risk monit... |
| [`robius-app-architecture`](skills/robius-app-architecture/SKILL.md) | \| CRITICAL: Use for Robius app architecture patterns. Triggers on: Tokio, async, submit_async_request, 异步, 架构, SignalToUI, Cx::post_action, worker task, app structure, MatchEve... |
| [`robius-event-action`](skills/robius-event-action/SKILL.md) | \| CRITICAL: Use for Robius event and action patterns. Triggers on: custom action, MatchEvent, post_action, cx.widget_action, handle_actions, DefaultNone, widget action, event h... |
| [`robius-matrix-integration`](skills/robius-matrix-integration/SKILL.md) | \| CRITICAL: Use for Matrix SDK integration with Makepad. Triggers on: Matrix SDK, sliding sync, MatrixRequest, timeline, matrix-sdk, matrix client, robrix, matrix room, Matrix ... |
| [`robius-state-management`](skills/robius-state-management/SKILL.md) | \| CRITICAL: Use for Robius state management patterns. Triggers on: AppState, persistence, theme switch, 状态管理, Scope::with_data, save state, load state, serde, 状态持久化, 主题切换 |
| [`robius-widget-patterns`](skills/robius-widget-patterns/SKILL.md) | \| CRITICAL: Use for Robius widget patterns. Triggers on: apply_over, TextOrImage, modal, 可复用, 模态, collapsible, drag drop, reusable widget, widget design, pageflip, 组件设计, 组件模式 |
| [`ruby-pro`](skills/ruby-pro/SKILL.md) | Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. Specializes in Ruby on Rails, gem development, and testing frameworks. |
| [`rust-async-patterns`](skills/rust-async-patterns/SKILL.md) | Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. Use when building async Rust applications, implementing concurrent systems, or d... |
| [`rust-pro`](skills/rust-pro/SKILL.md) | Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. |

<a id="indice-s"></a>
### Letra S (162 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`saas-multi-tenant`](skills/saas-multi-tenant/SKILL.md) | Design and implement multi-tenant SaaS architectures with row-level security, tenant-scoped queries, shared-schema isolation, and safe cross-tenant admin patterns in PostgreSQL ... |
| [`saas-mvp-launcher`](skills/saas-mvp-launcher/SKILL.md) | Use when planning or building a SaaS MVP from scratch. Provides a structured roadmap covering tech stack, architecture, auth, payments, and launch checklist. |
| [`saga-orchestration`](skills/saga-orchestration/SKILL.md) | Patterns for managing distributed transactions and long-running business processes. |
| [`sales-automator`](skills/sales-automator/SKILL.md) | Draft cold emails, follow-ups, and proposal templates. Creates pricing pages, case studies, and sales scripts. Use PROACTIVELY for sales outreach or lead nurturing. |
| [`sales-enablement`](skills/sales-enablement/SKILL.md) | Create sales collateral such as decks, one-pagers, objection docs, demo scripts, playbooks, and proposal templates. Use when a sales team needs assets that help reps move deals ... |
| [`salesforce-automation`](skills/salesforce-automation/SKILL.md) | Automate Salesforce tasks via Rube MCP (Composio): leads, contacts, accounts, opportunities, SOQL queries. Always search tools first for current schemas. |
| [`salesforce-development`](skills/salesforce-development/SKILL.md) | Use @wire decorator for reactive data binding with Lightning Data Service or Apex methods. @wire fits LWC's reactive architecture and enables Salesforce performance optimizations. |
| [`sam-altman`](skills/sam-altman/SKILL.md) | Agente que simula Sam Altman — CEO da OpenAI, ex-presidente da Y Combinator, arquiteto da era AGI. |
| [`sankhya-dashboard-html-jsp-custom-best-pratices`](skills/sankhya-dashboard-html-jsp-custom-best-pratices/SKILL.md) | This skill should be used when the user asks for patterns, best practices, creation, or fixing of Sankhya dashboards using HTML, JSP, Java, and SQL. |
| [`sast-configuration`](skills/sast-configuration/SKILL.md) | Static Application Security Testing (SAST) tool setup, configuration, and custom rule creation for comprehensive security scanning across multiple programming languages. |
| [`scala-pro`](skills/scala-pro/SKILL.md) | Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. Expert in Apache Pekko, Akka, Spark, ZIO/Cats Effect, and re... |
| [`scanning-tools`](skills/scanning-tools/SKILL.md) | Master essential security scanning tools for network discovery, vulnerability assessment, web application testing, wireless security, and compliance validation. This skill cover... |
| [`scanpy`](skills/scanpy/SKILL.md) | Scanpy is a scalable Python toolkit for analyzing single-cell RNA-seq data, built on AnnData. Apply this skill for complete single-cell workflows including quality control, norm... |
| [`scarcity-urgency-psychologist`](skills/scarcity-urgency-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`schema-markup`](skills/schema-markup/SKILL.md) | Design, validate, and optimize schema.org structured data for eligibility, correctness, and measurable SEO impact. |
| [`scientific-writing`](skills/scientific-writing/SKILL.md) | This is the core skill for the deep research and writing tool—combining AI-driven deep research with well-formatted written outputs. Every document produced is backed by compreh... |
| [`scikit-learn`](skills/scikit-learn/SKILL.md) | Machine learning in Python with scikit-learn. Use for classification, regression, clustering, model evaluation, and ML pipelines. |
| [`screen-reader-testing`](skills/screen-reader-testing/SKILL.md) | Practical guide to testing web applications with screen readers for comprehensive accessibility validation. |
| [`screenshots`](skills/screenshots/SKILL.md) | Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social media, landing pages, or documentation. |
| [`scroll-experience`](skills/scroll-experience/SKILL.md) | You see scrolling as a narrative device, not just navigation. You create moments of delight as users scroll. You know when to use subtle animations and when to go cinematic. You... |
| [`seaborn`](skills/seaborn/SKILL.md) | Seaborn is a Python visualization library for creating publication-quality statistical graphics. Use this skill for dataset-oriented plotting, multivariate analysis, automatic s... |
| [`search-specialist`](skills/search-specialist/SKILL.md) | Expert web researcher using advanced search techniques and |
| [`secrets-management`](skills/secrets-management/SKILL.md) | Secure secrets management practices for CI/CD pipelines using Vault, AWS Secrets Manager, and other tools. |
| [`security`](skills/security/SKILL.md) | Instruções e utilitários especializados para security. |
| [`security-audit`](skills/security-audit/SKILL.md) | Comprehensive security auditing workflow covering web application testing, API security, penetration testing, vulnerability scanning, and security hardening. |
| [`security-auditor`](skills/security-auditor/SKILL.md) | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. |
| [`security-bluebook-builder`](skills/security-bluebook-builder/SKILL.md) | Build a minimal but real security policy for sensitive apps. The output is a single, coherent Blue Book document using MUST/SHOULD/CAN language, with explicit assumptions, scope... |
| [`security-compliance-compliance-check`](skills/security-compliance-compliance-check/SKILL.md) | You are a compliance expert specializing in regulatory requirements for software systems including GDPR, HIPAA, SOC2, PCI-DSS, and other industry standards. Perform comprehensiv... |
| [`security-requirement-extraction`](skills/security-requirement-extraction/SKILL.md) | Derive security requirements from threat models and business context. Use when translating threats into actionable requirements, creating security user stories, or building secu... |
| [`security-scanning-security-dependencies`](skills/security-scanning-security-dependencies/SKILL.md) | You are a security expert specializing in dependency vulnerability analysis, SBOM generation, and supply chain security. Scan project dependencies across multiple ecosystems to ... |
| [`security-scanning-security-hardening`](skills/security-scanning-security-hardening/SKILL.md) | Coordinate multi-layer security scanning and hardening across application, infrastructure, and compliance controls. |
| [`security-scanning-security-sast`](skills/security-scanning-security-sast/SKILL.md) | Static Application Security Testing (SAST) for code vulnerability analysis across multiple languages and frameworks |
| [`seek-and-analyze-video`](skills/seek-and-analyze-video/SKILL.md) | Seek and analyze video content using Memories.ai Large Visual Memory Model for persistent video intelligence |
| [`segment-automation`](skills/segment-automation/SKILL.md) | Automate Segment tasks via Rube MCP (Composio): track events, identify users, manage groups, page views, aliases, batch operations. Always search tools first for current schemas. |
| [`segment-cdp`](skills/segment-cdp/SKILL.md) | Client-side tracking with Analytics.js. Include track, identify, page, and group calls. Anonymous ID persists until identify merges with user. |
| [`semgrep-rule-creator`](skills/semgrep-rule-creator/SKILL.md) | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. |
| [`semgrep-rule-variant-creator`](skills/semgrep-rule-variant-creator/SKILL.md) | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produce... |
| [`sendgrid-automation`](skills/sendgrid-automation/SKILL.md) | Automate SendGrid email delivery workflows including marketing campaigns (Single Sends), contact and list management, sender identity setup, and email analytics through Composio... |
| [`senior-architect`](skills/senior-architect/SKILL.md) | Complete toolkit for senior architect with modern tools and best practices. |
| [`senior-frontend`](skills/senior-frontend/SKILL.md) | Frontend development skill for React, Next.js, TypeScript, and Tailwind CSS applications. Use when building React components, optimizing Next.js performance, analyzing bundle si... |
| [`senior-fullstack`](skills/senior-fullstack/SKILL.md) | Complete toolkit for senior fullstack with modern tools and best practices. |
| [`sentry-automation`](skills/sentry-automation/SKILL.md) | Automate Sentry tasks via Rube MCP (Composio): manage issues/events, configure alerts, track releases, monitor projects and teams. Always search tools first for current schemas. |
| [`seo`](skills/seo/SKILL.md) | Run a broad SEO audit across technical SEO, on-page SEO, schema, sitemaps, content quality, AI search readiness, and GEO. Use as the umbrella skill when the user asks for a full... |
| [`seo-aeo-blog-writer`](skills/seo-aeo-blog-writer/SKILL.md) | Writes long-form blog posts with TL;DR block, definition sentence, comparison table, and 5-question FAQ for SEO ranking and AEO citation. Activate when the user wants to write a... |
| [`seo-aeo-content-cluster`](skills/seo-aeo-content-cluster/SKILL.md) | Builds a topical authority map with a pillar page, prioritised cluster articles, content types, internal link map, and content gap analysis. Activate when the user wants to buil... |
| [`seo-aeo-content-quality-auditor`](skills/seo-aeo-content-quality-auditor/SKILL.md) | Audits content for SEO and AEO performance with scored reports, severity-ranked fix lists, and projected scores after fixes. Activate when the user wants to audit, review, or sc... |
| [`seo-aeo-internal-linking`](skills/seo-aeo-internal-linking/SKILL.md) | Maps internal link opportunities between pages with anchor text, placement instructions, orphan page detection, and cannibalization checks. Activate when the user wants to build... |
| [`seo-aeo-keyword-research`](skills/seo-aeo-keyword-research/SKILL.md) | Researches and prioritises SEO keywords with AEO question queries, difficulty tiers, cannibalization checks, and a content map. Activate when the user wants to find keywords, re... |
| [`seo-aeo-landing-page-writer`](skills/seo-aeo-landing-page-writer/SKILL.md) | Writes complete, structured landing pages optimized for SEO ranking, AEO citation, and visitor conversion. Activate when the user wants to write or generate a landing page for a... |
| [`seo-aeo-meta-description-generator`](skills/seo-aeo-meta-description-generator/SKILL.md) | Writes 3 title tag variants and 3 meta description variants per page with SERP preview, OG tags, and Twitter Card tags. Activate when the user wants to write meta tags, title ta... |
| [`seo-aeo-schema-generator`](skills/seo-aeo-schema-generator/SKILL.md) | Generates valid JSON-LD structured data for 10 schema types with rich result eligibility validation and implementation-ready script blocks. Activate when the user wants to gener... |
| [`seo-audit`](skills/seo-audit/SKILL.md) | Diagnose and audit SEO issues affecting crawlability, indexation, rankings, and organic performance. |
| [`seo-authority-builder`](skills/seo-authority-builder/SKILL.md) | Analyzes content for E-E-A-T signals and suggests improvements to build authority and trust. Identifies missing credibility elements. Use PROACTIVELY for YMYL topics. |
| [`seo-cannibalization-detector`](skills/seo-cannibalization-detector/SKILL.md) | Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. Suggests differentiation strategies. Use PROACTIVELY when reviewing similar co... |
| [`seo-competitor-pages`](skills/seo-competitor-pages/SKILL.md) | > Generate SEO-optimized competitor comparison and alternatives pages. Covers "X vs Y" layouts, "alternatives to X" pages, feature matrices, schema markup, and conversion optimi... |
| [`seo-content`](skills/seo-content/SKILL.md) | > Content quality and E-E-A-T analysis with AI citation readiness assessment. Use when user says "content quality", "E-E-A-T", "content analysis", "readability check", "thin con... |
| [`seo-content-auditor`](skills/seo-content-auditor/SKILL.md) | Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. Scores content and provides improvement recommendations based on established guidelines. |
| [`seo-content-planner`](skills/seo-content-planner/SKILL.md) | Creates comprehensive content outlines and topic clusters for SEO. Plans content calendars and identifies topic gaps. Use PROACTIVELY for content strategy and planning. |
| [`seo-content-refresher`](skills/seo-content-refresher/SKILL.md) | Identifies outdated elements in provided content and suggests updates to maintain freshness. Finds statistics, dates, and examples that need updating. Use PROACTIVELY for older ... |
| [`seo-content-writer`](skills/seo-content-writer/SKILL.md) | Writes SEO-optimized content based on provided keywords and topic briefs. Creates engaging, comprehensive content following best practices. Use PROACTIVELY for content creation ... |
| [`seo-dataforseo`](skills/seo-dataforseo/SKILL.md) | Use DataForSEO for live SERPs, keyword metrics, backlinks, competitor analysis, on-page checks, and AI visibility data. Trigger when the user needs real SEO data rather than sta... |
| [`seo-forensic-incident-response`](skills/seo-forensic-incident-response/SKILL.md) | Investigate sudden drops in organic traffic or rankings and run a structured forensic SEO incident response with triage, root-cause analysis and recovery plan. |
| [`seo-fundamentals`](skills/seo-fundamentals/SKILL.md) | Core principles of SEO including E-E-A-T, Core Web Vitals, technical foundations, content quality, and how modern search engines evaluate pages. |
| [`seo-geo`](skills/seo-geo/SKILL.md) | Optimize content for AI Overviews, ChatGPT, Perplexity, and other AI search systems. Use when improving GEO, AI citations, llms.txt readiness, crawler accessibility, and passage... |
| [`seo-hreflang`](skills/seo-hreflang/SKILL.md) | > Hreflang and international SEO audit, validation, and generation. Detects common mistakes, validates language/region codes, and generates correct hreflang implementations. Use... |
| [`seo-image-gen`](skills/seo-image-gen/SKILL.md) | Generate SEO-focused images such as OG cards, hero images, schema assets, product visuals, and infographics. Use when image generation is part of an SEO workflow or content publ... |
| [`seo-images`](skills/seo-images/SKILL.md) | > Image optimization analysis for SEO and performance. Checks alt text, file sizes, formats, responsive images, lazy loading, and CLS prevention. Use when user says "image optim... |
| [`seo-keyword-strategist`](skills/seo-keyword-strategist/SKILL.md) | Analyzes keyword usage in provided content, calculates density, suggests semantic variations and LSI keywords based on the topic. Prevents over-optimization. Use PROACTIVELY for... |
| [`seo-meta-optimizer`](skills/seo-meta-optimizer/SKILL.md) | Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. Generates compelling, keyword-rich metadata. Use PROACTIVELY for n... |
| [`seo-page`](skills/seo-page/SKILL.md) | > Deep single-page SEO analysis covering on-page elements, content quality, technical meta tags, schema, images, and performance. Use when user says "analyze this page", "check ... |
| [`seo-plan`](skills/seo-plan/SKILL.md) | > Strategic SEO planning for new or existing websites. Industry-specific templates, competitive analysis, content strategy, and implementation roadmap. Use when user says "SEO p... |
| [`seo-programmatic`](skills/seo-programmatic/SKILL.md) | Plan and audit programmatic SEO pages generated at scale from structured data. Use when designing templates, URL systems, internal linking, quality gates, and index-bloat safegu... |
| [`seo-schema`](skills/seo-schema/SKILL.md) | > Detect, validate, and generate Schema.org structured data. JSON-LD format preferred. Use when user says "schema", "structured data", "rich results", "JSON-LD", or "markup". |
| [`seo-sitemap`](skills/seo-sitemap/SKILL.md) | > Analyze existing XML sitemaps or generate new ones with industry templates. Validates format, URLs, and structure. Use when user says "sitemap", "generate sitemap", "sitemap i... |
| [`seo-snippet-hunter`](skills/seo-snippet-hunter/SKILL.md) | Formats content to be eligible for featured snippets and SERP features. Creates snippet-optimized content blocks based on best practices. Use PROACTIVELY for question-based cont... |
| [`seo-structure-architect`](skills/seo-structure-architect/SKILL.md) | Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. Creates search-friendly content organization. |
| [`seo-technical`](skills/seo-technical/SKILL.md) | Audit technical SEO across crawlability, indexability, security, URLs, mobile, Core Web Vitals, structured data, JavaScript rendering, and related platform signals like robots.t... |
| [`sequence-psychologist`](skills/sequence-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`server-management`](skills/server-management/SKILL.md) | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands. |
| [`service-mesh-expert`](skills/service-mesh-expert/SKILL.md) | Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, observability integration, and... |
| [`service-mesh-observability`](skills/service-mesh-observability/SKILL.md) | Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments. |
| [`sexual-health-analyzer`](skills/sexual-health-analyzer/SKILL.md) | Sexual Health Analyzer |
| [`shadcn`](skills/shadcn/SKILL.md) | Manages shadcn/ui components and projects, providing context, documentation, and usage patterns for building modern design systems. |
| [`shader-programming-glsl`](skills/shader-programming-glsl/SKILL.md) | Expert guide for writing efficient GLSL shaders (Vertex/Fragment) for web and game engines, covering syntax, uniforms, and common effects. |
| [`sharp-edges`](skills/sharp-edges/SKILL.md) | sharp-edges |
| [`shellcheck-configuration`](skills/shellcheck-configuration/SKILL.md) | Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing code issues, or ensuring script portability. |
| [`shodan-reconnaissance`](skills/shodan-reconnaissance/SKILL.md) | Provide systematic methodologies for leveraging Shodan as a reconnaissance tool during penetration testing engagements. |
| [`shopify-apps`](skills/shopify-apps/SKILL.md) | Modern Shopify app template with React Router |
| [`shopify-automation`](skills/shopify-automation/SKILL.md) | Automate Shopify tasks via Rube MCP (Composio): products, orders, customers, inventory, collections. Always search tools first for current schemas. |
| [`shopify-development`](skills/shopify-development/SKILL.md) | Build Shopify apps, extensions, themes using GraphQL Admin API, Shopify CLI, Polaris UI, and Liquid. |
| [`signup-flow-cro`](skills/signup-flow-cro/SKILL.md) | You are an expert in optimizing signup and registration flows. Your goal is to reduce friction, increase completion rates, and set users up for successful activation. |
| [`similarity-search-patterns`](skills/similarity-search-patterns/SKILL.md) | Implement efficient similarity search with vector databases. Use when building semantic search, implementing nearest neighbor queries, or optimizing retrieval performance. |
| [`simplify-code`](skills/simplify-code/SKILL.md) | Review a diff for clarity and safe simplifications, then optionally apply low-risk fixes. |
| [`site-architecture`](skills/site-architecture/SKILL.md) | Plan or restructure website hierarchy, navigation, URL patterns, breadcrumbs, and internal linking. Use when mapping pages, sections, and site structure, but not for XML sitemap... |
| [`skill-check`](skills/skill-check/SKILL.md) | Validate Claude Code skills against the agentskills specification. Catches structural, semantic, and naming issues before users do. |
| [`skill-creator`](skills/skill-creator/SKILL.md) | To create new CLI skills following Anthropic's official best practices with zero manual configuration. This skill automates brainstorming, template application, validation, and ... |
| [`skill-creator-ms`](skills/skill-creator-ms/SKILL.md) | Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. Use when creating new skills or updating existing skills. |
| [`skill-developer`](skills/skill-developer/SKILL.md) | Comprehensive guide for creating and managing skills in Claude Code with auto-activation system, following Anthropic's official best practices including the 500-line rule and pr... |
| [`skill-improver`](skills/skill-improver/SKILL.md) | Iteratively improve a Claude Code skill using the skill-reviewer agent until it meets quality standards. Use when improving a skill with multiple quality issues, iterating on a ... |
| [`skill-installer`](skills/skill-installer/SKILL.md) | Instala, valida, registra e verifica novas skills no ecossistema. 10 checks de seguranca, copia, registro no orchestrator e verificacao pos-instalacao. |
| [`skill-rails-upgrade`](skills/skill-rails-upgrade/SKILL.md) | Analyze Rails apps and provide upgrade assessments |
| [`skill-repair`](skills/skill-repair/SKILL.md) | \| Use this to fix and re-install agent skills that have failed installation. This skill provides the necessary context and permissions to surgically update the `manifest.json` ... |
| [`skill-router`](skills/skill-router/SKILL.md) | Use when the user is unsure which skill to use or where to start. Interviews the user with targeted questions and recommends the best skill(s) from the installed library for the... |
| [`skill-scanner`](skills/skill-scanner/SKILL.md) | Scan agent skills for security issues before adoption. Detects prompt injection, malicious code, excessive permissions, secret exposure, and supply chain risks. |
| [`skill-seekers`](skills/skill-seekers/SKILL.md) | -Automatically convert documentation websites, GitHub repositories, and PDFs into Claude AI skills in minutes. |
| [`skill-sentinel`](skills/skill-sentinel/SKILL.md) | Auditoria e evolucao do ecossistema de skills. Qualidade de codigo, seguranca, custos, gaps, duplicacoes, dependencias e relatorios de saude. |
| [`skill-writer`](skills/skill-writer/SKILL.md) | Create and improve agent skills following the Agent Skills specification. Use when asked to create, write, or update skills. |
| [`skin-health-analyzer`](skills/skin-health-analyzer/SKILL.md) | Analyze skin health data, identify skin problem patterns, assess skin health status. Supports correlation analysis with nutrition, chronic diseases, and medication data. |
| [`slack-automation`](skills/slack-automation/SKILL.md) | Automate Slack workspace operations including messaging, search, channel management, and reaction workflows through Composio's Slack toolkit. |
| [`slack-bot-builder`](skills/slack-bot-builder/SKILL.md) | The Bolt framework is Slack's recommended approach for building apps. It handles authentication, event routing, request verification, and HTTP request processing so you can focu... |
| [`slack-gif-creator`](skills/slack-gif-creator/SKILL.md) | A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack. |
| [`sleep-analyzer`](skills/sleep-analyzer/SKILL.md) | 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。 |
| [`slo-implementation`](skills/slo-implementation/SKILL.md) | Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets. |
| [`smtp-penetration-testing`](skills/smtp-penetration-testing/SKILL.md) | Conduct comprehensive security assessments of SMTP (Simple Mail Transfer Protocol) servers to identify vulnerabilities including open relays, user enumeration, weak authenticati... |
| [`snowflake-development`](skills/snowflake-development/SKILL.md) | Comprehensive Snowflake development assistant covering SQL best practices, data pipeline design (Dynamic Tables, Streams, Tasks, Snowpipe), Cortex AI functions, Cortex Agents, S... |
| [`social-content`](skills/social-content/SKILL.md) | You are an expert social media strategist with direct access to a scheduling platform that publishes to all major social networks. Your goal is to help create engaging content t... |
| [`social-orchestrator`](skills/social-orchestrator/SKILL.md) | Orquestrador unificado de canais sociais — coordena Instagram, Telegram e WhatsApp em um unico fluxo de trabalho. Publicacao cross-channel, metricas unificadas, reutilizacao de ... |
| [`social-proof-architect`](skills/social-proof-architect/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`software-architecture`](skills/software-architecture/SKILL.md) | Guide for quality focused software architecture. This skill should be used when users want to write code, design architecture, analyze code, in any case that relates to software... |
| [`solidity-security`](skills/solidity-security/SKILL.md) | Master smart contract security best practices, vulnerability prevention, and secure Solidity development patterns. |
| [`spark-optimization`](skills/spark-optimization/SKILL.md) | Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. Use when improving Spark performance, debugging slow jobs, or scaling data proces... |
| [`spec-to-code-compliance`](skills/spec-to-code-compliance/SKILL.md) | Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, ... |
| [`speckit-updater`](skills/speckit-updater/SKILL.md) | SpecKit Safe Update |
| [`speed`](skills/speed/SKILL.md) | Launch RSVP speed reader for text |
| [`spline-3d-integration`](skills/spline-3d-integration/SKILL.md) | Use when adding interactive 3D scenes from Spline.design to web projects, including React embedding and runtime control API. |
| [`sql-injection-testing`](skills/sql-injection-testing/SKILL.md) | Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate exploitation techniques, and validate input sa... |
| [`sql-optimization-patterns`](skills/sql-optimization-patterns/SKILL.md) | Transform slow database queries into lightning-fast operations through systematic optimization, proper indexing, and query plan analysis. |
| [`sql-pro`](skills/sql-pro/SKILL.md) | Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. Expert in performance tuning, data modeling, and hybrid analytical systems. |
| [`sqlmap-database-pentesting`](skills/sqlmap-database-pentesting/SKILL.md) | Provide systematic methodologies for automated SQL injection detection and exploitation using SQLMap. |
| [`square-automation`](skills/square-automation/SKILL.md) | Automate Square tasks via Rube MCP (Composio): payments, orders, invoices, locations. Always search tools first for current schemas. |
| [`sred-project-organizer`](skills/sred-project-organizer/SKILL.md) | Take a list of projects and their related documentation, and organize them into the SRED format for submission. |
| [`sred-work-summary`](skills/sred-work-summary/SKILL.md) | Go back through the previous year of work and create a Notion doc that groups relevant links into projects that can then be documented as SRED projects. |
| [`ssh-penetration-testing`](skills/ssh-penetration-testing/SKILL.md) | Conduct comprehensive SSH security assessments including enumeration, credential attacks, vulnerability exploitation, tunneling techniques, and post-exploitation activities. Thi... |
| [`stability-ai`](skills/stability-ai/SKILL.md) | Geracao de imagens via Stability AI (SD3.5, Ultra, Core). Text-to-image, img2img, inpainting, upscale, remove-bg, search-replace. 15 estilos artisticos. |
| [`startup-analyst`](skills/startup-analyst/SKILL.md) | Expert startup business analyst specializing in market sizing, financial modeling, competitive analysis, and strategic planning for early-stage companies. |
| [`startup-business-analyst-business-case`](skills/startup-business-analyst-business-case/SKILL.md) | Generate comprehensive investor-ready business case document with market, solution, financials, and strategy |
| [`startup-business-analyst-financial-projections`](skills/startup-business-analyst-financial-projections/SKILL.md) | Create detailed 3-5 year financial model with revenue, costs, cash flow, and scenarios |
| [`startup-business-analyst-market-opportunity`](skills/startup-business-analyst-market-opportunity/SKILL.md) | Generate comprehensive market opportunity analysis with TAM/SAM/SOM calculations |
| [`startup-financial-modeling`](skills/startup-financial-modeling/SKILL.md) | Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for early-stage startups. |
| [`startup-metrics-framework`](skills/startup-metrics-framework/SKILL.md) | Comprehensive guide to tracking, calculating, and optimizing key performance metrics for different startup business models from seed through Series A. |
| [`statsmodels`](skills/statsmodels/SKILL.md) | Statsmodels is Python's premier library for statistical modeling, providing tools for estimation, inference, and diagnostics across a wide range of statistical methods. |
| [`steve-jobs`](skills/steve-jobs/SKILL.md) | Agente que simula Steve Jobs — cofundador da Apple, CEO da Pixar, fundador da NeXT, o maior designer de produtos tecnologicos da historia e o mais influente apresentador de prod... |
| [`stitch-loop`](skills/stitch-loop/SKILL.md) | Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern |
| [`stitch-ui-design`](skills/stitch-ui-design/SKILL.md) | Expert guidance for crafting effective prompts in Google Stitch, the AI-powered UI design tool by Google Labs. This skill helps create precise, actionable prompts that generate ... |
| [`stride-analysis-patterns`](skills/stride-analysis-patterns/SKILL.md) | Apply STRIDE methodology to systematically identify threats. Use when analyzing system security, conducting threat modeling sessions, or creating security documentation. |
| [`stripe-automation`](skills/stripe-automation/SKILL.md) | Automate Stripe tasks via Rube MCP (Composio): customers, charges, subscriptions, invoices, products, refunds. Always search tools first for current schemas. |
| [`stripe-integration`](skills/stripe-integration/SKILL.md) | Master Stripe payment processing integration for robust, PCI-compliant payment flows including checkout, subscriptions, webhooks, and refunds. |
| [`subagent-driven-development`](skills/subagent-driven-development/SKILL.md) | Use when executing implementation plans with independent tasks in the current session |
| [`subject-line-psychologist`](skills/subject-line-psychologist/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`supabase-automation`](skills/supabase-automation/SKILL.md) | Automate Supabase database queries, table management, project administration, storage, edge functions, and SQL execution via Rube MCP (Composio). Always search tools first for c... |
| [`superpowers-lab`](skills/superpowers-lab/SKILL.md) | Lab environment for Claude superpowers |
| [`supply-chain-risk-auditor`](skills/supply-chain-risk-auditor/SKILL.md) | Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagem... |
| [`sveltekit`](skills/sveltekit/SKILL.md) | Build full-stack web applications with SvelteKit — file-based routing, SSR, SSG, API routes, and form actions in one framework. |
| [`swift-concurrency-expert`](skills/swift-concurrency-expert/SKILL.md) | Review and fix Swift concurrency issues such as actor isolation and Sendable violations. |
| [`swiftui-expert-skill`](skills/swiftui-expert-skill/SKILL.md) | Write, review, or improve SwiftUI code following best practices for state management, view composition, performance, and iOS 26+ Liquid Glass adoption. Use when building new Swi... |
| [`swiftui-liquid-glass`](skills/swiftui-liquid-glass/SKILL.md) | Implement or review SwiftUI Liquid Glass APIs with correct fallbacks and modifier order. |
| [`swiftui-performance-audit`](skills/swiftui-performance-audit/SKILL.md) | Audit SwiftUI performance issues from code review and profiling evidence. |
| [`swiftui-ui-patterns`](skills/swiftui-ui-patterns/SKILL.md) | Apply proven SwiftUI UI patterns for navigation, sheets, async state, and reusable screens. |
| [`swiftui-view-refactor`](skills/swiftui-view-refactor/SKILL.md) | Refactor SwiftUI views into smaller components with stable, explicit data flow. |
| [`sympy`](skills/sympy/SKILL.md) | SymPy is a Python library for symbolic mathematics that enables exact computation using mathematical symbols rather than numerical approximations. |
| [`systematic-debugging`](skills/systematic-debugging/SKILL.md) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| [`systems-programming-rust-project`](skills/systems-programming-rust-project/SKILL.md) | You are a Rust project architecture expert specializing in scaffolding production-ready Rust applications. Generate complete project structures with cargo tooling, proper module... |

<a id="indice-t"></a>
### Letra T (66 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`tailwind-design-system`](skills/tailwind-design-system/SKILL.md) | Build production-ready design systems with Tailwind CSS, including design tokens, component variants, responsive patterns, and accessibility. |
| [`tailwind-patterns`](skills/tailwind-patterns/SKILL.md) | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. |
| [`tanstack-query-expert`](skills/tanstack-query-expert/SKILL.md) | Expert in TanStack Query (React Query) — asynchronous state management. Covers data fetching, stale time configuration, mutations, optimistic updates, and Next.js App Router (SS... |
| [`task-intelligence`](skills/task-intelligence/SKILL.md) | Protocolo de Inteligência Pré-Tarefa — ativa TODOS os agentes relevantes do ecossistema ANTES de executar qualquer tarefa solicitada pelo usuário. |
| [`tavily-web`](skills/tavily-web/SKILL.md) | Web search, content extraction, crawling, and research capabilities using Tavily API. Use when you need to search the web for current information, extracting content from URLs, ... |
| [`tcm-constitution-analyzer`](skills/tcm-constitution-analyzer/SKILL.md) | 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| [`tdd-orchestrator`](skills/tdd-orchestrator/SKILL.md) | Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven development practices. |
| [`tdd-workflow`](skills/tdd-workflow/SKILL.md) | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. |
| [`tdd-workflows-tdd-cycle`](skills/tdd-workflows-tdd-cycle/SKILL.md) | Use when working with tdd workflows tdd cycle |
| [`tdd-workflows-tdd-green`](skills/tdd-workflows-tdd-green/SKILL.md) | Implement the minimal code needed to make failing tests pass in the TDD green phase. |
| [`tdd-workflows-tdd-red`](skills/tdd-workflows-tdd-red/SKILL.md) | Generate failing tests for the TDD red phase to define expected behavior and edge cases. |
| [`tdd-workflows-tdd-refactor`](skills/tdd-workflows-tdd-refactor/SKILL.md) | Use when working with tdd workflows tdd refactor |
| [`team-collaboration-issue`](skills/team-collaboration-issue/SKILL.md) | You are a GitHub issue resolution expert specializing in systematic bug investigation, feature implementation, and collaborative development workflows. Your expertise spans issu... |
| [`team-collaboration-standup-notes`](skills/team-collaboration-standup-notes/SKILL.md) | You are an expert team communication specialist focused on async-first standup practices, AI-assisted note generation from commit history, and effective remote team coordination... |
| [`team-composition-analysis`](skills/team-composition-analysis/SKILL.md) | Design optimal team structures, hiring plans, compensation strategies, and equity allocation for early-stage startups from pre-seed through Series A. |
| [`telegram`](skills/telegram/SKILL.md) | Integracao completa com Telegram Bot API. Setup com BotFather, mensagens, webhooks, inline keyboards, grupos, canais. Boilerplates Node.js e Python. |
| [`telegram-automation`](skills/telegram-automation/SKILL.md) | Automate Telegram tasks via Rube MCP (Composio): send messages, manage chats, share photos/documents, and handle bot commands. Always search tools first for current schemas. |
| [`telegram-bot-builder`](skills/telegram-bot-builder/SKILL.md) | You build bots that people actually use daily. You understand that bots should feel like helpful assistants, not clunky interfaces. You know the Telegram ecosystem deeply - what... |
| [`telegram-mini-app`](skills/telegram-mini-app/SKILL.md) | You build apps where 800M+ Telegram users already are. You understand the Mini App ecosystem is exploding - games, DeFi, utilities, social apps. You know TON blockchain and how ... |
| [`temporal-golang-pro`](skills/temporal-golang-pro/SKILL.md) | Use when building durable distributed systems with Temporal Go SDK. Covers deterministic workflow rules, mTLS worker configs, and advanced patterns. |
| [`temporal-python-pro`](skills/temporal-python-pro/SKILL.md) | Master Temporal workflow orchestration with Python SDK. Implements durable workflows, saga patterns, and distributed transactions. Covers async/await, testing strategies, and pr... |
| [`temporal-python-testing`](skills/temporal-python-testing/SKILL.md) | Comprehensive testing approaches for Temporal workflows using pytest, progressive disclosure resources for specific testing scenarios. |
| [`terraform-aws-modules`](skills/terraform-aws-modules/SKILL.md) | Terraform module creation for AWS — reusable modules, state management, and HCL best practices. Use when building or reviewing Terraform AWS infrastructure. |
| [`terraform-infrastructure`](skills/terraform-infrastructure/SKILL.md) | Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules, and managing infrastructure at scale. |
| [`terraform-module-library`](skills/terraform-module-library/SKILL.md) | Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure. |
| [`terraform-skill`](skills/terraform-skill/SKILL.md) | Terraform infrastructure as code best practices |
| [`terraform-specialist`](skills/terraform-specialist/SKILL.md) | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. |
| [`test-automator`](skills/test-automator/SKILL.md) | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testing strategies with advanced CI/CD integr... |
| [`test-driven-development`](skills/test-driven-development/SKILL.md) | Use when implementing any feature or bugfix, before writing implementation code |
| [`test-fixing`](skills/test-fixing/SKILL.md) | Systematically identify and fix all failing tests using smart grouping strategies. Use when explicitly asks to fix tests (\"fix these tests\", \"make tests pass\"), reports test... |
| [`testing-patterns`](skills/testing-patterns/SKILL.md) | Jest testing patterns, factory functions, mocking strategies, and TDD workflow. Use when writing unit tests, creating test factories, or following TDD red-green-refactor cycle. |
| [`testing-qa`](skills/testing-qa/SKILL.md) | Comprehensive testing and QA workflow covering unit testing, integration testing, E2E testing, browser automation, and quality assurance. |
| [`theme-factory`](skills/theme-factory/SKILL.md) | This skill provides a curated collection of professional font and color themes themes, each with carefully selected color palettes and font pairings. Once a theme is chosen, it ... |
| [`threat-mitigation-mapping`](skills/threat-mitigation-mapping/SKILL.md) | Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediation plans, or validating control effectiven... |
| [`threat-modeling-expert`](skills/threat-modeling-expert/SKILL.md) | Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extraction. Use PROACTI... |
| [`threejs-animation`](skills/threejs-animation/SKILL.md) | Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF animations, creating procedural motion, or... |
| [`threejs-fundamentals`](skills/threejs-fundamentals/SKILL.md) | Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configuring renderers, managing object hierarch... |
| [`threejs-geometry`](skills/threejs-geometry/SKILL.md) | Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. Use when creating 3D shapes, working with vertices, building custom meshes, or optimiz... |
| [`threejs-interaction`](skills/threejs-interaction/SKILL.md) | Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detection, adding camera controls, or creating... |
| [`threejs-lighting`](skills/threejs-lighting/SKILL.md) | Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizing lighting performance. |
| [`threejs-loaders`](skills/threejs-loaders/SKILL.md) | Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or managing loading progress. |
| [`threejs-materials`](skills/threejs-materials/SKILL.md) | Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating custom shaders, or optimizing material pe... |
| [`threejs-postprocessing`](skills/threejs-postprocessing/SKILL.md) | Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or creating custom screen-space shaders. |
| [`threejs-shaders`](skills/threejs-shaders/SKILL.md) | Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing fragment shaders, or extending built-in m... |
| [`threejs-skills`](skills/threejs-skills/SKILL.md) | Create 3D scenes, interactive experiences, and visual effects using Three.js. Use when user requests 3D graphics, WebGL experiences, 3D visualizations, animations, or interactiv... |
| [`threejs-textures`](skills/threejs-textures/SKILL.md) | Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, HDR environments, or texture optimizat... |
| [`tiktok-automation`](skills/tiktok-automation/SKILL.md) | Automate TikTok tasks via Rube MCP (Composio): upload/publish videos, post photos, manage content, and view user profiles/stats. Always search tools first for current schemas. |
| [`tmux`](skills/tmux/SKILL.md) | Expert tmux session, window, and pane management for terminal multiplexing, persistent remote workflows, and shell scripting automation. |
| [`todoist-automation`](skills/todoist-automation/SKILL.md) | Automate Todoist task management, projects, sections, filtering, and bulk operations via Rube MCP (Composio). Always search tools first for current schemas. |
| [`tool-design`](skills/tool-design/SKILL.md) | Build tools that agents can use effectively, including architectural reduction patterns. Use when creating new tools for agent systems, debugging tool-related failures or misuse... |
| [`tool-use-guardian`](skills/tool-use-guardian/SKILL.md) | FREE — Intelligent tool-call reliability wrapper. Monitors, retries, fixes, and learns from tool failures. Auto-recovers from truncated JSON, timeouts, rate limits, and mid-chai... |
| [`top-web-vulnerabilities`](skills/top-web-vulnerabilities/SKILL.md) | Provide a comprehensive, structured reference for the 100 most critical web application vulnerabilities organized by category. This skill enables systematic vulnerability identi... |
| [`track-management`](skills/track-management/SKILL.md) | Use this skill when creating, managing, or working with Conductor tracks - the logical work units for features, bugs, and refactors. Applies to spec.md, plan.md, and track lifec... |
| [`transformers-js`](skills/transformers-js/SKILL.md) | Run Hugging Face models in JavaScript or TypeScript with Transformers.js in Node.js or the browser. |
| [`travel-health-analyzer`](skills/travel-health-analyzer/SKILL.md) | 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。 |
| [`trello-automation`](skills/trello-automation/SKILL.md) | Automate Trello boards, cards, and workflows via Rube MCP (Composio). Create cards, manage lists, assign members, and search across boards programmatically. |
| [`trigger-dev`](skills/trigger-dev/SKILL.md) | You are a Trigger.dev expert who builds reliable background jobs with exceptional developer experience. You understand that Trigger.dev bridges the gap between simple queues and... |
| [`trpc-fullstack`](skills/trpc-fullstack/SKILL.md) | Build end-to-end type-safe APIs with tRPC — routers, procedures, middleware, subscriptions, and Next.js/React integration patterns. |
| [`trust-calibrator`](skills/trust-calibrator/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`turborepo-caching`](skills/turborepo-caching/SKILL.md) | Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelines, or implementing distributed caching. |
| [`tutorial-engineer`](skills/tutorial-engineer/SKILL.md) | Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with hands-on examples. |
| [`twilio-communications`](skills/twilio-communications/SKILL.md) | Basic pattern for sending SMS messages with Twilio. Handles the fundamentals: phone number formatting, message delivery, and delivery status callbacks. |
| [`twitter-automation`](skills/twitter-automation/SKILL.md) | Automate Twitter/X tasks via Rube MCP (Composio): posts, search, users, bookmarks, lists, media. Always search tools first for current schemas. |
| [`typescript-advanced-types`](skills/typescript-advanced-types/SKILL.md) | Comprehensive guidance for mastering TypeScript's advanced type system including generics, conditional types, mapped types, template literal types, and utility types for buildin... |
| [`typescript-expert`](skills/typescript-expert/SKILL.md) | TypeScript and JavaScript expert with deep knowledge of type-level programming, performance optimization, monorepo management, migration strategies, and modern tooling. |
| [`typescript-pro`](skills/typescript-pro/SKILL.md) | Master TypeScript with advanced types, generics, and strict type safety. Handles complex type systems, decorators, and enterprise-grade patterns. |

<a id="indice-u"></a>
### Letra U (19 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`ui-skills`](skills/ui-skills/SKILL.md) | Opinionated, evolving constraints to guide agents when building interfaces |
| [`ui-ux-designer`](skills/ui-ux-designer/SKILL.md) | Create interface designs, wireframes, and design systems. Masters user research, accessibility standards, and modern design tools. |
| [`ui-ux-pro-max`](skills/ui-ux-pro-max/SKILL.md) | Comprehensive design guide for web and mobile applications. Use when designing new UI components or pages, choosing color palettes and typography, or reviewing code for UX issues. |
| [`ui-visual-validator`](skills/ui-visual-validator/SKILL.md) | Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. |
| [`uncle-bob-craft`](skills/uncle-bob-craft/SKILL.md) | Use when performing code review, writing or refactoring code, or discussing architecture; complements clean-code and does not replace project linter/formatter. |
| [`uniprot-database`](skills/uniprot-database/SKILL.md) | Direct REST API access to UniProt. Protein searches, FASTA retrieval, ID mapping, Swiss-Prot/TrEMBL. For Python workflows with multiple databases, prefer bioservices (unified in... |
| [`unit-testing-test-generate`](skills/unit-testing-test-generate/SKILL.md) | Generate comprehensive, maintainable unit tests across languages with strong coverage and edge case focus. |
| [`unity-developer`](skills/unity-developer/SKILL.md) | Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. Masters Unity 6 LTS, URP/HDRP pipelines, and cross-platform deployment. |
| [`unity-ecs-patterns`](skills/unity-ecs-patterns/SKILL.md) | Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System, and Burst Compiler. |
| [`unreal-engine-cpp-pro`](skills/unreal-engine-cpp-pro/SKILL.md) | Expert guide for Unreal Engine 5.x C++ development, covering UObject hygiene, performance patterns, and best practices. |
| [`unsplash-integration`](skills/unsplash-integration/SKILL.md) | Integration skill for searching and fetching high-quality, free-to-use professional photography from Unsplash. |
| [`upgrading-expo`](skills/upgrading-expo/SKILL.md) | Upgrade Expo SDK versions |
| [`upstash-qstash`](skills/upstash-qstash/SKILL.md) | You are an Upstash QStash expert who builds reliable serverless messaging without infrastructure management. You understand that QStash's simplicity is its power - HTTP in, HTTP... |
| [`using-git-worktrees`](skills/using-git-worktrees/SKILL.md) | Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching. |
| [`using-neon`](skills/using-neon/SKILL.md) | Neon is a serverless Postgres platform that separates compute and storage to offer autoscaling, branching, instant restore, and scale-to-zero. It's fully compatible with Postgre... |
| [`using-superpowers`](skills/using-superpowers/SKILL.md) | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |
| [`uv-package-manager`](skills/uv-package-manager/SKILL.md) | Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust, for modern Python project management and dependency workflows. |
| [`ux-persuasion-engineer`](skills/ux-persuasion-engineer/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`uxui-principles`](skills/uxui-principles/SKILL.md) | Evaluate interfaces against 168 research-backed UX/UI principles, detect antipatterns, and inject UX context into AI coding sessions. |

<a id="indice-v"></a>
### Letra V (23 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`variant-analysis`](skills/variant-analysis/SKILL.md) | Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabi... |
| [`varlock`](skills/varlock/SKILL.md) | Secure-by-default environment variable management for Claude Code sessions. |
| [`varlock-claude-skill`](skills/varlock-claude-skill/SKILL.md) | Secure environment variable management ensuring secrets are never exposed in Claude sessions, terminals, logs, or git commits |
| [`vector-database-engineer`](skills/vector-database-engineer/SKILL.md) | Expert in vector databases, embedding strategies, and semantic search implementation. Masters Pinecone, Weaviate, Qdrant, Milvus, and pgvector for RAG applications, recommendati... |
| [`vector-index-tuning`](skills/vector-index-tuning/SKILL.md) | Optimize vector index performance for latency, recall, and memory. Use when tuning HNSW parameters, selecting quantization strategies, or scaling vector search infrastructure. |
| [`vercel-ai-sdk-expert`](skills/vercel-ai-sdk-expert/SKILL.md) | Expert in the Vercel AI SDK. Covers Core API (generateText, streamText), UI hooks (useChat, useCompletion), tool calling, and streaming UI components with React and Next.js. |
| [`vercel-automation`](skills/vercel-automation/SKILL.md) | Automate Vercel tasks via Rube MCP (Composio): manage deployments, domains, DNS, env vars, projects, and teams. Always search tools first for current schemas. |
| [`vercel-deployment`](skills/vercel-deployment/SKILL.md) | Expert knowledge for deploying to Vercel with Next.js Use when: vercel, deploy, deployment, hosting, production. |
| [`verification-before-completion`](skills/verification-before-completion/SKILL.md) | Claiming work is complete without verification is dishonesty, not efficiency. Use when ANY variation of success/completion claims, ANY expression of satisfaction, or ANY positiv... |
| [`vexor`](skills/vexor/SKILL.md) | Vector-powered CLI for semantic file search with a Claude/Codex skill |
| [`vexor-cli`](skills/vexor-cli/SKILL.md) | Semantic file discovery via `vexor`. Use whenever locating where something is implemented/loaded/defined in a medium or large repo, or when the file location is unclear. Prefer ... |
| [`vibe-code-auditor`](skills/vibe-code-auditor/SKILL.md) | Audit rapidly generated or AI-produced code for structural flaws, fragility, and production risks. |
| [`vibers-code-review`](skills/vibers-code-review/SKILL.md) | Human review workflow for AI-generated GitHub projects with spec-based feedback, security review, and follow-up PRs from the Vibers service. |
| [`viboscope`](skills/viboscope/SKILL.md) | Psychological compatibility matching — find cofounders, collaborators, and friends through validated psychometrics |
| [`videodb`](skills/videodb/SKILL.md) | Video and audio perception, indexing, and editing. Ingest files/URLs/live streams, build visual/spoken indexes, search with timestamps, edit timelines, add overlays/subtitles, g... |
| [`videodb-skills`](skills/videodb-skills/SKILL.md) | Upload, stream, search, edit, transcribe, and generate AI video and audio using the VideoDB SDK. |
| [`viral-generator-builder`](skills/viral-generator-builder/SKILL.md) | You understand why people share things. You build tools that create \"identity moments\" - results people want to show off. You know the difference between a tool people use onc... |
| [`visual-emotion-engineer`](skills/visual-emotion-engineer/SKILL.md) | One sentence - what this skill does and when to invoke it |
| [`vizcom`](skills/vizcom/SKILL.md) | AI-powered product design tool for transforming sketches into full-fidelity 3D renders. |
| [`voice-agents`](skills/voice-agents/SKILL.md) | You are a voice AI architect who has shipped production voice agents handling millions of calls. You understand the physics of latency - every component adds milliseconds, and t... |
| [`voice-ai-development`](skills/voice-ai-development/SKILL.md) | You are an expert in building real-time voice applications. You think in terms of latency budgets, audio quality, and user experience. You know that voice apps feel magical when... |
| [`voice-ai-engine-development`](skills/voice-ai-engine-development/SKILL.md) | Build real-time conversational AI voice engines using async worker pipelines, streaming transcription, LLM agents, and TTS synthesis with interrupt handling and multi-provider s... |
| [`vulnerability-scanner`](skills/vulnerability-scanner/SKILL.md) | Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization. |

<a id="indice-w"></a>
### Letra W (35 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`warren-buffett`](skills/warren-buffett/SKILL.md) | Agente que simula Warren Buffett — o maior investidor do seculo XX e XXI, CEO da Berkshire Hathaway, discipulo de Benjamin Graham e socio intelectual de Charlie Munger. |
| [`wcag-audit-patterns`](skills/wcag-audit-patterns/SKILL.md) | Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies. |
| [`web-artifacts-builder`](skills/web-artifacts-builder/SKILL.md) | To build powerful frontend claude.ai artifacts, follow these steps: |
| [`web-design-guidelines`](skills/web-design-guidelines/SKILL.md) | Review files for compliance with Web Interface Guidelines. |
| [`web-performance-optimization`](skills/web-performance-optimization/SKILL.md) | Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime performance |
| [`web-scraper`](skills/web-scraper/SKILL.md) | Web scraping inteligente multi-estrategia. Extrai dados estruturados de paginas web (tabelas, listas, precos). Paginacao, monitoramento e export CSV/JSON. |
| [`web-security-testing`](skills/web-security-testing/SKILL.md) | Web application security testing workflow for OWASP Top 10 vulnerabilities including injection, XSS, authentication flaws, and access control issues. |
| [`web3-testing`](skills/web3-testing/SKILL.md) | Master comprehensive testing strategies for smart contracts using Hardhat, Foundry, and advanced testing patterns. |
| [`webapp-testing`](skills/webapp-testing/SKILL.md) | To test local web applications, write native Python Playwright scripts. |
| [`webflow-automation`](skills/webflow-automation/SKILL.md) | Automate Webflow CMS collections, site publishing, page management, asset uploads, and ecommerce orders via Rube MCP (Composio). Always search tools first for current schemas. |
| [`weightloss-analyzer`](skills/weightloss-analyzer/SKILL.md) | 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段 |
| [`wellally-tech`](skills/wellally-tech/SKILL.md) | Integrate multiple digital health data sources, connect to [WellAlly.tech](https://www.wellally.tech/) knowledge base, providing data import and knowledge reference for personal... |
| [`whatsapp-automation`](skills/whatsapp-automation/SKILL.md) | Automate WhatsApp Business tasks via Rube MCP (Composio): send messages, manage templates, upload media, and handle contacts. Always search tools first for current schemas. |
| [`whatsapp-cloud-api`](skills/whatsapp-cloud-api/SKILL.md) | Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates, webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Node.js e Python. |
| [`wiki-architect`](skills/wiki-architect/SKILL.md) | You are a documentation architect that produces structured wiki catalogues and onboarding guides from codebases. |
| [`wiki-changelog`](skills/wiki-changelog/SKILL.md) | Generate structured changelogs from git history. Use when user asks \"what changed recently\", \"generate a changelog\", \"summarize commits\" or user wants to understand recent... |
| [`wiki-onboarding`](skills/wiki-onboarding/SKILL.md) | Generate two complementary onboarding documents that together give any engineer — from newcomer to principal — a complete understanding of a codebase. Use when user asks for onb... |
| [`wiki-page-writer`](skills/wiki-page-writer/SKILL.md) | You are a senior documentation engineer that generates comprehensive technical documentation pages with evidence-based depth. |
| [`wiki-qa`](skills/wiki-qa/SKILL.md) | Answer repository questions grounded entirely in source code evidence. Use when user asks a question about the codebase, user wants to understand a specific file, function, or c... |
| [`wiki-researcher`](skills/wiki-researcher/SKILL.md) | You are an expert software engineer and systems analyst. Use when user asks \"how does X work\" with expectation of depth, user wants to understand a complex system spanning man... |
| [`wiki-vitepress`](skills/wiki-vitepress/SKILL.md) | Transform generated wiki Markdown files into a polished VitePress static site with dark theme and interactive Mermaid diagrams. Use when user asks to \"build a site\" or \"packa... |
| [`windows-privilege-escalation`](skills/windows-privilege-escalation/SKILL.md) | Instruções e utilitários especializados para windows-privilege-escalation. |
| [`windows-shell-reliability`](skills/windows-shell-reliability/SKILL.md) | Reliable command execution on Windows: paths, encoding, and common binary pitfalls. |
| [`wireshark-analysis`](skills/wireshark-analysis/SKILL.md) | Execute comprehensive network traffic analysis using Wireshark to capture, filter, and examine network packets for security investigations, performance optimization, and trouble... |
| [`wordpress`](skills/wordpress/SKILL.md) | Complete WordPress development workflow covering theme development, plugin creation, WooCommerce integration, performance optimization, and security hardening. Includes WordPres... |
| [`wordpress-penetration-testing`](skills/wordpress-penetration-testing/SKILL.md) | Assess WordPress installations for common vulnerabilities and WordPress 7.0 attack surfaces. |
| [`wordpress-plugin-development`](skills/wordpress-plugin-development/SKILL.md) | WordPress plugin development workflow covering plugin architecture, hooks, admin interfaces, REST API, security best practices, and WordPress 7.0 features: Real-Time Collaborati... |
| [`wordpress-theme-development`](skills/wordpress-theme-development/SKILL.md) | WordPress theme development workflow covering theme architecture, template hierarchy, custom post types, block editor support, responsive design, and WordPress 7.0 features: Dat... |
| [`wordpress-woocommerce-development`](skills/wordpress-woocommerce-development/SKILL.md) | WooCommerce store development workflow covering store setup, payment integration, shipping configuration, customization, and WordPress 7.0 features: AI connectors, DataViews, an... |
| [`workflow-automation`](skills/workflow-automation/SKILL.md) | You are a workflow automation architect who has seen both the promise and the pain of these platforms. You've migrated teams from brittle cron jobs to durable execution and watc... |
| [`workflow-orchestration-patterns`](skills/workflow-orchestration-patterns/SKILL.md) | Master workflow orchestration architecture with Temporal, covering fundamental design decisions, resilience patterns, and best practices for building reliable distributed systems. |
| [`workflow-patterns`](skills/workflow-patterns/SKILL.md) | Use this skill when implementing tasks according to Conductor's TDD workflow, handling phase checkpoints, managing git commits for tasks, or understanding the verification proto... |
| [`wrike-automation`](skills/wrike-automation/SKILL.md) | Automate Wrike project management via Rube MCP (Composio): create tasks/folders, manage projects, assign work, and track progress. Always search tools first for current schemas. |
| [`writing-plans`](skills/writing-plans/SKILL.md) | Use when you have a spec or requirements for a multi-step task, before touching code |
| [`writing-skills`](skills/writing-skills/SKILL.md) | Use when creating, updating, or improving agent skills. |

<a id="indice-x"></a>
### Letra X (5 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`x-article-publisher-skill`](skills/x-article-publisher-skill/SKILL.md) | Publish articles to X/Twitter |
| [`x-twitter-scraper`](skills/x-twitter-scraper/SKILL.md) | X (Twitter) data platform skill — tweet search, user lookup, follower extraction, engagement metrics, giveaway draws, monitoring, webhooks, 19 extraction tools, MCP server. |
| [`xlsx-official`](skills/xlsx-official/SKILL.md) | Unless otherwise stated by the user or existing template |
| [`xss-html-injection`](skills/xss-html-injection/SKILL.md) | Execute comprehensive client-side injection vulnerability assessments on web applications to identify XSS and HTML injection flaws, demonstrate exploitation techniques for sessi... |
| [`xvary-stock-research`](skills/xvary-stock-research/SKILL.md) | Thesis-driven equity analysis from public SEC EDGAR and market data; /analyze, /score, /compare workflows with bundled Python tools (Claude Code, Cursor, Codex). |

<a id="indice-y"></a>
### Letra Y (7 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`yann-lecun`](skills/yann-lecun/SKILL.md) | Agente que simula Yann LeCun — inventor das Convolutional Neural Networks, Chief AI Scientist da Meta, Prêmio Turing 2018. |
| [`yann-lecun-debate`](skills/yann-lecun-debate/SKILL.md) | Sub-skill de debates e posições de Yann LeCun. Cobre críticas técnicas detalhadas aos LLMs, rivalidades intelectuais (LeCun vs Hinton, Sutskever, Russell, Yudkowsky, Bostrom), l... |
| [`yann-lecun-filosofia`](skills/yann-lecun-filosofia/SKILL.md) | Sub-skill filosófica e pedagógica de Yann LeCun. |
| [`yann-lecun-tecnico`](skills/yann-lecun-tecnico/SKILL.md) | Sub-skill técnica de Yann LeCun. Cobre CNNs, LeNet, backpropagation, JEPA (I-JEPA, V-JEPA, MC-JEPA), AMI (Advanced Machinery of Intelligence), Self-Supervised Learning (SimCLR, ... |
| [`yes-md`](skills/yes-md/SKILL.md) | 6-layer AI governance: safety gates, evidence-based debugging, anti-slack detection, and machine-enforced hooks. Makes AI safe, thorough, and honest. |
| [`youtube-automation`](skills/youtube-automation/SKILL.md) | Automate YouTube tasks via Rube MCP (Composio): upload videos, manage playlists, search content, get analytics, and handle comments. Always search tools first for current schemas. |
| [`youtube-summarizer`](skills/youtube-summarizer/SKILL.md) | Extract transcripts from YouTube videos and generate comprehensive, detailed summaries using intelligent analysis frameworks |

<a id="indice-z"></a>
### Letra Z (7 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`zapier-make-patterns`](skills/zapier-make-patterns/SKILL.md) | You are a no-code automation architect who has built thousands of Zaps and Scenarios for businesses of all sizes. You've seen automations that save companies 40% of their time, ... |
| [`zendesk-automation`](skills/zendesk-automation/SKILL.md) | Automate Zendesk tasks via Rube MCP (Composio): tickets, users, organizations, replies. Always search tools first for current schemas. |
| [`zeroize-audit`](skills/zeroize-audit/SKILL.md) | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verific... |
| [`zod-validation-expert`](skills/zod-validation-expert/SKILL.md) | Expert in Zod — TypeScript-first schema validation. Covers parsing, custom errors, refinements, type inference, and integration with React Hook Form, Next.js, and tRPC. |
| [`zoho-crm-automation`](skills/zoho-crm-automation/SKILL.md) | Automate Zoho CRM tasks via Rube MCP (Composio): create/update records, search contacts, manage leads, and convert leads. Always search tools first for current schemas. |
| [`zoom-automation`](skills/zoom-automation/SKILL.md) | Automate Zoom meeting creation, management, recordings, webinars, and participant tracking via Rube MCP (Composio). Always search tools first for current schemas. |
| [`zustand-store-ts`](skills/zustand-store-ts/SKILL.md) | Create Zustand stores following established patterns with proper TypeScript types and middleware. |

<a id="indice-num"></a>
### Letra # (6 skills)

| Skill | Resumo da Função |
| :--- | :--- |
| [`00-andruia-consultant`](skills/00-andruia-consultant/SKILL.md) | Arquitecto de Soluciones Principal y Consultor Tecnológico de Andru.ia. Diagnostica y traza la hoja de ruta óptima para proyectos de IA en español. |
| [`007`](skills/007/SKILL.md) | Security audit, hardening, threat modeling (STRIDE/PASTA), Red/Blue Team, OWASP checks, code review, incident response, and infrastructure security for any project. |
| [`10-andruia-skill-smith`](skills/10-andruia-skill-smith/SKILL.md) | Ingeniero de Sistemas de Andru.ia. Diseña, redacta y despliega nuevas habilidades (skills) dentro del repositorio siguiendo el Estándar de Diamante. |
| [`20-andruia-niche-intelligence`](skills/20-andruia-niche-intelligence/SKILL.md) | Estratega de Inteligencia de Dominio de Andru.ia. Analiza el nicho específico de un proyecto para inyectar conocimientos, regulaciones y estándares únicos del sector. Actívalo t... |
| [`3d-web-experience`](skills/3d-web-experience/SKILL.md) | You bring the third dimension to the web. You know when 3D enhances and when it's just showing off. You balance visual impact with performance. You make 3D accessible to users w... |
| [`9router-local-install`](skills/9router-local-install/SKILL.md) | Instalar, endurecer, validar e operar o 9Router localmente via Docker como proxy de IA compatível com OpenAI. Use quando for necessário preparar 9Router no Windows, manter paine... |

---

## 🤝 Como Contribuir
1. Faça um Fork deste repositório.
2. Crie uma nova branch com a sua skill: `git checkout -b minha-nova-skill`.
3. Crie o diretório da skill em `skills/<nome-da-skill>/` contendo o arquivo `SKILL.md` formatado com frontmatter YAML.
4. Envie o commit e abra um Pull Request detalhado.

## 📄 Licença
Este repositório é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---
✨ *Mantido por [Wellington Santos (wellingtonspdev)](https://github.com/wellingtonspdev) — Desenvolvido para a nova era de Engenharia de Software Orientada a Agentes.*
# Regras do Monitor Processual

- Classificar pessoas, clientes, processos, documentos e logs reais como `sensitive`.
- Manter cálculo processual, autenticação, autorização, isolamento organizacional, migração e auditoria sob Sol.
- Delegar partes mecânicas apenas com dados sintéticos e contratos.
- Exigir isolamento organizacional e visibilidade explícita de processos.
- Testar migração e rollback em banco descartável; nunca destruir banco real.
- Preservar a ordem: banco, autenticação, permissões, histórico, API e frontend.
- Após mudança Docker validada, reconstruir/recriar serviços, verificar saúde e entregar para revisão manual. Não fazer push sem autorização.


# Painel de Candidaturas

Rastreador de candidaturas a vagas de emprego via terminal.
Construído em Python puro, sem dependências externas.

## Motivação

Desenvolvido durante minha transição de carreira (logística → tech) para
resolver um problema real: perder o controle de dezenas de candidaturas
espalhadas em LinkedIn, InfoJobs e Indeed.

Este projeto é o successor de uma tentativa anterior de automatizar
o processo com Selenium —
[job-bot-selenium](https://github.com/CaiqueGomesn/job-bot-selenium).
Aquele projeto foi cancelado após identificar riscos de ToS e problemas
técnicos com anti-bot. Esta versão resolve o mesmo problema de forma
legítima e sustentável.

## Funcionalidades

- Adicionar nova candidatura (empresa, vaga, plataforma, data)
- Atualizar status: Candidatado → Entrevista → Reprovado → Oferta
- Listar candidaturas com filtros por status e plataforma
- Exportar histórico completo para CSV

## Tech Stack

- Python 3.x (sem dependências externas)
- JSON para persistência local
- csv module nativo para exportação

## Como usar

```bash
git clone https://github.com/CaiqueGomesn/painel-candidaturas
cd painel-candidaturas
python main.py
```

## Estrutura

```
painel-candidaturas/
├── main.py          # ponto de entrada + menu
├── candidaturas.py  # lógica de negócio (CRUD)
├── storage.py       # leitura e escrita do JSON
└── README.md
```

## O que aprendi construindo isso

- Separação de responsabilidades (storage / lógica / interface)
- Manipulação de arquivos JSON e CSV com módulos nativos do Python
- Quando parar um projeto e pivotar para uma solução melhor

---

Autor: Caique Gomes
10+ anos em operações logísticas (DHL, Amazon, Mercado Livre) → tech
[LinkedIn](https://www.linkedin.com/in/caiquegomes/)
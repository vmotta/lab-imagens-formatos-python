# Laboratório de formatos e compressão de imagens com Python

Atividade prática de **50 minutos**, criada para a disciplina **Tópicos Especiais II — TADS**, sobre JPEG, PNG, WebP, TIFF, transparência, canal alpha e SVG.

[![Abrir no Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vmotta/lab-imagens-formatos-python/blob/main/notebooks/laboratorio_formatos_imagens.ipynb)

## Objetivo

Uma equipe está preparando imagens para um portal institucional. Os estudantes deverão medir tamanho, qualidade e transparência para escolher o formato mais adequado para cada uso.

Ao final, o estudante deverá conseguir:

- inspecionar dimensões, pixels, modo de cor e canal alpha;
- comparar JPEG, PNG, WebP e TIFF;
- observar artefatos produzidos pela compressão JPEG;
- medir a perda com MSE e PSNR;
- preservar e remover transparência de maneira controlada;
- explicar por que SVG pode ser ampliado sem pixelização;
- justificar uma decisão técnica de formato.

## Como executar

### Opção 1 — Google Colab

Clique no botão **Abrir no Google Colab**. No Colab, escolha **Arquivo → Salvar uma cópia no Drive** antes de começar.

### Opção 2 — computador local

```bash
git clone https://github.com/vmotta/lab-imagens-formatos-python.git
cd lab-imagens-formatos-python
python -m venv .venv
```

Ative o ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
jupyter notebook notebooks/laboratorio_formatos_imagens.ipynb
```

## Estrutura do repositório

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/       # modelos para entrega e dúvidas
│   └── workflows/            # validação automática
├── assets/                   # recurso SVG e explicação dos dados
├── docs/
│   ├── ENUNCIADO.md          # texto para publicar no Moodle
│   ├── GUIA_PROFESSOR.md     # planejamento e mediação
│   └── RUBRICA.md            # critérios de avaliação
├── notebooks/
│   └── laboratorio_formatos_imagens.ipynb
├── src/
│   ├── gerar_imagens_exemplo.py
│   └── image_utils.py
├── tests/
│   └── test_image_utils.py
├── CONTRIBUTING.md
└── requirements.txt
```

## Entrega

A entrega principal é o notebook preenchido. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para o fluxo recomendado com GitHub e [docs/RUBRICA.md](docs/RUBRICA.md) para os critérios.

## Materiais do professor

- [Enunciado da atividade](docs/ENUNCIADO.md)
- [Guia de aplicação em 50 minutos](docs/GUIA_PROFESSOR.md)
- [Rubrica de avaliação](docs/RUBRICA.md)

## Validação automática

O GitHub Actions verifica:

- sintaxe dos arquivos Python;
- validade estrutural do notebook;
- testes das funções de apoio.

Para testar localmente:

```bash
pytest -q
python -m json.tool notebooks/laboratorio_formatos_imagens.ipynb > /dev/null
```

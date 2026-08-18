# Instalação da Skill Cefor Slides — Claude Web (Personalizar)

## 📦 Arquivo pronto

**Arquivo:** `cefor-slides.zip` (177 KB — 21 arquivos)
**Atualizado:** 2026-08-18
**Inclui:** scaffold `new-deck.py`, Open Sans embutida (offline), export `.odp` (LibreOffice) e `.pptx`,
extração de `.pptx`, dois exemplos completos (Versão A e Versão B).

---

## 🚀 Como instalar no Claude Web

### Passo 1 — Abrir as configurações
1. Acesse **claude.ai**
2. Clique no seu **ícone de perfil** (canto inferior/superior esquerdo)
3. Selecione **Configurações** (*Settings*)

### Passo 2 — Ir em Personalizar
1. Abra a seção **Personalizar** (*Customize* / *Capabilities*, conforme o idioma da interface)
2. Role até o bloco **Skills** (Habilidades)
3. Se houver o toggle **Code execution / Análise de dados**, deixe **ligado** — é ele que permite rodar
   os scripts Python da skill (`new-deck.py`, `generate-odp.py`, `generate-pptx.py`)

### Passo 3 — Fazer o upload
1. Clique em **Upload skill** / **+ Adicionar skill**
2. Selecione o arquivo **`cefor-slides.zip`** (na raiz deste repositório)
3. Aguarde o processamento e confirme que **Cefor Slides** aparece listada e **ativada**

> O zip já vem no formato que o Claude Web espera: uma pasta raiz `cefor-slides/` contendo o
> `SKILL.md` com o frontmatter (`name`, `description`). Não recompacte manualmente — use
> `python cefor-slides/scripts/make-zip.py` para regerar.

### Passo 4 — Usar
Em qualquer conversa, a skill é acionada automaticamente quando o pedido for de apresentação. Exemplos:

> Crie uma apresentação sobre "Inovação em EaD" para o Cefor, 10 slides, público interno.

> Converta este PowerPoint para o padrão visual do Cefor. *(anexe o `.pptx`)*

> Gere o deck e depois exporte em `.odp` para eu editar no LibreOffice Impress.

---

## 📋 O que vai no pacote

```
cefor-slides/
├── SKILL.md                        ← Fluxo das 6 fases (o Claude lê primeiro)
├── README.md                       ← Documentação completa
├── CEFOR_BRAND.md                  ← Cores, Open Sans, SVGs de marca, voz, anti-patterns
├── STYLE_PRESETS.md                ← Versão A (Cor Sólida) e Versão B (Degradê) + 10 modelos
├── html-template.md                ← Arquitetura HTML/JS (fallback manual)
├── viewport-base.css               ← CSS do palco fixo 16:9 (fallback manual)
├── OTIMIZACAO-TOKENS.md            ← Estratégia de leitura econômica dos arquivos
├── brand/
│   └── CEFOR-Design-System.dc.html ← Design system oficial (referência visual)
├── slide-patterns/
│   └── slide-patterns.md           ← Catálogo de padrões de slide
├── exemplos/
│   ├── exemplo-versao-a.html       ← Deck completo Versão A
│   └── exemplo-versao-b.html       ← Deck completo Versão B
└── scripts/
    ├── new-deck.py                 ← Scaffold: monta o deck a partir só dos corpos de slide
    ├── deck-base.css               ← CSS fixo injetado pelo scaffold
    ├── deck-fonts.css              ← Open Sans embutida (woff2 base64, offline)
    ├── deck_parser.py              ← Parser HTML compartilhado pelos exports
    ├── generate-odp.py             ← HTML → .odp editável (LibreOffice) — recomendado
    ├── generate-pptx.py            ← HTML → .pptx editável (PowerPoint) — quando necessário
    ├── extract-pptx.py             ← Extrai conteúdo de um .pptx recebido
    ├── smoke-test.py               ← Testes de fumaça dos scripts
    ├── make-zip.py                 ← Regera este zip
    └── deploy.sh                   ← Publica link (Vercel, opcional)
```

---

## ✨ Nesta versão

- ✅ **Seta CEFOR corrigida** — novo path oficial, e agora **exclusiva da Versão A**; a Versão B usa os
  grafismos do degradê (quadrados em contorno, círculos concêntricos, linha pontilhada)
- ✅ **Scaffold `new-deck.py`** — você escreve só os corpos de slide, o script injeta head, CSS de palco,
  controlador JS, SVGs de marca e a fonte
- ✅ **Open Sans embutida** (woff2 base64) — o deck funciona **offline**, sem CDN
- ✅ **Export `.odp`** (LibreOffice Impress, software livre — recomendado) e **`.pptx`** (python-pptx, MIT)
  com tabelas reais e validação por releitura do arquivo
- ✅ **Design system atualizado** e exemplos A/B revisados

---

## 🔧 Requisitos

| Para | Precisa |
|------|---------|
| Gerar o HTML | Nada além do navegador (arquivo único, zero dependências) |
| Rodar os scripts no Claude Web | **Code execution** ligado nas configurações |
| Exportar `.odp` | Python 3.7+ e `pip install odfpy` (`pillow` só p/ imagens raster) |
| Exportar `.pptx` | `pip install python-pptx` |
| Abrir o `.odp` | LibreOffice Impress (software livre, padrão do governo federal) |

---

## 🔄 Como atualizar a skill

Depois de qualquer alteração nos arquivos da skill:

```bash
python cefor-slides/scripts/smoke-test.py      # valida os scripts
python cefor-slides/scripts/make-zip.py        # regera cefor-slides.zip
```

Depois, no Claude Web: **Configurações → Personalizar → Skills → Cefor Slides → remover e subir o zip novo**
(ou usar a opção de atualizar, se disponível).

---

## 📞 Problemas comuns

| Sintoma | Causa provável / solução |
|---------|--------------------------|
| Skill não aparece após o upload | Atualize a página (`F5`) e confira se ficou **ativada** na lista |
| Upload rejeitado | O zip precisa ter a pasta `cefor-slides/` na raiz com `SKILL.md` dentro — regere com `make-zip.py` |
| Claude não usa a skill | Cite explicitamente: "use a skill Cefor Slides para…" |
| Erro ao exportar `.odp`/`.pptx` | Falta `odfpy` / `python-pptx`, ou o **code execution** está desligado |
| Fonte trocada no `.odp`/`.pptx` | Instale a **Open Sans** na máquina que abre o arquivo (o HTML já traz a fonte embutida) |
| Cores estranhas | Confira os tokens de `:root` e o contraste em `CEFOR_BRAND.md` |

---

## 🎨 Identidade Cefor (resumo)

- **Lima:** `#B0CB1F` · **Azul:** `#2C459A` · **Oliva:** `#8C9A0D` · **Cinza:** `#EAEAEC`
- **Fonte:** Open Sans (400/600/700/800)
- **Palco:** 1920×1080 fixo, escalado como um todo (nunca reflui)
- **Linguagens visuais:** Versão A (Cor Sólida) e Versão B (Degradê) — **nunca misturadas no mesmo deck**

Referência visual completa: `brand/CEFOR-Design-System.dc.html`.

---

**Pronto para usar!** 🚀

# Instalação da Skill Cefor Slides — Claude Web

## 📦 Arquivo pronto

**Arquivo:** `cefor-slides.zip` (44 KB)  
**Versão:** 1.0 com suporte a .odp (LibreOffice Impress)  
**Atualizado:** 2026-06-19

---

## 🚀 Como instalar no Claude Web

### Passo 1: Acessar Configurações
1. Abra **claude.ai**
2. Clique no seu **ícone de perfil** (canto superior direito)
3. Selecione **Configurações**

### Passo 2: Acessar Capabilities
1. Vá para a aba **Capabilities**
2. Role até **Skills** (seção de habilidades customizadas)

### Passo 3: Upload da Skill
1. Clique em **Upload Skill** ou **+** (botão de adicionar)
2. Selecione o arquivo **`cefor-slides.zip`**
3. Aguarde o upload (deve ser rápido, menos de 1 MB)
4. Confirme se a skill aparece listada

### Passo 4: Usar a Skill
Na sua conversa com Claude, a skill estará disponível automaticamente. Você pode:

- Pedir para **criar uma apresentação** sobre um tema
- Pedir para **converter um PowerPoint** (.pptx)
- Pedir para **melhorar um deck** existente
- Pedir para **exportar em .odp** (LibreOffice Impress)

**Exemplo de prompt:**
> Crie uma apresentação sobre "Inovação em EaD" para o Cefor com 10 slides. Versão A (Cor Sólida). Público: comunidade interna.

---

## 📋 O que está incluído

```
cefor-slides/
├── SKILL.md                       ← Instruções e fluxo (ler primeiro!)
├── README.md                      ← Documentação completa
├── CEFOR_BRAND.md                 ← Identidade visual oficial
├── STYLE_PRESETS.md               ← Versão A e B + 10 modelos
├── html-template.md               ← Arquitetura HTML/JS
├── viewport-base.css              ← CSS do palco fixo 16:9
├── brand/
│   └── CEFOR-Design-System.dc.html ← Design system (referência visual)
├── slide-patterns/
│   └── slide-patterns.md          ← Catálogo de padrões
├── exemplos/
│   └── exemplo-versao-a.html      ← Deck de exemplo (pronto)
└── scripts/
    ├── generate-odp.py            ← Converter HTML → .odp
    ├── extract-pptx.py            ← Extrair conteúdo de .pptx
    └── deploy.sh                  ← Publicar em Vercel (opcional)
```

---

## ✨ Novidades desta versão (2026-06-19)

- ✅ **Exportação para LibreOffice Impress (.odp)** — antes era PowerPoint (.pptx)
- ✅ **Alinhamento com software livre** — conforme política do governo federal
- ✅ **Sem dependências proprietárias** — tudo open source
- ✅ **Script Python nativo** — `generate-odp.py` incluso

**Mudança principal:**  
Na Fase 6A (exportação), em vez de "exportar para PowerPoint", agora é:
```bash
python scripts/generate-odp.py seu-deck.html seu-deck.odp
```
E abre em **LibreOffice Impress** (software livre recomendado pelo gov federal).

---

## 🔧 Requisitos

- **Claude Web** (navegador moderno)
- **Para exportar .odp:** Python 3.7+ + biblioteca obrigatória `odfpy` (e `pillow` opcional, só para
  imagens raster):
  ```bash
  pip install odfpy        # obrigatória
  pip install pillow       # opcional (imagens raster locais)
  ```
- **Para abrir .odp:** LibreOffice Impress (gratuito, software livre)

---

## 📞 Suporte

Se encontrar problemas:

1. **Skill não aparece?** → Atualize a página (`F5`)
2. **Erro ao exportar .odp?** → Verifique se Python está instalado
3. **Cores estranhas?** → Verifique contraste em `CEFOR_BRAND.md`

---

## 📚 Documentação

Para entender completamente como usar, leia **em ordem**:

1. **SKILL.md** — fluxo das 6 fases (obrigatório)
2. **CEFOR_BRAND.md** — marca, cores, tipografia
3. **STYLE_PRESETS.md** — escolher entre Versão A ou B
4. **slide-patterns/** — catálogo de padrões de slide

---

## 🎨 Identidade Cefor

- **Lima:** `#B0CB1F`
- **Azul:** `#2C459A`
- **Oliva:** `#8C9A0D`
- **Fonte:** Open Sans (400/600/700/800)
- **Palco:** 1920×1080 fixo (nunca reflui)
- **Linguagens visuais:** Versão A (Cor Sólida) e Versão B (Degradê)

Consulte `brand/CEFOR-Design-System.dc.html` para ver todos os 10 modelos oficiais.

---

**Pronto para usar!** 🚀

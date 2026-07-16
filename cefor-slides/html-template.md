# Arquitetura HTML — Apresentações Cefor

Arquitetura de referência para gerar os decks. Todo deck usa o modelo de **palco fixo 16:9**: os slides
são criados em 1920×1080 e o palco inteiro é escalado para caber na janela do navegador.

> Inclua sempre o conteúdo COMPLETO de [viewport-base.css](viewport-base.css) no `<style>`, os tokens de
> [CEFOR_BRAND.md](CEFOR_BRAND.md) no `:root`, e siga os modelos oficiais de
> [STYLE_PRESETS.md](STYLE_PRESETS.md) (Versão A ou B). Referência visual para humanos em
> `brand/CEFOR-Design-System.dc.html` (renderizar no navegador; **não** ler como texto).

## Estrutura base

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título da Apresentação — Cefor</title>

    <!-- Fonte institucional do Cefor: Open Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap">

    <style>
        /* === TOKENS DE MARCA (de CEFOR_BRAND.md) === */
        :root {
            --lime: #B0CB1F; --lime-dk: #9DB400; --olive: #8C9A0D;
            --navy: #2C459A; --navy2: #2E3F8F;
            --gray: #EAEAEC; --gray-dk: #D7D7DA;
            --ink: #2B2B2B; --muted: #5A5A5A;
            --green: #2E9B30; --red: #CC1111;
            --grad: radial-gradient(120% 95% at 88% 6%,#C6D452 0%,rgba(198,212,82,0) 46%),
                    radial-gradient(95% 95% at 58% 28%,#7FC24A 0%,rgba(127,194,74,0) 56%),
                    radial-gradient(130% 130% at 16% 98%,#3F9FD6 0%,rgba(63,159,214,0) 58%),
                    linear-gradient(135deg,#57B86A 0%,#36B4A6 46%,#3F93CE 100%);
            --font: 'Open Sans', system-ui, sans-serif;
            --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
            --duration: 0.5s;
            --stage-bg: #11151c;   /* moldura fora do slide (letterbox) */
            --slide-bg: #FFFFFF;   /* Versão A; na B a capa usa var(--grad) */
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: var(--font); color: var(--ink); }

        /* === COLE AQUI O CONTEÚDO INTEIRO DE viewport-base.css === */

        /* === ANIMAÇÕES (sutis — institucional) === */
        .reveal { opacity: 0; transform: translateY(24px);
            transition: opacity var(--duration) var(--ease-out), transform var(--duration) var(--ease-out); }
        .slide.visible .reveal { opacity: 1; transform: translateY(0); }
        .reveal:nth-child(1){transition-delay:.08s} .reveal:nth-child(2){transition-delay:.16s}
        .reveal:nth-child(3){transition-delay:.24s} .reveal:nth-child(4){transition-delay:.32s}

        /* === TIPOGRAFIA (escala 1920×1080) === */
        .t-capa     { font-weight: 800; font-size: 80px; line-height: 1.04; }
        .t-secao    { font-weight: 700; font-size: 54px; line-height: 1.1; }
        .t-conteudo { font-weight: 700; font-size: 36px; }
        .corpo, li  { font-weight: 400; font-size: 26px; line-height: 1.45; }
        .eyebrow    { font-weight: 700; font-size: 15px; letter-spacing: .2em; text-transform: uppercase; }
        .num-secao  { font-weight: 800; font-size: 80px; line-height: 1; }
        .rodape     { font-weight: 600; font-size: 20px; color: #6E7A0A; } /* oliva escurecida p/ contraste AA (~4.7:1); a oliva oficial #8C9A0D dá só 3,1:1 */

        /* === COMPONENTES DE MARCA === */
        .seta { /* seta CEFOR — usar inline o SVG do path abaixo */ }
        .barra-titulo { background: var(--lime); border-radius: 9px; height: 92px;
            display: flex; align-items: center; padding: 0 36px; color: var(--ink); }
        .barra-titulo.b { background: var(--grad); color: #fff; text-shadow: 0 1px 6px rgba(0,0,0,.15); }
        .bullet { width: 18px; height: 18px; background: var(--lime); border-radius: 4px; flex: none; margin-top: 10px; }
        .bullet.b { background: #36B4A6; }
        .trilho { position: absolute; left: 0; top: 0; height: 100%; overflow: hidden; }
    </style>
</head>
<body>
    <div class="deck-viewport">
        <main class="deck-stage" id="deckStage">

            <!-- ===== A1 · CAPA (Versão A) ===== -->
            <section class="slide active" style="--slide-bg:#fff;">
                <!-- bloco lima superior -->
                <div style="position:absolute;left:0;top:0;width:100%;height:66%;background:var(--lime);border-bottom-left-radius:280px;"></div>
                <!-- moldura oliva -->
                <div style="position:absolute;left:120px;top:92px;right:120px;bottom:236px;border:3px solid rgba(140,154,13,.55);border-radius:60px;"></div>
                <!-- seta CEFOR d'água -->
                <svg width="220" height="220" viewBox="0 0 100 100" style="position:absolute;left:156px;top:168px;" aria-hidden="true"><path d="M41.8 26.2 L73.8 58.2 L81.6 50.4 L82 82 L50.4 81.6 L58.2 73.8 L26.2 41.8 Z" fill="rgba(120,134,0,.45)"/></svg>
                <!-- Texto da capa SEMPRE em tinta sobre lima (7,7:1 AA). Branco sobre lima = 1,8:1, reprova WCAG (auditoria A1). -->
                <div style="position:absolute;left:192px;top:300px;right:220px;color:var(--ink);">
                    <div class="eyebrow reveal" style="color:var(--ink);">Título da Apresentação</div>
                    <h1 class="t-capa reveal" style="color:var(--ink);margin-top:22px;">Formação que transforma<br>a educação pública</h1>
                    <p class="corpo reveal" style="color:var(--ink);font-size:36px;margin-top:28px;">Subtítulo · responsável · 2026</p>
                </div>
                <!-- logo IFES inferior-direito (ver SVG da marca em CEFOR_BRAND.md) -->
                <div style="position:absolute;right:108px;bottom:80px;">[LOGO IFES]</div>
            </section>

            <!-- ===== A3 · CONTEÚDO COM LISTA ===== -->
            <section class="slide">
                <div class="trilho" style="width:30%;background:var(--gray);border-top-right-radius:60px;border-bottom-right-radius:60px;">
                    <!-- marca d'água de setas (ver CEFOR_BRAND.md) -->
                </div>
                <svg width="148" height="148" viewBox="0 0 100 100" style="position:absolute;left:392px;top:300px;" aria-hidden="true"><path d="M41.8 26.2 L73.8 58.2 L81.6 50.4 L82 82 L50.4 81.6 L58.2 73.8 L26.2 41.8 Z" fill="var(--navy)"/></svg>
                <div style="position:absolute;left:660px;top:92px;right:108px;">
                    <div class="barra-titulo reveal"><h2 class="t-conteudo">Título do conteúdo</h2></div>
                    <div style="position:relative;height:10px;background:var(--navy);border-radius:5px;margin-top:18px;"><div style="position:absolute;left:62%;top:10px;width:10px;height:32px;background:var(--navy);"></div></div>
                </div>
                <ul style="position:absolute;left:668px;top:400px;right:128px;display:flex;flex-direction:column;gap:36px;list-style:none;">
                    <li class="reveal" style="display:flex;gap:28px;align-items:flex-start;"><span class="bullet"></span><span class="corpo">Primeiro ponto-chave do conteúdo apresentado neste slide.</span></li>
                    <li class="reveal" style="display:flex;gap:28px;align-items:flex-start;"><span class="bullet"></span><span class="corpo">Segundo argumento, com descrição complementar de apoio.</span></li>
                    <li class="reveal" style="display:flex;gap:28px;align-items:flex-start;"><span class="bullet"></span><span class="corpo">Terceiro item da lista, fechando o raciocínio.</span></li>
                </ul>
                <!-- rodapé -->
                <div style="position:absolute;right:0;bottom:84px;left:30%;height:4px;background:var(--olive);"></div>
                <div class="rodape" style="position:absolute;right:56px;bottom:48px;background:#fff;padding-left:28px;">cefor.ifes.edu.br</div>
            </section>

            <!-- ...demais modelos: A2 divisória, A4 destaque, A5 encerramento; ou B1–B5 (degradê)... -->
        </main>
    </div>

    <!-- Edição inline (incluída por padrão) -->
    <div class="edit-hotzone"></div>
    <button class="edit-toggle" id="editToggle" title="Modo edição (E)">✎</button>

    <script>
        /* === CONTROLADOR DA APRESENTAÇÃO === */
        class ApresentacaoCefor {
            constructor() {
                this.slides = document.querySelectorAll('.slide');
                this.atual = 0;
                this.stage = document.getElementById('deckStage');
                this.escalarPalco(); this.navTeclado(); this.navToque(); this.mostrar(0);
            }
            escalarPalco() {
                const escalar = () => {
                    const f = Math.min(window.innerWidth/1920, window.innerHeight/1080);
                    const x = (window.innerWidth - 1920*f)/2, y = (window.innerHeight - 1080*f)/2;
                    this.stage.style.transform = `translate(${x}px, ${y}px) scale(${f})`;
                };
                escalar(); window.addEventListener('resize', escalar);
            }
            navTeclado() {
                document.addEventListener('keydown', (e) => {
                    if (e.target.getAttribute('contenteditable')) return;
                    if (['ArrowRight',' ','PageDown'].includes(e.key)) this.mostrar(this.atual+1);
                    if (['ArrowLeft','PageUp'].includes(e.key)) this.mostrar(this.atual-1);
                    if (e.key==='Home') { e.preventDefault(); this.mostrar(0); }
                    if (e.key==='End') { e.preventDefault(); this.mostrar(this.slides.length-1); }
                    if (e.key==='f'||e.key==='F') {
                        document.fullscreenElement ? document.exitFullscreen()
                            : document.documentElement.requestFullscreen();
                    }
                });
            }
            navToque() {
                let x0 = null;
                document.addEventListener('touchstart', e => x0 = e.touches[0].clientX);
                document.addEventListener('touchend', e => {
                    if (x0===null) return;
                    const dx = e.changedTouches[0].clientX - x0;
                    if (dx < -50) this.mostrar(this.atual+1);
                    if (dx > 50) this.mostrar(this.atual-1);
                    x0 = null;
                });
            }
            mostrar(i) {
                this.atual = Math.max(0, Math.min(i, this.slides.length-1));
                this.slides.forEach((s, idx) => {
                    s.classList.toggle('active', idx===this.atual);
                    s.classList.toggle('visible', idx===this.atual);
                });
            }
        }
        const app = new ApresentacaoCefor();
        /* === EDIÇÃO INLINE: ver seção abaixo === */
    </script>
</body>
</html>
```

## Regras de aplicação dos modelos

- **Escolha UMA linguagem** (Versão A ou B) e use-a no deck inteiro.
- Reproduza fielmente os modelos oficiais (A1–A5 / B1–B5) descritos em
  [STYLE_PRESETS.md](STYLE_PRESETS.md) (a fonte de layout do agente). **Traduza as proporções** do
  preview (960×540) para o palco real **1920×1080** (≈ multiplicar por 2). Não carregue o
  `.dc.html` como texto — é artefato visual para humanos, sem ganho de fidelidade no markup.
- Capa, divisória, conteúdo, destaque/citação e encerramento já têm modelo. Slides de **dados**
  (indicador, gráfico, tabela, linha do tempo) estendem o modelo de **Conteúdo** (A3/B4) na mesma linguagem.
- Sempre presentes: **seta CEFOR** (azul ou lima), **logo IFES** na capa e encerramento, **rodapé**
  `cefor.ifes.edu.br` em oliva. SVGs prontos em [CEFOR_BRAND.md](CEFOR_BRAND.md).

## Recursos obrigatórios de JavaScript

1. **Classe controladora** — navegação por teclado (setas, espaço, PageUp/Down), toque/swipe, e escala
   do palco (uma única `transform`, sem reflow por dispositivo).
2. **Edição inline** (incluída por padrão; ver abaixo).
3. **Opcionais sutis** — contador de slides, indicador de progresso (fora do palco). Evitar efeitos
   chamativos (anti-pattern Cefor).

## Edição inline

Afordância pós-rascunho para ajustar texto no navegador. Incluir por padrão (salvo se pedirem arquivo
travado). **Não usar o seletor CSS `~`** para hover (quebra com `pointer-events:none`); usar JS com
timeout de 400ms.

```css
.edit-hotzone { position: fixed; top:0; left:0; width:80px; height:80px; z-index:10000; cursor:pointer; }
.edit-toggle { position: fixed; top:16px; left:16px; opacity:0; pointer-events:none; transition:opacity .3s ease;
               z-index:10001; background:var(--navy); color:#fff; border:0; border-radius:8px;
               width:44px; height:44px; font-size:20px; cursor:pointer; }
.edit-toggle.show, .edit-toggle.active { opacity:1; pointer-events:auto; }
[contenteditable="true"] { outline: 2px dashed var(--lime); outline-offset: 4px; }
```

```javascript
const editor = {
    isActive: false,
    toggle() {
        this.isActive = !this.isActive;
        document.querySelectorAll('h1,h2,h3,p,li,span').forEach(el => el.setAttribute('contenteditable', this.isActive));
        document.getElementById('editToggle').classList.toggle('active', this.isActive);
    },
    salvar() {
        /* Serializa uma CÓPIA limpa: sem contenteditable, sem elementos injetados por JS,
           sem estado do botão de edição (senão o arquivo salvo reabre "sujo"). */
        const doc = document.documentElement.cloneNode(true);
        doc.querySelectorAll('[contenteditable]').forEach(el => el.removeAttribute('contenteditable'));
        doc.querySelectorAll('.deck-progress').forEach(el => el.remove());
        const bt = doc.querySelector('#editToggle');
        if (bt) bt.classList.remove('active', 'show');
        const html = '<!DOCTYPE html>\n' + doc.outerHTML;
        const a = document.createElement('a');
        a.href = URL.createObjectURL(new Blob([html], {type:'text/html'}));
        const nome = (document.title || '').toLowerCase().normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-')
            .replace(/^-+|-+$/g, '').slice(0, 80) || 'apresentacao-cefor';
        a.download = nome + '.html'; a.click();
    }
};
const hotzone = document.querySelector('.edit-hotzone');
const editToggle = document.getElementById('editToggle');
let hideTimeout = null;
hotzone.addEventListener('mouseenter', () => { clearTimeout(hideTimeout); editToggle.classList.add('show'); });
hotzone.addEventListener('mouseleave', () => { hideTimeout = setTimeout(() => { if(!editor.isActive) editToggle.classList.remove('show'); }, 400); });
editToggle.addEventListener('mouseenter', () => clearTimeout(hideTimeout));
editToggle.addEventListener('mouseleave', () => { hideTimeout = setTimeout(() => { if(!editor.isActive) editToggle.classList.remove('show'); }, 400); });
editToggle.addEventListener('click', () => editor.toggle());
hotzone.addEventListener('click', () => editor.toggle());
document.addEventListener('keydown', (e) => {
    if ((e.key==='e'||e.key==='E') && !e.target.getAttribute('contenteditable')) editor.toggle();
    if (e.key==='Escape' && editor.isActive) editor.toggle();
    if ((e.ctrlKey||e.metaKey) && e.key==='s') { e.preventDefault(); editor.salvar(); }
});
```

## Imagens

- Use **caminhos relativos** (`src="assets/foto.png"`), não base64 — facilita o compartilhamento, a
  publicação por link e o reaproveitamento das imagens na exportação para PowerPoint.
- Logo IFES na capa e no encerramento (SVG inline da marca), preservando proporção.
- Fotos/telas em layout de duas colunas com texto. Mantenha tudo dentro do palco 1920×1080; se o slide
  já está cheio, divida em dois.

## Qualidade de código

- Comentários `/* === NOME DA SEÇÃO === */` e `<!-- ID do modelo -->` em cada slide.
- HTML semântico, navegação por teclado completa, ARIA quando necessário.
- **Hierarquia de títulos (auditoria A6):** `<h1>` só na capa; títulos de slide de conteúdo em
  `<h2 class="t-conteudo">` (não `<span>`/`<div>`); subseções em `<h3>`.
- **Decorativos (auditoria A7):** toda seta CEFOR, marca d'água e grafismo decorativo com
  `aria-hidden="true"`; logo IFES com `role="img"` + `aria-label`.
- `prefers-reduced-motion` já vem em viewport-base.css.
- Arquivo único autossuficiente: todo CSS/JS inline; só `assets/` para imagens.

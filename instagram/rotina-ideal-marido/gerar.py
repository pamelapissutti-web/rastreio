# Monta slides.html deste carrossel reaproveitando a base visual do carrossel
# de venda (../rotina-ideal-venda/slides.html). Uso: python3 gerar.py && node render.mjs
from pathlib import Path

aqui = Path(__file__).parent
src = (aqui / '../rotina-ideal-venda/slides.html').read_text()


def entre(a, b):
    i = src.index(a)
    return src[i:src.index(b, i)]


base = entre('  /* Recado de mãe pra mãe', '  .faixa {')
faixa = entre('  .faixa {', '  .selo {')
selo = entre('  .selo {', '  .polaroid {')
balao = entre('  .balao {', '  /* ---------- 1 · CAPA')

css = r'''
  .tinta .rodape { color: var(--papel); }
  .tinta .rodape .pag { color: var(--amarelo); }
  .amarelo mark::before { background: var(--papel); }
  .rec { font-family: 'Courier Prime', 'Courier New', monospace; }

  /* ---------- 1 · CAPA ---------- */
  .capa .abre { font-size: 62px; color: var(--amarelo); }
  .chat { margin-top: 44px; display: flex; flex-direction: column; gap: 18px; }
  .bolha {
    max-width: 760px;
    font-size: 44px;
    line-height: 1.2;
    font-weight: 500;
    padding: 24px 32px 18px;
    border-radius: 34px;
    box-shadow: 0 14px 24px -16px rgba(0,0,0,.6);
  }
  .bolha small { display: block; text-align: right; font-size: 22px; opacity: .55; margin-top: 6px; font-weight: 500; }
  .bolha.ela { align-self: flex-end; background: var(--amarelo); color: var(--tinta); border-bottom-right-radius: 8px; }
  .bolha.ele { align-self: flex-start; background: var(--papel); color: var(--tinta); border-bottom-left-radius: 8px; }
  .capa .grito { margin-top: 56px; font-size: 150px; color: var(--papel); }
  .capa .grito span { display: inline-block; background: var(--amarelo); color: var(--tinta); padding: 12px 24px 0; margin-top: 10px; transform: rotate(-2deg); }
  .capa .arrasta { margin-top: 40px; font-size: 56px; color: var(--amarelo); display: flex; align-items: center; gap: 18px; }

  /* ---------- 2 · CUPOM ---------- */
  .cupom-sl .abre { font-size: 68px; color: var(--tinta); }
  .cupom {
    position: relative;
    align-self: center;
    margin-top: 40px;
    width: 800px;
    background: var(--papel);
    padding: 54px 54px 60px;
    transform: rotate(-1.5deg);
    filter: drop-shadow(0 22px 22px rgba(27,24,48,.35));
    -webkit-mask: radial-gradient(14px at 50% 0, #0000 98%, #000) 50% 0 / 40px 51% repeat-x, radial-gradient(14px at 50% 100%, #0000 98%, #000) 50% 100% / 40px 51% repeat-x;
            mask: radial-gradient(14px at 50% 0, #0000 98%, #000) 50% 0 / 40px 51% repeat-x, radial-gradient(14px at 50% 100%, #0000 98%, #000) 50% 100% / 40px 51% repeat-x;
  }
  .cupom h3 { font-size: 40px; text-align: center; font-weight: 700; letter-spacing: .04em; }
  .cupom .sub { font-size: 26px; text-align: center; margin-top: 6px; color: #5B5770; }
  .cupom .tracejado { border-top: 3px dashed #9C98AE; margin: 26px 0; }
  .cupom .linha-c { display: flex; align-items: baseline; gap: 12px; font-size: 32px; margin-top: 16px; }
  .cupom .linha-c .pontos { flex: 1; border-bottom: 3px dotted #9C98AE; transform: translateY(-6px); }
  .cupom .linha-c .x { color: var(--vermelho); font-weight: 700; font-size: 38px; }
  .cupom .total { display: flex; justify-content: space-between; font-size: 34px; font-weight: 700; margin-top: 12px; }
  .cupom .total span:last-child { color: var(--vermelho); }
  .cupom .tchau { text-align: center; font-size: 26px; margin-top: 26px; color: #5B5770; }
  .cupom-sl .postit {
    position: absolute;
    right: 64px;
    bottom: 140px;
    width: 480px;
    background: var(--rosa);
    transform: rotate(4deg);
    font-size: 46px;
    z-index: 8;
  }
  .cupom-sl .postit .fita { top: -24px; left: 150px; transform: rotate(-3deg); }

  /* ---------- 3 · ELE TEM RAZÃO ---------- */
  .razao .grito { font-size: 176px; margin-top: 30px; }
  .razao .grito span { color: var(--vermelho); }
  .razao .texto { margin-top: 44px; font-size: 46px; line-height: 1.3; font-weight: 500; max-width: 880px; }
  .razao .nota {
    position: relative;
    margin-top: 50px;
    background: var(--papel);
    padding: 38px 42px;
    transform: rotate(-1.2deg);
    font-size: 42px;
    line-height: 1.3;
    font-weight: 500;
    box-shadow: 0 20px 34px -22px rgba(27,24,48,.6);
  }
  .razao .nota b { font-weight: 800; }
  .razao .nota .fita { top: -24px; right: 90px; transform: rotate(4deg); }
  .razao .fecho { margin-top: 48px; font-size: 76px; position: relative; align-self: flex-start; color: var(--caneta); }

  /* ---------- 4 · O RISCO FICA COMIGO ---------- */
  .risco .abre { font-size: 66px; color: var(--caneta); }
  .risco .grito { font-size: 172px; margin-top: 12px; }
  .risco .selo { right: 64px; top: 120px; transform: rotate(12deg); }
  .risco .selo b { font-size: 96px; }
  .risco .selo span { font-size: 34px; }
  .risco .nota {
    position: relative;
    margin-top: 50px;
    background: var(--papel);
    padding: 38px 44px 30px;
    transform: rotate(1deg);
    box-shadow: 0 20px 34px -22px rgba(27,24,48,.6);
  }
  .risco .nota .fita { top: -24px; left: 90px; transform: rotate(-4deg); }
  .risco .nota p { font-size: 44px; line-height: 1.26; font-weight: 500; }
  .risco .nota b { font-weight: 800; }
  .risco .assina { font-size: 60px; color: var(--caneta); margin-top: 8px; text-align: right; }
  .risco .miudo { margin-top: 30px; font-size: 26px; font-weight: 600; }

  /* ---------- 5 · ANTES × AGORA ---------- */
  .compara .abre { font-size: 66px; color: var(--caneta); }
  .compara .cab { display: grid; grid-template-columns: 1fr 1fr; gap: 26px; margin-top: 40px; }
  .compara .cab span { font-weight: 800; font-stretch: condensed; text-transform: uppercase; font-size: 38px; padding: 8px 18px 6px; justify-self: start; }
  .compara .cab span:first-child { background: #CFCBDB; color: #4A4664; }
  .compara .cab span:last-child { background: var(--tinta); color: var(--amarelo); }
  .compara .fila { display: grid; grid-template-columns: 1fr 1fr; gap: 26px; margin-top: 28px; align-items: stretch; }
  .compara .antes, .compara .agora { padding: 26px 28px; font-size: 38px; line-height: 1.16; font-weight: 600; }
  .compara .antes { background: rgba(207,203,219,.55); color: #6A6680; text-decoration: line-through; text-decoration-color: var(--vermelho); text-decoration-thickness: 4px; }
  .compara .agora { background: var(--amarelo); color: var(--tinta); box-shadow: 0 14px 22px -16px rgba(27,24,48,.55); }
  .compara .fila:nth-child(odd) .agora { transform: rotate(-1deg); }
  .compara .fila:nth-child(even) .agora { transform: rotate(1deg); }

  /* ---------- 6 · PRO MARIDO ---------- */
  .marido .topo { display: flex; justify-content: space-between; align-items: center; }
  .marido .topo .mao { font-size: 60px; color: var(--amarelo); }
  .printa {
    background: var(--vermelho);
    color: var(--papel);
    font-weight: 800;
    font-stretch: condensed;
    text-transform: uppercase;
    font-size: 34px;
    padding: 12px 22px 10px;
    transform: rotate(4deg);
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .carta {
    position: relative;
    margin-top: 56px;
    background:
      repeating-linear-gradient(180deg, transparent 0, transparent 57px, var(--linha) 57px, var(--linha) 58px),
      var(--papel);
    background-position: 0 20px;
    color: var(--tinta);
    padding: 40px 48px 44px;
    transform: rotate(-1deg);
    box-shadow: 0 26px 40px -24px rgba(0,0,0,.7);
  }
  .carta .fita { top: -24px; left: 50%; margin-left: -95px; transform: rotate(2deg); }
  .carta .oi { font-size: 72px; color: var(--caneta); line-height: 62px; }
  .carta ul { list-style: none; margin-top: 40px; display: flex; flex-direction: column; gap: 30px; }
  .carta li { font-size: 44px; line-height: 1.22; font-weight: 600; padding-left: 44px; position: relative; }
  .carta li::before { content: ''; position: absolute; left: 0; top: 17px; width: 18px; height: 18px; border-radius: 50%; background: var(--vermelho); }
  .carta .conclui { margin-top: 50px; font-size: 112px; }
  .carta .conclui span { color: var(--vermelho); }
  .carta .ast { font-size: 26px; font-weight: 600; margin-top: 22px; color: #5B5770; }

  /* ---------- 7 · CUSTA CARO ---------- */
  .caro .grito { font-size: 150px; margin-top: 10px; }
  .caro .texto { margin-top: 40px; font-size: 46px; line-height: 1.3; font-weight: 500; }
  .caro .tags { display: flex; flex-wrap: wrap; gap: 18px 20px; margin-top: 34px; }
  .caro .tags span {
    font-family: var(--mao);
    font-weight: 700;
    font-size: 60px;
    line-height: 1;
    color: var(--tinta);
    background: var(--papel);
    padding: 16px 28px 12px;
    box-shadow: 0 12px 20px -14px rgba(27,24,48,.55);
    transform: rotate(-2deg);
  }
  .caro .tags span:nth-child(even) { transform: rotate(2deg); background: var(--amarelo); }
  .caro .fecho { margin-top: 56px; font-size: 76px; color: var(--vermelho); position: relative; align-self: flex-start; }

  /* ---------- 8 · LETRA MIÚDA ---------- */
  .miuda .titulo { font-size: 80px; line-height: 60px; color: var(--caneta); padding-top: 28px; }
  .miuda .itens { margin-top: 60px; display: flex; flex-direction: column; gap: 60px; max-width: 860px; }
  .miuda .item { position: relative; font-size: 40px; line-height: 60px; font-weight: 500; }
  .miuda .item b { font-weight: 800; }
  .miuda .item svg { position: absolute; left: -96px; top: -4px; width: 64px; height: 64px; }
  .miuda .postit {
    margin-top: 26px;
    align-self: flex-end;
    width: 560px;
    padding: 26px 34px;
    background: var(--amarelo);
    transform: rotate(-3deg);
    font-size: 42px;
    z-index: 4;
  }
  .miuda .postit small { display: block; font-family: var(--display); font-weight: 600; font-size: 22px; margin-top: 14px; line-height: 1.3; }
  .miuda .postit .fita { top: -24px; left: 160px; transform: rotate(-3deg); }

  /* ---------- 9 · CTA ---------- */
  .cta .abre { font-size: 62px; color: var(--caneta); max-width: 860px; }
  .cta .grito { font-size: 180px; margin-top: 30px; }
  .cta .palavra {
    display: inline-block;
    background: var(--tinta);
    color: var(--amarelo);
    font-size: 236px;
    padding: 18px 40px 0;
    margin-top: 14px;
    transform: rotate(-2deg);
  }
  .cta .convite { display: flex; align-items: flex-end; gap: 18px; margin-top: 28px; font-size: 56px; max-width: 900px; }
  .cta .convite b { color: var(--vermelho); }
  .cta .notas { display: flex; justify-content: space-between; align-items: flex-start; margin-top: 40px; gap: 24px; }
  .cta .comenta {
    position: relative;
    background: var(--papel);
    padding: 24px 30px 20px;
    transform: rotate(-2deg);
    font-size: 32px;
    font-weight: 700;
    width: 430px;
    line-height: 1.2;
    box-shadow: 0 16px 28px -18px rgba(27,24,48,.6);
  }
  .cta .comenta .fita { top: -26px; left: 40px; transform: rotate(-6deg); width: 150px; }
  .cta .marca {
    background: var(--vermelho);
    color: var(--papel);
    font-family: var(--mao);
    font-weight: 700;
    font-size: 50px;
    line-height: 1;
    padding: 24px 30px 20px;
    border-radius: 999px;
    transform: rotate(5deg);
    box-shadow: 0 14px 24px -14px rgba(27,24,48,.7);
    margin-top: 20px;
  }
  .cta .faixa { position: relative; left: auto; right: auto; margin: auto -150px 0; transform: rotate(1.5deg); }
  .cta .rodape { margin-top: 40px; }
'''


def check(d):
    return (f'<svg viewBox="0 0 66 66"><path d="{d}" fill="none" stroke="#1B1830" stroke-width="4" stroke-linejoin="round"/>'
            '<path d="M14 34 L30 52 L64 4" fill="none" stroke="#E33B2B" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def seta(cor):
    return (f'<svg width="150" height="70" viewBox="0 0 150 70" style="overflow:visible;flex:none">'
            f'<path d="M4 44 C 40 14, 90 12, 136 34" fill="none" stroke="{cor}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M112 14 L138 35 L110 52" fill="none" stroke="{cor}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def rod(n):
    return f'<div class="rodape"><span class="arroba">@pamelapissutti</span><span class="pag">{n}/9</span></div>'


caixas = ['M8 10 L60 6 L62 60 L6 62 Z', 'M6 8 L62 10 L58 62 L8 58 Z', 'M10 6 L60 10 L62 58 L6 60 Z',
          'M6 10 L62 6 L60 62 L8 60 Z', 'M8 8 L60 10 L62 60 L8 58 Z']
sublinha = ('<svg class="doodle" style="left:-6px;right:-6px;bottom:-26px;width:calc(100% + 12px);height:34px" '
            'viewBox="0 0 600 34" preserveAspectRatio="none"><path d="M6 20 C 90 4, 170 30, 260 16 S 420 6, 594 18" '
            'stroke="#E33B2B" stroke-width="8"/></svg>')
aviao = ('<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#FFFDF6" stroke-width="2.4" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M21 3 10 14M21 3l-7 18-4-7-7-4z"/></svg>')

body = f'''
<!-- 1 · CAPA -->
<section class="slide tinta capa" id="s1">
  <p class="mao abre">já viveu essa conversa?</p>
  <div class="chat">
    <div class="bolha ela">amor, achei uma mentoria de sono pro nosso bebê...<small>23:47</small></div>
    <div class="bolha ele">de novo? a última não resolveu nada<small>23:52</small></div>
    <div class="bolha ele">isso é jogar dinheiro fora<small>23:52</small></div>
  </div>
  <h1 class="grito">E quem acorda<br>às 3h <span>é você.</span></h1>
  <div class="mao arrasta">arrasta, esse post é pra vocês dois {seta('#FFD93B')}</div>
  {rod(1)}
</section>

<!-- 2 · CUPOM DE TENTATIVAS -->
<section class="slide kraft cupom-sl" id="s2">
  <p class="mao abre">me deixa adivinhar o seu histórico:</p>
  <div class="cupom rec">
    <h3>CUPOM DE TENTATIVAS</h3>
    <p class="sub">desde que o bebê nasceu</p>
    <div class="tracejado"></div>
    <div class="linha-c"><span>consultoria com rotina pronta</span><span class="pontos"></span><span class="x">✕</span></div>
    <div class="linha-c"><span>curso gravado (parei na aula 3)</span><span class="pontos"></span><span class="x">✕</span></div>
    <div class="linha-c"><span>método que deixava chorar</span><span class="pontos"></span><span class="x">✕</span></div>
    <div class="linha-c"><span>dica milagrosa da internet</span><span class="pontos"></span><span class="x">✕</span></div>
    <div class="tracejado"></div>
    <div class="total"><span>RESULTADO:</span><span>acordando igual</span></div>
    <p class="tchau">obrigada, volte sempre :(</p>
  </div>
  <div class="postit mao">
    <span class="fita"></span>
    e a cada tentativa, ficava mais difícil pedir pra tentar de novo.
  </div>
  {rod(2)}
</section>

<!-- 3 · ELE TEM RAZÃO -->
<section class="slide rosa razao" id="s3">
  <h2 class="grito">Ele tem<br>razão em<br><span>desconfiar.</span></h2>
  <p class="texto">Se vocês já pagaram e não funcionou, é normal ele achar que é mais do mesmo.</p>
  <div class="nota">
    <span class="fita"></span>
    O problema não é ele ter dúvida. É que, até agora, <b>todo o risco ficou com vocês.</b>
  </div>
  <p class="mao fecho">e isso muda aqui.{sublinha}</p>
  {rod(3)}
</section>

<!-- 4 · O RISCO FICA COMIGO -->
<section class="slide amarelo risco" id="s4">
  <p class="mao abre">na Rotina Ideal,</p>
  <h2 class="grito">o risco<br>fica<br>comigo.</h2>
  <div class="selo"><b>100%</b><span>de volta</span></div>
  <div class="nota">
    <span class="fita"></span>
    <p>Se você seguir a rotina por <b>28 dias</b> e o sono do seu bebê não tiver <b>nenhuma melhora</b>, eu devolvo o valor inteiro da mentoria.</p>
    <p class="mao assina">— Pâmela</p>
  </div>
  <p class="miudo">Garantia condicional de devolução da mentoria completa. As regras estão no slide 8.</p>
  {rod(4)}
</section>

<!-- 5 · ANTES × AGORA -->
<section class="slide quadriculado compara" id="s5">
  <p class="mao abre">por que dessa vez é diferente:</p>
  <div class="cab"><span>o que você já tentou</span><span>A Rotina Ideal</span></div>
  <div class="linhas">
    <div class="fila"><div class="antes">rotina pronta, igual pra todo bebê</div><div class="agora">rotina desenhada pro SEU bebê, numa videochamada de 1h</div></div>
    <div class="fila"><div class="antes">um PDF e tchau</div><div class="agora">28 dias de acompanhamento no WhatsApp, 3x por semana</div></div>
    <div class="fila"><div class="antes">deixar o bebê chorar</div><div class="agora">métodos gentis, sem choro e sem trauma</div></div>
    <div class="fila"><div class="antes">pagar e torcer pra dar certo</div><div class="agora">se nada melhorar, o dinheiro volta</div></div>
  </div>
  {rod(5)}
</section>

<!-- 6 · PRO MARIDO -->
<section class="slide tinta marido" id="s6">
  <div class="topo"><span class="mao">esse slide é pra ele:</span><span class="printa">printa e manda {aviao}</span></div>
  <div class="carta">
    <span class="fita"></span>
    <p class="mao oi">Amor, antes de dizer não, lê isso:</p>
    <ul>
      <li>São R$&nbsp;797, ou 6x de R$&nbsp;132,83 sem juros.</li>
      <li>Não é um PDF: são 28 dias de acompanhamento com a mentora.</li>
      <li>Se a gente seguir a rotina e nada melhorar, recebe 100% de volta.</li>
    </ul>
    <p class="grito conclui">Ou o sono melhora,<br><span>ou o dinheiro volta.*</span></p>
    <p class="ast">*seguindo as condições da garantia condicional de devolução</p>
  </div>
  {rod(6)}
</section>

<!-- 7 · CUSTA CARO -->
<section class="slide rosa caro" id="s7">
  <h2 class="grito">Noite mal<br>dormida também<br>custa caro.</h2>
  <p class="texto">Essa conta não chega no cartão. Chega em você:</p>
  <div class="tags"><span>na paciência</span><span>no trabalho</span><span>no humor</span><span>no casamento</span></div>
  <p class="mao fecho">você também merece dormir.{sublinha}</p>
  {rod(7)}
</section>

<!-- 8 · LETRA MIÚDA -->
<section class="slide caderno miuda" id="s8">
  <p class="mao titulo">Pro marido que lê até a letra miúda:</p>
  <div class="itens">
    <p class="item">{check(caixas[0])}vale para a <b>mentoria completa</b> de 28 dias</p>
    <p class="item">{check(caixas[1])}bebê com <b>mais de 4 meses</b> no início</p>
    <p class="item">{check(caixas[2])}checklist da rotina <b>2x por semana</b>, da 2ª à 4ª semana</p>
    <p class="item">{check(caixas[3])}respostas à mentora em <b>até 2 dias úteis</b> (até 3 atrasos são tolerados)</p>
    <p class="item">{check(caixas[4])}pedido por escrito em <b>até 7 dias</b> depois do fim</p>
  </div>
  <div class="postit mao">
    <span class="fita"></span>
    regra clara é o que faz a garantia ser de verdade.
    <small>Condições completas no Termo de Garantia Condicional de Devolução.</small>
  </div>
  {rod(8)}
</section>

<!-- 9 · CTA -->
<section class="slide amarelo cta" id="s9">
  <p class="mao abre">bora resolver essa conversa?</p>
  <h2 class="grito">Comenta<br><span class="palavra">Rotina</span></h2>
  <div class="mao convite">
    <svg width="120" height="110" viewBox="0 0 120 110" style="overflow:visible;flex:none"><path d="M10 8 C 6 60, 40 92, 104 88" fill="none" stroke="#E33B2B" stroke-width="7" stroke-linecap="round"/><path d="M82 66 L106 88 L80 104" fill="none" stroke="#E33B2B" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <span>que eu te mando no direct <b>a mentoria e a garantia</b> explicadinhas</span>
  </div>
  <div class="notas">
    <div class="comenta"><span class="fita"></span>me segue antes, pra mensagem não cair nas solicitações</div>
    <div class="marca">e marca o pai do bebê aqui</div>
  </div>
  <div class="faixa">ou o sono melhora ✱ ou o dinheiro volta ✱ ou o sono melhora ✱ ou o dinheiro volta ✱ ou o sono melhora</div>
  {rod(9)}
</section>
'''

html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Carrossel — Rotina Ideal pro casal</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&family=Caveat:wght@400..700&family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
<style>
{base}
{faixa}
{selo}
{balao}
{css}
</style>
</head>
<body>
{body}
</body>
</html>
'''
(aqui / 'slides.html').write_text(html)

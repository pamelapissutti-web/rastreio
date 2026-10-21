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
ficha = entre('  .ficha {', '  .balao {')

css = r'''
  .tinta .rodape { color: var(--papel); }
  .tinta .rodape .pag { color: var(--amarelo); }
  .amarelo mark::before { background: var(--papel); }

  /* print do WhatsApp colado com fita */
  .print {
    position: relative;
    background: #242626;
    border-radius: 34px;
    box-shadow: 0 30px 50px -24px rgba(0, 0, 0, .75);
  }
  .print img { display: block; width: 100%; border-radius: 34px; }
  .print .fita { z-index: 9; }

  /* ---------- 1 · CAPA ---------- */
  .capa .abre { font-size: 64px; color: var(--amarelo); }
  .capa .print { width: 560px; margin-top: 34px; align-self: center; transform: rotate(-2.5deg); }
  .capa .print .fita { top: -26px; left: 50%; margin-left: -95px; transform: rotate(3deg); }
  .capa .print .alerta {
    position: absolute;
    right: -150px;
    top: 170px;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    background: var(--vermelho);
    color: var(--papel);
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-family: var(--mao);
    font-weight: 700;
    font-size: 52px;
    line-height: .95;
    transform: rotate(14deg);
    box-shadow: 0 14px 24px -14px rgba(0,0,0,.7);
    z-index: 9;
  }
  .capa .grito { margin-top: 56px; font-size: 128px; color: var(--papel); }
  .capa .grito span { display: inline-block; background: var(--amarelo); color: var(--tinta); padding: 12px 24px 0; margin-top: 10px; transform: rotate(-1.5deg); }
  .capa .arrasta { margin-top: 34px; font-size: 54px; color: var(--amarelo); display: flex; align-items: center; gap: 18px; }

  /* ---------- 2 · O QUE ACONTECEU ---------- */
  .resumo .titulo { font-size: 84px; line-height: 60px; color: var(--caneta); padding-top: 28px; }
  .resumo .corpo { margin-top: 60px; display: flex; flex-direction: column; gap: 60px; max-width: 830px; }
  .resumo .corpo p { font-size: 42px; line-height: 60px; font-weight: 500; }
  .resumo .corpo b { font-weight: 800; }
  .resumo .postit {
    margin-top: 40px;
    align-self: flex-end;
    width: 600px;
    background: var(--rosa);
    transform: rotate(2.5deg);
    font-size: 46px;
    z-index: 4;
  }
  .resumo .postit small { display: block; font-family: var(--display); font-weight: 600; font-size: 22px; margin-top: 12px; line-height: 1.3; }
  .resumo .postit .fita { top: -24px; left: 200px; transform: rotate(-3deg); }

  /* ---------- 3 · JÁ TOMOU A PNEUMO 10? ---------- */
  .p10 .abre { font-size: 66px; color: var(--caneta); }
  .p10 .grito { font-size: 160px; margin-top: 18px; }
  .p10 .grito span { color: var(--vermelho); }
  .p10 .nota {
    position: relative;
    margin-top: 56px;
    background: var(--papel);
    padding: 40px 44px;
    transform: rotate(-1deg);
    box-shadow: 0 20px 34px -22px rgba(27,24,48,.6);
  }
  .p10 .nota .fita { top: -24px; right: 90px; transform: rotate(4deg); }
  .p10 .nota p { font-size: 44px; line-height: 1.28; font-weight: 500; }
  .p10 .nota p + p { margin-top: 22px; }
  .p10 .nota b { font-weight: 800; }
  .p10 .fecho { margin-top: 50px; font-size: 64px; color: var(--caneta); }

  /* ---------- 4 · CALENDÁRIO ---------- */
  .calend .abre { font-size: 66px; color: var(--caneta); }
  .calend .grito { font-size: 122px; margin-top: 10px; }
  .linha-tempo { position: relative; margin-top: 50px; display: flex; flex-direction: column; gap: 34px; padding-left: 60px; }
  .linha-tempo::before { content: ''; position: absolute; left: 22px; top: 20px; bottom: 20px; width: 6px; background: var(--tinta); border-radius: 3px; }
  .marco { position: relative; display: flex; align-items: center; gap: 28px; }
  .marco::before { content: ''; position: absolute; left: -52px; width: 34px; height: 34px; border-radius: 50%; background: var(--papel); border: 6px solid var(--tinta); }
  .marco .idade { flex: none; width: 250px; font-family: var(--mao); font-weight: 700; font-size: 72px; color: var(--vermelho); line-height: 1; }
  .marco .vacina { padding: 24px 32px; font-weight: 800; font-size: 50px; box-shadow: 0 14px 22px -16px rgba(27,24,48,.55); }
  .marco .vacina small { display: block; font-weight: 500; font-size: 30px; margin-top: 4px; max-width: 470px; }
  .marco .v20 { background: var(--amarelo); transform: rotate(-1deg); }
  .marco .v10 { background: var(--azul); transform: rotate(1deg); }
  .calend .obs { margin-top: 44px; font-size: 33px; line-height: 1.35; font-weight: 500; max-width: 880px; }
  .calend .obs b { font-weight: 800; }

  /* ---------- 5 · O QUE FAZER ---------- */
  .fazer .grito { font-size: 150px; }
  .fazer .ficha { margin-top: 50px; gap: 36px; }
  .fazer .passo { display: flex; gap: 28px; align-items: flex-start; }
  .fazer .passo .n { flex: none; width: 70px; font-family: var(--mao); font-weight: 700; font-size: 104px; line-height: .8; color: var(--vermelho); }
  .fazer .passo h3 { font-weight: 800; font-size: 44px; line-height: 1.1; }
  .fazer .passo p { font-family: var(--mao); font-weight: 600; font-size: 44px; line-height: 1.05; color: var(--caneta); margin-top: 6px; }

  /* ---------- 6 · É GOLPE? ---------- */
  .golpe .balao {
    align-self: flex-start;
    background: var(--papel);
    border-radius: 36px 36px 36px 8px;
    padding: 24px 40px 26px;
    font-size: 60px;
    color: var(--caneta);
    box-shadow: 0 14px 24px -16px rgba(27,24,48,.5);
    transform: rotate(-1.5deg);
  }
  .golpe .grito { font-size: 230px; margin-top: 44px; color: var(--vermelho); }
  .golpe .texto { margin-top: 30px; font-size: 46px; line-height: 1.3; font-weight: 500; max-width: 880px; }
  .golpe .texto b { font-weight: 800; }
  .golpe .nota {
    position: relative;
    margin-top: 50px;
    background: var(--papel);
    padding: 36px 42px;
    transform: rotate(1deg);
    box-shadow: 0 20px 34px -22px rgba(27,24,48,.6);
  }
  .golpe .nota .fita { top: -24px; right: 80px; transform: rotate(4deg); }
  .golpe .nota .mao { font-size: 52px; color: var(--vermelho); }
  .golpe .nota p + p { font-size: 38px; line-height: 1.3; font-weight: 500; margin-top: 10px; }
  .golpe .nota b { font-weight: 800; }

  /* ---------- 7 · CTA ---------- */
  .cta .grito { font-size: 178px; margin-top: 30px; }
  .cta .sub { font-size: 60px; margin-top: 40px; max-width: 860px; color: var(--tinta); }
  .cta .segue {
    position: relative;
    margin-top: 50px;
    align-self: flex-start;
    background: var(--papel);
    padding: 26px 36px 22px;
    transform: rotate(-2deg);
    font-size: 40px;
    font-weight: 700;
    line-height: 1.2;
    max-width: 760px;
    box-shadow: 0 16px 28px -18px rgba(27,24,48,.6);
  }
  .cta .segue b { color: var(--vermelho); font-weight: 800; }
  .cta .segue .fita { top: -26px; left: 40px; transform: rotate(-6deg); width: 150px; }
  .cta .faixa { position: relative; left: auto; right: auto; margin: auto -150px 0; transform: rotate(1.5deg); }
  .cta .fonte { margin-top: 34px; font-size: 22px; line-height: 1.4; font-weight: 500; max-width: 860px; position: relative; z-index: 5; }
  .cta .rodape { margin-top: 18px; }
'''


def seta(cor):
    return (f'<svg width="150" height="70" viewBox="0 0 150 70" style="overflow:visible;flex:none">'
            f'<path d="M4 44 C 40 14, 90 12, 136 34" fill="none" stroke="{cor}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M112 14 L138 35 L110 52" fill="none" stroke="{cor}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def rod(n):
    return f'<div class="rodape"><span class="arroba">@pamelapissutti</span><span class="pag">{n}/7</span></div>'


body = f'''
<!-- 1 · CAPA -->
<section class="slide tinta capa" id="s1">
  <p class="mao abre">mãe, recebeu essa mensagem do GovBR?</p>
  <div class="print">
    <span class="fita"></span>
    <img src="print-topo.png" alt="">
    <div class="alerta">calma,<br>respira</div>
  </div>
  <h1 class="grito">Não quer dizer que<br><span>a vacina tá atrasada.</span></h1>
  <div class="mao arrasta">arrasta que eu te explico {seta('#FFD93B')}</div>
  {rod(1)}
</section>

<!-- 2 · O QUE ACONTECEU -->
<section class="slide caderno resumo" id="s2">
  <p class="mao titulo">Resumindo o que aconteceu:</p>
  <div class="corpo">
    <p>O canal oficial do GovBR no WhatsApp mandou um aviso dizendo que a criança <b>“ainda não completou o esquema vacinal”</b> e indicando a Pneumo 20.</p>
    <p>Só que o envio foi <mark>em massa</mark>: a mensagem chegou também pra muita família com a <b>caderneta em dia</b>.</p>
    <p>Por isso, a mensagem sozinha <b>não confirma</b> atraso nem dose a mais.</p>
  </div>
  <div class="postit mao">
    <span class="fita"></span>
    O Ministério da Saúde reconheceu os transtornos e vai rever os critérios de envio.
    <small>Segundo a Secretaria de Estado da Saúde de SP, em 20/10/2026.</small>
  </div>
  {rod(2)}
</section>

<!-- 3 · JÁ TOMOU A PNEUMO 10? -->
<section class="slide amarelo p10" id="s3">
  <p class="mao abre">“mas meu filho tomou a Pneumo 10...”</p>
  <h2 class="grito">Se completou,<br><span>tá em dia.</span></h2>
  <div class="nota">
    <span class="fita"></span>
    <p>Se ele completou o esquema com a Pneumo 10 (<b>2 doses + o reforço</b>), o esquema está completo.</p>
    <p>Ele <b>não precisa de dose extra</b> de Pneumo 20 só porque a vacina do calendário mudou.</p>
  </div>
  <p class="mao fecho">a troca de vacina não “zera” o que ele já tomou.</p>
  {rod(3)}
</section>

<!-- 4 · CALENDÁRIO -->
<section class="slide quadriculado calend" id="s4">
  <p class="mao abre">pra quem tá começando agora,</p>
  <h2 class="grito">como ficou<br>o calendário</h2>
  <div class="linha-tempo">
    <div class="marco"><span class="idade">2 meses</span><span class="vacina v20">Pneumo 20<small>1ª dose</small></span></div>
    <div class="marco"><span class="idade">4 meses</span><span class="vacina v10">Pneumo 10<small>2ª dose</small></span></div>
    <div class="marco"><span class="idade">12 meses</span><span class="vacina v20">Pneumo 20<small>reforço, pelo menos 60 dias depois da 2ª dose</small></span></div>
  </div>
  <p class="obs">No SUS, a Pneumo 20 é pra <b>crianças menores de 5 anos que ainda não completaram o esquema</b>. Esse é o esquema de transição, enquanto houver Pneumo 10. Crianças com algumas condições de saúde têm esquema especial: confirme com o pediatra.</p>
  {rod(4)}
</section>

<!-- 5 · O QUE FAZER -->
<section class="slide kraft fazer" id="s5">
  <h2 class="grito">E agora,<br>o que eu faço?</h2>
  <div class="ficha">
    <span class="fita"></span>
    <div class="passo"><span class="n">1</span><div><h3>Confira a caderneta.</h3><p>a de papel ou a digital, no app Meu SUS Digital</p></div></div>
    <div class="passo"><span class="n">2</span><div><h3>Tá tudo em dia?</h3><p>pode desconsiderar a mensagem</p></div></div>
    <div class="passo"><span class="n">3</span><div><h3>Ficou na dúvida?</h3><p>leve a caderneta e um documento da criança na UBS</p></div></div>
    <div class="passo"><span class="n">4</span><div><h3>A equipe confere as doses.</h3><p>e só aplica se faltar alguma, conforme o calendário</p></div></div>
  </div>
  {rod(5)}
</section>

<!-- 6 · É GOLPE? -->
<section class="slide rosa golpe" id="s6">
  <div class="balao mao">“então é golpe?”</div>
  <h2 class="grito">Não.</h2>
  <p class="texto">A mensagem veio do <b>canal oficial do GovBR</b>, com o selo azul de verificado. O problema foi o envio pra todo mundo, sem olhar a caderneta de cada criança.</p>
  <div class="nota">
    <span class="fita"></span>
    <p class="mao">mas fica esperta:</p>
    <p>Vacina no SUS é <b>gratuita</b>. Desconfie de qualquer mensagem que peça pagamento, senha ou código pra vacinar.</p>
  </div>
  {rod(6)}
</section>

<!-- 7 · CTA -->
<section class="slide amarelo cta" id="s7">
  <h2 class="grito">Manda pro<br>grupo das<br>mães.</h2>
  <p class="mao sub">Tem muita mãe preocupada à toa hoje. Esse post pode tirar esse peso dela.</p>
  <div class="segue">
    <span class="fita"></span>
    e <b>me segue</b> pra receber esses avisos explicados, sem pânico
  </div>
  <div class="faixa">sem pânico ✱ confira a caderneta ✱ sem pânico ✱ confira a caderneta ✱ sem pânico</div>
  <p class="fonte">Fontes: Programa Nacional de Imunizações / Ministério da Saúde, Secretaria de Estado da Saúde de São Paulo e Secretarias Municipais de Saúde de Cuiabá e Ubatuba (outubro de 2026). Em caso de dúvida sobre a saúde do seu filho, procure a UBS ou o pediatra.</p>
  {rod(7)}
</section>
'''

html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Carrossel — Mensagem GovBR Pneumo 20</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&family=Caveat:wght@400..700&display=swap" rel="stylesheet">
<style>
{base}
{faixa}
{selo}
{ficha}
{css}
</style>
</head>
<body>
{body}
</body>
</html>
'''
(aqui / 'slides.html').write_text(html)

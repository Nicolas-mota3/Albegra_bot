"""
ÁlgebraBot — Análise Combinatória · 2º Ano Técnico
"""

import tkinter as tk
from tkinter import ttk
from math import factorial
import random, re, unicodedata, threading, time, os, subprocess, sys

# ─── PALETA ───────────────────────────────────────────────────────────────────
C = {
    "bg":     "#0b0d12", "surf":   "#13151d", "surf2":  "#1a1d27",
    "surf3":  "#22263a", "border": "#2a2f45",
    "acc":    "#00e5a0", "acc2":   "#6c8fff",  "acc3":   "#ff6b9d",
    "acc4":   "#ffd166", "txt":    "#e8eaf6",  "txt2":   "#9ca3c0",
    "mut":    "#5a6180", "red":    "#ff5c7c",
}

# ─── VÍDEOS ───────────────────────────────────────────────────────────────────
VIDEOS = [
    {
        "id": "a0GcRAWcoUY",
        "titulo": "Princípio Fundamental da Contagem",
        "topico": "PFC",
        "cor": C["acc"],
        "desc": "Aprenda o PFC — base de toda a Análise Combinatória."
    },
    {
        "id": "m_1RxAZutR4",
        "titulo": "Permutação Simples e com Repetição",
        "topico": "Permutação",
        "cor": C["acc3"],
        "desc": "Anagramas de palavras com letras iguais ou distintas."
    },
    {
        "id": "fvPIb7Vtez4",
        "titulo": "Arranjo Simples",
        "topico": "Arranjo",
        "cor": C["acc2"],
        "desc": "Pódio, cargos e senhas sem repetição."
    },
    {
        "id": "OnRBToRk2gg",
        "titulo": "Combinação Simples",
        "topico": "Combinação",
        "cor": C["acc4"],
        "desc": "Grupos, equipes e diagonais — sem importar a ordem."
    },
    {
        "id": "JiW2Oyjx-CE",
        "titulo": "Revisão Geral de Análise Combinatória",
        "topico": "Revisão",
        "cor": "#a78bfa",
        "desc": "Saiba escolher entre PFC, Arranjo, Combinação e Permutação."
    },
]


def gerar_html_videos():
    cards = ""
    for v in VIDEOS:
        yt_url = f"https://www.youtube.com/watch?v={v['id']}"
        thumb  = f"https://img.youtube.com/vi/{v['id']}/hqdefault.jpg"
        cards += f"""
        <div class="card">
          <div class="tag" style="background:{v['cor']}22;color:{v['cor']};border:1px solid {v['cor']}55">{v['topico']}</div>
          <h3>{v['titulo']}</h3>
          <p>{v['desc']}</p>
          <a class="thumb-link" href="{yt_url}" target="_blank" rel="noopener">
            <div class="thumb-wrap">
              <img src="{thumb}" alt="Thumbnail {v['titulo']}" loading="lazy" onerror="this.style.display='none'">
              <div class="play-btn">
                <svg viewBox="0 0 68 48" width="68" height="48">
                  <path d="M66.52 7.74C65.7 4.65 63.35 2.3 60.26 1.48 54.96 0 34 0 34 0S13.04 0 7.74 1.48C4.65 2.3 2.3 4.65 1.48 7.74 0 13.04 0 24 0 24s0 10.96 1.48 16.26c.82 3.09 3.17 5.44 6.26 6.26C13.04 48 34 48 34 48s20.96 0 26.26-1.48c3.09-.82 5.44-3.17 6.26-6.26C68 34.96 68 24 68 24S68 13.04 66.52 7.74z" fill="#ff0000"/>
                  <path d="M45 24L27 14v20" fill="white"/>
                </svg>
              </div>
              <div class="open-label">Abrir no YouTube ↗</div>
            </div>
          </a>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Videoaulas — ÁlgebraBot</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;600;700&display=swap');
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{
    font-family:'DM Sans',sans-serif;
    background:#0b0d12;color:#e8eaf6;
    min-height:100vh;padding:0;
  }}
  header{{
    background:#13151d;
    border-bottom:1px solid #2a2f45;
    padding:18px 32px;
    display:flex;align-items:center;gap:14px;
    position:sticky;top:0;z-index:100;
  }}
  .logo{{
    width:42px;height:42px;background:#00e5a0;border-radius:10px;
    display:flex;align-items:center;justify-content:center;
    font-family:'Space Mono',monospace;font-size:20px;font-weight:700;
    color:#0b0d12;animation:pulse 3s ease-in-out infinite;flex-shrink:0;
  }}
  @keyframes pulse{{
    0%,100%{{box-shadow:0 0 0 0 rgba(0,229,160,.4)}}
    50%{{box-shadow:0 0 0 10px rgba(0,229,160,0)}}
  }}
  header h1{{font-size:16px;font-weight:700;color:#e8eaf6}}
  header p{{font-size:11px;color:#5a6180;font-family:'Space Mono',monospace}}
  .container{{max-width:1100px;margin:0 auto;padding:32px 24px}}
  .page-title{{
    font-family:'Space Mono',monospace;
    font-size:22px;color:#00e5a0;margin-bottom:6px;
  }}
  .page-sub{{color:#9ca3c0;font-size:14px;margin-bottom:8px}}
  .notice{{
    background:#1a1d27;border:1px solid #2a2f45;border-left:3px solid #ffd166;
    border-radius:8px;padding:10px 16px;font-size:12px;color:#ffd166;
    margin-bottom:28px;
  }}
  .grid{{
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(340px,1fr));
    gap:24px;
  }}
  .card{{
    background:#13151d;border:1px solid #2a2f45;
    border-radius:16px;overflow:hidden;
    transition:transform .3s,border-color .3s,box-shadow .3s;
    animation:card-in .5s cubic-bezier(.34,1.56,.64,1) both;
    padding:16px 18px 18px;
  }}
  .card:nth-child(1){{animation-delay:.05s}}
  .card:nth-child(2){{animation-delay:.10s}}
  .card:nth-child(3){{animation-delay:.15s}}
  .card:nth-child(4){{animation-delay:.20s}}
  .card:nth-child(5){{animation-delay:.25s}}
  @keyframes card-in{{
    from{{opacity:0;transform:translateY(24px) scale(.96)}}
    to  {{opacity:1;transform:translateY(0)   scale(1)}}
  }}
  .card:hover{{
    transform:translateY(-6px);
    border-color:#00e5a0;
    box-shadow:0 16px 48px rgba(0,229,160,.14);
  }}
  .tag{{
    display:inline-block;padding:3px 12px;border-radius:20px;
    font-size:10px;font-family:'Space Mono',monospace;font-weight:700;
    margin-bottom:8px;
  }}
  .card h3{{font-size:14px;font-weight:700;margin-bottom:5px;line-height:1.4}}
  .card p{{font-size:12px;color:#9ca3c0;line-height:1.5;margin-bottom:12px}}

  /* ── Thumbnail clicável ── */
  .thumb-link{{text-decoration:none;display:block}}
  .thumb-wrap{{
    position:relative;width:100%;padding-top:56.25%;
    background:#1a1d27;border-radius:10px;overflow:hidden;
    cursor:pointer;
  }}
  .thumb-wrap img{{
    position:absolute;top:0;left:0;
    width:100%;height:100%;object-fit:cover;
    transition:transform .3s,filter .3s;
    filter:brightness(.85);
  }}
  .thumb-link:hover .thumb-wrap img{{
    transform:scale(1.04);filter:brightness(1);
  }}
  .play-btn{{
    position:absolute;top:50%;left:50%;
    transform:translate(-50%,-50%) scale(1);
    transition:transform .2s;
    filter:drop-shadow(0 4px 16px rgba(0,0,0,.6));
    pointer-events:none;
  }}
  .thumb-link:hover .play-btn{{transform:translate(-50%,-50%) scale(1.12)}}
  .open-label{{
    position:absolute;bottom:10px;right:12px;
    background:rgba(0,0,0,.72);color:#fff;
    font-size:11px;font-family:'Space Mono',monospace;
    padding:4px 10px;border-radius:6px;
    opacity:0;transition:opacity .2s;
    pointer-events:none;
  }}
  .thumb-link:hover .open-label{{opacity:1}}

  /* fallback sem imagem */
  .thumb-wrap.no-img{{
    display:flex;align-items:center;justify-content:center;
    background:linear-gradient(135deg,#1a1d27,#22263a);
  }}
  ::-webkit-scrollbar{{width:6px}}
  ::-webkit-scrollbar-thumb{{background:#2a2f45;border-radius:4px}}
</style>
</head>
<body>
<header>
  <div class="logo">∑</div>
  <div>
    <h1>ÁlgebraBot — Videoaulas</h1>
    <p>Análise Combinatória · 2º Ano Técnico</p>
  </div>
</header>
<div class="container">
  <div class="page-title">🎬 Videoaulas de Análise Combinatória</div>
  <p class="page-sub">Clique em qualquer card para abrir o vídeo no YouTube.</p>
  <div class="notice">
    ⚠️ Os vídeos abrem no YouTube — embeds não funcionam em arquivos locais (file://).
  </div>
  <div class="grid">{cards}</div>
</div>
</body>
</html>"""


# ─── ABRIR JANELA DE VÍDEOS ───────────────────────────────────────────────────
def abrir_videos():
    """Abre a janela de vídeos usando pywebview (navegador embutido real)."""
    try:
        import webview
        html = gerar_html_videos()
        def _run():
            w = webview.create_window(
                "ÁlgebraBot — Videoaulas",
                html=html,
                width=1100,
                height=740,
                resizable=True,
                background_color='#0b0d12',
            )
            webview.start()
        threading.Thread(target=_run, daemon=True).start()
    except ImportError:
        # fallback: abre no navegador padrão
        import webbrowser, tempfile
        html = gerar_html_videos()
        with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as f:
            f.write(html)
            tmp = f.name
        webbrowser.open(f'file://{tmp}')


# ─── MATEMÁTICA ───────────────────────────────────────────────────────────────
def fat(n):   return factorial(n)
def arj(n,p): return factorial(n)//factorial(n-p) if n>=p>=0 else 0
def cmb(n,p): return factorial(n)//(factorial(p)*factorial(n-p)) if n>=p>=0 else 0
def perm_rep(n,*gs):
    d=1
    for g in gs: d*=factorial(g)
    return factorial(n)//d
def arr_rep(n,p): return n**p
def cmb_rep(n,p): return cmb(n+p-1,p)
def fmt(n):   return f"{n:,}".replace(",",".")
def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD",s.lower()) if not unicodedata.combining(c))

# ─── BANCO DE CONHECIMENTO ────────────────────────────────────────────────────
TOPICOS = {
    "pfc":{"titulo":"Princípio Fundamental da Contagem","emoji":"×","cor":C["acc"],
        "resumo":"Multiplica as opções de cada etapa independente.",
        "formula":"Total = n₁ × n₂ × n₃ × ...",
        "quando":"Quando há ETAPAS INDEPENDENTES e você quer o total.",
        "exemplos":[("Cardápio","3 entradas, 5 pratos, 4 sobremesas → 3×5×4 = 60 refeições."),
                    ("Placas","26 letras (3 posições) + 10 dígitos (4 posições) → 26³×10⁴ = 175.760.000 placas."),
                    ("Vestuário","4 calças, 6 camisas, 3 sapatos → 4×6×3 = 72 trajes."),
                    ("Senhas com letras e números","3 letras (A–Z) e 2 dígitos → 26³×10² = 1.757.600 senhas."),
                    ("Rotas","De A→B: 3 estradas. De B→C: 4 estradas → 3×4 = 12 rotas.")],
        "sins":["pfc","principio fundamental","contagem","multiplicacao","etapas","cardapio","traje","vestir","rotas","estradas"]},
    "arranjo":{"titulo":"Arranjo Simples","emoji":"A","cor":C["acc2"],
        "resumo":"Selecionar P de N elementos. A ORDEM IMPORTA!",
        "formula":"A(n,p) = n! / (n−p)!",
        "quando":"Quando a ORDEM dos elementos escolhidos faz diferença (cargos, pódio, senhas).",
        "exemplos":[("Pódio","10 atletas, 1º/2º/3º → A(10,3) = 720 formas."),
                    ("Presidente e Vice","5 candidatos → A(5,2) = 20 maneiras."),
                    ("Senha de 3 dígitos distintos","Dígitos 1–9 → A(9,3) = 504 senhas."),
                    ("Medalhas","8 corredores, ouro/prata/bronze → A(8,3) = 336 maneiras."),
                    ("Código de acesso","6 letras distintas, escolhe 3 → A(6,3) = 120 códigos.")],
        "sins":["arranjo","arranjos","podio","pódio","cargo","presidente","vice","secretario","senha sem repeticao","medalha","codigo"]},
    "arranjo_rep":{"titulo":"Arranjo com Repetição","emoji":"Aᵣ","cor":"#a78bfa",
        "resumo":"Selecionar P de N PODENDO REPETIR. Ordem importa!",
        "formula":"AR(n,p) = nᵖ",
        "quando":"Cada posição pode receber qualquer elemento (inclusive repetido).",
        "exemplos":[("Senha com repetição","4 dígitos (0–9) → 10⁴ = 10.000 senhas."),
                    ("Placas de 3 letras","26 letras, repetição → 26³ = 17.576 placas."),
                    ("Bits","2 valores (0/1), 8 posições → 2⁸ = 256 combinações."),
                    ("PIN bancário","4 dígitos com repetição → 10⁴ = 10.000 PINs.")],
        "sins":["arranjo com repeticao","arranjo repetido","ar(","senha com repeticao","pin","bits"]},
    "combinacao":{"titulo":"Combinação Simples","emoji":"C","cor":C["acc4"],
        "resumo":"Selecionar P de N. A ORDEM NÃO IMPORTA!",
        "formula":"C(n,p) = n! / (p! × (n−p)!)",
        "quando":"Quando forma GRUPOS/EQUIPES e a ordem não importa.",
        "exemplos":[("Equipe","10 pessoas, time de 3 → C(10,3) = 120 times."),
                    ("Sorvete","6 sabores, escolhe 2 → C(6,2) = 15 opções."),
                    ("Mega-Sena","60 números, marca 6 → C(60,6) = 50.063.860 apostas!"),
                    ("Diagonais de polígono","Hexágono: C(6,2)−6 = 9 diagonais."),
                    ("Handshake","8 pessoas → C(8,2) = 28 cumprimentos.")],
        "sins":["combinacao","combinacoes","combinação","combinações","grupo","equipe","time","comissao","c(","diagonal","handshake","cumprimento","subconjunto"]},
    "combinacao_rep":{"titulo":"Combinação com Repetição","emoji":"Cᵣ","cor":"#f472b6",
        "resumo":"Selecionar P de N PODENDO REPETIR. Ordem não importa!",
        "formula":"CR(n,p) = C(n+p−1, p)",
        "quando":"Escolher podendo repetir, sem importar a ordem.",
        "exemplos":[("Sorvete c/ repetição","3 sabores, 2 bolas → CR(3,2) = C(4,2) = 6 opções."),
                    ("Frutas repetidas","4 tipos de fruta, escolher 3 → CR(4,3) = 20 cestas.")],
        "sins":["combinacao com repeticao","combinacao repetida","cr(","fruta repetida","bola de sorvete"]},
    "permutacao":{"titulo":"Permutação Simples","emoji":"P","cor":C["acc3"],
        "resumo":"Ordenar TODOS os N elementos distintos.",
        "formula":"P(n) = n!",
        "quando":"Quando usa TODOS os elementos e só troca a ordem.",
        "exemplos":[("Anagrama","AMOR (4 letras distintas) → P(4) = 24 anagramas."),
                    ("Fila","6 pessoas numa fila → P(6) = 720 filas."),
                    ("Prateleira","5 livros distintos → P(5) = 120 maneiras.")],
        "sins":["permutacao","permutacoes","permutação","permutações","permutar","anagrama","fila","prateleira","agenda","corrida"]},
    "permutacao_rep":{"titulo":"Permutação com Repetição","emoji":"Pᵣ","cor":"#34d399",
        "resumo":"Ordenar N elementos com elementos REPETIDOS.",
        "formula":"PR(n; k₁,k₂,...) = n! / (k₁! × k₂! × ...)",
        "quando":"Anagramas de palavras com letras repetidas.",
        "exemplos":[("BANANA","B×1, A×3, N×2 → 6!/(1!×3!×2!) = 60 anagramas."),
                    ("ARARA","A×3, R×2 → 5!/(3!×2!) = 10 anagramas."),
                    ("BORBOLETA","B×2,O×2 → 8!/(2!×2!) = 10.080.")],
        "sins":["permutacao com repeticao","permutacao repetida","pr(","anagrama repetido","banana","arara","matematica","borboleta"]},
}

QUESTOES = [
    {"q":"De quantas formas podemos organizar as letras da palavra ROMA?",
     "r":fat(4),"res":"ROMA tem 4 letras distintas → Permutação Simples.\nP(4) = 4! = 24 anagramas."},
    {"q":"De quantas formas 5 livros distintos podem ser dispostos numa prateleira?",
     "r":fat(5),"res":"Todos os elementos, troca de ordem → Permutação Simples.\nP(5) = 5! = 120 formas."},
    {"q":"6 pessoas entram em fila. De quantas maneiras distintas podem se organizar?",
     "r":fat(6),"res":"Todos em fila → Permutação Simples.\nP(6) = 6! = 720 maneiras."},
    {"q":"Quantos anagramas tem a palavra BANANA?",
     "r":perm_rep(6,1,3,2),"res":"B×1,A×3,N×2 → PR = 6!/(1!×3!×2!) = 60 anagramas."},
    {"q":"Quantos anagramas tem a palavra ARARA?",
     "r":perm_rep(5,3,2),"res":"A×3, R×2 → PR = 5!/(3!×2!) = 10 anagramas."},
    {"q":"8 candidatos concorrem a presidente, vice e secretário. Quantas diretorias?",
     "r":arj(8,3),"res":"Cargos distintos = ordem importa → A(8,3) = 336 diretorias."},
    {"q":"10 atletas disputam corrida. De quantas formas podemos ter ouro, prata e bronze?",
     "r":arj(10,3),"res":"Pódio → Arranjo Simples.\nA(10,3) = 720 formas."},
    {"q":"Senha de 3 dígitos (0–9) com repetição. Quantas senhas?",
     "r":arr_rep(10,3),"res":"Com repetição, ordem importa → AR(10,3) = 10³ = 1.000 senhas."},
    {"q":"Uma comissão de 3 alunos de uma turma de 12. De quantas formas?",
     "r":cmb(12,3),"res":"Comissão = grupo sem ordem → C(12,3) = 220 comissões."},
    {"q":"10 pontos não colineares. Quantos triângulos distintos podemos formar?",
     "r":cmb(10,3),"res":"Triângulo = 3 pontos sem ordem → C(10,3) = 120 triângulos."},
    {"q":"Cardápio: 4 entradas e 6 pratos principais. Quantas refeições?",
     "r":4*6,"res":"Etapas independentes → PFC.\n4 × 6 = 24 refeições."},
    {"q":"Roupa: 3 calças, 5 camisas, 2 sapatos. Quantos trajes completos?",
     "r":3*5*2,"res":"PFC.\n3 × 5 × 2 = 30 trajes."},
    {"q":"Quantas sequências de 4 bits (0 ou 1) existem?",
     "r":arr_rep(2,4),"res":"AR(2,4) = 2⁴ = 16 sequências."},
    {"q":"Quantas diagonais tem um polígono de 8 lados?",
     "r":cmb(8,2)-8,"res":"C(8,2) − 8 = 28 − 8 = 20 diagonais."},
    {"q":"9 pessoas num grupo. Quantos apertos de mão ao todo?",
     "r":cmb(9,2),"res":"Par sem ordem → C(9,2) = 36 apertos de mão."},
]

CONCEITOS = {
    "diferenca arranjo combinacao": (
        "╔ ⚖️  Arranjo vs Combinação\n║\n"
        "║  A diferença fundamental é: A ORDEM IMPORTA?\n║\n"
        "║  📌 ARRANJO — ordem IMPORTA\n"
        "║     Ex: Presidente e Vice de 5 candidatos\n"
        "║     (A→B) ≠ (B→A) → A(5,2) = 20 pares\n║\n"
        "║  📌 COMBINAÇÃO — ordem NÃO importa\n"
        "║     Ex: Equipe de 2 de 5 pessoas\n"
        "║     {A,B} = {B,A} → C(5,2) = 10 equipes\n║\n"
        "║  💡 cargos/pódio/senha → Arranjo\n"
        "║     grupo/equipe/comissão → Combinação\n╚"
    ),
    "diferenca permutacao arranjo": (
        "╔ ⚖️  Permutação vs Arranjo\n║\n"
        "║  📌 PERMUTAÇÃO — usa TODOS os elementos\n"
        "║     P(n) = n!\n"
        "║     Ex: 4 livros → P(4) = 24\n║\n"
        "║  📌 ARRANJO — usa PARTE dos elementos\n"
        "║     A(n,p) = n!/(n-p)!\n"
        "║     Ex: 3 cargos de 10 → A(10,3) = 720\n║\n"
        "║  💡 todos → Permutação / parte → Arranjo\n╚"
    ),
    "quando usar permutacao": (
        "╔ 📖  Quando usar Permutação?\n║\n"
        "║  ✔ Usa TODOS os elementos\n"
        "║  ✔ A ORDEM importa\n"
        "║  ✔ Sem repetição\n║\n"
        "║  Exemplos: anagramas, fila, prateleira\n"
        "║  Fórmula: P(n) = n!\n╚"
    ),
    "quando usar combinacao": (
        "╔ 📖  Quando usar Combinação?\n║\n"
        "║  ✔ Escolhe PARTE dos elementos\n"
        "║  ✔ A ORDEM NÃO importa\n"
        "║  ✔ Grupos, equipes, comissões\n║\n"
        "║  Exemplos: times, sorvete, diagonais\n"
        "║  Fórmula: C(n,p) = n! / (p! × (n−p)!)\n╚"
    ),
    "quando usar arranjo": (
        "╔ 📖  Quando usar Arranjo?\n║\n"
        "║  ✔ Escolhe PARTE dos elementos\n"
        "║  ✔ A ORDEM IMPORTA\n"
        "║  ✔ Posições/cargos distintos\n║\n"
        "║  Exemplos: pódio, presidente/vice, senhas\n"
        "║  Fórmula: A(n,p) = n! / (n−p)!\n╚"
    ),
    "o que e fatorial": (
        "╔ 📖  O que é Fatorial?\n║\n"
        "║  n! = n × (n−1) × ... × 2 × 1\n"
        "║  Por definição: 0! = 1\n║\n"
        "║  3!=6  4!=24  5!=120  6!=720  10!=3.628.800\n║\n"
        "║  É a base de toda a Análise Combinatória!\n╚"
    ),
    "o que e diagonal": (
        "╔ 📖  Diagonais de Polígonos\n║\n"
        "║  Fórmula: D = C(n,2) − n\n║\n"
        "║  Quadrado(4): 2  Pentágono(5): 5\n"
        "║  Hexágono(6): 9  Octógono(8): 20\n╚"
    ),
}

estado = {"tema": None, "questao": None}

def anagrama_resp(palavra):
    p = palavra.upper()
    freq = {}
    for c in p: freq[c] = freq.get(c,0)+1
    n = len(p)
    r = perm_rep(n, *freq.values())
    reps = {k:v for k,v in freq.items() if v>1}
    if not reps:
        return (f"✦ Anagramas de {p}\n"
                f"  Letras todas distintas → Permutação Simples\n"
                f"  P({n}) = {n}! = {fmt(fat(n))} anagramas")
    fstr = ", ".join(f"{k}×{v}" for k,v in freq.items())
    den  = " × ".join(f"{v}!" for v in freq.values())
    return (f"✦ Anagramas de {p}\n"
            f"  Letras: {fstr}\n"
            f"  Repetições → Permutação com Repetição\n"
            f"  PR = {n}!/({den})\n"
            f"  PR = {fmt(r)} anagramas")

def resolver_diagonal(n_lados):
    d = cmb(n_lados,2) - n_lados
    return (f"✦ Diagonais de polígono com {n_lados} lados\n"
            f"  Fórmula: C(n,2) − n\n"
            f"  C({n_lados},2) − {n_lados} = {cmb(n_lados,2)} − {n_lados} = {d} diagonais")

def local_resp(q):
    p = norm(q)
    nums = [int(x) for x in re.findall(r"\d+", p)]

    for chave, resp in CONCEITOS.items():
        palavras = chave.split()
        if all(w in p for w in palavras):
            return resp

    m = re.search(r"(\d+)\s*!", p)
    if m:
        n = int(m.group(1))
        return f"✦ Fatorial\n  {n}! = {fmt(fat(n))}"

    m = re.search(r"anagrama[s]?\s+(?:d[aeo]\s+)?(?:palavra\s+)?([A-Za-zÁÉÍÓÚÂÊÎÔÛÃÕÇáéíóúâêîôûãõç]{3,})", q, re.I)
    if m: return anagrama_resp(m.group(1))

    m = re.search(r"diagonal.*?(\d+)\s*lado", p)
    if not m: m = re.search(r"(\d+)\s*lado.*?diagonal", p)
    if not m: m = re.search(r"poligono\s+(?:de\s+)?(\d+)", p)
    if m and "diagonal" in p:
        return resolver_diagonal(int(m.group(1)))

    m = re.search(r"(\d+)\s*pessoa[s]?.*?(?:aperto|cumprimenta|handshake)", p)
    if not m: m = re.search(r"(?:aperto|cumprimenta|handshake).*?(\d+)\s*pessoa[s]?", p)
    if m:
        n = int(m.group(1))
        return (f"✦ Apertos de mão entre {n} pessoas\n"
                f"  Par sem ordem → Combinação\n"
                f"  C({n},2) = {fmt(cmb(n,2))} apertos de mão")

    for pat, func in [
        (r"\bA\((\d+)\s*,\s*(\d+)\)", lambda a,b: f"Arranjo A({a},{b}) = {fmt(arj(a,b))}"),
        (r"\bC\((\d+)\s*,\s*(\d+)\)", lambda a,b: f"Combinação C({a},{b}) = {fmt(cmb(a,b))}"),
        (r"\bP\((\d+)\)",             lambda a,_=None: f"Permutação P({a}) = {fmt(fat(a))}"),
        (r"\bAR\((\d+)\s*,\s*(\d+)\)",lambda a,b: f"Arr. c/ Rep. AR({a},{b}) = {fmt(arr_rep(a,b))}"),
        (r"\bCR\((\d+)\s*,\s*(\d+)\)",lambda a,b: f"Comb. c/ Rep. CR({a},{b}) = {fmt(cmb_rep(a,b))}"),
    ]:
        m = re.search(pat, q, re.I)
        if m:
            gs = [int(x) for x in m.groups() if x]
            return "✦ " + func(*gs)

    for k, d in TOPICOS.items():
        if any(norm(s) in p for s in d["sins"]):
            return _resp_topico(k)

    if len(nums) >= 2:
        n, k2 = nums[0], nums[1]
        if any(w in p for w in ["podio","pódio","ouro","prata","bronze","cargo","presidente","vice","secretario"]):
            if n > k2:
                return (f"✦ Arranjo Simples — Cargos/Pódio\n"
                        f"  Ordem importa → A({n},{k2})\n"
                        f"  A({n},{k2}) = {fmt(arj(n,k2))}")
        if any(w in p for w in ["senha","codigo","código","pin","placa"]):
            if "repeticao" in p or "repetir" in p:
                return (f"✦ Arranjo com Repetição — Senha\n"
                        f"  AR({n},{k2}) = {n}^{k2} = {fmt(arr_rep(n,k2))}")
            else:
                return (f"✦ Arranjo Simples — Senha\n"
                        f"  A({n},{k2}) = {fmt(arj(n,k2))}")
        if any(w in p for w in ["equipe","time","grupo","comissao","comissão"]):
            if n > k2:
                return (f"✦ Combinação Simples — Grupo\n"
                        f"  C({n},{k2}) = {fmt(cmb(n,k2))}")

    return None

def _resp_topico(k):
    d = TOPICOS[k]
    exs = "\n".join(f"  • {n}: {desc}" for n,desc in d["exemplos"])
    return (f"╔ {d['emoji']}  {d['titulo']}\n"
            f"║ {d['resumo']}\n"
            f"║ Fórmula: {d['formula']}\n"
            f"║ Quando usar: {d['quando']}\n║\n"
            f"║ Exemplos:\n{exs}\n╚")


# ─── INTERFACE ────────────────────────────────────────────────────────────────
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ÁlgebraBot  ✦  Análise Combinatória")
        self.geometry("1020x680")
        self.minsize(760,520)
        self.configure(bg=C["bg"])
        self._build_header()
        body = tk.Frame(self, bg=C["bg"])
        body.pack(fill="both", expand=True)
        self._build_sidebar(body)
        self._build_chat(body)
        self._boas_vindas()

    def _build_header(self):
        h = tk.Frame(self, bg=C["surf"], height=56)
        h.pack(fill="x"); h.pack_propagate(False)
        logo = tk.Frame(h, bg=C["acc"], width=44, height=44)
        logo.pack(side="left", padx=14, pady=6); logo.pack_propagate(False)
        tk.Label(logo, text="∑", font=("Courier New",18,"bold"),
                 bg=C["acc"], fg=C["bg"]).place(relx=.5,rely=.5,anchor="center")
        info = tk.Frame(h, bg=C["surf"]); info.pack(side="left", pady=10)
        tk.Label(info, text="ÁlgebraBot",
                 font=("Helvetica",14,"bold"), bg=C["surf"], fg=C["txt"]).pack(anchor="w")
        tk.Label(info, text="Análise Combinatória · 2º Ano Técnico",
                 font=("Helvetica",9), bg=C["surf"], fg=C["mut"]).pack(anchor="w")

        vid_btn = tk.Button(h, text="🎬  Assistir Videoaulas",
                            font=("Helvetica",10,"bold"),
                            bg=C["acc3"], fg="white",
                            activebackground="#e0557f",
                            activeforeground="white",
                            relief="flat", cursor="hand2",
                            padx=14, pady=6,
                            command=self._on_videos)
        vid_btn.pack(side="right", padx=14, pady=10)

        tk.Frame(self, bg=C["border"], height=1).pack(fill="x")

    def _on_videos(self):
        self._inserir("ÁlgebraBot ∑",
            "🎬 Abrindo janela de videoaulas...\n"
            "Clique nas thumbnails para abrir cada vídeo no YouTube!", "bot")
        threading.Thread(target=abrir_videos, daemon=True).start()

    def _build_sidebar(self, parent):
        sb = tk.Frame(parent, bg=C["surf"], width=215)
        sb.pack(side="left", fill="y"); sb.pack_propagate(False)
        tk.Frame(parent, bg=C["border"], width=1).pack(side="left", fill="y")

        def sec(t):
            tk.Label(sb, text=t, font=("Courier New",8,"bold"), bg=C["surf"],
                     fg=C["mut"], anchor="w", padx=16).pack(fill="x", pady=(14,2))

        def btn(em, titulo, cmd, cor=C["mut"]):
            f = tk.Frame(sb, bg=C["surf"], cursor="hand2"); f.pack(fill="x")
            e = tk.Label(f, text=em, font=("Courier New",10,"bold"),
                         bg=C["surf"], fg=cor, width=3)
            e.pack(side="left", padx=(12,0), pady=6)
            l = tk.Label(f, text=titulo, font=("Helvetica",11),
                         bg=C["surf"], fg=C["txt"], anchor="w")
            l.pack(side="left", fill="x", expand=True, padx=(4,12))
            for w in (f,e,l):
                w.bind("<Button-1>", lambda ev,c=cmd: self._enviar(c))
                w.bind("<Enter>", lambda ev,ws=(f,e,l): [x.config(bg=C["surf3"]) for x in ws] or l.config(fg=C["acc"]))
                w.bind("<Leave>", lambda ev,ws=(f,e,l): [x.config(bg=C["surf"]) for x in ws] or l.config(fg=C["txt"]))

        sec("TÓPICOS")
        btn("×","PFC","Explique PFC",C["acc"])
        btn("A","Arranjo Simples","Explique arranjo",C["acc2"])
        btn("C","Combinação","Explique combinação",C["acc4"])
        btn("P","Permutação","Explique permutação",C["acc3"])
        btn("Aᵣ","Arr. c/ Repetição","Explique arranjo com repetição","#a78bfa")
        btn("Pᵣ","Perm. c/ Repetição","Explique permutação com repetição","#34d399")
        sec("PRATICAR")
        btn("📝","Nova Questão","nova questão",C["acc4"])
        btn("✅","Ver Gabarito","gabarito",C["acc"])
        btn("⚖️","Arranjo vs Combinação","qual a diferença entre arranjo e combinação",C["acc2"])
        btn("⚖️","Perm. vs Arranjo","qual a diferença entre permutação e arranjo",C["acc3"])
        sec("CONCEITOS")
        btn("?","Quando usar Permutação","quando usar permutacao",C["mut"])
        btn("?","Quando usar Combinação","quando usar combinacao",C["mut"])
        btn("?","O que é Fatorial","o que e fatorial",C["mut"])
        btn("📐","Diagonais de polígono","o que e diagonal",C["mut"])
        sec("AÇÕES")
        btn("🎬","Videoaulas","__videos__",C["acc3"])
        btn("📚","Mais exemplos","mais exemplos",C["mut"])
        btn("?","Ajuda","ajuda",C["mut"])
        btn("🧹","Limpar chat","__clear__",C["mut"])
        tk.Frame(sb, bg=C["border"], height=1).pack(fill="x", pady=6, padx=12)
        self._build_calc(sb)

    def _build_calc(self, parent):
        tk.Label(parent, text="CALCULADORA", font=("Courier New",8,"bold"),
                 bg=C["surf"], fg=C["mut"], anchor="w", padx=16).pack(fill="x", pady=(4,2))
        frame = tk.Frame(parent, bg=C["surf2"], padx=12, pady=10)
        frame.pack(fill="x", padx=10, pady=(0,10))
        self.calc_op = tk.StringVar(value="Arranjo")
        tipos = ["Arranjo","Combinação","Permutação","Arr.Rep","Comb.Rep","Fatorial"]
        style = ttk.Style(); style.theme_use("clam")
        style.configure("D.TCombobox",
                        fieldbackground=C["bg"], background=C["surf3"],
                        foreground=C["acc"], selectbackground=C["surf3"],
                        selectforeground=C["acc"], arrowcolor=C["acc"],
                        bordercolor=C["border"], lightcolor=C["border"], darkcolor=C["border"])
        style.map("D.TCombobox",
                  fieldbackground=[("readonly",C["bg"])],
                  foreground=[("readonly",C["acc"])],
                  selectbackground=[("readonly",C["surf3"])],
                  selectforeground=[("readonly",C["acc"])])
        cb = ttk.Combobox(frame, textvariable=self.calc_op, values=tipos,
                          state="readonly", font=("Helvetica",10,"bold"), style="D.TCombobox")
        cb.pack(fill="x", pady=(0,8))
        cb.bind("<<ComboboxSelected>>", self._tog_calc)
        row = tk.Frame(frame, bg=C["surf2"]); row.pack(fill="x", pady=(0,4))
        col_n = tk.Frame(row, bg=C["surf2"])
        col_n.pack(side="left", fill="x", expand=True, padx=(0,4))
        tk.Label(col_n, text="n", font=("Courier New",9,"bold"),
                 bg=C["surf2"], fg=C["acc2"]).pack(anchor="w")
        self.en_n = tk.Entry(col_n, font=("Helvetica",12,"bold"), width=5,
                             bg=C["bg"], fg=C["txt"], insertbackground=C["acc"],
                             relief="flat", bd=4, justify="center")
        self.en_n.pack(fill="x")
        col_p = tk.Frame(row, bg=C["surf2"])
        col_p.pack(side="left", fill="x", expand=True)
        self.lbl_p = tk.Label(col_p, text="p", font=("Courier New",9,"bold"),
                              bg=C["surf2"], fg=C["acc2"])
        self.lbl_p.pack(anchor="w")
        self.en_p = tk.Entry(col_p, font=("Helvetica",12,"bold"), width=5,
                             bg=C["bg"], fg=C["txt"], insertbackground=C["acc"],
                             relief="flat", bd=4, justify="center")
        self.en_p.pack(fill="x")
        tk.Button(frame, text="= Calcular", font=("Courier New",9,"bold"),
                  bg=C["acc"], fg=C["bg"], activebackground="#00c98a",
                  activeforeground=C["bg"], relief="flat", cursor="hand2",
                  command=self._calc_run).pack(fill="x", pady=(8,4))
        self.calc_res = tk.Label(frame, text="", font=("Courier New",11,"bold"),
                                 bg=C["surf2"], fg=C["acc"], wraplength=170)
        self.calc_res.pack()

    def _tog_calc(self, _=None):
        op = self.calc_op.get()
        needs = op not in ("Permutação","Fatorial")
        self.en_n.delete(0,"end"); self.en_p.delete(0,"end")
        self.calc_res.config(text="")
        if needs:
            self.en_p.config(state="normal", bg=C["bg"], fg=C["txt"])
            self.lbl_p.config(fg=C["acc2"])
        else:
            self.en_p.config(state="disabled", bg=C["surf3"], fg=C["mut"])
            self.lbl_p.config(fg=C["mut"])

    def _calc_run(self):
        op = self.calc_op.get()
        nv, pv = self.en_n.get().strip(), self.en_p.get().strip()
        try:
            n = int(nv) if nv else None
            p = int(pv) if pv else None
            if n is None: self.calc_res.config(text="Informe n!",fg=C["red"]); return
            if op=="Arranjo":
                if p is None: self.calc_res.config(text="Informe p!",fg=C["red"]); return
                self.calc_res.config(text=f"A({n},{p}) =\n{fmt(arj(n,p))}",fg=C["acc2"])
            elif op=="Combinação":
                if p is None: self.calc_res.config(text="Informe p!",fg=C["red"]); return
                self.calc_res.config(text=f"C({n},{p}) =\n{fmt(cmb(n,p))}",fg=C["acc4"])
            elif op=="Permutação":
                self.calc_res.config(text=f"P({n}) =\n{fmt(fat(n))}",fg=C["acc3"])
            elif op=="Arr.Rep":
                if p is None: self.calc_res.config(text="Informe p!",fg=C["red"]); return
                self.calc_res.config(text=f"AR({n},{p}) =\n{fmt(arr_rep(n,p))}",fg="#a78bfa")
            elif op=="Comb.Rep":
                if p is None: self.calc_res.config(text="Informe p!",fg=C["red"]); return
                self.calc_res.config(text=f"CR({n},{p}) =\n{fmt(cmb_rep(n,p))}",fg="#f472b6")
            elif op=="Fatorial":
                self.calc_res.config(text=f"{n}! =\n{fmt(fat(n))}",fg=C["acc"])
        except: self.calc_res.config(text="Valor inválido!",fg=C["red"])

    def _build_chat(self, parent):
        cf = tk.Frame(parent, bg=C["bg"]); cf.pack(side="left", fill="both", expand=True)
        mf = tk.Frame(cf, bg=C["bg"]); mf.pack(fill="both", expand=True)
        sb = tk.Scrollbar(mf, bg=C["surf"], troughcolor=C["bg"], width=6, relief="flat")
        sb.pack(side="right", fill="y")
        self.chat = tk.Text(mf, state="disabled", wrap="word", font=("Helvetica",12),
                            bg=C["bg"], fg=C["txt"], bd=0, padx=18, pady=14,
                            spacing1=2, spacing3=4, yscrollcommand=sb.set,
                            cursor="arrow", relief="flat", selectbackground=C["surf3"])
        self.chat.pack(fill="both", expand=True); sb.config(command=self.chat.yview)
        self.chat.tag_config("bn",  foreground=C["acc"],  font=("Courier New",9,"bold"))
        self.chat.tag_config("bm",  foreground=C["txt"],  font=("Helvetica",12), lmargin1=10, lmargin2=10)
        self.chat.tag_config("bf",  foreground=C["acc"],  font=("Courier New",12,"bold"), lmargin1=10, lmargin2=10)
        self.chat.tag_config("bi",  foreground=C["acc4"], font=("Helvetica",12,"italic"), lmargin1=10, lmargin2=10)
        self.chat.tag_config("un",  foreground=C["acc3"], font=("Courier New",9,"bold"))
        self.chat.tag_config("um",  foreground=C["txt"],  font=("Helvetica",12), lmargin1=10, lmargin2=10)
        self.chat.tag_config("ok",  foreground=C["acc"],  font=("Helvetica",12,"bold"), lmargin1=10, lmargin2=10)
        self.chat.tag_config("err", foreground=C["red"],  font=("Helvetica",12), lmargin1=10, lmargin2=10)
        tk.Frame(cf, bg=C["border"], height=1).pack(fill="x")
        ib = tk.Frame(cf, bg=C["surf"], pady=10, padx=10); ib.pack(fill="x")
        self.entry = tk.Entry(ib, font=("Helvetica",13), bg=C["surf2"], fg=C["txt"],
                              insertbackground=C["acc"], relief="flat", bd=0)
        self.entry.pack(side="left", fill="x", expand=True, ipady=10, padx=(8,10))
        self.entry.bind("<Return>", self._on_enter); self.entry.focus()
        self.send_btn = tk.Button(ib, text="Enviar ➤", font=("Helvetica",10,"bold"),
                                  bg=C["acc"], fg=C["bg"], activebackground="#00c98a",
                                  activeforeground=C["bg"], relief="flat", cursor="hand2",
                                  padx=14, pady=10, command=self._on_enter)
        self.send_btn.pack(side="right")

    def _inserir(self, nome, texto, tipo):
        self.chat.config(state="normal")
        nome_tag = {"bot":"bn","user":"un"}.get(tipo,"bn")
        if nome:
            self.chat.insert("end", f"  {nome}\n", nome_tag)
        for linha in texto.split("\n"):
            if tipo == "user":
                tag = "um"
            elif "=" in linha and any(c.isdigit() for c in linha):
                tag = "bf"
            elif "✅" in linha or "🎉" in linha:
                tag = "ok"
            elif "❌" in linha or "⚠️" in linha:
                tag = "err"
            else:
                tag = "bm"
            self.chat.insert("end", f"   {linha}\n", tag)
        self.chat.insert("end", "\n")
        self.chat.config(state="disabled"); self.chat.see("end")

    def _boas_vindas(self):
        self._inserir("ÁlgebraBot ∑",
            "Olá! Sou o ÁlgebraBot  — especialista em Análise Combinatória.\n\n"
            "Posso:\n"
            "  • Explicar PFC, Arranjo, Combinação, Permutação (e variações)\n"
            "  • Resolver questões em linguagem natural\n"
            "  • Gerar questões para praticar\n"
            "  • Explicar a diferença entre os conceitos\n\n"
            "🎬 Clique em 'Assistir Videoaulas' (canto superior direito)\n"
            "   para abrir os 5 vídeos — clique na thumbnail para assistir!\n\n"
            "Exemplos:\n"
            "  → 'Quantos anagramas tem BANANA?'\n"
            "  → 'A(10,3)' / 'C(6,2)' / 'P(5)'\n"
            "  → 'Diagonais de polígono de 8 lados'\n"
            "  → 'Nova questão'","bot")

    def _enviar(self, txt):
        self.entry.delete(0,"end"); self.entry.insert(0,txt); self._on_enter()

    def _on_enter(self, _=None):
        txt = self.entry.get().strip()
        if not txt: return
        self.entry.delete(0,"end")

        if txt == "__clear__":
            self.chat.config(state="normal"); self.chat.delete("1.0","end")
            self.chat.config(state="disabled")
            estado["questao"] = None
            self._boas_vindas(); return

        if txt == "__videos__":
            self._on_videos(); return

        self._inserir("Você", txt, "user")
        self.send_btn.config(state="disabled")

        def _processar():
            p = norm(txt)

            q_atual = estado.get("questao")
            if q_atual and re.search(r"\d+", txt):
                nums = [int(x) for x in re.findall(r"\d+", norm(txt))]
                if nums:
                    if nums[-1] == q_atual["r"]:
                        estado["questao"] = None
                        msg = (f"🎉 CORRETO! Parabéns!\n\n"
                               f"Resposta: {fmt(q_atual['r'])}\n\n"
                               f"{q_atual['res']}\n\n"
                               f"Digite 'nova questão' para continuar!")
                    else:
                        msg = (f"❌ Não foi dessa vez. Você respondeu {fmt(nums[-1])}.\n"
                               f"Dica: pense se a ordem importa ou não.\n"
                               f"(Digite 'gabarito' para ver a resolução)")
                    self.after(0, lambda m=msg: self._inserir("ÁlgebraBot ∑", m, "bot"))
                    self.after(0, lambda: self.send_btn.config(state="normal"))
                    return

            if any(x in p for x in ["gabarito","solucao","solução"]):
                if estado.get("questao"):
                    q = estado["questao"]
                    msg = (f"╔ ✅ GABARITO\n║\n║ {q['q']}\n║\n"
                           f"║ {q['res']}\n║\n╚ Resposta: {fmt(q['r'])}")
                else:
                    msg = "Não há questão aberta. Digite 'nova questão'!"
                self.after(0, lambda m=msg: self._inserir("ÁlgebraBot ∑", m, "bot"))
                self.after(0, lambda: self.send_btn.config(state="normal"))
                return

            if any(x in p for x in ["nova questao","nova questão","questao","questão",
                                      "exercicio","exercício","treinar","praticar","desafio"]):
                q = random.choice(QUESTOES)
                estado["questao"] = q
                msg = (f"╔ 📝 QUESTÃO\n║\n║  {q['q']}\n║\n"
                       f"╚ Qual é a sua resposta? (ou 'gabarito' para a solução)")
                self.after(0, lambda m=msg: self._inserir("ÁlgebraBot ∑", m, "bot"))
                self.after(0, lambda: self.send_btn.config(state="normal"))
                return

            if "video" in p or "videoaula" in p or "assistir" in p or "youtube" in p:
                self.after(0, self._on_videos)
                self.after(0, lambda: self.send_btn.config(state="normal"))
                return

            if "mais" in p and "exempl" in p:
                alvo = next((k for k,d in TOPICOS.items() if any(norm(s) in p for s in d["sins"])), estado.get("tema"))
                if alvo:
                    estado["tema"] = alvo
                    d = TOPICOS[alvo]
                    exs = "\n\n".join(f"  📌 {n}:\n     {desc}" for n,desc in d["exemplos"])
                    msg = f"╔ 📚 {d['titulo']} — Exemplos\n║\n{exs}\n╚"
                else:
                    msg = "De qual tópico? Ex: 'mais exemplos de combinação'"
                self.after(0, lambda m=msg: self._inserir("ÁlgebraBot ∑", m, "bot"))
                self.after(0, lambda: self.send_btn.config(state="normal"))
                return

            if any(x in p for x in ["ajuda","help","comandos"]):
                msg = ("╔ 📖 COMANDOS\n║\n"
                       "║ TÓPICOS: Explique PFC / Arranjo / Combinação / Permutação\n║\n"
                       "║ CÁLCULO: A(10,3)  C(6,2)  P(5)  AR(10,3)  CR(6,2)  8!\n"
                       "║          Anagramas de BANANA\n"
                       "║          Diagonais de polígono de 8 lados\n║\n"
                       "║ PRÁTICA: nova questão · gabarito\n║\n"
                       "║ VÍDEOS: clique em '🎬 Assistir Videoaulas' no topo\n"
                       "║         ou diga 'videoaulas'\n╚")
                self.after(0, lambda m=msg: self._inserir("ÁlgebraBot ∑", m, "bot"))
                self.after(0, lambda: self.send_btn.config(state="normal"))
                return

            resp_local = local_resp(txt)
            if resp_local:
                for k,d in TOPICOS.items():
                    if any(norm(s) in p for s in d["sins"]):
                        estado["tema"] = k; break
                self.after(0, lambda m=resp_local: self._inserir("ÁlgebraBot ∑", m, "bot"))
                self.after(0, lambda: self.send_btn.config(state="normal"))
                return

            msg = ("Hmm, não entendi bem. 🤔\n\n"
                   "Tente reformular. Exemplos:\n"
                   "  • 'Explique combinação'\n"
                   "  • 'A(10,3)' / 'C(6,2)' / 'P(5)'\n"
                   "  • 'Anagramas de ROMA'\n"
                   "  • 'Nova questão'\n"
                   "  • 'Videoaulas' para abrir os vídeos\n\n"
                   "Ou clique em 'Ajuda' no menu lateral.")
            self.after(0, lambda m=msg: self._inserir("ÁlgebraBot ∑", m, "bot"))
            self.after(0, lambda: self.send_btn.config(state="normal"))

        threading.Thread(target=_processar, daemon=True).start()


if __name__ == "__main__":
    App().mainloop()
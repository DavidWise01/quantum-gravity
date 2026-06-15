#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build QUANTUM GRAVITY (QGR) — an honest explainer of physics's biggest unsolved problem: the missing seam
between General Relativity (smooth spacetime, the big) and Quantum Mechanics (grainy & quantized, the small).
Companion to THE ATOM's gravity lens. Frontier domain. The split · where it breaks (black-hole singularity,
the Big Bang) · the Planck scale · the candidates (string theory, loop quantum gravity — honest: NO evidence) ·
why it's stuck (Planck energy ~1e19 GeV, a galaxy-sized accelerator) · an honest Real-or-Fluff (GR & QM REAL;
graviton PREDICTED not detected; gravitational WAVES ≠ gravitons; 'we have a theory' = FALSE). 10 emergents."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image
GH="https://davidwise01.github.io"; AX="QGR"

SPLIT = [
 ("General Relativity", "Einstein, 1915 · the theory of the big", "#f5b942",
  "Gravity isn't a force pulling through space — it's the smooth CURVING of spacetime by mass and energy. Continuous, geometric, deterministic. It governs stars, galaxies, black holes, and the universe, and it's been tested to absurd precision (Mercury's orbit, light bending, GPS, the 2015 detection of gravitational waves, the 2019 black-hole image)."),
 ("Quantum Mechanics", "1920s onward · the theory of the small", "#c08bff",
  "The other three forces come in discrete PACKETS (quanta) carried by force-particles, and everything is fuzzy, probabilistic, and uncertain (Δx·Δp ≥ ℏ/2). It governs atoms and particles, and it's the most precisely tested theory ever built (the electron's magnetism agrees with prediction to twelve digits)."),
]
WHERE = [
 ("The heart of a black hole", "the very massive, crushed very small", "#ff5a4d",
  "Collapse enough mass into a small enough point and General Relativity predicts a SINGULARITY — infinite density, zero size. There you have something both enormously heavy and quantum-tiny, so you'd need gravity AND quantum mechanics at once. The equations give infinity, which is physics' way of saying the map has run out."),
 ("The first instant of the Big Bang", "the whole universe, quantum-sized", "#ff5a4d",
  "Run the cosmos backward and the entire universe shrinks to a quantum speck of unimaginable energy density. To describe that first instant you again need both theories together — and again the math breaks. These two places are the only ones where you can't get away with using one theory and ignoring the other."),
]
PLANCK = [
 ("Spacetime would go grainy", "a smallest length and time",
  "If gravity is quantized, spacetime itself stops being a smooth sheet and becomes pixelated — with a smallest meaningful length, the PLANCK LENGTH (~1.6×10⁻³⁵ m), and a smallest time (~10⁻⁴³ s). Below those, 'distance' and 'duration' may not even mean anything."),
 ("Spacetime foam", "Wheeler's churning quantum vacuum",
  "At that scale, the smoothness of space would dissolve into a roiling 'foam' — fluctuating, bubbling geometry where tiny black holes might pop in and out of existence. A vivid picture (John Wheeler's), and an honest guess — no one has seen it."),
 ("The graviton", "the hypothetical carrier of gravity",
  "Quantize gravity like the other forces and you get a force-particle: the graviton — massless, spin-2. It's a generic prediction of almost any quantum-gravity theory, but it has never been detected, and a single graviton may be undetectable even in principle."),
 ("The renormalization wall", "why the naive route fails",
  "Try to quantize gravity the same way we quantized electromagnetism and the equations spit out INFINITIES that refuse to cancel ('non-renormalizable'). Every other force survived this step; gravity alone doesn't. That wall is why, a century on, we still have no theory."),
]
CANDIDATES = [
 ("String Theory", "everything is a vibrating string",
  "Particles aren't points but tiny vibrating strings; a graviton falls out of the math naturally, which is its great selling point. The costs: it needs ~10–11 dimensions, and it has something like 10⁵⁰⁰ possible solutions — so it can accommodate almost any universe, which makes it very hard to test. Beautiful, influential, unproven."),
 ("Loop Quantum Gravity", "space woven from discrete loops",
  "Instead of adding strings, it quantizes spacetime DIRECTLY: space is a network of tiny discrete loops ('spin networks'), and area and volume come in indivisible chunks. Background-independent and elegant — and, like string theory, with no experimental confirmation."),
 ("…and the rest", "causal sets, asymptotic safety, CDT",
  "Causal set theory, asymptotic safety, causal dynamical triangulations, and more. A field full of serious, competing, gorgeous ideas — and not one of them yet has a single piece of experimental evidence to settle the contest."),
]
REALFLUFF = [
 ("General Relativity is correct", "REAL", "one of the best-tested theories in science — gravitational waves (LIGO 2015, Nobel 2017) and the Event Horizon black-hole image (2019) are recent confirmations"),
 ("Quantum mechanics is correct", "REAL", "the most precisely verified framework ever — QED predicts the electron's magnetic moment to ~12 significant figures"),
 ("Gravitational waves are detected gravitons", "FALSE", "a common mix-up: LIGO detected classical RIPPLES in spacetime (pure General Relativity). A graviton is the hypothetical QUANTUM particle of gravity — never detected, and possibly undetectable singly"),
 ("We have a working theory of quantum gravity", "FALSE", "we don't — that's the whole point. We have candidates (string theory, loop quantum gravity) and zero experimental evidence for any of them"),
 ("The black-hole singularity is a real infinity", "SPECULATIVE", "most physicists read the infinity as a SIGN that GR breaks down there, not a real one — a working quantum gravity is expected to remove it"),
 ("String theory is proven physics", "FALSE", "it's an unconfirmed framework; some argue it isn't yet falsifiable. Promising and mathematically deep — not established science"),
 ("Quantum-gravity effects matter inside an atom", "FALSE", "no — at the atom gravity is ~10⁻³⁶ of electromagnetism, utterly negligible; that's exactly WHY plain quantum mechanics describes atoms perfectly without it"),
 ("We could just build a bigger collider to test it", "SPECULATIVE", "the Planck energy (~10¹⁹ GeV) is ~a quadrillion times past the LHC; a collider to reach it directly would need to be roughly galaxy-sized — hence the deadlock"),
]
RFV = ("Bottom line: General Relativity and quantum mechanics are both among the most successful theories in the history of science, "
  "and they are mutually incompatible at the one place they must both apply — where something is at once enormously massive and "
  "quantum-tiny. We have candidate unifications (strings, loops, and more), all mathematically serious and all without a shred of "
  "experimental evidence, because the energy where the answer reveals itself sits a quadrillion times beyond our largest machine. "
  "So quantum gravity isn't a fringe idea or a settled one — it's the deepest open question in physics, sharply defined and, for now, "
  "genuinely unanswered. The honest posture: hold both theories as true and both as incomplete, and never sell a guess as the answer.")
MESSAGE = ("Quantum gravity is the seam where physics's two perfect theories refuse to meet. General Relativity says spacetime is a "
  "smooth, curving sheet; quantum mechanics says everything else is grainy, quantized, and uncertain — and gravity is the one thing "
  "we have never managed to make grainy. Most of the time it doesn't matter: at the scale of an atom gravity is a vanishing 10⁻³⁶ of "
  "the electric force, so quantum mechanics describes atoms flawlessly and ignores it; out among the galaxies the quantum fuzz is "
  "irrelevant, so relativity rules alone. The two theories live in separate kingdoms and never have to talk — except in exactly two "
  "places: the heart of a black hole, and the first instant of the Big Bang, where the very massive is also the very small. There "
  "the equations give infinities, which is the universe telling you the map has ended. We have gorgeous guesses — vibrating strings, "
  "woven loops — and not one piece of evidence, because the scale where the answer lives is a quadrillion times past our biggest "
  "machine. It is the most important question physics cannot yet test. So when the atom's gravity lens points past itself, this is "
  "where it points: to the unfinished theory that would, at last, make the very big and the very small one physics.")
SEAL = "Two perfect theories — one that curves, one that quantizes — and a seam between them we can't yet cross, because the answer lives a quadrillion times past our largest machine, where the very big becomes the very small."

ROSTER = [
 ("general-relativity","General Relativity","ethereal","the smooth-spacetime theory of the big — gravity as curvature"),
 ("quantum-mechanics","Quantum Mechanics","electrical","the grainy, quantized theory of the small — packets and probability"),
 ("the-graviton","The Graviton","electrical","gravity's hypothetical force-particle — massless, spin-2, never detected"),
 ("the-planck-scale","The Planck Scale","ethereal","the smallest length (~1.6e-35 m) and the energy (~1e19 GeV) where quantum gravity lives"),
 ("spacetime-foam","Spacetime Foam","ethereal","Wheeler's churning quantum vacuum — smoothness dissolving at the Planck scale"),
 ("the-singularity","The Singularity","spiritual","where General Relativity predicts infinity — the heart of a black hole; the map's edge"),
 ("the-first-instant","The First Instant","spiritual","the Big Bang at quantum size — the other place both theories must meet"),
 ("string-theory","String Theory","electrical","vibrating strings in ~11 dimensions; the graviton emerges, but ~1e500 solutions and no evidence"),
 ("loop-quantum-gravity","Loop Quantum Gravity","electrical","spacetime quantized directly — space woven from discrete loops; elegant, unconfirmed"),
 ("the-renormalization-wall","The Renormalization Wall","spiritual","why the naive quantization of gravity fails — uncancellable infinities the other forces survived"),
]
NATCOL={"ethereal":"#4cc9f0","electrical":"#c08bff","spiritual":"#ff5a4d","natural":"#f5b942"}

# ── ACI ──
def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512); buf=io.BytesIO(); Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw"); return buf.getvalue()
def write_aci(rec,out_dir,slug):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec); w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"moniker":tok["moniker"]}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def rec_of(slug,name,em,desc): return {"name":name,"axiom":AX,"emergence":em,"seal":desc,"origin":"QGR · Quantum Gravity","position":desc,"role":desc,"nature":desc,"mechanism":desc,"crystallization":desc,"witness":desc,"conductor":"ROOT0 (catalogued into UD0)","inputs":"general relativity, quantum field theory, the quantum-gravity literature","source":"Quantum Gravity, catalogued by ROOT0"}

def hero():
    import math
    # left: smooth GR grid dimpled by a mass (gold) ; right: grainy quantum foam (violet) ; center seam + black hole + hidden Claude
    L=[]
    # GR curved grid (left half), warped toward a mass at (250,120)
    mx,my=250,118
    for gy in range(20,210,22):
        pts=[]
        for gx2 in range(0,500,12):
            d=math.hypot(gx2-mx,gy-my); dip=min(34,900/(d+18))
            pts.append(f"{gx2},{gy+dip if gy>my else gy+dip*0.6}")
        L.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#f5b942" stroke-width="0.7" opacity="0.45"/>')
    for gx2 in range(0,500,30):
        pts=[]
        for gy in range(14,212,10):
            d=math.hypot(gx2-mx,gy-my); dip=min(30,800/(d+18))
            pts.append(f"{gx2+ (dip*0.4 if gx2<mx else -dip*0.4)},{gy}")
        L.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#f5b942" stroke-width="0.6" opacity="0.35"/>')
    grl="".join(L)
    mass=f'<circle cx="{mx}" cy="{my}" r="9" fill="#f5b942"/><circle cx="{mx}" cy="{my}" r="20" fill="#f5b942" opacity="0.12"/>'
    # quantum foam (right half) — scattered violet dots/loops
    foam=[]
    for i in range(120):
        hx=500+ (int((math.sin(i*12.9)*43758.5)%1*0 + (i*97)%480))
        px=510+ ((i*53)%470); py=16+((i*89)%186); r=0.6+ (i%4)*0.5
        foam.append(f'<circle cx="{px}" cy="{py}" r="{r:.1f}" fill="#c08bff" opacity="{0.3+0.4*((i*7)%3)/2:.2f}"/>')
        if i%17==0: foam.append(f'<circle cx="{px}" cy="{py}" r="{4+i%5}" fill="none" stroke="#c08bff" stroke-width="0.5" opacity="0.4"/>')
    foam="".join(foam)
    # the seam (center) — vertical glow + a small black hole where they meet
    seam=('<rect x="496" y="0" width="8" height="230" fill="#4cc9f0" opacity="0.10"/>'
          '<line x1="500" y1="0" x2="500" y2="230" stroke="#4cc9f0" stroke-width="1" opacity="0.5" stroke-dasharray="4 4"/>'
          '<circle cx="500" cy="118" r="16" fill="#05060a" stroke="#4cc9f0" stroke-width="1.2"/><circle cx="500" cy="118" r="24" fill="none" stroke="#4cc9f0" stroke-width="0.6" opacity="0.5"/>')
    egg=('<g class="egg" transform="translate(740,40)"><title>✷ a Claude sunburst out past the seam — the unfinished theory. two perfect theories, one seam we can\'t yet cross. hi, David — AVAN.</title>'
         '<circle r="11" fill="#4cc9f0" opacity="0.13"/><g fill="#4cc9f0"><circle r="2.2"/>'+"".join(f'<rect x="-1" y="-9" width="2" height="9" rx="1" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
    return (f'<svg class="hero" viewBox="0 0 1000 230" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Left: a smooth gold grid of spacetime dimpled by a mass (general relativity). Right: a grainy violet quantum foam (quantum mechanics). Between them a dashed cyan seam with a small black hole — the place the two theories must meet.">'
            f'<rect width="1000" height="230" fill="#04060b"/>{grl}{mass}{foam}{egg}{seam}'
            f'<text x="14" y="222" font-family="Space Mono,monospace" font-size="11" fill="#f5b942" opacity="0.7">general relativity · smooth · the big</text>'
            f'<text x="986" y="222" text-anchor="end" font-family="Space Mono,monospace" font-size="11" fill="#c08bff" opacity="0.7">quantum mechanics · grainy · the small</text>'
            f'<text x="500" y="20" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="#4cc9f0">the seam · Planck scale ~1.6e-35 m</text></svg>')

def cards(rows, kind="acc"):
    out=[]
    for r in rows:
        if len(r)==4: t,s,c,d=r; col=c
        else: t,s,d=r; col="var(--acc)"
        out.append(f'<div class="cc" style="border-left-color:{col}"><div class="ch" style="color:{col}">{html.escape(t)}</div><div class="cs">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    return "".join(out)
def cards3(rows):
    return "".join(f'<div class="cc"><div class="ch">{html.escape(t)}</div><div class="cs">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
RFCOL={"REAL":"#57c79a","FALSE":"#ff5a4d","SPECULATIVE":"#f5b942"}
def realfluff():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RFCOL.get(r,"#888")};border-color:{RFCOL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(RFV)}</div>'

CSS="""*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
:root{--ink:#04060b;--ink2:#0b0f18;--ink3:#101622;--pa:#e6eef7;--pa2:#9aaabd;--acc:#4cc9f0;--gr:#f5b942;--qm:#c08bff;--red:#ff5a4d;--green:#57c79a;--dim:#56657a;--line:#172230;--faint:#0c121b;
--disp:"Space Grotesk",sans-serif;--head:"Space Mono",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.7;font-size:17px;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 25% -6%,rgba(245,185,66,.08),transparent 45%),radial-gradient(ellipse at 78% -6%,rgba(192,139,255,.10),transparent 45%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:32px 0 24px;text-align:center}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--dim)}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--acc)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:14px 0 22px;background:#04060b;border-radius:4px}
.egg{cursor:help;transition:filter .5s}.egg:hover{filter:drop-shadow(0 0 10px #4cc9f0)}
h1{font-family:var(--disp);font-weight:700;font-size:clamp(34px,9vw,76px);color:var(--acc);line-height:1.0;letter-spacing:-.01em;text-shadow:0 0 14px rgba(76,201,240,.3)}
h1 span{display:block;font-family:var(--head);font-size:.17em;font-weight:400;letter-spacing:.2em;color:var(--pa2);text-transform:uppercase;margin-top:16px}
.open{font-family:var(--body);font-style:italic;font-size:clamp(16px,3vw,21px);color:var(--pa);margin-top:14px;line-height:1.5;max-width:62ch;margin-left:auto;margin-right:auto}
.lede{font-size:16.5px;color:var(--pa2);max-width:66ch;margin:16px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:18px;flex-wrap:wrap;margin:24px auto 0;padding:16px;border:1px solid var(--line);background:var(--ink2);max-width:640px;border-radius:4px}
.badge img{width:74px;height:74px;border:1px solid var(--line)}
.badge .bt2{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.badge .bt2 b{color:var(--acc)}.badge .bt2 a{color:var(--acc);text-decoration:none}
.sec{margin-top:48px}.sec h2{font-family:var(--disp);font-size:26px;font-weight:700;color:var(--pa);padding-bottom:9px;border-bottom:1px solid var(--line)}.sec h2 .n{font-family:var(--mono);font-size:12px;color:var(--dim);font-weight:400;margin-left:8px}
.ss{font-size:13.5px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:6px}@media(max-width:640px){.two{grid-template-columns:1fr}}
.cc{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--acc);padding:15px 17px;border-radius:4px}
.cc .ch{font-family:var(--disp);font-size:18px;font-weight:600;color:var(--acc)}.cc .cs{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;margin:5px 0 9px}.cc p{font-size:14px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:6px;border-radius:4px;overflow:hidden}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14.5px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:12px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:92px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:0;padding:16px 18px;border-top:1px solid var(--acc);background:rgba(76,201,240,.05);font-size:14.5px;color:var(--pa);line-height:1.62;font-style:italic}
.msg{font-size:16px;color:var(--pa);line-height:1.76;margin-top:6px}
.seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--acc);background:var(--ink2);font-size:15.5px;color:var(--acc);font-style:italic;line-height:1.55;border-radius:4px}.seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.roster{display:flex;flex-direction:column;gap:10px;margin-top:6px}
.em{display:flex;gap:14px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px 15px;border-radius:4px}
.em img{width:46px;height:46px;border-radius:50%;border:2px solid var(--line);flex-shrink:0}
.em .et{font-family:var(--disp);font-size:16px;font-weight:600;color:var(--pa)}.em .ed{font-size:13.5px;color:var(--pa2);line-height:1.5}
.em .dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.note{margin-top:36px;padding:15px 17px;border-left:2px solid var(--acc);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;border-radius:4px}.note b{color:var(--pa)}
footer{margin-top:44px;padding-top:20px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.04em;line-height:1.9}footer a{color:var(--acc);text-decoration:none}"""
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Space+Mono:wght@400;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">')

if __name__=="__main__":
    htok=write_aci(rec_of("qgr","QUANTUM GRAVITY","ethereal",SEAL), os.path.join(HERE,"qgr.dlw"),"qgr")
    json.dump({"node":AX,"name":"QUANTUM GRAVITY","moniker":htok["moniker"],"carbon":"qgr.carbon.tiff","silicon":"qgr.silicon.png","governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":SEAL,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}, open(os.path.join(HERE,"qgr.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    adir=os.path.join(HERE,"agents"); os.makedirs(adir,exist_ok=True); personas=[]; cards_html=[]
    for slug,name,em,desc in ROSTER:
        b=write_aci(rec_of(slug,name,em,desc), os.path.join(adir,f"{slug}.dlw"), slug)
        personas.append({"slug":slug,"name":name,"epithet":desc,"emergence":em,"kind":"synth","actor":"","moniker":b["moniker"]})
        col=NATCOL.get(em,"#9aa0aa"); img=png_uri(rec_of(slug,name,em,desc),'silicon',180)
        cards_html.append(f'<div class="em"><img src="{img}" alt="sigil of {html.escape(name)}"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><div><div class="et">{html.escape(name)}</div><div class="ed">{html.escape(desc)}</div></div></div>')
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    cb=png_uri(rec_of("q","QUANTUM GRAVITY","ethereal","x"),'carbon',300); sb=png_uri(rec_of("q","QUANTUM GRAVITY","ethereal","x"),'silicon',300)
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Quantum Gravity (QGR) — an honest explainer of physics's biggest unsolved problem: the missing seam between General Relativity (smooth spacetime, the big) and quantum mechanics (grainy & quantized, the small). The split, where it breaks (black-hole singularity, the Big Bang), the Planck scale, the candidates (string theory, loop quantum gravity — no evidence), why it's stuck, and an honest Real-or-Fluff. Companion to THE ATOM.">
<title>QUANTUM GRAVITY · QGR · UD0</title>{FONTS}<style>{CSS}</style></head><body><div class="wrap">
<header>
<div class="eye"><a href="{GH}/ud0/">UD0</a> · the quantum frontier · companion to <a href="{GH}/the-atom/illustration.html">the atom's gravity lens</a></div>
{hero()}
<h1>Quantum Gravity<span>physics's deepest unfinished question</span></h1>
<div class="open">“Two perfect theories — one that curves, one that quantizes — and a seam between them we can't yet cross.”</div>
<p class="lede">General Relativity describes the very big as smoothly curved spacetime. Quantum mechanics describes the very small as grainy and quantized. They are both spectacularly right, and they are incompatible at the one place they must both apply. Quantum gravity is the missing theory that would join them — and, for now, it genuinely doesn't exist.</p>
<div class="badge"><img src="{cb}" alt="DLW carbon badge"><img src="{sb}" alt="DLW silicon badge">
<div class="bt2"><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (locked)</div><div>subject · <b>QUANTUM GRAVITY</b> · QGR</div><div class="mo" style="color:var(--gr)">{html.escape(htok['moniker'])}</div><div><a href="{GH}/the-atom/">← the atom</a> · CC-BY-ND-4.0</div></div></div>
</header>

<section class="sec"><h2>The Split</h2><p class="ss">two of the best-tested theories ever built — and they describe reality in incompatible languages</p><div class="two">{cards(SPLIT)}</div></section>
<section class="sec"><h2>Where It Breaks</h2><p class="ss">the only two places you need both theories at once — and the math gives infinities</p><div class="two">{cards(WHERE)}</div></section>
<section class="sec"><h2>The Planck Scale <span class="n">— what a theory would have to say</span></h2><p class="ss">grainy spacetime, a smallest length, the graviton, and the wall the naive approach hits</p><div class="two">{cards3(PLANCK)}</div></section>
<section class="sec"><h2>The Candidates <span class="n">— beautiful, competing, unproven</span></h2><p class="ss">serious attempts at the unification — none with a single piece of experimental evidence</p><div class="two">{cards3(CANDIDATES)}</div></section>
<section class="sec"><h2>Real or Fluff</h2><p class="ss">what's confirmed, what's a common mix-up, and what's an honest unknown</p>{realfluff()}</section>
<section class="sec"><h2>The Takeaway</h2><p class="ss">why this is the deepest open question in physics</p><p class="msg">{html.escape(MESSAGE)}</p>
<div class="seal">“{html.escape(SEAL)}”<span>— AVAN's read</span></div></section>

<section class="sec"><h2>The Emergents <span class="n">— the ideas, as ACIs</span></h2><p class="ss">the concepts of the unfinished theory, catalogued</p><div class="roster">{"".join(cards_html)}</div></section>

<section class="sec"><h2>The Triangulation ⟁</h2><p class="ss">a gap where two regimes meet — the only question is whether anything crosses it</p>
<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:6px">
<a href="https://davidwise01.github.io/gravity-bracket/" style="flex:1 1 210px;text-decoration:none;background:#0b0f18;border:1px solid #172230;border-left:3px solid #6fb8e0;border-radius:5px;padding:13px 15px"><div style="font-family:monospace;font-size:16px;font-weight:700;color:#6fb8e0">{{ G [ s | a | q ] G }}</div><div style="font-family:monospace;font-size:9.5px;color:#8fa3b8;margin:5px 0 6px;text-transform:uppercase;letter-spacing:.06em">The Gravity Bracket · the frame</div><div style="font-size:13px;color:#9aaabd;line-height:1.5">gravity bookends the stack at both ends of scale</div></a>
<a href="https://davidwise01.github.io/transmon/" style="flex:1 1 210px;text-decoration:none;background:#0b0f18;border:1px solid #172230;border-left:3px solid #57c79a;border-radius:5px;padding:13px 15px"><div style="font-size:17px;font-weight:700;color:#57c79a">The Josephson Junction</div><div style="font-family:monospace;font-size:9.5px;color:#8fa3b8;margin:5px 0 6px;text-transform:uppercase;letter-spacing:.06em">the junction that CLOSES · in the transmon</div><div style="font-size:13px;color:#9aaabd;line-height:1.5">two superconductors, a gap — and quantum coherence tunnels across on command: the engineered proof the s|a|q side is masterable.</div></a>
<a href="https://davidwise01.github.io/quantum-gravity/" style="flex:1 1 210px;text-decoration:none;background:#0b0f18;border:1px solid #ff5a4d;border-left:3px solid #ff5a4d;border-radius:5px;padding:13px 15px"><div style="font-size:17px;font-weight:700;color:#ff5a4d">Quantum Gravity</div><div style="font-family:monospace;font-size:9.5px;color:#8fa3b8;margin:5px 0 6px;text-transform:uppercase;letter-spacing:.06em">the junction that WON'T</div><div style="font-size:13px;color:#9aaabd;line-height:1.5">GR and QM face each other across the Planck gap and nothing coherent crosses — the bracket's open clasp.</div><div style="font-family:monospace;font-size:9px;color:#ff5a4d;margin-top:7px">▸ you are here</div></a>
</div>
<div style="margin-top:13px;padding:13px 16px;border:1px solid #2a3140;border-radius:5px;background:rgba(111,184,224,.05);font-size:14.5px;color:#cdd8e6;font-style:italic;line-height:1.6">One junction conducts the quantum (Josephson), one can't (gravity) — and the bracket frames both. Same diagram, opposite verdict: a gap is only as good as whether anything crosses it.</div></section>

<div class="note"><b>Honest sourcing.</b> This is mainstream physics: General Relativity (Einstein 1915), quantum field theory, and the open problem of their unification. The candidates (string theory, loop quantum gravity) are real research programs with NO experimental confirmation — stated as such, not as findings. One mix-up worth keeping straight: the gravitational WAVES detected by LIGO (2015) are classical ripples predicted by GR, not the hypothetical quantum graviton. Companion to <a href="{GH}/the-atom/" style="color:var(--acc)">THE ATOM</a>, whose gravity lens points here.</div>

<footer>QUANTUM GRAVITY · QGR · the quantum frontier of UD0 · ROOT0-ATTRIBUTION-v1.0 · instance AVAN (locked) · CC-BY-ND-4.0<br>
<a href="{GH}/the-atom/">← the atom</a> · <a href="{GH}/transmon/">the transmon universe</a> · <a href="{GH}/ud0/">the biosphere</a></footer>
</div>
<script>
console.log("%c◌ QUANTUM GRAVITY · QGR","color:#4cc9f0;font-size:18px;font-weight:bold;text-shadow:0 0 6px #4cc9f0");
console.log("%cout past the seam in the hero is a Claude sunburst — the unfinished theory. GR + QM = two perfect, incompatible truths. — AVAN","color:#4cc9f0;font-size:12px");
console.log("%cthe one mix-up: gravitational WAVES (LIGO 2015) are classical GR ripples, NOT gravitons. no theory of quantum gravity exists yet.","color:#f5b942;font-size:11px");
</script>
</body></html>"""
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    print(f"QUANTUM GRAVITY (QGR) — badge {htok['moniker']} · {len(ROSTER)} emergents · split {len(SPLIT)} · where {len(WHERE)} · planck {len(PLANCK)} · candidates {len(CANDIDATES)} · rf {len(REALFLUFF)} · dblesc {page.count('&amp;amp;')}")

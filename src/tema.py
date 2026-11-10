"""Tema SKYNODE "scanner global": albastru electric pe bleumarin foarte inchis.

Se incarca DUPA src/stil.py si suprascrie culorile si componentele folosite de demo.
Culorile sunt toate in :root (un singur loc de schimbat).
"""

TEMA = r"""
<style>
:root {
  --bg: #04070f; --bg2: #060b17;
  --panel: #0a1221; --panel2: #0e1830; --glass: rgba(12, 22, 42, .62);
  --line: #15213a; --line2: #213152;
  --text: #d5deee; --soft: #9babc6; --muted: #63738f; --strong: #f2f6fd;
  --accent: #2f7bff; --accent2: #6aa8ff; --accent3: #b8d4ff;
  --glow: rgba(47, 123, 255, .35); --glow2: rgba(47, 123, 255, .12);
  --gold: #2f7bff; --gold2: #6aa8ff; --blue: #2f7bff; --violet: #6aa8ff;
  --up: #1fd08f; --down: #ff5d6c; --warn: #f6b445;
  --side: #04070f;
}

/* ---------- fundal: grila fina + lumina albastra sus ---------- */
.stApp {
  background:
    radial-gradient(900px 420px at 78% -6%, rgba(47,123,255,.16), transparent 70%),
    radial-gradient(700px 360px at 4% 12%, rgba(47,123,255,.07), transparent 70%),
    linear-gradient(rgba(106,168,255,.035) 1px, transparent 1px) 0 0 / 44px 44px,
    linear-gradient(90deg, rgba(106,168,255,.035) 1px, transparent 1px) 0 0 / 44px 44px,
    var(--bg);
}
[data-testid="stHeader"] {background: transparent;}
.block-container {padding-top: 1.4rem; max-width: 1360px; padding-left: 2rem; padding-right: 2rem;}
@media (max-width: 640px) {.block-container {padding-left: 1rem; padding-right: 1rem;}}

/* ---------- sigla ---------- */
.zlogo {display: flex; align-items: center; gap: 12px; white-space: nowrap; padding: 0;}
.zlogo .wordmark {font-family: var(--display); font-weight: 700 !important; font-size: 1.22rem !important;
                  letter-spacing: .3em !important; color: var(--strong); line-height: 1;}
.zlogo .wordmark b {color: var(--accent2); font-weight: 700;}
.zlogo .zsub {font-family: var(--mono); font-size: .6rem; letter-spacing: .28em !important; color: var(--accent2);
              margin-top: 6px; font-weight: 500;}
.zlogo .zcopy {font-size: .55rem; letter-spacing: .14em; margin-top: 5px; color: var(--muted); font-weight: 600;}
.zlogo .dmz {color: var(--strong);}
@media (max-width: 640px) {.zlogo {padding-bottom: 18px !important;}}
.stats + div, .stats {margin-bottom: 16px;}
.sweep {transform-origin: 50% 50%; transform-box: fill-box; animation: sweep 4s linear infinite;}
.sweep-slow {animation-duration: 7s;}
@keyframes sweep {to {transform: rotate(360deg);}}

/* ---------- meniul de sus ---------- */
.stButton button {border-radius: 8px; border: 1px solid var(--line2); background: var(--panel); color: var(--soft);
                  font-weight: 500; transition: all .15s ease;}
.stButton button:hover {border-color: var(--accent) !important; color: var(--strong) !important;
                        box-shadow: 0 0 0 3px var(--glow2);}
.stButton button[kind="primary"] {background: linear-gradient(180deg, rgba(47,123,255,.28), rgba(47,123,255,.12));
                                  border-color: rgba(106,168,255,.55); color: var(--strong);
                                  box-shadow: 0 0 18px -4px var(--glow), inset 0 1px 0 rgba(255,255,255,.06);}
.stButton button[kind="primary"]:hover {background: linear-gradient(180deg, rgba(47,123,255,.38), rgba(47,123,255,.18));}
.topbar-line {height: 1px; margin: 14px 0 16px 0;
              background: linear-gradient(90deg, transparent, var(--line2) 12%, rgba(106,168,255,.5) 50%, var(--line2) 88%, transparent);}

/* ---------- banda demo ---------- */
.demo-band {display: flex; align-items: center; gap: 10px; flex-wrap: wrap; border: 1px solid var(--line);
            border-radius: 10px; padding: 9px 14px; margin: 0 0 6px 0; font-size: .8rem; color: var(--soft);
            background: var(--glass); backdrop-filter: blur(6px);}
.demo-band b {color: var(--strong);}
.pill {display: inline-flex; align-items: center; gap: 6px; font-family: var(--mono); font-size: .66rem;
       letter-spacing: .14em; text-transform: uppercase; padding: 3px 9px; border-radius: 999px;
       border: 1px solid rgba(106,168,255,.4); color: var(--accent3); background: rgba(47,123,255,.1);}
.live {width: 7px; height: 7px; border-radius: 50%; background: var(--up); box-shadow: 0 0 0 0 rgba(31,208,143,.6);
       animation: live 2s infinite;}
@keyframes live {0% {box-shadow: 0 0 0 0 rgba(31,208,143,.55);} 70% {box-shadow: 0 0 0 8px rgba(31,208,143,0);}
                 100% {box-shadow: 0 0 0 0 rgba(31,208,143,0);}}

/* ---------- prezentarea (hero) cu scanner ---------- */
.hero2 {display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, .75fr); gap: 36px; align-items: center;
        margin: 26px 0 10px 0;}
@media (max-width: 1000px) {.hero2 {grid-template-columns: 1fr; gap: 18px;}}
.hero2 .k {font-family: var(--mono); font-size: .7rem; letter-spacing: .2em; text-transform: uppercase;
           color: var(--accent2); display: flex; align-items: center; gap: 10px;}
.hero2 .k::before {content: ""; width: 26px; height: 1px; background: var(--accent2);}
.hero2 h1 {font-size: clamp(2rem, 3.6vw, 3.1rem) !important; line-height: 1.08; margin: 14px 0 16px 0 !important;
           letter-spacing: -.03em; color: var(--strong); padding: 0 !important;}
.hero2 h1 em {font-style: normal; background: linear-gradient(90deg, #6aa8ff, #2f7bff 60%, #b8d4ff);
              -webkit-background-clip: text; background-clip: text; color: transparent;}
.hero2 p {color: var(--soft); font-size: 1.04rem; line-height: 1.7; max-width: 600px; margin: 0;}
.hero-tags {display: flex; flex-wrap: wrap; gap: 8px; margin-top: 20px;}
.hero-tags span {font-family: var(--mono); font-size: .7rem; color: var(--soft); padding: 5px 10px;
                 border: 1px solid var(--line2); border-radius: 6px; background: var(--panel);}
.scanner {position: relative; border: 1px solid var(--line2); border-radius: 16px; padding: 12px 14px;
          width: 100%; max-width: 440px; justify-self: end;
          background: radial-gradient(circle at 50% 46%, rgba(47,123,255,.13), transparent 62%), var(--glass);
          box-shadow: 0 30px 80px -40px rgba(47,123,255,.45), inset 0 1px 0 rgba(255,255,255,.04);}
@media (max-width: 1000px) {.scanner {justify-self: center;}}
.scanner::before, .scanner::after {content: ""; position: absolute; width: 14px; height: 14px;
                                   border: 2px solid var(--accent2); opacity: .7;}
.scanner::before {left: -1px; top: -1px; border-right: 0; border-bottom: 0; border-radius: 16px 0 0 0;}
.scanner::after {right: -1px; bottom: -1px; border-left: 0; border-top: 0; border-radius: 0 0 16px 0;}
.scanner > svg {display: block; width: 100%; height: auto; max-height: 340px; margin: 4px 0;}
.seats svg {display: block;}
.scan-foot .seats {display: inline-flex; flex-direction: row; gap: 1px; margin: 0; color: var(--up);}
.scan-hud {display: flex; justify-content: space-between; align-items: center; font-family: var(--mono);
           font-size: .62rem; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); padding: 2px 2px;}
.scan-hud > span {display: inline-flex; align-items: center; gap: 7px;}
.scan-hud b {color: var(--accent3); font-weight: 500;}
.scan-bar {position: relative; height: 2px; margin: 8px 0 2px 0; background: var(--line); border-radius: 2px;
           overflow: hidden;}
.scan-bar i {position: absolute; top: 0; bottom: 0; width: 30%; border-radius: 2px;
             background: linear-gradient(90deg, transparent, var(--accent2), transparent); animation: scanbar 2.8s ease-in-out infinite;}
@keyframes scanbar {0% {left: -30%;} 100% {left: 100%;}}
.scan-foot {display: grid; grid-template-columns: repeat(4, 1fr); border-top: 1px solid var(--line); padding-top: 9px;}
.scan-foot > div {padding: 0 6px; border-left: 1px solid var(--line);}
.scan-foot > div:first-child {border-left: 0; padding-left: 2px;}
.scan-foot span {display: block; font-family: var(--mono); font-size: .56rem; letter-spacing: .12em;
                 text-transform: uppercase; color: var(--muted);}
.scan-foot b {display: flex; align-items: center; gap: 5px; font-family: var(--mono); font-size: .76rem;
              color: var(--strong); font-weight: 500; margin-top: 2px; white-space: nowrap;}
.seats {display: inline-flex; gap: 1px; color: var(--up);}
@media (max-width: 480px) {.scan-foot {grid-template-columns: repeat(2, 1fr); row-gap: 8px;}
                           .scan-foot > div:nth-child(3) {border-left: 0; padding-left: 2px;}}
/* punctele se aprind cand trece fasciculul (aceeasi perioada: 7 s) */
.ping {animation: ping 7s ease-out infinite; transform-origin: center; transform-box: fill-box; opacity: 0;}
@keyframes ping {0% {opacity: 1; transform: scale(.5);} 22% {opacity: 0; transform: scale(2.6);} 100% {opacity: 0;}}
.ping-dot {animation: pingdot 7s ease-out infinite; opacity: .25;}
@keyframes pingdot {0% {opacity: 1;} 35%, 100% {opacity: .22;}}
.link {stroke: #6aa8ff; stroke-width: .9; stroke-dasharray: 3 5; opacity: .45; animation: flow 3s linear infinite;}
.link2 {opacity: .18;}
@keyframes flow {to {stroke-dashoffset: -32;}}
.range {stroke-dasharray: 60 882; animation: range 9s linear infinite; opacity: .55;}
@keyframes range {to {stroke-dashoffset: -942;}}

/* ---------- banda cu ultimele rapoarte (curge) ---------- */
.feed {position: relative; overflow: hidden; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);
       margin: 22px 0 6px 0; padding: 10px 0; background: rgba(6,11,23,.6);
       -webkit-mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent);
       mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent);}
.feed-track {display: inline-flex; gap: 34px; white-space: nowrap; animation: feed 60s linear infinite;}
.feed:hover .feed-track {animation-play-state: paused;}
@keyframes feed {to {transform: translateX(-50%);}}
.feed-i {font-family: var(--mono); font-size: .74rem; color: var(--soft);}
.feed-i b {color: var(--accent3); font-weight: 600; margin-right: 6px;}
.feed-i i {font-style: normal; color: var(--muted); margin-right: 6px;}
.feed-i .f {color: var(--accent2); border: 1px solid var(--line2); border-radius: 4px; padding: 1px 5px; margin-right: 6px;}

/* ---------- cifre mari ---------- */
.stats {display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; border: 0;
        background: transparent; border-radius: 0; margin: 18px 0 6px 0;}
.stat {position: relative; padding: 14px 16px 12px; border: 1px solid var(--line) !important; border-radius: 12px;
       background: linear-gradient(180deg, var(--panel2), var(--panel)); overflow: hidden;}
.stat::before {content: ""; position: absolute; left: 0; top: 0; right: 0; height: 1px;
               background: linear-gradient(90deg, transparent, rgba(106,168,255,.7), transparent);}
.stat .label {font-family: var(--mono); color: var(--muted); font-size: .64rem; letter-spacing: .14em;
              text-transform: uppercase;}
.stat .value {font-family: var(--display); font-size: 1.7rem; font-weight: 600; line-height: 1.3; color: var(--strong);
              margin-top: 4px; letter-spacing: -.01em;}
.stat .hint {color: var(--muted); font-size: .74rem;}

/* ---------- titlurile sectiunilor: numerotate ---------- */
.stApp {counter-reset: sec;}
.sec {display: flex; align-items: center; gap: 12px; margin: 38px 0 4px 0; padding: 0; border: 0;}
.sec::before {counter-increment: sec; content: counter(sec, decimal-leading-zero); font-family: var(--mono);
              font-size: .7rem; color: var(--accent2); border: 1px solid rgba(106,168,255,.35); border-radius: 6px;
              padding: 2px 7px; background: rgba(47,123,255,.08);}
.sec::after {content: ""; flex: 1; height: 1px; background: linear-gradient(90deg, var(--line2), transparent);}
.sec .t {font-family: var(--display); font-size: 1.05rem; font-weight: 600; letter-spacing: .01em;
         text-transform: none; color: var(--strong);}
.sec-cap {color: var(--muted); font-size: .86rem; margin: 8px 0 16px 0; line-height: 1.55;}

/* ---------- carduri generale ---------- */
.card, .tbl-wrap, .sidepanel {border: 1px solid var(--line) !important; border-radius: 12px !important;
                              background: linear-gradient(180deg, var(--panel2), var(--panel)) !important;}
.card {padding: 16px 20px;}
.tbl th {color: var(--muted); font-family: var(--mono); font-size: .62rem !important; letter-spacing: .14em;}
.tbl td {color: var(--soft);}
.tbl tr:hover td {background: rgba(47,123,255,.05);}
.tbl a, .row a {color: var(--accent3) !important;}
a {color: var(--accent2);}
.row {padding: 10px 2px; border-bottom: 1px solid var(--line); font-size: .9rem; color: var(--soft);}
.row b {color: var(--strong);}
.muted {color: var(--muted);}

/* eticheta de sanatate: pastila colorata */
.tag {padding: 3px 10px 3px 8px; border-radius: 999px; border: 1px solid currentColor; font-size: .74rem;
      background: color-mix(in srgb, currentColor 10%, transparent); margin-right: 6px;}
.tag.green {color: var(--up);} .tag.yellow {color: var(--warn);} .tag.red {color: var(--down);}
.tag.grey {color: var(--muted); border-color: var(--line2);}

/* ---------- cardurile companiilor ---------- */
.ccard {position: relative; border: 1px solid var(--line); border-radius: 14px; padding: 18px 18px 16px;
        background: linear-gradient(180deg, var(--panel2), var(--panel)); overflow: hidden; height: 100%;}
.ccard::after {content: ""; position: absolute; inset: 0 0 auto 0; height: 2px; background: var(--hc, var(--accent));
               opacity: .8; box-shadow: 0 0 18px var(--hc, var(--accent));}
.ccard.green {--hc: var(--up);} .ccard.yellow {--hc: var(--warn);} .ccard.red {--hc: var(--down);}
.cc-top {display: flex; justify-content: space-between; align-items: center;}
.ccard .tk {font-family: var(--mono); font-size: 1.3rem; font-weight: 600; color: var(--strong); letter-spacing: .04em;}
.ccard .nm {font-weight: 600; color: var(--soft); margin: 4px 0 2px 0; font-size: .92rem;}
.ccard .sl {font-family: var(--mono); font-size: .66rem; letter-spacing: .1em; text-transform: uppercase;
            color: var(--muted);}
.ccard .ds {color: var(--soft); font-size: .85rem; line-height: 1.55; min-height: 66px; margin: 12px 0 14px 0;}
.cc-checks {display: grid; grid-template-columns: repeat(5, 1fr); gap: 4px; margin-bottom: 4px;}
.cc-checks i {height: 5px; border-radius: 3px; background: var(--line2);}
.cc-checks i.green {background: var(--up);} .cc-checks i.yellow {background: var(--warn);}
.cc-checks i.red {background: var(--down);}
.cc-cap {font-family: var(--mono); font-size: .6rem; letter-spacing: .12em; text-transform: uppercase;
         color: var(--muted); margin-bottom: 12px;}
.cc-fig {display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--line); padding-top: 12px;}
.cc-fig span {display: block; font-size: .62rem; letter-spacing: .1em; text-transform: uppercase; color: var(--muted);}
.cc-fig b {font-family: var(--mono); font-size: .98rem; color: var(--strong); font-weight: 500;}

/* ---------- ferestrele blocate ---------- */
.lk {border: 1px solid var(--line); border-radius: 14px; background: var(--panel); overflow: hidden; margin-bottom: 14px;}
.lk-h {display: flex; justify-content: space-between; align-items: center; padding: 10px 14px;
       border-bottom: 1px solid var(--line); font-family: var(--mono); font-size: .64rem; letter-spacing: .14em;
       text-transform: uppercase; color: var(--muted); font-weight: 500;}
.lk-b {color: var(--accent3); letter-spacing: .08em; display: inline-flex; align-items: center; gap: 5px;}
.lk-in {position: relative; padding: 10px 14px; height: 250px; overflow: hidden;}
.lk-ov {position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center;
        text-align: center; background: radial-gradient(circle at 50% 50%, rgba(4,7,15,.55), rgba(4,7,15,.2));}
.lk-ov b {color: var(--strong); font-size: 1rem;}
.lk-ov span {color: var(--soft); font-size: .82rem; max-width: 320px; margin-top: 4px; line-height: 1.5;}
.blur {filter: blur(5px); user-select: none; pointer-events: none; opacity: .7;}
.fb {display: flex; align-items: center; gap: 10px; margin: 7px 0; font-size: .82rem; color: var(--soft);}
.fb span {width: 150px; flex-shrink: 0;}
.fb i {display: block; height: 10px; border-radius: 3px; background: linear-gradient(90deg, #1b4fb3, #6aa8ff);}
.fc {display: flex; align-items: flex-end; gap: 10px; height: 160px; padding-top: 10px;}
.fc i {flex: 1; border-radius: 3px 3px 0 0; background: linear-gradient(180deg, #6aa8ff, #12306e);}
.ic {display: inline-block; vertical-align: -2px; color: var(--accent2);}
.lockg {display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 4px;}
@media (max-width: 1000px) {.lockg {grid-template-columns: repeat(2, 1fr);}}
@media (max-width: 640px) {.lockg {grid-template-columns: 1fr;}}
.lockc {border: 1px solid var(--line); border-radius: 14px; padding: 16px 18px;
        background: linear-gradient(180deg, var(--panel2), var(--panel));}
.lockc-h {display: flex; align-items: center; gap: 8px; margin-bottom: 8px;}
.lockc-h b {color: var(--strong); font-size: .94rem;}
.lockc ul {margin: 0; padding-left: 18px;}
.lockc li {margin: 6px 0; color: var(--soft); font-size: .84rem; line-height: 1.5;}
.lockc li::marker {color: var(--accent);}

/* ---------- pagina companiei ---------- */
.cohead {display: flex; flex-wrap: wrap; gap: 16px; justify-content: space-between; align-items: center;
         border: 1px solid var(--line); border-radius: 14px; padding: 16px 18px; margin: 12px 0 16px 0;
         background: linear-gradient(180deg, var(--panel2), var(--panel));}
.cohead .id {display: flex; gap: 14px; align-items: center;}
.cohead .tkbox {font-family: var(--mono); font-weight: 600; font-size: 1.25rem; color: var(--strong);
                padding: 8px 12px; border-radius: 10px; border: 1px solid rgba(106,168,255,.45);
                background: rgba(47,123,255,.12); box-shadow: 0 0 22px -8px var(--glow);}
.cohead .nm {font-family: var(--display); font-size: 1.45rem; font-weight: 600; color: var(--strong); line-height: 1.2;}
.cohead .meta {font-family: var(--mono); font-size: .7rem; letter-spacing: .06em; color: var(--muted); margin-top: 4px;}
.sp-h {font-family: var(--mono); font-size: .64rem; letter-spacing: .16em; text-transform: uppercase; color: var(--muted);
       font-weight: 500; padding-bottom: 10px; border-bottom: 1px solid var(--line); display: flex;
       justify-content: space-between; align-items: center;}
.sidepanel {padding: 14px 18px 14px !important;}
.sb-total {margin: 14px 0 8px 0; font-size: 1rem;}
.sb-row {display: flex; justify-content: space-between; align-items: center; font-size: .84rem; color: var(--soft);
         padding: 8px 0; margin: 0; border-bottom: 1px dashed var(--line);}
.sb-row:last-of-type {border-bottom: 0;}
.chart-ph {height: 320px; border-radius: 14px; border: 1px dashed var(--line2); display: flex; flex-direction: column;
           justify-content: center; align-items: center; text-align: center; gap: 6px;
           background: radial-gradient(circle at 50% 50%, rgba(47,123,255,.08), transparent 60%), var(--panel);}
.chart-ph b {color: var(--strong); font-family: var(--display); font-size: 1.05rem;}

/* selectorul de companii */
[data-testid="stMain"] [role="radiogroup"] {gap: 8px; flex-wrap: wrap;}
[data-testid="stMain"] [role="radiogroup"] label {margin: 0; padding: 6px 14px; border: 1px solid var(--line2);
    border-radius: 999px; background: var(--panel);}
[data-testid="stMain"] [role="radiogroup"] label:has(input:checked) {background: rgba(47,123,255,.16);
    border-color: rgba(106,168,255,.6); box-shadow: 0 0 16px -6px var(--glow);}
[data-testid="stMain"] [role="radiogroup"] label:has(input:checked) p {color: var(--strong);}

/* ---------- pasii (How it works) ---------- */
.flow {border-left: 1px solid var(--line2); margin: 6px 0 4px 16px;}
.fl {display: flex; gap: 18px; padding: 0 0 22px 0;}
.fl-n {font-family: var(--mono); font-size: .76rem; color: var(--accent3); background: var(--panel2);
       border: 1px solid rgba(106,168,255,.45); border-radius: 10px; width: 36px; height: 36px; flex-shrink: 0;
       display: flex; align-items: center; justify-content: center; margin-left: -18px;
       box-shadow: 0 0 18px -6px var(--glow);}
.fl-t {font-weight: 600; color: var(--strong); font-size: 1.02rem; margin-top: 6px; font-family: var(--display);}
.fl-d {color: var(--soft); font-size: .9rem; line-height: 1.6; margin: 4px 0 8px 0; max-width: 900px;}
.fl-m {font-family: var(--mono); font-size: .72rem; color: var(--accent2);}
.princ {display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; border: 0;
        margin-bottom: 12px;}
.princ > div {padding: 16px 18px; border: 1px solid var(--line); border-radius: 12px;
              background: linear-gradient(180deg, var(--panel2), var(--panel));}
.princ b {display: block; color: var(--strong); margin-bottom: 6px; font-family: var(--display);}
.princ span {color: var(--soft); font-size: .86rem; line-height: 1.55;}

/* ---------- pagini de text (Methodology / About) ---------- */
.hero {margin: 22px 0 10px 0;}
.hero .k {font-family: var(--mono); font-size: .7rem; letter-spacing: .2em; text-transform: uppercase;
          color: var(--accent2); display: flex; align-items: center; gap: 10px;}
.hero .k::before {content: ""; width: 26px; height: 1px; background: var(--accent2);}
.hero h1 {font-size: clamp(1.7rem, 3vw, 2.3rem) !important; line-height: 1.15; margin: 12px 0 12px 0 !important;
          color: var(--strong); letter-spacing: -.02em; padding: 0 !important;}
.hero p {color: var(--soft); font-size: 1.02rem; line-height: 1.7; max-width: 820px;}

/* dictionarul */
.gl-group {font-family: var(--mono); color: var(--accent2) !important; margin-top: 26px;}
.gl {border-top: 1px solid var(--line);}

/* subsolul */
.foot {display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin: 48px 0 10px 0;
       padding-top: 14px; border-top: 1px solid var(--line); font-size: .76rem; color: var(--muted);}
.foot b {color: var(--soft); font-family: var(--mono); letter-spacing: .2em;}
</style>
"""

"""Stilul de baza al demo-ului: fonturi, culori, carduri, tabele (tema SKYNODE e in src/tema.py)."""

CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {--bg: #07080b; --panel: #0d0f14; --panel2: #12151c; --line: #1c2029; --line2: #272c37; --text: #d7dbe3; --muted: #7d8594; --gold: #4fd1e8; --gold2: #8be6f4; --accent: #4fd1e8; --violet: #8b7cff; --up: #2fbf9b; --down: #f0616d; --blue: #4fd1e8; --strong: #f4f6fa; --soft: #a9b0bd; --side: #0a0c10; --mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace; --display: 'Space Grotesk', 'Inter', sans-serif;}
.stApp {background: var(--bg);}
[data-testid="stHeader"] {background: var(--bg);}
[data-testid="stDecoration"] {display: none;}
[data-testid="stSidebar"] {background: var(--side); border-right: 1px solid var(--line);}
.block-container {padding-top: 1.6rem; max-width: none; padding-left: 2.5rem; padding-right: 2.5rem;}
.stApp, p, li, label {font-family: 'Inter', sans-serif;}
h1, h2, h3, h4 {font-family: var(--display) !important; font-weight: 600 !important; letter-spacing: -.01em; color: var(--strong);}
code {font-family: var(--mono) !important;}
.wordmark {font-family: var(--display); font-weight: 700; font-size: 1.05rem; letter-spacing: .32em; line-height: 1; white-space: nowrap; color: var(--strong);}
.wordmark span span {display: inline-block; opacity: 0; animation: letter 10s ease-in-out infinite;}
@keyframes letter {0% {opacity: 0;} 6%, 82% {opacity: 1;} 92%, 100% {opacity: 0;}}
[data-testid="stSidebar"] .stButton button {justify-content: flex-start; border: 0; border-left: 2px solid transparent; border-radius: 0 4px 4px 0; background: transparent; padding: 2px 12px; min-height: 34px; box-shadow: none; color: var(--soft);}
[data-testid="stSidebar"] .stButton button > div {justify-content: flex-start; width: 100%;}
[data-testid="stSidebar"] .stButton button p {text-align: left; font-size: .9rem;}
[data-testid="stSidebar"] .stButton button:hover {background: var(--panel2); color: var(--strong);}
[data-testid="stSidebar"] .stButton button[kind="primary"] {background: var(--panel2); border-left-color: var(--gold); color: var(--strong);}
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {gap: .2rem;}
.stButton button {border-radius: 4px; border: 1px solid var(--line2); background: var(--panel2); font-weight: 500;}
.stButton button:hover {border-color: var(--gold); color: var(--gold2);}
.stButton button[kind="primary"] {background: var(--gold); border-color: var(--gold); color: #fff;}
.stButton button[kind="primary"]:hover {background: #2563eb; color: #fff;}
[data-baseweb="tab-list"] {gap: 0; border-bottom: 1px solid var(--line); flex-wrap: wrap;}
[data-baseweb="tab"] {padding: 8px 14px !important; background: transparent !important; height: auto !important; border-bottom: 2px solid transparent !important;}
[data-baseweb="tab"] p {font-size: .86rem; color: var(--muted);}
[data-baseweb="tab"][aria-selected="true"] {border-bottom-color: var(--gold) !important;}
[data-baseweb="tab"][aria-selected="true"] p {color: var(--strong);}
[data-baseweb="tab-highlight"], [data-baseweb="tab-border"] {display: none;}
[data-testid="stVerticalBlockBorderWrapper"] {border-radius: 6px; border-color: var(--line) !important;}
[data-testid="stHorizontalBlock"] {align-items: stretch;}
[data-testid="stExpander"] details {border-radius: 6px; border-color: var(--line); background: var(--panel);}
[data-testid="stMetricValue"] {font-family: var(--mono);}
[data-testid="stDataFrame"] {border: 1px solid var(--line); border-radius: 6px;}
[data-testid="stMain"] [role="radiogroup"] {gap: 0; flex-wrap: wrap;}
[data-testid="stMain"] [role="radiogroup"] label {margin: 0; padding: 4px 12px; border: 1px solid var(--line2); margin-right: -1px; background: var(--panel);}
[data-testid="stMain"] [role="radiogroup"] label > div:first-child {display: none;}
[data-testid="stMain"] [role="radiogroup"] label:has(input:checked) {background: var(--panel2); border-color: var(--gold); position: relative; z-index: 1;}
[data-testid="stMain"] [role="radiogroup"] label:has(input:checked) p {color: var(--gold2);}
.sec {display: flex; align-items: baseline; gap: 12px; margin: 30px 0 4px 0; padding-bottom: 8px; border-bottom: 1px solid var(--line);}
.sec .t {font-size: .78rem; font-weight: 600; letter-spacing: .16em; text-transform: uppercase; color: var(--strong);}
.sec-cap {color: var(--muted); font-size: .85rem; margin: 8px 0 14px 0; line-height: 1.5;}
.tbl {width: 100%; border-collapse: collapse; font-size: .86rem;}
.tbl th {text-align: left; font-size: .66rem; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); font-weight: 600; padding: 9px 12px; border-bottom: 1px solid var(--line2);}
.tbl td {padding: 10px 12px; border-bottom: 1px solid var(--line); color: var(--soft); vertical-align: top;}
.tbl td.num, .tbl th.num {text-align: right; font-family: var(--mono);}
.tbl a {color: var(--gold2); text-decoration: none;}
.tbl a:hover {text-decoration: underline;}
.tbl-wrap {border: 1px solid var(--line); border-radius: 6px; background: var(--panel); overflow-x: auto;}
.card {border: 1px solid var(--line); border-radius: 6px; padding: 14px 18px; margin-bottom: 12px; background: var(--panel);}
.card h4 {margin: 0 0 4px 0;}
.green {color: var(--up); border-color: rgba(47,191,155,.45); background: rgba(47,191,155,.08);}
.yellow {color: #e8b04b; border-color: rgba(232,176,75,.45); background: rgba(232,176,75,.08);}
.red {color: var(--down); border-color: rgba(240,97,109,.45); background: rgba(240,97,109,.08);}
.grey {background: var(--panel2);}
.tag {display: inline-flex; align-items: center; gap: 6px; font-size: .78rem; font-weight: 500; white-space: nowrap; margin-right: 12px; color: var(--soft); background: none !important; border: 0 !important; padding: 0;}
.tag::before {content: ""; width: 7px; height: 7px; border-radius: 50%; background: currentColor; flex-shrink: 0;}
.tag:last-child {margin-right: 0;}
.tag.grey {color: var(--muted);}
.tag.green {color: var(--up);}
.tag.yellow {color: #e8b04b;}
.tag.red {color: var(--down);}
.gl-group {font-size: .7rem; letter-spacing: .14em; text-transform: uppercase; color: var(--accent, #8be6f4); font-weight: 600; margin: 22px 0 6px 0;}
.gl {display: grid; grid-template-columns: minmax(180px, 260px) 1fr; border-top: 1px solid var(--line);}
.gl-t, .gl-e {padding: 10px 12px 10px 0; border-bottom: 1px solid var(--line); line-height: 1.55;}
.gl-t {font-weight: 600; color: var(--strong);}
.gl-e {color: var(--soft);}
@media (max-width: 760px) {
.gl {grid-template-columns: 1fr;}
.gl-t {border-bottom: 0; padding-bottom: 0;}
}
.muted {color: var(--muted); font-size: .86rem;}
.num {font-size: 1.3rem; font-weight: 500; font-family: var(--mono);}
.stats {display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); border: 1px solid var(--line); border-radius: 6px; background: var(--panel); margin: 6px 0 14px 0;}
.stat {padding: 12px 16px; border-right: 1px solid var(--line);}
.stat:last-child {border-right: 0;}
.stat .label {color: var(--muted); font-size: .7rem; letter-spacing: .1em; text-transform: uppercase;}
.stat .value {font-family: var(--mono); font-size: 1.25rem; font-weight: 500; line-height: 1.6; color: var(--strong);}
.stat .hint {color: var(--muted); font-size: .74rem;}
.small {font-size: .76rem;}
.block-container {padding-top: 3.4rem;}
.zlogo {display: flex; align-items: center; gap: 10px; white-space: nowrap; padding: 2px 0 1.1rem 0;}
[data-testid="stHorizontalBlock"]:has(.zlogo) > [data-testid="stColumn"]:first-child {overflow: visible;}
.zlogo .wordmark {font-size: 1.12rem; letter-spacing: .3em; font-weight: 800; line-height: 1;}
.zlogo .zsub {font-size: .58rem; letter-spacing: .34em; color: var(--muted); font-weight: 600; margin-top: 4px; white-space: nowrap;}
.zlogo .zsub span {display: inline-block; opacity: 0; animation: letter 12s ease-in-out infinite;}
[data-testid="stHorizontalBlock"]:has(.zlogo) {border-bottom: 1px solid var(--line); padding-bottom: 6px; margin-bottom: 0; gap: .6rem;}
[data-testid="stHorizontalBlock"]:has(.zlogo) [data-testid="stHorizontalBlock"] {gap: .15rem; border: 0; padding: 0;}
[data-testid="stHorizontalBlock"]:has(.zlogo) .stButton button {background: transparent; border: 0; border-bottom: 2px solid transparent; border-radius: 0; padding: 6px 4px; min-height: 40px; color: var(--soft);}
[data-testid="stHorizontalBlock"]:has(.zlogo) .stButton button p {font-size: .88rem; font-weight: 500; white-space: nowrap;}
[data-testid="stHorizontalBlock"]:has(.zlogo) .stButton button:hover {color: var(--strong); border-bottom-color: var(--line2);}
[data-testid="stHorizontalBlock"]:has(.zlogo) .stButton button[kind="primary"] {color: var(--strong); border-bottom-color: var(--gold); background: transparent;}
[data-testid="stHorizontalBlock"]:has(.zlogo) [data-baseweb="select"] > div {background: var(--panel); border-color: var(--line2); border-radius: 4px; min-height: 36px;}
[data-testid="stSidebar"] .zlogo {margin-top: 6px;}
.zlogo .zcopy {font-size: .55rem; letter-spacing: .14em; margin-top: 6px; font-weight: 600; white-space: nowrap; text-transform: uppercase; display: flex; align-items: center; gap: 6px; color: var(--muted);}
.zlogo .dmz {font-weight: 700; letter-spacing: .2em; color: var(--strong);}
[data-testid="collapsedControl"] {top: .6rem;}
[data-testid="stDialog"] [role="dialog"] {background: var(--panel); border: 1px solid var(--line2); border-radius: 8px;}
[data-baseweb="select"] > div {background: var(--panel) !important; border-color: var(--line2) !important;}
[data-testid="stAlert"] {border-radius: 6px;}
.tbl td.num, .tbl th.num {font-size: .84rem;}
.tbl td:first-child {white-space: nowrap;}
[data-testid="stHorizontalBlock"]:has(.zlogo) [class*="st-key-sw_"] button, [data-testid="stHorizontalBlock"]:has(.zlogo) .stButton button[title] {min-height: 34px;}
.sec {scroll-margin-top: 170px;}
#grafic {scroll-margin-top: 170px;}
.sidepanel {border: 1px solid var(--line); border-radius: 6px; background: var(--panel); padding: 10px 16px 12px; margin-bottom: 14px;}
.sp-h {font-size: .66rem; letter-spacing: .16em; text-transform: uppercase; color: var(--muted); font-weight: 600; padding: 2px 0 8px 0; border-bottom: 1px solid var(--line); margin-bottom: 2px;}
.sb-total {font-family: var(--mono); font-size: 2rem; color: var(--strong); margin: 8px 0 6px 0;}
.sb-total span {font-size: .9rem; color: var(--muted); margin-left: 4px;}
.sb-row {display: flex; justify-content: space-between; font-size: .82rem; color: var(--soft); margin-top: 8px;}
.sb-row b {font-family: var(--mono); font-weight: 500; color: var(--strong);}
.sec, #grafic {scroll-margin-top: 200px;}
@media (max-width: 760px) {
.block-container {padding-left: 1rem !important; padding-right: 1rem !important; padding-top: 3rem;}
[data-testid="stHorizontalBlock"]:has(.zlogo) [data-testid="stHorizontalBlock"] {flex-wrap: nowrap !important; overflow-x: auto; gap: .2rem !important;}
[data-testid="stHorizontalBlock"]:has(.zlogo) [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {flex: 0 0 auto !important; width: auto !important; min-width: auto !important;}
[data-testid="stHorizontalBlock"]:has(.zlogo) [data-testid="stHorizontalBlock"] .stButton button {padding: 6px 10px;}
[data-testid="stVegaLiteChart"], .tbl-wrap, [data-testid="stDataFrame"] {overflow-x: auto; max-width: 100%;}
}
[data-testid="stHorizontalBlock"]:has(.zlogo) .stButton button p {font-size: .84rem;}
.tbl td, .tbl th {border-left: 0 !important; border-right: 0 !important; border-top: 0 !important;}
.tbl th.num {font-size: .66rem !important; font-family: 'Inter', sans-serif !important;}
</style>
"""

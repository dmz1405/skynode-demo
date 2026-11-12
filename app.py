"""SKYNODE - demo public (doar in engleza).

Arata analiza completa pentru 3 companii (una Puternica, una De urmarit, una
Riscanta). Restul platformei (toate companiile, screener, alerte, watchlist,
verificarea pe istoric) e doar descris si apare blocat: codul lui nu exista aici.

Datele vin din date/demo.json: doar rezultatele gata calculate pentru cele 3 companii.
Graficele de pret sunt widget-urile oficiale TradingView, gratuite pentru orice site.

Rulare locala:  streamlit run app.py
"""
import html
import json
import random
from datetime import date
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

BRAND = "SKYNODE"      # numele produsului (mereu cu majuscule): schimbat doar aici
SEATS = 2              # cate persoane folosesc acum versiunea completa (de actualizat de mana)

st.set_page_config(page_title=f"{BRAND} · Demo", page_icon=str(Path(__file__).parent / "assets" / "icon.png"), layout="wide",
                   initial_sidebar_state="collapsed")

from src.dictionar import GLOSSARY  # noqa: E402
from src.stil import CSS           # noqa: E402
from src.tema import TEMA          # noqa: E402

st.markdown(CSS, unsafe_allow_html=True)
st.markdown(TEMA, unsafe_allow_html=True)   # tema SKYNODE, peste stilul de baza

DATA = json.loads((Path(__file__).parent / "date" / "demo.json").read_text(encoding="utf-8"))
COMPANIES = {c["ticker"]: c for c in DATA["companies"]}

# datele exportate sunt cu numele interne (romana); aici le afisam in engleza
# categoriile apar ca "sanatate financiara" (descriu cifrele firmei, nu ce sa faci cu actiunea)
CATEGORY = {"Puternica": ("Solid", "green"), "De urmarit": ("Mixed", "yellow"), "Riscanta": ("Fragile", "red")}
QUESTIONS = {"Creste repede?": "Revenue growing?", "Castiga bine din ce vinde?": "Healthy gross margin?",
             "Are bani destui?": "Enough cash on hand?", "Sefii cumpara actiuni?": "Insider purchases?",
             "Fara semne de pericol?": "No warning signs in filings?"}
DISCLAIMER = "Automated summary of public SEC filings, for information only. Not investment advice or a recommendation."
ANSWERS = {"Da": ("Yes", "green"), "Partial": ("Partly", "yellow"), "Nu": ("No", "red")}
SECTORS = {"ai_pur": "AI software", "infra_ai": "AI infrastructure (data centers, energy)", "cipuri": "Chips",
           "robotica": "Robotics", "medtech_ai": "Medicine + AI", "biotech_ai": "Biotech + AI",
           "cyber_ai": "Cybersecurity + AI", "cuantic": "Quantum computing"}
EVENTS = {"going_concern": "bankruptcy risk (going concern)", "8-K 3.01": "delisting warning",
          "8-K 4.02": "restated reports", "raport_intarziat": "late report", "8-K 4.01": "auditor changed",
          "8-K 1.03": "bankruptcy", "lockup": "lock-up expiry", "emisiune": "share issue (dilution)",
          "8-K 3.02": "unregistered share sale (dilution)"}
PAGES = ["Home", "Companies", "How it works", "Glossary", "About"]


# ---------------------------------------------------------------- ajutoare
def money(value) -> str:
    if value is None:
        return "-"
    sign = "−" if value < 0 else ""
    value = abs(value)
    if value >= 1e9:
        return f"{sign}${value / 1e9:,.2f}B"
    if value >= 1e6:
        return f"{sign}${value / 1e6:,.1f}M"
    return f"{sign}${value:,.0f}"


def pct(value) -> str:
    return "-" if value is None else f"{value * 100:+.0f}%"


def day(text: str) -> str:
    return date.fromisoformat(text[:10]).strftime("%b %d, %Y") if text else "-"


def tag(text: str, color: str) -> str:
    return f'<span class="tag {color}">{text}</span>'


def category_tag(name: str) -> str:
    return tag(*CATEGORY[name])


def event_name(kind: str) -> str:
    return EVENTS.get(kind, "heavy dilution" if kind.startswith("dilutie") else kind)


def section(title: str, caption: str = "") -> None:
    st.markdown(f'<div class="sec"><div class="t">{title}</div></div>'
                + (f'<div class="sec-cap">{caption}</div>' if caption else ""), unsafe_allow_html=True)


# ---------------------------------------------------------------- iconite (SVG simple, in loc de emoji)
def icon(name: str, size: int = 14) -> str:
    """Iconita mica, in culoarea de accent, aliniata cu textul."""
    paths = {
        "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
        "building": '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2M10 21v-3h4v3"/>',
        "users": '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14c2.8 0 5 2.2 5 5"/>',
    }
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="ic">{paths[name]}</svg>')


# ---------------------------------------------------------------- ferestre blocate (continut INVENTAT, doar ca imagine)
def _fake_ticker(rng) -> str:
    return "".join(rng.choice("ABCDEFGHKLMNPRSTVXZ") for _ in range(rng.choice((3, 4))))


def locked(title: str, note: str, inner: str) -> str:
    """O fereastra din versiunea completa: continut inventat, blurat, cu eticheta "Full version" deasupra."""
    return (f'<div class="lk"><div class="lk-h"><span>{title}</span><span class="lk-b">{icon("lock", 12)} Full version</span></div>'
            f'<div class="lk-in"><div class="blur">{inner}</div>'
            f'<div class="lk-ov"><b>{title}</b><span>{note}</span></div></div></div>')


def fake_table(seed: int, cols: list[str], rows: int = 6) -> str:
    rng = random.Random(seed)
    health = ["Solid", "Mixed", "Fragile"]
    body = ""
    for _ in range(rows):
        cells = [_fake_ticker(rng), rng.choice(health)] + [f"{rng.randint(-60, 140):+d}%" for _ in cols[2:]]
        body += "<tr>" + "".join(f'<td class="{"num" if i > 1 else ""}">{c}</td>' for i, c in enumerate(cells)) + "</tr>"
    head = "".join(f'<th class="{"num" if i > 1 else ""}">{c}</th>' for i, c in enumerate(cols))
    return f'<table class="tbl"><tr>{head}</tr>{body}</table>'


def fake_bars(seed: int, labels: list[str]) -> str:
    rng = random.Random(seed)
    return "".join(f'<div class="fb"><span>{l}</span><i style="width:{rng.randint(18, 96)}%"></i></div>' for l in labels)


def fake_timeline(seed: int, items: list[str], rows: int = 6) -> str:
    rng = random.Random(seed)
    return "".join(f'<div class="row">{rng.choice(["Jan", "Mar", "May", "Jul", "Sep", "Nov"])} {rng.randint(1, 28):02d} · '
                   f'<b>{_fake_ticker(rng)}</b> · {rng.choice(items)}</div>' for _ in range(rows))


def fake_columns(seed: int, n: int = 8) -> str:
    rng = random.Random(seed)
    return ('<div class="fc">' + "".join(f'<i style="height:{rng.randint(20, 100)}%"></i>' for _ in range(n)) + "</div>")


def go(page: str, ticker: str | None = None) -> None:
    st.session_state["page"] = page
    if ticker:
        st.session_state["ticker"] = ticker


def description(c: dict) -> tuple[str, str]:
    desc = c["description"].get("en")
    if desc:
        return desc[0], desc[1].split(":", 1)[-1].strip() if desc[1] else ""
    return (c.get("summary_en") or "-")[:400], ""


def logo_svg(size: int = 46) -> str:
    """Sigla: glob in vizor, cu un fascicul de radar care se roteste - un scanner global."""
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 48 48" aria-label="{BRAND}" style="overflow:visible">'
            '<defs><radialGradient id="lg-core" cx=".38" cy=".32" r=".9"><stop offset="0" stop-color="#12306e"/>'
            '<stop offset="1" stop-color="#050a16"/></radialGradient>'
            '<linearGradient id="lg-beam" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6aa8ff" stop-opacity="0"/>'
            '<stop offset="1" stop-color="#6aa8ff" stop-opacity=".85"/></linearGradient></defs>'
            # colturile vizorului
            '<path d="M3 12V3h9M36 3h9v9M45 36v9h-9M12 45H3v-9" fill="none" stroke="#6aa8ff" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/>'
            # globul: meridiane si paralele
            '<circle cx="24" cy="24" r="15" fill="url(#lg-core)" stroke="#2f7bff" stroke-width="2"/>'
            '<ellipse cx="24" cy="24" rx="6.5" ry="15" fill="none" stroke="#2f7bff" stroke-width="1.2" opacity=".9"/>'
            '<path d="M9 24h30M11 16.5h26M11 31.5h26" stroke="#2f7bff" stroke-width="1" opacity=".65"/>'
            # fasciculul radarului (se roteste)
            '<g class="sweep"><circle cx="24" cy="24" r="15" fill="none"/>'
            '<path d="M24 24 L24 9 A15 15 0 0 1 37 16.5 Z" fill="url(#lg-beam)" opacity=".9"/>'
            '<path d="M24 24 L37 16.5" stroke="#b8d4ff" stroke-width="1.4" stroke-linecap="round"/></g>'
            # nodul detectat
            '<circle cx="31" cy="19.5" r="2" fill="#ffffff"/><circle cx="31" cy="19.5" r="4" fill="#6aa8ff" opacity=".25"/>'
            '<circle cx="24" cy="24" r="1.6" fill="#b8d4ff"/></svg>')


def logo() -> str:
    return (f'<div class="zlogo">{logo_svg()}<div class="zname"><div class="wordmark">SKY<b>NODE</b></div>'
            '<div class="zsub">GLOBAL AI SCANNER</div>'
            f'<div class="zcopy">COPYRIGHT © {date.today().year} BY <span class="dmz">DMZ</span></div></div></div>')


SEAT_ICON = ('<svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="7" r="4.5"/>'
             '<path d="M3 22c0-5 4-8.5 9-8.5s9 3.5 9 8.5z"/></svg>')


# etichete scurte pentru matrice (un singur rand fiecare); intrebarile complete raman in profil
SHORT = {"Creste repede?": "Revenue growth", "Castiga bine din ce vinde?": "Gross margin",
         "Are bani destui?": "Cash runway", "Sefii cumpara actiuni?": "Insider buying",
         "Fara semne de pericol?": "Clean filings"}
GLYPH = {  # semnul din fiecare celula: bifa / liniuta / x (SVG, ca sa fie clare la orice marime)
    "green": '<path d="M5 12.5l4.2 4.2L19 7"/>',
    "yellow": '<path d="M6.5 12h11"/>',
    "red": '<path d="M7 7l10 10M17 7L7 17"/>',
}


def glyph(color: str, label: str = "") -> str:
    return (f'<span class="vx-g {color}" title="{label}" aria-label="{label}"><svg viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{GLYPH[color]}</svg></span>')


def scan_matrix() -> str:
    """Matricea de pe Home: cele 3 companii x cele 5 verificari, plus cate au trecut, evaluarea (blocata)
    si ultimul document depus. Totul din demo.json."""
    comps = DATA["companies"]
    last = [c["history"][-1] for c in comps]
    cells = ['<div class="vx-corner"></div>']
    for c, h in zip(comps, last):
        name, color = CATEGORY[h["category"]]
        cells.append(f'<div class="vx-co"><b>{c["ticker"]}</b><span class="vx-cat {color}">{name}</span></div>')
    for i, (q, _) in enumerate(last[0]["answers"]):
        cells.append(f'<div class="vx-l" title="{QUESTIONS.get(q, q)}">{SHORT.get(q, q)}</div>')
        for h in last:
            text, color = ANSWERS[h["answers"][i][1]]
            cells.append(f'<div class="vx-c">{glyph(color, f"{QUESTIONS.get(q, q)} {text}")}</div>')
    # verificarea de evaluare foloseste preturi: in demo ramane blocata
    cells.append(f'<div class="vx-l vx-locked">{icon("lock", 11)}Valuation</div>')
    cells += ['<div class="vx-c"><span class="vx-g vx-blur"></span></div>'] * len(comps)
    cells.append('<div class="vx-l vx-sum">Passed</div>')
    for h in last:
        yes = sum(1 for _, a in h["answers"] if a == "Da")
        n = len(h["answers"])
        color = CATEGORY[h["category"]][1]
        cells.append(f'<div class="vx-c vx-score"><b>{yes}<small>/{n}</small></b>'
                     f'<i class="vx-bar"><i class="{color}" style="width:{yes / n * 100:.0f}%"></i></i></div>')
    cells.append('<div class="vx-l">Last filing</div>')
    for c in comps:
        f = max(c["news"], key=lambda x: x["day"]) if c["news"] else None
        cells.append(f'<div class="vx-c vx-file"><b>{html.escape(f.get("form") or "8-K")}</b>{day(f["day"])[:6]}</div>'
                     if f else '<div class="vx-c vx-file">-</div>')
    legend = "".join(f'<span>{glyph(col)}{txt}</span>' for txt, col in ANSWERS.values())
    return ('<div class="vx">'
            f'<div class="vx-top"><span class="vx-title"><span class="live"></span>Latest scan</span>'
            f'<span class="vx-date">{day(DATA["updated"])}</span></div>'
            f'<div class="vx-grid">{"".join(cells)}</div>'
            f'<div class="vx-foot"><span class="vx-legend">{legend}</span>'
            f'<span class="vx-seats">{"".join(SEAT_ICON for _ in range(SEATS))}{SEATS} seats on the full version</span></div>'
            '</div>')


def feed_html() -> str:
    """Banda care curge: ultimele comunicate oficiale ale celor 3 companii (date reale din demo.json)."""
    items = sorted(((n["day"], c["ticker"], n) for c in DATA["companies"] for n in c["news"]),
                   key=lambda x: x[0], reverse=True)[:14]
    one = "".join(f'<span class="feed-i"><b>{tk}</b><span class="f">{html.escape(n.get("form") or "8-K")}</span>'
                  f'<i>{day(d)}</i>{html.escape((n.get("title") or n.get("items") or "")[:80]).replace("$", "&#36;")}</span>'
                  for d, tk, n in items)
    return f'<div class="feed"><div class="feed-track">{one}{one}</div></div>'


# ---------------------------------------------------------------- antet + meniu
st.session_state.setdefault("page", "Home")
st.session_state.setdefault("ticker", DATA["companies"][0]["ticker"])
head = st.columns([2.2, 1, 1.15, 1.25, 1, 1], gap="small", vertical_alignment="center")
head[0].markdown(logo(), unsafe_allow_html=True)
for col, page in zip(head[1:], PAGES):
    col.button(page, key=f"nav_{page}", width="stretch", on_click=go, args=(page,),
               type="primary" if st.session_state["page"] == page else "secondary")
st.markdown('<div class="topbar-line"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="demo-band"><span class="pill"><span class="live"></span>Public demo</span>'
            f'3 of the {DATA["tracked"]} companies we monitor · data as of {day(DATA["updated"])} · '
            f'{DISCLAIMER}</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------- Home
def page_home() -> None:
    left, right = st.columns([1.22, 1], gap="large", vertical_alignment="center")
    with left:
        st.markdown('<div class="hx"><span class="hx-eyebrow">AI company research<i></i>from official SEC filings</span>'
                    '<h1 class="hx-h">Every SEC filing, <em>scanned</em>.<br>Every AI company, explained.</h1>'
                    f'<p class="hx-p">{BRAND} reads what newly listed AI companies file with the SEC - financials, '
                    'insider trades, fund holdings, press releases - and turns it into a plain-language profile. '
                    'Every number links back to its official source.</p></div>', unsafe_allow_html=True)
        a, b, _ = st.columns([1.35, 1, .6], gap="small")
        a.button("Explore the 3 profiles  →", key="cta_main", type="primary", width="stretch",
                 on_click=go, args=("Companies",))
        b.button("How it works", key="cta_how", width="stretch", on_click=go, args=("How it works",))
        st.markdown('<div class="hx-src"><span>Reads</span>10-K<i></i>10-Q<i></i>8-K<i></i>Form 4<i></i>13F<i></i>'
                    '13D/G<i></i>S-3</div>', unsafe_allow_html=True)
    with right:
        st.markdown(scan_matrix(), unsafe_allow_html=True)
    st.markdown(feed_html(), unsafe_allow_html=True)
    stats = [("AI companies identified", f"{DATA['universe']:,}"), ("Tracked daily", f"{DATA['tracked']:,}"),
             ("Official SEC datasets", "7"), ("Open in this demo", "3")]
    st.markdown('<div class="stats">' + "".join(
        f'<div class="stat"><div class="label">{a}</div><div class="value">{b}</div></div>' for a, b in stats)
        + "</div>", unsafe_allow_html=True)

    section("The 3 companies in this demo", "Three different financial profiles, chosen to show how the analysis reads.")
    cols = st.columns(3, gap="medium")
    for col, c in zip(cols, DATA["companies"]):
        last = c["history"][-1]
        f = c["fundamentals"][-1] if c["fundamentals"] else {}
        color = CATEGORY[last["category"]][1]
        checks = "".join(f'<i class="{ANSWERS[a][1]}" title="{QUESTIONS.get(q, q)} {ANSWERS[a][0]}"></i>'
                         for q, a in last["answers"])
        yes = sum(1 for _, a in last["answers"] if a == "Da")
        runway = ("self-funded" if f.get("self_funded") else
                  f"{f['runway_months']:.0f} mo" if f.get("runway_months") is not None else "-")
        with col:
            st.markdown(f'<div class="ccard {color}"><div class="cc-top"><span class="tk">{c["ticker"]}</span>'
                        f'{category_tag(last["category"])}</div>'
                        f'<div class="nm">{c["name"].title()}</div>'
                        f'<div class="sl">{SECTORS.get(c["sector"], c["sector"])}</div>'
                        f'<div class="ds">{description(c)[0]}</div>'
                        f'<div class="cc-checks">{checks}</div>'
                        f'<div class="cc-cap">{yes} of {len(last["answers"])} checks passed</div>'
                        f'<div class="cc-fig"><div><span>Revenue</span><b>{money(f.get("revenue_ttm"))}</b></div>'
                        f'<div><span>Growth</span><b>{pct(f.get("revenue_growth"))}</b></div>'
                        f'<div><span>Runway</span><b>{runway}</b></div></div></div>', unsafe_allow_html=True)
            st.button("Open profile", key=f"open_{c['ticker']}", width="stretch",
                      on_click=go, args=("Companies", c["ticker"]))

    section("In the full version", "Available in the private app.")
    sectors = ["AI software", "AI infrastructure", "Chips", "Robotics", "Medicine + AI", "Cybersecurity", "Quantum"]
    a, b, c = st.columns(3, gap="medium")
    a.markdown(locked("Full company screener", f"All {DATA['tracked']} monitored companies, with filters and sorting.",
                      fake_table(7, ["Ticker", "Health", "Revenue / yr", "Margin"], 7)), unsafe_allow_html=True)
    b.markdown(locked("Sector overview", "How each AI sector's companies are doing, side by side.",
                      fake_bars(11, sectors)), unsafe_allow_html=True)
    c.markdown(locked("New filings feed", "Every new SEC filing across the monitored companies, as it lands.",
                      fake_timeline(13, ["new quarterly report", "insider filing", "fund holdings update",
                                         "press release", "ownership report"], 7)), unsafe_allow_html=True)
    groups = [
        ("Every monitored company",
         [f"Full profiles for all {DATA['tracked']} companies in the monitored range, refreshed every trading day",
          "Screener with filters by sector, financial health and listing type, shown as rows, cards or a table",
          "Side-by-side comparison of several companies, with the best value on each row highlighted"]),
        ("Deeper company profiles",
         ["Leadership: the CEO and the key people in each area, with their background",
          "Insider buying and selling from Form 4, with pre-scheduled sales kept apart",
          "Large funds (13F) and investors above 5% (13D/G), and how their stakes change"]),
        ("Alerts",
         ["A notification as soon as a company files something new with the SEC",
          "Early warnings: lock-up expiry dates, new share issues (dilution), going-concern doubts",
          "A short brief of what changed in the last few days, grouped by type"]),
        ("History and watchlists",
         ["The financial-health profile recalculated every month, using only what was public at the time",
          "What changed from one month to the next, and which filing changed it",
          "Personal watchlists, with alerts only for the companies you follow"]),
        ("Methodology and checks",
         ["The complete methodology, step by step, including its known limits",
          "Data-quality checks across filings, so one wrong number does not distort a profile",
          "Companies that later delisted stay in the data, so results are not flattered by survivors"]),
        ("Built for non-specialists",
         ["Every technical term explained in plain language, in a searchable glossary",
          "Available in English and Romanian",
          "Every figure links back to the official SEC document it came from"]),
    ]
    cards = "".join(f'<div class="lockc"><div class="lockc-h">{icon("lock")}<b>{title}</b></div>'
                    f'<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for title, items in groups)
    st.markdown(f'<div class="lockg">{cards}</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------- Companies
def tradingview(c: dict, height: int = 460) -> None:
    """The official TradingView chart (free widget; the price data comes from TradingView)."""
    exchange = {"nasdaq": "NASDAQ", "nyse": "NYSE"}.get((c.get("exchange") or "").lower(), "NASDAQ")
    config = {"width": "100%", "height": height - 10, "symbol": f"{exchange}:{c['ticker']}", "interval": "D",
              "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "backgroundColor": "#04070f",
              "gridColor": "rgba(106,168,255,0.07)", "hide_side_toolbar": True, "allow_symbol_change": False,
              "save_image": False}
    components.html(f"""<style>html, body {{margin: 0; background: #04070f;}}</style>
<div class="tradingview-widget-container">
<div class="tradingview-widget-container__widget"></div>
<script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
{json.dumps(config)}
</script></div>""", height=height)


def page_company() -> None:
    tickers = list(COMPANIES)
    pick = st.radio("Company", tickers, index=tickers.index(st.session_state["ticker"]), horizontal=True,
                    format_func=lambda t: f"{t} · {COMPANIES[t]['name'].title()}", label_visibility="collapsed")
    st.session_state["ticker"] = pick
    c = COMPANIES[pick]
    last = c["history"][-1]
    f = c["fundamentals"][-1] if c["fundamentals"] else {}
    alarms = "".join(tag(event_name(a), "red") for a in last["alarms"]) or tag("No alarms", "grey")
    st.markdown(f'<div class="cohead"><div class="id"><div class="tkbox">{c["ticker"]}</div><div>'
                f'<div class="nm">{c["name"].title()}</div><div class="meta">{SECTORS.get(c["sector"], c["sector"])} · '
                f'{c["listing_type"]} {day(c["listing_date"])} · {c["exchange"]}</div></div></div>'
                f'<div>{category_tag(last["category"])}{alarms}</div></div>', unsafe_allow_html=True)

    left, right = st.columns([2.2, 1], gap="large")
    with left:
        if st.session_state.get(f"chart_{pick}"):
            tradingview(c)
            st.caption("Chart and price data provided by TradingView, under its own terms and cookies.")
        else:
            st.markdown('<div class="chart-ph"><b>Price chart</b><div class="muted small">'
                        'Provided by TradingView. Loading it sets TradingView cookies.</div></div>', unsafe_allow_html=True)
            st.button("Load chart", key=f"load_{pick}", on_click=lambda: st.session_state.update({f"chart_{pick}": True}))
    with right:
        rows = "".join(f'<div class="sb-row"><span>{QUESTIONS.get(q, q)}</span>{tag(*ANSWERS[a])}</div>'
                       for q, a in last["answers"])
        st.markdown(f'<div class="sidepanel"><div class="sp-h"><span>Financial health</span><span>scan result</span></div>'
                    f'<div class="sb-total">{category_tag(last["category"])}</div>{rows}'
                    f'<div class="muted small" style="margin-top:10px">Describes the latest filed numbers. '
                    f'Not a view on the stock.</div></div>', unsafe_allow_html=True)

    section("Summary", "What the company does, for whom, and the numbers from its latest official report.")
    what, who = description(c)
    st.markdown(f'<div class="card"><div style="padding:4px 0">{icon("building")} <b>What it does:</b> {what}</div>'
                + (f'<div style="padding:4px 0">{icon("users")} <b>Customers / business:</b> {who}</div>' if who else "")
                + "</div>", unsafe_allow_html=True)
    if f:
        runway = ("self-funding" if f.get("self_funded") else
                  f"{f['runway_months']:.0f} months" if f.get("runway_months") is not None else "-")
        stats = [("Revenue (12 months)", money(f.get("revenue_ttm"))), ("Revenue vs last year", pct(f.get("revenue_growth"))),
                 ("Gross margin", "-" if f.get("gross_margin") is None else f"{f['gross_margin'] * 100:.0f}%"),
                 ("Operating cash flow", money(f.get("operating_cash_flow"))), ("Cash runway", runway),
                 ("Latest report", day(f.get("filed")))]
        st.markdown('<div class="stats">' + "".join(
            f'<div class="stat"><div class="label">{a}</div><div class="value" style="font-size:1.05rem">{b}</div></div>'
            for a, b in stats) + "</div>", unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3, gap="medium")   # nu "c": c e compania
    seed = sum(map(ord, pick))
    p1.markdown(locked("Peer comparison", "The company next to the other companies in its sector, metric by metric.",
                      fake_table(seed, ["Ticker", "Health", "Growth", "Margin"], 6)), unsafe_allow_html=True)
    p2.markdown(locked("Quarterly trends", "Revenue, margin and cash over the last eight quarters.",
                      fake_columns(seed + 1)), unsafe_allow_html=True)
    p3.markdown(locked("Fund ownership over time", "Funds entering and leaving, quarter by quarter (13F).",
                      fake_bars(seed + 2, ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"])), unsafe_allow_html=True)

    section("Financial health over time", "Recalculated at the start of each month, using only the filings public at the time.")
    names = ["Solid", "Mixed", "Fragile"]
    hist = pd.DataFrame([{"day": pd.to_datetime(h["day"]), "category": CATEGORY[h["category"]][0]} for h in c["history"]])
    st.altair_chart(alt.Chart(hist).mark_line(point=True, color="#6aa8ff", interpolate="step-after").encode(
        x=alt.X("day:T", title=None), y=alt.Y("category:N", title=None, sort=names, scale=alt.Scale(domain=names)),
        tooltip=[alt.Tooltip("day:T", title="Date", format="%b %d, %Y"), alt.Tooltip("category:N", title="Financial health")]
    ).properties(height=180, background="transparent"), width="stretch")

    a, b = st.columns(2, gap="large")
    with a:
        section("Insider activity", "Open-market trades reported by officers and directors over the last year "
                                    "(Form 4), excluding pre-scheduled sales. Shown in aggregate.")
        ins = c["insiders"]
        rows = [("Purchases", ins["purchases"]), ("Sales", ins["sales"])]
        st.markdown('<div class="tbl-wrap"><table class="tbl"><tr><th>Type</th><th class="num">Transactions</th>'
                    '<th class="num">Insiders</th><th class="num">Value</th></tr>'
                    + "".join(f'<tr><td>{t}</td><td class="num">{x["transactions"]}</td><td class="num">{x["people"]}</td>'
                              f'<td class="num">{money(x["value"]) if x["value"] else "-"}</td></tr>' for t, x in rows)
                    + "</table></div>", unsafe_allow_html=True)
        st.markdown(f'<div class="muted small">{c["people_count"]} officers and directors on record. Names are not '
                    f'shown in this demo; they are available in the original SEC filings.</div>', unsafe_allow_html=True)
    with b:
        section("Disclosed events", "Warning signs and notable events from official filings, last 2 years.")
        if c["events"]:
            st.markdown("".join(f'<div class="row">{day(e["day"])} · <b>{event_name(e["kind"])}</b></div>'
                                for e in c["events"]), unsafe_allow_html=True)
        else:
            st.info("No warning signs in the official filings.")

    a, b = st.columns(2, gap="large")
    with a:
        section("Major investors", "Firms and funds that have declared more than 5% of the company (13D / 13G).")
        if c["holders"]:
            st.markdown("".join(f'<div class="row"><b>{h["holder"]}</b> · {h["percent"] or 0:.1f}% '
                                f'<span class="muted small">({h["form"]}, {day(h["filed"])})</span></div>'
                                for h in c["holders"]), unsafe_allow_html=True)
        else:
            st.info("No investor above 5% declared.")
    with b:
        section("Big funds (13F)", "How many big funds hold shares, and the largest of them.")
        periods = c["funds"]["periods"]
        if periods:
            change = periods[0]["n"] - periods[1]["n"] if len(periods) > 1 else 0
            st.markdown(f'<div class="row"><b>{periods[0]["n"]}</b> funds ({change:+d} vs last quarter)</div>'
                        + "".join(f'<div class="row">{x["manager"]} <span class="muted small">· {x["shares"]:,.0f} '
                                  f'shares</span></div>' for x in c["funds"]["top"]), unsafe_allow_html=True)

    section("Official releases", "The latest announcements filed with the SEC (8-K / 6-K). The title opens the original.")
    st.markdown("".join(f'<div class="row">{day(n["day"])} · <a href="{n["url"]}" target="_blank">'
                        f'{(n["title"] or n["items"] or n["form"])[:160]}</a></div>' for n in c["news"]), unsafe_allow_html=True)
    st.markdown(f'<p style="margin-top:14px"><a href="{c["sec_url"]}" target="_blank">All of the company\'s SEC filings ↗</a></p>',
                unsafe_allow_html=True)


# ---------------------------------------------------------------- How it works
def page_method() -> None:
    st.markdown('<div class="hero" style="margin-top:10px"><div class="k">Methodology</div>'
                '<h1 style="font-size:2rem">From raw SEC filings to a structured company profile.</h1>'
                '<p>Company filings hold the facts that matter - revenue, cash, dilution, insider activity, going-concern '
                f'warnings - but they are long, technical and spread across dozens of forms. {BRAND} reads them '
                'automatically and reduces them to a profile you can scan in under a minute, with every figure traceable '
                'to its source.</p></div>', unsafe_allow_html=True)

    section("The pipeline", "Runs automatically on every trading day.")
    flow = [
        ("01", "Ingest", "New filings are pulled from SEC EDGAR for every AI company listed in the US over the past three "
                         "years - IPOs, SPAC mergers and direct listings, including companies that have since delisted.",
         "10-K · 10-Q · 20-F · 8-K · 6-K · Form 3/4 · 13D/G · 13F"),
        ("02", "Normalize and cross-check", "Financial statements are parsed from XBRL into comparable metrics, then "
                                            "checked against the other filings: insider filings (Form 4), fund holdings "
                                            "(13F), ownership reports (13D/G) and press releases (8-K). Insider "
                                            "transactions are de-duplicated, and pre-scheduled sales are separated.",
         "TTM revenue · growth · gross margin · operating cash flow · cash runway"),
        ("03", "Assess", "Five checks are applied to the latest filed figures and summarized as a financial-health "
                         "profile. Each assessment is point-in-time: it uses only what was public on that date.",
         "Solid · Mixed · Fragile"),
        ("04", "Monitor", "Profiles are recalculated every month, so you can see how a company's fundamentals have "
                          "changed - and what changed them.",
         "monthly history · event log · source links"),
    ]
    st.markdown('<div class="flow">' + "".join(
        f'<div class="fl"><div class="fl-n">{n}</div><div class="fl-b"><div class="fl-t">{t}</div>'
        f'<div class="fl-d">{d}</div><div class="fl-m">{m}</div></div></div>' for n, t, d, m in flow)
        + "</div>", unsafe_allow_html=True)

    section("The five checks", "What the financial-health profile is built from.")
    checks = [("Revenue growing?", "Trailing-twelve-month revenue versus the same period a year earlier.", "10-K / 10-Q (XBRL)"),
              ("Healthy gross margin?", "Share of revenue left after the direct cost of sales.", "10-K / 10-Q (XBRL)"),
              ("Enough cash on hand?", "Months of operation the current cash covers at the current burn rate.",
               "10-K / 10-Q (XBRL)"),
              ("Insider purchases?", "Open-market buying by officers and directors with their own money, last six months.",
               "Form 4"),
              ("No warning signs in filings?", "Going-concern doubts, delisting notices, restatements, auditor changes, "
                                               "heavy dilution.", "10-K / 10-Q · 8-K · S-3 / 424B")]
    st.markdown('<div class="tbl-wrap"><table class="tbl"><tr><th>Check</th><th>What it measures</th><th>Source</th></tr>'
                + "".join(f'<tr><td><b>{a}</b></td><td>{b}</td><td class="muted">{c}</td></tr>' for a, b, c in checks)
                + "</table></div>", unsafe_allow_html=True)
    st.caption("Thresholds and weighting are proprietary and part of the full version.")

    section("Design principles")
    principles = [("Point-in-time", "No hindsight: every historical profile uses only information that was public at "
                                    "that moment."),
                  ("Survivorship-free", "Delisted and failed companies stay in the dataset, so the record isn't "
                                        "flattered by the survivors."),
                  ("Source-linked", "Every figure can be traced back to an official SEC filing."),
                  ("Price-independent", "Profiles describe the business as reported. Share prices play no part.")]
    st.markdown('<div class="princ">' + "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in principles)
                + "</div>", unsafe_allow_html=True)

    section("Coverage")
    cover = [("AI companies identified", f"{DATA['universe']:,}"), ("Monitored daily", f"{DATA['tracked']:,}"),
             ("Sectors", "8"), ("Listing window", "3 years")]
    st.markdown('<div class="stats">' + "".join(
        f'<div class="stat"><div class="label">{a}</div><div class="value">{b}</div></div>' for a, b in cover)
        + "</div>", unsafe_allow_html=True)
    st.markdown('<div class="muted small">Monitored = market value between $50M and $2B when first tracked, with enough '
                'daily trading volume. Companies that later outgrow the range stay monitored.</div>',
                unsafe_allow_html=True)   # HTML, nu caption: in caption, textul dintre doua "$" devine formula

    a, b = st.columns(2, gap="medium")
    a.markdown(locked("Historical test", "How the financial-health profiles held up over time, point-in-time and "
                      "survivorship-free.", fake_columns(21, 9)), unsafe_allow_html=True)
    b.markdown(locked("Data-quality checks", "Coverage and consistency checks run on every update.",
                      fake_bars(23, ["Financial statements", "Insider filings", "Ownership reports", "Fund holdings",
                                     "Press releases", "Share issues"])), unsafe_allow_html=True)

    section("What this is not")
    st.markdown('<div class="card">A financial-health profile describes what a company has reported. It does not say '
                'whether its shares are worth buying or selling, at what price, or when - it ignores the share price, '
                'your objectives and your circumstances. ' + DISCLAIMER + '</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------- Glossary
def page_glossary() -> None:
    section("Glossary", "Every technical word and abbreviation on the site, explained simply.")
    search = st.text_input("Search a term", placeholder="e.g. EV/S, lock-up, 8-K", key="glossary_search")
    s = (search or "").strip().lower()
    for group, terms in GLOSSARY.items():
        rows = [(t, e) for t, e in terms if not s or s in t.lower() or s in e.lower()]
        if rows:
            st.markdown(f'<div class="gl-group">{group}</div><div class="gl">'
                        + "".join(f'<div class="gl-t">{t}</div><div class="gl-e">{e}</div>' for t, e in rows)
                        + "</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------- About
def page_about() -> None:
    st.markdown('<div class="hero" style="margin-top:10px"><div class="k">About</div>'
                '<h1 style="font-size:2rem">Making the public record of emerging AI companies readable.</h1>'
                '<p>Since 2023, more than a hundred AI companies have come to US markets through IPOs, SPAC mergers and '
                'direct listings. Most are small, young and thinly covered. What they disclose to the SEC is public - but '
                f'it is buried in long, technical documents that few people read. {BRAND} turns those filings into '
                'clear, structured, source-linked profiles, refreshed automatically.</p></div>', unsafe_allow_html=True)

    section("What it does")
    st.markdown('<div class="princ">'
                '<div><b>Profiles</b><span>What each company does, who it sells to, and how its finances look in the '
                'latest report.</span></div>'
                '<div><b>Insiders and ownership</b><span>Aggregated insider buying and selling, and the large '
                'investors and funds that hold the company.</span></div>'
                '<div><b>Disclosures</b><span>Official releases and warning signs - going-concern doubts, delisting '
                'notices, restatements, dilution - as they are filed.</span></div>'
                '<div><b>History</b><span>Month-by-month financial health, built point-in-time.</span></div>'
                '</div>', unsafe_allow_html=True)

    section("Status")
    st.markdown(f'<div class="card">{BRAND} is in active development. This public demo shows three of the '
                f'{DATA["tracked"]} companies monitored by the full platform, which remains private. Data as of '
                f'{day(DATA["updated"])}.</div>', unsafe_allow_html=True)

    section("Data")
    st.markdown('<div class="card">All company data comes from the <b>SEC</b> (the US Securities and Exchange '
                'Commission), the official regulator, through several independent datasets that are checked against each '
                'other: <ul style="margin:8px 0 8px 0;padding-left:18px;font-size:.92rem;line-height:1.7">'
                '<li><b>XBRL financial statements</b> reported by the company (10-K, 10-Q, 20-F)</li>'
                '<li><b>Insider filings</b> by officers and directors (Form 3, Form 4)</li>'
                '<li><b>Beneficial-ownership reports</b> by holders above 5% (Schedule 13D / 13G)</li>'
                '<li><b>Institutional holdings</b> reported by large funds (13F)</li>'
                '<li><b>Current reports and press releases</b> (8-K, 6-K)</li>'
                '<li><b>Share-issue filings</b> (S-3, 424B)</li>'
                '<li><b>The EDGAR filing index</b>, used to find new and delisted companies</li></ul>'
                'For example, revenue and cash from the XBRL statements are read alongside insider trades (Form 4), fund '
                'positions (13F) and the company\'s own announcements (8-K). <b>TradingView</b> provides the interactive '
                'price charts, loaded on request under TradingView\'s own terms.</div>', unsafe_allow_html=True)

    section("Disclosures")
    st.markdown(f'<div class="card"><ul style="margin:0;padding-left:18px;font-size:.92rem;line-height:1.7">'
                f'<li><b>Who:</b> {BRAND}, an independent project by DMZ (Romania). Not authorized or supervised '
                f'by the ASF or any financial regulator; not an investment firm.</li>'
                f'<li><b>Nature:</b> automated, general information, identical for every visitor. It is not personalized '
                f'and is not investment advice, a recommendation or an offer.</li>'
                f'<li><b>Method:</b> five checks on figures from several official SEC datasets, summarized as financial '
                f'health (see "How it works"). Share prices are not used.</li>'
                f'<li><b>Data date:</b> {day(DATA["updated"])}. Filings can be late or contain errors.</li>'
                f'<li><b>Conflicts of interest:</b> no payment is received from any company shown. The author may hold '
                f'shares in companies shown.</li>'
                f'<li><b>Privacy:</b> this site sets no cookies of its own and collects no data about visitors. It shows '
                f'no personal data about individuals: insider activity is aggregated and individual investors are not '
                f'named. TradingView charts load only on request.</li>'
                f'</ul></div>', unsafe_allow_html=True)

    section("Legal notice")
    st.markdown('<div class="card">The information presented is for informational and educational purposes only and '
                'does not constitute investment advice, a recommendation or an offer to buy or sell financial instruments. '
                'Data comes from public sources (SEC EDGAR, TradingView) and may contain errors or delays. Past performance '
                'does not guarantee future results. Any investment decision is solely yours, together with the associated '
                'risks.</div>', unsafe_allow_html=True)

    section("Terms of use")
    st.markdown(f'<div class="card">The content, analysis and design of this site are the property of the author. '
                f'Copying, reproducing or automatically extracting the data is prohibited without the author\'s written '
                f'consent. Copyright © {date.today().year} DMZ. All rights reserved.</div>', unsafe_allow_html=True)


{"Home": page_home, "Companies": page_company, "How it works": page_method,
 "Glossary": page_glossary, "About": page_about}[st.session_state["page"]]()
st.markdown(f'<div class="foot"><span>{DISCLAIMER}</span>'
            f'<span><b>SKYNODE</b> · © {date.today().year} DMZ</span></div>', unsafe_allow_html=True)

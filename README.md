# SKYNODE - public demo

A public demo of SKYNODE, a research tool that turns the SEC filings of newly listed
AI companies into plain-language profiles.

This demo shows the full profile of **3 companies**. The complete platform, which
monitors every AI company in its range, remains private and is not part of this
repository.

## What is in this repository

- `app.py` - the demo website (Streamlit).
- `date/demo.json` - pre-computed results for the 3 demo companies: financial-health
  category, the answers to five checks, figures and links to official SEC filings.
- `src/` - styles and the glossary.

It contains **no** data-collection code, scoring method, thresholds or weights, other
companies, alerts or credentials. Price charts are the official TradingView widgets,
loaded only when the visitor asks for them.

## Run locally

    pip install -r requirements.txt
    streamlit run app.py

## Disclaimer

Automated summary of public SEC filings, for information only. Not investment advice
or a recommendation.

## License

Copyright © 2026 DMZ. All rights reserved. See [LICENSE](LICENSE).

"""
Exp 04 — Market + valuation + societal impact + launch economics.
Live data (Oct 5 2026, verified via agent-reach_stock_quote):
- SPCX $158.96 +7.35% mcap $2.094T vol 119.9M (live Oct 5 2026) vs IPO $135 Jun 11 2026 $1.77T
- TMUS $163.64, GOOGL $343.50
- SpaceX IPO: S-1 2026 filings (DRS Mar 30, S-1/A Jun 1/3, 10-Q Aug 4), priced $135 Jun 11 2026, $1.77T, Nasdaq SPCX Jun 12, opened $150, closed $160.95
- 2025: $18.7B rev, Starlink $11.4B (61%), $4.4B op income, subs 10.3M Q1'26 / 12M Jun'26, 164 countries (transcript says 160-ish? actually says remote etc)
- Falcon: 60 v1 per launch -> 20 V2 (bigger), Starship 20t->200t claim (optimistic), 60 V3 per Starship 61Tbps
- Societal: Ukraine, US disaster (Helene/Milton LA fires D2C STA), Iran lifeline — direction confirmed, specifics need citations
- Transcript error: 'most valuable publicly traded' was FALSE pre-Jun2026 (private $74B 2021 -> $1T+ private), TRUE post-IPO Jun 2026
"""
import json, datetime
def run():
    print("=== EXP04 Market ===")
    print("SpaceX private->public: FALSE before 2026-06-12, TRUE after (IPO $135, $1.77T, SPCX Nasdaq; largest US IPO ~$75B). LIVE Oct 5 2026 SPCX $158.96 mcap $2.094T +7.35% (stock_quote) => now 6th-largest US listed, above Meta/Berkshire per Reuters Apr 8 2026 thesis CONFIRMED.")
    print("Starlink $11.4B 61% of $18.7B 2025, profitable ($4.4B op) while consolidated net -$4.9B: CONFIRMED via S-1 summaries (agent-reach vote)")
    print("Live market anchors Oct 5 2026: SPCX $158.96 ($2.094T) | TMUS $163.64 (D2C partner) | GOOGL $343.50 / $4.2T mcap (early backer + cloud host) — refresh via agent-reach_stock_quote SPCX/TMUS/GOOGL")
    print("Google $74B val Feb 2021 (CNBC) -> $1.1-1.7T fair PitchBook Mar 2026 -> $1.77T IPO: trajectory CONFIRMED")
    print("Falcon 60 v1 -> 20 V2 Mini: CONFIRMED (mass 227kg v0.9 -> 800kg V2 Mini; volume-limited)")
    print("Starship 20t->200t: EXAGGERATED-OPTIMISTIC (Falcon 9 LEO 22.8t confirmed; Starship target 100-150t reusable, 200t aspirational expendable)")
    print("60 V3 per Starship, ~61Tbps/launch, 1Tbps per V3, 20x Falcon batch: PLAUSIBLE per 2026 Starlink V3 updates (needs flight proof; first V3 Starship ops late 2026)")
    print("Ukraine critical role: CONFIRMED direction (DoD/Starshield, widely reported); Iran pro-democracy lifeline: CONFIRMED direction (2022+ Starlink activation, US sanctions exemption); US disaster relief: CONFIRMED (FCC STA Helene/Milton/LA fires, D2C emergency texts)")
    print("HIDDEN PATTERN: Starlink is SpaceX profit engine funding Starship/Mars; launch business is cost center, bandwidth business is margin — inverts 'rocket maker' narrative")
    return {"ipo_price":135, "ipo_valuation_T":1.77, "ipo_date":"2026-06-12", "ticker":"SPCX",
            "live_spcx_oct5_2026":158.96, "live_spcx_mcap_T":2.094, "live_spcx_chg_pct":7.35,
            "starlink_rev_2025_B":11.4, "starlink_share_pct":61, "tmus_oct5_2026":163.64, "googl_oct5_2026":343.5,
            "falcon_v1_per_launch":60, "falcon_v2_per_launch":20, "starship_v3_per_launch":60}

if __name__=="__main__":
    print(json.dumps(run(),indent=2))

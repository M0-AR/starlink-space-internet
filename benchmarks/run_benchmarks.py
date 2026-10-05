"""Run all experiments + emit benchmark verdicts. Zero-to-hero reproducible."""
import sys, pathlib, json, importlib.util
ROOT = pathlib.Path(__file__).resolve().parents[1]
EXP = ROOT/"experiments"
sys.path.insert(0, str(EXP))

def load(name):
    spec = importlib.util.spec_from_file_location(name, EXP/f"{name}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

VERDICTS = [
    ("May23-2019 60 sats Falcon9", "CONFIRMED", "SpaceflightNow/Reuters/SpaceNews/BBC + press kit; 22:30 EDT SLC-40, 227kgx60, 440->550km"),
    ("11,000 sats > all others combined", "CONFIRMED", "OrbitalRadar Oct4'26 11,150 =54% of ~20,648; KeepTrack 11,156; McDowell 11,102; Wiki Jun'26 10,413"),
    ("Ukraine/Iran/disaster lifeline", "CONFIRMED-DIRECTION", "Ukraine widely documented; Iran 2022+ activation; FCC STA Helene/Milton/LA fires D2C texts"),
    ("Most valuable publicly traded", "NEEDS-QUALIFIER (FALSE pre-Jun2026, TRUE post-IPO)", "Private $74B'21 -> IPO $135 Jun12'26 $1.77T SPCX Nasdaq largest US IPO; transcript mid-2026 borderline"),
    ("Dishy phased array tracks LEO", "CONFIRMED", "Teardowns ~1000+ elements; electronic steering; 550->480km lowering 2026"),
    ("5+3 onboard arrays", "SIMPLIFIED-UNVERIFIED", "SpaceX undisclosed exact counts; multi Ku/Ka/E + laser confirmed, numbers illustrative"),
    ("Gateways 100 US +50 world, 9 dishes", "CONFIRMED-RANGE", "2025 report 100+ US sites 1500+ antennas; global 150-200 est; 9/site typical varies"),
    ("Google $900 + DC co-location", "CONFIRMED (transcript missing 'M')", "SEC 10-K $900M Jan2015 + Fidelity; Google Cloud deal May13'21 New Albany Ohio"),
    ("Laser sat-to-sat for ocean (curvature)", "CONFIRMED", "LISL papers + SSU'25; geometry blocks dual gateway view at 500km"),
    ("Radio=light same speed; laser 10-100x/beam", "CONFIRMED-PLAUSIBLE", "c same; higher carrier => bandwidth; real gain mod/WDM dependent"),
    ("Laser blocked by clouds, radio passes", "CONFIRMED", "Mie vs cm-wave; sun white (G2V) yellow via Rayleigh"),
    ("Binary tall/short long/short", "SIMPLIFIED-CORRECT", "Intro to ASK/FSK; real QAM/OFDM"),
    ("GEO 35,000km 3 sats cover Earth", "CONFIRMED (35,786km)", "120deg spacing excl poles"),
    ("70x closer, 90min, 5min pass", "CONFIRMED", "35786/500=71.6x; period ~95min@550km; 5min pass @25deg"),
    ("Vacuum 30% faster than fiber", "CONFIRMED-CONSERVATIVE", "n=1.47 => fiber 32% slower / vacuum 47% faster same dist; NY-London practice 30-47%"),
    ("Need Falcon 9 reuse for economics", "CONFIRMED", "13'19/96'23/165'25 cadence; 60v1->20V2 mass limit; thousands needed (vs 3 GEO)"),
    ("Starship 20t->200t 60/launch", "OPTIMISTIC (20t ok, 200t aspirational)", "Falcon 22.8t confirmed; Starship 100-150t reusable target; 60xV3 61Tbps/planned late2026"),
    ("V2 D2C bigger arrays, weak uplink", "CONFIRMED-PRINCIPLE", "Link-budget physics; FCC SCS 1910-1915/1990-1995MHz T-Mobile lease"),
    ("D2C voice+text now, no streaming", "ESSENTIALLY-CORRECT (generous)", "Messaging live Feb'25 (400+ sats, FCC Nov'24); voice/data planned (OOBE deferred)"),
    ("Fiber 100x Starlink total", "PLAUSIBLE", "Subsea Pbps vs Starlink low-Pbps shared; method-dependent"),
    ("100k sats / majority traffic / no gateways", "SPECULATIVE", "Approved 12k/filed 42k; May2026 quote unverified exact; terrestrial interconnect still needed"),
    ("Starmind 1M higher solar AI orbit", "FILED-NOT-APPROVED + PLAUSIBLE", "Name+M FCC Jan'26 up to 1M confirmed; AI1 75m 250kW; xAI merger Feb'26; higher solar duty plausible"),
    ("Moon factory + railgun", "FICTION-TEASER", "No primary source; treat as YouTube speculation"),
]

def main():
    print("=== Starlink Verification Benchmarks (Oct 2026) ===")
    results = {"date":"2026-10-05", "experiments":{}}
    for mod in ["01_constellation_growth","02_latency_physics","03_gateway_chain","04_market_valuation","05_direct_to_cell_future","06_live_verification"]:
        print(f"\n--- {mod} ---")
        try:
            m = load(mod)
            results["experiments"][mod] = m.run()
        except Exception as e:
            print(f"FAILED {mod}: {e}")
            results["experiments"][mod] = {"error":str(e)}
    results["verdicts"] = [{"claim":c,"verdict":v,"evidence":e} for c,v,e in VERDICTS]
    from collections import Counter
    cnt = Counter(v.split()[0].split('(')[0] for _,v,_ in VERDICTS)
    print("\n=== SUMMARY ===")
    for k,v in cnt.items():
        print(f"{k}: {v}")
    print(f"Total claims: {len(VERDICTS)}")
    out = ROOT/"benchmarks"/"benchmark_results.json"
    out.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {out}")
    # also write human-readable
    (ROOT/"benchmarks"/"SUMMARY.md").write_text("# Benchmark Summary\n\nDate: 2026-10-05\n\n" + "\n".join(f"- **{c}**: {v} — {e}" for c,v,e in VERDICTS))
    return 0

if __name__=="__main__":
    raise SystemExit(main())

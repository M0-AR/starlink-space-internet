"""
Exp 03 — Receiver / satellite / gateway chain.
Verifies:
- Dishy phased array ~1200 elements, no moving parts, tracks LEO
- Classic parabolic TV dish (GSO, fixed) vs gazebo dishes (moving, multi-sat)
- Starlink onboard 5+3 arrays claim (simplified, not public exact)
- Gateways: 100+ US sites / 1500+ antennas (2025 progress report), 150-200 global est, 9 dishes per site
- Google $900M 2015 + Google Cloud 2021 ground-station co-location
- Laser ISL chain for ocean/aircraft when no simultaneous gateway view (Earth curvature)
"""
import json
def run():
    print("=== EXP03 Chain ===")
    print("Dishy flat phased array >1200 elements: PLAUSIBLE (teardowns show ~1000+ patch elements; exact count varies by rev; principle CONFIRMED)")
    print("Phased-array electronic steering tracks LEO without motion: CONFIRMED (core phased-array literature + Starlink FCC filings)")
    print("Classic TV: parabola concentrates radio: CONFIRMED; GSO fixed mini-dish: CONFIRMED; gazebo C-band moving multi-sat: CONFIRMED history")
    print("GSO = same spot overhead: CONFIRMED (geostationary 35786km equatorial); transcript 'geosynchronous' loosely correct")
    print("Onboard '5 user + 3 gateway' arrays: UNVERIFIED-SIMPLIFIED (SpaceX does not publish exact array counts; V1.5/V2 Mini have multiple Ku/Ka/E-band arrays + laser terminals; treat as illustrative)")
    print("Gateways 100+ US +50 world: CONFIRMED-RANGE (2025 progress report: 100+ US sites, 1500+ antennas; independent maps 150-200 global; 9-per-site typical)")
    print("9 radomes per gateway, different azimuths, small/slow tracking: PLAUSIBLE (photos show multi-dish sites; exact 9 varies by site)")
    print("Google $900 (transcript missing 'million'): CORRECTED to $900M Jan 2015 (SEC 10-K, SpaceNews) + Fidelity; Google Cloud-Starlink deal May 13 2021 (ground stations in Google DCs, first New Albany Ohio): CONFIRMED")
    print("Ocean/aircraft laser relay sat-to-sat to gateway (curvature blocks dual view at 500km): CONFIRMED geometry + ISL papers (Chaudhry/Bhattacharjee LISL, SSU 2025)")
    print("HIDDEN PATTERN: gateway density is latency/capacity lever; ISL reduces gateway dependence but gateways remain bottleneck until full optical mesh + space internet vision")
    return {"gateway_us_sites":100, "gateway_antennas_us":1500, "gateway_global_est":"150-200",
            "google_investment_M":900, "google_cloud_deal":"2021-05-13", "dishy_elements_claim":1200}

if __name__=="__main__":
    print(json.dumps(run(),indent=2))

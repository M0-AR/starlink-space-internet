"""Generate docs/demo.gif from verified timeline (same numbers as experiments/01)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter, FuncAnimation

years = [2019,2020,2021,2022,2023,2024,2025,2026]
counts = [120,1000,1900,3500,5000,6400,9400,11150]

fig, ax = plt.subplots(figsize=(6,3.4), dpi=150)
fig.patch.set_facecolor("#0b1326"); ax.set_facecolor("#0b1326")

def draw(n):
    ax.clear()
    ax.set_facecolor("#0b1326")
    ax.plot(years[:n], counts[:n], marker="o", linewidth=2.5)
    ax.fill_between(years[:n], counts[:n], alpha=0.15)
    for x,y in zip(years[:n], counts[:n]):
        ax.text(x, y+350, f"{y:,}", ha="center", fontsize=8, color="white")
    ax.set_xlim(2018.7,2026.3); ax.set_ylim(0,12500)
    ax.set_xticks(years); ax.set_ylabel("active satellites", color="#9fb0d0")
    ax.set_title(f"Starlink growth — 60 dots (2019) → 11,150 (2026)  |  frame {n}/{len(years)}", color="white", fontsize=10)
    ax.tick_params(colors="#9fb0d0")
    for s in ax.spines.values():
        s.set_color("#1e2c4d")

anim = FuncAnimation(fig, draw, frames=len(years)+1, interval=700)
anim.save("docs/demo.gif", writer=PillowWriter(fps=1.4))
print("wrote docs/demo.gif")

#!/usr/bin/env python3
"""Plot exact Bloch geometry and support deficits, not empirical protocol costs."""
from pathlib import Path
import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def deficit(eta, theta):
    a = 1.0 - eta
    numerator = a * (2.0 * np.sin(theta / 2.0) ** 2) ** 2
    denominator = (1.0 - a * np.cos(theta)
                   + np.sqrt(eta * np.sin(theta) ** 2
                             + eta ** 2 * np.cos(theta) ** 2))
    return numerator / denominator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1]
                        / "figures" / "amplitude_geometry.svg")
    parser.add_argument("--preview", type=Path)
    args = parser.parse_args()
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "svg.hashsalt": "channel-cost-geometry-v1"})
    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.5),
                             gridspec_kw={"width_ratios": [1, 1.15]},
                             constrained_layout=True)
    phases = np.linspace(0.0, 2.0 * np.pi, 1001)
    angles = np.geomspace(1e-3, 0.6, 401)
    etas = (0.2, 0.5, 0.8)
    colors = ("#18857d", "#345da7", "#8651a6")
    ax = axes[0]
    ax.plot(np.sin(phases), np.cos(phases), color="#555555", lw=1.2,
            ls="--", label="Pure-state boundary")
    for eta, color in zip(etas, colors):
        ax.plot(np.sqrt(eta) * np.sin(phases),
                1 - eta + eta * np.cos(phases), color=color, lw=2,
                label=fr"Survival $\eta={eta}$")
    ax.scatter([0], [1], s=26, c="#222222", zorder=5)
    ax.set(xlabel="Bloch coordinate x", ylabel="Bloch coordinate z",
           title="A. One pure output remains", xlim=(-1.08, 1.08),
           ylim=(-1.08, 1.14))
    ax.set_aspect("equal")
    ax.legend(loc="lower left", fontsize=8, frameon=True,
              facecolor="white", edgecolor="none", framealpha=0.96)
    ax = axes[1]
    for eta, color in zip(etas, colors):
        ax.loglog(angles, deficit(eta, angles), color=color, lw=2,
                  label=fr"$\eta={eta}$")
    ax.loglog(angles, angles ** 4 / 8.0, color="#777777", lw=1.4,
              ls="--", label=r"$\theta^4/8$ (reference slope)")
    ax.set(xlabel=r"Polar normal angle $\theta$ (radians)",
           ylabel=r"Support deficit $1-h_\eta(\theta)$",
           title="B. Quartic contact at that output")
    ax.grid(True, which="major", alpha=0.18)
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, metadata={"Date": None})
    if args.output.suffix.lower() == ".svg":
        args.output.write_text("\n".join(line.rstrip() for line in
                                          args.output.read_text().splitlines()) + "\n")
    if args.preview:
        args.preview.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.preview, dpi=170)
    plt.close(fig)
    print(args.output)


if __name__ == "__main__":
    main()

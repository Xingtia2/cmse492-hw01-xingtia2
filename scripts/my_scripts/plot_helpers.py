from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def make_revenue_plot(summary_df: pd.DataFrame, out_path: Path) -> None:
    revenue_by_region = (
        summary_df.groupby("region", as_index=False)["total_revenue"]
        .sum()
        .sort_values("total_revenue", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(revenue_by_region["region"], revenue_by_region["total_revenue"], color="#3b82f6")
    ax.set_title("Revenue by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Revenue (USD)")
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def make_revenue_share_plot(region_df: pd.DataFrame, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 4))

    sns.barplot(
        data=region_df,
        x="region",
        y="revenue_share_pct",
        ax=ax,
        color="#10b981"
    )

    ax.set_title("Revenue Share by Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Revenue Share (%)")
    ax.grid(axis="y", alpha=0.2)

    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)
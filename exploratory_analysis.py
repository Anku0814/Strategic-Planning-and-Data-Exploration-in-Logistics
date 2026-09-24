"""
Task 1 - Exploratory Analysis Starter Script
Indian Rail Freight Movement, DGCIS 2024-25

This script demonstrates the proposed analysis workflow.
Update the file path and column names after downloading and
checking the detailed DGCIS statistical table.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


FILE_PATH = "DGCIS_Rail_2024_25.xlsx"


def load_data(path):
    """Load the downloaded DGCIS table."""
    df = pd.read_excel(path)

    # Standardize column names for easier processing.
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def basic_checks(df):
    """Run simple data-quality checks."""
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nFirst five rows:")
    print(df.head())


def state_freight_analysis(df):
    """
    Example state-level aggregation.

    Change 'state' and 'quantity_tonnes' to the actual
    column names in the downloaded DGCIS table.
    """
    state_freight = (
        df.groupby("state", as_index=False)["quantity_tonnes"]
        .sum()
        .sort_values("quantity_tonnes", ascending=False)
    )

    total = state_freight["quantity_tonnes"].sum()

    state_freight["share_pct"] = (
        state_freight["quantity_tonnes"] / total * 100
    )

    return state_freight


def plot_top_states(state_freight):
    """Plot the ten largest states by freight movement."""
    top = state_freight.head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(top["state"], top["quantity_tonnes"])
    plt.title("Top States by Rail Freight Movement")
    plt.xlabel("State")
    plt.ylabel("Freight (tonnes)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def origin_destination_matrix(df):
    """
    Build an origin-destination matrix.

    Required columns:
    origin_state, destination_state, quantity_tonnes
    """
    return pd.pivot_table(
        df,
        values="quantity_tonnes",
        index="origin_state",
        columns="destination_state",
        aggfunc="sum",
        fill_value=0,
    )


def plot_od_matrix(od):
    """Visualize origin-destination freight flows."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(od)
    plt.title("Inter-State Rail Freight Flow Matrix")
    plt.xlabel("Destination State")
    plt.ylabel("Origin State")
    plt.tight_layout()
    plt.show()


def cluster_states(state_freight, n_clusters=4):
    """
    Simple K-Means example.

    More meaningful clustering should use several state-level
    features such as inward, outward, internal and commodity shares.
    """
    features = state_freight[["quantity_tonnes", "share_pct"]]

    scaled = StandardScaler().fit_transform(features)

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10,
    )

    result = state_freight.copy()
    result["cluster"] = model.fit_predict(scaled)

    return result


if __name__ == "__main__":
    # The following calls assume the downloaded table has
    # been mapped to the example column names above.

    rail = load_data(FILE_PATH)
    basic_checks(rail)

    # Uncomment after confirming column names:
    #
    # state_freight = state_freight_analysis(rail)
    # print(state_freight.head(10))
    # plot_top_states(state_freight)
    #
    # od = origin_destination_matrix(rail)
    # plot_od_matrix(od)
    #
    # clustered = cluster_states(state_freight)
    # print(clustered.head(10))

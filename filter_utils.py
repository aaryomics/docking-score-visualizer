import pandas as pd

def filter_by_rmsd(df, max_rmsd=2.0):
    """Return only ligands with RMSD ≤ max_rmsd (default = 2.0)."""
    if "rmsd" in df.columns:
        return df[df["rmsd"] <= max_rmsd]
    return df  # If RMSD not present, return original

def get_top_n_affinities(df, n=5):
    """Return top N ligands with best (most negative) binding affinity."""
    return df.nsmallest(n, "binding_affinity")

def export_to_csv(df, filename="filtered_results.csv"):
    """Export filtered DataFrame to CSV."""
    df.to_csv(filename, index=False)
    print(f"Exported to {filename}")

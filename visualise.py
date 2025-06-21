import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_affinities(df, title="Binding Affinity per Ligand"):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x="ligand_name", y="binding_affinity", palette="viridis", ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_ylabel("Binding Affinity (kcal/mol)")
    ax.set_title(title)
    st.pyplot(fig)

def plot_affinity_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["binding_affinity"], bins=10, kde=True, ax=ax)
    ax.set_xlabel("Binding Affinity (kcal/mol)")
    ax.set_title("Binding Affinity Distribution")
    st.pyplot(fig)

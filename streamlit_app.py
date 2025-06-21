import streamlit as st
import pandas as pd
import tempfile

from parser import parse_docking_file
from visualise import (
    plot_affinities,
    plot_affinity_distribution,
)
from filter_utils import (
    filter_by_rmsd,
    get_top_n_affinities,
)

st.set_page_config(page_title="Docking Score Visualiser", layout="wide")
st.markdown("""
<style>
h1 {
    font-size: 2.8rem;
    color: #0f4c5c;
}
.section-title {
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 1.5em;
    color: #264653;
}
hr {
    margin-top: 2em;
    margin-bottom: 2em;
}
</style>
""", unsafe_allow_html=True)

st.title("Protein-Ligand Docking Score Visualiser")
st.markdown("Upload your docking results below to explore **binding affinities** and identify top ligands based on RMSD and energy scores.")
st.markdown("---")

#Sidebar
with st.sidebar:
    st.header("📁 Upload Docked File")
    uploaded_file = st.file_uploader("Upload `.csv`, `.txt`, or `.pdbqt`", type=["csv", "txt", "pdbqt"])
    st.markdown("Accepted formats: PyRx CSV, AutoDock Vina logs, etc.")
    st.markdown("---")

#Main Workflow
if uploaded_file is not None:
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        df = parse_docking_file(tmp_path)
        st.success("File parsed successfully!")
        st.subheader("Raw Parsed Data")
        st.dataframe(df)

        left, right = st.columns(2)

        with left:
            st.subheader("📊 Binding Affinity Bar Chart")
            plot_affinities(df)

        with right:
            st.subheader("📈 Affinity Distribution")
            plot_affinity_distribution(df)

        st.markdown("---")

        #Filters
        st.subheader("🎯 Ligand Filtering")

        rmsd_thresh = st.slider("Maximum RMSD", 0.0, 5.0, 2.0, 0.1)
        top_n = st.slider("Top N ligands by best affinity", 1, 20, 5)

        filtered = filter_by_rmsd(df, max_rmsd=rmsd_thresh)
        top_hits = get_top_n_affinities(filtered, n=top_n)

        st.write(f"### Top {top_n} Ligands (RMSD ≤ {rmsd_thresh})")
        st.dataframe(top_hits)

        #Export
        csv = top_hits.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Download Filtered Results as CSV",
            data=csv,
            file_name="top_ligands.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Error parsing file: {e}")

import pandas as pd
import re
import streamlit as st

def parse_docking_file(file_path):
    st.info(f"🔍 Trying to parse uploaded file...")

    try:
        df = pd.read_csv(file_path, encoding="utf-8-sig")
        st.write("🧪 First 5 rows of raw file:")
        st.dataframe(df.head())

        # Normalize column names
        df.columns = [col.strip().lower() for col in df.columns]
        st.write("✅ Normalized column names:", df.columns.tolist())

        # Fuzzy matching for expected columns
        ligand_col = next((col for col in df.columns if "ligand" in col or "name" in col), None)
        affinity_col = next((col for col in df.columns if "affinity" in col or "score" in col), None)
        rmsd_col = next((col for col in df.columns if "rmsd" in col and "lb" in col), None)

        if ligand_col and affinity_col:
            df_out = pd.DataFrame()
            df_out["ligand_name"] = df[ligand_col]
            df_out["binding_affinity"] = df[affinity_col]
            df_out["rmsd"] = df[rmsd_col] if rmsd_col else None

            return df_out
        else:
            st.warning("CSV loaded, but no matching 'ligand' or 'affinity' columns found.")

    except Exception as e:
        st.warning(f"CSV parser failed: {e}")

    st.warning("Trying plain text fallback parser...")

    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        results = []
        current_ligand = "ligand"

        for line in lines:
            if "REMARK" in line and "Name" in line:
                match = re.search(r"Name:\s*(\S+)", line)
                if match:
                    current_ligand = match.group(1)

            if "VINA RESULT" in line:
                numbers = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                if len(numbers) >= 2:
                    results.append({
                        "ligand_name": current_ligand + f"_{len(results)+1}",
                        "binding_affinity": float(numbers[0]),
                        "rmsd": float(numbers[1])
                    })

        if results:
            return pd.DataFrame(results)

    except Exception as e:
        st.error(f"Plain text fallback parser error: {e}")

    raise ValueError("Unsupported or unrecognized file format.")

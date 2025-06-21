# docking-score-visualizer
A Streamlit-based interactive tool to visualize and analyze molecular docking results from tools like **AutoDock Vina** and **PyRx**. Upload your `.csv` or `.txt` docking output, explore ligand binding affinities, and filter top-performing ligands by RMSD and energy scores.
Ideal for computational biology, bioinformatics, or drug discovery projects!

# Live App
[Click here to try it live](https://docking-score-visualizer-qsmlctfnr89h4qqmefktdm.streamlit.app/)  
![image](https://github.com/user-attachments/assets/805a5f73-d63a-4132-ba62-ff316370626f)
![image](https://github.com/user-attachments/assets/ad7ba622-3d7a-465b-9734-a4749c9736e8)


# Features
- Upload docking results from `.csv`, `.txt`, or `.pdbqt` logs  
- Automatic file format detection (PyRx, Vina, etc.)
- Visualize binding affinities with bar & histogram plots
- Filter ligands by RMSD threshold and get top N hits
- Download filtered ligands as CSV
- Clean UI with sidebar upload + dual chart layout


# Example Inputs
Supports:
- PyRx CSV export
- Vina `.pdbqt` result logs (with `VINA RESULT:` lines)
- Custom text outputs (with `REMARK Name:` and `VINA RESULT:`)

# Tech Stack
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn + Matplotlib](https://seaborn.pydata.org/)

# Run Locally
```bash
git clone https://github.com/yourusername/docking-score-visualizer.git
cd docking-score-visualizer
pip install -r requirements.txt
streamlit run streamlit_app.py


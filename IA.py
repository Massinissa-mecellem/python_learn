import pandas as pd

# Charger le fichier Excel
excel_file = "dataset_quiz_p1.xlsx"

# Si vos tables sont dans des onglets séparés :
df_bien = pd.read_excel(excel_file, sheet_name="bien_immo")
df_trans = pd.read_excel(excel_file, sheet_name="transaction")
df_insee = pd.read_excel(excel_file, sheet_name="indice_insee")

# Exporter chaque dataframe en fichier CSV (séparateur virgule)
df_bien.to_csv("bien_immo.csv", index=False, encoding="utf-8")
df_trans.to_csv("transactions.csv", index=False, encoding="utf-8")
df_insee.to_csv("indice_insee.csv", index=False, encoding="utf-8")

print("Exportation en CSV terminée !")
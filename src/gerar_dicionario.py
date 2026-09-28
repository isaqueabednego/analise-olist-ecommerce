import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
linhas = []

for arquivo in sorted(RAW.glob("*.csv")):
    if "geolocation" in arquivo.name:
        continue
    df = pd.read_csv(arquivo)
    for coluna in df.columns:
        valores = df[coluna].dropna()
        linhas.append({
            "tabela": arquivo.stem,
            "coluna": coluna,
            "tipo": str(df[coluna].dtype),
            "nulos": int(df[coluna].isna().sum()),
            "exemplo": valores.iloc[0] if len(valores) else "",
            "descricao": "",
        })

Path("docs").mkdir(exist_ok=True)
pd.DataFrame(linhas).to_excel("docs/dicionario_dados.xlsx", index=False)
print(f"{len(linhas)} colunas documentadas")
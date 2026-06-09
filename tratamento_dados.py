import pandas as pd

# Carregar planilha
df = pd.read_excel("wagne_saeta-sem_altearacao.xlsx")

# Visualizar informações
print(df.info())

# Remover duplicados
df = df.drop_duplicates()

# Remover espaços
df["Estilo_Tatuagem"] = df["Estilo_Tatuagem"].str.strip()

# Converter data
df["Data_Atendimento"] = pd.to_datetime(
    df["Data_Atendimento"]
)

# Verificar nulos
print(df.isnull().sum())

# Salvar base tratada
df.to_excel(
    "wagne_saeta.xlsx",
    index=False
)
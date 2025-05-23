import pandas as pd


#fonction index colonne
def index_colonne(df, col):
    """
    Cette fonction verifie si une colonne existe, est non vide et la rend index du DataFrame 
    """
    try:
        if col in df.columns and not df[col].isnull().all():
            df.set_index(col, inplace=True)
            print(f"La colonne '{col}' a été définie comme index.")
        else:
            print(f"La colonne '{col}' n'existe pas ou est vide.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")




def verifier_et_transformer_datetime(df, col):
    """
    Vérifie si une colonne existe dans le DataFrame, détecte son type,
    et la convertit en datetime si elle ne l'est pas encore.
    Affiche un message selon l'état de la conversion.
    """
    try:
        if col not in df.columns:
            print(f"La colonne '{col}' n'existe pas dans le DataFrame.")
            return

        if pd.api.types.is_datetime64_any_dtype(df[col]):
            print(f"La colonne '{col}' est déjà au format datetime.")
        else:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            print(f"La colonne '{col}' a été convertie au format datetime.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


def verifier_valeur_binaire_col(df, col, valeur_1, valeur_2):
    """
    Vérifie si une colonne contient uniquement deux valeurs valeur1 et valeur2 
    """
    try:
        if col not in df.columns:
            print(f"La colonne '{col}' n'existe pas dans le DataFrame.")
            return

        unique_values = df[col].unique()
        if len(unique_values) == 2 and all(val in unique_values for val in [valeur_1, valeur_2]):
            print(f"La colonne '{col}' contient uniquement les valeurs {valeur_1} et {valeur_2}.")
        else:
            print(f"La colonne '{col}' ne contient pas uniquement les valeurs {valeur_1} et {valeur_2}.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


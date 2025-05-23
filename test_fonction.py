from fonctions import *
import pandas as pd
import pytest

@pytest.mark.parametrize("df, col, expected_index_name, expected_message", [
    (pd.DataFrame({'A': [1, 2, 3]}), 'A', 'A', "La colonne 'A' a été définie comme index."),
    (pd.DataFrame({'A': [None, None, None]}), 'A', None, "La colonne 'A' n'existe pas ou est vide."),
    (pd.DataFrame({'B': [4, 5, 6]}), 'A', None, "La colonne 'A' n'existe pas ou est vide."),
])
def test_index_colonne_message(df, col, expected_index_name, expected_message, capsys):
    df_copy = df.copy()
    index_colonne(df_copy, col)
    captured = capsys.readouterr()
    assert df_copy.index.name == expected_index_name
    assert expected_message in captured.out


import pandas as pd
import pytest
from fonctions import verifier_et_transformer_datetime

@pytest.mark.parametrize("df, col, expected_dtype, expected_msg", [
    # Colonne déjà datetime
    (pd.DataFrame({'date': pd.to_datetime(['2022-01-01', '2022-02-01'])}), 'date', 'datetime64[ns]', "déjà au format datetime"),
    # Colonne à convertir
    (pd.DataFrame({'date': ['2022-01-01', '2022-02-01']}), 'date', 'datetime64[ns]', "a été convertie au format datetime"),
    # Colonne absente
    (pd.DataFrame({'autre': ['2022-01-01']}), 'date', None, "n'existe pas"),
])
def test_verifier_et_transformer_datetime(df, col, expected_dtype, expected_msg, capsys):
    verifier_et_transformer_datetime(df, col)
    captured = capsys.readouterr()

    if expected_dtype:
        assert pd.api.types.is_datetime64_any_dtype(df[col])
    else:
        assert col not in df.columns or not pd.api.types.is_datetime64_any_dtype(df[col])

    assert expected_msg in captured.out



@pytest.mark.parametrize("df, col, valeur_1, valeur_2, expected_msg", [
    # Colonne avec deux valeurs binaires
    (pd.DataFrame({'col': [1, 0, 1]}), 'col', 1, 0, "contient uniquement les valeurs 1 et 0."),
    # Colonne avec plus de deux valeurs
    (pd.DataFrame({'col': [1, 0, 2]}), 'col', 1, 0, "ne contient pas uniquement les valeurs 1 et 0."),
    # Colonne absente
    (pd.DataFrame({'autre': [1, 0]}), 'col', 1, 0, "n'existe pas"),
])
def test_verifier_valeur_binaire_col(df, col, valeur_1, valeur_2, expected_msg, capsys):
    verifier_valeur_binaire_col(df, col, valeur_1, valeur_2)
    captured = capsys.readouterr()

    if col in df.columns:
        unique_values = df[col].unique()
        if len(unique_values) == 2 and all(val in unique_values for val in [valeur_1, valeur_2]):
            assert expected_msg in captured.out
        else:
            assert expected_msg in captured.out
    else:
        assert expected_msg in captured.out
import pytest
from juros.juros_composto import calcular_juros_compostos

@pytest.mark.parametrize("capital, juros, tempo, situacao_esperada"
                         [
                             (1000, 20, 1, (200, 1200)) #juros e montante
                         ]
                         )

def test_calcular_media_calculos_basicos_parametrizados(capital,juros, tempo, situacao_esperada):
    resultado = calcular_juros_compostos(capital, juros, tempo)
    assert resultado == situacao_esperada



# def test_verifica_negativo(capital, juros, tempo):

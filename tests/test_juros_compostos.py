import pytest
from juros.juros_composto import calcular_juros_compostos

@pytest.mark.parametrize("capital, juros, tempo, situacao_esperada"
                         [
                             (1000, 20, 1, (200, 1200)) #juros e montante
                         ]
                         )

def test_parametros(capital,juros, tempo, situacao_esperada):
    resultado = calcular_juros_compostos(capital, juros, tempo)
    assert resultado == situacao_esperada


# (-1000, -20, -1) exemplos para simular uma situação de erro
def test_verifica_negativo():
    # quando o capital for negativo
    with pytest.raises(ValueError, match="O capital investido não pode ser negativo."):
        calcular_juros_compostos(-1000, 20, 1)

    # quando a taxa de juros for negativa
    with pytest.raises(ValueError, match="A taxa de juros não pode ser negativa."):
        calcular_juros_compostos(1000, -20, 1)
    
    
    # quando o tempo for negativo
    with pytest.raises(ValueError, match="O tempo não pode ser negativo."):
        calcular_juros_compostos(1000, 20, -1)
    

def test_verifica_string():
    with pytest.raises(ValueError, match="O capital investido deve ser um número (int ou float).")
        calcular_juros_compostos("str", 20, 1)

    with pytest.raises(ValueError, match="A taxa de juros deve ser um número (int ou float).")
        calcular_juros_compostos(1000, "str", 1)

    with pytest.raises(ValueError, match="O tempo deve ser um número (int ou float).")
        calcular_juros_compostos(1000, 20, "str")

# verifica parametros vazios
def test_verifica_valor_vazio():
    with pytest.raises(ValueError, match="O capital investido deve ser um número (int ou float).")
        calcular_juros_compostos([], 20, 1)

    with pytest.raises(ValueError, match="O capital investido deve ser um número (int ou float).")
        calcular_juros_compostos(1000, [], 1)

    with pytest.raises(ValueError, match="O capital investido deve ser um número (int ou float).")
        calcular_juros_compostos(1000, 20, [])
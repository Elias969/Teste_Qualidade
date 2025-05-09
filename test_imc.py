from imc import calcular_imc
import pytest

def test_imc_valido():
    assert calcular_imc(70, 1.75) == 22.86
    
def test_imc_com_zero():
    with pytest.raises(ValueError):
         calcular_imc(70, 0) 
            
def test_imc_limite():
    assert calcular_imc(100, 2.0) == 25
    
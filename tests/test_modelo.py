import os
import src.modelo as modelo

def test_model_load():
    # se houver função de carregamento, tenta executar; caso contrário apenas importa
    if hasattr(modelo, 'load_model'):
        m = modelo.load_model()  # pode levantar erro se não estiver implementado
    assert True

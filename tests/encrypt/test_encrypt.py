import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    "Uma exceção de tipo deve ser lançada ao inserir parametros inválidos"
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 1)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("text", "abc")
    "retorna a string message invertida caso key > message.len"
    assert encrypt_message("palavra", 10) == "arvalap"
    "caso key possua valor impar"
    assert encrypt_message("palavra", 3) == "lap_arva"
    "caso key possua valor par"
    assert encrypt_message("palavra", 4) == "arv_alap"

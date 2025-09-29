# test_parser.py
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..')) #para poder importar la ruta de lexer

from lexer import lex_to_list  # Asegúrate de que el archivo se llama lexer.py

def test_variable_assignment():
    code = "var x = 5;"
    tokens = lex_to_list(code)

    # Debug: ver qué tokens se generan
    print("Tokens generados:")
    for i, token in enumerate(tokens):
        print(f"{i}: {token.type} = '{token.value}'")

    # El primer token debería ser la palabra reservada "var"
    assert tokens[0].type == "KEYWORD"
    assert tokens[0].value == "var"

    # Luego un identificador
    assert tokens[1].type == "ID"
    assert tokens[1].value == "x"

    # Luego el operador de asignación
    assert tokens[2].type == "ASSIGN"
    assert tokens[2].value == "="  # CORREGIDO: era "-"

    # Y un número entero
    assert tokens[3].type == "NUMBER"  # CORREGIDO: era "HUMBER"
    assert tokens[3].value == "5"      # CORREGIDO: era "S"

def test_arithmetic_expression():
    code = "x = x + 1;"
    tokens = lex_to_list(code)

    # Debug
    print("Tokens aritméticos:")
    for i, token in enumerate(tokens):
        print(f"{i}: {token.type} = '{token.value}'")

    assert any(t.type == "ARITH_OP" and t.value == "+" for t in tokens)
    assert any(t.type == "NUMBER" and t.value == "1" for t in tokens)

def test_logical_expression():
    code = "if (x && y) { return x || y; }"
    tokens = lex_to_list(code)

    # Debug
    print("Tokens lógicos:")
    for i, token in enumerate(tokens):
        print(f"{i}: {token.type} = '{token.value}'")

    # Verifica que detecta operadores lógicos
    assert any(t.type == "LOGIC_OP" and t.value == "&&" for t in tokens)
    assert any(t.type == "LOGIC_OP" and t.value == "||" for t in tokens)

# Para ejecutar y debuggear
if __name__ == "__main__":
    test_variable_assignment()
    test_arithmetic_expression()
    test_logical_expression()
    print("¡Todos los tests pasaron!")

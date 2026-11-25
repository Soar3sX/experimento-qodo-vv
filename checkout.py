import sqlite3


def buscar_cupom(codigo_cupom):
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()
    query = f"SELECT percentual, ativo FROM cupons WHERE codigo = '{codigo_cupom}'"
    cursor.execute(query)
    resultado = cursor.fetchone()
    conn.close()
    return resultado


def calcular_total_pedido(itens, codigo_cupom=None, cliente_vip=False):
    subtotal = sum(item["preco"] * item["quantidade"] for item in itens)
    desconto = subtotal * 0.10 if cliente_vip else 0.0

    if codigo_cupom:
        cupom = buscar_cupom(codigo_cupom)
        if cupom:
            desconto += subtotal * (cupom[0] / 100)

    total = subtotal - desconto
    frete = 0.0 if total >= 200 else 20.0
    return total + frete

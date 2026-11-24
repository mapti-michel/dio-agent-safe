import sqlite3


def fazer_login(usuario: str, senha: str) -> str:
    """Valida as credenciais usando parâmetros separados do SQL."""
    query = (
        "SELECT 1 FROM usuarios "
        "WHERE username = ? AND password = ? "
        "LIMIT 1"
    )

    try:
        conexao = sqlite3.connect("banco_de_dados.db")
        try:
            resultado = conexao.execute(query, (usuario, senha)).fetchone()
        finally:
            conexao.close()
    except sqlite3.Error:
        # Falha fechada: problemas no banco nunca concedem acesso.
        return "Não foi possível validar o acesso."

    if resultado:
        return "Acesso permitido!"
    return "Acesso negado."
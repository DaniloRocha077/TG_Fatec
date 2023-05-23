"""Module providingFunction printing python version."""
import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Conexão com o servidor bem-sucedida")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#Verificar se o banco de dados já existe
def verificar_banco():
    """
    verificar banco.
    """
    db = mysql.connector.connect(
    host="db4free.net",
    user="fatecmm",
    password="DanRocha!@#qaz"
)
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()

    database_existe = False
    for database in databases:
        if database[0] == "envios_tg":
            database_existe = False
            return database_existe
# Criar o banco de dados, se ele não existir
    if not database_existe:
        cursor.execute("CREATE DATABASE envios_tg")
        return True
    else:
        st.write("Banco de dados já existe!")

def banco_connection(host_name, user_name, user_password, banco):
    """
    Conectar ao banco.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=banco
        )
        print("Conectado ao Banco")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#Verificar se a tabela já existe
def verificar_tabela():
    """
    verificar tabela.
    """
    db1 = mysql.connector.connect(
    host="db4free.net",
    user="fatecmm",
    password="DanRocha!@#qaz",
    database="envios_tg"
)
    cursor = db1.cursor()
    cursor.execute("SHOW TABLES")
    databases = cursor.fetchall()

    tabela_existe = False
    for database in databases:
        if database[0] == "tbl_trabalhos":
            tabela_existe = False
            return tabela_existe
# Criar a tabela, se ele não existir
    if not tabela_existe:
        criar_tabela_sql = """
        CREATE TABLE IF NOT EXISTS tbl_trabalhos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            autores VARCHAR(255),
            orientador VARCHAR(255),
            tema VARCHAR(255),
            cidade VARCHAR(255),
            ano VARCHAR(4),
            resumo TEXT,
            keywords VARCHAR(255),
            introducao TEXT,
            conclusao TEXT
        )"""
        cursor.execute(criar_tabela_sql)
    else:
        print("A tabela já existe!")

def remover_caracteres_invalidos(texto):
    return texto.encode('utf-8', 'ignore').decode('utf-8')

#inserir registro no banco
def enviar_banco(autores, orientador, tema, cidade, ano, resumo, keywords, introducao, conclusao):
    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(
            host="db4free.net",
            user="fatecmm",
            password="DanRocha!@#qaz",
            database="envios_tg"
        )

        # Criar um cursor para executar as queries SQL
        cursor = conn.cursor()

        # Inserir os dados na tabela do banco de dados
        sql = "INSERT INTO tbl_trabalhos (autores, orientador, tema, cidade, ano, resumo, keywords, introducao, conclusao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (autores, ", ".join(orientador), tema, cidade, ano, resumo, ", ".join(keywords), introducao, conclusao)
        cursor.execute(sql, values)

        # Confirmar a inserção dos dados no banco de dados
        conn.commit()

        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conn.close()

        return True
    except Error as er:
        print("Ocorreu um erro ao enviar os dados para o banco de dados:", er)
    return False

def buscar_trabalhos(palavra_chave):
    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(
            host="db4free.net",
            user="fatecmm",
            password="DanRocha!@#qaz",
            database="envios_tg"
        )

        # Criar um cursor para executar as queries SQL
        cursor = conn.cursor()

        # Buscar os dados na tabela do banco de dados
        sql = "SELECT * FROM tbl_trabalhos WHERE tema LIKE %s OR keywords LIKE %s"
        values = ('%' + palavra_chave + '%', '%' + palavra_chave + '%')
        cursor.execute(sql, values)

        # Criar uma lista com os resultados da busca
        resultados = []
        for resultado in cursor.fetchall():
            resultados.append(resultado)

        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conn.close()

        return resultados
    except Error as er:
        print("Ocorreu um erro ao buscar os dados no banco de dados:", er)

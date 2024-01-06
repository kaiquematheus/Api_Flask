from flask import Flask, jsonify, request
import sqlite3
import uuid


# Configuração do banco de dados
DB_NAME = 'banco.db'

# Cria a tabela contendo 
# id, ientifer,NotificationSubscription e callback_uri
def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            hotel_id VARCHAR(36) PRIMARY KEY,
            nome VARCHAR(36) NOT NULL,
            estrelas VARCHAR(2) NOT NULL,
            diaria VARCHAR(8) NOT NULL,
            ciade VARCHAR(80) NOT NULL
        )
    ''')
    #c.execute('CREATE TABLE IF NOT EXISTS applications (id VARCHAR(36), identifier VARCHAR(36), NotificationSubscription VARCHAR(50), callback_uri VARCHAR(200))')
    conn.commit()
    conn.close()

# insert no bd
def insert_bd(hotel_id, nome, estrelas, diaria, cidade):
    # Verificar se a aplicação já está cadastrada
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM applications WHERE hotel_id = ?', (hotel_id,))
    result = c.fetchone()
    if result:
        conn.close()
        return result[0]  # Retorna o ID existente se a aplicação já estiver cadastrada

    # Gerar um novo ID
    id = str(uuid.uuid4())

    # Inserir a aplicação no banco de dados
    c.execute('INSERT INTO applications VALUES (?, ?, ?, ?, ?)', (hotel_id,  nome, estrelas, diaria, cidade))
    conn.commit()
    conn.close()

    return id
    

def update_bd(hotel_id, nome, estrelas, diaria, cidade):
    # Verificar se a aplicação já está cadastrada
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Inserir a aplicação no banco de dados

    c.execute('UPDATE applications SET nome = ?, estrelas = ?, diaria = ?, cidade = ? WHERE hotel_id = ?', (nome, estrelas, diaria, cidade, hotel_id))

    conn.commit()
    conn.close()

    return 'ok'


def get_bd():

    # Obter a lista de IDs e identificadores cadastrados
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM applications')
    rows = c.fetchall()
    conn.close()
    return [{'hotel_id': row[0], 'nome': row[1], 'estrelas': row[2], 'diaria': row[3], 'cidade': row[4]} for row in rows]

def get_item(hotel_id):

    # Obter a lista de IDs e identificadores cadastrados
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM applications WHERE hotel_id = ?',(hotel_id,))
    rows = c.fetchall()
    conn.close()
    return [{'hotel_id': row[0], 'nome': row[1], 'estrelas': row[2], 'diaria': row[3], 'cidade': row[4]} for row in rows]


# deleta algum cadastro do bd
def delete_bd(hotel_id):
    # Deletar a aplicação do banco de dados
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM applications WHERE hotel_id = ?', (hotel_id,))
    conn.commit()
    conn.close()




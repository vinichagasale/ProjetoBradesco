import sqlite3 as sql

class TransactionObjetct():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObjetct.conn = sql.connect(TransactionObjetct.database)
        TransactionObjetct.cur = TransactionObjetct.conn.cursor()
        TransactionObjetct.connected = True

    def disconnect(self):
        TransactionObjetct.conn.close()
        TransactionObjetct.connected = False

    def execute(self, sql, parms = None):
        if TransactionObjetct.connected:
            if parms == None:
                TransactionObjetct.cur.execute(sql)
            else:
                TransactionObjetct.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObjetct.cur.fetchall()

    def persist(self):
        if TransactionObjetct.connected:
            TransactionObjetct.conn.commit()
            return True
        else:
            return False

def initDB():
    trans = TransactionObjetct()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    trans.persist()
    trans.disconnect()

def insert(nome, sobrenome, email, cpf):
    trans = TransactionObjetct()
    trans.connect()
    trans.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
    trans.persist()
    trans.disconnect()

def view():
    trans = TransactionObjetct()
    trans.connect()
    trans.execute("SELECT * FROM clientes")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(nome="", sobrenome="", email="", cpf=""):
    trans = TransactionObjetct()
    trans.connect()
    trans.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email, cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def delete(id):
    trans = TransactionObjetct()
    trans.connect()
    trans.execute("DELETE FROM clientes WHERE id=?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, nome, sobrenome, email, cpf):
    trans = TransactionObjetct()
    trans.connect()
    trans.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
    trans.persist()
    trans.disconnect()

initDB()



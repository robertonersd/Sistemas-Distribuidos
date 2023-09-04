from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import datetime

app = FastAPI()

# Definir o modelo Pydantic para a criação de temperatura
class TemperaturaCreate(BaseModel):
    temperatura: float

# Definir o modelo Pydantic para a atualização de temperatura
class TemperaturaUpdate(BaseModel):
    temperatura: float

# Conectar ao banco de dados (criará um novo arquivo se não existir)
conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()

# Rota para criar uma nova entrada de temperatura
@app.post("/temperaturas/")
def create_temperatura(item: TemperaturaCreate):
    timestamp = datetime.now()
    insert_data_query = '''
        INSERT INTO temperatura (temperatura, timestamp)
        VALUES (?, ?);
    '''
    cursor.execute(insert_data_query, (item.temperatura, timestamp))
    conn.commit()
    return {"message": "Temperatura criada com sucesso"}

# Rota para atualizar uma entrada de temperatura pelo ID
@app.put("/temperaturas/{temperatura_id}")
def update_temperatura(temperatura_id: int, item: TemperaturaUpdate):
    select_data_query = '''
        SELECT COUNT(*) FROM temperatura WHERE id = ?;
    '''
    cursor.execute(select_data_query, (temperatura_id,))
    data_count = cursor.fetchone()[0]
    if data_count == 0:
        raise HTTPException(status_code=404, detail="Temperatura não encontrada")
    
    update_data_query = '''
        UPDATE temperatura SET temperatura = ? WHERE id = ?;
    '''
    cursor.execute(update_data_query, (item.temperatura, temperatura_id))
    conn.commit()
    return {"message": "Temperatura atualizada com sucesso"}

# Rota para deletar uma entrada de temperatura pelo ID
@app.delete("/temperaturas/{temperatura_id}")
def delete_temperatura(temperatura_id: int):
    select_data_query = '''
        SELECT COUNT(*) FROM temperatura WHERE id = ?;
    '''
    cursor.execute(select_data_query, (temperatura_id,))
    data_count = cursor.fetchone()[0]
    if data_count == 0:
        raise HTTPException(status_code=404, detail="Temperatura não encontrada")
    
    delete_data_query = '''
        DELETE FROM temperatura WHERE id = ?;
    '''
    cursor.execute(delete_data_query, (temperatura_id,))
    conn.commit()
    return {"message": "Temperatura deletada com sucesso"}

# Rota para obter todas as entradas de temperatura
@app.get("/temperaturas/")
def read_temperaturas():
    select_data_query = '''
        SELECT id, temperatura, timestamp FROM temperatura;
    '''
    cursor.execute(select_data_query)
    data = cursor.fetchall()
    return data

# Fechar a conexão com o banco de dados ao encerrar o aplicativo
@app.on_event("shutdown")
def shutdown_event():
    conn.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)






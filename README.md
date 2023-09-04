Caros alunos
Este será o repositório de códigos official da disciplina
Publique os seus códigos aqui e caprichem no READMEs

Sugiro que criem um ambiente virtual no Python. Para tanto sigam este tutorial:

https://docs.python.org/pt-br/3/tutorial/venv.html

Após criado o ambiente virtual você podem instalar os pacotes necessários de seus scripts com pip install

O script createdb.by cria um banc de dados SQLite com a seguinte estrutura:

create_table_query = '''
    CREATE TABLE IF NOT EXISTS temperatura (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura REAL,
        timestamp DATETIME
    );

    O id será usado como chave de busca para as rota PUT e DELETE


o script main.py é o wrapper que instancia a API codificada no script myapp.py. Para executá-la você deve instalar via pip o módulo fastapi
O script myapp.py é a API propriamente dita, com as rotas para executar o CRUDE no banco de dados.
Você precisa instalar via PIP os módulos HTTPException, Pydantic, uvicorn e datetime antes de executá-lo.

Para ativar a API deve executar o uvicorn com o seguinte comando: uvicorn main:app --host 0.0.0.0 --port 8000 (a api roda na porta 8000)
A aparencia da execução será essa:
(Sistemas_Distribuidos) beto@Inspiron-Beto:~/Sistemas_Distribuidos$ /home/beto/Sistemas_Distribuidos/bin/python /home/beto/Sistemas_Distribuidos/myapp.py
INFO:     Started server process [9405]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

O terminal ficará preso na API até você encerrar a API  com CTRL+C.

Exemplos de chamadas das rotas da API. Use o POSTMAN: https://www.postman.com/

Criar uma nova entrada de temperatura:

URL: http://localhost:8000/temperaturas/

Método: POST

Corpo da Requisição:

json no  Body da requisição
{
    "temperatura": 25.5
}

Obter todas as entradas de temperatura:

URL: http://localhost:8000/temperaturas/

Método: GET
Atualizar uma entrada de temperatura pelo ID:

URL: http://localhost:8000/temperaturas/{temperatura_id}

Método: PUT

Corpo da Requisição:

json no  Body da requisição

{
    "temperatura": 28.2
}

Deletar uma entrada de temperatura pelo ID:

URL: http://localhost:8000/temperaturas/{temperatura_id}

Método: DELETE


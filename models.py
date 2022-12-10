from peewee import CharField, IntegerField, Model, SqliteDatabase
from settings import DATABASE_FILE


# Cria instancia banco de dados
db = SqliteDatabase(DATABASE_FILE)

#modelo Base tabelas
class BaseModel(Model):
    class Meta:
        database = db


class Cep(BaseModel):
    cep = IntegerField(unique=True)
    logradouro = CharField()
    complemento = CharField(null=True)
    bairro = CharField()
    localidade = CharField()
    uf = CharField(max_length=2)
    ibge = IntegerField()
    gia = IntegerField()
    ddd = IntegerField()
    siafi = IntegerField()
    
    
class CepRange(BaseModel):
    min_cep = IntegerField()
    max_cep = IntegerField()
    last_cep = IntegerField(default=0)


#cria tabelas no banco de dados       
def create_tables():
    with db:
        db.create_tables([Cep, CepRange])
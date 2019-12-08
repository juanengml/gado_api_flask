import dataset

path_db = 'sqlite:///apigado.db'

class Banco:
    def listGados(self):
        with dataset.connect(path_db) as db:
                jogos = db["gado"].all()
                if db['gado'].count() > 0:
                    listaJogos = [dict(_ID_=data['_ID_'],fazenda=data['fazenda'], peso=data['peso']) for data in jogos]
                    return listaJogos
                else:
                    return False

    def save(self,data):
        with dataset.connect(path_db) as db:
            return db['gado'].insert(dict(_ID_=data['_ID_'],fazenda=data['fazenda'], peso=data['peso']))


    def getGado(self, id):
        with dataset.connect(path_db) as db:
            jogo = db['gado'].find_one(id=_ID_)
            if jogo:
                return jogo
            else:
                return False
    def update(self, id, data):
        with dataset.connect(path_db) as db:
            return db['gado'].update(dict(_ID_=id,fazenda=data['fazenda'], peso=data['peso']),['id'])
                                                  
    def delete(self, id):
        with dataset.connect(path_db) as db:
            return db['gado'].delete(id=id)


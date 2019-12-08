import dataset

db = dataset.connect('sqlite:///apigado.db')

table = db['gado']

table.insert(dict(_ID_=1,fazenda='John DRMe', peso='460'))

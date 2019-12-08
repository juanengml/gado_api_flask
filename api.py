from flask import Blueprint, jsonify, make_response, request
from banco import Banco

bp_api = Blueprint('api',__name__,url_prefix="/gado/api/v1/lista")
banco = Banco()


@bp_api.route("/",methods=['GET'])
@bp_api.route("/<int:id>",methods=['GET'])
def get_(id = None):
    lista = banco.listGados()
    if lista != False:
      if id != None:
         lista = banco.getGado(id)
         return jsonify({'lista':lista})
      else:
         return jsonify({'lista':lista})
    else:
      return make_response(jsonify({"error":"Not exite gado ome"}),404)     


@bp_api.route("/add/",methods=['POST'])
def add_():
   if request.json:
    banco.save(request.json[0])     
   return make_response(jsonify({"msg":"Dados Inseridos com Sucesso"}),200)     

@bp_api.route("/alter/<int:id>",methods=['PUT'])
def put_(id = None):
    if request.json and id != None:
        banco.update(id, request.json[0])     
    return make_response(jsonify({"msg":"Dados ALTERADOS com Sucesso"}),200)     




@bp_api.route("/del/<int:id>",methods=['DELETE'])
def del_(id  = None) :
    if request.json  and id != None:
      banco.delete(id)     
    return make_response(jsonify({"msg":"Dado {} DELETADO  com Sucesso".format(id)}),200)     


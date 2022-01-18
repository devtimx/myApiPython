from crypt import methods

from flask import Flask,jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app import create_app

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:toor@localhost:3306/bdpythonapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db  = SQLAlchemy(app)
ma = Marshmallow(app)

#Creacion de tabla categoria
class Categoria(db.Model):
    cat_id = db.Column(db.Integer,primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))

    def __init__(self,cat_nom,cat_desp):
        self.cat_nom = cat_nom
        self.cat_desp = cat_desp

db.create_all()

#Esquema
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('cat_id','cat_nom','cat_desp')


#una sola respuesta
categoria_schema = CategoriaSchema()
#Cuando sean muchas respuestas
categorias_schema = CategoriaSchema(many=True)


#GET
@app.route('/categoria',methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categorias_schema.dump(all_categorias)
    return jsonify(result)


#GET x ID 
@app.route('/categoria/<id>',methods=['GET'])
def get_Categoria_id(id):
    categoria = Categoria.query.get(id)
    result = categoria_schema.dump(categoria)
    return jsonify(result)


#POST
@app.route('/categoria',methods=['POST'])
def insert_categoria():
    data = request.get_json(force=True)
    cat_nom = data['cat_nom']
    cat_desp = data['cat_desp']

    new_register = Categoria(cat_nom,cat_desp)
    db.session.add(new_register)
    db.session.commit()
    return categoria_schema.jsonify(new_register)


#PUT
@app.route('/categoria/<id>',methods=['PUT'])
def update_categoria(id):
    updateCategory = Categoria.query.get(id)
    data = request.get_json(force=True)
    cat_nom = data['cat_nom']
    cat_desp = data['cat_desp']

    updateCategory.cat_nom = cat_nom
    updateCategory.cat_desp = cat_desp

    db.session.commit()

    return categoria_schema.jsonify(updateCategory)


#DELETE
@app.route('/categoria/<id>',methods=['DELETE'])
def delete_categoria(id):
    deleteCategory = Categoria.query.get(id)
    db.session.delete(deleteCategory)
    db.session.commit()
    return categoria_schema.jsonify(deleteCategory)


#Mensaje de bienbenida
@app.route('/',methods=['GET'])
def index():
    return jsonify({'Message':'Welcome to API REST Python'})

if __name__ == "__main__":
    app.run(debug=True)
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "olá, mundo!"}

@app.get("/sobre")
def sobre ():
    return{"projeto": "Sistema de Padaria", "autor": "José Augusto Medeiros de Lima"}


@app.get("/produtos")
def lista_produtos ():
 return [
    {"id": 1,
           "nome": "pão francês",
           "preco": 0.80},

    {
       "id": 2,
       "nome": "sonho",
       "preco": 6.50
    }
 ]
@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
   produtos = [
      {"id": 1, "nome": "pão francês", "preco": 0.80},
      {"id": 2, "nome": "sonho", "preco": 6.50}

   ]
   for produto in produtos:
      if produto["id"] == produto_id:
         return produto
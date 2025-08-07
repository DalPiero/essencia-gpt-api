from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class BannerRequest(BaseModel):
    frase: str
    contexto: str

class FilmeRequest(BaseModel):
    tema: str
    duracao: int
    roteiro: str

@app.get("/resposta")
def get_resposta(input: str = Query(..., description="Prompt codificado via encodeURIComponent")):
    return {
        "resposta": f"Recebido: {input}",
        "imagem": "https://via.placeholder.com/800x600?text=Imagem+Gerada"
    }

@app.post("/gerar-banner")
def post_gerar_banner(data: BannerRequest):
    return {
        "banner_url": "https://via.placeholder.com/1200x800?text=Banner+Essencia",
        "descricao_rodape": f"Contexto: {data.contexto} | Frase: {data.frase}"
    }

@app.post("/filme")
def post_filme(data: FilmeRequest):
    return {
        "video_url": "https://example.com/videos/filme-demo.mp4"
    }

@app.get("/frase-diaria")
def get_frase_diaria():
    return {
        "frase": "Toda beleza começa com um gesto de cuidado. – Essência que Brilha"
    }
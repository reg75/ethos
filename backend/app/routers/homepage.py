import os
from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.config import FRONTEND_DIR

router = APIRouter()

# EN: Serve the homepage HTML file (index.html) from the frontend folder
# BR: Servir o arquivo HTML da SPA (index.html) da pasta frontend
@router.get("/", response_class=FileResponse)
async def read_index():
    # EN: Returning the index.html file to the user
    # BR: Retornando o arquivo index.html para o usuário
    index_file = FRONTEND_DIR / "index.html"
    return FileResponse(index_file)
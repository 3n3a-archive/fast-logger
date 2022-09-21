from fastapi import FastAPI, File, UploadFile
from pathlib import Path
import aiofiles

app = FastAPI()
upload_dir = Path("./uploads")

@app.get("/")
async def root():
    return {"message": "FastLogger V1.0 - Log Files can be uploaded to \"POST /log\"."}

@app.post("/log")
async def create_log(file: UploadFile):
    async with aiofiles.open(upload_dir / file.filename, 'wb') as out_file:
        while content := await file.read(1024):
            await out_file.write(content)

    return {"filename": file.filename}

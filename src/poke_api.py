from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
import requests
import asyncpg
import pandas as pd
from hdfs import InsecureClient
import io

app = FastAPI()
DATABASE_URL = "postgresql://pokemon:Dev1!@postgres/pokemon_db"
HDFS_URL = "http://namenode:9870"

class EffectRequest(BaseModel):
    pokemon_ability_id: str

async def get_pool():
    return await asyncpg.create_pool(DATABASE_URL)

@app.post("/pokemon_effect/")
async def pokemon_effect(effect_request: EffectRequest):
    pokemon_ability_id = effect_request.pokemon_ability_id

    try:
        url = "https://pokeapi.co/api/v2/ability/" + pokemon_ability_id
        call = requests.get(url)
        response = call.json()
        
        pool = await get_pool()
        returned_entries = []
        async with pool.acquire() as conn:
            for effect_entries in response['effect_entries']:
                await conn.execute("""
                    INSERT INTO pokemon_effect (pokemon_ability_id, effect, language, short_effect)
                    VALUES ($1, $2, $3, $4);
                """, int(pokemon_ability_id), str(effect_entries['effect']), 
                str(effect_entries['language']), str(effect_entries['short_effect']))
                returned_entries.append(effect_entries)

        return {
            "pokemon_ability_id": pokemon_ability_id,
            "returned_entries": returned_entries
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # baca file
        content = await file.read()
        df = pd.read_csv(io.StringIO(content.decode('utf-8')))

        # Save  dataframe ke HDFS
        client = InsecureClient(HDFS_URL, user='root')
        
        # memastikan folder sudah dibuat
        if not client.status('/data', strict=False):
            client.makedirs('/data')

        # Tulis file ke HDFS
        with client.write('/data/' + file.filename, encoding='utf-8') as writer:
            df.to_csv(writer, index=False)

        with client.write('/data/' + file.filename, encoding='utf-8') as writer:
            df.to_csv(writer, index=False)

        return {"filename": file.filename, "message": "File uploaded successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


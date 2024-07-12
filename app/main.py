import os
from typing import Optional

from data_storage import save_to_excel, save_to_json
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from scraper import scrape_website_table

app = FastAPI()


class ScrapingTask(BaseModel):
    url: str
    table_selector: Optional[str] = None


@app.post("/scrape")
async def scrape(task: ScrapingTask):
    try:
        data = scrape_website_table(task.url, task.table_selector)
        json_filename = save_to_json(data)
        excel_filename = save_to_excel(data)
        return {
            "message": "Scraping completado",
            "json_file": json_filename,
            "excel_file": excel_filename,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join("/app/data", filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, filename=filename)
    raise HTTPException(status_code=404, detail="Archivo no encontrado")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8880, reload=True)

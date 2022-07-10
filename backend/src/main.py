from fastapi import FastAPI, Form, UploadFile, File
from enum import Enum
import uvicorn
from extractor import extract
import uuid
import os

app = FastAPI()

@app.post('/extract_from_doc')
def extract_from_doc(
    file_format: str = Form(...),
    file: UploadFile = File(...)
    ):
    file_path = "/Users/shikhabharati/Desktop/Python/medicalProject/backend/src/upload/"+str(uuid.uuid4())+'.pdf'
    content = file.file.read()
    with open(file_path, 'wb') as f:
    # with open("../upload/test.pdf", 'wb') as f:
        f.write(content)

    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data = { 
            'error': str(e)
        }

    if os.path.exists(file_path):
        os.remove(file_path)

    return data


if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port= 8080)

    
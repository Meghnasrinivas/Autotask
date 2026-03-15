from fastapi import UploadFile
from typing import List, Dict


def parse_uploaded_files(files: List[UploadFile]) -> List[Dict]:
    parsed = []
    for file in files:
        parsed.append({
            "filename": file.filename,
            "content_type": file.content_type,
            "size": None,
            "content": None,
        })
    return parsed

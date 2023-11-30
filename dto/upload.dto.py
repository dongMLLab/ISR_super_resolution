from pydantic import BaseModel


class UploadRequestDto(BaseModel):
    fileName: str
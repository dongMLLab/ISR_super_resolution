from pydantic import BaseModel


class UploadRequestDto(BaseModel):
    fileName: str
    versionId: str
    weights: str
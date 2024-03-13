from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class BaseDomain(BaseModel):
    id: UUID = Field(default=uuid4())
    created_at: str = Field(datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")[:-3])

from pydantic import BaseModel
from typing import List

class Diagram(BaseModel):
    shares: List[int]
    titles: List[str]
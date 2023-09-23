from pydantic import BaseModel
from typing import List

data = {
  "name": "Michael Kennedy",
  "age": "28",
  "location": {
    "city": "Portland",
    "state": "Oregon",
   
  },
  "bike": "KTM Duke 690",
  "rides": [7, 103, 22, "70", 1000]
}

class Location(BaseModel):
    city: str
    state: str
    

class User(BaseModel):
    name: str
    age: int
    location: Location = None
    bike: str
    rides: List[int] = []
  

user = User(**data)

print(f"found a user:{user}")
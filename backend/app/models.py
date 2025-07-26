from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    @classmethod
    def _get_pydantic_json_schema(cls,schema,handler):
        schema.update(type="string")
        return schema

class Message(BaseModel):
    sender:str
    text:str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
class Conversation(BaseModel):
    id:Optional[PyObjectId] = Field(alias="_id", default=None)
    user_id:str
    message:List[Message]=[]
    created_at:datetime= Field(default_factory=datetime.utcnow)

class Config:
    populate_by_name=True
    arbitary_types_allowed=True
    json_encoders={object:str}
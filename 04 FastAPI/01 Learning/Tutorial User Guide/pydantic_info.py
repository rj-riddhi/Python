# # Pydantic is the most widely used data validation library for Python.

# # Why use Pydantic?

# # Powered by type hints — with Pydantic, schema validation and serialization are controlled by type annotations; less to learn, less code to write, and seamless integration with your IDE and static analysis tools. Learn more…
# Speed — Pydantic's core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python. Learn more…
# JSON Schema — Pydantic models can emit JSON Schema, allowing for easy integration with other tools. Learn more…
# Strict and Lax mode — Pydantic can run in either strict mode (where data is not converted) or lax mode where Pydantic tries to coerce data to the correct type where appropriate. Learn more…
# Dataclasses, TypedDicts and more — Pydantic supports validation of many standard library types including dataclass and TypedDict. Learn more…
# Customisation — Pydantic allows custom validators and serializers to alter how data is processed in many powerful ways. Learn more…
# Ecosystem — around 8,000 packages on PyPI use Pydantic, including massively popular libraries like FastAPI, huggingface, Django Ninja, SQLModel, & LangChain. Learn more…
# Battle tested — Pydantic is downloaded over 360M times/month and is used by all FAANG companies and 20 of the 25 largest companies on NASDAQ. If you're trying to do something with Pydantic, someone else has probably already done it. 

from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime
    tastes: dict[str, int]  


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        'cheese': 7,  
        'cabbage': '1',  
    },
}

user = User(**external_data)  

print(user.id)  

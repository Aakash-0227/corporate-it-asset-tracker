
from datetime import date, datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field



class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)



class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"



class AssetCreate(BaseModel):
    asset_name: str = Field(min_length=2, max_length=100)
    asset_tag: str = Field(min_length=2, max_length=50)
    category: str = Field(min_length=2, max_length=50)
    serial_number: str | None = Field(default=None, max_length=100)
    purchase_date: date | None = None
    price: Decimal | None = Field(default=None, ge=0, max_digits=10, decimal_places=2)
    status: Literal["available", "assigned", "maintenance", "retired"] = "available"
    assigned_to: str | None = Field(default=None, max_length=100)


class AssetUpdate(BaseModel):
    asset_name: str = Field(min_length=2, max_length=100)
    asset_tag: str = Field(min_length=2, max_length=50)
    category: str = Field(min_length=2, max_length=50)
    serial_number: str | None = Field(default=None, max_length=100)
    purchase_date: date | None = None
    price: Decimal | None = Field(default=None, ge=0, max_digits=10, decimal_places=2)
    status: Literal["available", "assigned", "maintenance", "retired"]
    assigned_to: str | None = Field(default=None, max_length=100)



class AssetResponse(BaseModel):
    id: int
    asset_name: str
    asset_tag: str
    category: str
    serial_number: str | None = None
    purchase_date: date | None = None
    price: Decimal | None = None
    status: str
    assigned_to: str | None = None
    created_at: datetime | None = None
    user_id: int

    model_config = ConfigDict(from_attributes=True)

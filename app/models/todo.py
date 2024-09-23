from typing import Any, Optional
from venv import create

from flask import json, jsonify


class Todo:
    def __init__(
        self,
        *,
        id: str = "",
        name: str = "",
        description: str = "",
        price: int = 0,
        quantity: int = 0,
        created_at: int = 0,
        updated_at: Optional[int] = None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        result["id"] = self.id
        result["name"] = self.name
        result["description"] = self.description
        result["price"] = self.price
        result["quantity"] = self.quantity
        result["created_at"] = self.created_at
        result["updated_at"] = self.updated_at

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            description=data.get("description", ""),
            price=data.get("price", 0),
            quantity=data.get("quantity", 0),
            created_at=data.get("created_at", 0),
            updated_at=data.get("updated_at", None),
        )

    @classmethod
    def to_json(cls) -> str:
        jsonify(cls.to_dict())

    @classmethod
    def from_json(cls, source: str):
        cls.from_dict(json.loads(source))

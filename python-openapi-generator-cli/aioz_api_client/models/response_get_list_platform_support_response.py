from __future__ import annotations
import pprint
import json
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Set
from typing_extensions import Self

class ResponseGetListPlatformSupportResponse(BaseModel):
    """
    ResponseGetListPlatformSupportResponse
    """
    data: Optional[List[StrictStr]] = None
    message: Optional[StrictStr] = None
    status: Optional[StrictStr] = 'success'
    __properties: ClassVar[List[str]] = ["data", "message", "status"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ResponseGetListPlatformSupportResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias."""
        excluded_fields: Set[str] = set([])
        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance from a dict, unwrap `data` if needed"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)
        data_field = obj.get("data")
        if isinstance(data_field, dict) and "data" in data_field:
            data_field = data_field["data"]

        _obj = cls.model_validate({
            "data": data_field,
            "message": obj.get("message"),
            "status": obj.get("status") if obj.get("status") is not None else 'success'
        })
        return _obj

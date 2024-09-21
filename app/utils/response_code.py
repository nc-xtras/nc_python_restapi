from typing import Any
from flask import jsonify


class ResponseCode:
    def __success_code(code: int, status: str, data=None):
        response: dict[str, Any]
        if data == None:
            response = {"code": code, "status": status}
        else:
            response = {"code": code, "status": status, "data": data}
        return jsonify(response), code

    def __error_code(code: int, status: str, message=None):
        response = {"code": code, "status": status, "message": message}
        return jsonify(response), code

    @classmethod
    def success_ok(cls, data=None):
        return cls.__success_code(code=200, status="OK", data=data)

    @classmethod
    def success_created(cls, data):
        return cls.__success_code(code=201, status="Created", data=data)

    @classmethod
    def error_not_found(
        cls, message: str = "The requested resource could not be found"
    ):
        return cls.__error_code(code=404, status="not found", message=message)

    @classmethod
    def error_internal_server(cls, message=None):
        return cls.__error_code(
            code=500, status="internal server error", message=message
        )

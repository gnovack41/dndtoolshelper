from typing import Any, Literal

HTTP_METHODS = Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
JSON = str | int | float | bool | None | dict[str, Any] | list[Any]

class ReqBody:
    """A convenient way to handle request body"""

    def __init__(self, data, fields: list[str] = []):
        self.values = self.convert(data, fields)

    def get(self, field: str, default_value=None):
        return self.values.get(field, default_value)

    def set(self, field: str, new_value=None) -> None:
        self.values[field] = new_value

    def remove(self, field: str, default_value=None) -> None:
        return self.values.pop(field, default_value)

    def all_none(self) -> bool:
        return all(value is None for value in self.values.values())

    def some_none(self) -> bool:
        return any(value is None for value in self.values.values())

    @staticmethod
    def convert(data={}, fields: list[str] = []) -> dict:
        values = data if not fields else {
            field: str(getattr(data, field)) if hasattr(data, field)
            else data.get(field, None)
            for field in fields
        }
        return values

    def __repr__(self):
        return str(self.values)

    def __str__(self):
        return str(self.values)

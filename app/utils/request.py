class ReqBody:
    def __init__(self, data, fields=[]):
        self.values = data if not fields else {
            field: str(getattr(data, field)) if hasattr(data, field)
            else data.get(field, None)
            for field in fields
        }

    def get(self, field, default_value=None):
        return self.values.get(field, default_value)

    def set(self, field, new_value=None):
        self.values[field] = new_value

    def remove(self, field, default_value=None):
        return self.values.pop(field, default_value)

    def all_none(self):
        return all(value is None for value in self.values.values())

    def some_none(self):
        return any(value is None for value in self.values.values())

    def __repr__(self):
        return str(self.values)

    def __str__(self):
        return str(self.values)

from django.db import models
from .utils import trim_quotes, elisp_map_to_json
import json

class QuotedTextField(models.TextField):
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return trim_quotes(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return f'"{value}"'

class PropertiesField(models.TextField):
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        try: 
            jsonText = elisp_map_to_json(value)
            return json.loads(jsonText)
        except:
            return value

    def get_prep_value(self, value):
        if value is None:
            return value
        return value

class QuotedForeignKey(models.ForeignKey):
    
    def from_db_value(self, value, expression, connection):
        return value

    def get_prep_value(self, value):
        if value is None:
            return value
        return trim_quotes(value)

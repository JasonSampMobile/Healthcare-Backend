from language_strings.data_access import language_string_data_by_id
from web_errors import WebError


class LanguageString:
    def __init__(self, id, content_by_language):
        self.id = id
        self.content_by_language = content_by_language

    @classmethod
    def from_id(cls, id):
        data = {language: content
                for language, content in language_string_data_by_id(id)}
        if not len(data):
            raise WebError(f"string id '{id}' not found.", 404)
        return cls(id, data)

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content_by_language,
        }
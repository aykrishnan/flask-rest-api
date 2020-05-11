import abc
import simplejson as json


class ObjectMapper(abc.ABC):
    outgoing_fields = ()
    model_class = None

    @classmethod
    def convert_to_object(cls, json_data):
        return cls.model_class(**json_data)

    @classmethod
    def convert_to_json(cls, object_data):
        if object_data is None:
            return None
        if isinstance(object_data, list):
            return json.dumps(
                [
                    {
                        field_name: instance_data.__dict__[field_name] for field_name in cls.outgoing_fields
                    } for instance_data in object_data
                ],
                use_decimal=True
            )
        return json.dumps(
            {
                field_name: object_data.__dict__[field_name] for field_name in cls.outgoing_fields
            }, use_decimal=True
        )

from ..interfaces.item_interface import ItemInterface
import json

class Item(ItemInterface):

    def __init__(self, config):
        self.config = config
        self.__is_allow_stage_created = False
        self.__is_allow_stage_to_str = False
        self.__is_allow_stage_to_int = False
        self.__is_allow_stage_to_dict = False
        self.__is_allow_stage_to_json = False

    def to_dict(self):
        return self.config

    def __str__(self):
        result = ''
        return self.__trigger_stage('to.str', result) if self.__is_allow_stage_to_str else result

    def __int__(self):
        result = 0
        return self.__trigger_stage('to.int', result) if self.__is_allow_stage_to_int else result

    def __iter__(self):
        for i in self.config:
            yield i

    def json_encode(self) -> str:
        data = self.config
        return json.dumps(self.__trigger_stage('to.json', data)) if self.__is_allow_stage_to_json else json.dumps(data)

    def __eq__(self, other):
        attrs = self.config
        attrs_other = other.config
        if len(attrs) != len(attrs_other):
            return False

        attrs_keys = attrs.keys()

        equal = True
        for key in attrs_keys:
            if key in attrs_other:
                if attrs_other[key] != attrs[key]:
                    equal = False
                    break
            else:
                equal = False
                break

        return equal

    def created(self):
        if self.__is_allow_stage_created:
            self.__trigger_stage_to('created')

    def __trigger_stage(self, stage, result = None):
        """ get plugin by stage """
        plugins = []
        for plugin in plugins:
            result = plugin(self, result)

        return result
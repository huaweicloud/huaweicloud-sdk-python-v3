# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAssistantModelReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'name': 'str',
        'type': 'str',
        'model_service_api': 'str',
        'description': 'str',
        'function_call': 'bool',
        'chain_of_thought': 'bool'
    }

    attribute_map = {
        'service_name': 'service_name',
        'name': 'name',
        'type': 'type',
        'model_service_api': 'model_service_api',
        'description': 'description',
        'function_call': 'function_call',
        'chain_of_thought': 'chain_of_thought'
    }

    def __init__(self, service_name=None, name=None, type=None, model_service_api=None, description=None, function_call=None, chain_of_thought=None):
        r"""CreateAssistantModelReq

        The model defined in huaweicloud sdk

        :param service_name: **参数解释**： 服务名称。 **约束限制**： 不涉及 **取值范围**： 支持中英文、数字及 ._-，仅支持中英文、数字开头结尾，长度2-64。 **默认取值**： 不涉及 
        :type service_name: str
        :param name: **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 支持中英文、数字及 ._-，仅支持中英文、数字开头结尾，长度2-64。 **默认取值**： 不涉及 
        :type name: str
        :param type: **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * chat：文本对话模型 * embedding：嵌入模型 **默认取值**： 不涉及 
        :type type: str
        :param model_service_api: **参数解释**： 模型服务API地址。 **约束限制**： 不涉及 **取值范围**： 以http://或https://开头的有效API地址。 **默认取值**： 不涉及 
        :type model_service_api: str
        :param description: **参数解释**： 模型描述。 **约束限制**： 不涉及 **取值范围**： 字符长度为[0-1000]。 **默认取值**： 不涉及 
        :type description: str
        :param function_call: **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 
        :type function_call: bool
        :param chain_of_thought: **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 
        :type chain_of_thought: bool
        """
        
        

        self._service_name = None
        self._name = None
        self._type = None
        self._model_service_api = None
        self._description = None
        self._function_call = None
        self._chain_of_thought = None
        self.discriminator = None

        self.service_name = service_name
        self.name = name
        self.type = type
        self.model_service_api = model_service_api
        if description is not None:
            self.description = description
        self.function_call = function_call
        self.chain_of_thought = chain_of_thought

    @property
    def service_name(self):
        r"""Gets the service_name of this CreateAssistantModelReq.

        **参数解释**： 服务名称。 **约束限制**： 不涉及 **取值范围**： 支持中英文、数字及 ._-，仅支持中英文、数字开头结尾，长度2-64。 **默认取值**： 不涉及 

        :return: The service_name of this CreateAssistantModelReq.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this CreateAssistantModelReq.

        **参数解释**： 服务名称。 **约束限制**： 不涉及 **取值范围**： 支持中英文、数字及 ._-，仅支持中英文、数字开头结尾，长度2-64。 **默认取值**： 不涉及 

        :param service_name: The service_name of this CreateAssistantModelReq.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def name(self):
        r"""Gets the name of this CreateAssistantModelReq.

        **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 支持中英文、数字及 ._-，仅支持中英文、数字开头结尾，长度2-64。 **默认取值**： 不涉及 

        :return: The name of this CreateAssistantModelReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAssistantModelReq.

        **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 支持中英文、数字及 ._-，仅支持中英文、数字开头结尾，长度2-64。 **默认取值**： 不涉及 

        :param name: The name of this CreateAssistantModelReq.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreateAssistantModelReq.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * chat：文本对话模型 * embedding：嵌入模型 **默认取值**： 不涉及 

        :return: The type of this CreateAssistantModelReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateAssistantModelReq.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * chat：文本对话模型 * embedding：嵌入模型 **默认取值**： 不涉及 

        :param type: The type of this CreateAssistantModelReq.
        :type type: str
        """
        self._type = type

    @property
    def model_service_api(self):
        r"""Gets the model_service_api of this CreateAssistantModelReq.

        **参数解释**： 模型服务API地址。 **约束限制**： 不涉及 **取值范围**： 以http://或https://开头的有效API地址。 **默认取值**： 不涉及 

        :return: The model_service_api of this CreateAssistantModelReq.
        :rtype: str
        """
        return self._model_service_api

    @model_service_api.setter
    def model_service_api(self, model_service_api):
        r"""Sets the model_service_api of this CreateAssistantModelReq.

        **参数解释**： 模型服务API地址。 **约束限制**： 不涉及 **取值范围**： 以http://或https://开头的有效API地址。 **默认取值**： 不涉及 

        :param model_service_api: The model_service_api of this CreateAssistantModelReq.
        :type model_service_api: str
        """
        self._model_service_api = model_service_api

    @property
    def description(self):
        r"""Gets the description of this CreateAssistantModelReq.

        **参数解释**： 模型描述。 **约束限制**： 不涉及 **取值范围**： 字符长度为[0-1000]。 **默认取值**： 不涉及 

        :return: The description of this CreateAssistantModelReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAssistantModelReq.

        **参数解释**： 模型描述。 **约束限制**： 不涉及 **取值范围**： 字符长度为[0-1000]。 **默认取值**： 不涉及 

        :param description: The description of this CreateAssistantModelReq.
        :type description: str
        """
        self._description = description

    @property
    def function_call(self):
        r"""Gets the function_call of this CreateAssistantModelReq.

        **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 

        :return: The function_call of this CreateAssistantModelReq.
        :rtype: bool
        """
        return self._function_call

    @function_call.setter
    def function_call(self, function_call):
        r"""Sets the function_call of this CreateAssistantModelReq.

        **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 

        :param function_call: The function_call of this CreateAssistantModelReq.
        :type function_call: bool
        """
        self._function_call = function_call

    @property
    def chain_of_thought(self):
        r"""Gets the chain_of_thought of this CreateAssistantModelReq.

        **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 

        :return: The chain_of_thought of this CreateAssistantModelReq.
        :rtype: bool
        """
        return self._chain_of_thought

    @chain_of_thought.setter
    def chain_of_thought(self, chain_of_thought):
        r"""Sets the chain_of_thought of this CreateAssistantModelReq.

        **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 

        :param chain_of_thought: The chain_of_thought of this CreateAssistantModelReq.
        :type chain_of_thought: bool
        """
        self._chain_of_thought = chain_of_thought

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateAssistantModelReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

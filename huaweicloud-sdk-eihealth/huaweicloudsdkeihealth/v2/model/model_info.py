# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str',
        'service_name': 'str',
        'function_call': 'bool',
        'chain_of_thought': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'service_name': 'service_name',
        'function_call': 'function_call',
        'chain_of_thought': 'chain_of_thought'
    }

    def __init__(self, id=None, type=None, service_name=None, function_call=None, chain_of_thought=None):
        r"""ModelInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type id: str
        :param type: **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * CHAT：文本对话模型 * EMBEDDING：嵌入模型 **默认取值**： 不涉及 
        :type type: str
        :param service_name: **参数解释**： 服务名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type service_name: str
        :param function_call: **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 
        :type function_call: bool
        :param chain_of_thought: **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 
        :type chain_of_thought: bool
        """
        
        

        self._id = None
        self._type = None
        self._service_name = None
        self._function_call = None
        self._chain_of_thought = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if service_name is not None:
            self.service_name = service_name
        if function_call is not None:
            self.function_call = function_call
        if chain_of_thought is not None:
            self.chain_of_thought = chain_of_thought

    @property
    def id(self):
        r"""Gets the id of this ModelInfo.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The id of this ModelInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelInfo.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param id: The id of this ModelInfo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ModelInfo.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * CHAT：文本对话模型 * EMBEDDING：嵌入模型 **默认取值**： 不涉及 

        :return: The type of this ModelInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ModelInfo.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * CHAT：文本对话模型 * EMBEDDING：嵌入模型 **默认取值**： 不涉及 

        :param type: The type of this ModelInfo.
        :type type: str
        """
        self._type = type

    @property
    def service_name(self):
        r"""Gets the service_name of this ModelInfo.

        **参数解释**： 服务名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The service_name of this ModelInfo.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ModelInfo.

        **参数解释**： 服务名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param service_name: The service_name of this ModelInfo.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def function_call(self):
        r"""Gets the function_call of this ModelInfo.

        **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 

        :return: The function_call of this ModelInfo.
        :rtype: bool
        """
        return self._function_call

    @function_call.setter
    def function_call(self, function_call):
        r"""Sets the function_call of this ModelInfo.

        **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 

        :param function_call: The function_call of this ModelInfo.
        :type function_call: bool
        """
        self._function_call = function_call

    @property
    def chain_of_thought(self):
        r"""Gets the chain_of_thought of this ModelInfo.

        **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 

        :return: The chain_of_thought of this ModelInfo.
        :rtype: bool
        """
        return self._chain_of_thought

    @chain_of_thought.setter
    def chain_of_thought(self, chain_of_thought):
        r"""Sets the chain_of_thought of this ModelInfo.

        **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 

        :param chain_of_thought: The chain_of_thought of this ModelInfo.
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
        if not isinstance(other, ModelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

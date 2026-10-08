# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreModelBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model': 'str',
        'model_service_name': 'str',
        'type': 'list[str]',
        'protocol': 'str',
        'description': 'str'
    }

    attribute_map = {
        'model': 'model',
        'model_service_name': 'model_service_name',
        'type': 'type',
        'protocol': 'protocol',
        'description': 'description'
    }

    def __init__(self, model=None, model_service_name=None, type=None, protocol=None, description=None):
        r"""CoreModelBaseInfo

        The model defined in huaweicloud sdk

        :param model: **参数解释：** 模型名称。 **约束限制：** 不涉及。 **取值范围：** 长度为1-256个字符。由字母、数字、连字符、点、下划线、星号、问号和@符号组成的字符，支持*的前缀通配以及后缀通配。 **默认取值：** 不涉及。 
        :type model: str
        :param model_service_name: **参数解释：** 显示名称。 **约束限制：** 不涉及。 **取值范围：** 长度为2-64个字符，支持中英文、数字及符号: . _ / | \\ -，须以中英文或数字开头结尾。符合正则条件^[\\u4e00-\\u9fa5A-Za-z0-9][\\u4e00-\\u9fa5A-Za-z0-9._/|\\\\-]{0,62}[\\u4e00-\\u9fa5A-Za-z0-9]$。 **默认取值：** 不涉及。 
        :type model_service_name: str
        :param type: **参数解释：** 模型的类型。 **约束限制：** 不涉及。 **取值范围：** 数组长度为1-10个。 **默认取值：** 不涉及。 
        :type type: list[str]
        :param protocol: **参数解释：** API接口协议。 **约束限制：** 不涉及。 **取值范围：** - openai: 标准OpenAI协议 - anthropic: Anthropic协议 - maas_v1: MaaS标准API V1 **默认取值：** 不涉及。 
        :type protocol: str
        :param description: **参数解释：** 模型的详细描述。 **取值范围：** 长度为 0-1000 个字符。 
        :type description: str
        """
        
        

        self._model = None
        self._model_service_name = None
        self._type = None
        self._protocol = None
        self._description = None
        self.discriminator = None

        if model is not None:
            self.model = model
        if model_service_name is not None:
            self.model_service_name = model_service_name
        if type is not None:
            self.type = type
        if protocol is not None:
            self.protocol = protocol
        if description is not None:
            self.description = description

    @property
    def model(self):
        r"""Gets the model of this CoreModelBaseInfo.

        **参数解释：** 模型名称。 **约束限制：** 不涉及。 **取值范围：** 长度为1-256个字符。由字母、数字、连字符、点、下划线、星号、问号和@符号组成的字符，支持*的前缀通配以及后缀通配。 **默认取值：** 不涉及。 

        :return: The model of this CoreModelBaseInfo.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this CoreModelBaseInfo.

        **参数解释：** 模型名称。 **约束限制：** 不涉及。 **取值范围：** 长度为1-256个字符。由字母、数字、连字符、点、下划线、星号、问号和@符号组成的字符，支持*的前缀通配以及后缀通配。 **默认取值：** 不涉及。 

        :param model: The model of this CoreModelBaseInfo.
        :type model: str
        """
        self._model = model

    @property
    def model_service_name(self):
        r"""Gets the model_service_name of this CoreModelBaseInfo.

        **参数解释：** 显示名称。 **约束限制：** 不涉及。 **取值范围：** 长度为2-64个字符，支持中英文、数字及符号: . _ / | \\ -，须以中英文或数字开头结尾。符合正则条件^[\\u4e00-\\u9fa5A-Za-z0-9][\\u4e00-\\u9fa5A-Za-z0-9._/|\\\\-]{0,62}[\\u4e00-\\u9fa5A-Za-z0-9]$。 **默认取值：** 不涉及。 

        :return: The model_service_name of this CoreModelBaseInfo.
        :rtype: str
        """
        return self._model_service_name

    @model_service_name.setter
    def model_service_name(self, model_service_name):
        r"""Sets the model_service_name of this CoreModelBaseInfo.

        **参数解释：** 显示名称。 **约束限制：** 不涉及。 **取值范围：** 长度为2-64个字符，支持中英文、数字及符号: . _ / | \\ -，须以中英文或数字开头结尾。符合正则条件^[\\u4e00-\\u9fa5A-Za-z0-9][\\u4e00-\\u9fa5A-Za-z0-9._/|\\\\-]{0,62}[\\u4e00-\\u9fa5A-Za-z0-9]$。 **默认取值：** 不涉及。 

        :param model_service_name: The model_service_name of this CoreModelBaseInfo.
        :type model_service_name: str
        """
        self._model_service_name = model_service_name

    @property
    def type(self):
        r"""Gets the type of this CoreModelBaseInfo.

        **参数解释：** 模型的类型。 **约束限制：** 不涉及。 **取值范围：** 数组长度为1-10个。 **默认取值：** 不涉及。 

        :return: The type of this CoreModelBaseInfo.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CoreModelBaseInfo.

        **参数解释：** 模型的类型。 **约束限制：** 不涉及。 **取值范围：** 数组长度为1-10个。 **默认取值：** 不涉及。 

        :param type: The type of this CoreModelBaseInfo.
        :type type: list[str]
        """
        self._type = type

    @property
    def protocol(self):
        r"""Gets the protocol of this CoreModelBaseInfo.

        **参数解释：** API接口协议。 **约束限制：** 不涉及。 **取值范围：** - openai: 标准OpenAI协议 - anthropic: Anthropic协议 - maas_v1: MaaS标准API V1 **默认取值：** 不涉及。 

        :return: The protocol of this CoreModelBaseInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this CoreModelBaseInfo.

        **参数解释：** API接口协议。 **约束限制：** 不涉及。 **取值范围：** - openai: 标准OpenAI协议 - anthropic: Anthropic协议 - maas_v1: MaaS标准API V1 **默认取值：** 不涉及。 

        :param protocol: The protocol of this CoreModelBaseInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def description(self):
        r"""Gets the description of this CoreModelBaseInfo.

        **参数解释：** 模型的详细描述。 **取值范围：** 长度为 0-1000 个字符。 

        :return: The description of this CoreModelBaseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CoreModelBaseInfo.

        **参数解释：** 模型的详细描述。 **取值范围：** 长度为 0-1000 个字符。 

        :param description: The description of this CoreModelBaseInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CoreModelBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

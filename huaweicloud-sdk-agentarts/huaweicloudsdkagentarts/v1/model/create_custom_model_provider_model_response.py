# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCustomModelProviderModelResponse(SdkResponse):

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
        'description': 'str',
        'id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'model': 'model',
        'model_service_name': 'model_service_name',
        'type': 'type',
        'protocol': 'protocol',
        'description': 'description',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, model=None, model_service_name=None, type=None, protocol=None, description=None, id=None, created_at=None, updated_at=None):
        r"""CreateCustomModelProviderModelResponse

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
        :param id: **参数解释：** 模型配置ID。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 
        :type id: str
        :param created_at: **参数解释：** 模型配置创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 模型配置最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 
        :type updated_at: datetime
        """
        
        super().__init__()

        self._model = None
        self._model_service_name = None
        self._type = None
        self._protocol = None
        self._description = None
        self._id = None
        self._created_at = None
        self._updated_at = None
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
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def model(self):
        r"""Gets the model of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型名称。 **约束限制：** 不涉及。 **取值范围：** 长度为1-256个字符。由字母、数字、连字符、点、下划线、星号、问号和@符号组成的字符，支持*的前缀通配以及后缀通配。 **默认取值：** 不涉及。 

        :return: The model of this CreateCustomModelProviderModelResponse.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        r"""Sets the model of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型名称。 **约束限制：** 不涉及。 **取值范围：** 长度为1-256个字符。由字母、数字、连字符、点、下划线、星号、问号和@符号组成的字符，支持*的前缀通配以及后缀通配。 **默认取值：** 不涉及。 

        :param model: The model of this CreateCustomModelProviderModelResponse.
        :type model: str
        """
        self._model = model

    @property
    def model_service_name(self):
        r"""Gets the model_service_name of this CreateCustomModelProviderModelResponse.

        **参数解释：** 显示名称。 **约束限制：** 不涉及。 **取值范围：** 长度为2-64个字符，支持中英文、数字及符号: . _ / | \\ -，须以中英文或数字开头结尾。符合正则条件^[\\u4e00-\\u9fa5A-Za-z0-9][\\u4e00-\\u9fa5A-Za-z0-9._/|\\\\-]{0,62}[\\u4e00-\\u9fa5A-Za-z0-9]$。 **默认取值：** 不涉及。 

        :return: The model_service_name of this CreateCustomModelProviderModelResponse.
        :rtype: str
        """
        return self._model_service_name

    @model_service_name.setter
    def model_service_name(self, model_service_name):
        r"""Sets the model_service_name of this CreateCustomModelProviderModelResponse.

        **参数解释：** 显示名称。 **约束限制：** 不涉及。 **取值范围：** 长度为2-64个字符，支持中英文、数字及符号: . _ / | \\ -，须以中英文或数字开头结尾。符合正则条件^[\\u4e00-\\u9fa5A-Za-z0-9][\\u4e00-\\u9fa5A-Za-z0-9._/|\\\\-]{0,62}[\\u4e00-\\u9fa5A-Za-z0-9]$。 **默认取值：** 不涉及。 

        :param model_service_name: The model_service_name of this CreateCustomModelProviderModelResponse.
        :type model_service_name: str
        """
        self._model_service_name = model_service_name

    @property
    def type(self):
        r"""Gets the type of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型的类型。 **约束限制：** 不涉及。 **取值范围：** 数组长度为1-10个。 **默认取值：** 不涉及。 

        :return: The type of this CreateCustomModelProviderModelResponse.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型的类型。 **约束限制：** 不涉及。 **取值范围：** 数组长度为1-10个。 **默认取值：** 不涉及。 

        :param type: The type of this CreateCustomModelProviderModelResponse.
        :type type: list[str]
        """
        self._type = type

    @property
    def protocol(self):
        r"""Gets the protocol of this CreateCustomModelProviderModelResponse.

        **参数解释：** API接口协议。 **约束限制：** 不涉及。 **取值范围：** - openai: 标准OpenAI协议 - anthropic: Anthropic协议 - maas_v1: MaaS标准API V1 **默认取值：** 不涉及。 

        :return: The protocol of this CreateCustomModelProviderModelResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this CreateCustomModelProviderModelResponse.

        **参数解释：** API接口协议。 **约束限制：** 不涉及。 **取值范围：** - openai: 标准OpenAI协议 - anthropic: Anthropic协议 - maas_v1: MaaS标准API V1 **默认取值：** 不涉及。 

        :param protocol: The protocol of this CreateCustomModelProviderModelResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def description(self):
        r"""Gets the description of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型的详细描述。 **取值范围：** 长度为 0-1000 个字符。 

        :return: The description of this CreateCustomModelProviderModelResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型的详细描述。 **取值范围：** 长度为 0-1000 个字符。 

        :param description: The description of this CreateCustomModelProviderModelResponse.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型配置ID。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :return: The id of this CreateCustomModelProviderModelResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型配置ID。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :param id: The id of this CreateCustomModelProviderModelResponse.
        :type id: str
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型配置创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :return: The created_at of this CreateCustomModelProviderModelResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型配置创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :param created_at: The created_at of this CreateCustomModelProviderModelResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型配置最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :return: The updated_at of this CreateCustomModelProviderModelResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateCustomModelProviderModelResponse.

        **参数解释：** 模型配置最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :param updated_at: The updated_at of this CreateCustomModelProviderModelResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("CreateCustomModelProviderModelResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateCustomModelProviderModelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

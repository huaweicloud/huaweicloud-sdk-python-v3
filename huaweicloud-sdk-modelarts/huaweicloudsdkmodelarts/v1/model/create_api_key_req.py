# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateApiKeyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'scope': 'scope'
    }

    def __init__(self, name=None, description=None, scope=None):
        r"""CreateApiKeyReq

        The model defined in huaweicloud sdk

        :param name: **参数解释：** api-key名称，用户在[创建API_KEY](CreateInferApiKey.xml)时自定义。 **约束限制：** api-key在删除之前名字不能重复。 **取值范围：** 支持1-64个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** api-key描述。 **约束限制：** 不涉及。 **取值范围：** 长度不可以超过256，不能包含感叹号，大于号，小于号，等号，与，单引号，双引号。 **默认取值：** 默认为空。
        :type description: str
        :param scope: **参数解释：** api-key生效范围。 **约束限制：** 不涉及。 **取值范围：** - USER：表示生效范围为用户级别，可以访问该用户创建的所有在线服务。 - SERVICE：表示生效范围为单个服务，可以访问绑定该api-key的在线服务。 **默认取值：** 不涉及。
        :type scope: str
        """
        
        

        self._name = None
        self._description = None
        self._scope = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.scope = scope

    @property
    def name(self):
        r"""Gets the name of this CreateApiKeyReq.

        **参数解释：** api-key名称，用户在[创建API_KEY](CreateInferApiKey.xml)时自定义。 **约束限制：** api-key在删除之前名字不能重复。 **取值范围：** 支持1-64个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。

        :return: The name of this CreateApiKeyReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateApiKeyReq.

        **参数解释：** api-key名称，用户在[创建API_KEY](CreateInferApiKey.xml)时自定义。 **约束限制：** api-key在删除之前名字不能重复。 **取值范围：** 支持1-64个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。

        :param name: The name of this CreateApiKeyReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateApiKeyReq.

        **参数解释：** api-key描述。 **约束限制：** 不涉及。 **取值范围：** 长度不可以超过256，不能包含感叹号，大于号，小于号，等号，与，单引号，双引号。 **默认取值：** 默认为空。

        :return: The description of this CreateApiKeyReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateApiKeyReq.

        **参数解释：** api-key描述。 **约束限制：** 不涉及。 **取值范围：** 长度不可以超过256，不能包含感叹号，大于号，小于号，等号，与，单引号，双引号。 **默认取值：** 默认为空。

        :param description: The description of this CreateApiKeyReq.
        :type description: str
        """
        self._description = description

    @property
    def scope(self):
        r"""Gets the scope of this CreateApiKeyReq.

        **参数解释：** api-key生效范围。 **约束限制：** 不涉及。 **取值范围：** - USER：表示生效范围为用户级别，可以访问该用户创建的所有在线服务。 - SERVICE：表示生效范围为单个服务，可以访问绑定该api-key的在线服务。 **默认取值：** 不涉及。

        :return: The scope of this CreateApiKeyReq.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this CreateApiKeyReq.

        **参数解释：** api-key生效范围。 **约束限制：** 不涉及。 **取值范围：** - USER：表示生效范围为用户级别，可以访问该用户创建的所有在线服务。 - SERVICE：表示生效范围为单个服务，可以访问绑定该api-key的在线服务。 **默认取值：** 不涉及。

        :param scope: The scope of this CreateApiKeyReq.
        :type scope: str
        """
        self._scope = scope

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
        if not isinstance(other, CreateApiKeyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

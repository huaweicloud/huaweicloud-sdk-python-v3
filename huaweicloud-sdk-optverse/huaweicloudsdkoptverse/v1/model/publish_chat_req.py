# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishChatReq:

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
        'type': 'AgentType'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type'
    }

    def __init__(self, name=None, description=None, type=None):
        r"""PublishChatReq

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 发布资产名称。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-128]个字符。 **默认取值**： 不涉及 
        :type name: str
        :param description: **参数解释**： 发布资产描述。 **约束限制**： 不涉及 **取值范围**： 取值范围为[0-1024]个字符。 **默认取值**： 不涉及 
        :type description: str
        :param type: 
        :type type: :class:`huaweicloudsdkoptverse.v1.AgentType`
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type

    @property
    def name(self):
        r"""Gets the name of this PublishChatReq.

        **参数解释**： 发布资产名称。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The name of this PublishChatReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PublishChatReq.

        **参数解释**： 发布资产名称。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-128]个字符。 **默认取值**： 不涉及 

        :param name: The name of this PublishChatReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PublishChatReq.

        **参数解释**： 发布资产描述。 **约束限制**： 不涉及 **取值范围**： 取值范围为[0-1024]个字符。 **默认取值**： 不涉及 

        :return: The description of this PublishChatReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PublishChatReq.

        **参数解释**： 发布资产描述。 **约束限制**： 不涉及 **取值范围**： 取值范围为[0-1024]个字符。 **默认取值**： 不涉及 

        :param description: The description of this PublishChatReq.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this PublishChatReq.

        :return: The type of this PublishChatReq.
        :rtype: :class:`huaweicloudsdkoptverse.v1.AgentType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PublishChatReq.

        :param type: The type of this PublishChatReq.
        :type type: :class:`huaweicloudsdkoptverse.v1.AgentType`
        """
        self._type = type

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
        if not isinstance(other, PublishChatReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

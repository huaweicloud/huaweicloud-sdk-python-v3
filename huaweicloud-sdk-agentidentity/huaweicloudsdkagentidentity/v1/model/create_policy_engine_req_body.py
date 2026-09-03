# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyEngineReqBody:

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
        'type': 'PolicyEngineType',
        'description': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, name=None, type=None, description=None, tags=None):
        r"""CreatePolicyEngineReqBody

        The model defined in huaweicloud sdk

        :param name: Customer-assigned immutable name for the policy engine.
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineType`
        :param description: 策略集的可读描述。
        :type description: str
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.type = type
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreatePolicyEngineReqBody.

        Customer-assigned immutable name for the policy engine.

        :return: The name of this CreatePolicyEngineReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePolicyEngineReqBody.

        Customer-assigned immutable name for the policy engine.

        :param name: The name of this CreatePolicyEngineReqBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreatePolicyEngineReqBody.

        :return: The type of this CreatePolicyEngineReqBody.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreatePolicyEngineReqBody.

        :param type: The type of this CreatePolicyEngineReqBody.
        :type type: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineType`
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this CreatePolicyEngineReqBody.

        策略集的可读描述。

        :return: The description of this CreatePolicyEngineReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePolicyEngineReqBody.

        策略集的可读描述。

        :param description: The description of this CreatePolicyEngineReqBody.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this CreatePolicyEngineReqBody.

        自定义标签列表。

        :return: The tags of this CreatePolicyEngineReqBody.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreatePolicyEngineReqBody.

        自定义标签列表。

        :param tags: The tags of this CreatePolicyEngineReqBody.
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreatePolicyEngineReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

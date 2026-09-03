# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyEngineReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, description=None, tags=None):
        r"""UpdatePolicyEngineReqBody

        The model defined in huaweicloud sdk

        :param description: 策略集的更新描述。
        :type description: str
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        
        

        self._description = None
        self._tags = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def description(self):
        r"""Gets the description of this UpdatePolicyEngineReqBody.

        策略集的更新描述。

        :return: The description of this UpdatePolicyEngineReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePolicyEngineReqBody.

        策略集的更新描述。

        :param description: The description of this UpdatePolicyEngineReqBody.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this UpdatePolicyEngineReqBody.

        自定义标签列表。

        :return: The tags of this UpdatePolicyEngineReqBody.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdatePolicyEngineReqBody.

        自定义标签列表。

        :param tags: The tags of this UpdatePolicyEngineReqBody.
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
        if not isinstance(other, UpdatePolicyEngineReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

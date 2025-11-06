# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteIpRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str'
    }

    attribute_map = {
        'type': 'type'
    }

    def __init__(self, type=None):
        r"""DeleteIpRequestBody

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 需要删除IP的组类型。 **约束限制：** 不涉及。 **取值范围：** shard：表示删除所有Shard组IP。 config：表示删除Config组IP。 **默认取值：** 不涉及。
        :type type: str
        """
        
        

        self._type = None
        self.discriminator = None

        self.type = type

    @property
    def type(self):
        r"""Gets the type of this DeleteIpRequestBody.

        **参数解释：** 需要删除IP的组类型。 **约束限制：** 不涉及。 **取值范围：** shard：表示删除所有Shard组IP。 config：表示删除Config组IP。 **默认取值：** 不涉及。

        :return: The type of this DeleteIpRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeleteIpRequestBody.

        **参数解释：** 需要删除IP的组类型。 **约束限制：** 不涉及。 **取值范围：** shard：表示删除所有Shard组IP。 config：表示删除Config组IP。 **默认取值：** 不涉及。

        :param type: The type of this DeleteIpRequestBody.
        :type type: str
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
        if not isinstance(other, DeleteIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

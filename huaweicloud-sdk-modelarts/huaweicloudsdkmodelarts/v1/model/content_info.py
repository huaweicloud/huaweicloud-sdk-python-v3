# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_num': 'str',
        'desc': 'str'
    }

    attribute_map = {
        'version_num': 'version_num',
        'desc': 'desc'
    }

    def __init__(self, version_num=None, desc=None):
        r"""ContentInfo

        The model defined in huaweicloud sdk

        :param version_num: **参数解释**：版本数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type version_num: str
        :param desc: **参数解释**：描述。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type desc: str
        """
        
        

        self._version_num = None
        self._desc = None
        self.discriminator = None

        if version_num is not None:
            self.version_num = version_num
        if desc is not None:
            self.desc = desc

    @property
    def version_num(self):
        r"""Gets the version_num of this ContentInfo.

        **参数解释**：版本数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The version_num of this ContentInfo.
        :rtype: str
        """
        return self._version_num

    @version_num.setter
    def version_num(self, version_num):
        r"""Sets the version_num of this ContentInfo.

        **参数解释**：版本数量。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param version_num: The version_num of this ContentInfo.
        :type version_num: str
        """
        self._version_num = version_num

    @property
    def desc(self):
        r"""Gets the desc of this ContentInfo.

        **参数解释**：描述。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The desc of this ContentInfo.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ContentInfo.

        **参数解释**：描述。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param desc: The desc of this ContentInfo.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, ContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

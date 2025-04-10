# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagV5DTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_key': 'str',
        'tag_value': 'str'
    }

    attribute_map = {
        'tag_key': 'tag_key',
        'tag_value': 'tag_value'
    }

    def __init__(self, tag_key=None, tag_value=None):
        r"""TagV5DTO

        The model defined in huaweicloud sdk

        :param tag_key: **参数说明**：标签键，在同一资源下标签键唯一。绑定资源时，如果设置的键已存在，则将覆盖之前的标签值。如果设置的键值不存在，则新增标签。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_.-等字符的组合。
        :type tag_key: str
        :param tag_value: **参数说明**：标签值。 **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。
        :type tag_value: str
        """
        
        

        self._tag_key = None
        self._tag_value = None
        self.discriminator = None

        self.tag_key = tag_key
        if tag_value is not None:
            self.tag_value = tag_value

    @property
    def tag_key(self):
        r"""Gets the tag_key of this TagV5DTO.

        **参数说明**：标签键，在同一资源下标签键唯一。绑定资源时，如果设置的键已存在，则将覆盖之前的标签值。如果设置的键值不存在，则新增标签。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_.-等字符的组合。

        :return: The tag_key of this TagV5DTO.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this TagV5DTO.

        **参数说明**：标签键，在同一资源下标签键唯一。绑定资源时，如果设置的键已存在，则将覆盖之前的标签值。如果设置的键值不存在，则新增标签。 **取值范围**：长度不超过64，只允许中文、字母、数字、以及_.-等字符的组合。

        :param tag_key: The tag_key of this TagV5DTO.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def tag_value(self):
        r"""Gets the tag_value of this TagV5DTO.

        **参数说明**：标签值。 **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。

        :return: The tag_value of this TagV5DTO.
        :rtype: str
        """
        return self._tag_value

    @tag_value.setter
    def tag_value(self, tag_value):
        r"""Sets the tag_value of this TagV5DTO.

        **参数说明**：标签值。 **取值范围**：长度不超过128，只允许中文、字母、数字、以及_.-等字符的组合。

        :param tag_value: The tag_value of this TagV5DTO.
        :type tag_value: str
        """
        self._tag_value = tag_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TagV5DTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

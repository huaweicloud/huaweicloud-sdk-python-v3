# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TypedStatBucket:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'count': 'int'
    }

    attribute_map = {
        'key': 'key',
        'count': 'count'
    }

    def __init__(self, key=None, count=None):
        r"""TypedStatBucket

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 统计键（如bot类型、域名等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key: str
        :param count: **参数解释：** 该键对应的命中请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type count: int
        """
        
        

        self._key = None
        self._count = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if count is not None:
            self.count = count

    @property
    def key(self):
        r"""Gets the key of this TypedStatBucket.

        **参数解释：** 统计键（如bot类型、域名等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key of this TypedStatBucket.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this TypedStatBucket.

        **参数解释：** 统计键（如bot类型、域名等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key: The key of this TypedStatBucket.
        :type key: str
        """
        self._key = key

    @property
    def count(self):
        r"""Gets the count of this TypedStatBucket.

        **参数解释：** 该键对应的命中请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The count of this TypedStatBucket.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this TypedStatBucket.

        **参数解释：** 该键对应的命中请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param count: The count of this TypedStatBucket.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, TypedStatBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

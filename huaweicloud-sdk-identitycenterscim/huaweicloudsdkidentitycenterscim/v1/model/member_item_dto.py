# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberItemDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'str',
        'ref': 'str',
        'type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'ref': '$ref',
        'type': 'type'
    }

    def __init__(self, value=None, ref=None, type=None):
        r"""MemberItemDto

        The model defined in huaweicloud sdk

        :param value: 成员的全局唯一标识符（ID）
        :type value: str
        :param ref: 成员的引用信息
        :type ref: str
        :param type: 成员类型 User：用户
        :type type: str
        """
        
        

        self._value = None
        self._ref = None
        self._type = None
        self.discriminator = None

        self.value = value
        if ref is not None:
            self.ref = ref
        if type is not None:
            self.type = type

    @property
    def value(self):
        r"""Gets the value of this MemberItemDto.

        成员的全局唯一标识符（ID）

        :return: The value of this MemberItemDto.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this MemberItemDto.

        成员的全局唯一标识符（ID）

        :param value: The value of this MemberItemDto.
        :type value: str
        """
        self._value = value

    @property
    def ref(self):
        r"""Gets the ref of this MemberItemDto.

        成员的引用信息

        :return: The ref of this MemberItemDto.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this MemberItemDto.

        成员的引用信息

        :param ref: The ref of this MemberItemDto.
        :type ref: str
        """
        self._ref = ref

    @property
    def type(self):
        r"""Gets the type of this MemberItemDto.

        成员类型 User：用户

        :return: The type of this MemberItemDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MemberItemDto.

        成员类型 User：用户

        :param type: The type of this MemberItemDto.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, MemberItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

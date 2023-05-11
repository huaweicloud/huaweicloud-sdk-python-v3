# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MediaTypes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base': 'str',
        'type': 'str'
    }

    attribute_map = {
        'base': 'base',
        'type': 'type'
    }

    def __init__(self, base=None, type=None):
        """MediaTypes

        The model defined in huaweicloud sdk

        :param base: 文本类型
        :type base: str
        :param type: 返回类型
        :type type: str
        """
        
        

        self._base = None
        self._type = None
        self.discriminator = None

        self.base = base
        self.type = type

    @property
    def base(self):
        """Gets the base of this MediaTypes.

        文本类型

        :return: The base of this MediaTypes.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this MediaTypes.

        文本类型

        :param base: The base of this MediaTypes.
        :type base: str
        """
        self._base = base

    @property
    def type(self):
        """Gets the type of this MediaTypes.

        返回类型

        :return: The type of this MediaTypes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MediaTypes.

        返回类型

        :param type: The type of this MediaTypes.
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
        if not isinstance(other, MediaTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaVersionMediaType:

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
        r"""NovaVersionMediaType

        The model defined in huaweicloud sdk

        :param base: 基础类型。
        :type base: str
        :param type: 媒体类型。
        :type type: str
        """
        
        

        self._base = None
        self._type = None
        self.discriminator = None

        self.base = base
        self.type = type

    @property
    def base(self):
        r"""Gets the base of this NovaVersionMediaType.

        基础类型。

        :return: The base of this NovaVersionMediaType.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        r"""Sets the base of this NovaVersionMediaType.

        基础类型。

        :param base: The base of this NovaVersionMediaType.
        :type base: str
        """
        self._base = base

    @property
    def type(self):
        r"""Gets the type of this NovaVersionMediaType.

        媒体类型。

        :return: The type of this NovaVersionMediaType.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NovaVersionMediaType.

        媒体类型。

        :param type: The type of this NovaVersionMediaType.
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
        if not isinstance(other, NovaVersionMediaType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

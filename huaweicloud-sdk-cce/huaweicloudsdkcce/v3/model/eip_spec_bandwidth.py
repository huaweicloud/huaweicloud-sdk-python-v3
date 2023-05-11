# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipSpecBandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'sharetype': 'str'
    }

    attribute_map = {
        'size': 'size',
        'sharetype': 'sharetype'
    }

    def __init__(self, size=None, sharetype=None):
        """EipSpecBandwidth

        The model defined in huaweicloud sdk

        :param size: 带宽大小
        :type size: int
        :param sharetype: 带宽类型
        :type sharetype: str
        """
        
        

        self._size = None
        self._sharetype = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if sharetype is not None:
            self.sharetype = sharetype

    @property
    def size(self):
        """Gets the size of this EipSpecBandwidth.

        带宽大小

        :return: The size of this EipSpecBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this EipSpecBandwidth.

        带宽大小

        :param size: The size of this EipSpecBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def sharetype(self):
        """Gets the sharetype of this EipSpecBandwidth.

        带宽类型

        :return: The sharetype of this EipSpecBandwidth.
        :rtype: str
        """
        return self._sharetype

    @sharetype.setter
    def sharetype(self, sharetype):
        """Sets the sharetype of this EipSpecBandwidth.

        带宽类型

        :param sharetype: The sharetype of this EipSpecBandwidth.
        :type sharetype: str
        """
        self._sharetype = sharetype

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
        if not isinstance(other, EipSpecBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

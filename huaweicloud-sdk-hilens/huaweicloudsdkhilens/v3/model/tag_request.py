# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagRequest:

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
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        r"""TagRequest

        The model defined in huaweicloud sdk

        :param key: 部署节点标签的key值，长度取值范围为1~36，由英文字母，数字，中划线和下划线组成，长度1到36个字符
        :type key: str
        :param value: 部署节点标签的value值，长度取值范围为1~43，由英文字母，数字，下划线，点号和中划线组成，长度0到43个字符
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this TagRequest.

        部署节点标签的key值，长度取值范围为1~36，由英文字母，数字，中划线和下划线组成，长度1到36个字符

        :return: The key of this TagRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this TagRequest.

        部署节点标签的key值，长度取值范围为1~36，由英文字母，数字，中划线和下划线组成，长度1到36个字符

        :param key: The key of this TagRequest.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this TagRequest.

        部署节点标签的value值，长度取值范围为1~43，由英文字母，数字，下划线，点号和中划线组成，长度0到43个字符

        :return: The value of this TagRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this TagRequest.

        部署节点标签的value值，长度取值范围为1~43，由英文字母，数字，下划线，点号和中划线组成，长度0到43个字符

        :param value: The value of this TagRequest.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, TagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

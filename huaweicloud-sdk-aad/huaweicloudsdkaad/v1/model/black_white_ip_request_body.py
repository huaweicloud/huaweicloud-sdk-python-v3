# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlackWhiteIpRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'ip_list': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'ip_list': 'ip_list'
    }

    def __init__(self, type=None, ip_list=None):
        """BlackWhiteIpRequestBody

        The model defined in huaweicloud sdk

        :param type: 类型。white：白名单，black：黑名单
        :type type: str
        :param ip_list: ip列表
        :type ip_list: list[str]
        """
        
        

        self._type = None
        self._ip_list = None
        self.discriminator = None

        self.type = type
        self.ip_list = ip_list

    @property
    def type(self):
        """Gets the type of this BlackWhiteIpRequestBody.

        类型。white：白名单，black：黑名单

        :return: The type of this BlackWhiteIpRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BlackWhiteIpRequestBody.

        类型。white：白名单，black：黑名单

        :param type: The type of this BlackWhiteIpRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def ip_list(self):
        """Gets the ip_list of this BlackWhiteIpRequestBody.

        ip列表

        :return: The ip_list of this BlackWhiteIpRequestBody.
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this BlackWhiteIpRequestBody.

        ip列表

        :param ip_list: The ip_list of this BlackWhiteIpRequestBody.
        :type ip_list: list[str]
        """
        self._ip_list = ip_list

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
        if not isinstance(other, BlackWhiteIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

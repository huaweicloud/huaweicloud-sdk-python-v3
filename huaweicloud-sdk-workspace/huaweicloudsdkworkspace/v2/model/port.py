# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Port:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ip_address': 'ip_address'
    }

    def __init__(self, id=None, ip_address=None):
        r"""Port

        The model defined in huaweicloud sdk

        :param id: 私有IP唯一标识
        :type id: str
        :param ip_address: 私有IP地址
        :type ip_address: str
        """
        
        

        self._id = None
        self._ip_address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def id(self):
        r"""Gets the id of this Port.

        私有IP唯一标识

        :return: The id of this Port.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Port.

        私有IP唯一标识

        :param id: The id of this Port.
        :type id: str
        """
        self._id = id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this Port.

        私有IP地址

        :return: The ip_address of this Port.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this Port.

        私有IP地址

        :param ip_address: The ip_address of this Port.
        :type ip_address: str
        """
        self._ip_address = ip_address

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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

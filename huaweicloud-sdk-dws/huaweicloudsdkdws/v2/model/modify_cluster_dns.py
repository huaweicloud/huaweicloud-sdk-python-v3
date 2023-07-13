# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyClusterDns:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'ttl': 'ttl'
    }

    def __init__(self, name=None, type=None, ttl=None):
        """ModifyClusterDns

        The model defined in huaweicloud sdk

        :param name: 待修改的域名。
        :type name: str
        :param type: 域名类型。 - public：公网域名。 - private：内网域名。
        :type type: str
        :param ttl: 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。 - 取值范围：300~2147483647。 - 默认值为300s。
        :type ttl: int
        """
        
        

        self._name = None
        self._type = None
        self._ttl = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.ttl = ttl

    @property
    def name(self):
        """Gets the name of this ModifyClusterDns.

        待修改的域名。

        :return: The name of this ModifyClusterDns.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyClusterDns.

        待修改的域名。

        :param name: The name of this ModifyClusterDns.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ModifyClusterDns.

        域名类型。 - public：公网域名。 - private：内网域名。

        :return: The type of this ModifyClusterDns.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModifyClusterDns.

        域名类型。 - public：公网域名。 - private：内网域名。

        :param type: The type of this ModifyClusterDns.
        :type type: str
        """
        self._type = type

    @property
    def ttl(self):
        """Gets the ttl of this ModifyClusterDns.

        用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。 - 取值范围：300~2147483647。 - 默认值为300s。

        :return: The ttl of this ModifyClusterDns.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this ModifyClusterDns.

        用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。 - 取值范围：300~2147483647。 - 默认值为300s。

        :param ttl: The ttl of this ModifyClusterDns.
        :type ttl: int
        """
        self._ttl = ttl

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
        if not isinstance(other, ModifyClusterDns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

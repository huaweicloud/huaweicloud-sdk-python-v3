# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Nics:

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
        'name': 'str',
        'cidr': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'cidr': 'cidr',
        'ip': 'ip'
    }

    def __init__(self, id=None, name=None, cidr=None, ip=None):
        """Nics

        The model defined in huaweicloud sdk

        :param id: 子网ID，如果是自动创建，使用\&quot;autoCreate\&quot;
        :type id: str
        :param name: 子网名称
        :type name: str
        :param cidr: 子网网关/掩码
        :type cidr: str
        :param ip: 虚拟机IP地址，如果没有这个字段，自动分配IP
        :type ip: str
        """
        
        

        self._id = None
        self._name = None
        self._cidr = None
        self._ip = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.cidr = cidr
        if ip is not None:
            self.ip = ip

    @property
    def id(self):
        """Gets the id of this Nics.

        子网ID，如果是自动创建，使用\"autoCreate\"

        :return: The id of this Nics.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Nics.

        子网ID，如果是自动创建，使用\"autoCreate\"

        :param id: The id of this Nics.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Nics.

        子网名称

        :return: The name of this Nics.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Nics.

        子网名称

        :param name: The name of this Nics.
        :type name: str
        """
        self._name = name

    @property
    def cidr(self):
        """Gets the cidr of this Nics.

        子网网关/掩码

        :return: The cidr of this Nics.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Nics.

        子网网关/掩码

        :param cidr: The cidr of this Nics.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def ip(self):
        """Gets the ip of this Nics.

        虚拟机IP地址，如果没有这个字段，自动分配IP

        :return: The ip of this Nics.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Nics.

        虚拟机IP地址，如果没有这个字段，自动分配IP

        :param ip: The ip of this Nics.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, Nics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

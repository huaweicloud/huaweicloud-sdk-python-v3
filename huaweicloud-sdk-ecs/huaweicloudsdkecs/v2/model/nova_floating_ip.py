# coding: utf-8

import pprint
import re

import six


class NovaFloatingIp(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'fixed_ip': 'str',
        'id': 'str',
        'instance_id': 'str',
        'ip': 'str',
        'pool': 'str'
    }

    attribute_map = {
        'fixed_ip': 'fixed_ip',
        'id': 'id',
        'instance_id': 'instance_id',
        'ip': 'ip',
        'pool': 'pool'
    }

    def __init__(self, fixed_ip=None, id=None, instance_id=None, ip=None, pool=None):  # noqa: E501
        """NovaFloatingIp - a model defined in huaweicloud sdk"""

        self._fixed_ip = None
        self._id = None
        self._instance_id = None
        self._ip = None
        self._pool = None
        self.discriminator = None

        self.fixed_ip = fixed_ip
        self.id = id
        self.instance_id = instance_id
        self.ip = ip
        self.pool = pool

    @property
    def fixed_ip(self):
        """Gets the fixed_ip of this NovaFloatingIp.

        私有IP地址.

        :return: The fixed_ip of this NovaFloatingIp.
        :rtype: str
        """
        return self._fixed_ip

    @fixed_ip.setter
    def fixed_ip(self, fixed_ip):
        """Sets the fixed_ip of this NovaFloatingIp.

        私有IP地址.

        :param fixed_ip: The fixed_ip of this NovaFloatingIp.
        :type: str
        """
        self._fixed_ip = fixed_ip

    @property
    def id(self):
        """Gets the id of this NovaFloatingIp.

        浮动IP的ID，UUID格式。

        :return: The id of this NovaFloatingIp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaFloatingIp.

        浮动IP的ID，UUID格式。

        :param id: The id of this NovaFloatingIp.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this NovaFloatingIp.

        被绑定主机的ID，UUID格式。

        :return: The instance_id of this NovaFloatingIp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this NovaFloatingIp.

        被绑定主机的ID，UUID格式。

        :param instance_id: The instance_id of this NovaFloatingIp.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def ip(self):
        """Gets the ip of this NovaFloatingIp.

        浮动IP的ip地址。

        :return: The ip of this NovaFloatingIp.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this NovaFloatingIp.

        浮动IP的ip地址。

        :param ip: The ip of this NovaFloatingIp.
        :type: str
        """
        self._ip = ip

    @property
    def pool(self):
        """Gets the pool of this NovaFloatingIp.

        网络资源池名称，用于分配浮动IP。

        :return: The pool of this NovaFloatingIp.
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this NovaFloatingIp.

        网络资源池名称，用于分配浮动IP。

        :param pool: The pool of this NovaFloatingIp.
        :type: str
        """
        self._pool = pool

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NovaFloatingIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

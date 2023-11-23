# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EntrypointItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_entrypoint': 'str',
        'master_entrypoint_ipv6': 'str',
        'slave_entrypoint': 'str',
        'slave_entrypoint_ipv6': 'str',
        'type': 'str'
    }

    attribute_map = {
        'master_entrypoint': 'masterEntrypoint',
        'master_entrypoint_ipv6': 'masterEntrypointIpv6',
        'slave_entrypoint': 'slave_entrypoint',
        'slave_entrypoint_ipv6': 'slaveEntrypointIpv6',
        'type': 'type'
    }

    def __init__(self, master_entrypoint=None, master_entrypoint_ipv6=None, slave_entrypoint=None, slave_entrypoint_ipv6=None, type=None):
        """EntrypointItem

        The model defined in huaweicloud sdk

        :param master_entrypoint: 微服务引擎专享版组件的ipv4主接入地址
        :type master_entrypoint: str
        :param master_entrypoint_ipv6: 微服务引擎专享版组件的ipv6主接入地址
        :type master_entrypoint_ipv6: str
        :param slave_entrypoint: 微服务引擎专享版组件的ipv4备接入地址
        :type slave_entrypoint: str
        :param slave_entrypoint_ipv6: 微服务引擎专享版组件的ipv6备接入地址
        :type slave_entrypoint_ipv6: str
        :param type: 微服务引擎专享版组件类型
        :type type: str
        """
        
        

        self._master_entrypoint = None
        self._master_entrypoint_ipv6 = None
        self._slave_entrypoint = None
        self._slave_entrypoint_ipv6 = None
        self._type = None
        self.discriminator = None

        if master_entrypoint is not None:
            self.master_entrypoint = master_entrypoint
        if master_entrypoint_ipv6 is not None:
            self.master_entrypoint_ipv6 = master_entrypoint_ipv6
        if slave_entrypoint is not None:
            self.slave_entrypoint = slave_entrypoint
        if slave_entrypoint_ipv6 is not None:
            self.slave_entrypoint_ipv6 = slave_entrypoint_ipv6
        if type is not None:
            self.type = type

    @property
    def master_entrypoint(self):
        """Gets the master_entrypoint of this EntrypointItem.

        微服务引擎专享版组件的ipv4主接入地址

        :return: The master_entrypoint of this EntrypointItem.
        :rtype: str
        """
        return self._master_entrypoint

    @master_entrypoint.setter
    def master_entrypoint(self, master_entrypoint):
        """Sets the master_entrypoint of this EntrypointItem.

        微服务引擎专享版组件的ipv4主接入地址

        :param master_entrypoint: The master_entrypoint of this EntrypointItem.
        :type master_entrypoint: str
        """
        self._master_entrypoint = master_entrypoint

    @property
    def master_entrypoint_ipv6(self):
        """Gets the master_entrypoint_ipv6 of this EntrypointItem.

        微服务引擎专享版组件的ipv6主接入地址

        :return: The master_entrypoint_ipv6 of this EntrypointItem.
        :rtype: str
        """
        return self._master_entrypoint_ipv6

    @master_entrypoint_ipv6.setter
    def master_entrypoint_ipv6(self, master_entrypoint_ipv6):
        """Sets the master_entrypoint_ipv6 of this EntrypointItem.

        微服务引擎专享版组件的ipv6主接入地址

        :param master_entrypoint_ipv6: The master_entrypoint_ipv6 of this EntrypointItem.
        :type master_entrypoint_ipv6: str
        """
        self._master_entrypoint_ipv6 = master_entrypoint_ipv6

    @property
    def slave_entrypoint(self):
        """Gets the slave_entrypoint of this EntrypointItem.

        微服务引擎专享版组件的ipv4备接入地址

        :return: The slave_entrypoint of this EntrypointItem.
        :rtype: str
        """
        return self._slave_entrypoint

    @slave_entrypoint.setter
    def slave_entrypoint(self, slave_entrypoint):
        """Sets the slave_entrypoint of this EntrypointItem.

        微服务引擎专享版组件的ipv4备接入地址

        :param slave_entrypoint: The slave_entrypoint of this EntrypointItem.
        :type slave_entrypoint: str
        """
        self._slave_entrypoint = slave_entrypoint

    @property
    def slave_entrypoint_ipv6(self):
        """Gets the slave_entrypoint_ipv6 of this EntrypointItem.

        微服务引擎专享版组件的ipv6备接入地址

        :return: The slave_entrypoint_ipv6 of this EntrypointItem.
        :rtype: str
        """
        return self._slave_entrypoint_ipv6

    @slave_entrypoint_ipv6.setter
    def slave_entrypoint_ipv6(self, slave_entrypoint_ipv6):
        """Sets the slave_entrypoint_ipv6 of this EntrypointItem.

        微服务引擎专享版组件的ipv6备接入地址

        :param slave_entrypoint_ipv6: The slave_entrypoint_ipv6 of this EntrypointItem.
        :type slave_entrypoint_ipv6: str
        """
        self._slave_entrypoint_ipv6 = slave_entrypoint_ipv6

    @property
    def type(self):
        """Gets the type of this EntrypointItem.

        微服务引擎专享版组件类型

        :return: The type of this EntrypointItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntrypointItem.

        微服务引擎专享版组件类型

        :param type: The type of this EntrypointItem.
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
        if not isinstance(other, EntrypointItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

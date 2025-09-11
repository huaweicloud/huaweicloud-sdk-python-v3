# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutsideInsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_node_ip': 'str',
        'slave_node_ip': 'str',
        'virtual_ip': 'str'
    }

    attribute_map = {
        'master_node_ip': 'master_node_ip',
        'slave_node_ip': 'slave_node_ip',
        'virtual_ip': 'virtual_ip'
    }

    def __init__(self, master_node_ip=None, slave_node_ip=None, virtual_ip=None):
        r"""OutsideInsConfig

        The model defined in huaweicloud sdk

        :param master_node_ip: 主节点IP
        :type master_node_ip: str
        :param slave_node_ip: 从节点IP
        :type slave_node_ip: str
        :param virtual_ip: 虚拟IP
        :type virtual_ip: str
        """
        
        

        self._master_node_ip = None
        self._slave_node_ip = None
        self._virtual_ip = None
        self.discriminator = None

        if master_node_ip is not None:
            self.master_node_ip = master_node_ip
        if slave_node_ip is not None:
            self.slave_node_ip = slave_node_ip
        if virtual_ip is not None:
            self.virtual_ip = virtual_ip

    @property
    def master_node_ip(self):
        r"""Gets the master_node_ip of this OutsideInsConfig.

        主节点IP

        :return: The master_node_ip of this OutsideInsConfig.
        :rtype: str
        """
        return self._master_node_ip

    @master_node_ip.setter
    def master_node_ip(self, master_node_ip):
        r"""Sets the master_node_ip of this OutsideInsConfig.

        主节点IP

        :param master_node_ip: The master_node_ip of this OutsideInsConfig.
        :type master_node_ip: str
        """
        self._master_node_ip = master_node_ip

    @property
    def slave_node_ip(self):
        r"""Gets the slave_node_ip of this OutsideInsConfig.

        从节点IP

        :return: The slave_node_ip of this OutsideInsConfig.
        :rtype: str
        """
        return self._slave_node_ip

    @slave_node_ip.setter
    def slave_node_ip(self, slave_node_ip):
        r"""Sets the slave_node_ip of this OutsideInsConfig.

        从节点IP

        :param slave_node_ip: The slave_node_ip of this OutsideInsConfig.
        :type slave_node_ip: str
        """
        self._slave_node_ip = slave_node_ip

    @property
    def virtual_ip(self):
        r"""Gets the virtual_ip of this OutsideInsConfig.

        虚拟IP

        :return: The virtual_ip of this OutsideInsConfig.
        :rtype: str
        """
        return self._virtual_ip

    @virtual_ip.setter
    def virtual_ip(self, virtual_ip):
        r"""Sets the virtual_ip of this OutsideInsConfig.

        虚拟IP

        :param virtual_ip: The virtual_ip of this OutsideInsConfig.
        :type virtual_ip: str
        """
        self._virtual_ip = virtual_ip

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
        if not isinstance(other, OutsideInsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceActivateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dsc_proxy_domain_name': 'str',
        'dsc_proxy_ip': 'str',
        'dsc_proxy_port': 'int',
        'master_node_id': 'str',
        'slave_node_id': 'str'
    }

    attribute_map = {
        'dsc_proxy_domain_name': 'dsc_proxy_domain_name',
        'dsc_proxy_ip': 'dsc_proxy_ip',
        'dsc_proxy_port': 'dsc_proxy_port',
        'master_node_id': 'master_node_id',
        'slave_node_id': 'slave_node_id'
    }

    def __init__(self, dsc_proxy_domain_name=None, dsc_proxy_ip=None, dsc_proxy_port=None, master_node_id=None, slave_node_id=None):
        r"""InstanceActivateInfo

        The model defined in huaweicloud sdk

        :param dsc_proxy_domain_name: 代理DOMAIN名称
        :type dsc_proxy_domain_name: str
        :param dsc_proxy_ip: 代理IP
        :type dsc_proxy_ip: str
        :param dsc_proxy_port: 代理端口
        :type dsc_proxy_port: int
        :param master_node_id: 主节点ID
        :type master_node_id: str
        :param slave_node_id: 备节点ID
        :type slave_node_id: str
        """
        
        

        self._dsc_proxy_domain_name = None
        self._dsc_proxy_ip = None
        self._dsc_proxy_port = None
        self._master_node_id = None
        self._slave_node_id = None
        self.discriminator = None

        if dsc_proxy_domain_name is not None:
            self.dsc_proxy_domain_name = dsc_proxy_domain_name
        if dsc_proxy_ip is not None:
            self.dsc_proxy_ip = dsc_proxy_ip
        if dsc_proxy_port is not None:
            self.dsc_proxy_port = dsc_proxy_port
        if master_node_id is not None:
            self.master_node_id = master_node_id
        if slave_node_id is not None:
            self.slave_node_id = slave_node_id

    @property
    def dsc_proxy_domain_name(self):
        r"""Gets the dsc_proxy_domain_name of this InstanceActivateInfo.

        代理DOMAIN名称

        :return: The dsc_proxy_domain_name of this InstanceActivateInfo.
        :rtype: str
        """
        return self._dsc_proxy_domain_name

    @dsc_proxy_domain_name.setter
    def dsc_proxy_domain_name(self, dsc_proxy_domain_name):
        r"""Sets the dsc_proxy_domain_name of this InstanceActivateInfo.

        代理DOMAIN名称

        :param dsc_proxy_domain_name: The dsc_proxy_domain_name of this InstanceActivateInfo.
        :type dsc_proxy_domain_name: str
        """
        self._dsc_proxy_domain_name = dsc_proxy_domain_name

    @property
    def dsc_proxy_ip(self):
        r"""Gets the dsc_proxy_ip of this InstanceActivateInfo.

        代理IP

        :return: The dsc_proxy_ip of this InstanceActivateInfo.
        :rtype: str
        """
        return self._dsc_proxy_ip

    @dsc_proxy_ip.setter
    def dsc_proxy_ip(self, dsc_proxy_ip):
        r"""Sets the dsc_proxy_ip of this InstanceActivateInfo.

        代理IP

        :param dsc_proxy_ip: The dsc_proxy_ip of this InstanceActivateInfo.
        :type dsc_proxy_ip: str
        """
        self._dsc_proxy_ip = dsc_proxy_ip

    @property
    def dsc_proxy_port(self):
        r"""Gets the dsc_proxy_port of this InstanceActivateInfo.

        代理端口

        :return: The dsc_proxy_port of this InstanceActivateInfo.
        :rtype: int
        """
        return self._dsc_proxy_port

    @dsc_proxy_port.setter
    def dsc_proxy_port(self, dsc_proxy_port):
        r"""Sets the dsc_proxy_port of this InstanceActivateInfo.

        代理端口

        :param dsc_proxy_port: The dsc_proxy_port of this InstanceActivateInfo.
        :type dsc_proxy_port: int
        """
        self._dsc_proxy_port = dsc_proxy_port

    @property
    def master_node_id(self):
        r"""Gets the master_node_id of this InstanceActivateInfo.

        主节点ID

        :return: The master_node_id of this InstanceActivateInfo.
        :rtype: str
        """
        return self._master_node_id

    @master_node_id.setter
    def master_node_id(self, master_node_id):
        r"""Sets the master_node_id of this InstanceActivateInfo.

        主节点ID

        :param master_node_id: The master_node_id of this InstanceActivateInfo.
        :type master_node_id: str
        """
        self._master_node_id = master_node_id

    @property
    def slave_node_id(self):
        r"""Gets the slave_node_id of this InstanceActivateInfo.

        备节点ID

        :return: The slave_node_id of this InstanceActivateInfo.
        :rtype: str
        """
        return self._slave_node_id

    @slave_node_id.setter
    def slave_node_id(self, slave_node_id):
        r"""Sets the slave_node_id of this InstanceActivateInfo.

        备节点ID

        :param slave_node_id: The slave_node_id of this InstanceActivateInfo.
        :type slave_node_id: str
        """
        self._slave_node_id = slave_node_id

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
        if not isinstance(other, InstanceActivateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

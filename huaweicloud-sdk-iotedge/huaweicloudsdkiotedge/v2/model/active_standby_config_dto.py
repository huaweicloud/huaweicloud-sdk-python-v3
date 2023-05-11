# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActiveStandbyConfigDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_node': 'str',
        'master_interface_name': 'str',
        'slave_interface_name': 'str',
        'virtual_ip_address': 'str',
        'virtual_ipv6_address': 'str'
    }

    attribute_map = {
        'work_node': 'work_node',
        'master_interface_name': 'master_interface_name',
        'slave_interface_name': 'slave_interface_name',
        'virtual_ip_address': 'virtual_ip_address',
        'virtual_ipv6_address': 'virtual_ipv6_address'
    }

    def __init__(self, work_node=None, master_interface_name=None, slave_interface_name=None, virtual_ip_address=None, virtual_ipv6_address=None):
        """ActiveStandbyConfigDTO

        The model defined in huaweicloud sdk

        :param work_node: 当前的工作节点，主节点还是备节点在工作，初始创建时工作节点为DEFAULT节点，(DEFAULT|MASTER|SLAVE)
        :type work_node: str
        :param master_interface_name: 主节点网卡名称
        :type master_interface_name: str
        :param slave_interface_name: 备节点网卡名称
        :type slave_interface_name: str
        :param virtual_ip_address: 网卡ip
        :type virtual_ip_address: str
        :param virtual_ipv6_address: 网卡ipv6地址
        :type virtual_ipv6_address: str
        """
        
        

        self._work_node = None
        self._master_interface_name = None
        self._slave_interface_name = None
        self._virtual_ip_address = None
        self._virtual_ipv6_address = None
        self.discriminator = None

        if work_node is not None:
            self.work_node = work_node
        if master_interface_name is not None:
            self.master_interface_name = master_interface_name
        if slave_interface_name is not None:
            self.slave_interface_name = slave_interface_name
        if virtual_ip_address is not None:
            self.virtual_ip_address = virtual_ip_address
        if virtual_ipv6_address is not None:
            self.virtual_ipv6_address = virtual_ipv6_address

    @property
    def work_node(self):
        """Gets the work_node of this ActiveStandbyConfigDTO.

        当前的工作节点，主节点还是备节点在工作，初始创建时工作节点为DEFAULT节点，(DEFAULT|MASTER|SLAVE)

        :return: The work_node of this ActiveStandbyConfigDTO.
        :rtype: str
        """
        return self._work_node

    @work_node.setter
    def work_node(self, work_node):
        """Sets the work_node of this ActiveStandbyConfigDTO.

        当前的工作节点，主节点还是备节点在工作，初始创建时工作节点为DEFAULT节点，(DEFAULT|MASTER|SLAVE)

        :param work_node: The work_node of this ActiveStandbyConfigDTO.
        :type work_node: str
        """
        self._work_node = work_node

    @property
    def master_interface_name(self):
        """Gets the master_interface_name of this ActiveStandbyConfigDTO.

        主节点网卡名称

        :return: The master_interface_name of this ActiveStandbyConfigDTO.
        :rtype: str
        """
        return self._master_interface_name

    @master_interface_name.setter
    def master_interface_name(self, master_interface_name):
        """Sets the master_interface_name of this ActiveStandbyConfigDTO.

        主节点网卡名称

        :param master_interface_name: The master_interface_name of this ActiveStandbyConfigDTO.
        :type master_interface_name: str
        """
        self._master_interface_name = master_interface_name

    @property
    def slave_interface_name(self):
        """Gets the slave_interface_name of this ActiveStandbyConfigDTO.

        备节点网卡名称

        :return: The slave_interface_name of this ActiveStandbyConfigDTO.
        :rtype: str
        """
        return self._slave_interface_name

    @slave_interface_name.setter
    def slave_interface_name(self, slave_interface_name):
        """Sets the slave_interface_name of this ActiveStandbyConfigDTO.

        备节点网卡名称

        :param slave_interface_name: The slave_interface_name of this ActiveStandbyConfigDTO.
        :type slave_interface_name: str
        """
        self._slave_interface_name = slave_interface_name

    @property
    def virtual_ip_address(self):
        """Gets the virtual_ip_address of this ActiveStandbyConfigDTO.

        网卡ip

        :return: The virtual_ip_address of this ActiveStandbyConfigDTO.
        :rtype: str
        """
        return self._virtual_ip_address

    @virtual_ip_address.setter
    def virtual_ip_address(self, virtual_ip_address):
        """Sets the virtual_ip_address of this ActiveStandbyConfigDTO.

        网卡ip

        :param virtual_ip_address: The virtual_ip_address of this ActiveStandbyConfigDTO.
        :type virtual_ip_address: str
        """
        self._virtual_ip_address = virtual_ip_address

    @property
    def virtual_ipv6_address(self):
        """Gets the virtual_ipv6_address of this ActiveStandbyConfigDTO.

        网卡ipv6地址

        :return: The virtual_ipv6_address of this ActiveStandbyConfigDTO.
        :rtype: str
        """
        return self._virtual_ipv6_address

    @virtual_ipv6_address.setter
    def virtual_ipv6_address(self, virtual_ipv6_address):
        """Sets the virtual_ipv6_address of this ActiveStandbyConfigDTO.

        网卡ipv6地址

        :param virtual_ipv6_address: The virtual_ipv6_address of this ActiveStandbyConfigDTO.
        :type virtual_ipv6_address: str
        """
        self._virtual_ipv6_address = virtual_ipv6_address

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
        if not isinstance(other, ActiveStandbyConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

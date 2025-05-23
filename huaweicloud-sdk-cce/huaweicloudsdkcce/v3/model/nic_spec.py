# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NicSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'fixed_ips': 'list[str]',
        'ip_block': 'str',
        'subnet_list': 'list[str]'
    }

    attribute_map = {
        'subnet_id': 'subnetId',
        'fixed_ips': 'fixedIps',
        'ip_block': 'ipBlock',
        'subnet_list': 'subnetList'
    }

    def __init__(self, subnet_id=None, fixed_ips=None, ip_block=None, subnet_list=None):
        r"""NicSpec

        The model defined in huaweicloud sdk

        :param subnet_id: 网卡所在子网的网络ID。主网卡创建时若未指定subnetId,将使用集群子网。若节点池同时配置了subnetList，则节点池扩容子网以subnetList字段为准。扩展网卡创建时必须指定subnetId。  
        :type subnet_id: str
        :param fixed_ips: 主网卡的IP将通过fixedIps指定，数量不得大于创建的节点数。fixedIps或ipBlock同时只能指定一个。扩展网卡不支持指定fiexdIps。
        :type fixed_ips: list[str]
        :param ip_block: 主网卡的IP段的CIDR格式，创建的节点IP将属于该IP段内。fixedIps或ipBlock同时只能指定一个。
        :type ip_block: str
        :param subnet_list: 网卡所在子网的网络ID列表，支持节点池配置多个子网，最多支持配置20个子网。
        :type subnet_list: list[str]
        """
        
        

        self._subnet_id = None
        self._fixed_ips = None
        self._ip_block = None
        self._subnet_list = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        if ip_block is not None:
            self.ip_block = ip_block
        if subnet_list is not None:
            self.subnet_list = subnet_list

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this NicSpec.

        网卡所在子网的网络ID。主网卡创建时若未指定subnetId,将使用集群子网。若节点池同时配置了subnetList，则节点池扩容子网以subnetList字段为准。扩展网卡创建时必须指定subnetId。  

        :return: The subnet_id of this NicSpec.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this NicSpec.

        网卡所在子网的网络ID。主网卡创建时若未指定subnetId,将使用集群子网。若节点池同时配置了subnetList，则节点池扩容子网以subnetList字段为准。扩展网卡创建时必须指定subnetId。  

        :param subnet_id: The subnet_id of this NicSpec.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def fixed_ips(self):
        r"""Gets the fixed_ips of this NicSpec.

        主网卡的IP将通过fixedIps指定，数量不得大于创建的节点数。fixedIps或ipBlock同时只能指定一个。扩展网卡不支持指定fiexdIps。

        :return: The fixed_ips of this NicSpec.
        :rtype: list[str]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        r"""Sets the fixed_ips of this NicSpec.

        主网卡的IP将通过fixedIps指定，数量不得大于创建的节点数。fixedIps或ipBlock同时只能指定一个。扩展网卡不支持指定fiexdIps。

        :param fixed_ips: The fixed_ips of this NicSpec.
        :type fixed_ips: list[str]
        """
        self._fixed_ips = fixed_ips

    @property
    def ip_block(self):
        r"""Gets the ip_block of this NicSpec.

        主网卡的IP段的CIDR格式，创建的节点IP将属于该IP段内。fixedIps或ipBlock同时只能指定一个。

        :return: The ip_block of this NicSpec.
        :rtype: str
        """
        return self._ip_block

    @ip_block.setter
    def ip_block(self, ip_block):
        r"""Sets the ip_block of this NicSpec.

        主网卡的IP段的CIDR格式，创建的节点IP将属于该IP段内。fixedIps或ipBlock同时只能指定一个。

        :param ip_block: The ip_block of this NicSpec.
        :type ip_block: str
        """
        self._ip_block = ip_block

    @property
    def subnet_list(self):
        r"""Gets the subnet_list of this NicSpec.

        网卡所在子网的网络ID列表，支持节点池配置多个子网，最多支持配置20个子网。

        :return: The subnet_list of this NicSpec.
        :rtype: list[str]
        """
        return self._subnet_list

    @subnet_list.setter
    def subnet_list(self, subnet_list):
        r"""Sets the subnet_list of this NicSpec.

        网卡所在子网的网络ID列表，支持节点池配置多个子网，最多支持配置20个子网。

        :param subnet_list: The subnet_list of this NicSpec.
        :type subnet_list: list[str]
        """
        self._subnet_list = subnet_list

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
        if not isinstance(other, NicSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

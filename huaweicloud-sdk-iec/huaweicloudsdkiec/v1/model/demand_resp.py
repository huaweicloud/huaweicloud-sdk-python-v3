# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DemandResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'demand_count': 'int',
        'pool_id_v6': 'str',
        'ipv6_bandwidth_enable': 'bool'
    }

    attribute_map = {
        'demand_count': 'demand_count',
        'pool_id_v6': 'pool_id_v6',
        'ipv6_bandwidth_enable': 'ipv6_bandwidth_enable'
    }

    def __init__(self, demand_count=None, pool_id_v6=None, ipv6_bandwidth_enable=None):
        r"""DemandResp

        The model defined in huaweicloud sdk

        :param demand_count: 站点需要发放的资源(组)总数。  &gt; 实际发放实例数量为count*demand_count。
        :type demand_count: int
        :param pool_id_v6: 指定IPv6线路，使用该线路下的子网分配IPv6端口。 如果该线路下没有关联启用IPv6的子网，则创建新的子网。
        :type pool_id_v6: str
        :param ipv6_bandwidth_enable: 使用IPv6带宽。 边缘实例是否开启IPv6公网访问能力。如果该IPv6线路下没有带宽，则创建新的带宽。  
        :type ipv6_bandwidth_enable: bool
        """
        
        

        self._demand_count = None
        self._pool_id_v6 = None
        self._ipv6_bandwidth_enable = None
        self.discriminator = None

        self.demand_count = demand_count
        if pool_id_v6 is not None:
            self.pool_id_v6 = pool_id_v6
        if ipv6_bandwidth_enable is not None:
            self.ipv6_bandwidth_enable = ipv6_bandwidth_enable

    @property
    def demand_count(self):
        r"""Gets the demand_count of this DemandResp.

        站点需要发放的资源(组)总数。  > 实际发放实例数量为count*demand_count。

        :return: The demand_count of this DemandResp.
        :rtype: int
        """
        return self._demand_count

    @demand_count.setter
    def demand_count(self, demand_count):
        r"""Sets the demand_count of this DemandResp.

        站点需要发放的资源(组)总数。  > 实际发放实例数量为count*demand_count。

        :param demand_count: The demand_count of this DemandResp.
        :type demand_count: int
        """
        self._demand_count = demand_count

    @property
    def pool_id_v6(self):
        r"""Gets the pool_id_v6 of this DemandResp.

        指定IPv6线路，使用该线路下的子网分配IPv6端口。 如果该线路下没有关联启用IPv6的子网，则创建新的子网。

        :return: The pool_id_v6 of this DemandResp.
        :rtype: str
        """
        return self._pool_id_v6

    @pool_id_v6.setter
    def pool_id_v6(self, pool_id_v6):
        r"""Sets the pool_id_v6 of this DemandResp.

        指定IPv6线路，使用该线路下的子网分配IPv6端口。 如果该线路下没有关联启用IPv6的子网，则创建新的子网。

        :param pool_id_v6: The pool_id_v6 of this DemandResp.
        :type pool_id_v6: str
        """
        self._pool_id_v6 = pool_id_v6

    @property
    def ipv6_bandwidth_enable(self):
        r"""Gets the ipv6_bandwidth_enable of this DemandResp.

        使用IPv6带宽。 边缘实例是否开启IPv6公网访问能力。如果该IPv6线路下没有带宽，则创建新的带宽。  

        :return: The ipv6_bandwidth_enable of this DemandResp.
        :rtype: bool
        """
        return self._ipv6_bandwidth_enable

    @ipv6_bandwidth_enable.setter
    def ipv6_bandwidth_enable(self, ipv6_bandwidth_enable):
        r"""Sets the ipv6_bandwidth_enable of this DemandResp.

        使用IPv6带宽。 边缘实例是否开启IPv6公网访问能力。如果该IPv6线路下没有带宽，则创建新的带宽。  

        :param ipv6_bandwidth_enable: The ipv6_bandwidth_enable of this DemandResp.
        :type ipv6_bandwidth_enable: bool
        """
        self._ipv6_bandwidth_enable = ipv6_bandwidth_enable

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
        if not isinstance(other, DemandResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

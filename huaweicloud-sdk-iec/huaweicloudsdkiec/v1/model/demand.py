# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Demand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operator': 'str',
        'demand_count': 'int',
        'pool_id': 'str',
        'bandwidth_type': 'str',
        'pool_id_v6': 'str',
        'ipv6_bandwidth_enable': 'bool',
        'ipv6_bandwidth_type': 'str'
    }

    attribute_map = {
        'operator': 'operator',
        'demand_count': 'demand_count',
        'pool_id': 'pool_id',
        'bandwidth_type': 'bandwidth_type',
        'pool_id_v6': 'pool_id_v6',
        'ipv6_bandwidth_enable': 'ipv6_bandwidth_enable',
        'ipv6_bandwidth_type': 'ipv6_bandwidth_type'
    }

    def __init__(self, operator=None, demand_count=None, pool_id=None, bandwidth_type=None, pool_id_v6=None, ipv6_bandwidth_enable=None, ipv6_bandwidth_type=None):
        r"""Demand

        The model defined in huaweicloud sdk

        :param operator: 所属运营商。
        :type operator: str
        :param demand_count: 站点需要发放的资源(组)总数。  &gt; 实际发放实例数量为count*demand_count。
        :type demand_count: int
        :param pool_id: 线路ID。 多线路场景下，将在该线路下创建弹性公网IP。 &gt; 覆盖规则为省级/大区时不支持指定线路ID创建边缘业务。
        :type pool_id: str
        :param bandwidth_type: 带宽类型。 如果当前带宽类型下没有带宽，自动在该带宽类型下创建带宽
        :type bandwidth_type: str
        :param pool_id_v6: 指定IPv6线路，使用该线路下的子网分配IPv6端口。 如果该线路下没有关联启用IPv6的子网，则创建新的子网。
        :type pool_id_v6: str
        :param ipv6_bandwidth_enable: 使用IPv6带宽。 边缘实例是否开启IPv6公网访问能力。如果该IPv6线路没有可用的带宽，则创建新的带宽。
        :type ipv6_bandwidth_enable: bool
        :param ipv6_bandwidth_type: 带宽类型。  边缘实例开启IPv6访问公网能力后，如果当前带宽类型下没有带宽，自动在该带宽类型下创建带宽    
        :type ipv6_bandwidth_type: str
        """
        
        

        self._operator = None
        self._demand_count = None
        self._pool_id = None
        self._bandwidth_type = None
        self._pool_id_v6 = None
        self._ipv6_bandwidth_enable = None
        self._ipv6_bandwidth_type = None
        self.discriminator = None

        if operator is not None:
            self.operator = operator
        self.demand_count = demand_count
        if pool_id is not None:
            self.pool_id = pool_id
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if pool_id_v6 is not None:
            self.pool_id_v6 = pool_id_v6
        if ipv6_bandwidth_enable is not None:
            self.ipv6_bandwidth_enable = ipv6_bandwidth_enable
        if ipv6_bandwidth_type is not None:
            self.ipv6_bandwidth_type = ipv6_bandwidth_type

    @property
    def operator(self):
        r"""Gets the operator of this Demand.

        所属运营商。

        :return: The operator of this Demand.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this Demand.

        所属运营商。

        :param operator: The operator of this Demand.
        :type operator: str
        """
        self._operator = operator

    @property
    def demand_count(self):
        r"""Gets the demand_count of this Demand.

        站点需要发放的资源(组)总数。  > 实际发放实例数量为count*demand_count。

        :return: The demand_count of this Demand.
        :rtype: int
        """
        return self._demand_count

    @demand_count.setter
    def demand_count(self, demand_count):
        r"""Sets the demand_count of this Demand.

        站点需要发放的资源(组)总数。  > 实际发放实例数量为count*demand_count。

        :param demand_count: The demand_count of this Demand.
        :type demand_count: int
        """
        self._demand_count = demand_count

    @property
    def pool_id(self):
        r"""Gets the pool_id of this Demand.

        线路ID。 多线路场景下，将在该线路下创建弹性公网IP。 > 覆盖规则为省级/大区时不支持指定线路ID创建边缘业务。

        :return: The pool_id of this Demand.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this Demand.

        线路ID。 多线路场景下，将在该线路下创建弹性公网IP。 > 覆盖规则为省级/大区时不支持指定线路ID创建边缘业务。

        :param pool_id: The pool_id of this Demand.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def bandwidth_type(self):
        r"""Gets the bandwidth_type of this Demand.

        带宽类型。 如果当前带宽类型下没有带宽，自动在该带宽类型下创建带宽

        :return: The bandwidth_type of this Demand.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        r"""Sets the bandwidth_type of this Demand.

        带宽类型。 如果当前带宽类型下没有带宽，自动在该带宽类型下创建带宽

        :param bandwidth_type: The bandwidth_type of this Demand.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def pool_id_v6(self):
        r"""Gets the pool_id_v6 of this Demand.

        指定IPv6线路，使用该线路下的子网分配IPv6端口。 如果该线路下没有关联启用IPv6的子网，则创建新的子网。

        :return: The pool_id_v6 of this Demand.
        :rtype: str
        """
        return self._pool_id_v6

    @pool_id_v6.setter
    def pool_id_v6(self, pool_id_v6):
        r"""Sets the pool_id_v6 of this Demand.

        指定IPv6线路，使用该线路下的子网分配IPv6端口。 如果该线路下没有关联启用IPv6的子网，则创建新的子网。

        :param pool_id_v6: The pool_id_v6 of this Demand.
        :type pool_id_v6: str
        """
        self._pool_id_v6 = pool_id_v6

    @property
    def ipv6_bandwidth_enable(self):
        r"""Gets the ipv6_bandwidth_enable of this Demand.

        使用IPv6带宽。 边缘实例是否开启IPv6公网访问能力。如果该IPv6线路没有可用的带宽，则创建新的带宽。

        :return: The ipv6_bandwidth_enable of this Demand.
        :rtype: bool
        """
        return self._ipv6_bandwidth_enable

    @ipv6_bandwidth_enable.setter
    def ipv6_bandwidth_enable(self, ipv6_bandwidth_enable):
        r"""Sets the ipv6_bandwidth_enable of this Demand.

        使用IPv6带宽。 边缘实例是否开启IPv6公网访问能力。如果该IPv6线路没有可用的带宽，则创建新的带宽。

        :param ipv6_bandwidth_enable: The ipv6_bandwidth_enable of this Demand.
        :type ipv6_bandwidth_enable: bool
        """
        self._ipv6_bandwidth_enable = ipv6_bandwidth_enable

    @property
    def ipv6_bandwidth_type(self):
        r"""Gets the ipv6_bandwidth_type of this Demand.

        带宽类型。  边缘实例开启IPv6访问公网能力后，如果当前带宽类型下没有带宽，自动在该带宽类型下创建带宽    

        :return: The ipv6_bandwidth_type of this Demand.
        :rtype: str
        """
        return self._ipv6_bandwidth_type

    @ipv6_bandwidth_type.setter
    def ipv6_bandwidth_type(self, ipv6_bandwidth_type):
        r"""Sets the ipv6_bandwidth_type of this Demand.

        带宽类型。  边缘实例开启IPv6访问公网能力后，如果当前带宽类型下没有带宽，自动在该带宽类型下创建带宽    

        :param ipv6_bandwidth_type: The ipv6_bandwidth_type of this Demand.
        :type ipv6_bandwidth_type: str
        """
        self._ipv6_bandwidth_type = ipv6_bandwidth_type

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
        if not isinstance(other, Demand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

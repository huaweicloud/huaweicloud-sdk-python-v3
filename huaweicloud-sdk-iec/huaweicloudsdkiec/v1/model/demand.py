# coding: utf-8

import re
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
        'pool_id': 'str'
    }

    attribute_map = {
        'operator': 'operator',
        'demand_count': 'demand_count',
        'pool_id': 'pool_id'
    }

    def __init__(self, operator=None, demand_count=None, pool_id=None):
        """Demand

        The model defined in huaweicloud sdk

        :param operator: 所属运营商。
        :type operator: str
        :param demand_count: 站点需要发放的资源(组)总数。  &gt; 实际发放实例数量为count*demand_count。
        :type demand_count: int
        :param pool_id: 线路ID。 多线路场景下，将在该线路下创建弹性公网IP。 &gt; 覆盖规则为省级/大区时不支持指定线路ID创建边缘业务。
        :type pool_id: str
        """
        
        

        self._operator = None
        self._demand_count = None
        self._pool_id = None
        self.discriminator = None

        if operator is not None:
            self.operator = operator
        self.demand_count = demand_count
        if pool_id is not None:
            self.pool_id = pool_id

    @property
    def operator(self):
        """Gets the operator of this Demand.

        所属运营商。

        :return: The operator of this Demand.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Demand.

        所属运营商。

        :param operator: The operator of this Demand.
        :type operator: str
        """
        self._operator = operator

    @property
    def demand_count(self):
        """Gets the demand_count of this Demand.

        站点需要发放的资源(组)总数。  > 实际发放实例数量为count*demand_count。

        :return: The demand_count of this Demand.
        :rtype: int
        """
        return self._demand_count

    @demand_count.setter
    def demand_count(self, demand_count):
        """Sets the demand_count of this Demand.

        站点需要发放的资源(组)总数。  > 实际发放实例数量为count*demand_count。

        :param demand_count: The demand_count of this Demand.
        :type demand_count: int
        """
        self._demand_count = demand_count

    @property
    def pool_id(self):
        """Gets the pool_id of this Demand.

        线路ID。 多线路场景下，将在该线路下创建弹性公网IP。 > 覆盖规则为省级/大区时不支持指定线路ID创建边缘业务。

        :return: The pool_id of this Demand.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this Demand.

        线路ID。 多线路场景下，将在该线路下创建弹性公网IP。 > 覆盖规则为省级/大区时不支持指定线路ID创建边缘业务。

        :param pool_id: The pool_id of this Demand.
        :type pool_id: str
        """
        self._pool_id = pool_id

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

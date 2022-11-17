# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowUsageVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'billing_cycle': 'str',
        'flow_used': 'float'
    }

    attribute_map = {
        'billing_cycle': 'billing_cycle',
        'flow_used': 'flow_used'
    }

    def __init__(self, billing_cycle=None, flow_used=None):
        """FlowUsageVo

        The model defined in huaweicloud sdk

        :param billing_cycle: 账期
        :type billing_cycle: str
        :param flow_used: 已用流量
        :type flow_used: float
        """
        
        

        self._billing_cycle = None
        self._flow_used = None
        self.discriminator = None

        if billing_cycle is not None:
            self.billing_cycle = billing_cycle
        if flow_used is not None:
            self.flow_used = flow_used

    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this FlowUsageVo.

        账期

        :return: The billing_cycle of this FlowUsageVo.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this FlowUsageVo.

        账期

        :param billing_cycle: The billing_cycle of this FlowUsageVo.
        :type billing_cycle: str
        """
        self._billing_cycle = billing_cycle

    @property
    def flow_used(self):
        """Gets the flow_used of this FlowUsageVo.

        已用流量

        :return: The flow_used of this FlowUsageVo.
        :rtype: float
        """
        return self._flow_used

    @flow_used.setter
    def flow_used(self, flow_used):
        """Sets the flow_used of this FlowUsageVo.

        已用流量

        :param flow_used: The flow_used of this FlowUsageVo.
        :type flow_used: float
        """
        self._flow_used = flow_used

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
        if not isinstance(other, FlowUsageVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoadbalancerAutoscalingOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'min_l7_flavor_id': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'min_l7_flavor_id': 'min_l7_flavor_id'
    }

    def __init__(self, enable=None, min_l7_flavor_id=None):
        """CreateLoadbalancerAutoscalingOption

        The model defined in huaweicloud sdk

        :param enable: 负载均衡器弹性扩缩容开关
        :type enable: bool
        :param min_l7_flavor_id: 弹性扩缩容的最小七层规格ID，类型为L7_Elastic，有七层监听器时，该字段不能为空。
        :type min_l7_flavor_id: str
        """
        
        

        self._enable = None
        self._min_l7_flavor_id = None
        self.discriminator = None

        self.enable = enable
        if min_l7_flavor_id is not None:
            self.min_l7_flavor_id = min_l7_flavor_id

    @property
    def enable(self):
        """Gets the enable of this CreateLoadbalancerAutoscalingOption.

        负载均衡器弹性扩缩容开关

        :return: The enable of this CreateLoadbalancerAutoscalingOption.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateLoadbalancerAutoscalingOption.

        负载均衡器弹性扩缩容开关

        :param enable: The enable of this CreateLoadbalancerAutoscalingOption.
        :type enable: bool
        """
        self._enable = enable

    @property
    def min_l7_flavor_id(self):
        """Gets the min_l7_flavor_id of this CreateLoadbalancerAutoscalingOption.

        弹性扩缩容的最小七层规格ID，类型为L7_Elastic，有七层监听器时，该字段不能为空。

        :return: The min_l7_flavor_id of this CreateLoadbalancerAutoscalingOption.
        :rtype: str
        """
        return self._min_l7_flavor_id

    @min_l7_flavor_id.setter
    def min_l7_flavor_id(self, min_l7_flavor_id):
        """Sets the min_l7_flavor_id of this CreateLoadbalancerAutoscalingOption.

        弹性扩缩容的最小七层规格ID，类型为L7_Elastic，有七层监听器时，该字段不能为空。

        :param min_l7_flavor_id: The min_l7_flavor_id of this CreateLoadbalancerAutoscalingOption.
        :type min_l7_flavor_id: str
        """
        self._min_l7_flavor_id = min_l7_flavor_id

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
        if not isinstance(other, CreateLoadbalancerAutoscalingOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

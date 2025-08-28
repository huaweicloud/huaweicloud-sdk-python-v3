# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrafficLimitConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'qps': 'int',
        'per_source_ip_qps': 'int',
        'burst': 'int'
    }

    attribute_map = {
        'qps': 'qps',
        'per_source_ip_qps': 'per_source_ip_qps',
        'burst': 'burst'
    }

    def __init__(self, qps=None, per_source_ip_qps=None, burst=None):
        r"""TrafficLimitConfig

        The model defined in huaweicloud sdk

        :param qps: **参数解释**：转发策略qps限速。  **取值范围**：0-100000，单位：个/秒。0表示不限速。
        :type qps: int
        :param per_source_ip_qps: **参数解释**：对转发策略单源(单个客户端IP)进行限速。  **取值范围**：0-100000，单位：个/秒。0表示不限速。
        :type per_source_ip_qps: int
        :param burst: **参数解释**：设置当单源qps超限时，允许的局部突增请求数量。超出该限制的请求将返回503。  **取值范围**：0-100000，单位：个/秒。
        :type burst: int
        """
        
        

        self._qps = None
        self._per_source_ip_qps = None
        self._burst = None
        self.discriminator = None

        if qps is not None:
            self.qps = qps
        if per_source_ip_qps is not None:
            self.per_source_ip_qps = per_source_ip_qps
        if burst is not None:
            self.burst = burst

    @property
    def qps(self):
        r"""Gets the qps of this TrafficLimitConfig.

        **参数解释**：转发策略qps限速。  **取值范围**：0-100000，单位：个/秒。0表示不限速。

        :return: The qps of this TrafficLimitConfig.
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        r"""Sets the qps of this TrafficLimitConfig.

        **参数解释**：转发策略qps限速。  **取值范围**：0-100000，单位：个/秒。0表示不限速。

        :param qps: The qps of this TrafficLimitConfig.
        :type qps: int
        """
        self._qps = qps

    @property
    def per_source_ip_qps(self):
        r"""Gets the per_source_ip_qps of this TrafficLimitConfig.

        **参数解释**：对转发策略单源(单个客户端IP)进行限速。  **取值范围**：0-100000，单位：个/秒。0表示不限速。

        :return: The per_source_ip_qps of this TrafficLimitConfig.
        :rtype: int
        """
        return self._per_source_ip_qps

    @per_source_ip_qps.setter
    def per_source_ip_qps(self, per_source_ip_qps):
        r"""Sets the per_source_ip_qps of this TrafficLimitConfig.

        **参数解释**：对转发策略单源(单个客户端IP)进行限速。  **取值范围**：0-100000，单位：个/秒。0表示不限速。

        :param per_source_ip_qps: The per_source_ip_qps of this TrafficLimitConfig.
        :type per_source_ip_qps: int
        """
        self._per_source_ip_qps = per_source_ip_qps

    @property
    def burst(self):
        r"""Gets the burst of this TrafficLimitConfig.

        **参数解释**：设置当单源qps超限时，允许的局部突增请求数量。超出该限制的请求将返回503。  **取值范围**：0-100000，单位：个/秒。

        :return: The burst of this TrafficLimitConfig.
        :rtype: int
        """
        return self._burst

    @burst.setter
    def burst(self, burst):
        r"""Sets the burst of this TrafficLimitConfig.

        **参数解释**：设置当单源qps超限时，允许的局部突增请求数量。超出该限制的请求将返回503。  **取值范围**：0-100000，单位：个/秒。

        :param burst: The burst of this TrafficLimitConfig.
        :type burst: int
        """
        self._burst = burst

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
        if not isinstance(other, TrafficLimitConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

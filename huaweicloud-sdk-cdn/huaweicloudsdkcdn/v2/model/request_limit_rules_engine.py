# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequestLimitRulesEngine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit_rate_after': 'int',
        'limit_rate_value': 'int'
    }

    attribute_map = {
        'limit_rate_after': 'limit_rate_after',
        'limit_rate_value': 'limit_rate_value'
    }

    def __init__(self, limit_rate_after=None, limit_rate_value=None):
        r"""RequestLimitRulesEngine

        The model defined in huaweicloud sdk

        :param limit_rate_after: **参数解释：** 限速条件 &gt; 例如：type&#x3D;size，limit_rate_after&#x3D;50表示从传输50个字节后开始限速且限速值为limit_rate_value  **约束限制：** 不涉及 **取值范围：** 0-1073741824，单位：byte **默认取值：** 不涉及
        :type limit_rate_after: int
        :param limit_rate_value: **参数解释：** 限速值，即达到限速条件后的最大访问速度 **约束限制：** 不涉及 **取值范围：** 0-104857600，单位：Bps **默认取值：** 不涉及
        :type limit_rate_value: int
        """
        
        

        self._limit_rate_after = None
        self._limit_rate_value = None
        self.discriminator = None

        self.limit_rate_after = limit_rate_after
        self.limit_rate_value = limit_rate_value

    @property
    def limit_rate_after(self):
        r"""Gets the limit_rate_after of this RequestLimitRulesEngine.

        **参数解释：** 限速条件 > 例如：type=size，limit_rate_after=50表示从传输50个字节后开始限速且限速值为limit_rate_value  **约束限制：** 不涉及 **取值范围：** 0-1073741824，单位：byte **默认取值：** 不涉及

        :return: The limit_rate_after of this RequestLimitRulesEngine.
        :rtype: int
        """
        return self._limit_rate_after

    @limit_rate_after.setter
    def limit_rate_after(self, limit_rate_after):
        r"""Sets the limit_rate_after of this RequestLimitRulesEngine.

        **参数解释：** 限速条件 > 例如：type=size，limit_rate_after=50表示从传输50个字节后开始限速且限速值为limit_rate_value  **约束限制：** 不涉及 **取值范围：** 0-1073741824，单位：byte **默认取值：** 不涉及

        :param limit_rate_after: The limit_rate_after of this RequestLimitRulesEngine.
        :type limit_rate_after: int
        """
        self._limit_rate_after = limit_rate_after

    @property
    def limit_rate_value(self):
        r"""Gets the limit_rate_value of this RequestLimitRulesEngine.

        **参数解释：** 限速值，即达到限速条件后的最大访问速度 **约束限制：** 不涉及 **取值范围：** 0-104857600，单位：Bps **默认取值：** 不涉及

        :return: The limit_rate_value of this RequestLimitRulesEngine.
        :rtype: int
        """
        return self._limit_rate_value

    @limit_rate_value.setter
    def limit_rate_value(self, limit_rate_value):
        r"""Sets the limit_rate_value of this RequestLimitRulesEngine.

        **参数解释：** 限速值，即达到限速条件后的最大访问速度 **约束限制：** 不涉及 **取值范围：** 0-104857600，单位：Bps **默认取值：** 不涉及

        :param limit_rate_value: The limit_rate_value of this RequestLimitRulesEngine.
        :type limit_rate_value: int
        """
        self._limit_rate_value = limit_rate_value

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
        if not isinstance(other, RequestLimitRulesEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

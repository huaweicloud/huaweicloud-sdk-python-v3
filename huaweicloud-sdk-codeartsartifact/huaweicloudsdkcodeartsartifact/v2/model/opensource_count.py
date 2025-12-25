# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpensourceCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'critical': 'int',
        'high': 'int',
        'medium': 'int',
        'low': 'int'
    }

    attribute_map = {
        'critical': 'critical',
        'high': 'high',
        'medium': 'medium',
        'low': 'low'
    }

    def __init__(self, critical=None, high=None, medium=None, low=None):
        r"""OpensourceCount

        The model defined in huaweicloud sdk

        :param critical: **参数解释**: 危急漏洞数。 **取值范围**: 不涉及。
        :type critical: int
        :param high: **参数解释**: 高危漏洞数。 **取值范围**: 不涉及。
        :type high: int
        :param medium: **参数解释**: 中危漏洞数。 **取值范围**: 不涉及。
        :type medium: int
        :param low: **参数解释**: 低危漏洞数。 **取值范围**: 不涉及。
        :type low: int
        """
        
        

        self._critical = None
        self._high = None
        self._medium = None
        self._low = None
        self.discriminator = None

        if critical is not None:
            self.critical = critical
        if high is not None:
            self.high = high
        if medium is not None:
            self.medium = medium
        if low is not None:
            self.low = low

    @property
    def critical(self):
        r"""Gets the critical of this OpensourceCount.

        **参数解释**: 危急漏洞数。 **取值范围**: 不涉及。

        :return: The critical of this OpensourceCount.
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        r"""Sets the critical of this OpensourceCount.

        **参数解释**: 危急漏洞数。 **取值范围**: 不涉及。

        :param critical: The critical of this OpensourceCount.
        :type critical: int
        """
        self._critical = critical

    @property
    def high(self):
        r"""Gets the high of this OpensourceCount.

        **参数解释**: 高危漏洞数。 **取值范围**: 不涉及。

        :return: The high of this OpensourceCount.
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        r"""Sets the high of this OpensourceCount.

        **参数解释**: 高危漏洞数。 **取值范围**: 不涉及。

        :param high: The high of this OpensourceCount.
        :type high: int
        """
        self._high = high

    @property
    def medium(self):
        r"""Gets the medium of this OpensourceCount.

        **参数解释**: 中危漏洞数。 **取值范围**: 不涉及。

        :return: The medium of this OpensourceCount.
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        r"""Sets the medium of this OpensourceCount.

        **参数解释**: 中危漏洞数。 **取值范围**: 不涉及。

        :param medium: The medium of this OpensourceCount.
        :type medium: int
        """
        self._medium = medium

    @property
    def low(self):
        r"""Gets the low of this OpensourceCount.

        **参数解释**: 低危漏洞数。 **取值范围**: 不涉及。

        :return: The low of this OpensourceCount.
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        r"""Sets the low of this OpensourceCount.

        **参数解释**: 低危漏洞数。 **取值范围**: 不涉及。

        :param low: The low of this OpensourceCount.
        :type low: int
        """
        self._low = low

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OpensourceCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

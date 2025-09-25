# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBotMRuleDefenseStrategyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'low': 'BotMDefenseLevel',
        'medium': 'BotMDefenseLevel',
        'high': 'BotMDefenseLevel'
    }

    attribute_map = {
        'low': 'low',
        'medium': 'medium',
        'high': 'high'
    }

    def __init__(self, low=None, medium=None, high=None):
        r"""UpdateBotMRuleDefenseStrategyRequestBody

        The model defined in huaweicloud sdk

        :param low: 
        :type low: :class:`huaweicloudsdkwaf.v1.BotMDefenseLevel`
        :param medium: 
        :type medium: :class:`huaweicloudsdkwaf.v1.BotMDefenseLevel`
        :param high: 
        :type high: :class:`huaweicloudsdkwaf.v1.BotMDefenseLevel`
        """
        
        

        self._low = None
        self._medium = None
        self._high = None
        self.discriminator = None

        if low is not None:
            self.low = low
        if medium is not None:
            self.medium = medium
        if high is not None:
            self.high = high

    @property
    def low(self):
        r"""Gets the low of this UpdateBotMRuleDefenseStrategyRequestBody.

        :return: The low of this UpdateBotMRuleDefenseStrategyRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.BotMDefenseLevel`
        """
        return self._low

    @low.setter
    def low(self, low):
        r"""Sets the low of this UpdateBotMRuleDefenseStrategyRequestBody.

        :param low: The low of this UpdateBotMRuleDefenseStrategyRequestBody.
        :type low: :class:`huaweicloudsdkwaf.v1.BotMDefenseLevel`
        """
        self._low = low

    @property
    def medium(self):
        r"""Gets the medium of this UpdateBotMRuleDefenseStrategyRequestBody.

        :return: The medium of this UpdateBotMRuleDefenseStrategyRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.BotMDefenseLevel`
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        r"""Sets the medium of this UpdateBotMRuleDefenseStrategyRequestBody.

        :param medium: The medium of this UpdateBotMRuleDefenseStrategyRequestBody.
        :type medium: :class:`huaweicloudsdkwaf.v1.BotMDefenseLevel`
        """
        self._medium = medium

    @property
    def high(self):
        r"""Gets the high of this UpdateBotMRuleDefenseStrategyRequestBody.

        :return: The high of this UpdateBotMRuleDefenseStrategyRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.BotMDefenseLevel`
        """
        return self._high

    @high.setter
    def high(self, high):
        r"""Sets the high of this UpdateBotMRuleDefenseStrategyRequestBody.

        :param high: The high of this UpdateBotMRuleDefenseStrategyRequestBody.
        :type high: :class:`huaweicloudsdkwaf.v1.BotMDefenseLevel`
        """
        self._high = high

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
        if not isinstance(other, UpdateBotMRuleDefenseStrategyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

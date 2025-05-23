# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecyclePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'retention_period_in_days': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'retention_period_in_days': 'retention_period_in_days'
    }

    def __init__(self, enabled=None, retention_period_in_days=None):
        r"""RecyclePolicy

        The model defined in huaweicloud sdk

        :param enabled: 打开回收策略，不可关闭 - true 打开回收策略
        :type enabled: bool
        :param retention_period_in_days: 策略保持时长（1-7天），天数为正整数，不填默认保留7天
        :type retention_period_in_days: int
        """
        
        

        self._enabled = None
        self._retention_period_in_days = None
        self.discriminator = None

        self.enabled = enabled
        if retention_period_in_days is not None:
            self.retention_period_in_days = retention_period_in_days

    @property
    def enabled(self):
        r"""Gets the enabled of this RecyclePolicy.

        打开回收策略，不可关闭 - true 打开回收策略

        :return: The enabled of this RecyclePolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this RecyclePolicy.

        打开回收策略，不可关闭 - true 打开回收策略

        :param enabled: The enabled of this RecyclePolicy.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def retention_period_in_days(self):
        r"""Gets the retention_period_in_days of this RecyclePolicy.

        策略保持时长（1-7天），天数为正整数，不填默认保留7天

        :return: The retention_period_in_days of this RecyclePolicy.
        :rtype: int
        """
        return self._retention_period_in_days

    @retention_period_in_days.setter
    def retention_period_in_days(self, retention_period_in_days):
        r"""Sets the retention_period_in_days of this RecyclePolicy.

        策略保持时长（1-7天），天数为正整数，不填默认保留7天

        :param retention_period_in_days: The retention_period_in_days of this RecyclePolicy.
        :type retention_period_in_days: int
        """
        self._retention_period_in_days = retention_period_in_days

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
        if not isinstance(other, RecyclePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

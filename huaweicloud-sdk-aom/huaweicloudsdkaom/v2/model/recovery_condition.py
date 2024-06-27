# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecoveryCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recovery_timeframe': 'int'
    }

    attribute_map = {
        'recovery_timeframe': 'recovery_timeframe'
    }

    def __init__(self, recovery_timeframe=None):
        """RecoveryCondition

        The model defined in huaweicloud sdk

        :param recovery_timeframe: 告警恢复周期的个数。
        :type recovery_timeframe: int
        """
        
        

        self._recovery_timeframe = None
        self.discriminator = None

        if recovery_timeframe is not None:
            self.recovery_timeframe = recovery_timeframe

    @property
    def recovery_timeframe(self):
        """Gets the recovery_timeframe of this RecoveryCondition.

        告警恢复周期的个数。

        :return: The recovery_timeframe of this RecoveryCondition.
        :rtype: int
        """
        return self._recovery_timeframe

    @recovery_timeframe.setter
    def recovery_timeframe(self, recovery_timeframe):
        """Sets the recovery_timeframe of this RecoveryCondition.

        告警恢复周期的个数。

        :param recovery_timeframe: The recovery_timeframe of this RecoveryCondition.
        :type recovery_timeframe: int
        """
        self._recovery_timeframe = recovery_timeframe

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
        if not isinstance(other, RecoveryCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import re
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
        'retention_period_in_days': 'int'
    }

    attribute_map = {
        'retention_period_in_days': 'retention_period_in_days'
    }

    def __init__(self, retention_period_in_days=None):
        """RecyclePolicy

        The model defined in huaweicloud sdk

        :param retention_period_in_days: 已删除实例保留天数，可设置范围为1~7天。 - 取值1~7，设置已删除实例的保留天数为该值。
        :type retention_period_in_days: int
        """
        
        

        self._retention_period_in_days = None
        self.discriminator = None

        self.retention_period_in_days = retention_period_in_days

    @property
    def retention_period_in_days(self):
        """Gets the retention_period_in_days of this RecyclePolicy.

        已删除实例保留天数，可设置范围为1~7天。 - 取值1~7，设置已删除实例的保留天数为该值。

        :return: The retention_period_in_days of this RecyclePolicy.
        :rtype: int
        """
        return self._retention_period_in_days

    @retention_period_in_days.setter
    def retention_period_in_days(self, retention_period_in_days):
        """Sets the retention_period_in_days of this RecyclePolicy.

        已删除实例保留天数，可设置范围为1~7天。 - 取值1~7，设置已删除实例的保留天数为该值。

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

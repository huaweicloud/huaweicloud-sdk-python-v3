# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleTaskPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enforcement_enable': 'bool'
    }

    attribute_map = {
        'enforcement_enable': 'enforcement_enable'
    }

    def __init__(self, enforcement_enable=None):
        r"""ScheduleTaskPolicy

        The model defined in huaweicloud sdk

        :param enforcement_enable: 当存在会话的时候，是否强制执行，强制执行开关。取值为： * false：表示关闭。 * true：表示开启。
        :type enforcement_enable: bool
        """
        
        

        self._enforcement_enable = None
        self.discriminator = None

        if enforcement_enable is not None:
            self.enforcement_enable = enforcement_enable

    @property
    def enforcement_enable(self):
        r"""Gets the enforcement_enable of this ScheduleTaskPolicy.

        当存在会话的时候，是否强制执行，强制执行开关。取值为： * false：表示关闭。 * true：表示开启。

        :return: The enforcement_enable of this ScheduleTaskPolicy.
        :rtype: bool
        """
        return self._enforcement_enable

    @enforcement_enable.setter
    def enforcement_enable(self, enforcement_enable):
        r"""Sets the enforcement_enable of this ScheduleTaskPolicy.

        当存在会话的时候，是否强制执行，强制执行开关。取值为： * false：表示关闭。 * true：表示开启。

        :param enforcement_enable: The enforcement_enable of this ScheduleTaskPolicy.
        :type enforcement_enable: bool
        """
        self._enforcement_enable = enforcement_enable

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
        if not isinstance(other, ScheduleTaskPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

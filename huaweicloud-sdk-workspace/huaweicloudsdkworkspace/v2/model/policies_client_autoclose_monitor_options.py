# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesClientAutocloseMonitorOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'autoclose_monitor_wait_time': 'int'
    }

    attribute_map = {
        'autoclose_monitor_wait_time': 'autoclose_monitor_wait_time'
    }

    def __init__(self, autoclose_monitor_wait_time=None):
        r"""PoliciesClientAutocloseMonitorOptions

        The model defined in huaweicloud sdk

        :param autoclose_monitor_wait_time: 自动关闭显示器等待时间。取值范围为[10-600000]。默认：300。
        :type autoclose_monitor_wait_time: int
        """
        
        

        self._autoclose_monitor_wait_time = None
        self.discriminator = None

        if autoclose_monitor_wait_time is not None:
            self.autoclose_monitor_wait_time = autoclose_monitor_wait_time

    @property
    def autoclose_monitor_wait_time(self):
        r"""Gets the autoclose_monitor_wait_time of this PoliciesClientAutocloseMonitorOptions.

        自动关闭显示器等待时间。取值范围为[10-600000]。默认：300。

        :return: The autoclose_monitor_wait_time of this PoliciesClientAutocloseMonitorOptions.
        :rtype: int
        """
        return self._autoclose_monitor_wait_time

    @autoclose_monitor_wait_time.setter
    def autoclose_monitor_wait_time(self, autoclose_monitor_wait_time):
        r"""Sets the autoclose_monitor_wait_time of this PoliciesClientAutocloseMonitorOptions.

        自动关闭显示器等待时间。取值范围为[10-600000]。默认：300。

        :param autoclose_monitor_wait_time: The autoclose_monitor_wait_time of this PoliciesClientAutocloseMonitorOptions.
        :type autoclose_monitor_wait_time: int
        """
        self._autoclose_monitor_wait_time = autoclose_monitor_wait_time

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
        if not isinstance(other, PoliciesClientAutocloseMonitorOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RateControl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'have_rate_control': 'bool',
        'time_delay': 'int',
        'max': 'int'
    }

    attribute_map = {
        'have_rate_control': 'have_rate_control',
        'time_delay': 'time_delay',
        'max': 'max'
    }

    def __init__(self, have_rate_control=None, time_delay=None, max=None):
        """RateControl

        The model defined in huaweicloud sdk

        :param have_rate_control: 是否分批发布，默认值是false。
        :type have_rate_control: bool
        :param time_delay: 每批间隔。
        :type time_delay: int
        :param max: 每批支持的最大实例数。
        :type max: int
        """
        
        

        self._have_rate_control = None
        self._time_delay = None
        self._max = None
        self.discriminator = None

        if have_rate_control is not None:
            self.have_rate_control = have_rate_control
        if time_delay is not None:
            self.time_delay = time_delay
        if max is not None:
            self.max = max

    @property
    def have_rate_control(self):
        """Gets the have_rate_control of this RateControl.

        是否分批发布，默认值是false。

        :return: The have_rate_control of this RateControl.
        :rtype: bool
        """
        return self._have_rate_control

    @have_rate_control.setter
    def have_rate_control(self, have_rate_control):
        """Sets the have_rate_control of this RateControl.

        是否分批发布，默认值是false。

        :param have_rate_control: The have_rate_control of this RateControl.
        :type have_rate_control: bool
        """
        self._have_rate_control = have_rate_control

    @property
    def time_delay(self):
        """Gets the time_delay of this RateControl.

        每批间隔。

        :return: The time_delay of this RateControl.
        :rtype: int
        """
        return self._time_delay

    @time_delay.setter
    def time_delay(self, time_delay):
        """Sets the time_delay of this RateControl.

        每批间隔。

        :param time_delay: The time_delay of this RateControl.
        :type time_delay: int
        """
        self._time_delay = time_delay

    @property
    def max(self):
        """Gets the max of this RateControl.

        每批支持的最大实例数。

        :return: The max of this RateControl.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this RateControl.

        每批支持的最大实例数。

        :param max: The max of this RateControl.
        :type max: int
        """
        self._max = max

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
        if not isinstance(other, RateControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

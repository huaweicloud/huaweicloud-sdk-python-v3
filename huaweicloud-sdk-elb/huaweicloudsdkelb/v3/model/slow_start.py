# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowStart:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'duration': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'duration': 'duration'
    }

    def __init__(self, enable=None, duration=None):
        r"""SlowStart

        The model defined in huaweicloud sdk

        :param enable: 参数解释：慢启动的开关。  取值范围： - true：开启。 - false：关闭。  默认取值：false 
        :type enable: bool
        :param duration: 参数解释：慢启动的持续时间。  取值范围：30-1200，单位：秒。  默认取值：30
        :type duration: int
        """
        
        

        self._enable = None
        self._duration = None
        self.discriminator = None

        self.enable = enable
        self.duration = duration

    @property
    def enable(self):
        r"""Gets the enable of this SlowStart.

        参数解释：慢启动的开关。  取值范围： - true：开启。 - false：关闭。  默认取值：false 

        :return: The enable of this SlowStart.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this SlowStart.

        参数解释：慢启动的开关。  取值范围： - true：开启。 - false：关闭。  默认取值：false 

        :param enable: The enable of this SlowStart.
        :type enable: bool
        """
        self._enable = enable

    @property
    def duration(self):
        r"""Gets the duration of this SlowStart.

        参数解释：慢启动的持续时间。  取值范围：30-1200，单位：秒。  默认取值：30

        :return: The duration of this SlowStart.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SlowStart.

        参数解释：慢启动的持续时间。  取值范围：30-1200，单位：秒。  默认取值：30

        :param duration: The duration of this SlowStart.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, SlowStart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

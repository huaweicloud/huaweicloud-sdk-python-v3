# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePoolSlowStartOption:

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
        """CreatePoolSlowStartOption

        The model defined in huaweicloud sdk

        :param enable: 慢启动的开关，默认值：false； true：开启； false：关闭 
        :type enable: bool
        :param duration: 慢启动的持续时间，单位：s。默认：30； 取值范围：30~1200
        :type duration: int
        """
        
        

        self._enable = None
        self._duration = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if duration is not None:
            self.duration = duration

    @property
    def enable(self):
        """Gets the enable of this CreatePoolSlowStartOption.

        慢启动的开关，默认值：false； true：开启； false：关闭 

        :return: The enable of this CreatePoolSlowStartOption.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreatePoolSlowStartOption.

        慢启动的开关，默认值：false； true：开启； false：关闭 

        :param enable: The enable of this CreatePoolSlowStartOption.
        :type enable: bool
        """
        self._enable = enable

    @property
    def duration(self):
        """Gets the duration of this CreatePoolSlowStartOption.

        慢启动的持续时间，单位：s。默认：30； 取值范围：30~1200

        :return: The duration of this CreatePoolSlowStartOption.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this CreatePoolSlowStartOption.

        慢启动的持续时间，单位：s。默认：30； 取值范围：30~1200

        :param duration: The duration of this CreatePoolSlowStartOption.
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
        if not isinstance(other, CreatePoolSlowStartOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

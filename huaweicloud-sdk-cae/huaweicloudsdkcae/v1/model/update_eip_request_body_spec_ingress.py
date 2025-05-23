# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEipRequestBodySpecIngress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_size': 'int',
        'enabled': 'bool'
    }

    attribute_map = {
        'bandwidth_size': 'bandwidth_size',
        'enabled': 'enabled'
    }

    def __init__(self, bandwidth_size=None, enabled=None):
        r"""UpdateEipRequestBodySpecIngress

        The model defined in huaweicloud sdk

        :param bandwidth_size: 入网IP带宽。
        :type bandwidth_size: int
        :param enabled: 是否关闭入网IP。
        :type enabled: bool
        """
        
        

        self._bandwidth_size = None
        self._enabled = None
        self.discriminator = None

        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if enabled is not None:
            self.enabled = enabled

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this UpdateEipRequestBodySpecIngress.

        入网IP带宽。

        :return: The bandwidth_size of this UpdateEipRequestBodySpecIngress.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this UpdateEipRequestBodySpecIngress.

        入网IP带宽。

        :param bandwidth_size: The bandwidth_size of this UpdateEipRequestBodySpecIngress.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateEipRequestBodySpecIngress.

        是否关闭入网IP。

        :return: The enabled of this UpdateEipRequestBodySpecIngress.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateEipRequestBodySpecIngress.

        是否关闭入网IP。

        :param enabled: The enabled of this UpdateEipRequestBodySpecIngress.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, UpdateEipRequestBodySpecIngress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

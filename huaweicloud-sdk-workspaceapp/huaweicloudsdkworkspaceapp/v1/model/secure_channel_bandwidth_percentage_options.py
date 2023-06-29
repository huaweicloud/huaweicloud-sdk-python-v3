# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecureChannelBandwidthPercentageOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secure_channel_bandwidth_percentage_value': 'int'
    }

    attribute_map = {
        'secure_channel_bandwidth_percentage_value': 'secure_channel_bandwidth_percentage_value'
    }

    def __init__(self, secure_channel_bandwidth_percentage_value=None):
        """SecureChannelBandwidthPercentageOptions

        The model defined in huaweicloud sdk

        :param secure_channel_bandwidth_percentage_value: 安全通道带宽百分比控制量（%）。取值范围为[0-100]。默认：30。
        :type secure_channel_bandwidth_percentage_value: int
        """
        
        

        self._secure_channel_bandwidth_percentage_value = None
        self.discriminator = None

        if secure_channel_bandwidth_percentage_value is not None:
            self.secure_channel_bandwidth_percentage_value = secure_channel_bandwidth_percentage_value

    @property
    def secure_channel_bandwidth_percentage_value(self):
        """Gets the secure_channel_bandwidth_percentage_value of this SecureChannelBandwidthPercentageOptions.

        安全通道带宽百分比控制量（%）。取值范围为[0-100]。默认：30。

        :return: The secure_channel_bandwidth_percentage_value of this SecureChannelBandwidthPercentageOptions.
        :rtype: int
        """
        return self._secure_channel_bandwidth_percentage_value

    @secure_channel_bandwidth_percentage_value.setter
    def secure_channel_bandwidth_percentage_value(self, secure_channel_bandwidth_percentage_value):
        """Sets the secure_channel_bandwidth_percentage_value of this SecureChannelBandwidthPercentageOptions.

        安全通道带宽百分比控制量（%）。取值范围为[0-100]。默认：30。

        :param secure_channel_bandwidth_percentage_value: The secure_channel_bandwidth_percentage_value of this SecureChannelBandwidthPercentageOptions.
        :type secure_channel_bandwidth_percentage_value: int
        """
        self._secure_channel_bandwidth_percentage_value = secure_channel_bandwidth_percentage_value

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
        if not isinstance(other, SecureChannelBandwidthPercentageOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

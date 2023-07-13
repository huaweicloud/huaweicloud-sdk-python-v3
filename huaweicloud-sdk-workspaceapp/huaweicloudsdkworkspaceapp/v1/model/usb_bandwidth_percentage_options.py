# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UsbBandwidthPercentageOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'usb_bandwidth_percentage_value': 'int'
    }

    attribute_map = {
        'usb_bandwidth_percentage_value': 'usb_bandwidth_percentage_value'
    }

    def __init__(self, usb_bandwidth_percentage_value=None):
        """UsbBandwidthPercentageOptions

        The model defined in huaweicloud sdk

        :param usb_bandwidth_percentage_value: USB带宽百分比控制量（%）。取值范围为[0-100]。默认：100。
        :type usb_bandwidth_percentage_value: int
        """
        
        

        self._usb_bandwidth_percentage_value = None
        self.discriminator = None

        if usb_bandwidth_percentage_value is not None:
            self.usb_bandwidth_percentage_value = usb_bandwidth_percentage_value

    @property
    def usb_bandwidth_percentage_value(self):
        """Gets the usb_bandwidth_percentage_value of this UsbBandwidthPercentageOptions.

        USB带宽百分比控制量（%）。取值范围为[0-100]。默认：100。

        :return: The usb_bandwidth_percentage_value of this UsbBandwidthPercentageOptions.
        :rtype: int
        """
        return self._usb_bandwidth_percentage_value

    @usb_bandwidth_percentage_value.setter
    def usb_bandwidth_percentage_value(self, usb_bandwidth_percentage_value):
        """Sets the usb_bandwidth_percentage_value of this UsbBandwidthPercentageOptions.

        USB带宽百分比控制量（%）。取值范围为[0-100]。默认：100。

        :param usb_bandwidth_percentage_value: The usb_bandwidth_percentage_value of this UsbBandwidthPercentageOptions.
        :type usb_bandwidth_percentage_value: int
        """
        self._usb_bandwidth_percentage_value = usb_bandwidth_percentage_value

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
        if not isinstance(other, UsbBandwidthPercentageOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClipboardBandwidthPercentageOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clipboard_bandwidth_percentage_value': 'int'
    }

    attribute_map = {
        'clipboard_bandwidth_percentage_value': 'clipboard_bandwidth_percentage_value'
    }

    def __init__(self, clipboard_bandwidth_percentage_value=None):
        r"""ClipboardBandwidthPercentageOptions

        The model defined in huaweicloud sdk

        :param clipboard_bandwidth_percentage_value: 剪切板带宽百分比控制量（%）。取值范围为[0-100]。默认：3。
        :type clipboard_bandwidth_percentage_value: int
        """
        
        

        self._clipboard_bandwidth_percentage_value = None
        self.discriminator = None

        if clipboard_bandwidth_percentage_value is not None:
            self.clipboard_bandwidth_percentage_value = clipboard_bandwidth_percentage_value

    @property
    def clipboard_bandwidth_percentage_value(self):
        r"""Gets the clipboard_bandwidth_percentage_value of this ClipboardBandwidthPercentageOptions.

        剪切板带宽百分比控制量（%）。取值范围为[0-100]。默认：3。

        :return: The clipboard_bandwidth_percentage_value of this ClipboardBandwidthPercentageOptions.
        :rtype: int
        """
        return self._clipboard_bandwidth_percentage_value

    @clipboard_bandwidth_percentage_value.setter
    def clipboard_bandwidth_percentage_value(self, clipboard_bandwidth_percentage_value):
        r"""Sets the clipboard_bandwidth_percentage_value of this ClipboardBandwidthPercentageOptions.

        剪切板带宽百分比控制量（%）。取值范围为[0-100]。默认：3。

        :param clipboard_bandwidth_percentage_value: The clipboard_bandwidth_percentage_value of this ClipboardBandwidthPercentageOptions.
        :type clipboard_bandwidth_percentage_value: int
        """
        self._clipboard_bandwidth_percentage_value = clipboard_bandwidth_percentage_value

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
        if not isinstance(other, ClipboardBandwidthPercentageOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

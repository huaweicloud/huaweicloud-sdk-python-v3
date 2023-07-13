# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisplayBandwidthControlOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_bandwidth_control_value': 'int'
    }

    attribute_map = {
        'display_bandwidth_control_value': 'display_bandwidth_control_value'
    }

    def __init__(self, display_bandwidth_control_value=None):
        """DisplayBandwidthControlOptions

        The model defined in huaweicloud sdk

        :param display_bandwidth_control_value: 显示带宽控制量（Kbps）。取值范围为[500-50000]。默认：20000。
        :type display_bandwidth_control_value: int
        """
        
        

        self._display_bandwidth_control_value = None
        self.discriminator = None

        if display_bandwidth_control_value is not None:
            self.display_bandwidth_control_value = display_bandwidth_control_value

    @property
    def display_bandwidth_control_value(self):
        """Gets the display_bandwidth_control_value of this DisplayBandwidthControlOptions.

        显示带宽控制量（Kbps）。取值范围为[500-50000]。默认：20000。

        :return: The display_bandwidth_control_value of this DisplayBandwidthControlOptions.
        :rtype: int
        """
        return self._display_bandwidth_control_value

    @display_bandwidth_control_value.setter
    def display_bandwidth_control_value(self, display_bandwidth_control_value):
        """Sets the display_bandwidth_control_value of this DisplayBandwidthControlOptions.

        显示带宽控制量（Kbps）。取值范围为[500-50000]。默认：20000。

        :param display_bandwidth_control_value: The display_bandwidth_control_value of this DisplayBandwidthControlOptions.
        :type display_bandwidth_control_value: int
        """
        self._display_bandwidth_control_value = display_bandwidth_control_value

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
        if not isinstance(other, DisplayBandwidthControlOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

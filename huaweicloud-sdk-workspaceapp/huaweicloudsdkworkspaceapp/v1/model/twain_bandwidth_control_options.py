# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TwainBandwidthControlOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'twain_bandwidth_control_value': 'int'
    }

    attribute_map = {
        'twain_bandwidth_control_value': 'twain_bandwidth_control_value'
    }

    def __init__(self, twain_bandwidth_control_value=None):
        """TwainBandwidthControlOptions

        The model defined in huaweicloud sdk

        :param twain_bandwidth_control_value: TWAIN带宽控制量（Kbps）。取值范围为[2000-10000]。默认：5000。
        :type twain_bandwidth_control_value: int
        """
        
        

        self._twain_bandwidth_control_value = None
        self.discriminator = None

        if twain_bandwidth_control_value is not None:
            self.twain_bandwidth_control_value = twain_bandwidth_control_value

    @property
    def twain_bandwidth_control_value(self):
        """Gets the twain_bandwidth_control_value of this TwainBandwidthControlOptions.

        TWAIN带宽控制量（Kbps）。取值范围为[2000-10000]。默认：5000。

        :return: The twain_bandwidth_control_value of this TwainBandwidthControlOptions.
        :rtype: int
        """
        return self._twain_bandwidth_control_value

    @twain_bandwidth_control_value.setter
    def twain_bandwidth_control_value(self, twain_bandwidth_control_value):
        """Sets the twain_bandwidth_control_value of this TwainBandwidthControlOptions.

        TWAIN带宽控制量（Kbps）。取值范围为[2000-10000]。默认：5000。

        :param twain_bandwidth_control_value: The twain_bandwidth_control_value of this TwainBandwidthControlOptions.
        :type twain_bandwidth_control_value: int
        """
        self._twain_bandwidth_control_value = twain_bandwidth_control_value

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
        if not isinstance(other, TwainBandwidthControlOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

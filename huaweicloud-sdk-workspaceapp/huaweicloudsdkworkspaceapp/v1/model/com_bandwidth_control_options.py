# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComBandwidthControlOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'com_bandwidth_control_value': 'int'
    }

    attribute_map = {
        'com_bandwidth_control_value': 'com_bandwidth_control_value'
    }

    def __init__(self, com_bandwidth_control_value=None):
        """ComBandwidthControlOptions

        The model defined in huaweicloud sdk

        :param com_bandwidth_control_value: 串口带宽控制量（Kbps）。取值范围为[500-2000]。默认：1000。
        :type com_bandwidth_control_value: int
        """
        
        

        self._com_bandwidth_control_value = None
        self.discriminator = None

        if com_bandwidth_control_value is not None:
            self.com_bandwidth_control_value = com_bandwidth_control_value

    @property
    def com_bandwidth_control_value(self):
        """Gets the com_bandwidth_control_value of this ComBandwidthControlOptions.

        串口带宽控制量（Kbps）。取值范围为[500-2000]。默认：1000。

        :return: The com_bandwidth_control_value of this ComBandwidthControlOptions.
        :rtype: int
        """
        return self._com_bandwidth_control_value

    @com_bandwidth_control_value.setter
    def com_bandwidth_control_value(self, com_bandwidth_control_value):
        """Sets the com_bandwidth_control_value of this ComBandwidthControlOptions.

        串口带宽控制量（Kbps）。取值范围为[500-2000]。默认：1000。

        :param com_bandwidth_control_value: The com_bandwidth_control_value of this ComBandwidthControlOptions.
        :type com_bandwidth_control_value: int
        """
        self._com_bandwidth_control_value = com_bandwidth_control_value

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
        if not isinstance(other, ComBandwidthControlOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

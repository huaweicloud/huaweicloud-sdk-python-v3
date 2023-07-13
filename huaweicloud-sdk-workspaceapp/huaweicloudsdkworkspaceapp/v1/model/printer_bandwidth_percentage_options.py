# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrinterBandwidthPercentageOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'printer_bandwidth_percentage_value': 'int'
    }

    attribute_map = {
        'printer_bandwidth_percentage_value': 'printer_bandwidth_percentage_value'
    }

    def __init__(self, printer_bandwidth_percentage_value=None):
        """PrinterBandwidthPercentageOptions

        The model defined in huaweicloud sdk

        :param printer_bandwidth_percentage_value: 打印机带宽百分比控制量（%）。取值范围为[0-100]。默认：5。
        :type printer_bandwidth_percentage_value: int
        """
        
        

        self._printer_bandwidth_percentage_value = None
        self.discriminator = None

        if printer_bandwidth_percentage_value is not None:
            self.printer_bandwidth_percentage_value = printer_bandwidth_percentage_value

    @property
    def printer_bandwidth_percentage_value(self):
        """Gets the printer_bandwidth_percentage_value of this PrinterBandwidthPercentageOptions.

        打印机带宽百分比控制量（%）。取值范围为[0-100]。默认：5。

        :return: The printer_bandwidth_percentage_value of this PrinterBandwidthPercentageOptions.
        :rtype: int
        """
        return self._printer_bandwidth_percentage_value

    @printer_bandwidth_percentage_value.setter
    def printer_bandwidth_percentage_value(self, printer_bandwidth_percentage_value):
        """Sets the printer_bandwidth_percentage_value of this PrinterBandwidthPercentageOptions.

        打印机带宽百分比控制量（%）。取值范围为[0-100]。默认：5。

        :param printer_bandwidth_percentage_value: The printer_bandwidth_percentage_value of this PrinterBandwidthPercentageOptions.
        :type printer_bandwidth_percentage_value: int
        """
        self._printer_bandwidth_percentage_value = printer_bandwidth_percentage_value

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
        if not isinstance(other, PrinterBandwidthPercentageOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

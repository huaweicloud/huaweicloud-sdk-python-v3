# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsDeviceRedirectionPrinterRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'printer_enable': 'bool',
        'options': 'PrinterRedirectionOptions'
    }

    attribute_map = {
        'printer_enable': 'printer_enable',
        'options': 'options'
    }

    def __init__(self, printer_enable=None, options=None):
        """PoliciesPeripheralsDeviceRedirectionPrinterRedirection

        The model defined in huaweicloud sdk

        :param printer_enable: 是否开启打印机设备重定向。取值为： - false：表示关闭。 - true：表示开启。
        :type printer_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.PrinterRedirectionOptions`
        """
        
        

        self._printer_enable = None
        self._options = None
        self.discriminator = None

        if printer_enable is not None:
            self.printer_enable = printer_enable
        if options is not None:
            self.options = options

    @property
    def printer_enable(self):
        """Gets the printer_enable of this PoliciesPeripheralsDeviceRedirectionPrinterRedirection.

        是否开启打印机设备重定向。取值为： - false：表示关闭。 - true：表示开启。

        :return: The printer_enable of this PoliciesPeripheralsDeviceRedirectionPrinterRedirection.
        :rtype: bool
        """
        return self._printer_enable

    @printer_enable.setter
    def printer_enable(self, printer_enable):
        """Sets the printer_enable of this PoliciesPeripheralsDeviceRedirectionPrinterRedirection.

        是否开启打印机设备重定向。取值为： - false：表示关闭。 - true：表示开启。

        :param printer_enable: The printer_enable of this PoliciesPeripheralsDeviceRedirectionPrinterRedirection.
        :type printer_enable: bool
        """
        self._printer_enable = printer_enable

    @property
    def options(self):
        """Gets the options of this PoliciesPeripheralsDeviceRedirectionPrinterRedirection.

        :return: The options of this PoliciesPeripheralsDeviceRedirectionPrinterRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PrinterRedirectionOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PoliciesPeripheralsDeviceRedirectionPrinterRedirection.

        :param options: The options of this PoliciesPeripheralsDeviceRedirectionPrinterRedirection.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.PrinterRedirectionOptions`
        """
        self._options = options

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
        if not isinstance(other, PoliciesPeripheralsDeviceRedirectionPrinterRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

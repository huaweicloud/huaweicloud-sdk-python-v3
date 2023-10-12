# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsSerialPortRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'serial_port_enable': 'bool',
        'options': 'SerialPortRedirectionOptions'
    }

    attribute_map = {
        'serial_port_enable': 'serial_port_enable',
        'options': 'options'
    }

    def __init__(self, serial_port_enable=None, options=None):
        """PoliciesPeripheralsSerialPortRedirection

        The model defined in huaweicloud sdk

        :param serial_port_enable: 是否开启串口重定向。取值为： false：表示关闭。 true：表示开启。
        :type serial_port_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.SerialPortRedirectionOptions`
        """
        
        

        self._serial_port_enable = None
        self._options = None
        self.discriminator = None

        if serial_port_enable is not None:
            self.serial_port_enable = serial_port_enable
        if options is not None:
            self.options = options

    @property
    def serial_port_enable(self):
        """Gets the serial_port_enable of this PoliciesPeripheralsSerialPortRedirection.

        是否开启串口重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The serial_port_enable of this PoliciesPeripheralsSerialPortRedirection.
        :rtype: bool
        """
        return self._serial_port_enable

    @serial_port_enable.setter
    def serial_port_enable(self, serial_port_enable):
        """Sets the serial_port_enable of this PoliciesPeripheralsSerialPortRedirection.

        是否开启串口重定向。取值为： false：表示关闭。 true：表示开启。

        :param serial_port_enable: The serial_port_enable of this PoliciesPeripheralsSerialPortRedirection.
        :type serial_port_enable: bool
        """
        self._serial_port_enable = serial_port_enable

    @property
    def options(self):
        """Gets the options of this PoliciesPeripheralsSerialPortRedirection.

        :return: The options of this PoliciesPeripheralsSerialPortRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.SerialPortRedirectionOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PoliciesPeripheralsSerialPortRedirection.

        :param options: The options of this PoliciesPeripheralsSerialPortRedirection.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.SerialPortRedirectionOptions`
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
        if not isinstance(other, PoliciesPeripheralsSerialPortRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

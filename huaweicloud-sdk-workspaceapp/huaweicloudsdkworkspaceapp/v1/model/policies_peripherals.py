# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripherals:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'usb_port_redirection': 'PoliciesPeripheralsUsbPortRedirection',
        'device_redirection': 'PoliciesPeripheralsDeviceRedirection',
        'usb_device_common': 'PoliciesPeripheralsUsbDeviceCommon',
        'serial_port_redirection': 'PoliciesPeripheralsSerialPortRedirection'
    }

    attribute_map = {
        'usb_port_redirection': 'usb_port_redirection',
        'device_redirection': 'device_redirection',
        'usb_device_common': 'usb_device_common',
        'serial_port_redirection': 'serial_port_redirection'
    }

    def __init__(self, usb_port_redirection=None, device_redirection=None, usb_device_common=None, serial_port_redirection=None):
        """PoliciesPeripherals

        The model defined in huaweicloud sdk

        :param usb_port_redirection: 
        :type usb_port_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsUsbPortRedirection`
        :param device_redirection: 
        :type device_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirection`
        :param usb_device_common: 
        :type usb_device_common: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsUsbDeviceCommon`
        :param serial_port_redirection: 
        :type serial_port_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsSerialPortRedirection`
        """
        
        

        self._usb_port_redirection = None
        self._device_redirection = None
        self._usb_device_common = None
        self._serial_port_redirection = None
        self.discriminator = None

        if usb_port_redirection is not None:
            self.usb_port_redirection = usb_port_redirection
        if device_redirection is not None:
            self.device_redirection = device_redirection
        if usb_device_common is not None:
            self.usb_device_common = usb_device_common
        if serial_port_redirection is not None:
            self.serial_port_redirection = serial_port_redirection

    @property
    def usb_port_redirection(self):
        """Gets the usb_port_redirection of this PoliciesPeripherals.

        :return: The usb_port_redirection of this PoliciesPeripherals.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsUsbPortRedirection`
        """
        return self._usb_port_redirection

    @usb_port_redirection.setter
    def usb_port_redirection(self, usb_port_redirection):
        """Sets the usb_port_redirection of this PoliciesPeripherals.

        :param usb_port_redirection: The usb_port_redirection of this PoliciesPeripherals.
        :type usb_port_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsUsbPortRedirection`
        """
        self._usb_port_redirection = usb_port_redirection

    @property
    def device_redirection(self):
        """Gets the device_redirection of this PoliciesPeripherals.

        :return: The device_redirection of this PoliciesPeripherals.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirection`
        """
        return self._device_redirection

    @device_redirection.setter
    def device_redirection(self, device_redirection):
        """Sets the device_redirection of this PoliciesPeripherals.

        :param device_redirection: The device_redirection of this PoliciesPeripherals.
        :type device_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsDeviceRedirection`
        """
        self._device_redirection = device_redirection

    @property
    def usb_device_common(self):
        """Gets the usb_device_common of this PoliciesPeripherals.

        :return: The usb_device_common of this PoliciesPeripherals.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsUsbDeviceCommon`
        """
        return self._usb_device_common

    @usb_device_common.setter
    def usb_device_common(self, usb_device_common):
        """Sets the usb_device_common of this PoliciesPeripherals.

        :param usb_device_common: The usb_device_common of this PoliciesPeripherals.
        :type usb_device_common: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsUsbDeviceCommon`
        """
        self._usb_device_common = usb_device_common

    @property
    def serial_port_redirection(self):
        """Gets the serial_port_redirection of this PoliciesPeripherals.

        :return: The serial_port_redirection of this PoliciesPeripherals.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsSerialPortRedirection`
        """
        return self._serial_port_redirection

    @serial_port_redirection.setter
    def serial_port_redirection(self, serial_port_redirection):
        """Sets the serial_port_redirection of this PoliciesPeripherals.

        :param serial_port_redirection: The serial_port_redirection of this PoliciesPeripherals.
        :type serial_port_redirection: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesPeripheralsSerialPortRedirection`
        """
        self._serial_port_redirection = serial_port_redirection

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
        if not isinstance(other, PoliciesPeripherals):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

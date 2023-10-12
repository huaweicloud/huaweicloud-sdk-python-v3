# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsUsbPortRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'usb_enable': 'bool',
        'options': 'UsbPortRedirectionOptions'
    }

    attribute_map = {
        'usb_enable': 'usb_enable',
        'options': 'options'
    }

    def __init__(self, usb_enable=None, options=None):
        """PoliciesPeripheralsUsbPortRedirection

        The model defined in huaweicloud sdk

        :param usb_enable: 是否开启USB端口重定向。 - false：表示关闭。 - true：表示开启。
        :type usb_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.UsbPortRedirectionOptions`
        """
        
        

        self._usb_enable = None
        self._options = None
        self.discriminator = None

        if usb_enable is not None:
            self.usb_enable = usb_enable
        if options is not None:
            self.options = options

    @property
    def usb_enable(self):
        """Gets the usb_enable of this PoliciesPeripheralsUsbPortRedirection.

        是否开启USB端口重定向。 - false：表示关闭。 - true：表示开启。

        :return: The usb_enable of this PoliciesPeripheralsUsbPortRedirection.
        :rtype: bool
        """
        return self._usb_enable

    @usb_enable.setter
    def usb_enable(self, usb_enable):
        """Sets the usb_enable of this PoliciesPeripheralsUsbPortRedirection.

        是否开启USB端口重定向。 - false：表示关闭。 - true：表示开启。

        :param usb_enable: The usb_enable of this PoliciesPeripheralsUsbPortRedirection.
        :type usb_enable: bool
        """
        self._usb_enable = usb_enable

    @property
    def options(self):
        """Gets the options of this PoliciesPeripheralsUsbPortRedirection.

        :return: The options of this PoliciesPeripheralsUsbPortRedirection.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UsbPortRedirectionOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PoliciesPeripheralsUsbPortRedirection.

        :param options: The options of this PoliciesPeripheralsUsbPortRedirection.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.UsbPortRedirectionOptions`
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
        if not isinstance(other, PoliciesPeripheralsUsbPortRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

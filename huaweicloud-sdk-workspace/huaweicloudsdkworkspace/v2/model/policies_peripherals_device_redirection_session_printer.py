# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsDeviceRedirectionSessionPrinter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_printer_enable': 'bool',
        'options': 'PoliciesPeripheralsDeviceRedirectionSessionPrinterOptions'
    }

    attribute_map = {
        'session_printer_enable': 'session_printer_enable',
        'options': 'options'
    }

    def __init__(self, session_printer_enable=None, options=None):
        r"""PoliciesPeripheralsDeviceRedirectionSessionPrinter

        The model defined in huaweicloud sdk

        :param session_printer_enable: 是否开启会话打印机。取值为： false：表示关闭。 true：表示开启。
        :type session_printer_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesPeripheralsDeviceRedirectionSessionPrinterOptions`
        """
        
        

        self._session_printer_enable = None
        self._options = None
        self.discriminator = None

        if session_printer_enable is not None:
            self.session_printer_enable = session_printer_enable
        if options is not None:
            self.options = options

    @property
    def session_printer_enable(self):
        r"""Gets the session_printer_enable of this PoliciesPeripheralsDeviceRedirectionSessionPrinter.

        是否开启会话打印机。取值为： false：表示关闭。 true：表示开启。

        :return: The session_printer_enable of this PoliciesPeripheralsDeviceRedirectionSessionPrinter.
        :rtype: bool
        """
        return self._session_printer_enable

    @session_printer_enable.setter
    def session_printer_enable(self, session_printer_enable):
        r"""Sets the session_printer_enable of this PoliciesPeripheralsDeviceRedirectionSessionPrinter.

        是否开启会话打印机。取值为： false：表示关闭。 true：表示开启。

        :param session_printer_enable: The session_printer_enable of this PoliciesPeripheralsDeviceRedirectionSessionPrinter.
        :type session_printer_enable: bool
        """
        self._session_printer_enable = session_printer_enable

    @property
    def options(self):
        r"""Gets the options of this PoliciesPeripheralsDeviceRedirectionSessionPrinter.

        :return: The options of this PoliciesPeripheralsDeviceRedirectionSessionPrinter.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesPeripheralsDeviceRedirectionSessionPrinterOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesPeripheralsDeviceRedirectionSessionPrinter.

        :param options: The options of this PoliciesPeripheralsDeviceRedirectionSessionPrinter.
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesPeripheralsDeviceRedirectionSessionPrinterOptions`
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
        if not isinstance(other, PoliciesPeripheralsDeviceRedirectionSessionPrinter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

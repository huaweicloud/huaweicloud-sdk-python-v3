# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsDeviceRedirectionHidRedirection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hid_redirection_enable': 'bool',
        'options': 'PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions'
    }

    attribute_map = {
        'hid_redirection_enable': 'hid_redirection_enable',
        'options': 'options'
    }

    def __init__(self, hid_redirection_enable=None, options=None):
        r"""PoliciesPeripheralsDeviceRedirectionHidRedirection

        The model defined in huaweicloud sdk

        :param hid_redirection_enable: 是否开启HID（人体学设备）重定向。取值为： false：表示关闭。 true：表示开启。
        :type hid_redirection_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions`
        """
        
        

        self._hid_redirection_enable = None
        self._options = None
        self.discriminator = None

        if hid_redirection_enable is not None:
            self.hid_redirection_enable = hid_redirection_enable
        if options is not None:
            self.options = options

    @property
    def hid_redirection_enable(self):
        r"""Gets the hid_redirection_enable of this PoliciesPeripheralsDeviceRedirectionHidRedirection.

        是否开启HID（人体学设备）重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The hid_redirection_enable of this PoliciesPeripheralsDeviceRedirectionHidRedirection.
        :rtype: bool
        """
        return self._hid_redirection_enable

    @hid_redirection_enable.setter
    def hid_redirection_enable(self, hid_redirection_enable):
        r"""Sets the hid_redirection_enable of this PoliciesPeripheralsDeviceRedirectionHidRedirection.

        是否开启HID（人体学设备）重定向。取值为： false：表示关闭。 true：表示开启。

        :param hid_redirection_enable: The hid_redirection_enable of this PoliciesPeripheralsDeviceRedirectionHidRedirection.
        :type hid_redirection_enable: bool
        """
        self._hid_redirection_enable = hid_redirection_enable

    @property
    def options(self):
        r"""Gets the options of this PoliciesPeripheralsDeviceRedirectionHidRedirection.

        :return: The options of this PoliciesPeripheralsDeviceRedirectionHidRedirection.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesPeripheralsDeviceRedirectionHidRedirection.

        :param options: The options of this PoliciesPeripheralsDeviceRedirectionHidRedirection.
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions`
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
        if not isinstance(other, PoliciesPeripheralsDeviceRedirectionHidRedirection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

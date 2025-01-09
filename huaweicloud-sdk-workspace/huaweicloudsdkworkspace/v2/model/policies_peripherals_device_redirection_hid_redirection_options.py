# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hid_redirection_customization_policy': 'str'
    }

    attribute_map = {
        'hid_redirection_customization_policy': 'hid_redirection_customization_policy'
    }

    def __init__(self, hid_redirection_customization_policy=None):
        """PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions

        The model defined in huaweicloud sdk

        :param hid_redirection_customization_policy: HID重定向自定义策略。
        :type hid_redirection_customization_policy: str
        """
        
        

        self._hid_redirection_customization_policy = None
        self.discriminator = None

        if hid_redirection_customization_policy is not None:
            self.hid_redirection_customization_policy = hid_redirection_customization_policy

    @property
    def hid_redirection_customization_policy(self):
        """Gets the hid_redirection_customization_policy of this PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions.

        HID重定向自定义策略。

        :return: The hid_redirection_customization_policy of this PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions.
        :rtype: str
        """
        return self._hid_redirection_customization_policy

    @hid_redirection_customization_policy.setter
    def hid_redirection_customization_policy(self, hid_redirection_customization_policy):
        """Sets the hid_redirection_customization_policy of this PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions.

        HID重定向自定义策略。

        :param hid_redirection_customization_policy: The hid_redirection_customization_policy of this PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions.
        :type hid_redirection_customization_policy: str
        """
        self._hid_redirection_customization_policy = hid_redirection_customization_policy

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
        if not isinstance(other, PoliciesPeripheralsDeviceRedirectionHidRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

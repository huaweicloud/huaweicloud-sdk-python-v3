# coding: utf-8

import pprint
import re

import six





class AuthInfoWithoutSecret:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'secure_access': 'bool',
        'timeout': 'int'
    }

    attribute_map = {
        'secure_access': 'secure_access',
        'timeout': 'timeout'
    }

    def __init__(self, secure_access=True, timeout=0):
        """AuthInfoWithoutSecret - a model defined in huaweicloud sdk"""
        
        

        self._secure_access = None
        self._timeout = None
        self.discriminator = None

        if secure_access is not None:
            self.secure_access = secure_access
        if timeout is not None:
            self.timeout = timeout

    @property
    def secure_access(self):
        """Gets the secure_access of this AuthInfoWithoutSecret.

        指设备是否通过安全协议方式接入，默认值为true。 - true：通过安全协议方式接入。 - false：通过非安全协议方式接入。 

        :return: The secure_access of this AuthInfoWithoutSecret.
        :rtype: bool
        """
        return self._secure_access

    @secure_access.setter
    def secure_access(self, secure_access):
        """Sets the secure_access of this AuthInfoWithoutSecret.

        指设备是否通过安全协议方式接入，默认值为true。 - true：通过安全协议方式接入。 - false：通过非安全协议方式接入。 

        :param secure_access: The secure_access of this AuthInfoWithoutSecret.
        :type: bool
        """
        self._secure_access = secure_access

    @property
    def timeout(self):
        """Gets the timeout of this AuthInfoWithoutSecret.

        设备验证码的有效时间，单位：秒，默认值：0 若设备在有效时间内未接入物联网平台并激活，则平台会删除该设备的注册信息。若设置为“0”，则表示设备验证码不会失效（建议填写为“0”）。 

        :return: The timeout of this AuthInfoWithoutSecret.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this AuthInfoWithoutSecret.

        设备验证码的有效时间，单位：秒，默认值：0 若设备在有效时间内未接入物联网平台并激活，则平台会删除该设备的注册信息。若设置为“0”，则表示设备验证码不会失效（建议填写为“0”）。 

        :param timeout: The timeout of this AuthInfoWithoutSecret.
        :type: int
        """
        self._timeout = timeout

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuthInfoWithoutSecret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

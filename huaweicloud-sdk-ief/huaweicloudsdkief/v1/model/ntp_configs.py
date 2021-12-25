# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NtpConfigs:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ntp_enabled': 'bool',
        'ntpservers': 'list[str]'
    }

    attribute_map = {
        'ntp_enabled': 'ntp_enabled',
        'ntpservers': 'ntpservers'
    }

    def __init__(self, ntp_enabled=None, ntpservers=None):
        """NtpConfigs - a model defined in huaweicloud sdk"""
        
        

        self._ntp_enabled = None
        self._ntpservers = None
        self.discriminator = None

        if ntp_enabled is not None:
            self.ntp_enabled = ntp_enabled
        if ntpservers is not None:
            self.ntpservers = ntpservers

    @property
    def ntp_enabled(self):
        """Gets the ntp_enabled of this NtpConfigs.

        ntp服务是否开启

        :return: The ntp_enabled of this NtpConfigs.
        :rtype: bool
        """
        return self._ntp_enabled

    @ntp_enabled.setter
    def ntp_enabled(self, ntp_enabled):
        """Sets the ntp_enabled of this NtpConfigs.

        ntp服务是否开启

        :param ntp_enabled: The ntp_enabled of this NtpConfigs.
        :type: bool
        """
        self._ntp_enabled = ntp_enabled

    @property
    def ntpservers(self):
        """Gets the ntpservers of this NtpConfigs.

        ntp server地址

        :return: The ntpservers of this NtpConfigs.
        :rtype: list[str]
        """
        return self._ntpservers

    @ntpservers.setter
    def ntpservers(self, ntpservers):
        """Sets the ntpservers of this NtpConfigs.

        ntp server地址

        :param ntpservers: The ntpservers of this NtpConfigs.
        :type: list[str]
        """
        self._ntpservers = ntpservers

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
        if not isinstance(other, NtpConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

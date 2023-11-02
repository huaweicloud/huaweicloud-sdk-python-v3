# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClientIpTransparentTransmissionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transparent_client_ip_enable': 'bool'
    }

    attribute_map = {
        'transparent_client_ip_enable': 'transparent_client_ip_enable'
    }

    def __init__(self, transparent_client_ip_enable=None):
        """UpdateClientIpTransparentTransmissionRequestBody

        The model defined in huaweicloud sdk

        :param transparent_client_ip_enable: 开启或关闭客户ip透传标志
        :type transparent_client_ip_enable: bool
        """
        
        

        self._transparent_client_ip_enable = None
        self.discriminator = None

        if transparent_client_ip_enable is not None:
            self.transparent_client_ip_enable = transparent_client_ip_enable

    @property
    def transparent_client_ip_enable(self):
        """Gets the transparent_client_ip_enable of this UpdateClientIpTransparentTransmissionRequestBody.

        开启或关闭客户ip透传标志

        :return: The transparent_client_ip_enable of this UpdateClientIpTransparentTransmissionRequestBody.
        :rtype: bool
        """
        return self._transparent_client_ip_enable

    @transparent_client_ip_enable.setter
    def transparent_client_ip_enable(self, transparent_client_ip_enable):
        """Sets the transparent_client_ip_enable of this UpdateClientIpTransparentTransmissionRequestBody.

        开启或关闭客户ip透传标志

        :param transparent_client_ip_enable: The transparent_client_ip_enable of this UpdateClientIpTransparentTransmissionRequestBody.
        :type transparent_client_ip_enable: bool
        """
        self._transparent_client_ip_enable = transparent_client_ip_enable

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
        if not isinstance(other, UpdateClientIpTransparentTransmissionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

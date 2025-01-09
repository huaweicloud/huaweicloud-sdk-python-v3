# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessControl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_access_control': 'str'
    }

    attribute_map = {
        'ip_access_control': 'ip_access_control'
    }

    def __init__(self, ip_access_control=None):
        """AccessControl

        The model defined in huaweicloud sdk

        :param ip_access_control: IP接入控制。IP接入控制需输入有效的IP地址和子网掩码，IP和子网掩码间以\&quot;|\&quot;拼接组成一组，如果有多组用\&quot;;\&quot;分隔。如：IP|掩码;IP|掩码;IP|掩码。
        :type ip_access_control: str
        """
        
        

        self._ip_access_control = None
        self.discriminator = None

        if ip_access_control is not None:
            self.ip_access_control = ip_access_control

    @property
    def ip_access_control(self):
        """Gets the ip_access_control of this AccessControl.

        IP接入控制。IP接入控制需输入有效的IP地址和子网掩码，IP和子网掩码间以\"|\"拼接组成一组，如果有多组用\";\"分隔。如：IP|掩码;IP|掩码;IP|掩码。

        :return: The ip_access_control of this AccessControl.
        :rtype: str
        """
        return self._ip_access_control

    @ip_access_control.setter
    def ip_access_control(self, ip_access_control):
        """Sets the ip_access_control of this AccessControl.

        IP接入控制。IP接入控制需输入有效的IP地址和子网掩码，IP和子网掩码间以\"|\"拼接组成一组，如果有多组用\";\"分隔。如：IP|掩码;IP|掩码;IP|掩码。

        :param ip_access_control: The ip_access_control of this AccessControl.
        :type ip_access_control: str
        """
        self._ip_access_control = ip_access_control

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
        if not isinstance(other, AccessControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

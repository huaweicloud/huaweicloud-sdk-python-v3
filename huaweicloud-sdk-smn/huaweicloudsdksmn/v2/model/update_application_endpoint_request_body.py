# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateApplicationEndpointRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enabled': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'user_data': 'user_data'
    }

    def __init__(self, enabled=None, user_data=None):
        """UpdateApplicationEndpointRequestBody

        The model defined in huaweicloud sdk

        :param enabled: 设备是否可用，值为true或false字符串。
        :type enabled: str
        :param user_data: 用户自定义数据，最大长度支持UTF-8编码后2048字节。
        :type user_data: str
        """
        
        

        self._enabled = None
        self._user_data = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if user_data is not None:
            self.user_data = user_data

    @property
    def enabled(self):
        """Gets the enabled of this UpdateApplicationEndpointRequestBody.

        设备是否可用，值为true或false字符串。

        :return: The enabled of this UpdateApplicationEndpointRequestBody.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateApplicationEndpointRequestBody.

        设备是否可用，值为true或false字符串。

        :param enabled: The enabled of this UpdateApplicationEndpointRequestBody.
        :type enabled: str
        """
        self._enabled = enabled

    @property
    def user_data(self):
        """Gets the user_data of this UpdateApplicationEndpointRequestBody.

        用户自定义数据，最大长度支持UTF-8编码后2048字节。

        :return: The user_data of this UpdateApplicationEndpointRequestBody.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this UpdateApplicationEndpointRequestBody.

        用户自定义数据，最大长度支持UTF-8编码后2048字节。

        :param user_data: The user_data of this UpdateApplicationEndpointRequestBody.
        :type user_data: str
        """
        self._user_data = user_data

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
        if not isinstance(other, UpdateApplicationEndpointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

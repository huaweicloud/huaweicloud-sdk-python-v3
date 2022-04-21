# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateApplicationEndpointRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'token': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'token': 'token',
        'user_data': 'user_data'
    }

    def __init__(self, token=None, user_data=None):
        """CreateApplicationEndpointRequestBody

        The model defined in huaweicloud sdk

        :param token: 移动应用设备token，最大长度512个字节。
        :type token: str
        :param user_data: 用户自定义数据，最大长度支持UTF-8编码后2048字节。
        :type user_data: str
        """
        
        

        self._token = None
        self._user_data = None
        self.discriminator = None

        self.token = token
        self.user_data = user_data

    @property
    def token(self):
        """Gets the token of this CreateApplicationEndpointRequestBody.

        移动应用设备token，最大长度512个字节。

        :return: The token of this CreateApplicationEndpointRequestBody.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CreateApplicationEndpointRequestBody.

        移动应用设备token，最大长度512个字节。

        :param token: The token of this CreateApplicationEndpointRequestBody.
        :type token: str
        """
        self._token = token

    @property
    def user_data(self):
        """Gets the user_data of this CreateApplicationEndpointRequestBody.

        用户自定义数据，最大长度支持UTF-8编码后2048字节。

        :return: The user_data of this CreateApplicationEndpointRequestBody.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateApplicationEndpointRequestBody.

        用户自定义数据，最大长度支持UTF-8编码后2048字节。

        :param user_data: The user_data of this CreateApplicationEndpointRequestBody.
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
        if not isinstance(other, CreateApplicationEndpointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

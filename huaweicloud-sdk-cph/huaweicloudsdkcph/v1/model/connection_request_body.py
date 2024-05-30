# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phone_ids': 'list[str]',
        'client_type': 'str'
    }

    attribute_map = {
        'phone_ids': 'phone_ids',
        'client_type': 'client_type'
    }

    def __init__(self, phone_ids=None, client_type=None):
        """ConnectionRequestBody

        The model defined in huaweicloud sdk

        :param phone_ids: phone_id数组，单次请求最大限制10
        :type phone_ids: list[str]
        :param client_type: 申请接入的客户端类型 - ANDROID: 安卓平台SDK - WINDOWS: Windows平台SDK - H5_MOBILE: H5移动端SDK - H5_PC: H5 PC端SDK - IOS: iOS平台SDK
        :type client_type: str
        """
        
        

        self._phone_ids = None
        self._client_type = None
        self.discriminator = None

        self.phone_ids = phone_ids
        self.client_type = client_type

    @property
    def phone_ids(self):
        """Gets the phone_ids of this ConnectionRequestBody.

        phone_id数组，单次请求最大限制10

        :return: The phone_ids of this ConnectionRequestBody.
        :rtype: list[str]
        """
        return self._phone_ids

    @phone_ids.setter
    def phone_ids(self, phone_ids):
        """Sets the phone_ids of this ConnectionRequestBody.

        phone_id数组，单次请求最大限制10

        :param phone_ids: The phone_ids of this ConnectionRequestBody.
        :type phone_ids: list[str]
        """
        self._phone_ids = phone_ids

    @property
    def client_type(self):
        """Gets the client_type of this ConnectionRequestBody.

        申请接入的客户端类型 - ANDROID: 安卓平台SDK - WINDOWS: Windows平台SDK - H5_MOBILE: H5移动端SDK - H5_PC: H5 PC端SDK - IOS: iOS平台SDK

        :return: The client_type of this ConnectionRequestBody.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this ConnectionRequestBody.

        申请接入的客户端类型 - ANDROID: 安卓平台SDK - WINDOWS: Windows平台SDK - H5_MOBILE: H5移动端SDK - H5_PC: H5 PC端SDK - IOS: iOS平台SDK

        :param client_type: The client_type of this ConnectionRequestBody.
        :type client_type: str
        """
        self._client_type = client_type

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
        if not isinstance(other, ConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

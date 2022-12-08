# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCredentialRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_auth_token')

    openapi_types = {
        'x_auth_token': 'str',
        'content_type': 'str'
    }

    attribute_map = {
        'x_auth_token': 'X-Auth-Token',
        'content_type': 'Content-Type'
    }

    def __init__(self, x_auth_token=None, content_type=None):
        """ShowCredentialRequest

        The model defined in huaweicloud sdk

        :param x_auth_token: IAM用户的token，无需特殊权限。
        :type x_auth_token: str
        :param content_type: 该字段填为“application/json;charset&#x3D;utf8”。
        :type content_type: str
        """
        
        

        self._x_auth_token = None
        self._content_type = None
        self.discriminator = None

        self.x_auth_token = x_auth_token
        self.content_type = content_type

    @property
    def x_auth_token(self):
        """Gets the x_auth_token of this ShowCredentialRequest.

        IAM用户的token，无需特殊权限。

        :return: The x_auth_token of this ShowCredentialRequest.
        :rtype: str
        """
        return self._x_auth_token

    @x_auth_token.setter
    def x_auth_token(self, x_auth_token):
        """Sets the x_auth_token of this ShowCredentialRequest.

        IAM用户的token，无需特殊权限。

        :param x_auth_token: The x_auth_token of this ShowCredentialRequest.
        :type x_auth_token: str
        """
        self._x_auth_token = x_auth_token

    @property
    def content_type(self):
        """Gets the content_type of this ShowCredentialRequest.

        该字段填为“application/json;charset=utf8”。

        :return: The content_type of this ShowCredentialRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ShowCredentialRequest.

        该字段填为“application/json;charset=utf8”。

        :param content_type: The content_type of this ShowCredentialRequest.
        :type content_type: str
        """
        self._content_type = content_type

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
        if not isinstance(other, ShowCredentialRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

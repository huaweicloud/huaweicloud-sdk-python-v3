# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecretResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auths': 'dict(str, AuthInfo)',
        'x_swr_dockerlogin': 'str'
    }

    attribute_map = {
        'auths': 'auths',
        'x_swr_dockerlogin': 'X-Swr-Dockerlogin'
    }

    def __init__(self, auths=None, x_swr_dockerlogin=None):
        """CreateSecretResponse

        The model defined in huaweicloud sdk

        :param auths: 认证信息
        :type auths: dict(str, AuthInfo)
        :param x_swr_dockerlogin: 
        :type x_swr_dockerlogin: str
        """
        
        super(CreateSecretResponse, self).__init__()

        self._auths = None
        self._x_swr_dockerlogin = None
        self.discriminator = None

        if auths is not None:
            self.auths = auths
        if x_swr_dockerlogin is not None:
            self.x_swr_dockerlogin = x_swr_dockerlogin

    @property
    def auths(self):
        """Gets the auths of this CreateSecretResponse.

        认证信息

        :return: The auths of this CreateSecretResponse.
        :rtype: dict(str, AuthInfo)
        """
        return self._auths

    @auths.setter
    def auths(self, auths):
        """Sets the auths of this CreateSecretResponse.

        认证信息

        :param auths: The auths of this CreateSecretResponse.
        :type auths: dict(str, AuthInfo)
        """
        self._auths = auths

    @property
    def x_swr_dockerlogin(self):
        """Gets the x_swr_dockerlogin of this CreateSecretResponse.

        :return: The x_swr_dockerlogin of this CreateSecretResponse.
        :rtype: str
        """
        return self._x_swr_dockerlogin

    @x_swr_dockerlogin.setter
    def x_swr_dockerlogin(self, x_swr_dockerlogin):
        """Sets the x_swr_dockerlogin of this CreateSecretResponse.

        :param x_swr_dockerlogin: The x_swr_dockerlogin of this CreateSecretResponse.
        :type x_swr_dockerlogin: str
        """
        self._x_swr_dockerlogin = x_swr_dockerlogin

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
        if not isinstance(other, CreateSecretResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

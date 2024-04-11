# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonRemoteAuth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remote_authentication': 'str',
        'remote_auth_rules': 'RemoteAuthRule'
    }

    attribute_map = {
        'remote_authentication': 'remote_authentication',
        'remote_auth_rules': 'remote_auth_rules'
    }

    def __init__(self, remote_authentication=None, remote_auth_rules=None):
        """CommonRemoteAuth

        The model defined in huaweicloud sdk

        :param remote_authentication: 是否开启远程鉴权(on：开启，off：关闭)。
        :type remote_authentication: str
        :param remote_auth_rules: 
        :type remote_auth_rules: :class:`huaweicloudsdkcdn.v2.RemoteAuthRule`
        """
        
        

        self._remote_authentication = None
        self._remote_auth_rules = None
        self.discriminator = None

        self.remote_authentication = remote_authentication
        self.remote_auth_rules = remote_auth_rules

    @property
    def remote_authentication(self):
        """Gets the remote_authentication of this CommonRemoteAuth.

        是否开启远程鉴权(on：开启，off：关闭)。

        :return: The remote_authentication of this CommonRemoteAuth.
        :rtype: str
        """
        return self._remote_authentication

    @remote_authentication.setter
    def remote_authentication(self, remote_authentication):
        """Sets the remote_authentication of this CommonRemoteAuth.

        是否开启远程鉴权(on：开启，off：关闭)。

        :param remote_authentication: The remote_authentication of this CommonRemoteAuth.
        :type remote_authentication: str
        """
        self._remote_authentication = remote_authentication

    @property
    def remote_auth_rules(self):
        """Gets the remote_auth_rules of this CommonRemoteAuth.

        :return: The remote_auth_rules of this CommonRemoteAuth.
        :rtype: :class:`huaweicloudsdkcdn.v2.RemoteAuthRule`
        """
        return self._remote_auth_rules

    @remote_auth_rules.setter
    def remote_auth_rules(self, remote_auth_rules):
        """Sets the remote_auth_rules of this CommonRemoteAuth.

        :param remote_auth_rules: The remote_auth_rules of this CommonRemoteAuth.
        :type remote_auth_rules: :class:`huaweicloudsdkcdn.v2.RemoteAuthRule`
        """
        self._remote_auth_rules = remote_auth_rules

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
        if not isinstance(other, CommonRemoteAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth': 'AuthObjectAuth',
        'scope': 'AuthObjectScope'
    }

    attribute_map = {
        'auth': 'auth',
        'scope': 'scope'
    }

    def __init__(self, auth=None, scope=None):
        r"""AuthObject

        The model defined in huaweicloud sdk

        :param auth: 
        :type auth: :class:`huaweicloudsdkcpcs.v1.AuthObjectAuth`
        :param scope: 
        :type scope: :class:`huaweicloudsdkcpcs.v1.AuthObjectScope`
        """
        
        

        self._auth = None
        self._scope = None
        self.discriminator = None

        if auth is not None:
            self.auth = auth
        if scope is not None:
            self.scope = scope

    @property
    def auth(self):
        r"""Gets the auth of this AuthObject.

        :return: The auth of this AuthObject.
        :rtype: :class:`huaweicloudsdkcpcs.v1.AuthObjectAuth`
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        r"""Sets the auth of this AuthObject.

        :param auth: The auth of this AuthObject.
        :type auth: :class:`huaweicloudsdkcpcs.v1.AuthObjectAuth`
        """
        self._auth = auth

    @property
    def scope(self):
        r"""Gets the scope of this AuthObject.

        :return: The scope of this AuthObject.
        :rtype: :class:`huaweicloudsdkcpcs.v1.AuthObjectScope`
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this AuthObject.

        :param scope: The scope of this AuthObject.
        :type scope: :class:`huaweicloudsdkcpcs.v1.AuthObjectScope`
        """
        self._scope = scope

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuthObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

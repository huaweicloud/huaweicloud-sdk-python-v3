# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteLoginConnectionNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'login': 'LoginInfo',
        'logout': 'LogoutInfo',
        'retry_login': 'RetryLoginInfo'
    }

    attribute_map = {
        'login': 'login',
        'logout': 'logout',
        'retry_login': 'retry_login'
    }

    def __init__(self, login=None, logout=None, retry_login=None):
        r"""ExecuteLoginConnectionNewRequestBody

        The model defined in huaweicloud sdk

        :param login: 
        :type login: :class:`huaweicloudsdkdas.v3.LoginInfo`
        :param logout: 
        :type logout: :class:`huaweicloudsdkdas.v3.LogoutInfo`
        :param retry_login: 
        :type retry_login: :class:`huaweicloudsdkdas.v3.RetryLoginInfo`
        """
        
        

        self._login = None
        self._logout = None
        self._retry_login = None
        self.discriminator = None

        if login is not None:
            self.login = login
        if logout is not None:
            self.logout = logout
        if retry_login is not None:
            self.retry_login = retry_login

    @property
    def login(self):
        r"""Gets the login of this ExecuteLoginConnectionNewRequestBody.

        :return: The login of this ExecuteLoginConnectionNewRequestBody.
        :rtype: :class:`huaweicloudsdkdas.v3.LoginInfo`
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this ExecuteLoginConnectionNewRequestBody.

        :param login: The login of this ExecuteLoginConnectionNewRequestBody.
        :type login: :class:`huaweicloudsdkdas.v3.LoginInfo`
        """
        self._login = login

    @property
    def logout(self):
        r"""Gets the logout of this ExecuteLoginConnectionNewRequestBody.

        :return: The logout of this ExecuteLoginConnectionNewRequestBody.
        :rtype: :class:`huaweicloudsdkdas.v3.LogoutInfo`
        """
        return self._logout

    @logout.setter
    def logout(self, logout):
        r"""Sets the logout of this ExecuteLoginConnectionNewRequestBody.

        :param logout: The logout of this ExecuteLoginConnectionNewRequestBody.
        :type logout: :class:`huaweicloudsdkdas.v3.LogoutInfo`
        """
        self._logout = logout

    @property
    def retry_login(self):
        r"""Gets the retry_login of this ExecuteLoginConnectionNewRequestBody.

        :return: The retry_login of this ExecuteLoginConnectionNewRequestBody.
        :rtype: :class:`huaweicloudsdkdas.v3.RetryLoginInfo`
        """
        return self._retry_login

    @retry_login.setter
    def retry_login(self, retry_login):
        r"""Sets the retry_login of this ExecuteLoginConnectionNewRequestBody.

        :param retry_login: The retry_login of this ExecuteLoginConnectionNewRequestBody.
        :type retry_login: :class:`huaweicloudsdkdas.v3.RetryLoginInfo`
        """
        self._retry_login = retry_login

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
        if not isinstance(other, ExecuteLoginConnectionNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

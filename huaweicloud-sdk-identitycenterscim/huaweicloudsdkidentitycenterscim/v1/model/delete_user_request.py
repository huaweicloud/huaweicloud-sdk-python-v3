# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteUserRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization': 'str',
        'tenant_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'tenant_id': 'tenant_id',
        'user_id': 'user_id'
    }

    def __init__(self, authorization=None, tenant_id=None, user_id=None):
        r"""DeleteUserRequest

        The model defined in huaweicloud sdk

        :param authorization: 承载令牌
        :type authorization: str
        :param tenant_id: 租户的全局唯一标识符（ID）
        :type tenant_id: str
        :param user_id: 用户的全局唯一标识符（ID）
        :type user_id: str
        """
        
        

        self._authorization = None
        self._tenant_id = None
        self._user_id = None
        self.discriminator = None

        self.authorization = authorization
        self.tenant_id = tenant_id
        self.user_id = user_id

    @property
    def authorization(self):
        r"""Gets the authorization of this DeleteUserRequest.

        承载令牌

        :return: The authorization of this DeleteUserRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this DeleteUserRequest.

        承载令牌

        :param authorization: The authorization of this DeleteUserRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this DeleteUserRequest.

        租户的全局唯一标识符（ID）

        :return: The tenant_id of this DeleteUserRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this DeleteUserRequest.

        租户的全局唯一标识符（ID）

        :param tenant_id: The tenant_id of this DeleteUserRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def user_id(self):
        r"""Gets the user_id of this DeleteUserRequest.

        用户的全局唯一标识符（ID）

        :return: The user_id of this DeleteUserRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this DeleteUserRequest.

        用户的全局唯一标识符（ID）

        :param user_id: The user_id of this DeleteUserRequest.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, DeleteUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchUserRequest:

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
        'user_id': 'str',
        'body': 'PatchUserReqBody'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'tenant_id': 'tenant_id',
        'user_id': 'user_id',
        'body': 'body'
    }

    def __init__(self, authorization=None, tenant_id=None, user_id=None, body=None):
        """PatchUserRequest

        The model defined in huaweicloud sdk

        :param authorization: 承载令牌
        :type authorization: str
        :param tenant_id: 租户的全局唯一标识符（ID）
        :type tenant_id: str
        :param user_id: 用户的全局唯一标识符（ID）
        :type user_id: str
        :param body: Body of the PatchUserRequest
        :type body: :class:`huaweicloudsdkidentitycenterscim.v1.PatchUserReqBody`
        """
        
        

        self._authorization = None
        self._tenant_id = None
        self._user_id = None
        self._body = None
        self.discriminator = None

        self.authorization = authorization
        self.tenant_id = tenant_id
        self.user_id = user_id
        if body is not None:
            self.body = body

    @property
    def authorization(self):
        """Gets the authorization of this PatchUserRequest.

        承载令牌

        :return: The authorization of this PatchUserRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this PatchUserRequest.

        承载令牌

        :param authorization: The authorization of this PatchUserRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def tenant_id(self):
        """Gets the tenant_id of this PatchUserRequest.

        租户的全局唯一标识符（ID）

        :return: The tenant_id of this PatchUserRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this PatchUserRequest.

        租户的全局唯一标识符（ID）

        :param tenant_id: The tenant_id of this PatchUserRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def user_id(self):
        """Gets the user_id of this PatchUserRequest.

        用户的全局唯一标识符（ID）

        :return: The user_id of this PatchUserRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PatchUserRequest.

        用户的全局唯一标识符（ID）

        :param user_id: The user_id of this PatchUserRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def body(self):
        """Gets the body of this PatchUserRequest.

        :return: The body of this PatchUserRequest.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.PatchUserReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PatchUserRequest.

        :param body: The body of this PatchUserRequest.
        :type body: :class:`huaweicloudsdkidentitycenterscim.v1.PatchUserReqBody`
        """
        self._body = body

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
        if not isinstance(other, PatchUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'identity_store_id': 'str',
        'user_id': 'str',
        'body': 'UpdateUserReqBody'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'identity_store_id': 'identity_store_id',
        'user_id': 'user_id',
        'body': 'body'
    }

    def __init__(self, x_security_token=None, identity_store_id=None, user_id=None, body=None):
        """UpdateUserRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param user_id: 身份源中IAM身份中心用户的全局唯一标识符（ID）
        :type user_id: str
        :param body: Body of the UpdateUserRequest
        :type body: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateUserReqBody`
        """
        
        

        self._x_security_token = None
        self._identity_store_id = None
        self._user_id = None
        self._body = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.identity_store_id = identity_store_id
        self.user_id = user_id
        if body is not None:
            self.body = body

    @property
    def x_security_token(self):
        """Gets the x_security_token of this UpdateUserRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this UpdateUserRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this UpdateUserRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this UpdateUserRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def identity_store_id(self):
        """Gets the identity_store_id of this UpdateUserRequest.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this UpdateUserRequest.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        """Sets the identity_store_id of this UpdateUserRequest.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this UpdateUserRequest.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def user_id(self):
        """Gets the user_id of this UpdateUserRequest.

        身份源中IAM身份中心用户的全局唯一标识符（ID）

        :return: The user_id of this UpdateUserRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UpdateUserRequest.

        身份源中IAM身份中心用户的全局唯一标识符（ID）

        :param user_id: The user_id of this UpdateUserRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def body(self):
        """Gets the body of this UpdateUserRequest.

        :return: The body of this UpdateUserRequest.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateUserReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateUserRequest.

        :param body: The body of this UpdateUserRequest.
        :type body: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateUserReqBody`
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
        if not isinstance(other, UpdateUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

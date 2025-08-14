# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMfaDeviceForUserRequest:

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
        'device_id': 'str',
        'body': 'UpdateMfaDeviceForUserReqBody'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'identity_store_id': 'identity_store_id',
        'user_id': 'user_id',
        'device_id': 'device_id',
        'body': 'body'
    }

    def __init__(self, x_security_token=None, identity_store_id=None, user_id=None, device_id=None, body=None):
        r"""UpdateMfaDeviceForUserRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param user_id: 身份源中IdentityCenter用户的全局唯一标识符（ID）
        :type user_id: str
        :param device_id: MFA设备ID
        :type device_id: str
        :param body: Body of the UpdateMfaDeviceForUserRequest
        :type body: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateMfaDeviceForUserReqBody`
        """
        
        

        self._x_security_token = None
        self._identity_store_id = None
        self._user_id = None
        self._device_id = None
        self._body = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.identity_store_id = identity_store_id
        self.user_id = user_id
        self.device_id = device_id
        if body is not None:
            self.body = body

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this UpdateMfaDeviceForUserRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this UpdateMfaDeviceForUserRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this UpdateMfaDeviceForUserRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this UpdateMfaDeviceForUserRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this UpdateMfaDeviceForUserRequest.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this UpdateMfaDeviceForUserRequest.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this UpdateMfaDeviceForUserRequest.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this UpdateMfaDeviceForUserRequest.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def user_id(self):
        r"""Gets the user_id of this UpdateMfaDeviceForUserRequest.

        身份源中IdentityCenter用户的全局唯一标识符（ID）

        :return: The user_id of this UpdateMfaDeviceForUserRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UpdateMfaDeviceForUserRequest.

        身份源中IdentityCenter用户的全局唯一标识符（ID）

        :param user_id: The user_id of this UpdateMfaDeviceForUserRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def device_id(self):
        r"""Gets the device_id of this UpdateMfaDeviceForUserRequest.

        MFA设备ID

        :return: The device_id of this UpdateMfaDeviceForUserRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this UpdateMfaDeviceForUserRequest.

        MFA设备ID

        :param device_id: The device_id of this UpdateMfaDeviceForUserRequest.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def body(self):
        r"""Gets the body of this UpdateMfaDeviceForUserRequest.

        :return: The body of this UpdateMfaDeviceForUserRequest.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateMfaDeviceForUserReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateMfaDeviceForUserRequest.

        :param body: The body of this UpdateMfaDeviceForUserRequest.
        :type body: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateMfaDeviceForUserReqBody`
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
        if not isinstance(other, UpdateMfaDeviceForUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

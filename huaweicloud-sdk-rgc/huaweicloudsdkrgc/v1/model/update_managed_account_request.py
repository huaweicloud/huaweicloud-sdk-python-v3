# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateManagedAccountRequest:

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
        'managed_account_id': 'str',
        'x_security_token': 'str',
        'body': 'CreateManagedAccountRequest'
    }

    attribute_map = {
        'managed_account_id': 'managed_account_id',
        'x_security_token': 'X-Security-Token',
        'body': 'body'
    }

    def __init__(self, managed_account_id=None, x_security_token=None, body=None):
        """UpdateManagedAccountRequest

        The model defined in huaweicloud sdk

        :param managed_account_id: 账号ID。
        :type managed_account_id: str
        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param body: Body of the UpdateManagedAccountRequest
        :type body: :class:`huaweicloudsdkrgc.v1.CreateManagedAccountRequest`
        """
        
        

        self._managed_account_id = None
        self._x_security_token = None
        self._body = None
        self.discriminator = None

        self.managed_account_id = managed_account_id
        if x_security_token is not None:
            self.x_security_token = x_security_token
        if body is not None:
            self.body = body

    @property
    def managed_account_id(self):
        """Gets the managed_account_id of this UpdateManagedAccountRequest.

        账号ID。

        :return: The managed_account_id of this UpdateManagedAccountRequest.
        :rtype: str
        """
        return self._managed_account_id

    @managed_account_id.setter
    def managed_account_id(self, managed_account_id):
        """Sets the managed_account_id of this UpdateManagedAccountRequest.

        账号ID。

        :param managed_account_id: The managed_account_id of this UpdateManagedAccountRequest.
        :type managed_account_id: str
        """
        self._managed_account_id = managed_account_id

    @property
    def x_security_token(self):
        """Gets the x_security_token of this UpdateManagedAccountRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this UpdateManagedAccountRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this UpdateManagedAccountRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this UpdateManagedAccountRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def body(self):
        """Gets the body of this UpdateManagedAccountRequest.

        :return: The body of this UpdateManagedAccountRequest.
        :rtype: :class:`huaweicloudsdkrgc.v1.CreateManagedAccountRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateManagedAccountRequest.

        :param body: The body of this UpdateManagedAccountRequest.
        :type body: :class:`huaweicloudsdkrgc.v1.CreateManagedAccountRequest`
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
        if not isinstance(other, UpdateManagedAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

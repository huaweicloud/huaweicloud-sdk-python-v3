# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccountRequest:

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
        'account_id': 'str',
        'body': 'UpdateAccountReqBody'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'account_id': 'account_id',
        'body': 'body'
    }

    def __init__(self, x_security_token=None, account_id=None, body=None):
        r"""UpdateAccountRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param account_id: 账号的唯一标识符（ID）。
        :type account_id: str
        :param body: Body of the UpdateAccountRequest
        :type body: :class:`huaweicloudsdkorganizations.v1.UpdateAccountReqBody`
        """
        
        

        self._x_security_token = None
        self._account_id = None
        self._body = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.account_id = account_id
        if body is not None:
            self.body = body

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this UpdateAccountRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this UpdateAccountRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this UpdateAccountRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this UpdateAccountRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def account_id(self):
        r"""Gets the account_id of this UpdateAccountRequest.

        账号的唯一标识符（ID）。

        :return: The account_id of this UpdateAccountRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this UpdateAccountRequest.

        账号的唯一标识符（ID）。

        :param account_id: The account_id of this UpdateAccountRequest.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAccountRequest.

        :return: The body of this UpdateAccountRequest.
        :rtype: :class:`huaweicloudsdkorganizations.v1.UpdateAccountReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAccountRequest.

        :param body: The body of this UpdateAccountRequest.
        :type body: :class:`huaweicloudsdkorganizations.v1.UpdateAccountReqBody`
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
        if not isinstance(other, UpdateAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

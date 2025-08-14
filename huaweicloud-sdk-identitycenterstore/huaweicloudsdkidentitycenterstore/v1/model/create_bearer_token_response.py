# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBearerTokenResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creation_time': 'float',
        'expiration_time': 'float',
        'token': 'str',
        'token_id': 'str'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'expiration_time': 'expiration_time',
        'token': 'token',
        'token_id': 'token_id'
    }

    def __init__(self, creation_time=None, expiration_time=None, token=None, token_id=None):
        r"""CreateBearerTokenResponse

        The model defined in huaweicloud sdk

        :param creation_time: 创建时间
        :type creation_time: float
        :param expiration_time: 过期时间
        :type expiration_time: float
        :param token: 访问令牌
        :type token: str
        :param token_id: 访问令牌的全局唯一标识符（ID）
        :type token_id: str
        """
        
        super(CreateBearerTokenResponse, self).__init__()

        self._creation_time = None
        self._expiration_time = None
        self._token = None
        self._token_id = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if token is not None:
            self.token = token
        if token_id is not None:
            self.token_id = token_id

    @property
    def creation_time(self):
        r"""Gets the creation_time of this CreateBearerTokenResponse.

        创建时间

        :return: The creation_time of this CreateBearerTokenResponse.
        :rtype: float
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this CreateBearerTokenResponse.

        创建时间

        :param creation_time: The creation_time of this CreateBearerTokenResponse.
        :type creation_time: float
        """
        self._creation_time = creation_time

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this CreateBearerTokenResponse.

        过期时间

        :return: The expiration_time of this CreateBearerTokenResponse.
        :rtype: float
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this CreateBearerTokenResponse.

        过期时间

        :param expiration_time: The expiration_time of this CreateBearerTokenResponse.
        :type expiration_time: float
        """
        self._expiration_time = expiration_time

    @property
    def token(self):
        r"""Gets the token of this CreateBearerTokenResponse.

        访问令牌

        :return: The token of this CreateBearerTokenResponse.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this CreateBearerTokenResponse.

        访问令牌

        :param token: The token of this CreateBearerTokenResponse.
        :type token: str
        """
        self._token = token

    @property
    def token_id(self):
        r"""Gets the token_id of this CreateBearerTokenResponse.

        访问令牌的全局唯一标识符（ID）

        :return: The token_id of this CreateBearerTokenResponse.
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        r"""Sets the token_id of this CreateBearerTokenResponse.

        访问令牌的全局唯一标识符（ID）

        :param token_id: The token_id of this CreateBearerTokenResponse.
        :type token_id: str
        """
        self._token_id = token_id

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
        if not isinstance(other, CreateBearerTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

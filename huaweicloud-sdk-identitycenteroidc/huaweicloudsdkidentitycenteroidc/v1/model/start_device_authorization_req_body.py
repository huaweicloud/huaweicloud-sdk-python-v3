# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartDeviceAuthorizationReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_id': 'str',
        'client_secret': 'str',
        'start_url': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'start_url': 'start_url'
    }

    def __init__(self, client_id=None, client_secret=None, start_url=None):
        r"""StartDeviceAuthorizationReqBody

        The model defined in huaweicloud sdk

        :param client_id: 在IAM身份中心注册的客户端的唯一标识符
        :type client_id: str
        :param client_secret: 为客户端生成的秘密字符串。客户端将使用此字符串在后续调用中获得服务的身份验证
        :type client_secret: str
        :param start_url: 访问门户的URL
        :type start_url: str
        """
        
        

        self._client_id = None
        self._client_secret = None
        self._start_url = None
        self.discriminator = None

        self.client_id = client_id
        self.client_secret = client_secret
        self.start_url = start_url

    @property
    def client_id(self):
        r"""Gets the client_id of this StartDeviceAuthorizationReqBody.

        在IAM身份中心注册的客户端的唯一标识符

        :return: The client_id of this StartDeviceAuthorizationReqBody.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this StartDeviceAuthorizationReqBody.

        在IAM身份中心注册的客户端的唯一标识符

        :param client_id: The client_id of this StartDeviceAuthorizationReqBody.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        r"""Gets the client_secret of this StartDeviceAuthorizationReqBody.

        为客户端生成的秘密字符串。客户端将使用此字符串在后续调用中获得服务的身份验证

        :return: The client_secret of this StartDeviceAuthorizationReqBody.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        r"""Sets the client_secret of this StartDeviceAuthorizationReqBody.

        为客户端生成的秘密字符串。客户端将使用此字符串在后续调用中获得服务的身份验证

        :param client_secret: The client_secret of this StartDeviceAuthorizationReqBody.
        :type client_secret: str
        """
        self._client_secret = client_secret

    @property
    def start_url(self):
        r"""Gets the start_url of this StartDeviceAuthorizationReqBody.

        访问门户的URL

        :return: The start_url of this StartDeviceAuthorizationReqBody.
        :rtype: str
        """
        return self._start_url

    @start_url.setter
    def start_url(self, start_url):
        r"""Sets the start_url of this StartDeviceAuthorizationReqBody.

        访问门户的URL

        :param start_url: The start_url of this StartDeviceAuthorizationReqBody.
        :type start_url: str
        """
        self._start_url = start_url

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
        if not isinstance(other, StartDeviceAuthorizationReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartDeviceAuthorizationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_code': 'str',
        'expires_in': 'int',
        'interval': 'int',
        'user_code': 'str',
        'verification_uri': 'str',
        'verification_uri_complete': 'str'
    }

    attribute_map = {
        'device_code': 'device_code',
        'expires_in': 'expires_in',
        'interval': 'interval',
        'user_code': 'user_code',
        'verification_uri': 'verification_uri',
        'verification_uri_complete': 'verification_uri_complete'
    }

    def __init__(self, device_code=None, expires_in=None, interval=None, user_code=None, verification_uri=None, verification_uri_complete=None):
        r"""StartDeviceAuthorizationResponse

        The model defined in huaweicloud sdk

        :param device_code: 设备在轮询会话令牌时使用的设备码
        :type device_code: str
        :param expires_in: 设备码失效时间（以秒为单位）
        :type expires_in: int
        :param interval: 指示轮询会话时，客户端在两次尝试之间必须等待的秒数
        :type interval: int
        :param user_code: 一次性用户验证码。授权正在使用的设备时需要此操作
        :type user_code: str
        :param verification_uri: 使用一次性用户验证码授权设备的验证页面的URI
        :type verification_uri: str
        :param verification_uri_complete: 客户端可用于自动启动浏览器的备用URL。此过程跳过用户访问验证页面并输入代码的手动步骤
        :type verification_uri_complete: str
        """
        
        super(StartDeviceAuthorizationResponse, self).__init__()

        self._device_code = None
        self._expires_in = None
        self._interval = None
        self._user_code = None
        self._verification_uri = None
        self._verification_uri_complete = None
        self.discriminator = None

        if device_code is not None:
            self.device_code = device_code
        if expires_in is not None:
            self.expires_in = expires_in
        if interval is not None:
            self.interval = interval
        if user_code is not None:
            self.user_code = user_code
        if verification_uri is not None:
            self.verification_uri = verification_uri
        if verification_uri_complete is not None:
            self.verification_uri_complete = verification_uri_complete

    @property
    def device_code(self):
        r"""Gets the device_code of this StartDeviceAuthorizationResponse.

        设备在轮询会话令牌时使用的设备码

        :return: The device_code of this StartDeviceAuthorizationResponse.
        :rtype: str
        """
        return self._device_code

    @device_code.setter
    def device_code(self, device_code):
        r"""Sets the device_code of this StartDeviceAuthorizationResponse.

        设备在轮询会话令牌时使用的设备码

        :param device_code: The device_code of this StartDeviceAuthorizationResponse.
        :type device_code: str
        """
        self._device_code = device_code

    @property
    def expires_in(self):
        r"""Gets the expires_in of this StartDeviceAuthorizationResponse.

        设备码失效时间（以秒为单位）

        :return: The expires_in of this StartDeviceAuthorizationResponse.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        r"""Sets the expires_in of this StartDeviceAuthorizationResponse.

        设备码失效时间（以秒为单位）

        :param expires_in: The expires_in of this StartDeviceAuthorizationResponse.
        :type expires_in: int
        """
        self._expires_in = expires_in

    @property
    def interval(self):
        r"""Gets the interval of this StartDeviceAuthorizationResponse.

        指示轮询会话时，客户端在两次尝试之间必须等待的秒数

        :return: The interval of this StartDeviceAuthorizationResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this StartDeviceAuthorizationResponse.

        指示轮询会话时，客户端在两次尝试之间必须等待的秒数

        :param interval: The interval of this StartDeviceAuthorizationResponse.
        :type interval: int
        """
        self._interval = interval

    @property
    def user_code(self):
        r"""Gets the user_code of this StartDeviceAuthorizationResponse.

        一次性用户验证码。授权正在使用的设备时需要此操作

        :return: The user_code of this StartDeviceAuthorizationResponse.
        :rtype: str
        """
        return self._user_code

    @user_code.setter
    def user_code(self, user_code):
        r"""Sets the user_code of this StartDeviceAuthorizationResponse.

        一次性用户验证码。授权正在使用的设备时需要此操作

        :param user_code: The user_code of this StartDeviceAuthorizationResponse.
        :type user_code: str
        """
        self._user_code = user_code

    @property
    def verification_uri(self):
        r"""Gets the verification_uri of this StartDeviceAuthorizationResponse.

        使用一次性用户验证码授权设备的验证页面的URI

        :return: The verification_uri of this StartDeviceAuthorizationResponse.
        :rtype: str
        """
        return self._verification_uri

    @verification_uri.setter
    def verification_uri(self, verification_uri):
        r"""Sets the verification_uri of this StartDeviceAuthorizationResponse.

        使用一次性用户验证码授权设备的验证页面的URI

        :param verification_uri: The verification_uri of this StartDeviceAuthorizationResponse.
        :type verification_uri: str
        """
        self._verification_uri = verification_uri

    @property
    def verification_uri_complete(self):
        r"""Gets the verification_uri_complete of this StartDeviceAuthorizationResponse.

        客户端可用于自动启动浏览器的备用URL。此过程跳过用户访问验证页面并输入代码的手动步骤

        :return: The verification_uri_complete of this StartDeviceAuthorizationResponse.
        :rtype: str
        """
        return self._verification_uri_complete

    @verification_uri_complete.setter
    def verification_uri_complete(self, verification_uri_complete):
        r"""Sets the verification_uri_complete of this StartDeviceAuthorizationResponse.

        客户端可用于自动启动浏览器的备用URL。此过程跳过用户访问验证页面并输入代码的手动步骤

        :param verification_uri_complete: The verification_uri_complete of this StartDeviceAuthorizationResponse.
        :type verification_uri_complete: str
        """
        self._verification_uri_complete = verification_uri_complete

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
        if not isinstance(other, StartDeviceAuthorizationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

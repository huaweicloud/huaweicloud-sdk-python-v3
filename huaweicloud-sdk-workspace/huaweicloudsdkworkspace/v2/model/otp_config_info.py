# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OtpConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'receive_mode': 'ReceiveModeEnum',
        'auth_url': 'str',
        'app_id': 'str',
        'app_secret': 'str',
        'auth_server_access_mode': 'AuthServerAccessMode',
        'cert_content': 'str',
        'apply_rule': 'ApplyRuleInfo'
    }

    attribute_map = {
        'enable': 'enable',
        'receive_mode': 'receive_mode',
        'auth_url': 'auth_url',
        'app_id': 'app_id',
        'app_secret': 'app_secret',
        'auth_server_access_mode': 'auth_server_access_mode',
        'cert_content': 'cert_content',
        'apply_rule': 'apply_rule'
    }

    def __init__(self, enable=None, receive_mode=None, auth_url=None, app_id=None, app_secret=None, auth_server_access_mode=None, cert_content=None, apply_rule=None):
        """OtpConfigInfo

        The model defined in huaweicloud sdk

        :param enable: 是否启用
        :type enable: bool
        :param receive_mode: 
        :type receive_mode: :class:`huaweicloudsdkworkspace.v2.ReceiveModeEnum`
        :param auth_url: 辅助认证服务器地址
        :type auth_url: str
        :param app_id: 认证服务接入账号
        :type app_id: str
        :param app_secret: 认证服务接入密码
        :type app_secret: str
        :param auth_server_access_mode: 
        :type auth_server_access_mode: :class:`huaweicloudsdkworkspace.v2.AuthServerAccessMode`
        :param cert_content: pem格式证书内容
        :type cert_content: str
        :param apply_rule: 
        :type apply_rule: :class:`huaweicloudsdkworkspace.v2.ApplyRuleInfo`
        """
        
        

        self._enable = None
        self._receive_mode = None
        self._auth_url = None
        self._app_id = None
        self._app_secret = None
        self._auth_server_access_mode = None
        self._cert_content = None
        self._apply_rule = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if receive_mode is not None:
            self.receive_mode = receive_mode
        if auth_url is not None:
            self.auth_url = auth_url
        if app_id is not None:
            self.app_id = app_id
        if app_secret is not None:
            self.app_secret = app_secret
        if auth_server_access_mode is not None:
            self.auth_server_access_mode = auth_server_access_mode
        if cert_content is not None:
            self.cert_content = cert_content
        if apply_rule is not None:
            self.apply_rule = apply_rule

    @property
    def enable(self):
        """Gets the enable of this OtpConfigInfo.

        是否启用

        :return: The enable of this OtpConfigInfo.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this OtpConfigInfo.

        是否启用

        :param enable: The enable of this OtpConfigInfo.
        :type enable: bool
        """
        self._enable = enable

    @property
    def receive_mode(self):
        """Gets the receive_mode of this OtpConfigInfo.

        :return: The receive_mode of this OtpConfigInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ReceiveModeEnum`
        """
        return self._receive_mode

    @receive_mode.setter
    def receive_mode(self, receive_mode):
        """Sets the receive_mode of this OtpConfigInfo.

        :param receive_mode: The receive_mode of this OtpConfigInfo.
        :type receive_mode: :class:`huaweicloudsdkworkspace.v2.ReceiveModeEnum`
        """
        self._receive_mode = receive_mode

    @property
    def auth_url(self):
        """Gets the auth_url of this OtpConfigInfo.

        辅助认证服务器地址

        :return: The auth_url of this OtpConfigInfo.
        :rtype: str
        """
        return self._auth_url

    @auth_url.setter
    def auth_url(self, auth_url):
        """Sets the auth_url of this OtpConfigInfo.

        辅助认证服务器地址

        :param auth_url: The auth_url of this OtpConfigInfo.
        :type auth_url: str
        """
        self._auth_url = auth_url

    @property
    def app_id(self):
        """Gets the app_id of this OtpConfigInfo.

        认证服务接入账号

        :return: The app_id of this OtpConfigInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this OtpConfigInfo.

        认证服务接入账号

        :param app_id: The app_id of this OtpConfigInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_secret(self):
        """Gets the app_secret of this OtpConfigInfo.

        认证服务接入密码

        :return: The app_secret of this OtpConfigInfo.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this OtpConfigInfo.

        认证服务接入密码

        :param app_secret: The app_secret of this OtpConfigInfo.
        :type app_secret: str
        """
        self._app_secret = app_secret

    @property
    def auth_server_access_mode(self):
        """Gets the auth_server_access_mode of this OtpConfigInfo.

        :return: The auth_server_access_mode of this OtpConfigInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AuthServerAccessMode`
        """
        return self._auth_server_access_mode

    @auth_server_access_mode.setter
    def auth_server_access_mode(self, auth_server_access_mode):
        """Sets the auth_server_access_mode of this OtpConfigInfo.

        :param auth_server_access_mode: The auth_server_access_mode of this OtpConfigInfo.
        :type auth_server_access_mode: :class:`huaweicloudsdkworkspace.v2.AuthServerAccessMode`
        """
        self._auth_server_access_mode = auth_server_access_mode

    @property
    def cert_content(self):
        """Gets the cert_content of this OtpConfigInfo.

        pem格式证书内容

        :return: The cert_content of this OtpConfigInfo.
        :rtype: str
        """
        return self._cert_content

    @cert_content.setter
    def cert_content(self, cert_content):
        """Sets the cert_content of this OtpConfigInfo.

        pem格式证书内容

        :param cert_content: The cert_content of this OtpConfigInfo.
        :type cert_content: str
        """
        self._cert_content = cert_content

    @property
    def apply_rule(self):
        """Gets the apply_rule of this OtpConfigInfo.

        :return: The apply_rule of this OtpConfigInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApplyRuleInfo`
        """
        return self._apply_rule

    @apply_rule.setter
    def apply_rule(self, apply_rule):
        """Sets the apply_rule of this OtpConfigInfo.

        :param apply_rule: The apply_rule of this OtpConfigInfo.
        :type apply_rule: :class:`huaweicloudsdkworkspace.v2.ApplyRuleInfo`
        """
        self._apply_rule = apply_rule

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
        if not isinstance(other, OtpConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

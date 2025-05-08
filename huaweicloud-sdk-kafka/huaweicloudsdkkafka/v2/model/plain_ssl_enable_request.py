# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlainSslEnableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'enable': 'bool',
        'user_name': 'str',
        'pass_word': 'str',
        'sasl_enabled_mechanisms': 'list[str]'
    }

    attribute_map = {
        'protocol': 'protocol',
        'enable': 'enable',
        'user_name': 'user_name',
        'pass_word': 'pass_word',
        'sasl_enabled_mechanisms': 'sasl_enabled_mechanisms'
    }

    def __init__(self, protocol=None, enable=None, user_name=None, pass_word=None, sasl_enabled_mechanisms=None):
        r"""PlainSslEnableRequest

        The model defined in huaweicloud sdk

        :param protocol: 需要开启或者关闭的接入方式。
        :type protocol: str
        :param enable: - true：开启指定的接入方式。 - false：关闭指定的接入方式。
        :type enable: bool
        :param user_name: 首次开启SASL时，需要输入用户名。 实例创建后，关闭SASL并不会删除已经创建的用户，再次开启SASL时无需传入用户名，传入的用户名将无效。
        :type user_name: str
        :param pass_word: 首次开启SASL时，需要输入用户名的密码。
        :type pass_word: str
        :param sasl_enabled_mechanisms: 开启SASL后使用的认证机制。仅在第一次开启SASL时传入生效。生效后再次传入无效。 - PLAIN：简单的用户名密码校验。 - SCRAM-SHA-512：用户凭证校验，安全性比PLAIN机制更高。
        :type sasl_enabled_mechanisms: list[str]
        """
        
        

        self._protocol = None
        self._enable = None
        self._user_name = None
        self._pass_word = None
        self._sasl_enabled_mechanisms = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if enable is not None:
            self.enable = enable
        if user_name is not None:
            self.user_name = user_name
        if pass_word is not None:
            self.pass_word = pass_word
        if sasl_enabled_mechanisms is not None:
            self.sasl_enabled_mechanisms = sasl_enabled_mechanisms

    @property
    def protocol(self):
        r"""Gets the protocol of this PlainSslEnableRequest.

        需要开启或者关闭的接入方式。

        :return: The protocol of this PlainSslEnableRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this PlainSslEnableRequest.

        需要开启或者关闭的接入方式。

        :param protocol: The protocol of this PlainSslEnableRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def enable(self):
        r"""Gets the enable of this PlainSslEnableRequest.

        - true：开启指定的接入方式。 - false：关闭指定的接入方式。

        :return: The enable of this PlainSslEnableRequest.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this PlainSslEnableRequest.

        - true：开启指定的接入方式。 - false：关闭指定的接入方式。

        :param enable: The enable of this PlainSslEnableRequest.
        :type enable: bool
        """
        self._enable = enable

    @property
    def user_name(self):
        r"""Gets the user_name of this PlainSslEnableRequest.

        首次开启SASL时，需要输入用户名。 实例创建后，关闭SASL并不会删除已经创建的用户，再次开启SASL时无需传入用户名，传入的用户名将无效。

        :return: The user_name of this PlainSslEnableRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this PlainSslEnableRequest.

        首次开启SASL时，需要输入用户名。 实例创建后，关闭SASL并不会删除已经创建的用户，再次开启SASL时无需传入用户名，传入的用户名将无效。

        :param user_name: The user_name of this PlainSslEnableRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def pass_word(self):
        r"""Gets the pass_word of this PlainSslEnableRequest.

        首次开启SASL时，需要输入用户名的密码。

        :return: The pass_word of this PlainSslEnableRequest.
        :rtype: str
        """
        return self._pass_word

    @pass_word.setter
    def pass_word(self, pass_word):
        r"""Sets the pass_word of this PlainSslEnableRequest.

        首次开启SASL时，需要输入用户名的密码。

        :param pass_word: The pass_word of this PlainSslEnableRequest.
        :type pass_word: str
        """
        self._pass_word = pass_word

    @property
    def sasl_enabled_mechanisms(self):
        r"""Gets the sasl_enabled_mechanisms of this PlainSslEnableRequest.

        开启SASL后使用的认证机制。仅在第一次开启SASL时传入生效。生效后再次传入无效。 - PLAIN：简单的用户名密码校验。 - SCRAM-SHA-512：用户凭证校验，安全性比PLAIN机制更高。

        :return: The sasl_enabled_mechanisms of this PlainSslEnableRequest.
        :rtype: list[str]
        """
        return self._sasl_enabled_mechanisms

    @sasl_enabled_mechanisms.setter
    def sasl_enabled_mechanisms(self, sasl_enabled_mechanisms):
        r"""Sets the sasl_enabled_mechanisms of this PlainSslEnableRequest.

        开启SASL后使用的认证机制。仅在第一次开启SASL时传入生效。生效后再次传入无效。 - PLAIN：简单的用户名密码校验。 - SCRAM-SHA-512：用户凭证校验，安全性比PLAIN机制更高。

        :param sasl_enabled_mechanisms: The sasl_enabled_mechanisms of this PlainSslEnableRequest.
        :type sasl_enabled_mechanisms: list[str]
        """
        self._sasl_enabled_mechanisms = sasl_enabled_mechanisms

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
        if not isinstance(other, PlainSslEnableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

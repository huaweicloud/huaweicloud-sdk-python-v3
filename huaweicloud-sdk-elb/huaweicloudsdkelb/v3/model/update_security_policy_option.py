# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityPolicyOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'protocols': 'list[str]',
        'ciphers': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'protocols': 'protocols',
        'ciphers': 'ciphers'
    }

    def __init__(self, name=None, description=None, protocols=None, ciphers=None):
        """UpdateSecurityPolicyOption

        The model defined in huaweicloud sdk

        :param name: 自定义安全策略的名称。
        :type name: str
        :param description: 自定义安全策略的描述信息。
        :type description: str
        :param protocols: 自定义安全策略选择的TLS协议列表。取值：TLSv1, TLSv1.1, TLSv1.2, TLSv1.3
        :type protocols: list[str]
        :param ciphers: 自定义安全策略的加密套件列表。支持以下加密套件：  ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256, AES128-GCM-SHA256,AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA256, ECDHE-RSA-AES128-SHA256,AES128-SHA256,AES256-SHA256, ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA, ECDHE-ECDSA-AES256-SHA,AES128-SHA,AES256-SHA,CAMELLIA128-SHA, DES-CBC3-SHA,CAMELLIA256-SHA,ECDHE-RSA-CHACHA20-POLY1305, ECDHE-ECDSA-CHACHA20-POLY1305,TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256,TLS_AES_128_CCM_8_SHA256  使用说明： - 协议和加密套件必须匹配，即ciphers中必须至少有一种有与协议匹配的加密套件。  &gt; 协议与加密套件的匹配关系可参考系统安全策略
        :type ciphers: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._protocols = None
        self._ciphers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if protocols is not None:
            self.protocols = protocols
        if ciphers is not None:
            self.ciphers = ciphers

    @property
    def name(self):
        """Gets the name of this UpdateSecurityPolicyOption.

        自定义安全策略的名称。

        :return: The name of this UpdateSecurityPolicyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateSecurityPolicyOption.

        自定义安全策略的名称。

        :param name: The name of this UpdateSecurityPolicyOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateSecurityPolicyOption.

        自定义安全策略的描述信息。

        :return: The description of this UpdateSecurityPolicyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSecurityPolicyOption.

        自定义安全策略的描述信息。

        :param description: The description of this UpdateSecurityPolicyOption.
        :type description: str
        """
        self._description = description

    @property
    def protocols(self):
        """Gets the protocols of this UpdateSecurityPolicyOption.

        自定义安全策略选择的TLS协议列表。取值：TLSv1, TLSv1.1, TLSv1.2, TLSv1.3

        :return: The protocols of this UpdateSecurityPolicyOption.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this UpdateSecurityPolicyOption.

        自定义安全策略选择的TLS协议列表。取值：TLSv1, TLSv1.1, TLSv1.2, TLSv1.3

        :param protocols: The protocols of this UpdateSecurityPolicyOption.
        :type protocols: list[str]
        """
        self._protocols = protocols

    @property
    def ciphers(self):
        """Gets the ciphers of this UpdateSecurityPolicyOption.

        自定义安全策略的加密套件列表。支持以下加密套件：  ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256, AES128-GCM-SHA256,AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA256, ECDHE-RSA-AES128-SHA256,AES128-SHA256,AES256-SHA256, ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA, ECDHE-ECDSA-AES256-SHA,AES128-SHA,AES256-SHA,CAMELLIA128-SHA, DES-CBC3-SHA,CAMELLIA256-SHA,ECDHE-RSA-CHACHA20-POLY1305, ECDHE-ECDSA-CHACHA20-POLY1305,TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256,TLS_AES_128_CCM_8_SHA256  使用说明： - 协议和加密套件必须匹配，即ciphers中必须至少有一种有与协议匹配的加密套件。  > 协议与加密套件的匹配关系可参考系统安全策略

        :return: The ciphers of this UpdateSecurityPolicyOption.
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this UpdateSecurityPolicyOption.

        自定义安全策略的加密套件列表。支持以下加密套件：  ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256, AES128-GCM-SHA256,AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA256, ECDHE-RSA-AES128-SHA256,AES128-SHA256,AES256-SHA256, ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA, ECDHE-ECDSA-AES256-SHA,AES128-SHA,AES256-SHA,CAMELLIA128-SHA, DES-CBC3-SHA,CAMELLIA256-SHA,ECDHE-RSA-CHACHA20-POLY1305, ECDHE-ECDSA-CHACHA20-POLY1305,TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256,TLS_AES_128_CCM_8_SHA256  使用说明： - 协议和加密套件必须匹配，即ciphers中必须至少有一种有与协议匹配的加密套件。  > 协议与加密套件的匹配关系可参考系统安全策略

        :param ciphers: The ciphers of this UpdateSecurityPolicyOption.
        :type ciphers: list[str]
        """
        self._ciphers = ciphers

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
        if not isinstance(other, UpdateSecurityPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

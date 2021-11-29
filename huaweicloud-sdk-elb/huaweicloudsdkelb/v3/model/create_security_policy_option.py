# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityPolicyOption:


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
        'enterprise_project_id': 'str',
        'protocols': 'list[str]',
        'ciphers': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'protocols': 'protocols',
        'ciphers': 'ciphers'
    }

    def __init__(self, name=None, description=None, enterprise_project_id=None, protocols=None, ciphers=None):
        """CreateSecurityPolicyOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._protocols = None
        self._ciphers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.protocols = protocols
        self.ciphers = ciphers

    @property
    def name(self):
        """Gets the name of this CreateSecurityPolicyOption.

        自定义安全策略的名称。默认空字符串\"\"。

        :return: The name of this CreateSecurityPolicyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSecurityPolicyOption.

        自定义安全策略的名称。默认空字符串\"\"。

        :param name: The name of this CreateSecurityPolicyOption.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateSecurityPolicyOption.

        自定义安全策略的描述信息。默认空字符串\"\"。

        :return: The description of this CreateSecurityPolicyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSecurityPolicyOption.

        自定义安全策略的描述信息。默认空字符串\"\"。

        :param description: The description of this CreateSecurityPolicyOption.
        :type: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateSecurityPolicyOption.

        所属企业项目ID。

        :return: The enterprise_project_id of this CreateSecurityPolicyOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateSecurityPolicyOption.

        所属企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateSecurityPolicyOption.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def protocols(self):
        """Gets the protocols of this CreateSecurityPolicyOption.

        自定义安全策略选择的TLS协议列表。取值：TLSv1, TLSv1.1, TLSv1.2, TLSv1.3, GMTLS

        :return: The protocols of this CreateSecurityPolicyOption.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this CreateSecurityPolicyOption.

        自定义安全策略选择的TLS协议列表。取值：TLSv1, TLSv1.1, TLSv1.2, TLSv1.3, GMTLS

        :param protocols: The protocols of this CreateSecurityPolicyOption.
        :type: list[str]
        """
        self._protocols = protocols

    @property
    def ciphers(self):
        """Gets the ciphers of this CreateSecurityPolicyOption.

        自定义策略的加密套件列表。支持以下加密套件： ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256,AES128-GCM-SHA256,AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA256,ECDHE-RSA-AES128-SHA256,AES128-SHA256,AES256-SHA256,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA,ECDHE-ECDSA-AES256-SHA,AES128-SHA,AES256-SHA,CAMELLIA128-SHA,DES-CBC3-SHA,CAMELLIA256-SHA,ECDHE-RSA-CHACHA20-POLY1305,ECDHE-ECDSA-CHACHA20-POLY1305,TLS_AES_128_GCM_SHA256,TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SHA256,TLS_AES_128_CCM_SHA256,TLS_AES_128_CCM_8_SHA256, ECC-SM4-SM3, ECDHE-SM4-SM3

        :return: The ciphers of this CreateSecurityPolicyOption.
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        """Sets the ciphers of this CreateSecurityPolicyOption.

        自定义策略的加密套件列表。支持以下加密套件： ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-GCM-SHA256,ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256,AES128-GCM-SHA256,AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA256,ECDHE-RSA-AES128-SHA256,AES128-SHA256,AES256-SHA256,ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA,ECDHE-ECDSA-AES256-SHA,AES128-SHA,AES256-SHA,CAMELLIA128-SHA,DES-CBC3-SHA,CAMELLIA256-SHA,ECDHE-RSA-CHACHA20-POLY1305,ECDHE-ECDSA-CHACHA20-POLY1305,TLS_AES_128_GCM_SHA256,TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SHA256,TLS_AES_128_CCM_SHA256,TLS_AES_128_CCM_8_SHA256, ECC-SM4-SM3, ECDHE-SM4-SM3

        :param ciphers: The ciphers of this CreateSecurityPolicyOption.
        :type: list[str]
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
        if not isinstance(other, CreateSecurityPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

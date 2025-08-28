# coding: utf-8

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
        r"""CreateSecurityPolicyOption

        The model defined in huaweicloud sdk

        :param name: **参数解释**：自定义安全策略的名称。  **约束限制**：不涉及  **取值范围**：0到255个字符。  **默认取值**：不涉及
        :type name: str
        :param description: **参数解释**：自定义安全策略的描述信息。  **约束限制**：不涉及  **取值范围**：0到255个字符。  **默认取值**：不涉及
        :type description: str
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。创建时不传则资源属于default企业项目，返回enterprise_project_id&#x3D;\&quot;0\&quot;。  **约束限制**：不能传入空字符串\&quot;\&quot;、\&quot;0\&quot;或不存在的企业项目ID。  **取值范围**：不涉及  **默认取值**：\&quot;0\&quot;  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: str
        :param protocols: **参数解释**：自定义安全策略选择的TLS协议列表。  **约束限制**：不涉及  **取值范围**：TLSv1, TLSv1.1, TLSv1.2, TLSv1.3  **默认取值**：不涉及
        :type protocols: list[str]
        :param ciphers: **参数解释**：自定义安全策略的加密套件列表。  **约束限制**：协议和加密套件必须匹配，即ciphers中必须至少有一种与协议匹配的加密套件。  **取值范围**：ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256, AES128-GCM-SHA256,AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA256, ECDHE-RSA-AES128-SHA256,AES128-SHA256,AES256-SHA256, ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA, ECDHE-ECDSA-AES256-SHA,AES128-SHA,AES256-SHA,CAMELLIA128-SHA, DES-CBC3-SHA,CAMELLIA256-SHA,ECDHE-RSA-CHACHA20-POLY1305, ECDHE-ECDSA-CHACHA20-POLY1305,TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256,TLS_AES_128_CCM_8_SHA256  **默认取值**：不涉及  &gt; 协议与加密套件的匹配关系可参考系统安全策略
        :type ciphers: list[str]
        """
        
        

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
        r"""Gets the name of this CreateSecurityPolicyOption.

        **参数解释**：自定义安全策略的名称。  **约束限制**：不涉及  **取值范围**：0到255个字符。  **默认取值**：不涉及

        :return: The name of this CreateSecurityPolicyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSecurityPolicyOption.

        **参数解释**：自定义安全策略的名称。  **约束限制**：不涉及  **取值范围**：0到255个字符。  **默认取值**：不涉及

        :param name: The name of this CreateSecurityPolicyOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateSecurityPolicyOption.

        **参数解释**：自定义安全策略的描述信息。  **约束限制**：不涉及  **取值范围**：0到255个字符。  **默认取值**：不涉及

        :return: The description of this CreateSecurityPolicyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSecurityPolicyOption.

        **参数解释**：自定义安全策略的描述信息。  **约束限制**：不涉及  **取值范围**：0到255个字符。  **默认取值**：不涉及

        :param description: The description of this CreateSecurityPolicyOption.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateSecurityPolicyOption.

        **参数解释**：资源所属的企业项目ID。创建时不传则资源属于default企业项目，返回enterprise_project_id=\"0\"。  **约束限制**：不能传入空字符串\"\"、\"0\"或不存在的企业项目ID。  **取值范围**：不涉及  **默认取值**：\"0\"  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this CreateSecurityPolicyOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateSecurityPolicyOption.

        **参数解释**：资源所属的企业项目ID。创建时不传则资源属于default企业项目，返回enterprise_project_id=\"0\"。  **约束限制**：不能传入空字符串\"\"、\"0\"或不存在的企业项目ID。  **取值范围**：不涉及  **默认取值**：\"0\"  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this CreateSecurityPolicyOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def protocols(self):
        r"""Gets the protocols of this CreateSecurityPolicyOption.

        **参数解释**：自定义安全策略选择的TLS协议列表。  **约束限制**：不涉及  **取值范围**：TLSv1, TLSv1.1, TLSv1.2, TLSv1.3  **默认取值**：不涉及

        :return: The protocols of this CreateSecurityPolicyOption.
        :rtype: list[str]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        r"""Sets the protocols of this CreateSecurityPolicyOption.

        **参数解释**：自定义安全策略选择的TLS协议列表。  **约束限制**：不涉及  **取值范围**：TLSv1, TLSv1.1, TLSv1.2, TLSv1.3  **默认取值**：不涉及

        :param protocols: The protocols of this CreateSecurityPolicyOption.
        :type protocols: list[str]
        """
        self._protocols = protocols

    @property
    def ciphers(self):
        r"""Gets the ciphers of this CreateSecurityPolicyOption.

        **参数解释**：自定义安全策略的加密套件列表。  **约束限制**：协议和加密套件必须匹配，即ciphers中必须至少有一种与协议匹配的加密套件。  **取值范围**：ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256, AES128-GCM-SHA256,AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA256, ECDHE-RSA-AES128-SHA256,AES128-SHA256,AES256-SHA256, ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA, ECDHE-ECDSA-AES256-SHA,AES128-SHA,AES256-SHA,CAMELLIA128-SHA, DES-CBC3-SHA,CAMELLIA256-SHA,ECDHE-RSA-CHACHA20-POLY1305, ECDHE-ECDSA-CHACHA20-POLY1305,TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256,TLS_AES_128_CCM_8_SHA256  **默认取值**：不涉及  > 协议与加密套件的匹配关系可参考系统安全策略

        :return: The ciphers of this CreateSecurityPolicyOption.
        :rtype: list[str]
        """
        return self._ciphers

    @ciphers.setter
    def ciphers(self, ciphers):
        r"""Sets the ciphers of this CreateSecurityPolicyOption.

        **参数解释**：自定义安全策略的加密套件列表。  **约束限制**：协议和加密套件必须匹配，即ciphers中必须至少有一种与协议匹配的加密套件。  **取值范围**：ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256, AES128-GCM-SHA256,AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA256, ECDHE-RSA-AES128-SHA256,AES128-SHA256,AES256-SHA256, ECDHE-ECDSA-AES256-SHA384,ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA, ECDHE-ECDSA-AES256-SHA,AES128-SHA,AES256-SHA,CAMELLIA128-SHA, DES-CBC3-SHA,CAMELLIA256-SHA,ECDHE-RSA-CHACHA20-POLY1305, ECDHE-ECDSA-CHACHA20-POLY1305,TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384,TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256,TLS_AES_128_CCM_8_SHA256  **默认取值**：不涉及  > 协议与加密套件的匹配关系可参考系统安全策略

        :param ciphers: The ciphers of this CreateSecurityPolicyOption.
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
        if not isinstance(other, CreateSecurityPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

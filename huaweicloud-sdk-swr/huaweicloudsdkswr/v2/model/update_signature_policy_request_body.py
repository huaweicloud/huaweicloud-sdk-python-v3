# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSignaturePolicyRequestBody:

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
        'enabled': 'bool',
        'signature_method': 'str',
        'signature_algorithm': 'str',
        'signature_key': 'str',
        'trigger': 'TriggerConfig',
        'scope_rules': 'list[SignScopeRule]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enabled': 'enabled',
        'signature_method': 'signature_method',
        'signature_algorithm': 'signature_algorithm',
        'signature_key': 'signature_key',
        'trigger': 'trigger',
        'scope_rules': 'scope_rules'
    }

    def __init__(self, name=None, description=None, enabled=None, signature_method=None, signature_algorithm=None, signature_key=None, trigger=None, scope_rules=None):
        r"""UpdateSignaturePolicyRequestBody

        The model defined in huaweicloud sdk

        :param name: 签名策略名称，由字母、汉字、数字、下划线（_）、中划线 (-)组成，1-256个字符。
        :type name: str
        :param description: 签名策略描述
        :type description: str
        :param enabled: 是否开启
        :type enabled: bool
        :param signature_method: 加签方式，可选KMS
        :type signature_method: str
        :param signature_algorithm: 加签算法，KMS的密钥算法EC_P256对应着ECDSA_SHA_256，EC_P384对应着ECDSA_SHA_384，SM2对应着SM2DSA_SM3
        :type signature_algorithm: str
        :param signature_key: 加签Key
        :type signature_key: str
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        :param scope_rules: 作用范围规则
        :type scope_rules: list[:class:`huaweicloudsdkswr.v2.SignScopeRule`]
        """
        
        

        self._name = None
        self._description = None
        self._enabled = None
        self._signature_method = None
        self._signature_algorithm = None
        self._signature_key = None
        self._trigger = None
        self._scope_rules = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.enabled = enabled
        self.signature_method = signature_method
        self.signature_algorithm = signature_algorithm
        self.signature_key = signature_key
        self.trigger = trigger
        self.scope_rules = scope_rules

    @property
    def name(self):
        r"""Gets the name of this UpdateSignaturePolicyRequestBody.

        签名策略名称，由字母、汉字、数字、下划线（_）、中划线 (-)组成，1-256个字符。

        :return: The name of this UpdateSignaturePolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateSignaturePolicyRequestBody.

        签名策略名称，由字母、汉字、数字、下划线（_）、中划线 (-)组成，1-256个字符。

        :param name: The name of this UpdateSignaturePolicyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateSignaturePolicyRequestBody.

        签名策略描述

        :return: The description of this UpdateSignaturePolicyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateSignaturePolicyRequestBody.

        签名策略描述

        :param description: The description of this UpdateSignaturePolicyRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateSignaturePolicyRequestBody.

        是否开启

        :return: The enabled of this UpdateSignaturePolicyRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateSignaturePolicyRequestBody.

        是否开启

        :param enabled: The enabled of this UpdateSignaturePolicyRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def signature_method(self):
        r"""Gets the signature_method of this UpdateSignaturePolicyRequestBody.

        加签方式，可选KMS

        :return: The signature_method of this UpdateSignaturePolicyRequestBody.
        :rtype: str
        """
        return self._signature_method

    @signature_method.setter
    def signature_method(self, signature_method):
        r"""Sets the signature_method of this UpdateSignaturePolicyRequestBody.

        加签方式，可选KMS

        :param signature_method: The signature_method of this UpdateSignaturePolicyRequestBody.
        :type signature_method: str
        """
        self._signature_method = signature_method

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this UpdateSignaturePolicyRequestBody.

        加签算法，KMS的密钥算法EC_P256对应着ECDSA_SHA_256，EC_P384对应着ECDSA_SHA_384，SM2对应着SM2DSA_SM3

        :return: The signature_algorithm of this UpdateSignaturePolicyRequestBody.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this UpdateSignaturePolicyRequestBody.

        加签算法，KMS的密钥算法EC_P256对应着ECDSA_SHA_256，EC_P384对应着ECDSA_SHA_384，SM2对应着SM2DSA_SM3

        :param signature_algorithm: The signature_algorithm of this UpdateSignaturePolicyRequestBody.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def signature_key(self):
        r"""Gets the signature_key of this UpdateSignaturePolicyRequestBody.

        加签Key

        :return: The signature_key of this UpdateSignaturePolicyRequestBody.
        :rtype: str
        """
        return self._signature_key

    @signature_key.setter
    def signature_key(self, signature_key):
        r"""Sets the signature_key of this UpdateSignaturePolicyRequestBody.

        加签Key

        :param signature_key: The signature_key of this UpdateSignaturePolicyRequestBody.
        :type signature_key: str
        """
        self._signature_key = signature_key

    @property
    def trigger(self):
        r"""Gets the trigger of this UpdateSignaturePolicyRequestBody.

        :return: The trigger of this UpdateSignaturePolicyRequestBody.
        :rtype: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this UpdateSignaturePolicyRequestBody.

        :param trigger: The trigger of this UpdateSignaturePolicyRequestBody.
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        self._trigger = trigger

    @property
    def scope_rules(self):
        r"""Gets the scope_rules of this UpdateSignaturePolicyRequestBody.

        作用范围规则

        :return: The scope_rules of this UpdateSignaturePolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkswr.v2.SignScopeRule`]
        """
        return self._scope_rules

    @scope_rules.setter
    def scope_rules(self, scope_rules):
        r"""Sets the scope_rules of this UpdateSignaturePolicyRequestBody.

        作用范围规则

        :param scope_rules: The scope_rules of this UpdateSignaturePolicyRequestBody.
        :type scope_rules: list[:class:`huaweicloudsdkswr.v2.SignScopeRule`]
        """
        self._scope_rules = scope_rules

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
        if not isinstance(other, UpdateSignaturePolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignPolicyDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'namespace_id': 'int',
        'namespace_name': 'str',
        'trigger': 'TriggerConfig',
        'creator': 'str',
        'enabled': 'bool',
        'scope_rules': 'list[SignScopeRule]',
        'created_at': 'str',
        'updated_at': 'str',
        'signature_algorithm': 'str',
        'signature_key': 'str',
        'signature_method': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'namespace_id': 'namespace_id',
        'namespace_name': 'namespace_name',
        'trigger': 'trigger',
        'creator': 'creator',
        'enabled': 'enabled',
        'scope_rules': 'scope_rules',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'signature_algorithm': 'signature_algorithm',
        'signature_key': 'signature_key',
        'signature_method': 'signature_method'
    }

    def __init__(self, id=None, name=None, description=None, namespace_id=None, namespace_name=None, trigger=None, creator=None, enabled=None, scope_rules=None, created_at=None, updated_at=None, signature_algorithm=None, signature_key=None, signature_method=None):
        r"""SignPolicyDetail

        The model defined in huaweicloud sdk

        :param id: 签名策略ID
        :type id: int
        :param name: 签名策略名称
        :type name: str
        :param description: 签名策略描述
        :type description: str
        :param namespace_id: 命名空间ID
        :type namespace_id: int
        :param namespace_name: 命名空间名
        :type namespace_name: str
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        :param creator: 创建者
        :type creator: str
        :param enabled: 是否
        :type enabled: bool
        :param scope_rules: 作用范围规则
        :type scope_rules: list[:class:`huaweicloudsdkswr.v2.SignScopeRule`]
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param signature_algorithm: 加签算法，KMS的密钥算法EC_P256对应着ECDSA_SHA_256，EC_P384对应着ECDSA_SHA_384，SM2对应着SM2DSA_SM3
        :type signature_algorithm: str
        :param signature_key: 签名算法key ID
        :type signature_key: str
        :param signature_method: 镜像签名方式
        :type signature_method: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._namespace_id = None
        self._namespace_name = None
        self._trigger = None
        self._creator = None
        self._enabled = None
        self._scope_rules = None
        self._created_at = None
        self._updated_at = None
        self._signature_algorithm = None
        self._signature_key = None
        self._signature_method = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if trigger is not None:
            self.trigger = trigger
        if creator is not None:
            self.creator = creator
        if enabled is not None:
            self.enabled = enabled
        if scope_rules is not None:
            self.scope_rules = scope_rules
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if signature_key is not None:
            self.signature_key = signature_key
        if signature_method is not None:
            self.signature_method = signature_method

    @property
    def id(self):
        r"""Gets the id of this SignPolicyDetail.

        签名策略ID

        :return: The id of this SignPolicyDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SignPolicyDetail.

        签名策略ID

        :param id: The id of this SignPolicyDetail.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SignPolicyDetail.

        签名策略名称

        :return: The name of this SignPolicyDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SignPolicyDetail.

        签名策略名称

        :param name: The name of this SignPolicyDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SignPolicyDetail.

        签名策略描述

        :return: The description of this SignPolicyDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SignPolicyDetail.

        签名策略描述

        :param description: The description of this SignPolicyDetail.
        :type description: str
        """
        self._description = description

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this SignPolicyDetail.

        命名空间ID

        :return: The namespace_id of this SignPolicyDetail.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this SignPolicyDetail.

        命名空间ID

        :param namespace_id: The namespace_id of this SignPolicyDetail.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this SignPolicyDetail.

        命名空间名

        :return: The namespace_name of this SignPolicyDetail.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this SignPolicyDetail.

        命名空间名

        :param namespace_name: The namespace_name of this SignPolicyDetail.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def trigger(self):
        r"""Gets the trigger of this SignPolicyDetail.

        :return: The trigger of this SignPolicyDetail.
        :rtype: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this SignPolicyDetail.

        :param trigger: The trigger of this SignPolicyDetail.
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        self._trigger = trigger

    @property
    def creator(self):
        r"""Gets the creator of this SignPolicyDetail.

        创建者

        :return: The creator of this SignPolicyDetail.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this SignPolicyDetail.

        创建者

        :param creator: The creator of this SignPolicyDetail.
        :type creator: str
        """
        self._creator = creator

    @property
    def enabled(self):
        r"""Gets the enabled of this SignPolicyDetail.

        是否

        :return: The enabled of this SignPolicyDetail.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this SignPolicyDetail.

        是否

        :param enabled: The enabled of this SignPolicyDetail.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def scope_rules(self):
        r"""Gets the scope_rules of this SignPolicyDetail.

        作用范围规则

        :return: The scope_rules of this SignPolicyDetail.
        :rtype: list[:class:`huaweicloudsdkswr.v2.SignScopeRule`]
        """
        return self._scope_rules

    @scope_rules.setter
    def scope_rules(self, scope_rules):
        r"""Sets the scope_rules of this SignPolicyDetail.

        作用范围规则

        :param scope_rules: The scope_rules of this SignPolicyDetail.
        :type scope_rules: list[:class:`huaweicloudsdkswr.v2.SignScopeRule`]
        """
        self._scope_rules = scope_rules

    @property
    def created_at(self):
        r"""Gets the created_at of this SignPolicyDetail.

        创建时间

        :return: The created_at of this SignPolicyDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SignPolicyDetail.

        创建时间

        :param created_at: The created_at of this SignPolicyDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SignPolicyDetail.

        更新时间

        :return: The updated_at of this SignPolicyDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SignPolicyDetail.

        更新时间

        :param updated_at: The updated_at of this SignPolicyDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this SignPolicyDetail.

        加签算法，KMS的密钥算法EC_P256对应着ECDSA_SHA_256，EC_P384对应着ECDSA_SHA_384，SM2对应着SM2DSA_SM3

        :return: The signature_algorithm of this SignPolicyDetail.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this SignPolicyDetail.

        加签算法，KMS的密钥算法EC_P256对应着ECDSA_SHA_256，EC_P384对应着ECDSA_SHA_384，SM2对应着SM2DSA_SM3

        :param signature_algorithm: The signature_algorithm of this SignPolicyDetail.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def signature_key(self):
        r"""Gets the signature_key of this SignPolicyDetail.

        签名算法key ID

        :return: The signature_key of this SignPolicyDetail.
        :rtype: str
        """
        return self._signature_key

    @signature_key.setter
    def signature_key(self, signature_key):
        r"""Sets the signature_key of this SignPolicyDetail.

        签名算法key ID

        :param signature_key: The signature_key of this SignPolicyDetail.
        :type signature_key: str
        """
        self._signature_key = signature_key

    @property
    def signature_method(self):
        r"""Gets the signature_method of this SignPolicyDetail.

        镜像签名方式

        :return: The signature_method of this SignPolicyDetail.
        :rtype: str
        """
        return self._signature_method

    @signature_method.setter
    def signature_method(self, signature_method):
        r"""Sets the signature_method of this SignPolicyDetail.

        镜像签名方式

        :param signature_method: The signature_method of this SignPolicyDetail.
        :type signature_method: str
        """
        self._signature_method = signature_method

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
        if not isinstance(other, SignPolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

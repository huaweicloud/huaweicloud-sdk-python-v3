# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'name': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'is_default': 'bool',
        'create_time': 'int',
        'rules': 'list[AlertRuleDTO]'
    }

    attribute_map = {
        'policy_id': 'policyId',
        'name': 'name',
        'domain_id': 'domainId',
        'project_id': 'projectId',
        'is_default': 'isDefault',
        'create_time': 'createTime',
        'rules': 'rules'
    }

    def __init__(self, policy_id=None, name=None, domain_id=None, project_id=None, is_default=None, create_time=None, rules=None):
        r"""ShowAlertPolicyResponse

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释**： 策略ID。 **约束限制**： 更新时传，新增时不传。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type policy_id: str
        :param name: **参数解释**： 策略名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type name: str
        :param domain_id: **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type domain_id: str
        :param project_id: **参数解释**： 项目ID。 **约束限制**： 暂时不用。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type project_id: str
        :param is_default: **参数解释**： 是否为默认策略。 **约束限制**： 不涉及。 **取值范围**： - true：是默认策略。 - false：不是默认策略。 **默认取值**： 不涉及。 
        :type is_default: bool
        :param create_time: **参数解释**： 创建时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type create_time: int
        :param rules: **参数解释**： 所有规则。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type rules: list[:class:`huaweicloudsdkcodeartspipeline.v2.AlertRuleDTO`]
        """
        
        super().__init__()

        self._policy_id = None
        self._name = None
        self._domain_id = None
        self._project_id = None
        self._is_default = None
        self._create_time = None
        self._rules = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if name is not None:
            self.name = name
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if is_default is not None:
            self.is_default = is_default
        if create_time is not None:
            self.create_time = create_time
        if rules is not None:
            self.rules = rules

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowAlertPolicyResponse.

        **参数解释**： 策略ID。 **约束限制**： 更新时传，新增时不传。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The policy_id of this ShowAlertPolicyResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowAlertPolicyResponse.

        **参数解释**： 策略ID。 **约束限制**： 更新时传，新增时不传。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param policy_id: The policy_id of this ShowAlertPolicyResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def name(self):
        r"""Gets the name of this ShowAlertPolicyResponse.

        **参数解释**： 策略名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The name of this ShowAlertPolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAlertPolicyResponse.

        **参数解释**： 策略名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param name: The name of this ShowAlertPolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowAlertPolicyResponse.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The domain_id of this ShowAlertPolicyResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowAlertPolicyResponse.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param domain_id: The domain_id of this ShowAlertPolicyResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowAlertPolicyResponse.

        **参数解释**： 项目ID。 **约束限制**： 暂时不用。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The project_id of this ShowAlertPolicyResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowAlertPolicyResponse.

        **参数解释**： 项目ID。 **约束限制**： 暂时不用。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param project_id: The project_id of this ShowAlertPolicyResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_default(self):
        r"""Gets the is_default of this ShowAlertPolicyResponse.

        **参数解释**： 是否为默认策略。 **约束限制**： 不涉及。 **取值范围**： - true：是默认策略。 - false：不是默认策略。 **默认取值**： 不涉及。 

        :return: The is_default of this ShowAlertPolicyResponse.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this ShowAlertPolicyResponse.

        **参数解释**： 是否为默认策略。 **约束限制**： 不涉及。 **取值范围**： - true：是默认策略。 - false：不是默认策略。 **默认取值**： 不涉及。 

        :param is_default: The is_default of this ShowAlertPolicyResponse.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowAlertPolicyResponse.

        **参数解释**： 创建时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The create_time of this ShowAlertPolicyResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowAlertPolicyResponse.

        **参数解释**： 创建时间。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param create_time: The create_time of this ShowAlertPolicyResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def rules(self):
        r"""Gets the rules of this ShowAlertPolicyResponse.

        **参数解释**： 所有规则。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The rules of this ShowAlertPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.AlertRuleDTO`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ShowAlertPolicyResponse.

        **参数解释**： 所有规则。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param rules: The rules of this ShowAlertPolicyResponse.
        :type rules: list[:class:`huaweicloudsdkcodeartspipeline.v2.AlertRuleDTO`]
        """
        self._rules = rules

    def to_dict(self):
        import warnings
        warnings.warn("ShowAlertPolicyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowAlertPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

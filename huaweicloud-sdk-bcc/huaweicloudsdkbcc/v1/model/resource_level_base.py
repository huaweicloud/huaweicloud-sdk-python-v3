# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceLevelBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'resource_level_name': 'str',
        'providers': 'list[str]',
        'resource_level': 'int',
        'domain_id': 'str',
        'description': 'str',
        'apply_type': 'int',
        'apply_rule': 'str',
        'compliance_rule_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'resource_level_name': 'resource_level_name',
        'providers': 'providers',
        'resource_level': 'resource_level',
        'domain_id': 'domain_id',
        'description': 'description',
        'apply_type': 'apply_type',
        'apply_rule': 'apply_rule',
        'compliance_rule_id': 'compliance_rule_id'
    }

    def __init__(self, id=None, resource_level_name=None, providers=None, resource_level=None, domain_id=None, description=None, apply_type=None, apply_rule=None, compliance_rule_id=None):
        r"""ResourceLevelBase

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param resource_level_name: 资源等级名称
        :type resource_level_name: str
        :param providers: 云服务
        :type providers: list[str]
        :param resource_level: 重要程度
        :type resource_level: int
        :param domain_id: 账户ID
        :type domain_id: str
        :param description: 描述
        :type description: str
        :param apply_type: 应用方式
        :type apply_type: int
        :param apply_rule: 应用规则
        :type apply_rule: str
        :param compliance_rule_id: 合规规则ID
        :type compliance_rule_id: str
        """
        
        

        self._id = None
        self._resource_level_name = None
        self._providers = None
        self._resource_level = None
        self._domain_id = None
        self._description = None
        self._apply_type = None
        self._apply_rule = None
        self._compliance_rule_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_level_name is not None:
            self.resource_level_name = resource_level_name
        if providers is not None:
            self.providers = providers
        if resource_level is not None:
            self.resource_level = resource_level
        if domain_id is not None:
            self.domain_id = domain_id
        if description is not None:
            self.description = description
        if apply_type is not None:
            self.apply_type = apply_type
        if apply_rule is not None:
            self.apply_rule = apply_rule
        if compliance_rule_id is not None:
            self.compliance_rule_id = compliance_rule_id

    @property
    def id(self):
        r"""Gets the id of this ResourceLevelBase.

        ID

        :return: The id of this ResourceLevelBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResourceLevelBase.

        ID

        :param id: The id of this ResourceLevelBase.
        :type id: str
        """
        self._id = id

    @property
    def resource_level_name(self):
        r"""Gets the resource_level_name of this ResourceLevelBase.

        资源等级名称

        :return: The resource_level_name of this ResourceLevelBase.
        :rtype: str
        """
        return self._resource_level_name

    @resource_level_name.setter
    def resource_level_name(self, resource_level_name):
        r"""Sets the resource_level_name of this ResourceLevelBase.

        资源等级名称

        :param resource_level_name: The resource_level_name of this ResourceLevelBase.
        :type resource_level_name: str
        """
        self._resource_level_name = resource_level_name

    @property
    def providers(self):
        r"""Gets the providers of this ResourceLevelBase.

        云服务

        :return: The providers of this ResourceLevelBase.
        :rtype: list[str]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        r"""Sets the providers of this ResourceLevelBase.

        云服务

        :param providers: The providers of this ResourceLevelBase.
        :type providers: list[str]
        """
        self._providers = providers

    @property
    def resource_level(self):
        r"""Gets the resource_level of this ResourceLevelBase.

        重要程度

        :return: The resource_level of this ResourceLevelBase.
        :rtype: int
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this ResourceLevelBase.

        重要程度

        :param resource_level: The resource_level of this ResourceLevelBase.
        :type resource_level: int
        """
        self._resource_level = resource_level

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ResourceLevelBase.

        账户ID

        :return: The domain_id of this ResourceLevelBase.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ResourceLevelBase.

        账户ID

        :param domain_id: The domain_id of this ResourceLevelBase.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def description(self):
        r"""Gets the description of this ResourceLevelBase.

        描述

        :return: The description of this ResourceLevelBase.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ResourceLevelBase.

        描述

        :param description: The description of this ResourceLevelBase.
        :type description: str
        """
        self._description = description

    @property
    def apply_type(self):
        r"""Gets the apply_type of this ResourceLevelBase.

        应用方式

        :return: The apply_type of this ResourceLevelBase.
        :rtype: int
        """
        return self._apply_type

    @apply_type.setter
    def apply_type(self, apply_type):
        r"""Sets the apply_type of this ResourceLevelBase.

        应用方式

        :param apply_type: The apply_type of this ResourceLevelBase.
        :type apply_type: int
        """
        self._apply_type = apply_type

    @property
    def apply_rule(self):
        r"""Gets the apply_rule of this ResourceLevelBase.

        应用规则

        :return: The apply_rule of this ResourceLevelBase.
        :rtype: str
        """
        return self._apply_rule

    @apply_rule.setter
    def apply_rule(self, apply_rule):
        r"""Sets the apply_rule of this ResourceLevelBase.

        应用规则

        :param apply_rule: The apply_rule of this ResourceLevelBase.
        :type apply_rule: str
        """
        self._apply_rule = apply_rule

    @property
    def compliance_rule_id(self):
        r"""Gets the compliance_rule_id of this ResourceLevelBase.

        合规规则ID

        :return: The compliance_rule_id of this ResourceLevelBase.
        :rtype: str
        """
        return self._compliance_rule_id

    @compliance_rule_id.setter
    def compliance_rule_id(self, compliance_rule_id):
        r"""Sets the compliance_rule_id of this ResourceLevelBase.

        合规规则ID

        :param compliance_rule_id: The compliance_rule_id of this ResourceLevelBase.
        :type compliance_rule_id: str
        """
        self._compliance_rule_id = compliance_rule_id

    def to_dict(self):
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
        if not isinstance(other, ResourceLevelBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

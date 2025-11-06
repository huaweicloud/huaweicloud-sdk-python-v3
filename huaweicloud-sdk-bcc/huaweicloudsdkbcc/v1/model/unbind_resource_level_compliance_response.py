# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnbindResourceLevelComplianceResponse(SdkResponse):

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
        'description': 'str',
        'domain_id': 'str',
        'organization_id': 'str',
        'project_id': 'str',
        'apply_type': 'int',
        'apply_rule': 'str',
        'compliance_rule': 'ComplianceRule',
        'resource_count_list': 'list[LevelResourceCount]'
    }

    attribute_map = {
        'id': 'id',
        'resource_level_name': 'resource_level_name',
        'providers': 'providers',
        'resource_level': 'resource_level',
        'description': 'description',
        'domain_id': 'domain_id',
        'organization_id': 'organization_id',
        'project_id': 'project_id',
        'apply_type': 'apply_type',
        'apply_rule': 'apply_rule',
        'compliance_rule': 'compliance_rule',
        'resource_count_list': 'resource_count_list'
    }

    def __init__(self, id=None, resource_level_name=None, providers=None, resource_level=None, description=None, domain_id=None, organization_id=None, project_id=None, apply_type=None, apply_rule=None, compliance_rule=None, resource_count_list=None):
        r"""UnbindResourceLevelComplianceResponse

        The model defined in huaweicloud sdk

        :param id: 资源分级ID
        :type id: str
        :param resource_level_name: 资源分级名称
        :type resource_level_name: str
        :param providers: 资源类型
        :type providers: list[str]
        :param resource_level: 资产级别，支持五级 。1公开，2一般，3关键，4重要，5核心
        :type resource_level: int
        :param description: 描述
        :type description: str
        :param domain_id: 账户ID
        :type domain_id: str
        :param organization_id: 组织ID
        :type organization_id: str
        :param project_id: 企业项目ID
        :type project_id: str
        :param apply_type: 应用方式。1：按标签匹配；2：按照资源类型和资源名称正则匹配；3：按照资源ID
        :type apply_type: int
        :param apply_rule: 应用的规则
        :type apply_rule: str
        :param compliance_rule: 
        :type compliance_rule: :class:`huaweicloudsdkbcc.v1.ComplianceRule`
        :param resource_count_list: 各类资源数量
        :type resource_count_list: list[:class:`huaweicloudsdkbcc.v1.LevelResourceCount`]
        """
        
        super().__init__()

        self._id = None
        self._resource_level_name = None
        self._providers = None
        self._resource_level = None
        self._description = None
        self._domain_id = None
        self._organization_id = None
        self._project_id = None
        self._apply_type = None
        self._apply_rule = None
        self._compliance_rule = None
        self._resource_count_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_level_name is not None:
            self.resource_level_name = resource_level_name
        if providers is not None:
            self.providers = providers
        if resource_level is not None:
            self.resource_level = resource_level
        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if organization_id is not None:
            self.organization_id = organization_id
        if project_id is not None:
            self.project_id = project_id
        if apply_type is not None:
            self.apply_type = apply_type
        if apply_rule is not None:
            self.apply_rule = apply_rule
        if compliance_rule is not None:
            self.compliance_rule = compliance_rule
        if resource_count_list is not None:
            self.resource_count_list = resource_count_list

    @property
    def id(self):
        r"""Gets the id of this UnbindResourceLevelComplianceResponse.

        资源分级ID

        :return: The id of this UnbindResourceLevelComplianceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UnbindResourceLevelComplianceResponse.

        资源分级ID

        :param id: The id of this UnbindResourceLevelComplianceResponse.
        :type id: str
        """
        self._id = id

    @property
    def resource_level_name(self):
        r"""Gets the resource_level_name of this UnbindResourceLevelComplianceResponse.

        资源分级名称

        :return: The resource_level_name of this UnbindResourceLevelComplianceResponse.
        :rtype: str
        """
        return self._resource_level_name

    @resource_level_name.setter
    def resource_level_name(self, resource_level_name):
        r"""Sets the resource_level_name of this UnbindResourceLevelComplianceResponse.

        资源分级名称

        :param resource_level_name: The resource_level_name of this UnbindResourceLevelComplianceResponse.
        :type resource_level_name: str
        """
        self._resource_level_name = resource_level_name

    @property
    def providers(self):
        r"""Gets the providers of this UnbindResourceLevelComplianceResponse.

        资源类型

        :return: The providers of this UnbindResourceLevelComplianceResponse.
        :rtype: list[str]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        r"""Sets the providers of this UnbindResourceLevelComplianceResponse.

        资源类型

        :param providers: The providers of this UnbindResourceLevelComplianceResponse.
        :type providers: list[str]
        """
        self._providers = providers

    @property
    def resource_level(self):
        r"""Gets the resource_level of this UnbindResourceLevelComplianceResponse.

        资产级别，支持五级 。1公开，2一般，3关键，4重要，5核心

        :return: The resource_level of this UnbindResourceLevelComplianceResponse.
        :rtype: int
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this UnbindResourceLevelComplianceResponse.

        资产级别，支持五级 。1公开，2一般，3关键，4重要，5核心

        :param resource_level: The resource_level of this UnbindResourceLevelComplianceResponse.
        :type resource_level: int
        """
        self._resource_level = resource_level

    @property
    def description(self):
        r"""Gets the description of this UnbindResourceLevelComplianceResponse.

        描述

        :return: The description of this UnbindResourceLevelComplianceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UnbindResourceLevelComplianceResponse.

        描述

        :param description: The description of this UnbindResourceLevelComplianceResponse.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UnbindResourceLevelComplianceResponse.

        账户ID

        :return: The domain_id of this UnbindResourceLevelComplianceResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UnbindResourceLevelComplianceResponse.

        账户ID

        :param domain_id: The domain_id of this UnbindResourceLevelComplianceResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def organization_id(self):
        r"""Gets the organization_id of this UnbindResourceLevelComplianceResponse.

        组织ID

        :return: The organization_id of this UnbindResourceLevelComplianceResponse.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this UnbindResourceLevelComplianceResponse.

        组织ID

        :param organization_id: The organization_id of this UnbindResourceLevelComplianceResponse.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def project_id(self):
        r"""Gets the project_id of this UnbindResourceLevelComplianceResponse.

        企业项目ID

        :return: The project_id of this UnbindResourceLevelComplianceResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UnbindResourceLevelComplianceResponse.

        企业项目ID

        :param project_id: The project_id of this UnbindResourceLevelComplianceResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def apply_type(self):
        r"""Gets the apply_type of this UnbindResourceLevelComplianceResponse.

        应用方式。1：按标签匹配；2：按照资源类型和资源名称正则匹配；3：按照资源ID

        :return: The apply_type of this UnbindResourceLevelComplianceResponse.
        :rtype: int
        """
        return self._apply_type

    @apply_type.setter
    def apply_type(self, apply_type):
        r"""Sets the apply_type of this UnbindResourceLevelComplianceResponse.

        应用方式。1：按标签匹配；2：按照资源类型和资源名称正则匹配；3：按照资源ID

        :param apply_type: The apply_type of this UnbindResourceLevelComplianceResponse.
        :type apply_type: int
        """
        self._apply_type = apply_type

    @property
    def apply_rule(self):
        r"""Gets the apply_rule of this UnbindResourceLevelComplianceResponse.

        应用的规则

        :return: The apply_rule of this UnbindResourceLevelComplianceResponse.
        :rtype: str
        """
        return self._apply_rule

    @apply_rule.setter
    def apply_rule(self, apply_rule):
        r"""Sets the apply_rule of this UnbindResourceLevelComplianceResponse.

        应用的规则

        :param apply_rule: The apply_rule of this UnbindResourceLevelComplianceResponse.
        :type apply_rule: str
        """
        self._apply_rule = apply_rule

    @property
    def compliance_rule(self):
        r"""Gets the compliance_rule of this UnbindResourceLevelComplianceResponse.

        :return: The compliance_rule of this UnbindResourceLevelComplianceResponse.
        :rtype: :class:`huaweicloudsdkbcc.v1.ComplianceRule`
        """
        return self._compliance_rule

    @compliance_rule.setter
    def compliance_rule(self, compliance_rule):
        r"""Sets the compliance_rule of this UnbindResourceLevelComplianceResponse.

        :param compliance_rule: The compliance_rule of this UnbindResourceLevelComplianceResponse.
        :type compliance_rule: :class:`huaweicloudsdkbcc.v1.ComplianceRule`
        """
        self._compliance_rule = compliance_rule

    @property
    def resource_count_list(self):
        r"""Gets the resource_count_list of this UnbindResourceLevelComplianceResponse.

        各类资源数量

        :return: The resource_count_list of this UnbindResourceLevelComplianceResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.LevelResourceCount`]
        """
        return self._resource_count_list

    @resource_count_list.setter
    def resource_count_list(self, resource_count_list):
        r"""Sets the resource_count_list of this UnbindResourceLevelComplianceResponse.

        各类资源数量

        :param resource_count_list: The resource_count_list of this UnbindResourceLevelComplianceResponse.
        :type resource_count_list: list[:class:`huaweicloudsdkbcc.v1.LevelResourceCount`]
        """
        self._resource_count_list = resource_count_list

    def to_dict(self):
        import warnings
        warnings.warn("UnbindResourceLevelComplianceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UnbindResourceLevelComplianceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

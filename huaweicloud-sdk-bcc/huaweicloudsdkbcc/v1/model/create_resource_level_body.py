# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceLevelBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_level_name': 'str',
        'providers': 'list[str]',
        'resource_level': 'int',
        'description': 'str',
        'apply_type': 'int',
        'apply_rule': 'str',
        'compliance_rule_id': 'str'
    }

    attribute_map = {
        'resource_level_name': 'resource_level_name',
        'providers': 'providers',
        'resource_level': 'resource_level',
        'description': 'description',
        'apply_type': 'apply_type',
        'apply_rule': 'apply_rule',
        'compliance_rule_id': 'compliance_rule_id'
    }

    def __init__(self, resource_level_name=None, providers=None, resource_level=None, description=None, apply_type=None, apply_rule=None, compliance_rule_id=None):
        r"""CreateResourceLevelBody

        The model defined in huaweicloud sdk

        :param resource_level_name: 资源分级名称，只能是汉字、大小写字母、下划线、中划线、数字组成，且不能以数字或者中划线或者下划线开头
        :type resource_level_name: str
        :param providers: 资源类型
        :type providers: list[str]
        :param resource_level: 资源级别，创建时为5
        :type resource_level: int
        :param description: 描述
        :type description: str
        :param apply_type: 应用方式
        :type apply_type: int
        :param apply_rule: 应用的规则, 标签的格式为\&quot;[{\\\&quot;key\\\&quot;: \\\&quot;A\\\&quot;, \&quot;value\\\&quot;:\\\&quot;a\\\&quot;}]\&quot;
        :type apply_rule: str
        :param compliance_rule_id: 合规规则的id
        :type compliance_rule_id: str
        """
        
        

        self._resource_level_name = None
        self._providers = None
        self._resource_level = None
        self._description = None
        self._apply_type = None
        self._apply_rule = None
        self._compliance_rule_id = None
        self.discriminator = None

        self.resource_level_name = resource_level_name
        self.providers = providers
        self.resource_level = resource_level
        if description is not None:
            self.description = description
        if apply_type is not None:
            self.apply_type = apply_type
        if apply_rule is not None:
            self.apply_rule = apply_rule
        if compliance_rule_id is not None:
            self.compliance_rule_id = compliance_rule_id

    @property
    def resource_level_name(self):
        r"""Gets the resource_level_name of this CreateResourceLevelBody.

        资源分级名称，只能是汉字、大小写字母、下划线、中划线、数字组成，且不能以数字或者中划线或者下划线开头

        :return: The resource_level_name of this CreateResourceLevelBody.
        :rtype: str
        """
        return self._resource_level_name

    @resource_level_name.setter
    def resource_level_name(self, resource_level_name):
        r"""Sets the resource_level_name of this CreateResourceLevelBody.

        资源分级名称，只能是汉字、大小写字母、下划线、中划线、数字组成，且不能以数字或者中划线或者下划线开头

        :param resource_level_name: The resource_level_name of this CreateResourceLevelBody.
        :type resource_level_name: str
        """
        self._resource_level_name = resource_level_name

    @property
    def providers(self):
        r"""Gets the providers of this CreateResourceLevelBody.

        资源类型

        :return: The providers of this CreateResourceLevelBody.
        :rtype: list[str]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        r"""Sets the providers of this CreateResourceLevelBody.

        资源类型

        :param providers: The providers of this CreateResourceLevelBody.
        :type providers: list[str]
        """
        self._providers = providers

    @property
    def resource_level(self):
        r"""Gets the resource_level of this CreateResourceLevelBody.

        资源级别，创建时为5

        :return: The resource_level of this CreateResourceLevelBody.
        :rtype: int
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this CreateResourceLevelBody.

        资源级别，创建时为5

        :param resource_level: The resource_level of this CreateResourceLevelBody.
        :type resource_level: int
        """
        self._resource_level = resource_level

    @property
    def description(self):
        r"""Gets the description of this CreateResourceLevelBody.

        描述

        :return: The description of this CreateResourceLevelBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateResourceLevelBody.

        描述

        :param description: The description of this CreateResourceLevelBody.
        :type description: str
        """
        self._description = description

    @property
    def apply_type(self):
        r"""Gets the apply_type of this CreateResourceLevelBody.

        应用方式

        :return: The apply_type of this CreateResourceLevelBody.
        :rtype: int
        """
        return self._apply_type

    @apply_type.setter
    def apply_type(self, apply_type):
        r"""Sets the apply_type of this CreateResourceLevelBody.

        应用方式

        :param apply_type: The apply_type of this CreateResourceLevelBody.
        :type apply_type: int
        """
        self._apply_type = apply_type

    @property
    def apply_rule(self):
        r"""Gets the apply_rule of this CreateResourceLevelBody.

        应用的规则, 标签的格式为\"[{\\\"key\\\": \\\"A\\\", \"value\\\":\\\"a\\\"}]\"

        :return: The apply_rule of this CreateResourceLevelBody.
        :rtype: str
        """
        return self._apply_rule

    @apply_rule.setter
    def apply_rule(self, apply_rule):
        r"""Sets the apply_rule of this CreateResourceLevelBody.

        应用的规则, 标签的格式为\"[{\\\"key\\\": \\\"A\\\", \"value\\\":\\\"a\\\"}]\"

        :param apply_rule: The apply_rule of this CreateResourceLevelBody.
        :type apply_rule: str
        """
        self._apply_rule = apply_rule

    @property
    def compliance_rule_id(self):
        r"""Gets the compliance_rule_id of this CreateResourceLevelBody.

        合规规则的id

        :return: The compliance_rule_id of this CreateResourceLevelBody.
        :rtype: str
        """
        return self._compliance_rule_id

    @compliance_rule_id.setter
    def compliance_rule_id(self, compliance_rule_id):
        r"""Sets the compliance_rule_id of this CreateResourceLevelBody.

        合规规则的id

        :param compliance_rule_id: The compliance_rule_id of this CreateResourceLevelBody.
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
        if not isinstance(other, CreateResourceLevelBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

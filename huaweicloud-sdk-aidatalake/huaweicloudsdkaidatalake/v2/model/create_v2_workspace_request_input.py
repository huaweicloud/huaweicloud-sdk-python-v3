# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateV2WorkspaceRequestInput:

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
        'metastore_id': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[V2ResourceTag]',
        'cross_tenant_access': 'bool',
        'target_domain_id': 'str',
        'target_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'metastore_id': 'metastore_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'cross_tenant_access': 'cross_tenant_access',
        'target_domain_id': 'target_domain_id',
        'target_project_id': 'target_project_id'
    }

    def __init__(self, name=None, description=None, metastore_id=None, enterprise_project_id=None, tags=None, cross_tenant_access=None, target_domain_id=None, target_project_id=None):
        r"""CreateV2WorkspaceRequestInput

        The model defined in huaweicloud sdk

        :param name: **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 
        :type name: str
        :param description: **参数解释**：用户输入的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~255个字符。 **默认取值**：不涉及。 
        :type description: str
        :param metastore_id: **参数解释**：LakeFormation服务的实例ID，可在LakeFormation控制台实例列表中查看，或通过调用LakeFormation服务的查询实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字母、数字和中划线的组合。 **默认取值**：不涉及。 
        :type metastore_id: str
        :param enterprise_project_id: **参数解释**：企业项目ID，获取方法，请参见[获取企业项目ID](aidatalake_02_0042.xml)。 **约束限制**：不涉及。 **取值范围**：长度为0~128个英文字母、数字、下划线和中划线的组合。 **默认取值**：0。 
        :type enterprise_project_id: str
        :param tags: **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        :param cross_tenant_access: **参数解释**：是否跨租户访问。 **取值范围**：   - true：允许跨租户访问。   - false：不允许跨租户访问。
        :type cross_tenant_access: bool
        :param target_domain_id: **参数解释**：目标租户Domain ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。
        :type target_domain_id: str
        :param target_project_id: **参数解释**：目标租户Project ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。
        :type target_project_id: str
        """
        
        

        self._name = None
        self._description = None
        self._metastore_id = None
        self._enterprise_project_id = None
        self._tags = None
        self._cross_tenant_access = None
        self._target_domain_id = None
        self._target_project_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.metastore_id = metastore_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if cross_tenant_access is not None:
            self.cross_tenant_access = cross_tenant_access
        if target_domain_id is not None:
            self.target_domain_id = target_domain_id
        if target_project_id is not None:
            self.target_project_id = target_project_id

    @property
    def name(self):
        r"""Gets the name of this CreateV2WorkspaceRequestInput.

        **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 

        :return: The name of this CreateV2WorkspaceRequestInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateV2WorkspaceRequestInput.

        **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 

        :param name: The name of this CreateV2WorkspaceRequestInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateV2WorkspaceRequestInput.

        **参数解释**：用户输入的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~255个字符。 **默认取值**：不涉及。 

        :return: The description of this CreateV2WorkspaceRequestInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateV2WorkspaceRequestInput.

        **参数解释**：用户输入的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~255个字符。 **默认取值**：不涉及。 

        :param description: The description of this CreateV2WorkspaceRequestInput.
        :type description: str
        """
        self._description = description

    @property
    def metastore_id(self):
        r"""Gets the metastore_id of this CreateV2WorkspaceRequestInput.

        **参数解释**：LakeFormation服务的实例ID，可在LakeFormation控制台实例列表中查看，或通过调用LakeFormation服务的查询实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The metastore_id of this CreateV2WorkspaceRequestInput.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        r"""Sets the metastore_id of this CreateV2WorkspaceRequestInput.

        **参数解释**：LakeFormation服务的实例ID，可在LakeFormation控制台实例列表中查看，或通过调用LakeFormation服务的查询实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :param metastore_id: The metastore_id of this CreateV2WorkspaceRequestInput.
        :type metastore_id: str
        """
        self._metastore_id = metastore_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateV2WorkspaceRequestInput.

        **参数解释**：企业项目ID，获取方法，请参见[获取企业项目ID](aidatalake_02_0042.xml)。 **约束限制**：不涉及。 **取值范围**：长度为0~128个英文字母、数字、下划线和中划线的组合。 **默认取值**：0。 

        :return: The enterprise_project_id of this CreateV2WorkspaceRequestInput.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateV2WorkspaceRequestInput.

        **参数解释**：企业项目ID，获取方法，请参见[获取企业项目ID](aidatalake_02_0042.xml)。 **约束限制**：不涉及。 **取值范围**：长度为0~128个英文字母、数字、下划线和中划线的组合。 **默认取值**：0。 

        :param enterprise_project_id: The enterprise_project_id of this CreateV2WorkspaceRequestInput.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateV2WorkspaceRequestInput.

        **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 

        :return: The tags of this CreateV2WorkspaceRequestInput.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateV2WorkspaceRequestInput.

        **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 

        :param tags: The tags of this CreateV2WorkspaceRequestInput.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        self._tags = tags

    @property
    def cross_tenant_access(self):
        r"""Gets the cross_tenant_access of this CreateV2WorkspaceRequestInput.

        **参数解释**：是否跨租户访问。 **取值范围**：   - true：允许跨租户访问。   - false：不允许跨租户访问。

        :return: The cross_tenant_access of this CreateV2WorkspaceRequestInput.
        :rtype: bool
        """
        return self._cross_tenant_access

    @cross_tenant_access.setter
    def cross_tenant_access(self, cross_tenant_access):
        r"""Sets the cross_tenant_access of this CreateV2WorkspaceRequestInput.

        **参数解释**：是否跨租户访问。 **取值范围**：   - true：允许跨租户访问。   - false：不允许跨租户访问。

        :param cross_tenant_access: The cross_tenant_access of this CreateV2WorkspaceRequestInput.
        :type cross_tenant_access: bool
        """
        self._cross_tenant_access = cross_tenant_access

    @property
    def target_domain_id(self):
        r"""Gets the target_domain_id of this CreateV2WorkspaceRequestInput.

        **参数解释**：目标租户Domain ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。

        :return: The target_domain_id of this CreateV2WorkspaceRequestInput.
        :rtype: str
        """
        return self._target_domain_id

    @target_domain_id.setter
    def target_domain_id(self, target_domain_id):
        r"""Sets the target_domain_id of this CreateV2WorkspaceRequestInput.

        **参数解释**：目标租户Domain ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。

        :param target_domain_id: The target_domain_id of this CreateV2WorkspaceRequestInput.
        :type target_domain_id: str
        """
        self._target_domain_id = target_domain_id

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this CreateV2WorkspaceRequestInput.

        **参数解释**：目标租户Project ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。

        :return: The target_project_id of this CreateV2WorkspaceRequestInput.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this CreateV2WorkspaceRequestInput.

        **参数解释**：目标租户Project ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。

        :param target_project_id: The target_project_id of this CreateV2WorkspaceRequestInput.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

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
        if not isinstance(other, CreateV2WorkspaceRequestInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

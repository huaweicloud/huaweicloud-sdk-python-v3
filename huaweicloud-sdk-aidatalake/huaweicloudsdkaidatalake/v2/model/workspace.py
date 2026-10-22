# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Workspace:

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
        'name': 'str',
        'description': 'str',
        'create_time': 'datetime',
        'create_domain_name': 'str',
        'create_user_name': 'str',
        'metastore_id': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[ResourceTag]',
        'cross_tenant_access': 'bool',
        'target_domain_id': 'str',
        'target_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'create_time': 'create_time',
        'create_domain_name': 'create_domain_name',
        'create_user_name': 'create_user_name',
        'metastore_id': 'metastore_id',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'cross_tenant_access': 'cross_tenant_access',
        'target_domain_id': 'target_domain_id',
        'target_project_id': 'target_project_id'
    }

    def __init__(self, id=None, name=None, description=None, create_time=None, create_domain_name=None, create_user_name=None, metastore_id=None, enterprise_project_id=None, tags=None, cross_tenant_access=None, target_domain_id=None, target_project_id=None):
        r"""Workspace

        The model defined in huaweicloud sdk

        :param id: **参数解释**：工作空间ID。 **取值范围**：长度为1~36的英文字母、数字和中划线的组合。 
        :type id: str
        :param name: **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 
        :type name: str
        :param description: **参数解释**：用户输入的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~255个字符。 **默认取值**：不涉及。 
        :type description: str
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        :param create_domain_name: **参数解释**：创建账号名称。 **取值范围**：长度为0~64个英文字母、数字、下划线和中划线的组合。
        :type create_domain_name: str
        :param create_user_name: **参数解释**：创建用户名称。 **取值范围**：长度为0~64个英文字母、数字、下划线和中划线的组合。
        :type create_user_name: str
        :param metastore_id: **参数解释**：LakeFormation服务的实例ID，可在LakeFormation控制台实例列表中查看，或通过调用LakeFormation服务的查询实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字母、数字和中划线的组合。 **默认取值**：不涉及。 
        :type metastore_id: str
        :param enterprise_project_id: **参数解释**：企业项目ID，获取方法，请参见[获取企业项目ID](aidatalake_02_0042.xml)。 **约束限制**：不涉及。 **取值范围**：长度为0~128个英文字母、数字、下划线和中划线的组合。 **默认取值**：0。 
        :type enterprise_project_id: str
        :param tags: **参数解释**：工作空间的资源标签，每个元素为一个ResourceTag对象，包含key（标签键）和value（标签值）字段。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.ResourceTag`]
        :param cross_tenant_access: **参数解释**：是否跨租户访问。 **取值范围**：   - true：允许跨租户访问。   - false：不允许跨租户访问。
        :type cross_tenant_access: bool
        :param target_domain_id: **参数解释**：目标租户Domain ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。
        :type target_domain_id: str
        :param target_project_id: **参数解释**：目标租户Project ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。
        :type target_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._create_time = None
        self._create_domain_name = None
        self._create_user_name = None
        self._metastore_id = None
        self._enterprise_project_id = None
        self._tags = None
        self._cross_tenant_access = None
        self._target_domain_id = None
        self._target_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if create_domain_name is not None:
            self.create_domain_name = create_domain_name
        if create_user_name is not None:
            self.create_user_name = create_user_name
        if metastore_id is not None:
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
    def id(self):
        r"""Gets the id of this Workspace.

        **参数解释**：工作空间ID。 **取值范围**：长度为1~36的英文字母、数字和中划线的组合。 

        :return: The id of this Workspace.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Workspace.

        **参数解释**：工作空间ID。 **取值范围**：长度为1~36的英文字母、数字和中划线的组合。 

        :param id: The id of this Workspace.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Workspace.

        **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 

        :return: The name of this Workspace.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Workspace.

        **参数解释**：工作空间名称。 **约束限制**：不涉及。 **取值范围**：长度为4~32的英文字母、数字、下划线和中划线的组合。 **默认取值**：不涉及。 

        :param name: The name of this Workspace.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Workspace.

        **参数解释**：用户输入的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~255个字符。 **默认取值**：不涉及。 

        :return: The description of this Workspace.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Workspace.

        **参数解释**：用户输入的描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~255个字符。 **默认取值**：不涉及。 

        :param description: The description of this Workspace.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this Workspace.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this Workspace.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Workspace.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this Workspace.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_domain_name(self):
        r"""Gets the create_domain_name of this Workspace.

        **参数解释**：创建账号名称。 **取值范围**：长度为0~64个英文字母、数字、下划线和中划线的组合。

        :return: The create_domain_name of this Workspace.
        :rtype: str
        """
        return self._create_domain_name

    @create_domain_name.setter
    def create_domain_name(self, create_domain_name):
        r"""Sets the create_domain_name of this Workspace.

        **参数解释**：创建账号名称。 **取值范围**：长度为0~64个英文字母、数字、下划线和中划线的组合。

        :param create_domain_name: The create_domain_name of this Workspace.
        :type create_domain_name: str
        """
        self._create_domain_name = create_domain_name

    @property
    def create_user_name(self):
        r"""Gets the create_user_name of this Workspace.

        **参数解释**：创建用户名称。 **取值范围**：长度为0~64个英文字母、数字、下划线和中划线的组合。

        :return: The create_user_name of this Workspace.
        :rtype: str
        """
        return self._create_user_name

    @create_user_name.setter
    def create_user_name(self, create_user_name):
        r"""Sets the create_user_name of this Workspace.

        **参数解释**：创建用户名称。 **取值范围**：长度为0~64个英文字母、数字、下划线和中划线的组合。

        :param create_user_name: The create_user_name of this Workspace.
        :type create_user_name: str
        """
        self._create_user_name = create_user_name

    @property
    def metastore_id(self):
        r"""Gets the metastore_id of this Workspace.

        **参数解释**：LakeFormation服务的实例ID，可在LakeFormation控制台实例列表中查看，或通过调用LakeFormation服务的查询实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The metastore_id of this Workspace.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        r"""Sets the metastore_id of this Workspace.

        **参数解释**：LakeFormation服务的实例ID，可在LakeFormation控制台实例列表中查看，或通过调用LakeFormation服务的查询实例列表接口获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :param metastore_id: The metastore_id of this Workspace.
        :type metastore_id: str
        """
        self._metastore_id = metastore_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Workspace.

        **参数解释**：企业项目ID，获取方法，请参见[获取企业项目ID](aidatalake_02_0042.xml)。 **约束限制**：不涉及。 **取值范围**：长度为0~128个英文字母、数字、下划线和中划线的组合。 **默认取值**：0。 

        :return: The enterprise_project_id of this Workspace.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Workspace.

        **参数解释**：企业项目ID，获取方法，请参见[获取企业项目ID](aidatalake_02_0042.xml)。 **约束限制**：不涉及。 **取值范围**：长度为0~128个英文字母、数字、下划线和中划线的组合。 **默认取值**：0。 

        :param enterprise_project_id: The enterprise_project_id of this Workspace.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this Workspace.

        **参数解释**：工作空间的资源标签，每个元素为一个ResourceTag对象，包含key（标签键）和value（标签值）字段。 

        :return: The tags of this Workspace.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Workspace.

        **参数解释**：工作空间的资源标签，每个元素为一个ResourceTag对象，包含key（标签键）和value（标签值）字段。 

        :param tags: The tags of this Workspace.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.ResourceTag`]
        """
        self._tags = tags

    @property
    def cross_tenant_access(self):
        r"""Gets the cross_tenant_access of this Workspace.

        **参数解释**：是否跨租户访问。 **取值范围**：   - true：允许跨租户访问。   - false：不允许跨租户访问。

        :return: The cross_tenant_access of this Workspace.
        :rtype: bool
        """
        return self._cross_tenant_access

    @cross_tenant_access.setter
    def cross_tenant_access(self, cross_tenant_access):
        r"""Sets the cross_tenant_access of this Workspace.

        **参数解释**：是否跨租户访问。 **取值范围**：   - true：允许跨租户访问。   - false：不允许跨租户访问。

        :param cross_tenant_access: The cross_tenant_access of this Workspace.
        :type cross_tenant_access: bool
        """
        self._cross_tenant_access = cross_tenant_access

    @property
    def target_domain_id(self):
        r"""Gets the target_domain_id of this Workspace.

        **参数解释**：目标租户Domain ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。

        :return: The target_domain_id of this Workspace.
        :rtype: str
        """
        return self._target_domain_id

    @target_domain_id.setter
    def target_domain_id(self, target_domain_id):
        r"""Sets the target_domain_id of this Workspace.

        **参数解释**：目标租户Domain ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。

        :param target_domain_id: The target_domain_id of this Workspace.
        :type target_domain_id: str
        """
        self._target_domain_id = target_domain_id

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this Workspace.

        **参数解释**：目标租户Project ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。

        :return: The target_project_id of this Workspace.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this Workspace.

        **参数解释**：目标租户Project ID。 **取值范围**：长度为1~64的英文字母、数字和中划线的组合。

        :param target_project_id: The target_project_id of this Workspace.
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
        if not isinstance(other, Workspace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

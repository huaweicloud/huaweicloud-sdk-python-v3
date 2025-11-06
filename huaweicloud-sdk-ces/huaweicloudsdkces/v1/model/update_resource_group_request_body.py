# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResourceGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'resources': 'list[CreateResourceGroup]',
        'type': 'str',
        'relation_ids': 'list[str]',
        'tags': 'list[ResourceGroupTagRelation]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'resources': 'resources',
        'type': 'type',
        'relation_ids': 'relation_ids',
        'tags': 'tags'
    }

    def __init__(self, group_name=None, resources=None, type=None, relation_ids=None, tags=None):
        r"""UpdateResourceGroupRequestBody

        The model defined in huaweicloud sdk

        :param group_name: **参数解释** 资源分组的名称 **约束限制** 不涉及 **取值范围** 只能为字母、数字、汉字、-或_，长度为[1,128]个字符 **默认取值** 不涉及 
        :type group_name: str
        :param resources: **参数解释** 手动创建时的资源详情。 **约束限制** 不超过1000个资源。 
        :type resources: list[:class:`huaweicloudsdkces.v1.CreateResourceGroup`]
        :param type: **参数解释** 资源分组添加资源方式 **约束限制** 不涉及 **取值范围** 取值只能为EPS（同步企业项目），TAG（标签动态匹配），不传为手动添加。 **默认取值** 不涉及 
        :type type: str
        :param relation_ids: **参数解释** 该资源分组内包含的资源来源的企业项目ID。 **约束限制** type为EPS时必传，不超过50个企业项目ID。 
        :type relation_ids: list[str]
        :param tags: **参数解释** 标签动态匹配时的关联标签。 **约束限制** type为TAG时必传，不超过50个标签。 
        :type tags: list[:class:`huaweicloudsdkces.v1.ResourceGroupTagRelation`]
        """
        
        

        self._group_name = None
        self._resources = None
        self._type = None
        self._relation_ids = None
        self._tags = None
        self.discriminator = None

        self.group_name = group_name
        if resources is not None:
            self.resources = resources
        if type is not None:
            self.type = type
        if relation_ids is not None:
            self.relation_ids = relation_ids
        if tags is not None:
            self.tags = tags

    @property
    def group_name(self):
        r"""Gets the group_name of this UpdateResourceGroupRequestBody.

        **参数解释** 资源分组的名称 **约束限制** 不涉及 **取值范围** 只能为字母、数字、汉字、-或_，长度为[1,128]个字符 **默认取值** 不涉及 

        :return: The group_name of this UpdateResourceGroupRequestBody.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this UpdateResourceGroupRequestBody.

        **参数解释** 资源分组的名称 **约束限制** 不涉及 **取值范围** 只能为字母、数字、汉字、-或_，长度为[1,128]个字符 **默认取值** 不涉及 

        :param group_name: The group_name of this UpdateResourceGroupRequestBody.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def resources(self):
        r"""Gets the resources of this UpdateResourceGroupRequestBody.

        **参数解释** 手动创建时的资源详情。 **约束限制** 不超过1000个资源。 

        :return: The resources of this UpdateResourceGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.CreateResourceGroup`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this UpdateResourceGroupRequestBody.

        **参数解释** 手动创建时的资源详情。 **约束限制** 不超过1000个资源。 

        :param resources: The resources of this UpdateResourceGroupRequestBody.
        :type resources: list[:class:`huaweicloudsdkces.v1.CreateResourceGroup`]
        """
        self._resources = resources

    @property
    def type(self):
        r"""Gets the type of this UpdateResourceGroupRequestBody.

        **参数解释** 资源分组添加资源方式 **约束限制** 不涉及 **取值范围** 取值只能为EPS（同步企业项目），TAG（标签动态匹配），不传为手动添加。 **默认取值** 不涉及 

        :return: The type of this UpdateResourceGroupRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateResourceGroupRequestBody.

        **参数解释** 资源分组添加资源方式 **约束限制** 不涉及 **取值范围** 取值只能为EPS（同步企业项目），TAG（标签动态匹配），不传为手动添加。 **默认取值** 不涉及 

        :param type: The type of this UpdateResourceGroupRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def relation_ids(self):
        r"""Gets the relation_ids of this UpdateResourceGroupRequestBody.

        **参数解释** 该资源分组内包含的资源来源的企业项目ID。 **约束限制** type为EPS时必传，不超过50个企业项目ID。 

        :return: The relation_ids of this UpdateResourceGroupRequestBody.
        :rtype: list[str]
        """
        return self._relation_ids

    @relation_ids.setter
    def relation_ids(self, relation_ids):
        r"""Sets the relation_ids of this UpdateResourceGroupRequestBody.

        **参数解释** 该资源分组内包含的资源来源的企业项目ID。 **约束限制** type为EPS时必传，不超过50个企业项目ID。 

        :param relation_ids: The relation_ids of this UpdateResourceGroupRequestBody.
        :type relation_ids: list[str]
        """
        self._relation_ids = relation_ids

    @property
    def tags(self):
        r"""Gets the tags of this UpdateResourceGroupRequestBody.

        **参数解释** 标签动态匹配时的关联标签。 **约束限制** type为TAG时必传，不超过50个标签。 

        :return: The tags of this UpdateResourceGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkces.v1.ResourceGroupTagRelation`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateResourceGroupRequestBody.

        **参数解释** 标签动态匹配时的关联标签。 **约束限制** type为TAG时必传，不超过50个标签。 

        :param tags: The tags of this UpdateResourceGroupRequestBody.
        :type tags: list[:class:`huaweicloudsdkces.v1.ResourceGroupTagRelation`]
        """
        self._tags = tags

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
        if not isinstance(other, UpdateResourceGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResourceViewsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organization_unit_ids': 'list[str]',
        'resource_types': 'list[str]',
        'organization_id': 'str',
        'view_type': 'str',
        'name': 'str',
        'domain_ids': 'list[str]'
    }

    attribute_map = {
        'organization_unit_ids': 'organization_unit_ids',
        'resource_types': 'resource_types',
        'organization_id': 'organization_id',
        'view_type': 'view_type',
        'name': 'name',
        'domain_ids': 'domain_ids'
    }

    def __init__(self, organization_unit_ids=None, resource_types=None, organization_id=None, view_type=None, name=None, domain_ids=None):
        r"""UpdateResourceViewsRequestBody

        The model defined in huaweicloud sdk

        :param organization_unit_ids: **参数解释：** 组织单元id。 **约束限制：** 不涉及。 **取值范围：** 自定义，视图所聚合的组织单元id列表。 **默认取值：** 不涉及。
        :type organization_unit_ids: list[str]
        :param resource_types: **参数解释：** 资源类型列表。 **约束限制：** 不涉及。 **取值范围：** 自定义，用户创建视图时，选择的资源，资源对应类别组合成资源类型列表。 **默认取值：** 不涉及
        :type resource_types: list[str]
        :param organization_id: **参数解释：** 组织ID。 **约束限制：** 不涉及。 **取值范围：** 视图归属的组织id。 **默认取值：** 不涉及。
        :type organization_id: str
        :param view_type: **参数解释：** 视图类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type view_type: str
        :param name: **参数解释：** 视图名称。 **约束限制：** 不涉及。 **取值范围：** 用户自定义编辑。 **默认取值：** 不涉及。
        :type name: str
        :param domain_ids: **参数解释：** 视图包含的租户账号id值组成列表。 **取值范围：** 不涉及。 example:   - id1   - id2
        :type domain_ids: list[str]
        """
        
        

        self._organization_unit_ids = None
        self._resource_types = None
        self._organization_id = None
        self._view_type = None
        self._name = None
        self._domain_ids = None
        self.discriminator = None

        self.organization_unit_ids = organization_unit_ids
        self.resource_types = resource_types
        if organization_id is not None:
            self.organization_id = organization_id
        self.view_type = view_type
        self.name = name
        if domain_ids is not None:
            self.domain_ids = domain_ids

    @property
    def organization_unit_ids(self):
        r"""Gets the organization_unit_ids of this UpdateResourceViewsRequestBody.

        **参数解释：** 组织单元id。 **约束限制：** 不涉及。 **取值范围：** 自定义，视图所聚合的组织单元id列表。 **默认取值：** 不涉及。

        :return: The organization_unit_ids of this UpdateResourceViewsRequestBody.
        :rtype: list[str]
        """
        return self._organization_unit_ids

    @organization_unit_ids.setter
    def organization_unit_ids(self, organization_unit_ids):
        r"""Sets the organization_unit_ids of this UpdateResourceViewsRequestBody.

        **参数解释：** 组织单元id。 **约束限制：** 不涉及。 **取值范围：** 自定义，视图所聚合的组织单元id列表。 **默认取值：** 不涉及。

        :param organization_unit_ids: The organization_unit_ids of this UpdateResourceViewsRequestBody.
        :type organization_unit_ids: list[str]
        """
        self._organization_unit_ids = organization_unit_ids

    @property
    def resource_types(self):
        r"""Gets the resource_types of this UpdateResourceViewsRequestBody.

        **参数解释：** 资源类型列表。 **约束限制：** 不涉及。 **取值范围：** 自定义，用户创建视图时，选择的资源，资源对应类别组合成资源类型列表。 **默认取值：** 不涉及

        :return: The resource_types of this UpdateResourceViewsRequestBody.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        r"""Sets the resource_types of this UpdateResourceViewsRequestBody.

        **参数解释：** 资源类型列表。 **约束限制：** 不涉及。 **取值范围：** 自定义，用户创建视图时，选择的资源，资源对应类别组合成资源类型列表。 **默认取值：** 不涉及

        :param resource_types: The resource_types of this UpdateResourceViewsRequestBody.
        :type resource_types: list[str]
        """
        self._resource_types = resource_types

    @property
    def organization_id(self):
        r"""Gets the organization_id of this UpdateResourceViewsRequestBody.

        **参数解释：** 组织ID。 **约束限制：** 不涉及。 **取值范围：** 视图归属的组织id。 **默认取值：** 不涉及。

        :return: The organization_id of this UpdateResourceViewsRequestBody.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this UpdateResourceViewsRequestBody.

        **参数解释：** 组织ID。 **约束限制：** 不涉及。 **取值范围：** 视图归属的组织id。 **默认取值：** 不涉及。

        :param organization_id: The organization_id of this UpdateResourceViewsRequestBody.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def view_type(self):
        r"""Gets the view_type of this UpdateResourceViewsRequestBody.

        **参数解释：** 视图类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The view_type of this UpdateResourceViewsRequestBody.
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        r"""Sets the view_type of this UpdateResourceViewsRequestBody.

        **参数解释：** 视图类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param view_type: The view_type of this UpdateResourceViewsRequestBody.
        :type view_type: str
        """
        self._view_type = view_type

    @property
    def name(self):
        r"""Gets the name of this UpdateResourceViewsRequestBody.

        **参数解释：** 视图名称。 **约束限制：** 不涉及。 **取值范围：** 用户自定义编辑。 **默认取值：** 不涉及。

        :return: The name of this UpdateResourceViewsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateResourceViewsRequestBody.

        **参数解释：** 视图名称。 **约束限制：** 不涉及。 **取值范围：** 用户自定义编辑。 **默认取值：** 不涉及。

        :param name: The name of this UpdateResourceViewsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def domain_ids(self):
        r"""Gets the domain_ids of this UpdateResourceViewsRequestBody.

        **参数解释：** 视图包含的租户账号id值组成列表。 **取值范围：** 不涉及。 example:   - id1   - id2

        :return: The domain_ids of this UpdateResourceViewsRequestBody.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        r"""Sets the domain_ids of this UpdateResourceViewsRequestBody.

        **参数解释：** 视图包含的租户账号id值组成列表。 **取值范围：** 不涉及。 example:   - id1   - id2

        :param domain_ids: The domain_ids of this UpdateResourceViewsRequestBody.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

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
        if not isinstance(other, UpdateResourceViewsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

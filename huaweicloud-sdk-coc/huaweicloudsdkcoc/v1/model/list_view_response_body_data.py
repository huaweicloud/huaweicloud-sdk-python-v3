# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListViewResponseBodyData:

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
        'manager_domain_id': 'str',
        'organization_id': 'str',
        'organization_unit_ids': 'list[str]',
        'domain_ids': 'list[str]',
        'resource_types': 'list[str]',
        'view_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'manager_domain_id': 'manager_domain_id',
        'organization_id': 'organization_id',
        'organization_unit_ids': 'organization_unit_ids',
        'domain_ids': 'domain_ids',
        'resource_types': 'resource_types',
        'view_type': 'view_type'
    }

    def __init__(self, id=None, name=None, manager_domain_id=None, organization_id=None, organization_unit_ids=None, domain_ids=None, resource_types=None, view_type=None):
        r"""ListViewResponseBodyData

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 资源视图id。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 资源视图名称。 **取值范围：** 不涉及。
        :type name: str
        :param manager_domain_id: **参数解释：** 视图创建者的domainId，视图资源聚合的归属者。 **取值范围：** 不涉及。
        :type manager_domain_id: str
        :param organization_id: **参数解释：** 视图归属的组织id。 **取值范围：** 不涉及。
        :type organization_id: str
        :param organization_unit_ids: **参数解释：** 视图所聚合的组织单元id列表。 **取值范围：** 不涉及。
        :type organization_unit_ids: list[str]
        :param domain_ids: **参数解释：** 视图包含的租户账号id列表。 **取值范围：** 不涉及。
        :type domain_ids: list[str]
        :param resource_types: **参数解释：** 视图包含的资源类型列表。 **取值范围：** 不涉及。
        :type resource_types: list[str]
        :param view_type: **参数解释：** 视图类型。 **取值范围：** 不涉及。
        :type view_type: str
        """
        
        

        self._id = None
        self._name = None
        self._manager_domain_id = None
        self._organization_id = None
        self._organization_unit_ids = None
        self._domain_ids = None
        self._resource_types = None
        self._view_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if manager_domain_id is not None:
            self.manager_domain_id = manager_domain_id
        if organization_id is not None:
            self.organization_id = organization_id
        if organization_unit_ids is not None:
            self.organization_unit_ids = organization_unit_ids
        if domain_ids is not None:
            self.domain_ids = domain_ids
        if resource_types is not None:
            self.resource_types = resource_types
        if view_type is not None:
            self.view_type = view_type

    @property
    def id(self):
        r"""Gets the id of this ListViewResponseBodyData.

        **参数解释：** 资源视图id。 **取值范围：** 不涉及。

        :return: The id of this ListViewResponseBodyData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListViewResponseBodyData.

        **参数解释：** 资源视图id。 **取值范围：** 不涉及。

        :param id: The id of this ListViewResponseBodyData.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListViewResponseBodyData.

        **参数解释：** 资源视图名称。 **取值范围：** 不涉及。

        :return: The name of this ListViewResponseBodyData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListViewResponseBodyData.

        **参数解释：** 资源视图名称。 **取值范围：** 不涉及。

        :param name: The name of this ListViewResponseBodyData.
        :type name: str
        """
        self._name = name

    @property
    def manager_domain_id(self):
        r"""Gets the manager_domain_id of this ListViewResponseBodyData.

        **参数解释：** 视图创建者的domainId，视图资源聚合的归属者。 **取值范围：** 不涉及。

        :return: The manager_domain_id of this ListViewResponseBodyData.
        :rtype: str
        """
        return self._manager_domain_id

    @manager_domain_id.setter
    def manager_domain_id(self, manager_domain_id):
        r"""Sets the manager_domain_id of this ListViewResponseBodyData.

        **参数解释：** 视图创建者的domainId，视图资源聚合的归属者。 **取值范围：** 不涉及。

        :param manager_domain_id: The manager_domain_id of this ListViewResponseBodyData.
        :type manager_domain_id: str
        """
        self._manager_domain_id = manager_domain_id

    @property
    def organization_id(self):
        r"""Gets the organization_id of this ListViewResponseBodyData.

        **参数解释：** 视图归属的组织id。 **取值范围：** 不涉及。

        :return: The organization_id of this ListViewResponseBodyData.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this ListViewResponseBodyData.

        **参数解释：** 视图归属的组织id。 **取值范围：** 不涉及。

        :param organization_id: The organization_id of this ListViewResponseBodyData.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def organization_unit_ids(self):
        r"""Gets the organization_unit_ids of this ListViewResponseBodyData.

        **参数解释：** 视图所聚合的组织单元id列表。 **取值范围：** 不涉及。

        :return: The organization_unit_ids of this ListViewResponseBodyData.
        :rtype: list[str]
        """
        return self._organization_unit_ids

    @organization_unit_ids.setter
    def organization_unit_ids(self, organization_unit_ids):
        r"""Sets the organization_unit_ids of this ListViewResponseBodyData.

        **参数解释：** 视图所聚合的组织单元id列表。 **取值范围：** 不涉及。

        :param organization_unit_ids: The organization_unit_ids of this ListViewResponseBodyData.
        :type organization_unit_ids: list[str]
        """
        self._organization_unit_ids = organization_unit_ids

    @property
    def domain_ids(self):
        r"""Gets the domain_ids of this ListViewResponseBodyData.

        **参数解释：** 视图包含的租户账号id列表。 **取值范围：** 不涉及。

        :return: The domain_ids of this ListViewResponseBodyData.
        :rtype: list[str]
        """
        return self._domain_ids

    @domain_ids.setter
    def domain_ids(self, domain_ids):
        r"""Sets the domain_ids of this ListViewResponseBodyData.

        **参数解释：** 视图包含的租户账号id列表。 **取值范围：** 不涉及。

        :param domain_ids: The domain_ids of this ListViewResponseBodyData.
        :type domain_ids: list[str]
        """
        self._domain_ids = domain_ids

    @property
    def resource_types(self):
        r"""Gets the resource_types of this ListViewResponseBodyData.

        **参数解释：** 视图包含的资源类型列表。 **取值范围：** 不涉及。

        :return: The resource_types of this ListViewResponseBodyData.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        r"""Sets the resource_types of this ListViewResponseBodyData.

        **参数解释：** 视图包含的资源类型列表。 **取值范围：** 不涉及。

        :param resource_types: The resource_types of this ListViewResponseBodyData.
        :type resource_types: list[str]
        """
        self._resource_types = resource_types

    @property
    def view_type(self):
        r"""Gets the view_type of this ListViewResponseBodyData.

        **参数解释：** 视图类型。 **取值范围：** 不涉及。

        :return: The view_type of this ListViewResponseBodyData.
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        r"""Sets the view_type of this ListViewResponseBodyData.

        **参数解释：** 视图类型。 **取值范围：** 不涉及。

        :param view_type: The view_type of this ListViewResponseBodyData.
        :type view_type: str
        """
        self._view_type = view_type

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
        if not isinstance(other, ListViewResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'ip_list': 'list[str]',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'ip_list': 'ip_list',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, id=None, name=None, description=None, ip_list=None, enterprise_project_id=None):
        r"""ListIpGroupsRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param id: **参数解释**：IP地址组的ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param name: **参数解释**：IP地址组的名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param description: **参数解释**：IP地址组的描述。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: list[str]
        :param ip_list: **参数解释**：IP地址组的IP地址。若一次传入多个，则查询满足任意一个IP地址的所有IP地址组。 注意：不管是单个IP、网段还是连续地址段，都全匹配查询。比如存在IP地址组的IP地址是127.0.0.1-127.0.0.10，则需要传入ip_list&#x3D;127.0.0.1-127.0.0.10 才能查询到。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type ip_list: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:ipgroups:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._ip_list = None
        self._enterprise_project_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ip_list is not None:
            self.ip_list = ip_list
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def marker(self):
        r"""Gets the marker of this ListIpGroupsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListIpGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListIpGroupsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListIpGroupsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListIpGroupsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListIpGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIpGroupsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListIpGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListIpGroupsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListIpGroupsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListIpGroupsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListIpGroupsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListIpGroupsRequest.

        **参数解释**：IP地址组的ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListIpGroupsRequest.

        **参数解释**：IP地址组的ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListIpGroupsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListIpGroupsRequest.

        **参数解释**：IP地址组的名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListIpGroupsRequest.

        **参数解释**：IP地址组的名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListIpGroupsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListIpGroupsRequest.

        **参数解释**：IP地址组的描述。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListIpGroupsRequest.

        **参数解释**：IP地址组的描述。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this ListIpGroupsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def ip_list(self):
        r"""Gets the ip_list of this ListIpGroupsRequest.

        **参数解释**：IP地址组的IP地址。若一次传入多个，则查询满足任意一个IP地址的所有IP地址组。 注意：不管是单个IP、网段还是连续地址段，都全匹配查询。比如存在IP地址组的IP地址是127.0.0.1-127.0.0.10，则需要传入ip_list=127.0.0.1-127.0.0.10 才能查询到。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The ip_list of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this ListIpGroupsRequest.

        **参数解释**：IP地址组的IP地址。若一次传入多个，则查询满足任意一个IP地址的所有IP地址组。 注意：不管是单个IP、网段还是连续地址段，都全匹配查询。比如存在IP地址组的IP地址是127.0.0.1-127.0.0.10，则需要传入ip_list=127.0.0.1-127.0.0.10 才能查询到。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param ip_list: The ip_list of this ListIpGroupsRequest.
        :type ip_list: list[str]
        """
        self._ip_list = ip_list

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListIpGroupsRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:ipgroups:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this ListIpGroupsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListIpGroupsRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:ipgroups:list权限。 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListIpGroupsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListIpGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

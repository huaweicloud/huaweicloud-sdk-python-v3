# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListL7RulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'l7policy_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'compare_type': 'list[str]',
        'provisioning_status': 'list[str]',
        'invert': 'bool',
        'admin_state_up': 'bool',
        'value': 'list[str]',
        'key': 'list[str]',
        'type': 'list[str]',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'l7policy_id': 'l7policy_id',
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'compare_type': 'compare_type',
        'provisioning_status': 'provisioning_status',
        'invert': 'invert',
        'admin_state_up': 'admin_state_up',
        'value': 'value',
        'key': 'key',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, l7policy_id=None, limit=None, marker=None, page_reverse=None, id=None, compare_type=None, provisioning_status=None, invert=None, admin_state_up=None, value=None, key=None, type=None, enterprise_project_id=None):
        r"""ListL7RulesRequest

        The model defined in huaweicloud sdk

        :param l7policy_id: **参数解释**：策略ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type l7policy_id: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param id: **参数解释**：转发规则ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param compare_type: **参数解释**：转发匹配方式。 支持多值查询，查询条件格式：*compare_type&#x3D;xxx&amp;compare_type&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**： - EQUAL_TO 表示精确匹配。 - REGEX 表示正则匹配。 - STARTS_WITH 表示前缀匹配。  **默认取值**：不涉及
        :type compare_type: list[str]
        :param provisioning_status: **参数解释**：转发规则的配置状态。 支持多值查询，查询条件格式：*provisioning_status&#x3D;xxx&amp;provisioning_status&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：ACTIVE 表示正常。  **默认取值**：不涉及
        :type provisioning_status: list[str]
        :param invert: **参数解释**：是否反向匹配。  **约束限制**：不涉及  **取值范围**：false  **默认取值**：不涉及
        :type invert: bool
        :param admin_state_up: **参数解释**：转发规则的管理状态。 不支持该字段，请勿使用。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type admin_state_up: bool
        :param value: **参数解释**：匹配内容的值。 支持多值查询，查询条件格式：*value&#x3D;xxx&amp;value&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type value: list[str]
        :param key: **参数解释**：匹配内容的键值，用于标识规则。 支持多值查询，查询条件格式：*key&#x3D;xxx&amp;key&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type key: list[str]
        :param type: **参数解释**：匹配类别，可以为HOST_NAME，PATH。 支持多值查询，查询条件格式：*type&#x3D;xxx&amp;type&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type type: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:l7rules:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: list[str]
        """
        
        

        self._l7policy_id = None
        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._compare_type = None
        self._provisioning_status = None
        self._invert = None
        self._admin_state_up = None
        self._value = None
        self._key = None
        self._type = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.l7policy_id = l7policy_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if compare_type is not None:
            self.compare_type = compare_type
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if invert is not None:
            self.invert = invert
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if value is not None:
            self.value = value
        if key is not None:
            self.key = key
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def l7policy_id(self):
        r"""Gets the l7policy_id of this ListL7RulesRequest.

        **参数解释**：策略ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The l7policy_id of this ListL7RulesRequest.
        :rtype: str
        """
        return self._l7policy_id

    @l7policy_id.setter
    def l7policy_id(self, l7policy_id):
        r"""Sets the l7policy_id of this ListL7RulesRequest.

        **参数解释**：策略ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param l7policy_id: The l7policy_id of this ListL7RulesRequest.
        :type l7policy_id: str
        """
        self._l7policy_id = l7policy_id

    @property
    def limit(self):
        r"""Gets the limit of this ListL7RulesRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListL7RulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListL7RulesRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListL7RulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListL7RulesRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListL7RulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListL7RulesRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListL7RulesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListL7RulesRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListL7RulesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListL7RulesRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListL7RulesRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListL7RulesRequest.

        **参数解释**：转发规则ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListL7RulesRequest.

        **参数解释**：转发规则ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListL7RulesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def compare_type(self):
        r"""Gets the compare_type of this ListL7RulesRequest.

        **参数解释**：转发匹配方式。 支持多值查询，查询条件格式：*compare_type=xxx&compare_type=xxx*。  **约束限制**：不涉及  **取值范围**： - EQUAL_TO 表示精确匹配。 - REGEX 表示正则匹配。 - STARTS_WITH 表示前缀匹配。  **默认取值**：不涉及

        :return: The compare_type of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        r"""Sets the compare_type of this ListL7RulesRequest.

        **参数解释**：转发匹配方式。 支持多值查询，查询条件格式：*compare_type=xxx&compare_type=xxx*。  **约束限制**：不涉及  **取值范围**： - EQUAL_TO 表示精确匹配。 - REGEX 表示正则匹配。 - STARTS_WITH 表示前缀匹配。  **默认取值**：不涉及

        :param compare_type: The compare_type of this ListL7RulesRequest.
        :type compare_type: list[str]
        """
        self._compare_type = compare_type

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this ListL7RulesRequest.

        **参数解释**：转发规则的配置状态。 支持多值查询，查询条件格式：*provisioning_status=xxx&provisioning_status=xxx*。  **约束限制**：不涉及  **取值范围**：ACTIVE 表示正常。  **默认取值**：不涉及

        :return: The provisioning_status of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this ListL7RulesRequest.

        **参数解释**：转发规则的配置状态。 支持多值查询，查询条件格式：*provisioning_status=xxx&provisioning_status=xxx*。  **约束限制**：不涉及  **取值范围**：ACTIVE 表示正常。  **默认取值**：不涉及

        :param provisioning_status: The provisioning_status of this ListL7RulesRequest.
        :type provisioning_status: list[str]
        """
        self._provisioning_status = provisioning_status

    @property
    def invert(self):
        r"""Gets the invert of this ListL7RulesRequest.

        **参数解释**：是否反向匹配。  **约束限制**：不涉及  **取值范围**：false  **默认取值**：不涉及

        :return: The invert of this ListL7RulesRequest.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        r"""Sets the invert of this ListL7RulesRequest.

        **参数解释**：是否反向匹配。  **约束限制**：不涉及  **取值范围**：false  **默认取值**：不涉及

        :param invert: The invert of this ListL7RulesRequest.
        :type invert: bool
        """
        self._invert = invert

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListL7RulesRequest.

        **参数解释**：转发规则的管理状态。 不支持该字段，请勿使用。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The admin_state_up of this ListL7RulesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListL7RulesRequest.

        **参数解释**：转发规则的管理状态。 不支持该字段，请勿使用。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param admin_state_up: The admin_state_up of this ListL7RulesRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def value(self):
        r"""Gets the value of this ListL7RulesRequest.

        **参数解释**：匹配内容的值。 支持多值查询，查询条件格式：*value=xxx&value=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The value of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ListL7RulesRequest.

        **参数解释**：匹配内容的值。 支持多值查询，查询条件格式：*value=xxx&value=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param value: The value of this ListL7RulesRequest.
        :type value: list[str]
        """
        self._value = value

    @property
    def key(self):
        r"""Gets the key of this ListL7RulesRequest.

        **参数解释**：匹配内容的键值，用于标识规则。 支持多值查询，查询条件格式：*key=xxx&key=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The key of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ListL7RulesRequest.

        **参数解释**：匹配内容的键值，用于标识规则。 支持多值查询，查询条件格式：*key=xxx&key=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param key: The key of this ListL7RulesRequest.
        :type key: list[str]
        """
        self._key = key

    @property
    def type(self):
        r"""Gets the type of this ListL7RulesRequest.

        **参数解释**：匹配类别，可以为HOST_NAME，PATH。 支持多值查询，查询条件格式：*type=xxx&type=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The type of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListL7RulesRequest.

        **参数解释**：匹配类别，可以为HOST_NAME，PATH。 支持多值查询，查询条件格式：*type=xxx&type=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param type: The type of this ListL7RulesRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListL7RulesRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:l7rules:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this ListL7RulesRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListL7RulesRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:l7rules:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListL7RulesRequest.
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
        if not isinstance(other, ListL7RulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

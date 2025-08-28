# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListL7PoliciesRequest:

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
        'enterprise_project_id': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'admin_state_up': 'bool',
        'listener_id': 'list[str]',
        'position': 'list[int]',
        'action': 'list[str]',
        'redirect_url': 'list[str]',
        'redirect_pool_id': 'list[str]',
        'redirect_listener_id': 'list[str]',
        'provisioning_status': 'list[str]',
        'display_all_rules': 'bool',
        'priority': 'list[int]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'listener_id': 'listener_id',
        'position': 'position',
        'action': 'action',
        'redirect_url': 'redirect_url',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_listener_id': 'redirect_listener_id',
        'provisioning_status': 'provisioning_status',
        'display_all_rules': 'display_all_rules',
        'priority': 'priority'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, enterprise_project_id=None, id=None, name=None, description=None, admin_state_up=None, listener_id=None, position=None, action=None, redirect_url=None, redirect_pool_id=None, redirect_listener_id=None, provisioning_status=None, display_all_rules=None, priority=None):
        r"""ListL7PoliciesRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:l7policies:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: list[str]
        :param id: **参数解释**：转发策略ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param name: **参数解释**：转发策略名称。 支持多值查询，查询条件格式：**name&#x3D;xxx&amp;name&#x3D;xxx**。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param description: **参数解释**：转发策略额描述信息。 支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: list[str]
        :param admin_state_up: **参数解释**：转发策略的管理状态。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type admin_state_up: bool
        :param listener_id: **参数解释**：转发策略所属的监听器ID。 支持多值查询，查询条件格式：*******listener_id&#x3D;xxx&amp;listener_id&#x3D;xxx*******。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type listener_id: list[str]
        :param position: **参数解释**：转发策略的优先级。 支持多值查询，查询条件格式：****position&#x3D;xxx&amp;position&#x3D;xxx****。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type position: list[int]
        :param action: **参数解释**：转发策略的转发动作。 支持多值查询，查询条件格式：*****action&#x3D;xxx&amp;action&#x3D;xxx*****。  **约束限制**：不涉及  **取值范围**： - REDIRECT_TO_POOL：转发到后端服务器组。 - REDIRECT_TO_LISTENER：重定向到监听器。 - REDIRECT_TO_URL：重定向到URL。 - FIXED_RESPONSE：返回固定响应体。  **默认取值**：不涉及
        :type action: list[str]
        :param redirect_url: **参数解释**：转发到的url。 支持多值查询，查询条件格式：****redirect_url&#x3D;xxx&amp;redirect_url&#x3D;xxx****。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  不支持该字段，请勿使用。
        :type redirect_url: list[str]
        :param redirect_pool_id: **参数解释**：转发到pool的ID。 支持多值查询，查询条件格式：***redirect_pool_id&#x3D;xxx&amp;redirect_pool_id&#x3D;xxx***。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type redirect_pool_id: list[str]
        :param redirect_listener_id: **参数解释**：转发到的listener的ID。 支持多值查询，查询条件格式：**redirect_listener_id&#x3D;xxx&amp;redirect_listener_id&#x3D;xxx**。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type redirect_listener_id: list[str]
        :param provisioning_status: **参数解释**：转发策略的配置状态。 支持多值查询，查询条件格式：*provisioning_status&#x3D;xxx&amp;provisioning_status&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**： - ACTIVE: 表示正常。 - ERROR: 表示当前策略与同一监听器下的其他策略存在相同的规则配置。  **默认取值**：不涉及
        :type provisioning_status: list[str]
        :param display_all_rules: **参数解释**：是否显示转发策略下的rule详细信息。  **约束限制**：不涉及  **取值范围**： - true：显示policy下面的rule的详细信息。 - false：只显示policy下面的rule的id信息。  **默认取值**：不涉及
        :type display_all_rules: bool
        :param priority: **参数解释**：转发策略的优先级。数值越小，优先级越高。 支持多值查询，查询条件格式：*priority&#x3D;xxx&amp;priority&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hcso_dt)
        :type priority: list[int]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._enterprise_project_id = None
        self._id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._listener_id = None
        self._position = None
        self._action = None
        self._redirect_url = None
        self._redirect_pool_id = None
        self._redirect_listener_id = None
        self._provisioning_status = None
        self._display_all_rules = None
        self._priority = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if listener_id is not None:
            self.listener_id = listener_id
        if position is not None:
            self.position = position
        if action is not None:
            self.action = action
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if redirect_pool_id is not None:
            self.redirect_pool_id = redirect_pool_id
        if redirect_listener_id is not None:
            self.redirect_listener_id = redirect_listener_id
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if display_all_rules is not None:
            self.display_all_rules = display_all_rules
        if priority is not None:
            self.priority = priority

    @property
    def marker(self):
        r"""Gets the marker of this ListL7PoliciesRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListL7PoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListL7PoliciesRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListL7PoliciesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListL7PoliciesRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListL7PoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListL7PoliciesRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListL7PoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListL7PoliciesRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListL7PoliciesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListL7PoliciesRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListL7PoliciesRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListL7PoliciesRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:l7policies:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListL7PoliciesRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:l7policies:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListL7PoliciesRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this ListL7PoliciesRequest.

        **参数解释**：转发策略ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListL7PoliciesRequest.

        **参数解释**：转发策略ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListL7PoliciesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListL7PoliciesRequest.

        **参数解释**：转发策略名称。 支持多值查询，查询条件格式：**name=xxx&name=xxx**。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListL7PoliciesRequest.

        **参数解释**：转发策略名称。 支持多值查询，查询条件格式：**name=xxx&name=xxx**。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListL7PoliciesRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListL7PoliciesRequest.

        **参数解释**：转发策略额描述信息。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListL7PoliciesRequest.

        **参数解释**：转发策略额描述信息。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this ListL7PoliciesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListL7PoliciesRequest.

        **参数解释**：转发策略的管理状态。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The admin_state_up of this ListL7PoliciesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListL7PoliciesRequest.

        **参数解释**：转发策略的管理状态。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param admin_state_up: The admin_state_up of this ListL7PoliciesRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def listener_id(self):
        r"""Gets the listener_id of this ListL7PoliciesRequest.

        **参数解释**：转发策略所属的监听器ID。 支持多值查询，查询条件格式：*******listener_id=xxx&listener_id=xxx*******。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The listener_id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this ListL7PoliciesRequest.

        **参数解释**：转发策略所属的监听器ID。 支持多值查询，查询条件格式：*******listener_id=xxx&listener_id=xxx*******。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param listener_id: The listener_id of this ListL7PoliciesRequest.
        :type listener_id: list[str]
        """
        self._listener_id = listener_id

    @property
    def position(self):
        r"""Gets the position of this ListL7PoliciesRequest.

        **参数解释**：转发策略的优先级。 支持多值查询，查询条件格式：****position=xxx&position=xxx****。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The position of this ListL7PoliciesRequest.
        :rtype: list[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this ListL7PoliciesRequest.

        **参数解释**：转发策略的优先级。 支持多值查询，查询条件格式：****position=xxx&position=xxx****。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param position: The position of this ListL7PoliciesRequest.
        :type position: list[int]
        """
        self._position = position

    @property
    def action(self):
        r"""Gets the action of this ListL7PoliciesRequest.

        **参数解释**：转发策略的转发动作。 支持多值查询，查询条件格式：*****action=xxx&action=xxx*****。  **约束限制**：不涉及  **取值范围**： - REDIRECT_TO_POOL：转发到后端服务器组。 - REDIRECT_TO_LISTENER：重定向到监听器。 - REDIRECT_TO_URL：重定向到URL。 - FIXED_RESPONSE：返回固定响应体。  **默认取值**：不涉及

        :return: The action of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListL7PoliciesRequest.

        **参数解释**：转发策略的转发动作。 支持多值查询，查询条件格式：*****action=xxx&action=xxx*****。  **约束限制**：不涉及  **取值范围**： - REDIRECT_TO_POOL：转发到后端服务器组。 - REDIRECT_TO_LISTENER：重定向到监听器。 - REDIRECT_TO_URL：重定向到URL。 - FIXED_RESPONSE：返回固定响应体。  **默认取值**：不涉及

        :param action: The action of this ListL7PoliciesRequest.
        :type action: list[str]
        """
        self._action = action

    @property
    def redirect_url(self):
        r"""Gets the redirect_url of this ListL7PoliciesRequest.

        **参数解释**：转发到的url。 支持多值查询，查询条件格式：****redirect_url=xxx&redirect_url=xxx****。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  不支持该字段，请勿使用。

        :return: The redirect_url of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        r"""Sets the redirect_url of this ListL7PoliciesRequest.

        **参数解释**：转发到的url。 支持多值查询，查询条件格式：****redirect_url=xxx&redirect_url=xxx****。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  不支持该字段，请勿使用。

        :param redirect_url: The redirect_url of this ListL7PoliciesRequest.
        :type redirect_url: list[str]
        """
        self._redirect_url = redirect_url

    @property
    def redirect_pool_id(self):
        r"""Gets the redirect_pool_id of this ListL7PoliciesRequest.

        **参数解释**：转发到pool的ID。 支持多值查询，查询条件格式：***redirect_pool_id=xxx&redirect_pool_id=xxx***。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The redirect_pool_id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        r"""Sets the redirect_pool_id of this ListL7PoliciesRequest.

        **参数解释**：转发到pool的ID。 支持多值查询，查询条件格式：***redirect_pool_id=xxx&redirect_pool_id=xxx***。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param redirect_pool_id: The redirect_pool_id of this ListL7PoliciesRequest.
        :type redirect_pool_id: list[str]
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_listener_id(self):
        r"""Gets the redirect_listener_id of this ListL7PoliciesRequest.

        **参数解释**：转发到的listener的ID。 支持多值查询，查询条件格式：**redirect_listener_id=xxx&redirect_listener_id=xxx**。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The redirect_listener_id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        r"""Sets the redirect_listener_id of this ListL7PoliciesRequest.

        **参数解释**：转发到的listener的ID。 支持多值查询，查询条件格式：**redirect_listener_id=xxx&redirect_listener_id=xxx**。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param redirect_listener_id: The redirect_listener_id of this ListL7PoliciesRequest.
        :type redirect_listener_id: list[str]
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this ListL7PoliciesRequest.

        **参数解释**：转发策略的配置状态。 支持多值查询，查询条件格式：*provisioning_status=xxx&provisioning_status=xxx*。  **约束限制**：不涉及  **取值范围**： - ACTIVE: 表示正常。 - ERROR: 表示当前策略与同一监听器下的其他策略存在相同的规则配置。  **默认取值**：不涉及

        :return: The provisioning_status of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this ListL7PoliciesRequest.

        **参数解释**：转发策略的配置状态。 支持多值查询，查询条件格式：*provisioning_status=xxx&provisioning_status=xxx*。  **约束限制**：不涉及  **取值范围**： - ACTIVE: 表示正常。 - ERROR: 表示当前策略与同一监听器下的其他策略存在相同的规则配置。  **默认取值**：不涉及

        :param provisioning_status: The provisioning_status of this ListL7PoliciesRequest.
        :type provisioning_status: list[str]
        """
        self._provisioning_status = provisioning_status

    @property
    def display_all_rules(self):
        r"""Gets the display_all_rules of this ListL7PoliciesRequest.

        **参数解释**：是否显示转发策略下的rule详细信息。  **约束限制**：不涉及  **取值范围**： - true：显示policy下面的rule的详细信息。 - false：只显示policy下面的rule的id信息。  **默认取值**：不涉及

        :return: The display_all_rules of this ListL7PoliciesRequest.
        :rtype: bool
        """
        return self._display_all_rules

    @display_all_rules.setter
    def display_all_rules(self, display_all_rules):
        r"""Sets the display_all_rules of this ListL7PoliciesRequest.

        **参数解释**：是否显示转发策略下的rule详细信息。  **约束限制**：不涉及  **取值范围**： - true：显示policy下面的rule的详细信息。 - false：只显示policy下面的rule的id信息。  **默认取值**：不涉及

        :param display_all_rules: The display_all_rules of this ListL7PoliciesRequest.
        :type display_all_rules: bool
        """
        self._display_all_rules = display_all_rules

    @property
    def priority(self):
        r"""Gets the priority of this ListL7PoliciesRequest.

        **参数解释**：转发策略的优先级。数值越小，优先级越高。 支持多值查询，查询条件格式：*priority=xxx&priority=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hcso_dt)

        :return: The priority of this ListL7PoliciesRequest.
        :rtype: list[int]
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ListL7PoliciesRequest.

        **参数解释**：转发策略的优先级。数值越小，优先级越高。 支持多值查询，查询条件格式：*priority=xxx&priority=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:hcso_dt)

        :param priority: The priority of this ListL7PoliciesRequest.
        :type priority: list[int]
        """
        self._priority = priority

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
        if not isinstance(other, ListL7PoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

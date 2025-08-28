# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class L7Policy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'admin_state_up': 'bool',
        'description': 'str',
        'id': 'str',
        'listener_id': 'str',
        'name': 'str',
        'position': 'int',
        'priority': 'int',
        'project_id': 'str',
        'provisioning_status': 'str',
        'redirect_pool_id': 'str',
        'redirect_listener_id': 'str',
        'redirect_url': 'str',
        'rules': 'list[RuleRef]',
        'redirect_url_config': 'RedirectUrlConfig',
        'redirect_pools_config': 'list[RedirectPoolsConfig]',
        'redirect_pools_sticky_session_config': 'RedirectPoolsStickySessionConfig',
        'redirect_pools_extend_config': 'RedirectPoolsExtendConfig',
        'fixed_response_config': 'FixtedResponseConfig',
        'created_at': 'str',
        'updated_at': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'id': 'id',
        'listener_id': 'listener_id',
        'name': 'name',
        'position': 'position',
        'priority': 'priority',
        'project_id': 'project_id',
        'provisioning_status': 'provisioning_status',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_url': 'redirect_url',
        'rules': 'rules',
        'redirect_url_config': 'redirect_url_config',
        'redirect_pools_config': 'redirect_pools_config',
        'redirect_pools_sticky_session_config': 'redirect_pools_sticky_session_config',
        'redirect_pools_extend_config': 'redirect_pools_extend_config',
        'fixed_response_config': 'fixed_response_config',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, action=None, admin_state_up=None, description=None, id=None, listener_id=None, name=None, position=None, priority=None, project_id=None, provisioning_status=None, redirect_pool_id=None, redirect_listener_id=None, redirect_url=None, rules=None, redirect_url_config=None, redirect_pools_config=None, redirect_pools_sticky_session_config=None, redirect_pools_extend_config=None, fixed_response_config=None, created_at=None, updated_at=None, enterprise_project_id=None):
        r"""L7Policy

        The model defined in huaweicloud sdk

        :param action: **参数解释**：转发策略的转发动作。  **取值范围**： - REDIRECT_TO_POOL：转发到后端服务器组； - REDIRECT_TO_LISTENER：重定向到监听器； - REDIRECT_TO_URL：重定向到URL； - FIXED_RESPONSE：返回固定响应体。  [不支持REDIRECT_TO_URL和FIXED_RESPONSE](tag:hcso_dt)
        :type action: str
        :param admin_state_up: **参数解释**：转发策略的管理状态。  **取值范围**：只支持设置为true。
        :type admin_state_up: bool
        :param description: **参数解释**：转发策略描述信息。  **取值范围**：不涉及
        :type description: str
        :param id: **参数解释**：转发策略ID。  **取值范围**：不涉及
        :type id: str
        :param listener_id: **参数解释**：转发策略所属的监听器ID。  **取值范围**：不涉及
        :type listener_id: str
        :param name: **参数解释**：转发策略名称  **取值范围**：不涉及
        :type name: str
        :param position: **参数解释**：转发策略的优先级，不支持更新。  不支持该字段，请勿使用。
        :type position: int
        :param priority: **参数解释**：转发策略的优先级。数字越小表示优先级越高。  **取值范围**： - 当action为REDIRECT_TO_LISTENER时，支持指定为0-10000。 - 其它action取值，支持指定为1-10000。  [不支持该字段，请勿使用。](tag:hcso_dt)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type priority: int
        :param project_id: **参数解释**：转发策略所在的项目ID。  **取值范围**：不涉及
        :type project_id: str
        :param provisioning_status: **参数解释**：转发策略的配置状态。  **取值范围**： - ACTIVE: 默认值，表示正常。 [- ERROR: 表示当前策略与同一监听器下的其他策略存在相同的规则配置。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)
        :type provisioning_status: str
        :param redirect_pool_id: **参数解释**：转发到pool的ID。  **取值范围**：不涉及
        :type redirect_pool_id: str
        :param redirect_listener_id: **参数解释**：转发到的listener的ID。  **取值范围**：不涉及
        :type redirect_listener_id: str
        :param redirect_url: **参数解释**：转发到的url。  **取值范围**：必须满足格式: protocol://host:port/path?query。  不支持该字段，请勿使用。
        :type redirect_url: str
        :param rules: **参数解释**：转发策略关联的转发规则列表。
        :type rules: list[:class:`huaweicloudsdkelb.v3.RuleRef`]
        :param redirect_url_config: 
        :type redirect_url_config: :class:`huaweicloudsdkelb.v3.RedirectUrlConfig`
        :param redirect_pools_config: **参数解释**：转发策略服务器组的权重配置。当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效，未开启传入该字段会报错。
        :type redirect_pools_config: list[:class:`huaweicloudsdkelb.v3.RedirectPoolsConfig`]
        :param redirect_pools_sticky_session_config: 
        :type redirect_pools_sticky_session_config: :class:`huaweicloudsdkelb.v3.RedirectPoolsStickySessionConfig`
        :param redirect_pools_extend_config: 
        :type redirect_pools_extend_config: :class:`huaweicloudsdkelb.v3.RedirectPoolsExtendConfig`
        :param fixed_response_config: 
        :type fixed_response_config: :class:`huaweicloudsdkelb.v3.FixtedResponseConfig`
        :param created_at: **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type created_at: str
        :param updated_at: **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)
        :type updated_at: str
        :param enterprise_project_id: **参数解释**：企业项目ID。  **取值范围**：不涉及
        :type enterprise_project_id: str
        """
        
        

        self._action = None
        self._admin_state_up = None
        self._description = None
        self._id = None
        self._listener_id = None
        self._name = None
        self._position = None
        self._priority = None
        self._project_id = None
        self._provisioning_status = None
        self._redirect_pool_id = None
        self._redirect_listener_id = None
        self._redirect_url = None
        self._rules = None
        self._redirect_url_config = None
        self._redirect_pools_config = None
        self._redirect_pools_sticky_session_config = None
        self._redirect_pools_extend_config = None
        self._fixed_response_config = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.action = action
        self.admin_state_up = admin_state_up
        self.description = description
        self.id = id
        self.listener_id = listener_id
        self.name = name
        self.position = position
        if priority is not None:
            self.priority = priority
        self.project_id = project_id
        self.provisioning_status = provisioning_status
        self.redirect_pool_id = redirect_pool_id
        self.redirect_listener_id = redirect_listener_id
        self.redirect_url = redirect_url
        self.rules = rules
        self.redirect_url_config = redirect_url_config
        if redirect_pools_config is not None:
            self.redirect_pools_config = redirect_pools_config
        if redirect_pools_sticky_session_config is not None:
            self.redirect_pools_sticky_session_config = redirect_pools_sticky_session_config
        if redirect_pools_extend_config is not None:
            self.redirect_pools_extend_config = redirect_pools_extend_config
        self.fixed_response_config = fixed_response_config
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def action(self):
        r"""Gets the action of this L7Policy.

        **参数解释**：转发策略的转发动作。  **取值范围**： - REDIRECT_TO_POOL：转发到后端服务器组； - REDIRECT_TO_LISTENER：重定向到监听器； - REDIRECT_TO_URL：重定向到URL； - FIXED_RESPONSE：返回固定响应体。  [不支持REDIRECT_TO_URL和FIXED_RESPONSE](tag:hcso_dt)

        :return: The action of this L7Policy.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this L7Policy.

        **参数解释**：转发策略的转发动作。  **取值范围**： - REDIRECT_TO_POOL：转发到后端服务器组； - REDIRECT_TO_LISTENER：重定向到监听器； - REDIRECT_TO_URL：重定向到URL； - FIXED_RESPONSE：返回固定响应体。  [不支持REDIRECT_TO_URL和FIXED_RESPONSE](tag:hcso_dt)

        :param action: The action of this L7Policy.
        :type action: str
        """
        self._action = action

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this L7Policy.

        **参数解释**：转发策略的管理状态。  **取值范围**：只支持设置为true。

        :return: The admin_state_up of this L7Policy.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this L7Policy.

        **参数解释**：转发策略的管理状态。  **取值范围**：只支持设置为true。

        :param admin_state_up: The admin_state_up of this L7Policy.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        r"""Gets the description of this L7Policy.

        **参数解释**：转发策略描述信息。  **取值范围**：不涉及

        :return: The description of this L7Policy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this L7Policy.

        **参数解释**：转发策略描述信息。  **取值范围**：不涉及

        :param description: The description of this L7Policy.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this L7Policy.

        **参数解释**：转发策略ID。  **取值范围**：不涉及

        :return: The id of this L7Policy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this L7Policy.

        **参数解释**：转发策略ID。  **取值范围**：不涉及

        :param id: The id of this L7Policy.
        :type id: str
        """
        self._id = id

    @property
    def listener_id(self):
        r"""Gets the listener_id of this L7Policy.

        **参数解释**：转发策略所属的监听器ID。  **取值范围**：不涉及

        :return: The listener_id of this L7Policy.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this L7Policy.

        **参数解释**：转发策略所属的监听器ID。  **取值范围**：不涉及

        :param listener_id: The listener_id of this L7Policy.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def name(self):
        r"""Gets the name of this L7Policy.

        **参数解释**：转发策略名称  **取值范围**：不涉及

        :return: The name of this L7Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this L7Policy.

        **参数解释**：转发策略名称  **取值范围**：不涉及

        :param name: The name of this L7Policy.
        :type name: str
        """
        self._name = name

    @property
    def position(self):
        r"""Gets the position of this L7Policy.

        **参数解释**：转发策略的优先级，不支持更新。  不支持该字段，请勿使用。

        :return: The position of this L7Policy.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this L7Policy.

        **参数解释**：转发策略的优先级，不支持更新。  不支持该字段，请勿使用。

        :param position: The position of this L7Policy.
        :type position: int
        """
        self._position = position

    @property
    def priority(self):
        r"""Gets the priority of this L7Policy.

        **参数解释**：转发策略的优先级。数字越小表示优先级越高。  **取值范围**： - 当action为REDIRECT_TO_LISTENER时，支持指定为0-10000。 - 其它action取值，支持指定为1-10000。  [不支持该字段，请勿使用。](tag:hcso_dt)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The priority of this L7Policy.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this L7Policy.

        **参数解释**：转发策略的优先级。数字越小表示优先级越高。  **取值范围**： - 当action为REDIRECT_TO_LISTENER时，支持指定为0-10000。 - 其它action取值，支持指定为1-10000。  [不支持该字段，请勿使用。](tag:hcso_dt)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param priority: The priority of this L7Policy.
        :type priority: int
        """
        self._priority = priority

    @property
    def project_id(self):
        r"""Gets the project_id of this L7Policy.

        **参数解释**：转发策略所在的项目ID。  **取值范围**：不涉及

        :return: The project_id of this L7Policy.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this L7Policy.

        **参数解释**：转发策略所在的项目ID。  **取值范围**：不涉及

        :param project_id: The project_id of this L7Policy.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this L7Policy.

        **参数解释**：转发策略的配置状态。  **取值范围**： - ACTIVE: 默认值，表示正常。 [- ERROR: 表示当前策略与同一监听器下的其他策略存在相同的规则配置。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)

        :return: The provisioning_status of this L7Policy.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this L7Policy.

        **参数解释**：转发策略的配置状态。  **取值范围**： - ACTIVE: 默认值，表示正常。 [- ERROR: 表示当前策略与同一监听器下的其他策略存在相同的规则配置。](tag:hws,hws_hk,ocb,ctc,hcs,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs)

        :param provisioning_status: The provisioning_status of this L7Policy.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def redirect_pool_id(self):
        r"""Gets the redirect_pool_id of this L7Policy.

        **参数解释**：转发到pool的ID。  **取值范围**：不涉及

        :return: The redirect_pool_id of this L7Policy.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        r"""Sets the redirect_pool_id of this L7Policy.

        **参数解释**：转发到pool的ID。  **取值范围**：不涉及

        :param redirect_pool_id: The redirect_pool_id of this L7Policy.
        :type redirect_pool_id: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_listener_id(self):
        r"""Gets the redirect_listener_id of this L7Policy.

        **参数解释**：转发到的listener的ID。  **取值范围**：不涉及

        :return: The redirect_listener_id of this L7Policy.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        r"""Sets the redirect_listener_id of this L7Policy.

        **参数解释**：转发到的listener的ID。  **取值范围**：不涉及

        :param redirect_listener_id: The redirect_listener_id of this L7Policy.
        :type redirect_listener_id: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_url(self):
        r"""Gets the redirect_url of this L7Policy.

        **参数解释**：转发到的url。  **取值范围**：必须满足格式: protocol://host:port/path?query。  不支持该字段，请勿使用。

        :return: The redirect_url of this L7Policy.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        r"""Sets the redirect_url of this L7Policy.

        **参数解释**：转发到的url。  **取值范围**：必须满足格式: protocol://host:port/path?query。  不支持该字段，请勿使用。

        :param redirect_url: The redirect_url of this L7Policy.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def rules(self):
        r"""Gets the rules of this L7Policy.

        **参数解释**：转发策略关联的转发规则列表。

        :return: The rules of this L7Policy.
        :rtype: list[:class:`huaweicloudsdkelb.v3.RuleRef`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this L7Policy.

        **参数解释**：转发策略关联的转发规则列表。

        :param rules: The rules of this L7Policy.
        :type rules: list[:class:`huaweicloudsdkelb.v3.RuleRef`]
        """
        self._rules = rules

    @property
    def redirect_url_config(self):
        r"""Gets the redirect_url_config of this L7Policy.

        :return: The redirect_url_config of this L7Policy.
        :rtype: :class:`huaweicloudsdkelb.v3.RedirectUrlConfig`
        """
        return self._redirect_url_config

    @redirect_url_config.setter
    def redirect_url_config(self, redirect_url_config):
        r"""Sets the redirect_url_config of this L7Policy.

        :param redirect_url_config: The redirect_url_config of this L7Policy.
        :type redirect_url_config: :class:`huaweicloudsdkelb.v3.RedirectUrlConfig`
        """
        self._redirect_url_config = redirect_url_config

    @property
    def redirect_pools_config(self):
        r"""Gets the redirect_pools_config of this L7Policy.

        **参数解释**：转发策略服务器组的权重配置。当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效，未开启传入该字段会报错。

        :return: The redirect_pools_config of this L7Policy.
        :rtype: list[:class:`huaweicloudsdkelb.v3.RedirectPoolsConfig`]
        """
        return self._redirect_pools_config

    @redirect_pools_config.setter
    def redirect_pools_config(self, redirect_pools_config):
        r"""Sets the redirect_pools_config of this L7Policy.

        **参数解释**：转发策略服务器组的权重配置。当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效，未开启传入该字段会报错。

        :param redirect_pools_config: The redirect_pools_config of this L7Policy.
        :type redirect_pools_config: list[:class:`huaweicloudsdkelb.v3.RedirectPoolsConfig`]
        """
        self._redirect_pools_config = redirect_pools_config

    @property
    def redirect_pools_sticky_session_config(self):
        r"""Gets the redirect_pools_sticky_session_config of this L7Policy.

        :return: The redirect_pools_sticky_session_config of this L7Policy.
        :rtype: :class:`huaweicloudsdkelb.v3.RedirectPoolsStickySessionConfig`
        """
        return self._redirect_pools_sticky_session_config

    @redirect_pools_sticky_session_config.setter
    def redirect_pools_sticky_session_config(self, redirect_pools_sticky_session_config):
        r"""Sets the redirect_pools_sticky_session_config of this L7Policy.

        :param redirect_pools_sticky_session_config: The redirect_pools_sticky_session_config of this L7Policy.
        :type redirect_pools_sticky_session_config: :class:`huaweicloudsdkelb.v3.RedirectPoolsStickySessionConfig`
        """
        self._redirect_pools_sticky_session_config = redirect_pools_sticky_session_config

    @property
    def redirect_pools_extend_config(self):
        r"""Gets the redirect_pools_extend_config of this L7Policy.

        :return: The redirect_pools_extend_config of this L7Policy.
        :rtype: :class:`huaweicloudsdkelb.v3.RedirectPoolsExtendConfig`
        """
        return self._redirect_pools_extend_config

    @redirect_pools_extend_config.setter
    def redirect_pools_extend_config(self, redirect_pools_extend_config):
        r"""Sets the redirect_pools_extend_config of this L7Policy.

        :param redirect_pools_extend_config: The redirect_pools_extend_config of this L7Policy.
        :type redirect_pools_extend_config: :class:`huaweicloudsdkelb.v3.RedirectPoolsExtendConfig`
        """
        self._redirect_pools_extend_config = redirect_pools_extend_config

    @property
    def fixed_response_config(self):
        r"""Gets the fixed_response_config of this L7Policy.

        :return: The fixed_response_config of this L7Policy.
        :rtype: :class:`huaweicloudsdkelb.v3.FixtedResponseConfig`
        """
        return self._fixed_response_config

    @fixed_response_config.setter
    def fixed_response_config(self, fixed_response_config):
        r"""Sets the fixed_response_config of this L7Policy.

        :param fixed_response_config: The fixed_response_config of this L7Policy.
        :type fixed_response_config: :class:`huaweicloudsdkelb.v3.FixtedResponseConfig`
        """
        self._fixed_response_config = fixed_response_config

    @property
    def created_at(self):
        r"""Gets the created_at of this L7Policy.

        **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The created_at of this L7Policy.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this L7Policy.

        **参数解释**：创建时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param created_at: The created_at of this L7Policy.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this L7Policy.

        **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :return: The updated_at of this L7Policy.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this L7Policy.

        **参数解释**：更新时间。  **取值范围**：格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,hk_vdf,srg,fcs,dt,hk_tm)

        :param updated_at: The updated_at of this L7Policy.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this L7Policy.

        **参数解释**：企业项目ID。  **取值范围**：不涉及

        :return: The enterprise_project_id of this L7Policy.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this L7Policy.

        **参数解释**：企业项目ID。  **取值范围**：不涉及

        :param enterprise_project_id: The enterprise_project_id of this L7Policy.
        :type enterprise_project_id: str
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
        if not isinstance(other, L7Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

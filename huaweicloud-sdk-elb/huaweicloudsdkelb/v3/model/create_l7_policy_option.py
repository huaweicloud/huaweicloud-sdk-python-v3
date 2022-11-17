# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateL7PolicyOption:

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
        'listener_id': 'str',
        'name': 'str',
        'position': 'int',
        'priority': 'int',
        'project_id': 'str',
        'redirect_listener_id': 'str',
        'redirect_pool_id': 'str',
        'redirect_pools_config': 'list[CreateRedirectPoolsConfig]',
        'redirect_url': 'str',
        'redirect_url_config': 'CreateRedirectUrlConfig',
        'fixed_response_config': 'CreateFixtedResponseConfig',
        'rules': 'list[CreateL7PolicyRuleOption]'
    }

    attribute_map = {
        'action': 'action',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'listener_id': 'listener_id',
        'name': 'name',
        'position': 'position',
        'priority': 'priority',
        'project_id': 'project_id',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_pools_config': 'redirect_pools_config',
        'redirect_url': 'redirect_url',
        'redirect_url_config': 'redirect_url_config',
        'fixed_response_config': 'fixed_response_config',
        'rules': 'rules'
    }

    def __init__(self, action=None, admin_state_up=None, description=None, listener_id=None, name=None, position=None, priority=None, project_id=None, redirect_listener_id=None, redirect_pool_id=None, redirect_pools_config=None, redirect_url=None, redirect_url_config=None, fixed_response_config=None, rules=None):
        """CreateL7PolicyOption

        The model defined in huaweicloud sdk

        :param action: 转发策略的转发动作。  取值： - REDIRECT_TO_POOL：转发到后端云服务器组。 - REDIRECT_TO_LISTENER：重定向到监听器。 - REDIRECT_TO_URL：重定向到URL。 - FIXED_RESPONSE：返回固定响应体。  使用说明： - REDIRECT_TO_LISTENER的优先级最高，配置了以后，该监听器下的其他policy会失效。 - 当action为REDIRECT_TO_POOL时， 只支持创建在PROTOCOL为HTTP、HTTPS、TERMINATED_HTTPS的listener上。 - 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。  [不支持REDIRECT_TO_URL和FIXED_RESPONSE](tag:hcso_dt)
        :type action: str
        :param admin_state_up: 转发策略的管理状态，默认为true。  不支持该字段，请勿使用。
        :type admin_state_up: bool
        :param description: 转发策略描述信息。
        :type description: str
        :param listener_id: 转发策略对应的监听器ID。 当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或HTTPS的listener上。  当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。
        :type listener_id: str
        :param name: 转发策略名称。
        :type name: str
        :param position: 转发策略的优先级，不支持更新。  不支持该字段，请勿使用。
        :type position: int
        :param priority: 转发策略的优先级。数字越小表示优先级越高，同一监听器下不允许重复。  当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效，未开启传入该字段会报错。  当action为REDIRECT_TO_LISTENER时，仅支持指定为0，优先级最高。  当关联的listener没有开启enhance_l7policy_enable，按原有policy的排序逻辑，自动排序。 各域名之间优先级独立，相同域名下，按path的compare_type排序， 精确&gt;前缀&gt;正则，匹配类型相同时，path的长度越长优先级越高。 若policy下只有域名rule，没有路径rule，默认path为前缀匹配/。  当关联的listener开启了enhance_l7policy_enable，且不传该字段， 则新创建的转发策略的优先级的值为：同一监听器下已有转发策略的优先级的最大值+1。 因此，若当前已有转发策略的优先级的最大值是10000，新创建会因超出取值范围10000而失败。 此时可通过传入指定priority，或调整原有policy的优先级来避免错误。 若监听器下没有转发策略，则新建的转发策略的优先级为1。  [共享型负载均衡器下的转发策略不支持该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)  [不支持该字段，请勿使用。](tag:hcso_dt)
        :type priority: int
        :param project_id: 转发策略所在的项目ID。
        :type project_id: str
        :param redirect_listener_id: 转发到的listener的ID，当action为REDIRECT_TO_LISTENER时必选。  使用说明： - 只支持protocol为HTTPS/TERMINATED_HTTPS的listener。 - 不能指定为其他loadbalancer下的listener。 - 当action为REDIRECT_TO_POOL时，创建或更新时不能传入该参数。 [- 共享型负载均衡器下的转发策略不支持该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)
        :type redirect_listener_id: str
        :param redirect_pool_id: 转发到pool的ID。当action为REDIRECT_TO_POOL时生效。  使用说明： - 当action为REDIRECT_TO_POOL时，redirect_pool_id和redirect_pools_config 必须指定一个，两个都指定时按redirect_pools_config生效。 - 当action为REDIRECT_TO_LISTENER时，不可指定。
        :type redirect_pool_id: str
        :param redirect_pools_config: 转发到的后端主机组的配置。当action为REDIRECT_TO_POOL时生效。  使用说明： - 当action为REDIRECT_TO_POOL时redirect_pool_id和redirect_pools_config 必须指定一个，两个都指定时按redirect_pools_config生效。 - 当action为REDIRECT_TO_LISTENER时，不可指定。
        :type redirect_pools_config: list[:class:`huaweicloudsdkelb.v3.CreateRedirectPoolsConfig`]
        :param redirect_url: 转发到的url。必须满足格式: protocol://host:port/path?query。  [不支持该字段，请勿使用。](tag:hcso_dt)
        :type redirect_url: str
        :param redirect_url_config: 
        :type redirect_url_config: :class:`huaweicloudsdkelb.v3.CreateRedirectUrlConfig`
        :param fixed_response_config: 
        :type fixed_response_config: :class:`huaweicloudsdkelb.v3.CreateFixtedResponseConfig`
        :param rules: 转发策略关联的转发规则对象。详细参考表 l7rule字段说明。rules列表中最多含有10个rule规则 （若rule中包含conditions字段，一条condition算一个规则）， 且列表中type为HOST_NAME，PATH，METHOD，SOURCE_IP的rule不能重复，至多指定一条。  使用说明： - 仅支持全量替换。 - 如果l7policy 是重定向到listener的话，不允许创建l7rule。
        :type rules: list[:class:`huaweicloudsdkelb.v3.CreateL7PolicyRuleOption`]
        """
        
        

        self._action = None
        self._admin_state_up = None
        self._description = None
        self._listener_id = None
        self._name = None
        self._position = None
        self._priority = None
        self._project_id = None
        self._redirect_listener_id = None
        self._redirect_pool_id = None
        self._redirect_pools_config = None
        self._redirect_url = None
        self._redirect_url_config = None
        self._fixed_response_config = None
        self._rules = None
        self.discriminator = None

        self.action = action
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        self.listener_id = listener_id
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if priority is not None:
            self.priority = priority
        if project_id is not None:
            self.project_id = project_id
        if redirect_listener_id is not None:
            self.redirect_listener_id = redirect_listener_id
        if redirect_pool_id is not None:
            self.redirect_pool_id = redirect_pool_id
        if redirect_pools_config is not None:
            self.redirect_pools_config = redirect_pools_config
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if redirect_url_config is not None:
            self.redirect_url_config = redirect_url_config
        if fixed_response_config is not None:
            self.fixed_response_config = fixed_response_config
        if rules is not None:
            self.rules = rules

    @property
    def action(self):
        """Gets the action of this CreateL7PolicyOption.

        转发策略的转发动作。  取值： - REDIRECT_TO_POOL：转发到后端云服务器组。 - REDIRECT_TO_LISTENER：重定向到监听器。 - REDIRECT_TO_URL：重定向到URL。 - FIXED_RESPONSE：返回固定响应体。  使用说明： - REDIRECT_TO_LISTENER的优先级最高，配置了以后，该监听器下的其他policy会失效。 - 当action为REDIRECT_TO_POOL时， 只支持创建在PROTOCOL为HTTP、HTTPS、TERMINATED_HTTPS的listener上。 - 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。  [不支持REDIRECT_TO_URL和FIXED_RESPONSE](tag:hcso_dt)

        :return: The action of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateL7PolicyOption.

        转发策略的转发动作。  取值： - REDIRECT_TO_POOL：转发到后端云服务器组。 - REDIRECT_TO_LISTENER：重定向到监听器。 - REDIRECT_TO_URL：重定向到URL。 - FIXED_RESPONSE：返回固定响应体。  使用说明： - REDIRECT_TO_LISTENER的优先级最高，配置了以后，该监听器下的其他policy会失效。 - 当action为REDIRECT_TO_POOL时， 只支持创建在PROTOCOL为HTTP、HTTPS、TERMINATED_HTTPS的listener上。 - 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。  [不支持REDIRECT_TO_URL和FIXED_RESPONSE](tag:hcso_dt)

        :param action: The action of this CreateL7PolicyOption.
        :type action: str
        """
        self._action = action

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateL7PolicyOption.

        转发策略的管理状态，默认为true。  不支持该字段，请勿使用。

        :return: The admin_state_up of this CreateL7PolicyOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateL7PolicyOption.

        转发策略的管理状态，默认为true。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this CreateL7PolicyOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this CreateL7PolicyOption.

        转发策略描述信息。

        :return: The description of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateL7PolicyOption.

        转发策略描述信息。

        :param description: The description of this CreateL7PolicyOption.
        :type description: str
        """
        self._description = description

    @property
    def listener_id(self):
        """Gets the listener_id of this CreateL7PolicyOption.

        转发策略对应的监听器ID。 当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或HTTPS的listener上。  当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。

        :return: The listener_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CreateL7PolicyOption.

        转发策略对应的监听器ID。 当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或HTTPS的listener上。  当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。

        :param listener_id: The listener_id of this CreateL7PolicyOption.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def name(self):
        """Gets the name of this CreateL7PolicyOption.

        转发策略名称。

        :return: The name of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateL7PolicyOption.

        转发策略名称。

        :param name: The name of this CreateL7PolicyOption.
        :type name: str
        """
        self._name = name

    @property
    def position(self):
        """Gets the position of this CreateL7PolicyOption.

        转发策略的优先级，不支持更新。  不支持该字段，请勿使用。

        :return: The position of this CreateL7PolicyOption.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CreateL7PolicyOption.

        转发策略的优先级，不支持更新。  不支持该字段，请勿使用。

        :param position: The position of this CreateL7PolicyOption.
        :type position: int
        """
        self._position = position

    @property
    def priority(self):
        """Gets the priority of this CreateL7PolicyOption.

        转发策略的优先级。数字越小表示优先级越高，同一监听器下不允许重复。  当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效，未开启传入该字段会报错。  当action为REDIRECT_TO_LISTENER时，仅支持指定为0，优先级最高。  当关联的listener没有开启enhance_l7policy_enable，按原有policy的排序逻辑，自动排序。 各域名之间优先级独立，相同域名下，按path的compare_type排序， 精确>前缀>正则，匹配类型相同时，path的长度越长优先级越高。 若policy下只有域名rule，没有路径rule，默认path为前缀匹配/。  当关联的listener开启了enhance_l7policy_enable，且不传该字段， 则新创建的转发策略的优先级的值为：同一监听器下已有转发策略的优先级的最大值+1。 因此，若当前已有转发策略的优先级的最大值是10000，新创建会因超出取值范围10000而失败。 此时可通过传入指定priority，或调整原有policy的优先级来避免错误。 若监听器下没有转发策略，则新建的转发策略的优先级为1。  [共享型负载均衡器下的转发策略不支持该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)  [不支持该字段，请勿使用。](tag:hcso_dt)

        :return: The priority of this CreateL7PolicyOption.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateL7PolicyOption.

        转发策略的优先级。数字越小表示优先级越高，同一监听器下不允许重复。  当监听器的高级转发策略功能（enhance_l7policy_enable）开启后才会生效，未开启传入该字段会报错。  当action为REDIRECT_TO_LISTENER时，仅支持指定为0，优先级最高。  当关联的listener没有开启enhance_l7policy_enable，按原有policy的排序逻辑，自动排序。 各域名之间优先级独立，相同域名下，按path的compare_type排序， 精确>前缀>正则，匹配类型相同时，path的长度越长优先级越高。 若policy下只有域名rule，没有路径rule，默认path为前缀匹配/。  当关联的listener开启了enhance_l7policy_enable，且不传该字段， 则新创建的转发策略的优先级的值为：同一监听器下已有转发策略的优先级的最大值+1。 因此，若当前已有转发策略的优先级的最大值是10000，新创建会因超出取值范围10000而失败。 此时可通过传入指定priority，或调整原有policy的优先级来避免错误。 若监听器下没有转发策略，则新建的转发策略的优先级为1。  [共享型负载均衡器下的转发策略不支持该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)  [不支持该字段，请勿使用。](tag:hcso_dt)

        :param priority: The priority of this CreateL7PolicyOption.
        :type priority: int
        """
        self._priority = priority

    @property
    def project_id(self):
        """Gets the project_id of this CreateL7PolicyOption.

        转发策略所在的项目ID。

        :return: The project_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateL7PolicyOption.

        转发策略所在的项目ID。

        :param project_id: The project_id of this CreateL7PolicyOption.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this CreateL7PolicyOption.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时必选。  使用说明： - 只支持protocol为HTTPS/TERMINATED_HTTPS的listener。 - 不能指定为其他loadbalancer下的listener。 - 当action为REDIRECT_TO_POOL时，创建或更新时不能传入该参数。 [- 共享型负载均衡器下的转发策略不支持该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :return: The redirect_listener_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this CreateL7PolicyOption.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时必选。  使用说明： - 只支持protocol为HTTPS/TERMINATED_HTTPS的listener。 - 不能指定为其他loadbalancer下的listener。 - 当action为REDIRECT_TO_POOL时，创建或更新时不能传入该参数。 [- 共享型负载均衡器下的转发策略不支持该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :param redirect_listener_id: The redirect_listener_id of this CreateL7PolicyOption.
        :type redirect_listener_id: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this CreateL7PolicyOption.

        转发到pool的ID。当action为REDIRECT_TO_POOL时生效。  使用说明： - 当action为REDIRECT_TO_POOL时，redirect_pool_id和redirect_pools_config 必须指定一个，两个都指定时按redirect_pools_config生效。 - 当action为REDIRECT_TO_LISTENER时，不可指定。

        :return: The redirect_pool_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this CreateL7PolicyOption.

        转发到pool的ID。当action为REDIRECT_TO_POOL时生效。  使用说明： - 当action为REDIRECT_TO_POOL时，redirect_pool_id和redirect_pools_config 必须指定一个，两个都指定时按redirect_pools_config生效。 - 当action为REDIRECT_TO_LISTENER时，不可指定。

        :param redirect_pool_id: The redirect_pool_id of this CreateL7PolicyOption.
        :type redirect_pool_id: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_pools_config(self):
        """Gets the redirect_pools_config of this CreateL7PolicyOption.

        转发到的后端主机组的配置。当action为REDIRECT_TO_POOL时生效。  使用说明： - 当action为REDIRECT_TO_POOL时redirect_pool_id和redirect_pools_config 必须指定一个，两个都指定时按redirect_pools_config生效。 - 当action为REDIRECT_TO_LISTENER时，不可指定。

        :return: The redirect_pools_config of this CreateL7PolicyOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.CreateRedirectPoolsConfig`]
        """
        return self._redirect_pools_config

    @redirect_pools_config.setter
    def redirect_pools_config(self, redirect_pools_config):
        """Sets the redirect_pools_config of this CreateL7PolicyOption.

        转发到的后端主机组的配置。当action为REDIRECT_TO_POOL时生效。  使用说明： - 当action为REDIRECT_TO_POOL时redirect_pool_id和redirect_pools_config 必须指定一个，两个都指定时按redirect_pools_config生效。 - 当action为REDIRECT_TO_LISTENER时，不可指定。

        :param redirect_pools_config: The redirect_pools_config of this CreateL7PolicyOption.
        :type redirect_pools_config: list[:class:`huaweicloudsdkelb.v3.CreateRedirectPoolsConfig`]
        """
        self._redirect_pools_config = redirect_pools_config

    @property
    def redirect_url(self):
        """Gets the redirect_url of this CreateL7PolicyOption.

        转发到的url。必须满足格式: protocol://host:port/path?query。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :return: The redirect_url of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this CreateL7PolicyOption.

        转发到的url。必须满足格式: protocol://host:port/path?query。  [不支持该字段，请勿使用。](tag:hcso_dt)

        :param redirect_url: The redirect_url of this CreateL7PolicyOption.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def redirect_url_config(self):
        """Gets the redirect_url_config of this CreateL7PolicyOption.

        :return: The redirect_url_config of this CreateL7PolicyOption.
        :rtype: :class:`huaweicloudsdkelb.v3.CreateRedirectUrlConfig`
        """
        return self._redirect_url_config

    @redirect_url_config.setter
    def redirect_url_config(self, redirect_url_config):
        """Sets the redirect_url_config of this CreateL7PolicyOption.

        :param redirect_url_config: The redirect_url_config of this CreateL7PolicyOption.
        :type redirect_url_config: :class:`huaweicloudsdkelb.v3.CreateRedirectUrlConfig`
        """
        self._redirect_url_config = redirect_url_config

    @property
    def fixed_response_config(self):
        """Gets the fixed_response_config of this CreateL7PolicyOption.

        :return: The fixed_response_config of this CreateL7PolicyOption.
        :rtype: :class:`huaweicloudsdkelb.v3.CreateFixtedResponseConfig`
        """
        return self._fixed_response_config

    @fixed_response_config.setter
    def fixed_response_config(self, fixed_response_config):
        """Sets the fixed_response_config of this CreateL7PolicyOption.

        :param fixed_response_config: The fixed_response_config of this CreateL7PolicyOption.
        :type fixed_response_config: :class:`huaweicloudsdkelb.v3.CreateFixtedResponseConfig`
        """
        self._fixed_response_config = fixed_response_config

    @property
    def rules(self):
        """Gets the rules of this CreateL7PolicyOption.

        转发策略关联的转发规则对象。详细参考表 l7rule字段说明。rules列表中最多含有10个rule规则 （若rule中包含conditions字段，一条condition算一个规则）， 且列表中type为HOST_NAME，PATH，METHOD，SOURCE_IP的rule不能重复，至多指定一条。  使用说明： - 仅支持全量替换。 - 如果l7policy 是重定向到listener的话，不允许创建l7rule。

        :return: The rules of this CreateL7PolicyOption.
        :rtype: list[:class:`huaweicloudsdkelb.v3.CreateL7PolicyRuleOption`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this CreateL7PolicyOption.

        转发策略关联的转发规则对象。详细参考表 l7rule字段说明。rules列表中最多含有10个rule规则 （若rule中包含conditions字段，一条condition算一个规则）， 且列表中type为HOST_NAME，PATH，METHOD，SOURCE_IP的rule不能重复，至多指定一条。  使用说明： - 仅支持全量替换。 - 如果l7policy 是重定向到listener的话，不允许创建l7rule。

        :param rules: The rules of this CreateL7PolicyOption.
        :type rules: list[:class:`huaweicloudsdkelb.v3.CreateL7PolicyRuleOption`]
        """
        self._rules = rules

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
        if not isinstance(other, CreateL7PolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateL7policyReq:

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
        'action': 'str',
        'tenant_id': 'str',
        'admin_state_up': 'bool',
        'description': 'str',
        'listener_id': 'str',
        'redirect_pool_id': 'str',
        'redirect_listener_id': 'str',
        'redirect_url': 'str',
        'position': 'int',
        'rules': 'list[CreateL7ruleReqInPolicy]'
    }

    attribute_map = {
        'name': 'name',
        'action': 'action',
        'tenant_id': 'tenant_id',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'listener_id': 'listener_id',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_url': 'redirect_url',
        'position': 'position',
        'rules': 'rules'
    }

    def __init__(self, name=None, action=None, tenant_id=None, admin_state_up=None, description=None, listener_id=None, redirect_pool_id=None, redirect_listener_id=None, redirect_url=None, position=None, rules=None):
        r"""CreateL7policyReq

        The model defined in huaweicloud sdk

        :param name: 转发策略名称
        :type name: str
        :param action: 转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器
        :type action: str
        :param tenant_id: 转发策略所在的项目ID。
        :type tenant_id: str
        :param admin_state_up: 转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。
        :type admin_state_up: bool
        :param description: 转发策略额描述信息
        :type description: str
        :param listener_id: 转发策略对应的监听器ID。当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或TERMINATED_HTTPS的listener上。 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。
        :type listener_id: str
        :param redirect_pool_id: 转发到pool的ID。转发到pool的ID。当action为REDIRECT_TO_POOL时生效。当action为REDIRECT_TO_POOL时必选
        :type redirect_pool_id: str
        :param redirect_listener_id: 转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。当action为REDIRECT_TO_LISTENER时必选
        :type redirect_listener_id: str
        :param redirect_url: 转发到的url。该字段未启用。
        :type redirect_url: str
        :param position: 转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。
        :type position: int
        :param rules: 指定L7rule的参数，可以在创建L7policy的同时创建L7rule
        :type rules: list[:class:`huaweicloudsdkelb.v2.CreateL7ruleReqInPolicy`]
        """
        
        

        self._name = None
        self._action = None
        self._tenant_id = None
        self._admin_state_up = None
        self._description = None
        self._listener_id = None
        self._redirect_pool_id = None
        self._redirect_listener_id = None
        self._redirect_url = None
        self._position = None
        self._rules = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.action = action
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        self.listener_id = listener_id
        if redirect_pool_id is not None:
            self.redirect_pool_id = redirect_pool_id
        if redirect_listener_id is not None:
            self.redirect_listener_id = redirect_listener_id
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if position is not None:
            self.position = position
        if rules is not None:
            self.rules = rules

    @property
    def name(self):
        r"""Gets the name of this CreateL7policyReq.

        转发策略名称

        :return: The name of this CreateL7policyReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateL7policyReq.

        转发策略名称

        :param name: The name of this CreateL7policyReq.
        :type name: str
        """
        self._name = name

    @property
    def action(self):
        r"""Gets the action of this CreateL7policyReq.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :return: The action of this CreateL7policyReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateL7policyReq.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :param action: The action of this CreateL7policyReq.
        :type action: str
        """
        self._action = action

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreateL7policyReq.

        转发策略所在的项目ID。

        :return: The tenant_id of this CreateL7policyReq.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreateL7policyReq.

        转发策略所在的项目ID。

        :param tenant_id: The tenant_id of this CreateL7policyReq.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this CreateL7policyReq.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this CreateL7policyReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this CreateL7policyReq.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this CreateL7policyReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        r"""Gets the description of this CreateL7policyReq.

        转发策略额描述信息

        :return: The description of this CreateL7policyReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateL7policyReq.

        转发策略额描述信息

        :param description: The description of this CreateL7policyReq.
        :type description: str
        """
        self._description = description

    @property
    def listener_id(self):
        r"""Gets the listener_id of this CreateL7policyReq.

        转发策略对应的监听器ID。当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或TERMINATED_HTTPS的listener上。 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。

        :return: The listener_id of this CreateL7policyReq.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this CreateL7policyReq.

        转发策略对应的监听器ID。当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或TERMINATED_HTTPS的listener上。 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。

        :param listener_id: The listener_id of this CreateL7policyReq.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def redirect_pool_id(self):
        r"""Gets the redirect_pool_id of this CreateL7policyReq.

        转发到pool的ID。转发到pool的ID。当action为REDIRECT_TO_POOL时生效。当action为REDIRECT_TO_POOL时必选

        :return: The redirect_pool_id of this CreateL7policyReq.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        r"""Sets the redirect_pool_id of this CreateL7policyReq.

        转发到pool的ID。转发到pool的ID。当action为REDIRECT_TO_POOL时生效。当action为REDIRECT_TO_POOL时必选

        :param redirect_pool_id: The redirect_pool_id of this CreateL7policyReq.
        :type redirect_pool_id: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_listener_id(self):
        r"""Gets the redirect_listener_id of this CreateL7policyReq.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。当action为REDIRECT_TO_LISTENER时必选

        :return: The redirect_listener_id of this CreateL7policyReq.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        r"""Sets the redirect_listener_id of this CreateL7policyReq.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。当action为REDIRECT_TO_LISTENER时必选

        :param redirect_listener_id: The redirect_listener_id of this CreateL7policyReq.
        :type redirect_listener_id: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_url(self):
        r"""Gets the redirect_url of this CreateL7policyReq.

        转发到的url。该字段未启用。

        :return: The redirect_url of this CreateL7policyReq.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        r"""Sets the redirect_url of this CreateL7policyReq.

        转发到的url。该字段未启用。

        :param redirect_url: The redirect_url of this CreateL7policyReq.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def position(self):
        r"""Gets the position of this CreateL7policyReq.

        转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。

        :return: The position of this CreateL7policyReq.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this CreateL7policyReq.

        转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。

        :param position: The position of this CreateL7policyReq.
        :type position: int
        """
        self._position = position

    @property
    def rules(self):
        r"""Gets the rules of this CreateL7policyReq.

        指定L7rule的参数，可以在创建L7policy的同时创建L7rule

        :return: The rules of this CreateL7policyReq.
        :rtype: list[:class:`huaweicloudsdkelb.v2.CreateL7ruleReqInPolicy`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this CreateL7policyReq.

        指定L7rule的参数，可以在创建L7policy的同时创建L7rule

        :param rules: The rules of this CreateL7policyReq.
        :type rules: list[:class:`huaweicloudsdkelb.v2.CreateL7ruleReqInPolicy`]
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
        if not isinstance(other, CreateL7policyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

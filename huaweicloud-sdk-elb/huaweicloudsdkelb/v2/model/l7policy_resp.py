# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class L7policyResp:

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
        'rules': 'list[ResourceList]',
        'action': 'str',
        'provisioning_status': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'admin_state_up': 'bool',
        'description': 'str',
        'listener_id': 'str',
        'redirect_pool_id': 'str',
        'redirect_listener_id': 'str',
        'redirect_url': 'str',
        'position': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'rules': 'rules',
        'action': 'action',
        'provisioning_status': 'provisioning_status',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'listener_id': 'listener_id',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_url': 'redirect_url',
        'position': 'position'
    }

    def __init__(self, id=None, name=None, rules=None, action=None, provisioning_status=None, tenant_id=None, project_id=None, admin_state_up=None, description=None, listener_id=None, redirect_pool_id=None, redirect_listener_id=None, redirect_url=None, position=None):
        """L7policyResp

        The model defined in huaweicloud sdk

        :param id: 转发策略ID
        :type id: str
        :param name: 转发策略名称
        :type name: str
        :param rules: 转发策略关联的转发规则列表
        :type rules: list[:class:`huaweicloudsdkelb.v2.ResourceList`]
        :param action: 转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器
        :type action: str
        :param provisioning_status: 健康检查的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。
        :type provisioning_status: str
        :param tenant_id: 转发策略所在的项目ID。
        :type tenant_id: str
        :param project_id: 转发策略所在的项目ID。
        :type project_id: str
        :param admin_state_up: 转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。
        :type admin_state_up: bool
        :param description: 转发策略额描述信息
        :type description: str
        :param listener_id: 转发策略对应的监听器ID
        :type listener_id: str
        :param redirect_pool_id: 转发到pool的ID。转发到pool的ID。当action为REDIRECT_TO_POOL时生效。
        :type redirect_pool_id: str
        :param redirect_listener_id: 转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。
        :type redirect_listener_id: str
        :param redirect_url: 转发到的url。该字段未启用。
        :type redirect_url: str
        :param position: 转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。
        :type position: int
        """
        
        

        self._id = None
        self._name = None
        self._rules = None
        self._action = None
        self._provisioning_status = None
        self._tenant_id = None
        self._project_id = None
        self._admin_state_up = None
        self._description = None
        self._listener_id = None
        self._redirect_pool_id = None
        self._redirect_listener_id = None
        self._redirect_url = None
        self._position = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.rules = rules
        self.action = action
        self.provisioning_status = provisioning_status
        self.tenant_id = tenant_id
        self.project_id = project_id
        self.admin_state_up = admin_state_up
        self.description = description
        self.listener_id = listener_id
        self.redirect_pool_id = redirect_pool_id
        self.redirect_listener_id = redirect_listener_id
        self.redirect_url = redirect_url
        self.position = position

    @property
    def id(self):
        """Gets the id of this L7policyResp.

        转发策略ID

        :return: The id of this L7policyResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this L7policyResp.

        转发策略ID

        :param id: The id of this L7policyResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this L7policyResp.

        转发策略名称

        :return: The name of this L7policyResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this L7policyResp.

        转发策略名称

        :param name: The name of this L7policyResp.
        :type name: str
        """
        self._name = name

    @property
    def rules(self):
        """Gets the rules of this L7policyResp.

        转发策略关联的转发规则列表

        :return: The rules of this L7policyResp.
        :rtype: list[:class:`huaweicloudsdkelb.v2.ResourceList`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this L7policyResp.

        转发策略关联的转发规则列表

        :param rules: The rules of this L7policyResp.
        :type rules: list[:class:`huaweicloudsdkelb.v2.ResourceList`]
        """
        self._rules = rules

    @property
    def action(self):
        """Gets the action of this L7policyResp.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :return: The action of this L7policyResp.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this L7policyResp.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :param action: The action of this L7policyResp.
        :type action: str
        """
        self._action = action

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this L7policyResp.

        健康检查的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :return: The provisioning_status of this L7policyResp.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this L7policyResp.

        健康检查的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this L7policyResp.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this L7policyResp.

        转发策略所在的项目ID。

        :return: The tenant_id of this L7policyResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this L7policyResp.

        转发策略所在的项目ID。

        :param tenant_id: The tenant_id of this L7policyResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        """Gets the project_id of this L7policyResp.

        转发策略所在的项目ID。

        :return: The project_id of this L7policyResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this L7policyResp.

        转发策略所在的项目ID。

        :param project_id: The project_id of this L7policyResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this L7policyResp.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this L7policyResp.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this L7policyResp.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this L7policyResp.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this L7policyResp.

        转发策略额描述信息

        :return: The description of this L7policyResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this L7policyResp.

        转发策略额描述信息

        :param description: The description of this L7policyResp.
        :type description: str
        """
        self._description = description

    @property
    def listener_id(self):
        """Gets the listener_id of this L7policyResp.

        转发策略对应的监听器ID

        :return: The listener_id of this L7policyResp.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this L7policyResp.

        转发策略对应的监听器ID

        :param listener_id: The listener_id of this L7policyResp.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this L7policyResp.

        转发到pool的ID。转发到pool的ID。当action为REDIRECT_TO_POOL时生效。

        :return: The redirect_pool_id of this L7policyResp.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this L7policyResp.

        转发到pool的ID。转发到pool的ID。当action为REDIRECT_TO_POOL时生效。

        :param redirect_pool_id: The redirect_pool_id of this L7policyResp.
        :type redirect_pool_id: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this L7policyResp.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。

        :return: The redirect_listener_id of this L7policyResp.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this L7policyResp.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。

        :param redirect_listener_id: The redirect_listener_id of this L7policyResp.
        :type redirect_listener_id: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_url(self):
        """Gets the redirect_url of this L7policyResp.

        转发到的url。该字段未启用。

        :return: The redirect_url of this L7policyResp.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this L7policyResp.

        转发到的url。该字段未启用。

        :param redirect_url: The redirect_url of this L7policyResp.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def position(self):
        """Gets the position of this L7policyResp.

        转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。

        :return: The position of this L7policyResp.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this L7policyResp.

        转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。

        :param position: The position of this L7policyResp.
        :type position: int
        """
        self._position = position

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
        if not isinstance(other, L7policyResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

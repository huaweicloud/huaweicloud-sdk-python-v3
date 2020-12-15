# coding: utf-8

import pprint
import re

import six





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
        'project_id': 'str',
        'provisioning_status': 'str',
        'redirect_listener_id': 'str',
        'redirect_pool_id': 'str',
        'redirect_url': 'str',
        'rules': 'list[RuleRef]'
    }

    attribute_map = {
        'action': 'action',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'id': 'id',
        'listener_id': 'listener_id',
        'name': 'name',
        'position': 'position',
        'project_id': 'project_id',
        'provisioning_status': 'provisioning_status',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_url': 'redirect_url',
        'rules': 'rules'
    }

    def __init__(self, action=None, admin_state_up=None, description=None, id=None, listener_id=None, name=None, position=None, project_id=None, provisioning_status=None, redirect_listener_id=None, redirect_pool_id=None, redirect_url=None, rules=None):
        """L7Policy - a model defined in huaweicloud sdk"""
        
        

        self._action = None
        self._admin_state_up = None
        self._description = None
        self._id = None
        self._listener_id = None
        self._name = None
        self._position = None
        self._project_id = None
        self._provisioning_status = None
        self._redirect_listener_id = None
        self._redirect_pool_id = None
        self._redirect_url = None
        self._rules = None
        self.discriminator = None

        self.action = action
        self.admin_state_up = admin_state_up
        self.description = description
        self.id = id
        self.listener_id = listener_id
        self.name = name
        self.position = position
        self.project_id = project_id
        self.provisioning_status = provisioning_status
        self.redirect_listener_id = redirect_listener_id
        self.redirect_pool_id = redirect_pool_id
        self.redirect_url = redirect_url
        self.rules = rules

    @property
    def action(self):
        """Gets the action of this L7Policy.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :return: The action of this L7Policy.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this L7Policy.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :param action: The action of this L7Policy.
        :type: str
        """
        self._action = action

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this L7Policy.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this L7Policy.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this L7Policy.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this L7Policy.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this L7Policy.

        转发策略描述信息

        :return: The description of this L7Policy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this L7Policy.

        转发策略描述信息

        :param description: The description of this L7Policy.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this L7Policy.

        转发策略ID

        :return: The id of this L7Policy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this L7Policy.

        转发策略ID

        :param id: The id of this L7Policy.
        :type: str
        """
        self._id = id

    @property
    def listener_id(self):
        """Gets the listener_id of this L7Policy.

        转发策略对应的监听器ID。当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或TERMINATED_HTTPS的listener上。 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。

        :return: The listener_id of this L7Policy.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this L7Policy.

        转发策略对应的监听器ID。当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或TERMINATED_HTTPS的listener上。 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。

        :param listener_id: The listener_id of this L7Policy.
        :type: str
        """
        self._listener_id = listener_id

    @property
    def name(self):
        """Gets the name of this L7Policy.

        转发策略名称

        :return: The name of this L7Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this L7Policy.

        转发策略名称

        :param name: The name of this L7Policy.
        :type: str
        """
        self._name = name

    @property
    def position(self):
        """Gets the position of this L7Policy.

        转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。

        :return: The position of this L7Policy.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this L7Policy.

        转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。

        :param position: The position of this L7Policy.
        :type: int
        """
        self._position = position

    @property
    def project_id(self):
        """Gets the project_id of this L7Policy.

        转发策略所在的项目ID。

        :return: The project_id of this L7Policy.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this L7Policy.

        转发策略所在的项目ID。

        :param project_id: The project_id of this L7Policy.
        :type: str
        """
        self._project_id = project_id

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this L7Policy.

        provisioning状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。 默认为ACTIVE。

        :return: The provisioning_status of this L7Policy.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this L7Policy.

        provisioning状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。 默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this L7Policy.
        :type: str
        """
        self._provisioning_status = provisioning_status

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this L7Policy.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。使用说明：只支持protocol为TERMINATED_HTTPS的listener。不能指定为其他loadbalancer下的listener。当action为REDIRECT_TO_POOL时，不可指定。

        :return: The redirect_listener_id of this L7Policy.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this L7Policy.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。使用说明：只支持protocol为TERMINATED_HTTPS的listener。不能指定为其他loadbalancer下的listener。当action为REDIRECT_TO_POOL时，不可指定。

        :param redirect_listener_id: The redirect_listener_id of this L7Policy.
        :type: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this L7Policy.

        转发到pool的ID。当action为REDIRECT_TO_POOL时生效。使用说明：指定的pool不能是listener的default_pool。不能是其他listener的l7policy使用的pool。当action为REDIRECT_TO_LISTENER时，不可指定。

        :return: The redirect_pool_id of this L7Policy.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this L7Policy.

        转发到pool的ID。当action为REDIRECT_TO_POOL时生效。使用说明：指定的pool不能是listener的default_pool。不能是其他listener的l7policy使用的pool。当action为REDIRECT_TO_LISTENER时，不可指定。

        :param redirect_pool_id: The redirect_pool_id of this L7Policy.
        :type: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_url(self):
        """Gets the redirect_url of this L7Policy.

        转发到的url。该字段未启用。

        :return: The redirect_url of this L7Policy.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this L7Policy.

        转发到的url。该字段未启用。

        :param redirect_url: The redirect_url of this L7Policy.
        :type: str
        """
        self._redirect_url = redirect_url

    @property
    def rules(self):
        """Gets the rules of this L7Policy.

        转发策略关联的转发规则列表

        :return: The rules of this L7Policy.
        :rtype: list[RuleRef]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this L7Policy.

        转发策略关联的转发规则列表

        :param rules: The rules of this L7Policy.
        :type: list[RuleRef]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, L7Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

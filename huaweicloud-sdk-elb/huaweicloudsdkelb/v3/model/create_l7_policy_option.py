# coding: utf-8

import pprint
import re

import six





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
        'project_id': 'str',
        'redirect_listener_id': 'str',
        'redirect_pool_id': 'str',
        'redirect_url': 'str',
        'rules': 'list[CreateL7PolicyRuleOption]'
    }

    attribute_map = {
        'action': 'action',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'listener_id': 'listener_id',
        'name': 'name',
        'position': 'position',
        'project_id': 'project_id',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_url': 'redirect_url',
        'rules': 'rules'
    }

    def __init__(self, action=None, admin_state_up=None, description=None, listener_id=None, name=None, position=None, project_id=None, redirect_listener_id=None, redirect_pool_id=None, redirect_url=None, rules=None):
        """CreateL7PolicyOption - a model defined in huaweicloud sdk"""
        
        

        self._action = None
        self._admin_state_up = None
        self._description = None
        self._listener_id = None
        self._name = None
        self._position = None
        self._project_id = None
        self._redirect_listener_id = None
        self._redirect_pool_id = None
        self._redirect_url = None
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
        if project_id is not None:
            self.project_id = project_id
        if redirect_listener_id is not None:
            self.redirect_listener_id = redirect_listener_id
        if redirect_pool_id is not None:
            self.redirect_pool_id = redirect_pool_id
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if rules is not None:
            self.rules = rules

    @property
    def action(self):
        """Gets the action of this CreateL7PolicyOption.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :return: The action of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateL7PolicyOption.

        转发策略的转发动作；取值：REDIRECT_TO_POOL：转发到后端云服务器组；REDIRECT_TO_LISTENER：重定向到监听器

        :param action: The action of this CreateL7PolicyOption.
        :type: str
        """
        self._action = action

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateL7PolicyOption.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this CreateL7PolicyOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateL7PolicyOption.

        转发策略的管理状态；该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this CreateL7PolicyOption.
        :type: bool
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
        :type: str
        """
        self._description = description

    @property
    def listener_id(self):
        """Gets the listener_id of this CreateL7PolicyOption.

        转发策略对应的监听器ID。当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或TERMINATED_HTTPS的listener上。 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。

        :return: The listener_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CreateL7PolicyOption.

        转发策略对应的监听器ID。当action为REDIRECT_TO_POOL时，只支持创建在PROTOCOL为HTTP或TERMINATED_HTTPS的listener上。 当action为REDIRECT_TO_LISTENER时，只支持创建在PROTOCOL为HTTP的listener上。

        :param listener_id: The listener_id of this CreateL7PolicyOption.
        :type: str
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
        :type: str
        """
        self._name = name

    @property
    def position(self):
        """Gets the position of this CreateL7PolicyOption.

        转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。

        :return: The position of this CreateL7PolicyOption.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CreateL7PolicyOption.

        转发策略的优先级，从1递增，最高100。该字段为预留字段，暂未启用。

        :param position: The position of this CreateL7PolicyOption.
        :type: int
        """
        self._position = position

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
        :type: str
        """
        self._project_id = project_id

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this CreateL7PolicyOption.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。当action为REDIRECT_TO_LISTENER时必选。

        :return: The redirect_listener_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this CreateL7PolicyOption.

        转发到的listener的ID，当action为REDIRECT_TO_LISTENER时生效。当action为REDIRECT_TO_LISTENER时必选。

        :param redirect_listener_id: The redirect_listener_id of this CreateL7PolicyOption.
        :type: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this CreateL7PolicyOption.

        转发到pool的ID。当action为REDIRECT_TO_POOL时生效。使用说明：指定的pool不能是listener的default_pool。不能是其他listener的l7policy使用的pool。当action为REDIRECT_TO_POOL时为必选字段。当action为REDIRECT_TO_LISTENER时，不可指定。

        :return: The redirect_pool_id of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this CreateL7PolicyOption.

        转发到pool的ID。当action为REDIRECT_TO_POOL时生效。使用说明：指定的pool不能是listener的default_pool。不能是其他listener的l7policy使用的pool。当action为REDIRECT_TO_POOL时为必选字段。当action为REDIRECT_TO_LISTENER时，不可指定。

        :param redirect_pool_id: The redirect_pool_id of this CreateL7PolicyOption.
        :type: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_url(self):
        """Gets the redirect_url of this CreateL7PolicyOption.

        转发到的url。该字段未启用。

        :return: The redirect_url of this CreateL7PolicyOption.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this CreateL7PolicyOption.

        转发到的url。该字段未启用。

        :param redirect_url: The redirect_url of this CreateL7PolicyOption.
        :type: str
        """
        self._redirect_url = redirect_url

    @property
    def rules(self):
        """Gets the rules of this CreateL7PolicyOption.

        转发策略关联的转发规则对象。详细参考表 l7rule字段说明。rules列表中最多含有2个rule对象，且每个rule的type字段不可相同。

        :return: The rules of this CreateL7PolicyOption.
        :rtype: list[CreateL7PolicyRuleOption]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this CreateL7PolicyOption.

        转发策略关联的转发规则对象。详细参考表 l7rule字段说明。rules列表中最多含有2个rule对象，且每个rule的type字段不可相同。

        :param rules: The rules of this CreateL7PolicyOption.
        :type: list[CreateL7PolicyRuleOption]
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
        if not isinstance(other, CreateL7PolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

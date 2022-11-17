# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListL7policiesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'admin_state_up': 'bool',
        'listener_id': 'str',
        'action': 'str',
        'redirect_pool_id': 'str',
        'redirect_listener_id': 'str',
        'redirect_url': 'str',
        'position': 'int',
        'provisioning_status': 'str',
        'enterprise_project_id': 'str',
        'display_all_rules': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
        'listener_id': 'listener_id',
        'action': 'action',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_url': 'redirect_url',
        'position': 'position',
        'provisioning_status': 'provisioning_status',
        'enterprise_project_id': 'enterprise_project_id',
        'display_all_rules': 'display_all_rules'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, description=None, admin_state_up=None, listener_id=None, action=None, redirect_pool_id=None, redirect_listener_id=None, redirect_url=None, position=None, provisioning_status=None, enterprise_project_id=None, display_all_rules=None):
        """ListL7policiesRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询中每页的转发策略个数
        :type limit: int
        :param marker: 分页查询的起始的资源id，表示上一页最后一条查询记录的转发策略的id。不指定时表示查询第一页。
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。
        :type page_reverse: bool
        :param id: 转发策略ID。
        :type id: str
        :param name: 转发策略名称。
        :type name: str
        :param description: 转发策略的描述信息。
        :type description: str
        :param admin_state_up: 转发策略的管理状态；取值范围： true/false。该字段为预留字段，暂未启用。默认为true。
        :type admin_state_up: bool
        :param listener_id: 转发策略所在的监听器ID。
        :type listener_id: str
        :param action: 转发策略的匹配动作。 取值范围：REDIRECT_TO_POOL：将匹配的流量转发到redirect_pool_id指定的后端云服务器组上；REDIRECT_TO_LISTENER：将listener_id指定的HTTP监听器的流量重定向到redirect_listener_id指定的TERMINATED_HTTPS监听器上。
        :type action: str
        :param redirect_pool_id: 流量匹配后转发到后端云服务器组的ID。
        :type redirect_pool_id: str
        :param redirect_listener_id: 流量匹配后转发到的监听器的ID。
        :type redirect_listener_id: str
        :param redirect_url: 转发策略重定向到的url。该字段为预留字段，暂未启用。
        :type redirect_url: str
        :param position: 转发优先级，从1递增，最高100。默认值：100；该字段为预留字段，暂未启用。
        :type position: int
        :param provisioning_status: 转发策略的配置状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。默认值：ACTIVE；该字段为预留字段，暂未启用。
        :type provisioning_status: str
        :param enterprise_project_id: 企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\&quot;0\&quot;表示查询默认企业项目资源；或者指定的企业项目ID下的资源。
        :type enterprise_project_id: str
        :param display_all_rules: 是否显示所有的rule信息。取值范围：false表示不显示（跟以前一样只显示ID）；true表示显示。
        :type display_all_rules: bool
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._admin_state_up = None
        self._listener_id = None
        self._action = None
        self._redirect_pool_id = None
        self._redirect_listener_id = None
        self._redirect_url = None
        self._position = None
        self._provisioning_status = None
        self._enterprise_project_id = None
        self._display_all_rules = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
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
        if action is not None:
            self.action = action
        if redirect_pool_id is not None:
            self.redirect_pool_id = redirect_pool_id
        if redirect_listener_id is not None:
            self.redirect_listener_id = redirect_listener_id
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if position is not None:
            self.position = position
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if display_all_rules is not None:
            self.display_all_rules = display_all_rules

    @property
    def limit(self):
        """Gets the limit of this ListL7policiesRequest.

        分页查询中每页的转发策略个数

        :return: The limit of this ListL7policiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListL7policiesRequest.

        分页查询中每页的转发策略个数

        :param limit: The limit of this ListL7policiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListL7policiesRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的转发策略的id。不指定时表示查询第一页。

        :return: The marker of this ListL7policiesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListL7policiesRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的转发策略的id。不指定时表示查询第一页。

        :param marker: The marker of this ListL7policiesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListL7policiesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListL7policiesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListL7policiesRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListL7policiesRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListL7policiesRequest.

        转发策略ID。

        :return: The id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListL7policiesRequest.

        转发策略ID。

        :param id: The id of this ListL7policiesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListL7policiesRequest.

        转发策略名称。

        :return: The name of this ListL7policiesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListL7policiesRequest.

        转发策略名称。

        :param name: The name of this ListL7policiesRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListL7policiesRequest.

        转发策略的描述信息。

        :return: The description of this ListL7policiesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListL7policiesRequest.

        转发策略的描述信息。

        :param description: The description of this ListL7policiesRequest.
        :type description: str
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListL7policiesRequest.

        转发策略的管理状态；取值范围： true/false。该字段为预留字段，暂未启用。默认为true。

        :return: The admin_state_up of this ListL7policiesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListL7policiesRequest.

        转发策略的管理状态；取值范围： true/false。该字段为预留字段，暂未启用。默认为true。

        :param admin_state_up: The admin_state_up of this ListL7policiesRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def listener_id(self):
        """Gets the listener_id of this ListL7policiesRequest.

        转发策略所在的监听器ID。

        :return: The listener_id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ListL7policiesRequest.

        转发策略所在的监听器ID。

        :param listener_id: The listener_id of this ListL7policiesRequest.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def action(self):
        """Gets the action of this ListL7policiesRequest.

        转发策略的匹配动作。 取值范围：REDIRECT_TO_POOL：将匹配的流量转发到redirect_pool_id指定的后端云服务器组上；REDIRECT_TO_LISTENER：将listener_id指定的HTTP监听器的流量重定向到redirect_listener_id指定的TERMINATED_HTTPS监听器上。

        :return: The action of this ListL7policiesRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListL7policiesRequest.

        转发策略的匹配动作。 取值范围：REDIRECT_TO_POOL：将匹配的流量转发到redirect_pool_id指定的后端云服务器组上；REDIRECT_TO_LISTENER：将listener_id指定的HTTP监听器的流量重定向到redirect_listener_id指定的TERMINATED_HTTPS监听器上。

        :param action: The action of this ListL7policiesRequest.
        :type action: str
        """
        self._action = action

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this ListL7policiesRequest.

        流量匹配后转发到后端云服务器组的ID。

        :return: The redirect_pool_id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this ListL7policiesRequest.

        流量匹配后转发到后端云服务器组的ID。

        :param redirect_pool_id: The redirect_pool_id of this ListL7policiesRequest.
        :type redirect_pool_id: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this ListL7policiesRequest.

        流量匹配后转发到的监听器的ID。

        :return: The redirect_listener_id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this ListL7policiesRequest.

        流量匹配后转发到的监听器的ID。

        :param redirect_listener_id: The redirect_listener_id of this ListL7policiesRequest.
        :type redirect_listener_id: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_url(self):
        """Gets the redirect_url of this ListL7policiesRequest.

        转发策略重定向到的url。该字段为预留字段，暂未启用。

        :return: The redirect_url of this ListL7policiesRequest.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this ListL7policiesRequest.

        转发策略重定向到的url。该字段为预留字段，暂未启用。

        :param redirect_url: The redirect_url of this ListL7policiesRequest.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

    @property
    def position(self):
        """Gets the position of this ListL7policiesRequest.

        转发优先级，从1递增，最高100。默认值：100；该字段为预留字段，暂未启用。

        :return: The position of this ListL7policiesRequest.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ListL7policiesRequest.

        转发优先级，从1递增，最高100。默认值：100；该字段为预留字段，暂未启用。

        :param position: The position of this ListL7policiesRequest.
        :type position: int
        """
        self._position = position

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ListL7policiesRequest.

        转发策略的配置状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。默认值：ACTIVE；该字段为预留字段，暂未启用。

        :return: The provisioning_status of this ListL7policiesRequest.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ListL7policiesRequest.

        转发策略的配置状态，可以为ACTIVE、PENDING_CREATE 或者ERROR。默认值：ACTIVE；该字段为预留字段，暂未启用。

        :param provisioning_status: The provisioning_status of this ListL7policiesRequest.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListL7policiesRequest.

        企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\"0\"表示查询默认企业项目资源；或者指定的企业项目ID下的资源。

        :return: The enterprise_project_id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListL7policiesRequest.

        企业项目ID。  传入all_granted_eps表示查询所有有权限的企业项目资源；\"0\"表示查询默认企业项目资源；或者指定的企业项目ID下的资源。

        :param enterprise_project_id: The enterprise_project_id of this ListL7policiesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def display_all_rules(self):
        """Gets the display_all_rules of this ListL7policiesRequest.

        是否显示所有的rule信息。取值范围：false表示不显示（跟以前一样只显示ID）；true表示显示。

        :return: The display_all_rules of this ListL7policiesRequest.
        :rtype: bool
        """
        return self._display_all_rules

    @display_all_rules.setter
    def display_all_rules(self, display_all_rules):
        """Sets the display_all_rules of this ListL7policiesRequest.

        是否显示所有的rule信息。取值范围：false表示不显示（跟以前一样只显示ID）；true表示显示。

        :param display_all_rules: The display_all_rules of this ListL7policiesRequest.
        :type display_all_rules: bool
        """
        self._display_all_rules = display_all_rules

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
        if not isinstance(other, ListL7policiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

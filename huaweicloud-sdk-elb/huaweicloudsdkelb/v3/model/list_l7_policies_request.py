# coding: utf-8

import pprint
import re

import six





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
        'action': 'list[str]',
        'admin_state_up': 'bool',
        'description': 'list[str]',
        'display_all_rules': 'bool',
        'enterprise_project_id': 'list[str]',
        'id': 'list[str]',
        'limit': 'int',
        'listener_id': 'list[str]',
        'marker': 'str',
        'name': 'list[str]',
        'page_reverse': 'bool',
        'position': 'list[int]',
        'provisioning_status': 'list[str]',
        'redirect_listener_id': 'list[str]',
        'redirect_pool_id': 'list[str]',
        'redirect_url': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'admin_state_up': 'admin_state_up',
        'description': 'description',
        'display_all_rules': 'display_all_rules',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'limit': 'limit',
        'listener_id': 'listener_id',
        'marker': 'marker',
        'name': 'name',
        'page_reverse': 'page_reverse',
        'position': 'position',
        'provisioning_status': 'provisioning_status',
        'redirect_listener_id': 'redirect_listener_id',
        'redirect_pool_id': 'redirect_pool_id',
        'redirect_url': 'redirect_url'
    }

    def __init__(self, action=None, admin_state_up=None, description=None, display_all_rules=None, enterprise_project_id=None, id=None, limit=None, listener_id=None, marker=None, name=None, page_reverse=None, position=None, provisioning_status=None, redirect_listener_id=None, redirect_pool_id=None, redirect_url=None):
        """ListL7PoliciesRequest - a model defined in huaweicloud sdk"""
        
        

        self._action = None
        self._admin_state_up = None
        self._description = None
        self._display_all_rules = None
        self._enterprise_project_id = None
        self._id = None
        self._limit = None
        self._listener_id = None
        self._marker = None
        self._name = None
        self._page_reverse = None
        self._position = None
        self._provisioning_status = None
        self._redirect_listener_id = None
        self._redirect_pool_id = None
        self._redirect_url = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if description is not None:
            self.description = description
        if display_all_rules is not None:
            self.display_all_rules = display_all_rules
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if listener_id is not None:
            self.listener_id = listener_id
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if position is not None:
            self.position = position
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if redirect_listener_id is not None:
            self.redirect_listener_id = redirect_listener_id
        if redirect_pool_id is not None:
            self.redirect_pool_id = redirect_pool_id
        if redirect_url is not None:
            self.redirect_url = redirect_url

    @property
    def action(self):
        """Gets the action of this ListL7PoliciesRequest.


        :return: The action of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListL7PoliciesRequest.


        :param action: The action of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._action = action

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListL7PoliciesRequest.


        :return: The admin_state_up of this ListL7PoliciesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListL7PoliciesRequest.


        :param admin_state_up: The admin_state_up of this ListL7PoliciesRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def description(self):
        """Gets the description of this ListL7PoliciesRequest.


        :return: The description of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListL7PoliciesRequest.


        :param description: The description of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._description = description

    @property
    def display_all_rules(self):
        """Gets the display_all_rules of this ListL7PoliciesRequest.


        :return: The display_all_rules of this ListL7PoliciesRequest.
        :rtype: bool
        """
        return self._display_all_rules

    @display_all_rules.setter
    def display_all_rules(self, display_all_rules):
        """Sets the display_all_rules of this ListL7PoliciesRequest.


        :param display_all_rules: The display_all_rules of this ListL7PoliciesRequest.
        :type: bool
        """
        self._display_all_rules = display_all_rules

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListL7PoliciesRequest.


        :return: The enterprise_project_id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListL7PoliciesRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this ListL7PoliciesRequest.


        :return: The id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListL7PoliciesRequest.


        :param id: The id of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListL7PoliciesRequest.


        :return: The limit of this ListL7PoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListL7PoliciesRequest.


        :param limit: The limit of this ListL7PoliciesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def listener_id(self):
        """Gets the listener_id of this ListL7PoliciesRequest.


        :return: The listener_id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ListL7PoliciesRequest.


        :param listener_id: The listener_id of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._listener_id = listener_id

    @property
    def marker(self):
        """Gets the marker of this ListL7PoliciesRequest.


        :return: The marker of this ListL7PoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListL7PoliciesRequest.


        :param marker: The marker of this ListL7PoliciesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListL7PoliciesRequest.


        :return: The name of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListL7PoliciesRequest.


        :param name: The name of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListL7PoliciesRequest.


        :return: The page_reverse of this ListL7PoliciesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListL7PoliciesRequest.


        :param page_reverse: The page_reverse of this ListL7PoliciesRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def position(self):
        """Gets the position of this ListL7PoliciesRequest.


        :return: The position of this ListL7PoliciesRequest.
        :rtype: list[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ListL7PoliciesRequest.


        :param position: The position of this ListL7PoliciesRequest.
        :type: list[int]
        """
        self._position = position

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ListL7PoliciesRequest.


        :return: The provisioning_status of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ListL7PoliciesRequest.


        :param provisioning_status: The provisioning_status of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._provisioning_status = provisioning_status

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this ListL7PoliciesRequest.


        :return: The redirect_listener_id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this ListL7PoliciesRequest.


        :param redirect_listener_id: The redirect_listener_id of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this ListL7PoliciesRequest.


        :return: The redirect_pool_id of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this ListL7PoliciesRequest.


        :param redirect_pool_id: The redirect_pool_id of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_url(self):
        """Gets the redirect_url of this ListL7PoliciesRequest.


        :return: The redirect_url of this ListL7PoliciesRequest.
        :rtype: list[str]
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this ListL7PoliciesRequest.


        :param redirect_url: The redirect_url of this ListL7PoliciesRequest.
        :type: list[str]
        """
        self._redirect_url = redirect_url

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
        if not isinstance(other, ListL7PoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

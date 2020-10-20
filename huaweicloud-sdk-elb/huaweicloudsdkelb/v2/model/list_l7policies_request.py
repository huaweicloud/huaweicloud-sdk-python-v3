# coding: utf-8

import pprint
import re

import six





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
        """ListL7policiesRequest - a model defined in huaweicloud sdk"""
        
        

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


        :return: The limit of this ListL7policiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListL7policiesRequest.


        :param limit: The limit of this ListL7policiesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListL7policiesRequest.


        :return: The marker of this ListL7policiesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListL7policiesRequest.


        :param marker: The marker of this ListL7policiesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListL7policiesRequest.


        :return: The page_reverse of this ListL7policiesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListL7policiesRequest.


        :param page_reverse: The page_reverse of this ListL7policiesRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListL7policiesRequest.


        :return: The id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListL7policiesRequest.


        :param id: The id of this ListL7policiesRequest.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListL7policiesRequest.


        :return: The name of this ListL7policiesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListL7policiesRequest.


        :param name: The name of this ListL7policiesRequest.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListL7policiesRequest.


        :return: The description of this ListL7policiesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListL7policiesRequest.


        :param description: The description of this ListL7policiesRequest.
        :type: str
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListL7policiesRequest.


        :return: The admin_state_up of this ListL7policiesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListL7policiesRequest.


        :param admin_state_up: The admin_state_up of this ListL7policiesRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def listener_id(self):
        """Gets the listener_id of this ListL7policiesRequest.


        :return: The listener_id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ListL7policiesRequest.


        :param listener_id: The listener_id of this ListL7policiesRequest.
        :type: str
        """
        self._listener_id = listener_id

    @property
    def action(self):
        """Gets the action of this ListL7policiesRequest.


        :return: The action of this ListL7policiesRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListL7policiesRequest.


        :param action: The action of this ListL7policiesRequest.
        :type: str
        """
        self._action = action

    @property
    def redirect_pool_id(self):
        """Gets the redirect_pool_id of this ListL7policiesRequest.


        :return: The redirect_pool_id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._redirect_pool_id

    @redirect_pool_id.setter
    def redirect_pool_id(self, redirect_pool_id):
        """Sets the redirect_pool_id of this ListL7policiesRequest.


        :param redirect_pool_id: The redirect_pool_id of this ListL7policiesRequest.
        :type: str
        """
        self._redirect_pool_id = redirect_pool_id

    @property
    def redirect_listener_id(self):
        """Gets the redirect_listener_id of this ListL7policiesRequest.


        :return: The redirect_listener_id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._redirect_listener_id

    @redirect_listener_id.setter
    def redirect_listener_id(self, redirect_listener_id):
        """Sets the redirect_listener_id of this ListL7policiesRequest.


        :param redirect_listener_id: The redirect_listener_id of this ListL7policiesRequest.
        :type: str
        """
        self._redirect_listener_id = redirect_listener_id

    @property
    def redirect_url(self):
        """Gets the redirect_url of this ListL7policiesRequest.


        :return: The redirect_url of this ListL7policiesRequest.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this ListL7policiesRequest.


        :param redirect_url: The redirect_url of this ListL7policiesRequest.
        :type: str
        """
        self._redirect_url = redirect_url

    @property
    def position(self):
        """Gets the position of this ListL7policiesRequest.


        :return: The position of this ListL7policiesRequest.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ListL7policiesRequest.


        :param position: The position of this ListL7policiesRequest.
        :type: int
        """
        self._position = position

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ListL7policiesRequest.


        :return: The provisioning_status of this ListL7policiesRequest.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ListL7policiesRequest.


        :param provisioning_status: The provisioning_status of this ListL7policiesRequest.
        :type: str
        """
        self._provisioning_status = provisioning_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListL7policiesRequest.


        :return: The enterprise_project_id of this ListL7policiesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListL7policiesRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListL7policiesRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def display_all_rules(self):
        """Gets the display_all_rules of this ListL7policiesRequest.


        :return: The display_all_rules of this ListL7policiesRequest.
        :rtype: bool
        """
        return self._display_all_rules

    @display_all_rules.setter
    def display_all_rules(self, display_all_rules):
        """Sets the display_all_rules of this ListL7policiesRequest.


        :param display_all_rules: The display_all_rules of this ListL7policiesRequest.
        :type: bool
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListL7policiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

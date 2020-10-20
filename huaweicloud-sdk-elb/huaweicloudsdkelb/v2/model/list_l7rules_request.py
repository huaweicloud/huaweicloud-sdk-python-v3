# coding: utf-8

import pprint
import re

import six





class ListL7rulesRequest:


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
        'l7policy_id': 'str',
        'id': 'str',
        'admin_state_up': 'bool',
        'type': 'str',
        'compare_type': 'str',
        'invert': 'bool',
        'key': 'str',
        'value': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'l7policy_id': 'l7policy_id',
        'id': 'id',
        'admin_state_up': 'admin_state_up',
        'type': 'type',
        'compare_type': 'compare_type',
        'invert': 'invert',
        'key': 'key',
        'value': 'value',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, l7policy_id=None, id=None, admin_state_up=None, type=None, compare_type=None, invert=None, key=None, value=None, provisioning_status=None):
        """ListL7rulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._l7policy_id = None
        self._id = None
        self._admin_state_up = None
        self._type = None
        self._compare_type = None
        self._invert = None
        self._key = None
        self._value = None
        self._provisioning_status = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        self.l7policy_id = l7policy_id
        if id is not None:
            self.id = id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if type is not None:
            self.type = type
        if compare_type is not None:
            self.compare_type = compare_type
        if invert is not None:
            self.invert = invert
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status

    @property
    def limit(self):
        """Gets the limit of this ListL7rulesRequest.


        :return: The limit of this ListL7rulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListL7rulesRequest.


        :param limit: The limit of this ListL7rulesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListL7rulesRequest.


        :return: The marker of this ListL7rulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListL7rulesRequest.


        :param marker: The marker of this ListL7rulesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListL7rulesRequest.


        :return: The page_reverse of this ListL7rulesRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListL7rulesRequest.


        :param page_reverse: The page_reverse of this ListL7rulesRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def l7policy_id(self):
        """Gets the l7policy_id of this ListL7rulesRequest.


        :return: The l7policy_id of this ListL7rulesRequest.
        :rtype: str
        """
        return self._l7policy_id

    @l7policy_id.setter
    def l7policy_id(self, l7policy_id):
        """Sets the l7policy_id of this ListL7rulesRequest.


        :param l7policy_id: The l7policy_id of this ListL7rulesRequest.
        :type: str
        """
        self._l7policy_id = l7policy_id

    @property
    def id(self):
        """Gets the id of this ListL7rulesRequest.


        :return: The id of this ListL7rulesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListL7rulesRequest.


        :param id: The id of this ListL7rulesRequest.
        :type: str
        """
        self._id = id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListL7rulesRequest.


        :return: The admin_state_up of this ListL7rulesRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListL7rulesRequest.


        :param admin_state_up: The admin_state_up of this ListL7rulesRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def type(self):
        """Gets the type of this ListL7rulesRequest.


        :return: The type of this ListL7rulesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListL7rulesRequest.


        :param type: The type of this ListL7rulesRequest.
        :type: str
        """
        self._type = type

    @property
    def compare_type(self):
        """Gets the compare_type of this ListL7rulesRequest.


        :return: The compare_type of this ListL7rulesRequest.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this ListL7rulesRequest.


        :param compare_type: The compare_type of this ListL7rulesRequest.
        :type: str
        """
        self._compare_type = compare_type

    @property
    def invert(self):
        """Gets the invert of this ListL7rulesRequest.


        :return: The invert of this ListL7rulesRequest.
        :rtype: bool
        """
        return self._invert

    @invert.setter
    def invert(self, invert):
        """Sets the invert of this ListL7rulesRequest.


        :param invert: The invert of this ListL7rulesRequest.
        :type: bool
        """
        self._invert = invert

    @property
    def key(self):
        """Gets the key of this ListL7rulesRequest.


        :return: The key of this ListL7rulesRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ListL7rulesRequest.


        :param key: The key of this ListL7rulesRequest.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this ListL7rulesRequest.


        :return: The value of this ListL7rulesRequest.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ListL7rulesRequest.


        :param value: The value of this ListL7rulesRequest.
        :type: str
        """
        self._value = value

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ListL7rulesRequest.


        :return: The provisioning_status of this ListL7rulesRequest.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ListL7rulesRequest.


        :param provisioning_status: The provisioning_status of this ListL7rulesRequest.
        :type: str
        """
        self._provisioning_status = provisioning_status

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
        if not isinstance(other, ListL7rulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

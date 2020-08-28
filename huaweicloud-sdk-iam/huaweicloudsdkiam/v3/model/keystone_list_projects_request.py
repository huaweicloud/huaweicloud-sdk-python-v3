# coding: utf-8

import pprint
import re

import six





class KeystoneListProjectsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'name': 'str',
        'parent_id': 'str',
        'enabled': 'bool',
        'is_domain': 'bool',
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'name': 'name',
        'parent_id': 'parent_id',
        'enabled': 'enabled',
        'is_domain': 'is_domain',
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, domain_id=None, name=None, parent_id=None, enabled=None, is_domain=None, page=None, per_page=None):
        """KeystoneListProjectsRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._name = None
        self._parent_id = None
        self._enabled = None
        self._is_domain = None
        self._page = None
        self._per_page = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if enabled is not None:
            self.enabled = enabled
        if is_domain is not None:
            self.is_domain = is_domain
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneListProjectsRequest.


        :return: The domain_id of this KeystoneListProjectsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneListProjectsRequest.


        :param domain_id: The domain_id of this KeystoneListProjectsRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this KeystoneListProjectsRequest.


        :return: The name of this KeystoneListProjectsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeystoneListProjectsRequest.


        :param name: The name of this KeystoneListProjectsRequest.
        :type: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this KeystoneListProjectsRequest.


        :return: The parent_id of this KeystoneListProjectsRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this KeystoneListProjectsRequest.


        :param parent_id: The parent_id of this KeystoneListProjectsRequest.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def enabled(self):
        """Gets the enabled of this KeystoneListProjectsRequest.


        :return: The enabled of this KeystoneListProjectsRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this KeystoneListProjectsRequest.


        :param enabled: The enabled of this KeystoneListProjectsRequest.
        :type: bool
        """
        self._enabled = enabled

    @property
    def is_domain(self):
        """Gets the is_domain of this KeystoneListProjectsRequest.


        :return: The is_domain of this KeystoneListProjectsRequest.
        :rtype: bool
        """
        return self._is_domain

    @is_domain.setter
    def is_domain(self, is_domain):
        """Sets the is_domain of this KeystoneListProjectsRequest.


        :param is_domain: The is_domain of this KeystoneListProjectsRequest.
        :type: bool
        """
        self._is_domain = is_domain

    @property
    def page(self):
        """Gets the page of this KeystoneListProjectsRequest.


        :return: The page of this KeystoneListProjectsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this KeystoneListProjectsRequest.


        :param page: The page of this KeystoneListProjectsRequest.
        :type: int
        """
        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this KeystoneListProjectsRequest.


        :return: The per_page of this KeystoneListProjectsRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this KeystoneListProjectsRequest.


        :param per_page: The per_page of this KeystoneListProjectsRequest.
        :type: int
        """
        self._per_page = per_page

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
        if not isinstance(other, KeystoneListProjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

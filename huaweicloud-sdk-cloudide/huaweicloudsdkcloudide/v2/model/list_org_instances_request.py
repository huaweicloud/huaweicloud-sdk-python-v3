# coding: utf-8

import pprint
import re

import six





class ListOrgInstancesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_temporary': 'bool',
        'limit': 'int',
        'offset': 'int',
        'org_id': 'str',
        'search': 'str'
    }

    attribute_map = {
        'is_temporary': 'is_temporary',
        'limit': 'limit',
        'offset': 'offset',
        'org_id': 'org_id',
        'search': 'search'
    }

    def __init__(self, is_temporary=None, limit=30, offset=0, org_id=None, search=None):
        """ListOrgInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._is_temporary = None
        self._limit = None
        self._offset = None
        self._org_id = None
        self._search = None
        self.discriminator = None

        if is_temporary is not None:
            self.is_temporary = is_temporary
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.org_id = org_id
        if search is not None:
            self.search = search

    @property
    def is_temporary(self):
        """Gets the is_temporary of this ListOrgInstancesRequest.


        :return: The is_temporary of this ListOrgInstancesRequest.
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        """Sets the is_temporary of this ListOrgInstancesRequest.


        :param is_temporary: The is_temporary of this ListOrgInstancesRequest.
        :type: bool
        """
        self._is_temporary = is_temporary

    @property
    def limit(self):
        """Gets the limit of this ListOrgInstancesRequest.


        :return: The limit of this ListOrgInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListOrgInstancesRequest.


        :param limit: The limit of this ListOrgInstancesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListOrgInstancesRequest.


        :return: The offset of this ListOrgInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListOrgInstancesRequest.


        :param offset: The offset of this ListOrgInstancesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def org_id(self):
        """Gets the org_id of this ListOrgInstancesRequest.


        :return: The org_id of this ListOrgInstancesRequest.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this ListOrgInstancesRequest.


        :param org_id: The org_id of this ListOrgInstancesRequest.
        :type: str
        """
        self._org_id = org_id

    @property
    def search(self):
        """Gets the search of this ListOrgInstancesRequest.


        :return: The search of this ListOrgInstancesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListOrgInstancesRequest.


        :param search: The search of this ListOrgInstancesRequest.
        :type: str
        """
        self._search = search

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
        if not isinstance(other, ListOrgInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import pprint
import re

import six





class ListEnterpriseOrganizationsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'recursive_query': 'int',
        'parent_id': 'str'
    }

    attribute_map = {
        'recursive_query': 'recursive_query',
        'parent_id': 'parent_id'
    }

    def __init__(self, recursive_query=0, parent_id=None):
        """ListEnterpriseOrganizationsRequest - a model defined in huaweicloud sdk"""
        
        

        self._recursive_query = None
        self._parent_id = None
        self.discriminator = None

        if recursive_query is not None:
            self.recursive_query = recursive_query
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def recursive_query(self):
        """Gets the recursive_query of this ListEnterpriseOrganizationsRequest.


        :return: The recursive_query of this ListEnterpriseOrganizationsRequest.
        :rtype: int
        """
        return self._recursive_query

    @recursive_query.setter
    def recursive_query(self, recursive_query):
        """Sets the recursive_query of this ListEnterpriseOrganizationsRequest.


        :param recursive_query: The recursive_query of this ListEnterpriseOrganizationsRequest.
        :type: int
        """
        self._recursive_query = recursive_query

    @property
    def parent_id(self):
        """Gets the parent_id of this ListEnterpriseOrganizationsRequest.


        :return: The parent_id of this ListEnterpriseOrganizationsRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ListEnterpriseOrganizationsRequest.


        :param parent_id: The parent_id of this ListEnterpriseOrganizationsRequest.
        :type: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, ListEnterpriseOrganizationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

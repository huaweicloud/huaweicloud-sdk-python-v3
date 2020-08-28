# coding: utf-8

import pprint
import re

import six





class AssociateAgencyWithAllProjectsPermissionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'agency_id': 'str',
        'domain_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'agency_id': 'agency_id',
        'domain_id': 'domain_id',
        'role_id': 'role_id'
    }

    def __init__(self, agency_id=None, domain_id=None, role_id=None):
        """AssociateAgencyWithAllProjectsPermissionRequest - a model defined in huaweicloud sdk"""
        
        

        self._agency_id = None
        self._domain_id = None
        self._role_id = None
        self.discriminator = None

        self.agency_id = agency_id
        self.domain_id = domain_id
        self.role_id = role_id

    @property
    def agency_id(self):
        """Gets the agency_id of this AssociateAgencyWithAllProjectsPermissionRequest.


        :return: The agency_id of this AssociateAgencyWithAllProjectsPermissionRequest.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        """Sets the agency_id of this AssociateAgencyWithAllProjectsPermissionRequest.


        :param agency_id: The agency_id of this AssociateAgencyWithAllProjectsPermissionRequest.
        :type: str
        """
        self._agency_id = agency_id

    @property
    def domain_id(self):
        """Gets the domain_id of this AssociateAgencyWithAllProjectsPermissionRequest.


        :return: The domain_id of this AssociateAgencyWithAllProjectsPermissionRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this AssociateAgencyWithAllProjectsPermissionRequest.


        :param domain_id: The domain_id of this AssociateAgencyWithAllProjectsPermissionRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def role_id(self):
        """Gets the role_id of this AssociateAgencyWithAllProjectsPermissionRequest.


        :return: The role_id of this AssociateAgencyWithAllProjectsPermissionRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this AssociateAgencyWithAllProjectsPermissionRequest.


        :param role_id: The role_id of this AssociateAgencyWithAllProjectsPermissionRequest.
        :type: str
        """
        self._role_id = role_id

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
        if not isinstance(other, AssociateAgencyWithAllProjectsPermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

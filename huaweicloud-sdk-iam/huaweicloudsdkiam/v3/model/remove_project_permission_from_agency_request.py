# coding: utf-8

import pprint
import re

import six





class RemoveProjectPermissionFromAgencyRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'agency_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'agency_id': 'agency_id',
        'role_id': 'role_id'
    }

    def __init__(self, project_id=None, agency_id=None, role_id=None):
        """RemoveProjectPermissionFromAgencyRequest - a model defined in huaweicloud sdk"""
        
        

        self._project_id = None
        self._agency_id = None
        self._role_id = None
        self.discriminator = None

        self.project_id = project_id
        self.agency_id = agency_id
        self.role_id = role_id

    @property
    def project_id(self):
        """Gets the project_id of this RemoveProjectPermissionFromAgencyRequest.


        :return: The project_id of this RemoveProjectPermissionFromAgencyRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RemoveProjectPermissionFromAgencyRequest.


        :param project_id: The project_id of this RemoveProjectPermissionFromAgencyRequest.
        :type: str
        """
        self._project_id = project_id

    @property
    def agency_id(self):
        """Gets the agency_id of this RemoveProjectPermissionFromAgencyRequest.


        :return: The agency_id of this RemoveProjectPermissionFromAgencyRequest.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        """Sets the agency_id of this RemoveProjectPermissionFromAgencyRequest.


        :param agency_id: The agency_id of this RemoveProjectPermissionFromAgencyRequest.
        :type: str
        """
        self._agency_id = agency_id

    @property
    def role_id(self):
        """Gets the role_id of this RemoveProjectPermissionFromAgencyRequest.


        :return: The role_id of this RemoveProjectPermissionFromAgencyRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this RemoveProjectPermissionFromAgencyRequest.


        :param role_id: The role_id of this RemoveProjectPermissionFromAgencyRequest.
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
        if not isinstance(other, RemoveProjectPermissionFromAgencyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

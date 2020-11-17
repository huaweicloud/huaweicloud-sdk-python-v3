# coding: utf-8

import pprint
import re

import six





class ListPolicyStatesByAssignmentIdRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'policy_assignment_id': 'str',
        'compliance_state': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'policy_assignment_id': 'policy_assignment_id',
        'compliance_state': 'compliance_state',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, policy_assignment_id=None, compliance_state=None, resource_id=None, resource_name=None, limit=None, marker=None):
        """ListPolicyStatesByAssignmentIdRequest - a model defined in huaweicloud sdk"""
        
        

        self._policy_assignment_id = None
        self._compliance_state = None
        self._resource_id = None
        self._resource_name = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.policy_assignment_id = policy_assignment_id
        if compliance_state is not None:
            self.compliance_state = compliance_state
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def policy_assignment_id(self):
        """Gets the policy_assignment_id of this ListPolicyStatesByAssignmentIdRequest.


        :return: The policy_assignment_id of this ListPolicyStatesByAssignmentIdRequest.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        """Sets the policy_assignment_id of this ListPolicyStatesByAssignmentIdRequest.


        :param policy_assignment_id: The policy_assignment_id of this ListPolicyStatesByAssignmentIdRequest.
        :type: str
        """
        self._policy_assignment_id = policy_assignment_id

    @property
    def compliance_state(self):
        """Gets the compliance_state of this ListPolicyStatesByAssignmentIdRequest.


        :return: The compliance_state of this ListPolicyStatesByAssignmentIdRequest.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        """Sets the compliance_state of this ListPolicyStatesByAssignmentIdRequest.


        :param compliance_state: The compliance_state of this ListPolicyStatesByAssignmentIdRequest.
        :type: str
        """
        self._compliance_state = compliance_state

    @property
    def resource_id(self):
        """Gets the resource_id of this ListPolicyStatesByAssignmentIdRequest.


        :return: The resource_id of this ListPolicyStatesByAssignmentIdRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListPolicyStatesByAssignmentIdRequest.


        :param resource_id: The resource_id of this ListPolicyStatesByAssignmentIdRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ListPolicyStatesByAssignmentIdRequest.


        :return: The resource_name of this ListPolicyStatesByAssignmentIdRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListPolicyStatesByAssignmentIdRequest.


        :param resource_name: The resource_name of this ListPolicyStatesByAssignmentIdRequest.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def limit(self):
        """Gets the limit of this ListPolicyStatesByAssignmentIdRequest.


        :return: The limit of this ListPolicyStatesByAssignmentIdRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPolicyStatesByAssignmentIdRequest.


        :param limit: The limit of this ListPolicyStatesByAssignmentIdRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPolicyStatesByAssignmentIdRequest.


        :return: The marker of this ListPolicyStatesByAssignmentIdRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPolicyStatesByAssignmentIdRequest.


        :param marker: The marker of this ListPolicyStatesByAssignmentIdRequest.
        :type: str
        """
        self._marker = marker

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
        if not isinstance(other, ListPolicyStatesByAssignmentIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

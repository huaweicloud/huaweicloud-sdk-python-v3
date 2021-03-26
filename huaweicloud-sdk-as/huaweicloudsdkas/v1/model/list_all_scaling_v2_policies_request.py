# coding: utf-8

import pprint
import re

import six





class ListAllScalingV2PoliciesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_resource_id': 'str',
        'scaling_resource_type': 'str',
        'scaling_policy_name': 'str',
        'scaling_policy_type': 'str',
        'scaling_policy_id': 'str',
        'start_number': 'int',
        'limit': 'int',
        'sort_by': 'str',
        'order': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'scaling_resource_id': 'scaling_resource_id',
        'scaling_resource_type': 'scaling_resource_type',
        'scaling_policy_name': 'scaling_policy_name',
        'scaling_policy_type': 'scaling_policy_type',
        'scaling_policy_id': 'scaling_policy_id',
        'start_number': 'start_number',
        'limit': 'limit',
        'sort_by': 'sort_by',
        'order': 'order',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, scaling_resource_id=None, scaling_resource_type=None, scaling_policy_name=None, scaling_policy_type=None, scaling_policy_id=None, start_number=None, limit=None, sort_by=None, order=None, enterprise_project_id=None):
        """ListAllScalingV2PoliciesRequest - a model defined in huaweicloud sdk"""
        
        

        self._scaling_resource_id = None
        self._scaling_resource_type = None
        self._scaling_policy_name = None
        self._scaling_policy_type = None
        self._scaling_policy_id = None
        self._start_number = None
        self._limit = None
        self._sort_by = None
        self._order = None
        self._enterprise_project_id = None
        self.discriminator = None

        if scaling_resource_id is not None:
            self.scaling_resource_id = scaling_resource_id
        if scaling_resource_type is not None:
            self.scaling_resource_type = scaling_resource_type
        if scaling_policy_name is not None:
            self.scaling_policy_name = scaling_policy_name
        if scaling_policy_type is not None:
            self.scaling_policy_type = scaling_policy_type
        if scaling_policy_id is not None:
            self.scaling_policy_id = scaling_policy_id
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def scaling_resource_id(self):
        """Gets the scaling_resource_id of this ListAllScalingV2PoliciesRequest.


        :return: The scaling_resource_id of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_resource_id

    @scaling_resource_id.setter
    def scaling_resource_id(self, scaling_resource_id):
        """Sets the scaling_resource_id of this ListAllScalingV2PoliciesRequest.


        :param scaling_resource_id: The scaling_resource_id of this ListAllScalingV2PoliciesRequest.
        :type: str
        """
        self._scaling_resource_id = scaling_resource_id

    @property
    def scaling_resource_type(self):
        """Gets the scaling_resource_type of this ListAllScalingV2PoliciesRequest.


        :return: The scaling_resource_type of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_resource_type

    @scaling_resource_type.setter
    def scaling_resource_type(self, scaling_resource_type):
        """Sets the scaling_resource_type of this ListAllScalingV2PoliciesRequest.


        :param scaling_resource_type: The scaling_resource_type of this ListAllScalingV2PoliciesRequest.
        :type: str
        """
        self._scaling_resource_type = scaling_resource_type

    @property
    def scaling_policy_name(self):
        """Gets the scaling_policy_name of this ListAllScalingV2PoliciesRequest.


        :return: The scaling_policy_name of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_policy_name

    @scaling_policy_name.setter
    def scaling_policy_name(self, scaling_policy_name):
        """Sets the scaling_policy_name of this ListAllScalingV2PoliciesRequest.


        :param scaling_policy_name: The scaling_policy_name of this ListAllScalingV2PoliciesRequest.
        :type: str
        """
        self._scaling_policy_name = scaling_policy_name

    @property
    def scaling_policy_type(self):
        """Gets the scaling_policy_type of this ListAllScalingV2PoliciesRequest.


        :return: The scaling_policy_type of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_policy_type

    @scaling_policy_type.setter
    def scaling_policy_type(self, scaling_policy_type):
        """Sets the scaling_policy_type of this ListAllScalingV2PoliciesRequest.


        :param scaling_policy_type: The scaling_policy_type of this ListAllScalingV2PoliciesRequest.
        :type: str
        """
        self._scaling_policy_type = scaling_policy_type

    @property
    def scaling_policy_id(self):
        """Gets the scaling_policy_id of this ListAllScalingV2PoliciesRequest.


        :return: The scaling_policy_id of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        """Sets the scaling_policy_id of this ListAllScalingV2PoliciesRequest.


        :param scaling_policy_id: The scaling_policy_id of this ListAllScalingV2PoliciesRequest.
        :type: str
        """
        self._scaling_policy_id = scaling_policy_id

    @property
    def start_number(self):
        """Gets the start_number of this ListAllScalingV2PoliciesRequest.


        :return: The start_number of this ListAllScalingV2PoliciesRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListAllScalingV2PoliciesRequest.


        :param start_number: The start_number of this ListAllScalingV2PoliciesRequest.
        :type: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListAllScalingV2PoliciesRequest.


        :return: The limit of this ListAllScalingV2PoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAllScalingV2PoliciesRequest.


        :param limit: The limit of this ListAllScalingV2PoliciesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def sort_by(self):
        """Gets the sort_by of this ListAllScalingV2PoliciesRequest.


        :return: The sort_by of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListAllScalingV2PoliciesRequest.


        :param sort_by: The sort_by of this ListAllScalingV2PoliciesRequest.
        :type: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        """Gets the order of this ListAllScalingV2PoliciesRequest.


        :return: The order of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListAllScalingV2PoliciesRequest.


        :param order: The order of this ListAllScalingV2PoliciesRequest.
        :type: str
        """
        self._order = order

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAllScalingV2PoliciesRequest.


        :return: The enterprise_project_id of this ListAllScalingV2PoliciesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAllScalingV2PoliciesRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListAllScalingV2PoliciesRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListAllScalingV2PoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

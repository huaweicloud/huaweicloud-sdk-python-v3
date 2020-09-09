# coding: utf-8

import pprint
import re

import six





class ListInstancesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'name': 'str',
        'instance_id': 'str',
        'status': 'str',
        'include_failure': 'str',
        'exact_match_name': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'name': 'name',
        'instance_id': 'instance_id',
        'status': 'status',
        'include_failure': 'include_failure',
        'exact_match_name': 'exact_match_name',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, engine=None, name=None, instance_id=None, status=None, include_failure=None, exact_match_name=None, enterprise_project_id=None):
        """ListInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._engine = None
        self._name = None
        self._instance_id = None
        self._status = None
        self._include_failure = None
        self._exact_match_name = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.engine = engine
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if include_failure is not None:
            self.include_failure = include_failure
        if exact_match_name is not None:
            self.exact_match_name = exact_match_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def engine(self):
        """Gets the engine of this ListInstancesRequest.


        :return: The engine of this ListInstancesRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ListInstancesRequest.


        :param engine: The engine of this ListInstancesRequest.
        :type: str
        """
        self._engine = engine

    @property
    def name(self):
        """Gets the name of this ListInstancesRequest.


        :return: The name of this ListInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesRequest.


        :param name: The name of this ListInstancesRequest.
        :type: str
        """
        self._name = name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListInstancesRequest.


        :return: The instance_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListInstancesRequest.


        :param instance_id: The instance_id of this ListInstancesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        """Gets the status of this ListInstancesRequest.


        :return: The status of this ListInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesRequest.


        :param status: The status of this ListInstancesRequest.
        :type: str
        """
        self._status = status

    @property
    def include_failure(self):
        """Gets the include_failure of this ListInstancesRequest.


        :return: The include_failure of this ListInstancesRequest.
        :rtype: str
        """
        return self._include_failure

    @include_failure.setter
    def include_failure(self, include_failure):
        """Sets the include_failure of this ListInstancesRequest.


        :param include_failure: The include_failure of this ListInstancesRequest.
        :type: str
        """
        self._include_failure = include_failure

    @property
    def exact_match_name(self):
        """Gets the exact_match_name of this ListInstancesRequest.


        :return: The exact_match_name of this ListInstancesRequest.
        :rtype: str
        """
        return self._exact_match_name

    @exact_match_name.setter
    def exact_match_name(self, exact_match_name):
        """Sets the exact_match_name of this ListInstancesRequest.


        :param exact_match_name: The exact_match_name of this ListInstancesRequest.
        :type: str
        """
        self._exact_match_name = exact_match_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListInstancesRequest.


        :return: The enterprise_project_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListInstancesRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListInstancesRequest.
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
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

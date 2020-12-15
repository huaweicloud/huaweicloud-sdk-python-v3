# coding: utf-8

import pprint
import re

import six





class ListDependenciesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dependency_type': 'str',
        'runtime': 'str',
        'name': 'str',
        'marker': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'dependency_type': 'dependency_type',
        'runtime': 'runtime',
        'name': 'name',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, dependency_type=None, runtime=None, name=None, marker=None, limit=None):
        """ListDependenciesRequest - a model defined in huaweicloud sdk"""
        
        

        self._dependency_type = None
        self._runtime = None
        self._name = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if dependency_type is not None:
            self.dependency_type = dependency_type
        if runtime is not None:
            self.runtime = runtime
        if name is not None:
            self.name = name
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def dependency_type(self):
        """Gets the dependency_type of this ListDependenciesRequest.


        :return: The dependency_type of this ListDependenciesRequest.
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        """Sets the dependency_type of this ListDependenciesRequest.


        :param dependency_type: The dependency_type of this ListDependenciesRequest.
        :type: str
        """
        self._dependency_type = dependency_type

    @property
    def runtime(self):
        """Gets the runtime of this ListDependenciesRequest.


        :return: The runtime of this ListDependenciesRequest.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ListDependenciesRequest.


        :param runtime: The runtime of this ListDependenciesRequest.
        :type: str
        """
        self._runtime = runtime

    @property
    def name(self):
        """Gets the name of this ListDependenciesRequest.


        :return: The name of this ListDependenciesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDependenciesRequest.


        :param name: The name of this ListDependenciesRequest.
        :type: str
        """
        self._name = name

    @property
    def marker(self):
        """Gets the marker of this ListDependenciesRequest.


        :return: The marker of this ListDependenciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListDependenciesRequest.


        :param marker: The marker of this ListDependenciesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListDependenciesRequest.


        :return: The limit of this ListDependenciesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDependenciesRequest.


        :param limit: The limit of this ListDependenciesRequest.
        :type: str
        """
        self._limit = limit

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
        if not isinstance(other, ListDependenciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

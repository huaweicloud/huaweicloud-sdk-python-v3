# coding: utf-8

import pprint
import re

import six





class ListRetentionHistoriesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, namespace=None, repository=None, offset=None, limit=None):
        """ListRetentionHistoriesRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._repository = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def namespace(self):
        """Gets the namespace of this ListRetentionHistoriesRequest.


        :return: The namespace of this ListRetentionHistoriesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListRetentionHistoriesRequest.


        :param namespace: The namespace of this ListRetentionHistoriesRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this ListRetentionHistoriesRequest.


        :return: The repository of this ListRetentionHistoriesRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ListRetentionHistoriesRequest.


        :param repository: The repository of this ListRetentionHistoriesRequest.
        :type: str
        """
        self._repository = repository

    @property
    def offset(self):
        """Gets the offset of this ListRetentionHistoriesRequest.


        :return: The offset of this ListRetentionHistoriesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRetentionHistoriesRequest.


        :param offset: The offset of this ListRetentionHistoriesRequest.
        :type: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRetentionHistoriesRequest.


        :return: The limit of this ListRetentionHistoriesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRetentionHistoriesRequest.


        :param limit: The limit of this ListRetentionHistoriesRequest.
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
        if not isinstance(other, ListRetentionHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

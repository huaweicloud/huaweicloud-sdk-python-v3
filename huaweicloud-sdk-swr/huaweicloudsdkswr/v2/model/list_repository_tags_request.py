# coding: utf-8

import pprint
import re

import six





class ListRepositoryTagsRequest:


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
        'limit': 'str',
        'order_column': 'str',
        'order_type': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'offset': 'offset',
        'limit': 'limit',
        'order_column': 'order_column',
        'order_type': 'order_type',
        'tag': 'tag'
    }

    def __init__(self, namespace=None, repository=None, offset=None, limit=None, order_column=None, order_type=None, tag=None):
        """ListRepositoryTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._repository = None
        self._offset = None
        self._limit = None
        self._order_column = None
        self._order_type = None
        self._tag = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_column is not None:
            self.order_column = order_column
        if order_type is not None:
            self.order_type = order_type
        if tag is not None:
            self.tag = tag

    @property
    def namespace(self):
        """Gets the namespace of this ListRepositoryTagsRequest.


        :return: The namespace of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListRepositoryTagsRequest.


        :param namespace: The namespace of this ListRepositoryTagsRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this ListRepositoryTagsRequest.


        :return: The repository of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ListRepositoryTagsRequest.


        :param repository: The repository of this ListRepositoryTagsRequest.
        :type: str
        """
        self._repository = repository

    @property
    def offset(self):
        """Gets the offset of this ListRepositoryTagsRequest.


        :return: The offset of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRepositoryTagsRequest.


        :param offset: The offset of this ListRepositoryTagsRequest.
        :type: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRepositoryTagsRequest.


        :return: The limit of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRepositoryTagsRequest.


        :param limit: The limit of this ListRepositoryTagsRequest.
        :type: str
        """
        self._limit = limit

    @property
    def order_column(self):
        """Gets the order_column of this ListRepositoryTagsRequest.


        :return: The order_column of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._order_column

    @order_column.setter
    def order_column(self, order_column):
        """Sets the order_column of this ListRepositoryTagsRequest.


        :param order_column: The order_column of this ListRepositoryTagsRequest.
        :type: str
        """
        self._order_column = order_column

    @property
    def order_type(self):
        """Gets the order_type of this ListRepositoryTagsRequest.


        :return: The order_type of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this ListRepositoryTagsRequest.


        :param order_type: The order_type of this ListRepositoryTagsRequest.
        :type: str
        """
        self._order_type = order_type

    @property
    def tag(self):
        """Gets the tag of this ListRepositoryTagsRequest.


        :return: The tag of this ListRepositoryTagsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListRepositoryTagsRequest.


        :param tag: The tag of this ListRepositoryTagsRequest.
        :type: str
        """
        self._tag = tag

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
        if not isinstance(other, ListRepositoryTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

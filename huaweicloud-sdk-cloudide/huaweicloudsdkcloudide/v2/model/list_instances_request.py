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
        'limit': 'int',
        'offset': 'int',
        'is_temporary': 'bool',
        'label': 'str',
        'search': 'str',
        'sort_dir': 'str',
        'sort_key': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'is_temporary': 'is_temporary',
        'label': 'label',
        'search': 'search',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key'
    }

    def __init__(self, limit=30, offset=0, is_temporary=None, label=None, search=None, sort_dir='desc', sort_key='created_time'):
        """ListInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._offset = None
        self._is_temporary = None
        self._label = None
        self._search = None
        self._sort_dir = None
        self._sort_key = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if is_temporary is not None:
            self.is_temporary = is_temporary
        if label is not None:
            self.label = label
        if search is not None:
            self.search = search
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key

    @property
    def limit(self):
        """Gets the limit of this ListInstancesRequest.


        :return: The limit of this ListInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstancesRequest.


        :param limit: The limit of this ListInstancesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListInstancesRequest.


        :return: The offset of this ListInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstancesRequest.


        :param offset: The offset of this ListInstancesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def is_temporary(self):
        """Gets the is_temporary of this ListInstancesRequest.


        :return: The is_temporary of this ListInstancesRequest.
        :rtype: bool
        """
        return self._is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary):
        """Sets the is_temporary of this ListInstancesRequest.


        :param is_temporary: The is_temporary of this ListInstancesRequest.
        :type: bool
        """
        self._is_temporary = is_temporary

    @property
    def label(self):
        """Gets the label of this ListInstancesRequest.


        :return: The label of this ListInstancesRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ListInstancesRequest.


        :param label: The label of this ListInstancesRequest.
        :type: str
        """
        self._label = label

    @property
    def search(self):
        """Gets the search of this ListInstancesRequest.


        :return: The search of this ListInstancesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListInstancesRequest.


        :param search: The search of this ListInstancesRequest.
        :type: str
        """
        self._search = search

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListInstancesRequest.


        :return: The sort_dir of this ListInstancesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListInstancesRequest.


        :param sort_dir: The sort_dir of this ListInstancesRequest.
        :type: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListInstancesRequest.


        :return: The sort_key of this ListInstancesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListInstancesRequest.


        :param sort_key: The sort_key of this ListInstancesRequest.
        :type: str
        """
        self._sort_key = sort_key

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

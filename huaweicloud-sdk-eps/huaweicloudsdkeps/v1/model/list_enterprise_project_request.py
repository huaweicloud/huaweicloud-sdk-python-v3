# coding: utf-8

import pprint
import re

import six





class ListEnterpriseProjectRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'sort_dir': 'str',
        'sort_key': 'str',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'status': 'status'
    }

    def __init__(self, id=None, limit=None, name=None, offset=None, sort_dir=None, sort_key=None, status=None):
        """ListEnterpriseProjectRequest - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._limit = None
        self._name = None
        self._offset = None
        self._sort_dir = None
        self._sort_key = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ListEnterpriseProjectRequest.


        :return: The id of this ListEnterpriseProjectRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEnterpriseProjectRequest.


        :param id: The id of this ListEnterpriseProjectRequest.
        :type: str
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListEnterpriseProjectRequest.


        :return: The limit of this ListEnterpriseProjectRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnterpriseProjectRequest.


        :param limit: The limit of this ListEnterpriseProjectRequest.
        :type: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListEnterpriseProjectRequest.


        :return: The name of this ListEnterpriseProjectRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEnterpriseProjectRequest.


        :param name: The name of this ListEnterpriseProjectRequest.
        :type: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListEnterpriseProjectRequest.


        :return: The offset of this ListEnterpriseProjectRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnterpriseProjectRequest.


        :param offset: The offset of this ListEnterpriseProjectRequest.
        :type: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListEnterpriseProjectRequest.


        :return: The sort_dir of this ListEnterpriseProjectRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListEnterpriseProjectRequest.


        :param sort_dir: The sort_dir of this ListEnterpriseProjectRequest.
        :type: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListEnterpriseProjectRequest.


        :return: The sort_key of this ListEnterpriseProjectRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListEnterpriseProjectRequest.


        :param sort_key: The sort_key of this ListEnterpriseProjectRequest.
        :type: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        """Gets the status of this ListEnterpriseProjectRequest.


        :return: The status of this ListEnterpriseProjectRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEnterpriseProjectRequest.


        :param status: The status of this ListEnterpriseProjectRequest.
        :type: int
        """
        self._status = status

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
        if not isinstance(other, ListEnterpriseProjectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

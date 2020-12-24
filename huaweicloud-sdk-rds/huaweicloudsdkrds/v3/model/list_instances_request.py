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
        'x_language': 'str',
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'datastore_type': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'tags': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'datastore_type': 'datastore_type',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'offset': 'offset',
        'limit': 'limit',
        'tags': 'tags'
    }

    def __init__(self, x_language=None, id=None, name=None, type=None, datastore_type=None, vpc_id=None, subnet_id=None, offset=None, limit=None, tags=None):
        """ListInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._id = None
        self._name = None
        self._type = None
        self._datastore_type = None
        self._vpc_id = None
        self._subnet_id = None
        self._offset = None
        self._limit = None
        self._tags = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if tags is not None:
            self.tags = tags

    @property
    def x_language(self):
        """Gets the x_language of this ListInstancesRequest.


        :return: The x_language of this ListInstancesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListInstancesRequest.


        :param x_language: The x_language of this ListInstancesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def id(self):
        """Gets the id of this ListInstancesRequest.


        :return: The id of this ListInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInstancesRequest.


        :param id: The id of this ListInstancesRequest.
        :type: str
        """
        self._id = id

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
    def type(self):
        """Gets the type of this ListInstancesRequest.


        :return: The type of this ListInstancesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListInstancesRequest.


        :param type: The type of this ListInstancesRequest.
        :type: str
        """
        self._type = type

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ListInstancesRequest.


        :return: The datastore_type of this ListInstancesRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ListInstancesRequest.


        :param datastore_type: The datastore_type of this ListInstancesRequest.
        :type: str
        """
        self._datastore_type = datastore_type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListInstancesRequest.


        :return: The vpc_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListInstancesRequest.


        :param vpc_id: The vpc_id of this ListInstancesRequest.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListInstancesRequest.


        :return: The subnet_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListInstancesRequest.


        :param subnet_id: The subnet_id of this ListInstancesRequest.
        :type: str
        """
        self._subnet_id = subnet_id

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
    def tags(self):
        """Gets the tags of this ListInstancesRequest.


        :return: The tags of this ListInstancesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListInstancesRequest.


        :param tags: The tags of this ListInstancesRequest.
        :type: str
        """
        self._tags = tags

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

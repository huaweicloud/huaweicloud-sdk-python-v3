# coding: utf-8

import pprint
import re

import six





class ListSlowLogsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'node_id': 'str',
        'type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'node_id': 'node_id',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, start_date=None, end_date=None, node_id=None, type=None, offset=None, limit=None):
        """ListSlowLogsRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._start_date = None
        self._end_date = None
        self._node_id = None
        self._type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_date = start_date
        self.end_date = end_date
        if node_id is not None:
            self.node_id = node_id
        if type is not None:
            self.type = type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSlowLogsRequest.


        :return: The instance_id of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSlowLogsRequest.


        :param instance_id: The instance_id of this ListSlowLogsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def start_date(self):
        """Gets the start_date of this ListSlowLogsRequest.


        :return: The start_date of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ListSlowLogsRequest.


        :param start_date: The start_date of this ListSlowLogsRequest.
        :type: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ListSlowLogsRequest.


        :return: The end_date of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ListSlowLogsRequest.


        :param end_date: The end_date of this ListSlowLogsRequest.
        :type: str
        """
        self._end_date = end_date

    @property
    def node_id(self):
        """Gets the node_id of this ListSlowLogsRequest.


        :return: The node_id of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ListSlowLogsRequest.


        :param node_id: The node_id of this ListSlowLogsRequest.
        :type: str
        """
        self._node_id = node_id

    @property
    def type(self):
        """Gets the type of this ListSlowLogsRequest.


        :return: The type of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListSlowLogsRequest.


        :param type: The type of this ListSlowLogsRequest.
        :type: str
        """
        self._type = type

    @property
    def offset(self):
        """Gets the offset of this ListSlowLogsRequest.


        :return: The offset of this ListSlowLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSlowLogsRequest.


        :param offset: The offset of this ListSlowLogsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSlowLogsRequest.


        :return: The limit of this ListSlowLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSlowLogsRequest.


        :param limit: The limit of this ListSlowLogsRequest.
        :type: int
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
        if not isinstance(other, ListSlowLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

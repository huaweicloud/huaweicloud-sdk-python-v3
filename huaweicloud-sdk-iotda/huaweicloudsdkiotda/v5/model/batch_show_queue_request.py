# coding: utf-8

import pprint
import re

import six





class BatchShowQueueRequest:


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
        'queue_name': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'queue_name': 'queue_name',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, queue_name=None, limit=10, marker='ffffffffffffffffffffffff', offset=0):
        """BatchShowQueueRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._queue_name = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if queue_name is not None:
            self.queue_name = queue_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this BatchShowQueueRequest.


        :return: The instance_id of this BatchShowQueueRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BatchShowQueueRequest.


        :param instance_id: The instance_id of this BatchShowQueueRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def queue_name(self):
        """Gets the queue_name of this BatchShowQueueRequest.


        :return: The queue_name of this BatchShowQueueRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this BatchShowQueueRequest.


        :param queue_name: The queue_name of this BatchShowQueueRequest.
        :type: str
        """
        self._queue_name = queue_name

    @property
    def limit(self):
        """Gets the limit of this BatchShowQueueRequest.


        :return: The limit of this BatchShowQueueRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this BatchShowQueueRequest.


        :param limit: The limit of this BatchShowQueueRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this BatchShowQueueRequest.


        :return: The marker of this BatchShowQueueRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this BatchShowQueueRequest.


        :param marker: The marker of this BatchShowQueueRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this BatchShowQueueRequest.


        :return: The offset of this BatchShowQueueRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BatchShowQueueRequest.


        :param offset: The offset of this BatchShowQueueRequest.
        :type: int
        """
        self._offset = offset

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
        if not isinstance(other, BatchShowQueueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

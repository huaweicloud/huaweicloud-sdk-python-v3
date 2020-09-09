# coding: utf-8

import pprint
import re

import six





class ShowQueueRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'queue_id': 'str',
        'include_deadletter': 'bool'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'include_deadletter': 'include_deadletter'
    }

    def __init__(self, queue_id=None, include_deadletter=None):
        """ShowQueueRequest - a model defined in huaweicloud sdk"""
        
        

        self._queue_id = None
        self._include_deadletter = None
        self.discriminator = None

        self.queue_id = queue_id
        if include_deadletter is not None:
            self.include_deadletter = include_deadletter

    @property
    def queue_id(self):
        """Gets the queue_id of this ShowQueueRequest.


        :return: The queue_id of this ShowQueueRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this ShowQueueRequest.


        :param queue_id: The queue_id of this ShowQueueRequest.
        :type: str
        """
        self._queue_id = queue_id

    @property
    def include_deadletter(self):
        """Gets the include_deadletter of this ShowQueueRequest.


        :return: The include_deadletter of this ShowQueueRequest.
        :rtype: bool
        """
        return self._include_deadletter

    @include_deadletter.setter
    def include_deadletter(self, include_deadletter):
        """Sets the include_deadletter of this ShowQueueRequest.


        :param include_deadletter: The include_deadletter of this ShowQueueRequest.
        :type: bool
        """
        self._include_deadletter = include_deadletter

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
        if not isinstance(other, ShowQueueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import pprint
import re

import six





class AmqpForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'queue_name': 'str'
    }

    attribute_map = {
        'queue_name': 'queue_name'
    }

    def __init__(self, queue_name=None):
        """AmqpForwarding - a model defined in huaweicloud sdk"""
        
        

        self._queue_name = None
        self.discriminator = None

        self.queue_name = queue_name

    @property
    def queue_name(self):
        """Gets the queue_name of this AmqpForwarding.

        用于接收满足规则条件数据的amqp queue。

        :return: The queue_name of this AmqpForwarding.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this AmqpForwarding.

        用于接收满足规则条件数据的amqp queue。

        :param queue_name: The queue_name of this AmqpForwarding.
        :type: str
        """
        self._queue_name = queue_name

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
        if not isinstance(other, AmqpForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

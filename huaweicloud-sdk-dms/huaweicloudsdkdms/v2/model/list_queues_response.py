# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListQueuesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'queues': 'list[ListQueuesRespQueues]'
    }

    attribute_map = {
        'total': 'total',
        'queues': 'queues'
    }

    def __init__(self, total=None, queues=None):
        """ListQueuesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total = None
        self._queues = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if queues is not None:
            self.queues = queues

    @property
    def total(self):
        """Gets the total of this ListQueuesResponse.

        该租户的所有队列总数。

        :return: The total of this ListQueuesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListQueuesResponse.

        该租户的所有队列总数。

        :param total: The total of this ListQueuesResponse.
        :type: int
        """
        self._total = total

    @property
    def queues(self):
        """Gets the queues of this ListQueuesResponse.

        该租户的所有队列数组。

        :return: The queues of this ListQueuesResponse.
        :rtype: list[ListQueuesRespQueues]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this ListQueuesResponse.

        该租户的所有队列数组。

        :param queues: The queues of this ListQueuesResponse.
        :type: list[ListQueuesRespQueues]
        """
        self._queues = queues

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
        if not isinstance(other, ListQueuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSpecifiedConsumerGroupRequest:

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
        'group_id': 'str'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'group_id': 'group_id'
    }

    def __init__(self, queue_id=None, group_id=None):
        """DeleteSpecifiedConsumerGroupRequest

        The model defined in huaweicloud sdk

        :param queue_id: 队列ID
        :type queue_id: str
        :param group_id: 待删除的消费组ID
        :type group_id: str
        """
        
        

        self._queue_id = None
        self._group_id = None
        self.discriminator = None

        self.queue_id = queue_id
        self.group_id = group_id

    @property
    def queue_id(self):
        """Gets the queue_id of this DeleteSpecifiedConsumerGroupRequest.

        队列ID

        :return: The queue_id of this DeleteSpecifiedConsumerGroupRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this DeleteSpecifiedConsumerGroupRequest.

        队列ID

        :param queue_id: The queue_id of this DeleteSpecifiedConsumerGroupRequest.
        :type queue_id: str
        """
        self._queue_id = queue_id

    @property
    def group_id(self):
        """Gets the group_id of this DeleteSpecifiedConsumerGroupRequest.

        待删除的消费组ID

        :return: The group_id of this DeleteSpecifiedConsumerGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DeleteSpecifiedConsumerGroupRequest.

        待删除的消费组ID

        :param group_id: The group_id of this DeleteSpecifiedConsumerGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteSpecifiedConsumerGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

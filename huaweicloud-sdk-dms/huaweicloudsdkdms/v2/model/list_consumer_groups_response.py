# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListConsumerGroupsResponse(SdkResponse):


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
        'queue_name': 'str',
        'groups': 'list[ListQueueGroupsRespGroups]',
        'redrive_policy': 'str'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'queue_name': 'queue_name',
        'groups': 'groups',
        'redrive_policy': 'redrive_policy'
    }

    def __init__(self, queue_id=None, queue_name=None, groups=None, redrive_policy=None):
        """ListConsumerGroupsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._queue_id = None
        self._queue_name = None
        self._groups = None
        self._redrive_policy = None
        self.discriminator = None

        if queue_id is not None:
            self.queue_id = queue_id
        if queue_name is not None:
            self.queue_name = queue_name
        if groups is not None:
            self.groups = groups
        if redrive_policy is not None:
            self.redrive_policy = redrive_policy

    @property
    def queue_id(self):
        """Gets the queue_id of this ListConsumerGroupsResponse.

        队列ID。

        :return: The queue_id of this ListConsumerGroupsResponse.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this ListConsumerGroupsResponse.

        队列ID。

        :param queue_id: The queue_id of this ListConsumerGroupsResponse.
        :type: str
        """
        self._queue_id = queue_id

    @property
    def queue_name(self):
        """Gets the queue_name of this ListConsumerGroupsResponse.

        队列的名称。

        :return: The queue_name of this ListConsumerGroupsResponse.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ListConsumerGroupsResponse.

        队列的名称。

        :param queue_name: The queue_name of this ListConsumerGroupsResponse.
        :type: str
        """
        self._queue_name = queue_name

    @property
    def groups(self):
        """Gets the groups of this ListConsumerGroupsResponse.

        消费组列表。

        :return: The groups of this ListConsumerGroupsResponse.
        :rtype: list[ListQueueGroupsRespGroups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ListConsumerGroupsResponse.

        消费组列表。

        :param groups: The groups of this ListConsumerGroupsResponse.
        :type: list[ListQueueGroupsRespGroups]
        """
        self._groups = groups

    @property
    def redrive_policy(self):
        """Gets the redrive_policy of this ListConsumerGroupsResponse.

        该队列是否开启死信消息。仅当include_deadletter为true时，才有该响应参数。 - enable：表示开启。 - disable：表示不开启。

        :return: The redrive_policy of this ListConsumerGroupsResponse.
        :rtype: str
        """
        return self._redrive_policy

    @redrive_policy.setter
    def redrive_policy(self, redrive_policy):
        """Sets the redrive_policy of this ListConsumerGroupsResponse.

        该队列是否开启死信消息。仅当include_deadletter为true时，才有该响应参数。 - enable：表示开启。 - disable：表示不开启。

        :param redrive_policy: The redrive_policy of this ListConsumerGroupsResponse.
        :type: str
        """
        self._redrive_policy = redrive_policy

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
        if not isinstance(other, ListConsumerGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

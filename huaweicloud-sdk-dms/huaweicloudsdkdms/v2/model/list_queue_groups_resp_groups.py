# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueueGroupsRespGroups:

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
        'name': 'str',
        'produced_messages': 'int',
        'consumed_messages': 'int',
        'available_messages': 'int',
        'produced_deadletters': 'int',
        'available_deadletters': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'produced_messages': 'produced_messages',
        'consumed_messages': 'consumed_messages',
        'available_messages': 'available_messages',
        'produced_deadletters': 'produced_deadletters',
        'available_deadletters': 'available_deadletters'
    }

    def __init__(self, id=None, name=None, produced_messages=None, consumed_messages=None, available_messages=None, produced_deadletters=None, available_deadletters=None):
        """ListQueueGroupsRespGroups

        The model defined in huaweicloud sdk

        :param id: 队列的名称。
        :type id: str
        :param name: 队列的名称。
        :type name: str
        :param produced_messages: 队列的消息总数，不包含过期删除的消息数。
        :type produced_messages: int
        :param consumed_messages: 已正常消费的消息总数。
        :type consumed_messages: int
        :param available_messages: 该消费组可以消费的普通消息数。
        :type available_messages: int
        :param produced_deadletters: 该消费组产生的死信息消息总数。仅当include_deadletter为true时，才有该响应参数。
        :type produced_deadletters: int
        :param available_deadletters: 该消费组未消费的死信消息数。仅当include_deadletter为true时，才有该响应参数。
        :type available_deadletters: int
        """
        
        

        self._id = None
        self._name = None
        self._produced_messages = None
        self._consumed_messages = None
        self._available_messages = None
        self._produced_deadletters = None
        self._available_deadletters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if produced_messages is not None:
            self.produced_messages = produced_messages
        if consumed_messages is not None:
            self.consumed_messages = consumed_messages
        if available_messages is not None:
            self.available_messages = available_messages
        if produced_deadletters is not None:
            self.produced_deadletters = produced_deadletters
        if available_deadletters is not None:
            self.available_deadletters = available_deadletters

    @property
    def id(self):
        """Gets the id of this ListQueueGroupsRespGroups.

        队列的名称。

        :return: The id of this ListQueueGroupsRespGroups.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListQueueGroupsRespGroups.

        队列的名称。

        :param id: The id of this ListQueueGroupsRespGroups.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListQueueGroupsRespGroups.

        队列的名称。

        :return: The name of this ListQueueGroupsRespGroups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListQueueGroupsRespGroups.

        队列的名称。

        :param name: The name of this ListQueueGroupsRespGroups.
        :type name: str
        """
        self._name = name

    @property
    def produced_messages(self):
        """Gets the produced_messages of this ListQueueGroupsRespGroups.

        队列的消息总数，不包含过期删除的消息数。

        :return: The produced_messages of this ListQueueGroupsRespGroups.
        :rtype: int
        """
        return self._produced_messages

    @produced_messages.setter
    def produced_messages(self, produced_messages):
        """Sets the produced_messages of this ListQueueGroupsRespGroups.

        队列的消息总数，不包含过期删除的消息数。

        :param produced_messages: The produced_messages of this ListQueueGroupsRespGroups.
        :type produced_messages: int
        """
        self._produced_messages = produced_messages

    @property
    def consumed_messages(self):
        """Gets the consumed_messages of this ListQueueGroupsRespGroups.

        已正常消费的消息总数。

        :return: The consumed_messages of this ListQueueGroupsRespGroups.
        :rtype: int
        """
        return self._consumed_messages

    @consumed_messages.setter
    def consumed_messages(self, consumed_messages):
        """Sets the consumed_messages of this ListQueueGroupsRespGroups.

        已正常消费的消息总数。

        :param consumed_messages: The consumed_messages of this ListQueueGroupsRespGroups.
        :type consumed_messages: int
        """
        self._consumed_messages = consumed_messages

    @property
    def available_messages(self):
        """Gets the available_messages of this ListQueueGroupsRespGroups.

        该消费组可以消费的普通消息数。

        :return: The available_messages of this ListQueueGroupsRespGroups.
        :rtype: int
        """
        return self._available_messages

    @available_messages.setter
    def available_messages(self, available_messages):
        """Sets the available_messages of this ListQueueGroupsRespGroups.

        该消费组可以消费的普通消息数。

        :param available_messages: The available_messages of this ListQueueGroupsRespGroups.
        :type available_messages: int
        """
        self._available_messages = available_messages

    @property
    def produced_deadletters(self):
        """Gets the produced_deadletters of this ListQueueGroupsRespGroups.

        该消费组产生的死信息消息总数。仅当include_deadletter为true时，才有该响应参数。

        :return: The produced_deadletters of this ListQueueGroupsRespGroups.
        :rtype: int
        """
        return self._produced_deadletters

    @produced_deadletters.setter
    def produced_deadletters(self, produced_deadletters):
        """Sets the produced_deadletters of this ListQueueGroupsRespGroups.

        该消费组产生的死信息消息总数。仅当include_deadletter为true时，才有该响应参数。

        :param produced_deadletters: The produced_deadletters of this ListQueueGroupsRespGroups.
        :type produced_deadletters: int
        """
        self._produced_deadletters = produced_deadletters

    @property
    def available_deadletters(self):
        """Gets the available_deadletters of this ListQueueGroupsRespGroups.

        该消费组未消费的死信消息数。仅当include_deadletter为true时，才有该响应参数。

        :return: The available_deadletters of this ListQueueGroupsRespGroups.
        :rtype: int
        """
        return self._available_deadletters

    @available_deadletters.setter
    def available_deadletters(self, available_deadletters):
        """Sets the available_deadletters of this ListQueueGroupsRespGroups.

        该消费组未消费的死信消息数。仅当include_deadletter为true时，才有该响应参数。

        :param available_deadletters: The available_deadletters of this ListQueueGroupsRespGroups.
        :type available_deadletters: int
        """
        self._available_deadletters = available_deadletters

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
        if not isinstance(other, ListQueueGroupsRespGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

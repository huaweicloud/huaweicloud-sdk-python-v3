# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """ShowQueueRequest

        The model defined in huaweicloud sdk

        :param queue_id: 待查询的队列ID
        :type queue_id: str
        :param include_deadletter: 是否包含死信信息。  支持的值如下：  - true：包含死信消息。 - false：不包含死信消息。  默认值为：false。  Kafka队列没有死信功能，该参数对于Kafka队列无效。
        :type include_deadletter: bool
        """
        
        

        self._queue_id = None
        self._include_deadletter = None
        self.discriminator = None

        self.queue_id = queue_id
        if include_deadletter is not None:
            self.include_deadletter = include_deadletter

    @property
    def queue_id(self):
        """Gets the queue_id of this ShowQueueRequest.

        待查询的队列ID

        :return: The queue_id of this ShowQueueRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this ShowQueueRequest.

        待查询的队列ID

        :param queue_id: The queue_id of this ShowQueueRequest.
        :type queue_id: str
        """
        self._queue_id = queue_id

    @property
    def include_deadletter(self):
        """Gets the include_deadletter of this ShowQueueRequest.

        是否包含死信信息。  支持的值如下：  - true：包含死信消息。 - false：不包含死信消息。  默认值为：false。  Kafka队列没有死信功能，该参数对于Kafka队列无效。

        :return: The include_deadletter of this ShowQueueRequest.
        :rtype: bool
        """
        return self._include_deadletter

    @include_deadletter.setter
    def include_deadletter(self, include_deadletter):
        """Sets the include_deadletter of this ShowQueueRequest.

        是否包含死信信息。  支持的值如下：  - true：包含死信消息。 - false：不包含死信消息。  默认值为：false。  Kafka队列没有死信功能，该参数对于Kafka队列无效。

        :param include_deadletter: The include_deadletter of this ShowQueueRequest.
        :type include_deadletter: bool
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
        if not isinstance(other, ShowQueueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

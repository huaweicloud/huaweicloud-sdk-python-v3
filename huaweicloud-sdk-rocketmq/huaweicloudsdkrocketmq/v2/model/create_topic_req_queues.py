# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTopicReqQueues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'broker': 'str',
        'queue_num': 'float'
    }

    attribute_map = {
        'broker': 'broker',
        'queue_num': 'queue_num'
    }

    def __init__(self, broker=None, queue_num=None):
        r"""CreateTopicReqQueues

        The model defined in huaweicloud sdk

        :param broker: 关联的代理。
        :type broker: str
        :param queue_num: 队列数，范围1~50。
        :type queue_num: float
        """
        
        

        self._broker = None
        self._queue_num = None
        self.discriminator = None

        if broker is not None:
            self.broker = broker
        if queue_num is not None:
            self.queue_num = queue_num

    @property
    def broker(self):
        r"""Gets the broker of this CreateTopicReqQueues.

        关联的代理。

        :return: The broker of this CreateTopicReqQueues.
        :rtype: str
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        r"""Sets the broker of this CreateTopicReqQueues.

        关联的代理。

        :param broker: The broker of this CreateTopicReqQueues.
        :type broker: str
        """
        self._broker = broker

    @property
    def queue_num(self):
        r"""Gets the queue_num of this CreateTopicReqQueues.

        队列数，范围1~50。

        :return: The queue_num of this CreateTopicReqQueues.
        :rtype: float
        """
        return self._queue_num

    @queue_num.setter
    def queue_num(self, queue_num):
        r"""Sets the queue_num of this CreateTopicReqQueues.

        队列数，范围1~50。

        :param queue_num: The queue_num of this CreateTopicReqQueues.
        :type queue_num: float
        """
        self._queue_num = queue_num

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
        if not isinstance(other, CreateTopicReqQueues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Result:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average_msg_bytes': 'float',
        'subscribe_msgs': 'int'
    }

    attribute_map = {
        'average_msg_bytes': 'average_msg_bytes',
        'subscribe_msgs': 'subscribe_msgs'
    }

    def __init__(self, average_msg_bytes=None, subscribe_msgs=None):
        r"""Result

        The model defined in huaweicloud sdk

        :param average_msg_bytes: 平均消费大小
        :type average_msg_bytes: float
        :param subscribe_msgs: 消费条数
        :type subscribe_msgs: int
        """
        
        

        self._average_msg_bytes = None
        self._subscribe_msgs = None
        self.discriminator = None

        self.average_msg_bytes = average_msg_bytes
        self.subscribe_msgs = subscribe_msgs

    @property
    def average_msg_bytes(self):
        r"""Gets the average_msg_bytes of this Result.

        平均消费大小

        :return: The average_msg_bytes of this Result.
        :rtype: float
        """
        return self._average_msg_bytes

    @average_msg_bytes.setter
    def average_msg_bytes(self, average_msg_bytes):
        r"""Sets the average_msg_bytes of this Result.

        平均消费大小

        :param average_msg_bytes: The average_msg_bytes of this Result.
        :type average_msg_bytes: float
        """
        self._average_msg_bytes = average_msg_bytes

    @property
    def subscribe_msgs(self):
        r"""Gets the subscribe_msgs of this Result.

        消费条数

        :return: The subscribe_msgs of this Result.
        :rtype: int
        """
        return self._subscribe_msgs

    @subscribe_msgs.setter
    def subscribe_msgs(self, subscribe_msgs):
        r"""Sets the subscribe_msgs of this Result.

        消费条数

        :param subscribe_msgs: The subscribe_msgs of this Result.
        :type subscribe_msgs: int
        """
        self._subscribe_msgs = subscribe_msgs

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

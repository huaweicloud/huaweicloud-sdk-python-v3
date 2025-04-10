# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeadletterResendReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'msg_id_list': 'list[str]'
    }

    attribute_map = {
        'topic': 'topic',
        'msg_id_list': 'msg_id_list'
    }

    def __init__(self, topic=None, msg_id_list=None):
        r"""DeadletterResendReq

        The model defined in huaweicloud sdk

        :param topic: Topic名称。
        :type topic: str
        :param msg_id_list: 消息列表。
        :type msg_id_list: list[str]
        """
        
        

        self._topic = None
        self._msg_id_list = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if msg_id_list is not None:
            self.msg_id_list = msg_id_list

    @property
    def topic(self):
        r"""Gets the topic of this DeadletterResendReq.

        Topic名称。

        :return: The topic of this DeadletterResendReq.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this DeadletterResendReq.

        Topic名称。

        :param topic: The topic of this DeadletterResendReq.
        :type topic: str
        """
        self._topic = topic

    @property
    def msg_id_list(self):
        r"""Gets the msg_id_list of this DeadletterResendReq.

        消息列表。

        :return: The msg_id_list of this DeadletterResendReq.
        :rtype: list[str]
        """
        return self._msg_id_list

    @msg_id_list.setter
    def msg_id_list(self, msg_id_list):
        r"""Sets the msg_id_list of this DeadletterResendReq.

        消息列表。

        :param msg_id_list: The msg_id_list of this DeadletterResendReq.
        :type msg_id_list: list[str]
        """
        self._msg_id_list = msg_id_list

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
        if not isinstance(other, DeadletterResendReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

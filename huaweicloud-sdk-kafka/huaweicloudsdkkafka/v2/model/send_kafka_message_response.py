# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendKafkaMessageResponse(SdkResponse):

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
        'body': 'str',
        'property_list': 'list[object]'
    }

    attribute_map = {
        'topic': 'topic',
        'body': 'body',
        'property_list': 'property_list'
    }

    def __init__(self, topic=None, body=None, property_list=None):
        r"""SendKafkaMessageResponse

        The model defined in huaweicloud sdk

        :param topic: Kafka的Topic
        :type topic: str
        :param body: 消息内容
        :type body: str
        :param property_list: Topic的分区信息等
        :type property_list: list[object]
        """
        
        super(SendKafkaMessageResponse, self).__init__()

        self._topic = None
        self._body = None
        self._property_list = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if body is not None:
            self.body = body
        if property_list is not None:
            self.property_list = property_list

    @property
    def topic(self):
        r"""Gets the topic of this SendKafkaMessageResponse.

        Kafka的Topic

        :return: The topic of this SendKafkaMessageResponse.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SendKafkaMessageResponse.

        Kafka的Topic

        :param topic: The topic of this SendKafkaMessageResponse.
        :type topic: str
        """
        self._topic = topic

    @property
    def body(self):
        r"""Gets the body of this SendKafkaMessageResponse.

        消息内容

        :return: The body of this SendKafkaMessageResponse.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SendKafkaMessageResponse.

        消息内容

        :param body: The body of this SendKafkaMessageResponse.
        :type body: str
        """
        self._body = body

    @property
    def property_list(self):
        r"""Gets the property_list of this SendKafkaMessageResponse.

        Topic的分区信息等

        :return: The property_list of this SendKafkaMessageResponse.
        :rtype: list[object]
        """
        return self._property_list

    @property_list.setter
    def property_list(self, property_list):
        r"""Sets the property_list of this SendKafkaMessageResponse.

        Topic的分区信息等

        :param property_list: The property_list of this SendKafkaMessageResponse.
        :type property_list: list[object]
        """
        self._property_list = property_list

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
        if not isinstance(other, SendKafkaMessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendMessageRep:

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
        'property_list': 'list[SendMessageProperties]'
    }

    attribute_map = {
        'topic': 'topic',
        'body': 'body',
        'property_list': 'property_list'
    }

    def __init__(self, topic=None, body=None, property_list=None):
        r"""SendMessageRep

        The model defined in huaweicloud sdk

        :param topic: **参数解释**： 主题名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type topic: str
        :param body: **参数解释**： 消息内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type body: str
        :param property_list: **参数解释**： 特性列表。
        :type property_list: list[:class:`huaweicloudsdkrocketmq.v2.SendMessageProperties`]
        """
        
        

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
        r"""Gets the topic of this SendMessageRep.

        **参数解释**： 主题名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The topic of this SendMessageRep.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SendMessageRep.

        **参数解释**： 主题名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param topic: The topic of this SendMessageRep.
        :type topic: str
        """
        self._topic = topic

    @property
    def body(self):
        r"""Gets the body of this SendMessageRep.

        **参数解释**： 消息内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The body of this SendMessageRep.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SendMessageRep.

        **参数解释**： 消息内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param body: The body of this SendMessageRep.
        :type body: str
        """
        self._body = body

    @property
    def property_list(self):
        r"""Gets the property_list of this SendMessageRep.

        **参数解释**： 特性列表。

        :return: The property_list of this SendMessageRep.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.SendMessageProperties`]
        """
        return self._property_list

    @property_list.setter
    def property_list(self, property_list):
        r"""Sets the property_list of this SendMessageRep.

        **参数解释**： 特性列表。

        :param property_list: The property_list of this SendMessageRep.
        :type property_list: list[:class:`huaweicloudsdkrocketmq.v2.SendMessageProperties`]
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
        if not isinstance(other, SendMessageRep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Subscription:

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
        'type': 'str',
        'expression': 'str'
    }

    attribute_map = {
        'topic': 'topic',
        'type': 'type',
        'expression': 'expression'
    }

    def __init__(self, topic=None, type=None, expression=None):
        """Subscription

        The model defined in huaweicloud sdk

        :param topic: 订阅的topic名称
        :type topic: str
        :param type: 订阅类型，取值如下：TAG和SQL92
        :type type: str
        :param expression: 订阅tag字符
        :type expression: str
        """
        
        

        self._topic = None
        self._type = None
        self._expression = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if type is not None:
            self.type = type
        if expression is not None:
            self.expression = expression

    @property
    def topic(self):
        """Gets the topic of this Subscription.

        订阅的topic名称

        :return: The topic of this Subscription.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this Subscription.

        订阅的topic名称

        :param topic: The topic of this Subscription.
        :type topic: str
        """
        self._topic = topic

    @property
    def type(self):
        """Gets the type of this Subscription.

        订阅类型，取值如下：TAG和SQL92

        :return: The type of this Subscription.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Subscription.

        订阅类型，取值如下：TAG和SQL92

        :param type: The type of this Subscription.
        :type type: str
        """
        self._type = type

    @property
    def expression(self):
        """Gets the expression of this Subscription.

        订阅tag字符

        :return: The expression of this Subscription.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this Subscription.

        订阅tag字符

        :param expression: The expression of this Subscription.
        :type expression: str
        """
        self._expression = expression

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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

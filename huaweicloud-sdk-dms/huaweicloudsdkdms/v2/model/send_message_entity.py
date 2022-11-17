# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendMessageEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'object',
        'attributes': 'object',
        'tags': 'object',
        'delay_time': 'object'
    }

    attribute_map = {
        'body': 'body',
        'attributes': 'attributes',
        'tags': 'tags',
        'delay_time': 'delay_time'
    }

    def __init__(self, body=None, attributes=None, tags=None, delay_time=None):
        """SendMessageEntity

        The model defined in huaweicloud sdk

        :param body: 消息正文。
        :type body: object
        :param attributes: 属性列表，包含属性名称和属性值。  同一条消息的属性名称不可重复，否则属性值将被覆盖。 
        :type attributes: object
        :param tags: 消息标签，即Label，是通过对消息增加Label来区分队列中的消息分类，DMS允许消费者按照Label对消息进行过滤，确保消费者最终只消费到他关心的消息类型。  消息标签只能包含a~z，A~Z，0-9，-，_，长度是[1，64]。  最多可添加3个标签。 
        :type tags: object
        :param delay_time: 延时消息的延时时长。  延时消息是指消息发送到DMS服务后，并不期望这条消息立即被消费，而是延迟一段时间后才能被消费。  取值范围：0~604800000  单位：毫秒  不配置该参数或者配置为0，表示无延时。  配置为浮点数时，自动取小数点前面的整数值，比如配置为6000.9，则自动取值为6000。  仅NORMAL队列和FIFO队列可以设置延时消息，Kafka队列不支持延时消息的功能，如果向Kafka队列生产延时消息，提示{\&quot;code\&quot;:10540010, \&quot;message\&quot;:\&quot;Invalid request format: kafka queue message could not have delayTime.\&quot;}。 
        :type delay_time: object
        """
        
        

        self._body = None
        self._attributes = None
        self._tags = None
        self._delay_time = None
        self.discriminator = None

        self.body = body
        if attributes is not None:
            self.attributes = attributes
        if tags is not None:
            self.tags = tags
        if delay_time is not None:
            self.delay_time = delay_time

    @property
    def body(self):
        """Gets the body of this SendMessageEntity.

        消息正文。

        :return: The body of this SendMessageEntity.
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SendMessageEntity.

        消息正文。

        :param body: The body of this SendMessageEntity.
        :type body: object
        """
        self._body = body

    @property
    def attributes(self):
        """Gets the attributes of this SendMessageEntity.

        属性列表，包含属性名称和属性值。  同一条消息的属性名称不可重复，否则属性值将被覆盖。 

        :return: The attributes of this SendMessageEntity.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this SendMessageEntity.

        属性列表，包含属性名称和属性值。  同一条消息的属性名称不可重复，否则属性值将被覆盖。 

        :param attributes: The attributes of this SendMessageEntity.
        :type attributes: object
        """
        self._attributes = attributes

    @property
    def tags(self):
        """Gets the tags of this SendMessageEntity.

        消息标签，即Label，是通过对消息增加Label来区分队列中的消息分类，DMS允许消费者按照Label对消息进行过滤，确保消费者最终只消费到他关心的消息类型。  消息标签只能包含a~z，A~Z，0-9，-，_，长度是[1，64]。  最多可添加3个标签。 

        :return: The tags of this SendMessageEntity.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SendMessageEntity.

        消息标签，即Label，是通过对消息增加Label来区分队列中的消息分类，DMS允许消费者按照Label对消息进行过滤，确保消费者最终只消费到他关心的消息类型。  消息标签只能包含a~z，A~Z，0-9，-，_，长度是[1，64]。  最多可添加3个标签。 

        :param tags: The tags of this SendMessageEntity.
        :type tags: object
        """
        self._tags = tags

    @property
    def delay_time(self):
        """Gets the delay_time of this SendMessageEntity.

        延时消息的延时时长。  延时消息是指消息发送到DMS服务后，并不期望这条消息立即被消费，而是延迟一段时间后才能被消费。  取值范围：0~604800000  单位：毫秒  不配置该参数或者配置为0，表示无延时。  配置为浮点数时，自动取小数点前面的整数值，比如配置为6000.9，则自动取值为6000。  仅NORMAL队列和FIFO队列可以设置延时消息，Kafka队列不支持延时消息的功能，如果向Kafka队列生产延时消息，提示{\"code\":10540010, \"message\":\"Invalid request format: kafka queue message could not have delayTime.\"}。 

        :return: The delay_time of this SendMessageEntity.
        :rtype: object
        """
        return self._delay_time

    @delay_time.setter
    def delay_time(self, delay_time):
        """Sets the delay_time of this SendMessageEntity.

        延时消息的延时时长。  延时消息是指消息发送到DMS服务后，并不期望这条消息立即被消费，而是延迟一段时间后才能被消费。  取值范围：0~604800000  单位：毫秒  不配置该参数或者配置为0，表示无延时。  配置为浮点数时，自动取小数点前面的整数值，比如配置为6000.9，则自动取值为6000。  仅NORMAL队列和FIFO队列可以设置延时消息，Kafka队列不支持延时消息的功能，如果向Kafka队列生产延时消息，提示{\"code\":10540010, \"message\":\"Invalid request format: kafka queue message could not have delayTime.\"}。 

        :param delay_time: The delay_time of this SendMessageEntity.
        :type delay_time: object
        """
        self._delay_time = delay_time

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
        if not isinstance(other, SendMessageEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBindingBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination': 'str',
        'routing_key': 'str',
        'destination_type': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'routing_key': 'routing_key',
        'destination_type': 'destination_type'
    }

    def __init__(self, destination=None, routing_key=None, destination_type=None):
        r"""CreateBindingBody

        The model defined in huaweicloud sdk

        :param destination: 要投递的Exchange或Queue名称
        :type destination: str
        :param routing_key: 绑定键值，用于告知Exchange应该将消息投递到哪些Queue或Exchange中
        :type routing_key: str
        :param destination_type: 绑定目标端类型，Exchange或Queue。[（AMQP版本只支持绑定Queue）](tag:hws,hws_hk)
        :type destination_type: str
        """
        
        

        self._destination = None
        self._routing_key = None
        self._destination_type = None
        self.discriminator = None

        self.destination = destination
        self.routing_key = routing_key
        self.destination_type = destination_type

    @property
    def destination(self):
        r"""Gets the destination of this CreateBindingBody.

        要投递的Exchange或Queue名称

        :return: The destination of this CreateBindingBody.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this CreateBindingBody.

        要投递的Exchange或Queue名称

        :param destination: The destination of this CreateBindingBody.
        :type destination: str
        """
        self._destination = destination

    @property
    def routing_key(self):
        r"""Gets the routing_key of this CreateBindingBody.

        绑定键值，用于告知Exchange应该将消息投递到哪些Queue或Exchange中

        :return: The routing_key of this CreateBindingBody.
        :rtype: str
        """
        return self._routing_key

    @routing_key.setter
    def routing_key(self, routing_key):
        r"""Sets the routing_key of this CreateBindingBody.

        绑定键值，用于告知Exchange应该将消息投递到哪些Queue或Exchange中

        :param routing_key: The routing_key of this CreateBindingBody.
        :type routing_key: str
        """
        self._routing_key = routing_key

    @property
    def destination_type(self):
        r"""Gets the destination_type of this CreateBindingBody.

        绑定目标端类型，Exchange或Queue。[（AMQP版本只支持绑定Queue）](tag:hws,hws_hk)

        :return: The destination_type of this CreateBindingBody.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        r"""Sets the destination_type of this CreateBindingBody.

        绑定目标端类型，Exchange或Queue。[（AMQP版本只支持绑定Queue）](tag:hws,hws_hk)

        :param destination_type: The destination_type of this CreateBindingBody.
        :type destination_type: str
        """
        self._destination_type = destination_type

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
        if not isinstance(other, CreateBindingBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

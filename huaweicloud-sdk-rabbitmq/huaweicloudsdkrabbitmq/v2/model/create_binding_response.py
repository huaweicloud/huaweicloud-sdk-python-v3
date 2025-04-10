# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBindingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'destination_type': 'str',
        'destination': 'str',
        'routing_key': 'str'
    }

    attribute_map = {
        'source': 'source',
        'destination_type': 'destination_type',
        'destination': 'destination',
        'routing_key': 'routing_key'
    }

    def __init__(self, source=None, destination_type=None, destination=None, routing_key=None):
        r"""CreateBindingResponse

        The model defined in huaweicloud sdk

        :param source: 绑定对象
        :type source: str
        :param destination_type: 绑定Exchange或者Queue
        :type destination_type: str
        :param destination: 要投递的Exchange或Queue名称
        :type destination: str
        :param routing_key: 绑定键值，用于告知Exchange应该将消息投递到哪些Queue中
        :type routing_key: str
        """
        
        super(CreateBindingResponse, self).__init__()

        self._source = None
        self._destination_type = None
        self._destination = None
        self._routing_key = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if destination_type is not None:
            self.destination_type = destination_type
        if destination is not None:
            self.destination = destination
        if routing_key is not None:
            self.routing_key = routing_key

    @property
    def source(self):
        r"""Gets the source of this CreateBindingResponse.

        绑定对象

        :return: The source of this CreateBindingResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateBindingResponse.

        绑定对象

        :param source: The source of this CreateBindingResponse.
        :type source: str
        """
        self._source = source

    @property
    def destination_type(self):
        r"""Gets the destination_type of this CreateBindingResponse.

        绑定Exchange或者Queue

        :return: The destination_type of this CreateBindingResponse.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        r"""Sets the destination_type of this CreateBindingResponse.

        绑定Exchange或者Queue

        :param destination_type: The destination_type of this CreateBindingResponse.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def destination(self):
        r"""Gets the destination of this CreateBindingResponse.

        要投递的Exchange或Queue名称

        :return: The destination of this CreateBindingResponse.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this CreateBindingResponse.

        要投递的Exchange或Queue名称

        :param destination: The destination of this CreateBindingResponse.
        :type destination: str
        """
        self._destination = destination

    @property
    def routing_key(self):
        r"""Gets the routing_key of this CreateBindingResponse.

        绑定键值，用于告知Exchange应该将消息投递到哪些Queue中

        :return: The routing_key of this CreateBindingResponse.
        :rtype: str
        """
        return self._routing_key

    @routing_key.setter
    def routing_key(self, routing_key):
        r"""Sets the routing_key of this CreateBindingResponse.

        绑定键值，用于告知Exchange应该将消息投递到哪些Queue中

        :param routing_key: The routing_key of this CreateBindingResponse.
        :type routing_key: str
        """
        self._routing_key = routing_key

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
        if not isinstance(other, CreateBindingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

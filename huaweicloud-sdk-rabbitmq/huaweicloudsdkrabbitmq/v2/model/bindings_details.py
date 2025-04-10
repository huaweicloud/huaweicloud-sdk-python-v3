# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindingsDetails:

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
        'routing_key': 'str',
        'properties_key': 'str'
    }

    attribute_map = {
        'source': 'source',
        'destination_type': 'destination_type',
        'destination': 'destination',
        'routing_key': 'routing_key',
        'properties_key': 'properties_key'
    }

    def __init__(self, source=None, destination_type=None, destination=None, routing_key=None, properties_key=None):
        r"""BindingsDetails

        The model defined in huaweicloud sdk

        :param source: Exchange名称
        :type source: str
        :param destination_type: 绑定目标类型
        :type destination_type: str
        :param destination: 绑定目标的名称
        :type destination: str
        :param routing_key: 绑定键值
        :type routing_key: str
        :param properties_key: 经过URL转译后routing_key
        :type properties_key: str
        """
        
        

        self._source = None
        self._destination_type = None
        self._destination = None
        self._routing_key = None
        self._properties_key = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if destination_type is not None:
            self.destination_type = destination_type
        if destination is not None:
            self.destination = destination
        if routing_key is not None:
            self.routing_key = routing_key
        if properties_key is not None:
            self.properties_key = properties_key

    @property
    def source(self):
        r"""Gets the source of this BindingsDetails.

        Exchange名称

        :return: The source of this BindingsDetails.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this BindingsDetails.

        Exchange名称

        :param source: The source of this BindingsDetails.
        :type source: str
        """
        self._source = source

    @property
    def destination_type(self):
        r"""Gets the destination_type of this BindingsDetails.

        绑定目标类型

        :return: The destination_type of this BindingsDetails.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        r"""Sets the destination_type of this BindingsDetails.

        绑定目标类型

        :param destination_type: The destination_type of this BindingsDetails.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def destination(self):
        r"""Gets the destination of this BindingsDetails.

        绑定目标的名称

        :return: The destination of this BindingsDetails.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this BindingsDetails.

        绑定目标的名称

        :param destination: The destination of this BindingsDetails.
        :type destination: str
        """
        self._destination = destination

    @property
    def routing_key(self):
        r"""Gets the routing_key of this BindingsDetails.

        绑定键值

        :return: The routing_key of this BindingsDetails.
        :rtype: str
        """
        return self._routing_key

    @routing_key.setter
    def routing_key(self, routing_key):
        r"""Sets the routing_key of this BindingsDetails.

        绑定键值

        :param routing_key: The routing_key of this BindingsDetails.
        :type routing_key: str
        """
        self._routing_key = routing_key

    @property
    def properties_key(self):
        r"""Gets the properties_key of this BindingsDetails.

        经过URL转译后routing_key

        :return: The properties_key of this BindingsDetails.
        :rtype: str
        """
        return self._properties_key

    @properties_key.setter
    def properties_key(self, properties_key):
        r"""Sets the properties_key of this BindingsDetails.

        经过URL转译后routing_key

        :param properties_key: The properties_key of this BindingsDetails.
        :type properties_key: str
        """
        self._properties_key = properties_key

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
        if not isinstance(other, BindingsDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

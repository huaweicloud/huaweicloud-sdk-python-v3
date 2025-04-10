# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBindingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'vhost': 'str',
        'exchange': 'str',
        'destination_type': 'str',
        'destination': 'str',
        'properties_key': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'vhost': 'vhost',
        'exchange': 'exchange',
        'destination_type': 'destination_type',
        'destination': 'destination',
        'properties_key': 'properties_key'
    }

    def __init__(self, instance_id=None, vhost=None, exchange=None, destination_type=None, destination=None, properties_key=None):
        r"""DeleteBindingRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param vhost: Vhost名称
        :type vhost: str
        :param exchange: Exchange名称
        :type exchange: str
        :param destination_type: 绑定目标端类型，Exchange或Queue。[（AMQP版本只支持Queue绑定类型）](tag:hws,hws_hk)
        :type destination_type: str
        :param destination: 绑定的目标端名称
        :type destination: str
        :param properties_key: 绑定路由键，经过URL转译后routing_key，可通过调用[查询Exchange绑定列表](ListBindings.xml)或者[查询指定Queue详情](ShowQueueDetails.xml)接口的响应信息获取。
        :type properties_key: str
        """
        
        

        self._instance_id = None
        self._vhost = None
        self._exchange = None
        self._destination_type = None
        self._destination = None
        self._properties_key = None
        self.discriminator = None

        self.instance_id = instance_id
        self.vhost = vhost
        self.exchange = exchange
        self.destination_type = destination_type
        self.destination = destination
        self.properties_key = properties_key

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteBindingRequest.

        实例ID

        :return: The instance_id of this DeleteBindingRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteBindingRequest.

        实例ID

        :param instance_id: The instance_id of this DeleteBindingRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vhost(self):
        r"""Gets the vhost of this DeleteBindingRequest.

        Vhost名称

        :return: The vhost of this DeleteBindingRequest.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this DeleteBindingRequest.

        Vhost名称

        :param vhost: The vhost of this DeleteBindingRequest.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def exchange(self):
        r"""Gets the exchange of this DeleteBindingRequest.

        Exchange名称

        :return: The exchange of this DeleteBindingRequest.
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        r"""Sets the exchange of this DeleteBindingRequest.

        Exchange名称

        :param exchange: The exchange of this DeleteBindingRequest.
        :type exchange: str
        """
        self._exchange = exchange

    @property
    def destination_type(self):
        r"""Gets the destination_type of this DeleteBindingRequest.

        绑定目标端类型，Exchange或Queue。[（AMQP版本只支持Queue绑定类型）](tag:hws,hws_hk)

        :return: The destination_type of this DeleteBindingRequest.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        r"""Sets the destination_type of this DeleteBindingRequest.

        绑定目标端类型，Exchange或Queue。[（AMQP版本只支持Queue绑定类型）](tag:hws,hws_hk)

        :param destination_type: The destination_type of this DeleteBindingRequest.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def destination(self):
        r"""Gets the destination of this DeleteBindingRequest.

        绑定的目标端名称

        :return: The destination of this DeleteBindingRequest.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this DeleteBindingRequest.

        绑定的目标端名称

        :param destination: The destination of this DeleteBindingRequest.
        :type destination: str
        """
        self._destination = destination

    @property
    def properties_key(self):
        r"""Gets the properties_key of this DeleteBindingRequest.

        绑定路由键，经过URL转译后routing_key，可通过调用[查询Exchange绑定列表](ListBindings.xml)或者[查询指定Queue详情](ShowQueueDetails.xml)接口的响应信息获取。

        :return: The properties_key of this DeleteBindingRequest.
        :rtype: str
        """
        return self._properties_key

    @properties_key.setter
    def properties_key(self, properties_key):
        r"""Sets the properties_key of this DeleteBindingRequest.

        绑定路由键，经过URL转译后routing_key，可通过调用[查询Exchange绑定列表](ListBindings.xml)或者[查询指定Queue详情](ShowQueueDetails.xml)接口的响应信息获取。

        :param properties_key: The properties_key of this DeleteBindingRequest.
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
        if not isinstance(other, DeleteBindingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

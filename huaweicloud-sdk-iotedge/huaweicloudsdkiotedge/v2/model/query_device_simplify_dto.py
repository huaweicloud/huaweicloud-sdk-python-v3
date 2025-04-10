# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDeviceSimplifyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'node_id': 'str',
        'gateway_id': 'str',
        'device_name': 'str',
        'protocol_type': 'str',
        'product_name': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'node_id': 'node_id',
        'gateway_id': 'gateway_id',
        'device_name': 'device_name',
        'protocol_type': 'protocol_type',
        'product_name': 'product_name',
        'product_id': 'product_id'
    }

    def __init__(self, device_id=None, node_id=None, gateway_id=None, device_name=None, protocol_type=None, product_name=None, product_id=None):
        r"""QueryDeviceSimplifyDto

        The model defined in huaweicloud sdk

        :param device_id: 设备id
        :type device_id: str
        :param node_id: 设备识别码
        :type node_id: str
        :param gateway_id: 父设备id
        :type gateway_id: str
        :param device_name: 设备名称
        :type device_name: str
        :param protocol_type: 设备协议类型
        :type protocol_type: str
        :param product_name: 产品名称
        :type product_name: str
        :param product_id: 产品ID
        :type product_id: str
        """
        
        

        self._device_id = None
        self._node_id = None
        self._gateway_id = None
        self._device_name = None
        self._protocol_type = None
        self._product_name = None
        self._product_id = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if node_id is not None:
            self.node_id = node_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if device_name is not None:
            self.device_name = device_name
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if product_name is not None:
            self.product_name = product_name
        if product_id is not None:
            self.product_id = product_id

    @property
    def device_id(self):
        r"""Gets the device_id of this QueryDeviceSimplifyDto.

        设备id

        :return: The device_id of this QueryDeviceSimplifyDto.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this QueryDeviceSimplifyDto.

        设备id

        :param device_id: The device_id of this QueryDeviceSimplifyDto.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def node_id(self):
        r"""Gets the node_id of this QueryDeviceSimplifyDto.

        设备识别码

        :return: The node_id of this QueryDeviceSimplifyDto.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this QueryDeviceSimplifyDto.

        设备识别码

        :param node_id: The node_id of this QueryDeviceSimplifyDto.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this QueryDeviceSimplifyDto.

        父设备id

        :return: The gateway_id of this QueryDeviceSimplifyDto.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this QueryDeviceSimplifyDto.

        父设备id

        :param gateway_id: The gateway_id of this QueryDeviceSimplifyDto.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def device_name(self):
        r"""Gets the device_name of this QueryDeviceSimplifyDto.

        设备名称

        :return: The device_name of this QueryDeviceSimplifyDto.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        r"""Sets the device_name of this QueryDeviceSimplifyDto.

        设备名称

        :param device_name: The device_name of this QueryDeviceSimplifyDto.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def protocol_type(self):
        r"""Gets the protocol_type of this QueryDeviceSimplifyDto.

        设备协议类型

        :return: The protocol_type of this QueryDeviceSimplifyDto.
        :rtype: str
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        r"""Sets the protocol_type of this QueryDeviceSimplifyDto.

        设备协议类型

        :param protocol_type: The protocol_type of this QueryDeviceSimplifyDto.
        :type protocol_type: str
        """
        self._protocol_type = protocol_type

    @property
    def product_name(self):
        r"""Gets the product_name of this QueryDeviceSimplifyDto.

        产品名称

        :return: The product_name of this QueryDeviceSimplifyDto.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this QueryDeviceSimplifyDto.

        产品名称

        :param product_name: The product_name of this QueryDeviceSimplifyDto.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def product_id(self):
        r"""Gets the product_id of this QueryDeviceSimplifyDto.

        产品ID

        :return: The product_id of this QueryDeviceSimplifyDto.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this QueryDeviceSimplifyDto.

        产品ID

        :param product_id: The product_id of this QueryDeviceSimplifyDto.
        :type product_id: str
        """
        self._product_id = product_id

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
        if not isinstance(other, QueryDeviceSimplifyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

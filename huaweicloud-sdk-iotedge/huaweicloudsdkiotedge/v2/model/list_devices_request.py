# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevicesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_node_id': 'str',
        'gateway_id': 'str',
        'device_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'gateway_id': 'gateway_id',
        'device_name': 'device_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, edge_node_id=None, gateway_id=None, device_name=None, offset=None, limit=None):
        """ListDevicesRequest

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param gateway_id: 父设备ID,对应之前的gatewayId的概念，传该参数时代表查询网关下的子设备，不传代表查询网关直连设备
        :type gateway_id: str
        :param device_name: 设备名称
        :type device_name: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页记录数，默认值为10，取值区间为1-1000
        :type limit: int
        """
        
        

        self._edge_node_id = None
        self._gateway_id = None
        self._device_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.edge_node_id = edge_node_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if device_name is not None:
            self.device_name = device_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def edge_node_id(self):
        """Gets the edge_node_id of this ListDevicesRequest.

        边缘节点ID

        :return: The edge_node_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        """Sets the edge_node_id of this ListDevicesRequest.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this ListDevicesRequest.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ListDevicesRequest.

        父设备ID,对应之前的gatewayId的概念，传该参数时代表查询网关下的子设备，不传代表查询网关直连设备

        :return: The gateway_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ListDevicesRequest.

        父设备ID,对应之前的gatewayId的概念，传该参数时代表查询网关下的子设备，不传代表查询网关直连设备

        :param gateway_id: The gateway_id of this ListDevicesRequest.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def device_name(self):
        """Gets the device_name of this ListDevicesRequest.

        设备名称

        :return: The device_name of this ListDevicesRequest.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ListDevicesRequest.

        设备名称

        :param device_name: The device_name of this ListDevicesRequest.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def offset(self):
        """Gets the offset of this ListDevicesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListDevicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDevicesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListDevicesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDevicesRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :return: The limit of this ListDevicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDevicesRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :param limit: The limit of this ListDevicesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDevicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

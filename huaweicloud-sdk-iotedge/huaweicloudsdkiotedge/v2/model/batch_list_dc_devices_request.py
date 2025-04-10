# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListDcDevicesRequest:

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
        'ds_id': 'str',
        'device_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'ds_id': 'ds_id',
        'device_id': 'device_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, edge_node_id=None, ds_id=None, device_id=None, offset=None, limit=None):
        r"""BatchListDcDevicesRequest

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param ds_id: 采集数据源id，创建数据源配置时设置，节点下唯一。
        :type ds_id: str
        :param device_id: 设备标识码。
        :type device_id: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页记录数，默认值为10，取值区间为1-1000
        :type limit: int
        """
        
        

        self._edge_node_id = None
        self._ds_id = None
        self._device_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.edge_node_id = edge_node_id
        self.ds_id = ds_id
        if device_id is not None:
            self.device_id = device_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def edge_node_id(self):
        r"""Gets the edge_node_id of this BatchListDcDevicesRequest.

        边缘节点ID

        :return: The edge_node_id of this BatchListDcDevicesRequest.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        r"""Sets the edge_node_id of this BatchListDcDevicesRequest.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this BatchListDcDevicesRequest.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def ds_id(self):
        r"""Gets the ds_id of this BatchListDcDevicesRequest.

        采集数据源id，创建数据源配置时设置，节点下唯一。

        :return: The ds_id of this BatchListDcDevicesRequest.
        :rtype: str
        """
        return self._ds_id

    @ds_id.setter
    def ds_id(self, ds_id):
        r"""Sets the ds_id of this BatchListDcDevicesRequest.

        采集数据源id，创建数据源配置时设置，节点下唯一。

        :param ds_id: The ds_id of this BatchListDcDevicesRequest.
        :type ds_id: str
        """
        self._ds_id = ds_id

    @property
    def device_id(self):
        r"""Gets the device_id of this BatchListDcDevicesRequest.

        设备标识码。

        :return: The device_id of this BatchListDcDevicesRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this BatchListDcDevicesRequest.

        设备标识码。

        :param device_id: The device_id of this BatchListDcDevicesRequest.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def offset(self):
        r"""Gets the offset of this BatchListDcDevicesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this BatchListDcDevicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BatchListDcDevicesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this BatchListDcDevicesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this BatchListDcDevicesRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :return: The limit of this BatchListDcDevicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BatchListDcDevicesRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :param limit: The limit of this BatchListDcDevicesRequest.
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
        if not isinstance(other, BatchListDcDevicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

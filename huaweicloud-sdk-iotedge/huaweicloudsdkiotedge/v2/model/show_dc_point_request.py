# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDcPointRequest:

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
        'point_id': 'str',
        'device_id': 'str',
        '_property': 'str'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'ds_id': 'ds_id',
        'point_id': 'point_id',
        'device_id': 'device_id',
        '_property': 'property'
    }

    def __init__(self, edge_node_id=None, ds_id=None, point_id=None, device_id=None, _property=None):
        r"""ShowDcPointRequest

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param ds_id: 采集数据源id，创建数据源配置时设置，节点下唯一。
        :type ds_id: str
        :param point_id: 采集点位表id，创建点位表时设置，数据源下唯一。
        :type point_id: str
        :param device_id: 设备id
        :type device_id: str
        :param _property: 设备服务属性，允许中、数字、英文大小写、下划线、中划线
        :type _property: str
        """
        
        

        self._edge_node_id = None
        self._ds_id = None
        self._point_id = None
        self._device_id = None
        self.__property = None
        self.discriminator = None

        self.edge_node_id = edge_node_id
        self.ds_id = ds_id
        self.point_id = point_id
        if device_id is not None:
            self.device_id = device_id
        if _property is not None:
            self._property = _property

    @property
    def edge_node_id(self):
        r"""Gets the edge_node_id of this ShowDcPointRequest.

        边缘节点ID

        :return: The edge_node_id of this ShowDcPointRequest.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        r"""Sets the edge_node_id of this ShowDcPointRequest.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this ShowDcPointRequest.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def ds_id(self):
        r"""Gets the ds_id of this ShowDcPointRequest.

        采集数据源id，创建数据源配置时设置，节点下唯一。

        :return: The ds_id of this ShowDcPointRequest.
        :rtype: str
        """
        return self._ds_id

    @ds_id.setter
    def ds_id(self, ds_id):
        r"""Sets the ds_id of this ShowDcPointRequest.

        采集数据源id，创建数据源配置时设置，节点下唯一。

        :param ds_id: The ds_id of this ShowDcPointRequest.
        :type ds_id: str
        """
        self._ds_id = ds_id

    @property
    def point_id(self):
        r"""Gets the point_id of this ShowDcPointRequest.

        采集点位表id，创建点位表时设置，数据源下唯一。

        :return: The point_id of this ShowDcPointRequest.
        :rtype: str
        """
        return self._point_id

    @point_id.setter
    def point_id(self, point_id):
        r"""Sets the point_id of this ShowDcPointRequest.

        采集点位表id，创建点位表时设置，数据源下唯一。

        :param point_id: The point_id of this ShowDcPointRequest.
        :type point_id: str
        """
        self._point_id = point_id

    @property
    def device_id(self):
        r"""Gets the device_id of this ShowDcPointRequest.

        设备id

        :return: The device_id of this ShowDcPointRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this ShowDcPointRequest.

        设备id

        :param device_id: The device_id of this ShowDcPointRequest.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def _property(self):
        r"""Gets the _property of this ShowDcPointRequest.

        设备服务属性，允许中、数字、英文大小写、下划线、中划线

        :return: The _property of this ShowDcPointRequest.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        r"""Sets the _property of this ShowDcPointRequest.

        设备服务属性，允许中、数字、英文大小写、下划线、中划线

        :param _property: The _property of this ShowDcPointRequest.
        :type _property: str
        """
        self.__property = _property

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
        if not isinstance(other, ShowDcPointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

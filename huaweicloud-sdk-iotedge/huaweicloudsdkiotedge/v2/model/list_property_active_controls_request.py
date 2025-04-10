# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPropertyActiveControlsRequest:

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
        'device_id': 'str',
        'service_id': 'str',
        '_property': 'str'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'device_id': 'device_id',
        'service_id': 'service_id',
        '_property': 'property'
    }

    def __init__(self, edge_node_id=None, device_id=None, service_id=None, _property=None):
        r"""ListPropertyActiveControlsRequest

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param device_id: 设备ID
        :type device_id: str
        :param service_id: 设备服务id。可选，在属性平铺场景不需要填，如果不填则表示service_id为空字符串
        :type service_id: str
        :param _property: 设备属性。必选
        :type _property: str
        """
        
        

        self._edge_node_id = None
        self._device_id = None
        self._service_id = None
        self.__property = None
        self.discriminator = None

        self.edge_node_id = edge_node_id
        self.device_id = device_id
        if service_id is not None:
            self.service_id = service_id
        self._property = _property

    @property
    def edge_node_id(self):
        r"""Gets the edge_node_id of this ListPropertyActiveControlsRequest.

        边缘节点ID

        :return: The edge_node_id of this ListPropertyActiveControlsRequest.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        r"""Sets the edge_node_id of this ListPropertyActiveControlsRequest.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this ListPropertyActiveControlsRequest.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def device_id(self):
        r"""Gets the device_id of this ListPropertyActiveControlsRequest.

        设备ID

        :return: The device_id of this ListPropertyActiveControlsRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this ListPropertyActiveControlsRequest.

        设备ID

        :param device_id: The device_id of this ListPropertyActiveControlsRequest.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def service_id(self):
        r"""Gets the service_id of this ListPropertyActiveControlsRequest.

        设备服务id。可选，在属性平铺场景不需要填，如果不填则表示service_id为空字符串

        :return: The service_id of this ListPropertyActiveControlsRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ListPropertyActiveControlsRequest.

        设备服务id。可选，在属性平铺场景不需要填，如果不填则表示service_id为空字符串

        :param service_id: The service_id of this ListPropertyActiveControlsRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def _property(self):
        r"""Gets the _property of this ListPropertyActiveControlsRequest.

        设备属性。必选

        :return: The _property of this ListPropertyActiveControlsRequest.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        r"""Sets the _property of this ListPropertyActiveControlsRequest.

        设备属性。必选

        :param _property: The _property of this ListPropertyActiveControlsRequest.
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
        if not isinstance(other, ListPropertyActiveControlsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

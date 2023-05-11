# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDcPointRequest:

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
        'body': 'UpdateDcPointReqDTO'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'ds_id': 'ds_id',
        'point_id': 'point_id',
        'body': 'body'
    }

    def __init__(self, edge_node_id=None, ds_id=None, point_id=None, body=None):
        """UpdateDcPointRequest

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param ds_id: 采集数据源id，创建数据源配置时设置，节点下唯一。
        :type ds_id: str
        :param point_id: 采集点位表id，创建点位表时设置，数据源下唯一。
        :type point_id: str
        :param body: Body of the UpdateDcPointRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateDcPointReqDTO`
        """
        
        

        self._edge_node_id = None
        self._ds_id = None
        self._point_id = None
        self._body = None
        self.discriminator = None

        self.edge_node_id = edge_node_id
        self.ds_id = ds_id
        self.point_id = point_id
        if body is not None:
            self.body = body

    @property
    def edge_node_id(self):
        """Gets the edge_node_id of this UpdateDcPointRequest.

        边缘节点ID

        :return: The edge_node_id of this UpdateDcPointRequest.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        """Sets the edge_node_id of this UpdateDcPointRequest.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this UpdateDcPointRequest.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def ds_id(self):
        """Gets the ds_id of this UpdateDcPointRequest.

        采集数据源id，创建数据源配置时设置，节点下唯一。

        :return: The ds_id of this UpdateDcPointRequest.
        :rtype: str
        """
        return self._ds_id

    @ds_id.setter
    def ds_id(self, ds_id):
        """Sets the ds_id of this UpdateDcPointRequest.

        采集数据源id，创建数据源配置时设置，节点下唯一。

        :param ds_id: The ds_id of this UpdateDcPointRequest.
        :type ds_id: str
        """
        self._ds_id = ds_id

    @property
    def point_id(self):
        """Gets the point_id of this UpdateDcPointRequest.

        采集点位表id，创建点位表时设置，数据源下唯一。

        :return: The point_id of this UpdateDcPointRequest.
        :rtype: str
        """
        return self._point_id

    @point_id.setter
    def point_id(self, point_id):
        """Sets the point_id of this UpdateDcPointRequest.

        采集点位表id，创建点位表时设置，数据源下唯一。

        :param point_id: The point_id of this UpdateDcPointRequest.
        :type point_id: str
        """
        self._point_id = point_id

    @property
    def body(self):
        """Gets the body of this UpdateDcPointRequest.

        :return: The body of this UpdateDcPointRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.UpdateDcPointReqDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDcPointRequest.

        :param body: The body of this UpdateDcPointRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.UpdateDcPointReqDTO`
        """
        self._body = body

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
        if not isinstance(other, UpdateDcPointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

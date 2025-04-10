# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointConnectionsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'id': 'str',
        'marker_id': 'int',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'id': 'id',
        'marker_id': 'marker_id',
        'status': 'status'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, id=None, marker_id=None, status=None):
        r"""ListEndpointConnectionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500
        :type limit: int
        :param id: 终端节点的ID，唯一标识
        :type id: str
        :param marker_id: 终端节点的报文标识
        :type marker_id: int
        :param status: 终端节点的连接状态 - pendingAcceptance 待接受 - accepted 已接受 - rejected 已拒绝 - failed 失败
        :type status: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._id = None
        self._marker_id = None
        self._status = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if marker_id is not None:
            self.marker_id = marker_id
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListEndpointConnectionsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ListEndpointConnectionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListEndpointConnectionsRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ListEndpointConnectionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListEndpointConnectionsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListEndpointConnectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEndpointConnectionsRequest.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListEndpointConnectionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEndpointConnectionsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :return: The limit of this ListEndpointConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEndpointConnectionsRequest.

        每页显示的条目数量，条目数量小于等于0时，自动转换为20，条目数量大于500时，自动转换为500

        :param limit: The limit of this ListEndpointConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListEndpointConnectionsRequest.

        终端节点的ID，唯一标识

        :return: The id of this ListEndpointConnectionsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListEndpointConnectionsRequest.

        终端节点的ID，唯一标识

        :param id: The id of this ListEndpointConnectionsRequest.
        :type id: str
        """
        self._id = id

    @property
    def marker_id(self):
        r"""Gets the marker_id of this ListEndpointConnectionsRequest.

        终端节点的报文标识

        :return: The marker_id of this ListEndpointConnectionsRequest.
        :rtype: int
        """
        return self._marker_id

    @marker_id.setter
    def marker_id(self, marker_id):
        r"""Sets the marker_id of this ListEndpointConnectionsRequest.

        终端节点的报文标识

        :param marker_id: The marker_id of this ListEndpointConnectionsRequest.
        :type marker_id: int
        """
        self._marker_id = marker_id

    @property
    def status(self):
        r"""Gets the status of this ListEndpointConnectionsRequest.

        终端节点的连接状态 - pendingAcceptance 待接受 - accepted 已接受 - rejected 已拒绝 - failed 失败

        :return: The status of this ListEndpointConnectionsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListEndpointConnectionsRequest.

        终端节点的连接状态 - pendingAcceptance 待接受 - accepted 已接受 - rejected 已拒绝 - failed 失败

        :param status: The status of this ListEndpointConnectionsRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListEndpointConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

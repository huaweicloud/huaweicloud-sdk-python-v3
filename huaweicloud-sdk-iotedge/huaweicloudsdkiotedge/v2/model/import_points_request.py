# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportPointsRequest:

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
        'update_type': 'str',
        'body': 'ImportPointsRequestBody'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'ds_id': 'ds_id',
        'update_type': 'update_type',
        'body': 'body'
    }

    def __init__(self, edge_node_id=None, ds_id=None, update_type=None, body=None):
        r"""ImportPointsRequest

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param ds_id: 采集数据源id，创建数据源配置时设置，节点下唯一。
        :type ds_id: str
        :param update_type: 该字段PARTIAL则增量覆盖，已有点位更新，新增点位插入;该字段为COMPLETE则全量覆盖，则删除数据源下所有点位，插入当前导入所有点位
        :type update_type: str
        :param body: Body of the ImportPointsRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.ImportPointsRequestBody`
        """
        
        

        self._edge_node_id = None
        self._ds_id = None
        self._update_type = None
        self._body = None
        self.discriminator = None

        self.edge_node_id = edge_node_id
        self.ds_id = ds_id
        self.update_type = update_type
        if body is not None:
            self.body = body

    @property
    def edge_node_id(self):
        r"""Gets the edge_node_id of this ImportPointsRequest.

        边缘节点ID

        :return: The edge_node_id of this ImportPointsRequest.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        r"""Sets the edge_node_id of this ImportPointsRequest.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this ImportPointsRequest.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def ds_id(self):
        r"""Gets the ds_id of this ImportPointsRequest.

        采集数据源id，创建数据源配置时设置，节点下唯一。

        :return: The ds_id of this ImportPointsRequest.
        :rtype: str
        """
        return self._ds_id

    @ds_id.setter
    def ds_id(self, ds_id):
        r"""Sets the ds_id of this ImportPointsRequest.

        采集数据源id，创建数据源配置时设置，节点下唯一。

        :param ds_id: The ds_id of this ImportPointsRequest.
        :type ds_id: str
        """
        self._ds_id = ds_id

    @property
    def update_type(self):
        r"""Gets the update_type of this ImportPointsRequest.

        该字段PARTIAL则增量覆盖，已有点位更新，新增点位插入;该字段为COMPLETE则全量覆盖，则删除数据源下所有点位，插入当前导入所有点位

        :return: The update_type of this ImportPointsRequest.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        r"""Sets the update_type of this ImportPointsRequest.

        该字段PARTIAL则增量覆盖，已有点位更新，新增点位插入;该字段为COMPLETE则全量覆盖，则删除数据源下所有点位，插入当前导入所有点位

        :param update_type: The update_type of this ImportPointsRequest.
        :type update_type: str
        """
        self._update_type = update_type

    @property
    def body(self):
        r"""Gets the body of this ImportPointsRequest.

        :return: The body of this ImportPointsRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ImportPointsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ImportPointsRequest.

        :param body: The body of this ImportPointsRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.ImportPointsRequestBody`
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
        if not isinstance(other, ImportPointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

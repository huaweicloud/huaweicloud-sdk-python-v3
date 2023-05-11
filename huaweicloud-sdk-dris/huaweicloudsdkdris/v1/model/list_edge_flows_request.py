# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeFlowsRequest:

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
        'from_date': 'str',
        'to_date': 'str',
        'edge_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'offset': 'offset',
        'limit': 'limit',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'edge_id': 'edge_id'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, from_date=None, to_date=None, edge_id=None):
        """ListEdgeFlowsRequest

        The model defined in huaweicloud sdk

        :param instance_id: \&quot;**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\&quot;
        :type instance_id: str
        :param offset: **参数说明**：分页查询时的页码。
        :type offset: int
        :param limit: **参数说明**：分页查询时每页显示的记录数。
        :type limit: int
        :param from_date: **参数说明**：查询此时间后达到平台的消息。  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;。  例如 2020-09-01T01:37:01.000Z。  **取值范围**：携带edge_id参数查询时，from_date和to_date的时间范围不能超过24小时；未携带edge_id参数查询时，from_date和to_date的时间范围不能超过1小时。 
        :type from_date: str
        :param to_date: **参数说明**：查询此时间前达到平台的消息。  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;。  例如 2020-09-02T01:37:01.000Z。  **取值范围**：携带edge_id参数查询时，from_date和to_date的时间范围不能超过24小时；未携带edge_id参数查询时，from_date和to_date的时间范围不能超过1小时。 
        :type to_date: str
        :param edge_id: **参数说明**：Edge ID，用于唯一标识一个Edge。  **取值范围**：数字，a至f的小写字母，横杠（-），长度为36的组合。 
        :type edge_id: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._from_date = None
        self._to_date = None
        self._edge_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if edge_id is not None:
            self.edge_id = edge_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListEdgeFlowsRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :return: The instance_id of this ListEdgeFlowsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListEdgeFlowsRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :param instance_id: The instance_id of this ListEdgeFlowsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListEdgeFlowsRequest.

        **参数说明**：分页查询时的页码。

        :return: The offset of this ListEdgeFlowsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEdgeFlowsRequest.

        **参数说明**：分页查询时的页码。

        :param offset: The offset of this ListEdgeFlowsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEdgeFlowsRequest.

        **参数说明**：分页查询时每页显示的记录数。

        :return: The limit of this ListEdgeFlowsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEdgeFlowsRequest.

        **参数说明**：分页查询时每页显示的记录数。

        :param limit: The limit of this ListEdgeFlowsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def from_date(self):
        """Gets the from_date of this ListEdgeFlowsRequest.

        **参数说明**：查询此时间后达到平台的消息。  格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z'。  例如 2020-09-01T01:37:01.000Z。  **取值范围**：携带edge_id参数查询时，from_date和to_date的时间范围不能超过24小时；未携带edge_id参数查询时，from_date和to_date的时间范围不能超过1小时。 

        :return: The from_date of this ListEdgeFlowsRequest.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this ListEdgeFlowsRequest.

        **参数说明**：查询此时间后达到平台的消息。  格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z'。  例如 2020-09-01T01:37:01.000Z。  **取值范围**：携带edge_id参数查询时，from_date和to_date的时间范围不能超过24小时；未携带edge_id参数查询时，from_date和to_date的时间范围不能超过1小时。 

        :param from_date: The from_date of this ListEdgeFlowsRequest.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this ListEdgeFlowsRequest.

        **参数说明**：查询此时间前达到平台的消息。  格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z'。  例如 2020-09-02T01:37:01.000Z。  **取值范围**：携带edge_id参数查询时，from_date和to_date的时间范围不能超过24小时；未携带edge_id参数查询时，from_date和to_date的时间范围不能超过1小时。 

        :return: The to_date of this ListEdgeFlowsRequest.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this ListEdgeFlowsRequest.

        **参数说明**：查询此时间前达到平台的消息。  格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z'。  例如 2020-09-02T01:37:01.000Z。  **取值范围**：携带edge_id参数查询时，from_date和to_date的时间范围不能超过24小时；未携带edge_id参数查询时，from_date和to_date的时间范围不能超过1小时。 

        :param to_date: The to_date of this ListEdgeFlowsRequest.
        :type to_date: str
        """
        self._to_date = to_date

    @property
    def edge_id(self):
        """Gets the edge_id of this ListEdgeFlowsRequest.

        **参数说明**：Edge ID，用于唯一标识一个Edge。  **取值范围**：数字，a至f的小写字母，横杠（-），长度为36的组合。 

        :return: The edge_id of this ListEdgeFlowsRequest.
        :rtype: str
        """
        return self._edge_id

    @edge_id.setter
    def edge_id(self, edge_id):
        """Sets the edge_id of this ListEdgeFlowsRequest.

        **参数说明**：Edge ID，用于唯一标识一个Edge。  **取值范围**：数字，a至f的小写字母，横杠（-），长度为36的组合。 

        :param edge_id: The edge_id of this ListEdgeFlowsRequest.
        :type edge_id: str
        """
        self._edge_id = edge_id

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
        if not isinstance(other, ListEdgeFlowsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

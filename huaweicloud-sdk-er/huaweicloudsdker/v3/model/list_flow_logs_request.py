# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlowLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'resource_type': 'str',
        'resource_id': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]'
    }

    attribute_map = {
        'er_id': 'er_id',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'limit': 'limit',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, er_id=None, resource_type=None, resource_id=None, limit=None, marker=None, sort_key=None, sort_dir=None):
        r"""ListFlowLogsRequest

        The model defined in huaweicloud sdk

        :param er_id: 企业路由器实例ID
        :type er_id: str
        :param resource_type: 采集的资源类型
        :type resource_type: str
        :param resource_id: 连接对应的资源ID列表
        :type resource_id: list[str]
        :param limit: 每页返回的个数。 取值范围：0~2000。
        :type limit: int
        :param marker: 上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param sort_key: 按关键字排序，默认按照id排序，可选值:id|name|state
        :type sort_key: list[str]
        :param sort_dir: 返回结果按照升序或降序排列，默认为asc,降序为desc
        :type sort_dir: list[str]
        """
        
        

        self._er_id = None
        self._resource_type = None
        self._resource_id = None
        self._limit = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.er_id = er_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def er_id(self):
        r"""Gets the er_id of this ListFlowLogsRequest.

        企业路由器实例ID

        :return: The er_id of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        r"""Sets the er_id of this ListFlowLogsRequest.

        企业路由器实例ID

        :param er_id: The er_id of this ListFlowLogsRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListFlowLogsRequest.

        采集的资源类型

        :return: The resource_type of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListFlowLogsRequest.

        采集的资源类型

        :param resource_type: The resource_type of this ListFlowLogsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListFlowLogsRequest.

        连接对应的资源ID列表

        :return: The resource_id of this ListFlowLogsRequest.
        :rtype: list[str]
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListFlowLogsRequest.

        连接对应的资源ID列表

        :param resource_id: The resource_id of this ListFlowLogsRequest.
        :type resource_id: list[str]
        """
        self._resource_id = resource_id

    @property
    def limit(self):
        r"""Gets the limit of this ListFlowLogsRequest.

        每页返回的个数。 取值范围：0~2000。

        :return: The limit of this ListFlowLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFlowLogsRequest.

        每页返回的个数。 取值范围：0~2000。

        :param limit: The limit of this ListFlowLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListFlowLogsRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFlowLogsRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListFlowLogsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListFlowLogsRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :return: The sort_key of this ListFlowLogsRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListFlowLogsRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :param sort_key: The sort_key of this ListFlowLogsRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListFlowLogsRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :return: The sort_dir of this ListFlowLogsRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListFlowLogsRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :param sort_dir: The sort_dir of this ListFlowLogsRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListFlowLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

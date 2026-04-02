# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGcTasksRequest:

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
        'marker': 'str',
        'limit': 'int',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'marker': 'marker',
        'limit': 'limit',
        'status': 'status'
    }

    def __init__(self, instance_id=None, marker=None, limit=None, status=None):
        r"""ListGcTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param marker: 分页查询时的查询标记，使用上一次接口调用返回的next_marker值，默认值从第一条数据查询。**注意：marker和limit参数需要配套使用。**
        :type marker: str
        :param limit: 条目数量，用于分页查询，默认值为10，最大值为100
        :type limit: int
        :param status: 任务状态，Success：已完成，Stopped：已停止，Running：清理中，Pending：排队中，Error：失败。
        :type status: str
        """
        
        

        self._instance_id = None
        self._marker = None
        self._limit = None
        self._status = None
        self.discriminator = None

        self.instance_id = instance_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListGcTasksRequest.

        企业仓库实例ID

        :return: The instance_id of this ListGcTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListGcTasksRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListGcTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def marker(self):
        r"""Gets the marker of this ListGcTasksRequest.

        分页查询时的查询标记，使用上一次接口调用返回的next_marker值，默认值从第一条数据查询。**注意：marker和limit参数需要配套使用。**

        :return: The marker of this ListGcTasksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListGcTasksRequest.

        分页查询时的查询标记，使用上一次接口调用返回的next_marker值，默认值从第一条数据查询。**注意：marker和limit参数需要配套使用。**

        :param marker: The marker of this ListGcTasksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListGcTasksRequest.

        条目数量，用于分页查询，默认值为10，最大值为100

        :return: The limit of this ListGcTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGcTasksRequest.

        条目数量，用于分页查询，默认值为10，最大值为100

        :param limit: The limit of this ListGcTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListGcTasksRequest.

        任务状态，Success：已完成，Stopped：已停止，Running：清理中，Pending：排队中，Error：失败。

        :return: The status of this ListGcTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListGcTasksRequest.

        任务状态，Success：已完成，Stopped：已停止，Running：清理中，Pending：排队中，Error：失败。

        :param status: The status of this ListGcTasksRequest.
        :type status: str
        """
        self._status = status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListGcTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

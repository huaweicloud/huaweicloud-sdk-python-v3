# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogicalClusterTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logical_cluster_tasks': 'list[LogicalClusterTaskInfo]',
        'count': 'int'
    }

    attribute_map = {
        'logical_cluster_tasks': 'logical_cluster_tasks',
        'count': 'count'
    }

    def __init__(self, logical_cluster_tasks=None, count=None):
        """ListLogicalClusterTasksResponse

        The model defined in huaweicloud sdk

        :param logical_cluster_tasks: 逻辑集群任务信息
        :type logical_cluster_tasks: list[:class:`huaweicloudsdkdws.v2.LogicalClusterTaskInfo`]
        :param count: 逻辑集群任务总数
        :type count: int
        """
        
        super(ListLogicalClusterTasksResponse, self).__init__()

        self._logical_cluster_tasks = None
        self._count = None
        self.discriminator = None

        if logical_cluster_tasks is not None:
            self.logical_cluster_tasks = logical_cluster_tasks
        if count is not None:
            self.count = count

    @property
    def logical_cluster_tasks(self):
        """Gets the logical_cluster_tasks of this ListLogicalClusterTasksResponse.

        逻辑集群任务信息

        :return: The logical_cluster_tasks of this ListLogicalClusterTasksResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.LogicalClusterTaskInfo`]
        """
        return self._logical_cluster_tasks

    @logical_cluster_tasks.setter
    def logical_cluster_tasks(self, logical_cluster_tasks):
        """Sets the logical_cluster_tasks of this ListLogicalClusterTasksResponse.

        逻辑集群任务信息

        :param logical_cluster_tasks: The logical_cluster_tasks of this ListLogicalClusterTasksResponse.
        :type logical_cluster_tasks: list[:class:`huaweicloudsdkdws.v2.LogicalClusterTaskInfo`]
        """
        self._logical_cluster_tasks = logical_cluster_tasks

    @property
    def count(self):
        """Gets the count of this ListLogicalClusterTasksResponse.

        逻辑集群任务总数

        :return: The count of this ListLogicalClusterTasksResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListLogicalClusterTasksResponse.

        逻辑集群任务总数

        :param count: The count of this ListLogicalClusterTasksResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListLogicalClusterTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

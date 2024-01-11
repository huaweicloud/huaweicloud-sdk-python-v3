# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadQueueInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workload_queue_name': 'str',
        'logical_cluster_name': 'str',
        'resource_item_list': 'list[WorkloadResourceItem]'
    }

    attribute_map = {
        'workload_queue_name': 'workload_queue_name',
        'logical_cluster_name': 'logical_cluster_name',
        'resource_item_list': 'resource_item_list'
    }

    def __init__(self, workload_queue_name=None, logical_cluster_name=None, resource_item_list=None):
        """WorkloadQueueInfo

        The model defined in huaweicloud sdk

        :param workload_queue_name: 资源池名称。
        :type workload_queue_name: str
        :param logical_cluster_name: 逻辑集群名称。
        :type logical_cluster_name: str
        :param resource_item_list: 资源配置队列。
        :type resource_item_list: list[:class:`huaweicloudsdkdws.v2.WorkloadResourceItem`]
        """
        
        

        self._workload_queue_name = None
        self._logical_cluster_name = None
        self._resource_item_list = None
        self.discriminator = None

        self.workload_queue_name = workload_queue_name
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        self.resource_item_list = resource_item_list

    @property
    def workload_queue_name(self):
        """Gets the workload_queue_name of this WorkloadQueueInfo.

        资源池名称。

        :return: The workload_queue_name of this WorkloadQueueInfo.
        :rtype: str
        """
        return self._workload_queue_name

    @workload_queue_name.setter
    def workload_queue_name(self, workload_queue_name):
        """Sets the workload_queue_name of this WorkloadQueueInfo.

        资源池名称。

        :param workload_queue_name: The workload_queue_name of this WorkloadQueueInfo.
        :type workload_queue_name: str
        """
        self._workload_queue_name = workload_queue_name

    @property
    def logical_cluster_name(self):
        """Gets the logical_cluster_name of this WorkloadQueueInfo.

        逻辑集群名称。

        :return: The logical_cluster_name of this WorkloadQueueInfo.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        """Sets the logical_cluster_name of this WorkloadQueueInfo.

        逻辑集群名称。

        :param logical_cluster_name: The logical_cluster_name of this WorkloadQueueInfo.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def resource_item_list(self):
        """Gets the resource_item_list of this WorkloadQueueInfo.

        资源配置队列。

        :return: The resource_item_list of this WorkloadQueueInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.WorkloadResourceItem`]
        """
        return self._resource_item_list

    @resource_item_list.setter
    def resource_item_list(self, resource_item_list):
        """Sets the resource_item_list of this WorkloadQueueInfo.

        资源配置队列。

        :param resource_item_list: The resource_item_list of this WorkloadQueueInfo.
        :type resource_item_list: list[:class:`huaweicloudsdkdws.v2.WorkloadResourceItem`]
        """
        self._resource_item_list = resource_item_list

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
        if not isinstance(other, WorkloadQueueInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

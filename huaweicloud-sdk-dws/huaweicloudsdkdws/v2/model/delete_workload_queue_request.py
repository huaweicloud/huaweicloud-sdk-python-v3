# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteWorkloadQueueRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'logical_cluster_name': 'str',
        'workload_queue_name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'logical_cluster_name': 'logical_cluster_name',
        'workload_queue_name': 'workload_queue_name'
    }

    def __init__(self, cluster_id=None, logical_cluster_name=None, workload_queue_name=None):
        """DeleteWorkloadQueueRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param logical_cluster_name: 逻辑集群名称。逻辑集群模式下该字段必填。
        :type logical_cluster_name: str
        :param workload_queue_name: 工作负载队列名称。
        :type workload_queue_name: str
        """
        
        

        self._cluster_id = None
        self._logical_cluster_name = None
        self._workload_queue_name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        self.workload_queue_name = workload_queue_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DeleteWorkloadQueueRequest.

        集群ID。

        :return: The cluster_id of this DeleteWorkloadQueueRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DeleteWorkloadQueueRequest.

        集群ID。

        :param cluster_id: The cluster_id of this DeleteWorkloadQueueRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def logical_cluster_name(self):
        """Gets the logical_cluster_name of this DeleteWorkloadQueueRequest.

        逻辑集群名称。逻辑集群模式下该字段必填。

        :return: The logical_cluster_name of this DeleteWorkloadQueueRequest.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        """Sets the logical_cluster_name of this DeleteWorkloadQueueRequest.

        逻辑集群名称。逻辑集群模式下该字段必填。

        :param logical_cluster_name: The logical_cluster_name of this DeleteWorkloadQueueRequest.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def workload_queue_name(self):
        """Gets the workload_queue_name of this DeleteWorkloadQueueRequest.

        工作负载队列名称。

        :return: The workload_queue_name of this DeleteWorkloadQueueRequest.
        :rtype: str
        """
        return self._workload_queue_name

    @workload_queue_name.setter
    def workload_queue_name(self, workload_queue_name):
        """Sets the workload_queue_name of this DeleteWorkloadQueueRequest.

        工作负载队列名称。

        :param workload_queue_name: The workload_queue_name of this DeleteWorkloadQueueRequest.
        :type workload_queue_name: str
        """
        self._workload_queue_name = workload_queue_name

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
        if not isinstance(other, DeleteWorkloadQueueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutopilotUpgradeClusterTaskRequest:

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
        'task_id': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'task_id': 'task_id'
    }

    def __init__(self, cluster_id=None, task_id=None):
        r"""ShowAutopilotUpgradeClusterTaskRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param task_id: 升级任务ID，调用集群升级API后从响应体中uid字段获取。
        :type task_id: str
        """
        
        

        self._cluster_id = None
        self._task_id = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.task_id = task_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowAutopilotUpgradeClusterTaskRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this ShowAutopilotUpgradeClusterTaskRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowAutopilotUpgradeClusterTaskRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this ShowAutopilotUpgradeClusterTaskRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowAutopilotUpgradeClusterTaskRequest.

        升级任务ID，调用集群升级API后从响应体中uid字段获取。

        :return: The task_id of this ShowAutopilotUpgradeClusterTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowAutopilotUpgradeClusterTaskRequest.

        升级任务ID，调用集群升级API后从响应体中uid字段获取。

        :param task_id: The task_id of this ShowAutopilotUpgradeClusterTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, ShowAutopilotUpgradeClusterTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

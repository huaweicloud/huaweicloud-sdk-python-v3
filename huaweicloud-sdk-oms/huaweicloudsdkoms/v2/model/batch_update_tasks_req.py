# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateTasksReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'ids': 'list[int]',
        'bandwidth_policy': 'list[BandwidthPolicyDto]',
        'task_priority': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'ids': 'ids',
        'bandwidth_policy': 'bandwidth_policy',
        'task_priority': 'task_priority'
    }

    def __init__(self, group_id=None, ids=None, bandwidth_policy=None, task_priority=None):
        r"""BatchUpdateTasksReq

        The model defined in huaweicloud sdk

        :param group_id: 迁移任务组ID，表示批量更新该任务组下所有任务。 group_id和ids为二选一参数，不可同时存在或同时缺失。
        :type group_id: str
        :param ids: 迁移任务id数组，包含所有需要批量更新操作的任务id。 group_id和ids为二选一参数，不可同时存在或同时缺失。
        :type ids: list[int]
        :param bandwidth_policy: 配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。
        :type bandwidth_policy: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        :param task_priority: 任务优先级配置，存在高中低三个优先级档次，限制仅在等待中、已暂停、已失败的任务进行修改 HIGH：高优先级 MEDIUM：中优先级 LOW：低优先级
        :type task_priority: str
        """
        
        

        self._group_id = None
        self._ids = None
        self._bandwidth_policy = None
        self._task_priority = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if ids is not None:
            self.ids = ids
        self.bandwidth_policy = bandwidth_policy
        if task_priority is not None:
            self.task_priority = task_priority

    @property
    def group_id(self):
        r"""Gets the group_id of this BatchUpdateTasksReq.

        迁移任务组ID，表示批量更新该任务组下所有任务。 group_id和ids为二选一参数，不可同时存在或同时缺失。

        :return: The group_id of this BatchUpdateTasksReq.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this BatchUpdateTasksReq.

        迁移任务组ID，表示批量更新该任务组下所有任务。 group_id和ids为二选一参数，不可同时存在或同时缺失。

        :param group_id: The group_id of this BatchUpdateTasksReq.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def ids(self):
        r"""Gets the ids of this BatchUpdateTasksReq.

        迁移任务id数组，包含所有需要批量更新操作的任务id。 group_id和ids为二选一参数，不可同时存在或同时缺失。

        :return: The ids of this BatchUpdateTasksReq.
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this BatchUpdateTasksReq.

        迁移任务id数组，包含所有需要批量更新操作的任务id。 group_id和ids为二选一参数，不可同时存在或同时缺失。

        :param ids: The ids of this BatchUpdateTasksReq.
        :type ids: list[int]
        """
        self._ids = ids

    @property
    def bandwidth_policy(self):
        r"""Gets the bandwidth_policy of this BatchUpdateTasksReq.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :return: The bandwidth_policy of this BatchUpdateTasksReq.
        :rtype: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        """
        return self._bandwidth_policy

    @bandwidth_policy.setter
    def bandwidth_policy(self, bandwidth_policy):
        r"""Sets the bandwidth_policy of this BatchUpdateTasksReq.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :param bandwidth_policy: The bandwidth_policy of this BatchUpdateTasksReq.
        :type bandwidth_policy: list[:class:`huaweicloudsdkoms.v2.BandwidthPolicyDto`]
        """
        self._bandwidth_policy = bandwidth_policy

    @property
    def task_priority(self):
        r"""Gets the task_priority of this BatchUpdateTasksReq.

        任务优先级配置，存在高中低三个优先级档次，限制仅在等待中、已暂停、已失败的任务进行修改 HIGH：高优先级 MEDIUM：中优先级 LOW：低优先级

        :return: The task_priority of this BatchUpdateTasksReq.
        :rtype: str
        """
        return self._task_priority

    @task_priority.setter
    def task_priority(self, task_priority):
        r"""Sets the task_priority of this BatchUpdateTasksReq.

        任务优先级配置，存在高中低三个优先级档次，限制仅在等待中、已暂停、已失败的任务进行修改 HIGH：高优先级 MEDIUM：中优先级 LOW：低优先级

        :param task_priority: The task_priority of this BatchUpdateTasksReq.
        :type task_priority: str
        """
        self._task_priority = task_priority

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
        if not isinstance(other, BatchUpdateTasksReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkRestoreStrategy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_type': 'str',
        'allow_non_restored_state': 'bool',
        'job_start_time_in_ms': 'int',
        'savepoint_id': 'str'
    }

    attribute_map = {
        'restore_type': 'restore_type',
        'allow_non_restored_state': 'allow_non_restored_state',
        'job_start_time_in_ms': 'job_start_time_in_ms',
        'savepoint_id': 'savepoint_id'
    }

    def __init__(self, restore_type=None, allow_non_restored_state=None, job_start_time_in_ms=None, savepoint_id=None):
        """FlinkRestoreStrategy

        The model defined in huaweicloud sdk

        :param restore_type: 启动位点类型。 NONE：无状态启动。 LATEST_SAVEPOINT：最新的作业快照启动。 FROM_SAVEPOINT：从指定快照启动。 LATEST_STATE：最新状态启动。
        :type restore_type: str
        :param allow_non_restored_state: 允许忽略部分算子状态。仅当作业选择有状态恢复时需要设置。
        :type allow_non_restored_state: bool
        :param job_start_time_in_ms: 无状态启动时间，需输入 13 位时间戳。当选择无状态启动时，可以设置本参数让所有支持 startTime 的源表均从该时刻开始读取数据。
        :type job_start_time_in_ms: int
        :param savepoint_id: 启动作业快照 ID，启动策略为 FROM_SAVEPOINT 时必填。
        :type savepoint_id: str
        """
        
        

        self._restore_type = None
        self._allow_non_restored_state = None
        self._job_start_time_in_ms = None
        self._savepoint_id = None
        self.discriminator = None

        if restore_type is not None:
            self.restore_type = restore_type
        if allow_non_restored_state is not None:
            self.allow_non_restored_state = allow_non_restored_state
        if job_start_time_in_ms is not None:
            self.job_start_time_in_ms = job_start_time_in_ms
        if savepoint_id is not None:
            self.savepoint_id = savepoint_id

    @property
    def restore_type(self):
        """Gets the restore_type of this FlinkRestoreStrategy.

        启动位点类型。 NONE：无状态启动。 LATEST_SAVEPOINT：最新的作业快照启动。 FROM_SAVEPOINT：从指定快照启动。 LATEST_STATE：最新状态启动。

        :return: The restore_type of this FlinkRestoreStrategy.
        :rtype: str
        """
        return self._restore_type

    @restore_type.setter
    def restore_type(self, restore_type):
        """Sets the restore_type of this FlinkRestoreStrategy.

        启动位点类型。 NONE：无状态启动。 LATEST_SAVEPOINT：最新的作业快照启动。 FROM_SAVEPOINT：从指定快照启动。 LATEST_STATE：最新状态启动。

        :param restore_type: The restore_type of this FlinkRestoreStrategy.
        :type restore_type: str
        """
        self._restore_type = restore_type

    @property
    def allow_non_restored_state(self):
        """Gets the allow_non_restored_state of this FlinkRestoreStrategy.

        允许忽略部分算子状态。仅当作业选择有状态恢复时需要设置。

        :return: The allow_non_restored_state of this FlinkRestoreStrategy.
        :rtype: bool
        """
        return self._allow_non_restored_state

    @allow_non_restored_state.setter
    def allow_non_restored_state(self, allow_non_restored_state):
        """Sets the allow_non_restored_state of this FlinkRestoreStrategy.

        允许忽略部分算子状态。仅当作业选择有状态恢复时需要设置。

        :param allow_non_restored_state: The allow_non_restored_state of this FlinkRestoreStrategy.
        :type allow_non_restored_state: bool
        """
        self._allow_non_restored_state = allow_non_restored_state

    @property
    def job_start_time_in_ms(self):
        """Gets the job_start_time_in_ms of this FlinkRestoreStrategy.

        无状态启动时间，需输入 13 位时间戳。当选择无状态启动时，可以设置本参数让所有支持 startTime 的源表均从该时刻开始读取数据。

        :return: The job_start_time_in_ms of this FlinkRestoreStrategy.
        :rtype: int
        """
        return self._job_start_time_in_ms

    @job_start_time_in_ms.setter
    def job_start_time_in_ms(self, job_start_time_in_ms):
        """Sets the job_start_time_in_ms of this FlinkRestoreStrategy.

        无状态启动时间，需输入 13 位时间戳。当选择无状态启动时，可以设置本参数让所有支持 startTime 的源表均从该时刻开始读取数据。

        :param job_start_time_in_ms: The job_start_time_in_ms of this FlinkRestoreStrategy.
        :type job_start_time_in_ms: int
        """
        self._job_start_time_in_ms = job_start_time_in_ms

    @property
    def savepoint_id(self):
        """Gets the savepoint_id of this FlinkRestoreStrategy.

        启动作业快照 ID，启动策略为 FROM_SAVEPOINT 时必填。

        :return: The savepoint_id of this FlinkRestoreStrategy.
        :rtype: str
        """
        return self._savepoint_id

    @savepoint_id.setter
    def savepoint_id(self, savepoint_id):
        """Sets the savepoint_id of this FlinkRestoreStrategy.

        启动作业快照 ID，启动策略为 FROM_SAVEPOINT 时必填。

        :param savepoint_id: The savepoint_id of this FlinkRestoreStrategy.
        :type savepoint_id: str
        """
        self._savepoint_id = savepoint_id

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
        if not isinstance(other, FlinkRestoreStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

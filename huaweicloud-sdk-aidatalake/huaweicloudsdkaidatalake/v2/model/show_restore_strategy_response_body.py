# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRestoreStrategyResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_type': 'FlinkJobRestoreType',
        'savepoint_id': 'str',
        'checkpoint_path': 'str',
        'allow_non_restored_state': 'bool',
        'job_start_time_in_ms': 'int'
    }

    attribute_map = {
        'restore_type': 'restore_type',
        'savepoint_id': 'savepoint_id',
        'checkpoint_path': 'checkpoint_path',
        'allow_non_restored_state': 'allow_non_restored_state',
        'job_start_time_in_ms': 'job_start_time_in_ms'
    }

    def __init__(self, restore_type=None, savepoint_id=None, checkpoint_path=None, allow_non_restored_state=None, job_start_time_in_ms=None):
        r"""ShowRestoreStrategyResponseBody

        The model defined in huaweicloud sdk

        :param restore_type: 
        :type restore_type: :class:`huaweicloudsdkaidatalake.v2.FlinkJobRestoreType`
        :param savepoint_id: **参数解释**：Savepoint的ID，唯一标识一个快照。当restore_type为FROM_SAVEPOINT_ID时返回。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type savepoint_id: str
        :param checkpoint_path: **参数解释**：Checkpoint的存储路径，指向_metadata文件的上一级目录。仅当restore_type为FROM_CHECKPOINT_PATH时返回。 **取值范围**：1~512个字符，需以obs://开头。 
        :type checkpoint_path: str
        :param allow_non_restored_state: **参数解释**：允许忽略部分算子状态。仅当restore_type为FROM_SAVEPOINT_ID或FROM_CHECKPOINT_PATH时返回。 **取值范围**：   - true：允许忽略部分算子状态。设为true时，如果快照中包含当前作业不再使用的算子状态，将跳过这些状态而非报错。   - false：不允许忽略算子状态。 
        :type allow_non_restored_state: bool
        :param job_start_time_in_ms: **参数解释**：源表的数据消费起始时间戳，用于指定作业启动后从源表的哪个时间点开始消费数据。仅当restore_type为FROM_SPECIFIED_TIMESTAMP时返回，且仅支持Kafka源表。 **取值范围**：0~4102416000000，13位毫秒时间戳。 
        :type job_start_time_in_ms: int
        """
        
        

        self._restore_type = None
        self._savepoint_id = None
        self._checkpoint_path = None
        self._allow_non_restored_state = None
        self._job_start_time_in_ms = None
        self.discriminator = None

        self.restore_type = restore_type
        if savepoint_id is not None:
            self.savepoint_id = savepoint_id
        if checkpoint_path is not None:
            self.checkpoint_path = checkpoint_path
        if allow_non_restored_state is not None:
            self.allow_non_restored_state = allow_non_restored_state
        if job_start_time_in_ms is not None:
            self.job_start_time_in_ms = job_start_time_in_ms

    @property
    def restore_type(self):
        r"""Gets the restore_type of this ShowRestoreStrategyResponseBody.

        :return: The restore_type of this ShowRestoreStrategyResponseBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobRestoreType`
        """
        return self._restore_type

    @restore_type.setter
    def restore_type(self, restore_type):
        r"""Sets the restore_type of this ShowRestoreStrategyResponseBody.

        :param restore_type: The restore_type of this ShowRestoreStrategyResponseBody.
        :type restore_type: :class:`huaweicloudsdkaidatalake.v2.FlinkJobRestoreType`
        """
        self._restore_type = restore_type

    @property
    def savepoint_id(self):
        r"""Gets the savepoint_id of this ShowRestoreStrategyResponseBody.

        **参数解释**：Savepoint的ID，唯一标识一个快照。当restore_type为FROM_SAVEPOINT_ID时返回。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The savepoint_id of this ShowRestoreStrategyResponseBody.
        :rtype: str
        """
        return self._savepoint_id

    @savepoint_id.setter
    def savepoint_id(self, savepoint_id):
        r"""Sets the savepoint_id of this ShowRestoreStrategyResponseBody.

        **参数解释**：Savepoint的ID，唯一标识一个快照。当restore_type为FROM_SAVEPOINT_ID时返回。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param savepoint_id: The savepoint_id of this ShowRestoreStrategyResponseBody.
        :type savepoint_id: str
        """
        self._savepoint_id = savepoint_id

    @property
    def checkpoint_path(self):
        r"""Gets the checkpoint_path of this ShowRestoreStrategyResponseBody.

        **参数解释**：Checkpoint的存储路径，指向_metadata文件的上一级目录。仅当restore_type为FROM_CHECKPOINT_PATH时返回。 **取值范围**：1~512个字符，需以obs://开头。 

        :return: The checkpoint_path of this ShowRestoreStrategyResponseBody.
        :rtype: str
        """
        return self._checkpoint_path

    @checkpoint_path.setter
    def checkpoint_path(self, checkpoint_path):
        r"""Sets the checkpoint_path of this ShowRestoreStrategyResponseBody.

        **参数解释**：Checkpoint的存储路径，指向_metadata文件的上一级目录。仅当restore_type为FROM_CHECKPOINT_PATH时返回。 **取值范围**：1~512个字符，需以obs://开头。 

        :param checkpoint_path: The checkpoint_path of this ShowRestoreStrategyResponseBody.
        :type checkpoint_path: str
        """
        self._checkpoint_path = checkpoint_path

    @property
    def allow_non_restored_state(self):
        r"""Gets the allow_non_restored_state of this ShowRestoreStrategyResponseBody.

        **参数解释**：允许忽略部分算子状态。仅当restore_type为FROM_SAVEPOINT_ID或FROM_CHECKPOINT_PATH时返回。 **取值范围**：   - true：允许忽略部分算子状态。设为true时，如果快照中包含当前作业不再使用的算子状态，将跳过这些状态而非报错。   - false：不允许忽略算子状态。 

        :return: The allow_non_restored_state of this ShowRestoreStrategyResponseBody.
        :rtype: bool
        """
        return self._allow_non_restored_state

    @allow_non_restored_state.setter
    def allow_non_restored_state(self, allow_non_restored_state):
        r"""Sets the allow_non_restored_state of this ShowRestoreStrategyResponseBody.

        **参数解释**：允许忽略部分算子状态。仅当restore_type为FROM_SAVEPOINT_ID或FROM_CHECKPOINT_PATH时返回。 **取值范围**：   - true：允许忽略部分算子状态。设为true时，如果快照中包含当前作业不再使用的算子状态，将跳过这些状态而非报错。   - false：不允许忽略算子状态。 

        :param allow_non_restored_state: The allow_non_restored_state of this ShowRestoreStrategyResponseBody.
        :type allow_non_restored_state: bool
        """
        self._allow_non_restored_state = allow_non_restored_state

    @property
    def job_start_time_in_ms(self):
        r"""Gets the job_start_time_in_ms of this ShowRestoreStrategyResponseBody.

        **参数解释**：源表的数据消费起始时间戳，用于指定作业启动后从源表的哪个时间点开始消费数据。仅当restore_type为FROM_SPECIFIED_TIMESTAMP时返回，且仅支持Kafka源表。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :return: The job_start_time_in_ms of this ShowRestoreStrategyResponseBody.
        :rtype: int
        """
        return self._job_start_time_in_ms

    @job_start_time_in_ms.setter
    def job_start_time_in_ms(self, job_start_time_in_ms):
        r"""Sets the job_start_time_in_ms of this ShowRestoreStrategyResponseBody.

        **参数解释**：源表的数据消费起始时间戳，用于指定作业启动后从源表的哪个时间点开始消费数据。仅当restore_type为FROM_SPECIFIED_TIMESTAMP时返回，且仅支持Kafka源表。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :param job_start_time_in_ms: The job_start_time_in_ms of this ShowRestoreStrategyResponseBody.
        :type job_start_time_in_ms: int
        """
        self._job_start_time_in_ms = job_start_time_in_ms

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
        if not isinstance(other, ShowRestoreStrategyResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
